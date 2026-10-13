#!/usr/bin/env python3
"""pdf2md: PDF -> Markdown an AI can read without losing anything, with proof.

    uv run --with pymupdf4llm python pdf2md.py convert book.pdf --out book-md
    python3 pdf2md.py audit book.pdf book-md          # poppler only, no packages
    python3 pdf2md.py selftest

convert writes index.md (chapter table, audit, pages to look at), chapter files with
`<!-- page N -->` anchors, assets/ (figures, page images) and report.json.

The converter (pymupdf4llm, AGPL, installed per run by uv; or --engine plain, which
needs only poppler) is allowed to be imperfect. What makes the result lossless is the
audit: every page is compared word by word with the PDF's own text layer
(`pdftotext`); lines the converter dropped are appended from that layer; pages with no
text layer are OCR'd with tesseract or flagged with a page image. Nothing is dropped
silently. Content that exists only as pixels (charts, scans, equations drawn as
graphics) is kept as an image and listed in index.md under "Look at these pages".
"""
import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

TOKEN = re.compile(r"[^\W_]+|[∀-⋿Ͱ-Ͽ±×÷°µ€£]")
ANCHOR = re.compile(r"<!-- page (\d+) -->")
TAGS = "br|mark|table|thead|tbody|tfoot|tr|th|td|code|pre|b|i|u|em|strong|a|img|span|div|p|h[1-6]|ul|ol|li|hr|details|summary|blockquote"
MIN_RECALL = 0.985
MATHY = re.compile(r"[=\u2200-\u22ff\u0370-\u03ff\u221a\u00b1\u00d7\u00f7]")


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace").stdout


def page_count(pdf):
    r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, errors="replace")
    m = re.search(r"Pages:\s+(\d+)", r.stdout)
    if not m:
        why = (r.stderr.strip().splitlines() or ["not a readable PDF"])[0]
        sys.exit(f"cannot read {pdf}: {why}" + ("  (remove the password first, e.g. qpdf --decrypt)" if "assword" in why else ""))
    return int(m.group(1))


def raw_page(pdf, p):
    return sh("pdftotext", "-f", str(p), "-l", str(p), "-enc", "UTF-8", str(pdf), "-")


def tokens(text):
    t = unicodedata.normalize("NFKC", text).replace("­", "")
    t = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)  # a hyphen at a line break is not a word break
    return Counter(m.group().casefold() for m in TOKEN.finditer(t))


def md_plain(md):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"</?(?:sup|sub)>", "", md)  # 10<sup>19</sup> is the number 1019
    md = re.sub(r"</?(?:%s)(?:\s[^<>]*)?/?>" % TAGS, " ", md)  # real tags only: "k < n" and "<pad>" are text
    md = html.unescape(md).replace("\\", "")
    return re.sub(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", "", md)  # italic markers; keeps snake_case


def recall(ref, md):
    r, m = tokens(ref), tokens(md_plain(md))
    n = sum(r.values())
    return (sum((r & m).values()) / n if n else 1.0), n


def lost_lines(ref, md):
    """Lines of the PDF text layer whose words the Markdown does not contain."""
    pool, lost = tokens(md_plain(md)), []
    for line in re.sub(r"(\w)-\n(\w)", r"\1\2", ref).splitlines():  # rejoin words hyphenated at a line break
        ws = list(tokens(line).elements())
        if not ws:
            continue
        have = [w for w in ws if pool[w] > 0]
        for w in have:
            pool[w] -= 1
        miss = len(ws) - len(have)
        if miss:
            lost.append(line.strip())
    return lost


def ink(pdf, p, tmp):
    """Fraction of dark pixels on the page at low resolution: tells blank from scanned."""
    base = tmp / f"ink{p}"
    subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "30", "-gray", str(pdf), str(base)], capture_output=True)
    for f in tmp.glob(f"ink{p}-*.pgm"):
        data = f.read_bytes()
        f.unlink()
        body = data.split(b"\n", 3)[3] if data[:2] == b"P5" else b""
        return sum(1 for b in body if b < 200) / max(len(body), 1)
    return 0.0


def is_scan(pdf, p):
    """True when one image covers most of the page: a scan has pixels where text should be."""
    size = re.search(r"size:\s+([\d.]+) x ([\d.]+)", sh("pdfinfo", "-f", str(p), "-l", str(p), str(pdf)))
    if not size:
        return False
    page_area = float(size.group(1)) * float(size.group(2))
    for row in sh("pdfimages", "-list", "-f", str(p), "-l", str(p), str(pdf)).splitlines()[2:]:
        c = row.split()
        try:
            w, h, xppi, yppi = int(c[3]), int(c[4]), float(c[12]), float(c[13])
        except (IndexError, ValueError):
            continue
        if xppi and yppi and (w / xppi * 72) * (h / yppi * 72) >= 0.7 * page_area:
            return True
    return False


def render(pdf, p, dest, tmp, dpi=110):
    subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi), "-png", str(pdf), str(tmp / "pg")], capture_output=True)
    for f in tmp.glob("pg-*.png"):
        shutil.move(str(f), dest)
        return True
    return False


def ocr(png, lang):
    out = sh("tesseract", str(png), "stdout", "-l", lang, "tsv")
    words, confs = [], []
    for row in out.splitlines()[1:]:
        c = row.split("\t")
        if len(c) == 12 and c[11].strip() and float(c[10]) >= 0:
            words.append((c[2], c[3], c[4], c[11]))
            confs.append(float(c[10]))
    lines, cur, key = [], [], None
    for blk, par, ln, w in words:
        if (blk, par, ln) != key and cur:
            lines.append(" ".join(cur))
            cur = []
        key = (blk, par, ln)
        cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    return "\n".join(lines), (sum(confs) / len(confs) if confs else 0.0)


def engine_pymupdf(pdf, assets, tables, lang, use_ocr):
    try:
        import pymupdf
        import pymupdf4llm
    except ImportError:
        sys.exit("pymupdf4llm is not installed. Run through uv:  uv run --with pymupdf4llm python pdf2md.py ...   (or use --engine plain)")
    doc = pymupdf.open(str(pdf))
    chunks = pymupdf4llm.to_markdown(doc, page_chunks=True, write_images=True, image_path=str(assets),
                                     image_format="png", dpi=150, table_output=tables, show_progress=False,
                                     use_ocr=use_ocr, ocr_language=lang)
    toc = [(lvl, title, pg) for lvl, title, pg in doc.get_toc(simple=True) if pg >= 1]
    pre = str(assets) + "/"
    return [tidy(c["text"].replace(pre, "assets/")) for c in chunks], toc, doc.metadata or {}


def tidy(md):
    """Headings come out as '## **5 Training**'; the bold adds tokens and no meaning."""
    md = re.sub(r"^(#{1,6}) \*\*(.+?)\*\*\s*$", r"\1 \2", md, flags=re.M)
    md = re.sub(r"_([.\u00b7,:;])_", r"\1", md)  # '1_._0_·_10' is the number 1.0·10 with italic noise
    return re.sub(r"</?mark>", "", md)  # highlight tags are noise


def engine_plain(pdf, n):
    pages = []
    for p in range(1, n + 1):
        txt = re.sub(r"(?<=[^\n])\n(?=[^\n])", " ", raw_page(pdf, p))
        pages.append(re.sub(r"\n{3,}", "\n\n", txt).strip())
    return pages, [], {}


def sparse_table(md):
    """A Markdown table with many empty cells is usually a merged-cell table the converter split."""
    cells = [c.strip() for row in re.findall(r"^\|.*\|\s*$", md, flags=re.M) if not re.fullmatch(r"[|\s:-]+", row)
             for c in row.strip().strip("|").split("|")]
    return len(cells) >= 6 and sum(not c for c in cells) / len(cells) > 0.25


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48] or "section"


def chapters(toc, n, split, pages=()):
    """[(title, first_page, last_page)]: the PDF outline, else top-level headings, else 25-page chunks, else one."""
    if split != "none":
        for lvl in sorted({t[0] for t in toc}):
            at = sorted({(pg, t) for l, t, pg in toc if l == lvl})
            starts = {}
            for pg, t in at:
                starts.setdefault(pg, t)
            if len(starts) >= 2:
                pgs = sorted(starts)
                out = [(starts[pg], pg, (pgs[i + 1] - 1 if i + 1 < len(pgs) else n)) for i, pg in enumerate(pgs)]
                if pgs[0] > 1:
                    out.insert(0, ("Front matter", 1, pgs[0] - 1))
                return out
        for lvl in (1, 2, 3):
            starts = {}
            for p, md in enumerate(pages, 1):
                m = re.search(r"^#{%d} (.+?)\s*$" % lvl, md, flags=re.M)
                if m:
                    starts[p] = m.group(1)
            if 3 <= len(starts) <= max(n // 2, 3):
                pgs = sorted(starts)
                out = [(starts[pg], pg, (pgs[i + 1] - 1 if i + 1 < len(pgs) else n)) for i, pg in enumerate(pgs)]
                return ([("Front matter", 1, pgs[0] - 1)] if pgs[0] > 1 else []) + out
        if n > 60:
            return [(f"Pages {a}-{min(a + 24, n)}", a, min(a + 24, n)) for a in range(1, n + 1, 25)]
    return [("Full text", 1, n)]


def convert(pdf, out, engine, tables, lang, ocr_mode, split, force=False):
    pdf, out = Path(pdf), Path(out)
    n = page_count(pdf)
    if out.exists() and any(out.iterdir()):
        if not force:
            sys.exit(f"{out} is not empty; pass --force to replace the .md files, assets/ and report.json pdf2md wrote there")
        for f in out.glob("*.md"):
            f.unlink()
        shutil.rmtree(out / "assets", ignore_errors=True)
        (out / "report.json").unlink(missing_ok=True)
    assets, tmp = out / "assets", out / ".tmp"
    can_ocr = ocr_mode != "off" and shutil.which("tesseract")
    if can_ocr and lang not in sh("tesseract", "--list-langs").split():
        sys.exit(f"tesseract has no '{lang}' data. Installed: {' '.join(sh('tesseract', '--list-langs').splitlines()[1:])}. "
                 f"Install it (Arch: sudo pacman -S tesseract-data-{lang}) or pass --lang / --ocr off.")
    assets.mkdir(parents=True, exist_ok=True)
    tmp.mkdir(exist_ok=True)
    pages, toc, meta = engine_plain(pdf, n) if engine == "plain" else engine_pymupdf(pdf, assets, tables, lang, ocr_mode != "off")
    report, notes = [], {}

    def flag(p, why, png):
        notes.setdefault(p, (png.name, []))[1].append(why)

    for p in range(1, n + 1):
        md, ref = (pages[p - 1] if p <= len(pages) else ""), raw_page(pdf, p)
        rec, words = recall(ref, md)
        row = {"page": p, "words": words, "recall": round(rec, 4), "recovered": 0, "flags": []}
        if words < 3 and ink(pdf, p, tmp) > 0.01:
            png = assets / f"page-{p:03d}.png"
            if is_scan(pdf, p):
                row["flags"].append("no text layer")
                render(pdf, p, png, tmp, dpi=200)
                md = f"![page {p}](assets/page-{p:03d}.png)"
                why = "scanned page, no OCR available"
                if can_ocr:
                    text, conf = ocr(png, lang)
                    md = f"<!-- OCR: tesseract {lang}, mean confidence {conf:.0f}% -->\n{text}\n\n" + md
                    row["flags"].append(f"OCR {conf:.0f}%")
                    why = f"scanned page, OCR {conf:.0f}% confidence (unverifiable)"
                flag(p, why, png)
            elif render(pdf, p, png, tmp):
                flag(p, "mostly graphics: the text layer has almost no words", png)
        else:
            lost = lost_lines(ref, md) if rec < 1 else []  # any missing word is recovered, however small the gap
            if sparse_table(md) and tables == "markdown":
                row["flags"].append("sparse table")
                png = assets / f"page-{p:03d}.png"
                if render(pdf, p, png, tmp):
                    flag(p, "table with many empty cells (merged cells?); try --tables html", png)
            if lost:
                md += "\n\n<!-- recovered: lines the converter dropped, taken from the PDF text layer -->\n" + "\n".join("> " + html.escape(l, quote=False) for l in lost)
                row["recovered"] = len(lost)
            mathy = any(MATHY.search(l) for l in lost)
            if rec < 0.95 or mathy:
                png = assets / f"page-{p:03d}.png"
                if render(pdf, p, png, tmp):
                    flag(p, f"recall {rec:.1%}; {len(lost)} line(s) recovered" + (", equations or symbols" if mathy else ""), png)
        pages_i = pages if p <= len(pages) else pages + [""] * (p - len(pages))
        pages_i[p - 1] = md
        pages = pages_i
        row["final"] = round(recall(ref, md)[0], 4)
        report.append(row)
    shutil.rmtree(tmp, ignore_errors=True)
    look = [(p, "; ".join(w), img) for p, (img, w) in sorted(notes.items())]
    secs, files = chapters(toc, n, split, pages), []
    for i, (title, a, b) in enumerate(secs, 1):
        name = "full.md" if len(secs) == 1 else f"{i:02d}-{slug(title)}.md"
        body = "\n\n".join(f"<!-- page {p} -->\n{pages[p - 1].strip()}" for p in range(a, b + 1))
        (out / name).write_text(body + "\n", encoding="utf-8")
        w = sum(r["words"] for r in report[a - 1:b])
        files.append((name, title, a, b, w, len(body) // 4))
    write_index(out, pdf, n, meta, files, report, look, engine)
    (out / "report.json").write_text(json.dumps({"pages": report, "files": [f[0] for f in files]}, indent=1), encoding="utf-8")
    return report, files, look


def write_index(out, pdf, n, meta, files, report, look, engine):
    sha = hashlib.sha256(Path(pdf).read_bytes()).hexdigest()[:16]
    worst = min(report, key=lambda r: r["recall"] if r["words"] >= 3 else 1)
    rec_pages = sum(1 for r in report if r["recovered"])
    L = [f"# {meta.get('title') or Path(pdf).stem}", "",
         f"Converted from `{Path(pdf).name}` (sha256 {sha}), {n} pages, engine `{engine}`. "
         "Every page is checked word by word against the PDF's text layer; see Audit.", "",
         "## Files", "", "| File | Section | Pages | Words | ~Tokens |", "|---|---|---|---|---|"]
    L += [f"| [{f}]({f}) | {t} | {a}-{b} | {w} | {tk} |" for f, t, a, b, w, tk in files]
    L += ["", "## Audit", "",
          f"- Converter alone kept {sum(r['recall'] * r['words'] for r in report) / max(sum(r['words'] for r in report), 1):.2%} "
          f"of the {sum(r['words'] for r in report)} words in the PDF's text layer (lowest page {worst['page']} at {worst['recall']:.1%}).",
          f"- After recovery: {sum(r['final'] * r['words'] for r in report) / max(sum(r['words'] for r in report), 1):.2%}. "
          f"{sum(r['recovered'] for r in report)} dropped line(s) on {rec_pages} page(s) were appended from the text layer, "
          "each under a `recovered` comment.",
          "- Page anchors: `<!-- page N -->`. Figures and graphics are PNGs in `assets/`."]
    if look:
        L += ["", "## Look at these pages", "", "Content here may exist only as pixels (scans, graphics, equations). "
              "A reader with vision should open the page image.", "", "| Page | Why | Image |", "|---|---|---|"]
        L += [f"| {p} | {why} | [{img}](assets/{img}) |" for p, why, img in look]
    (out / "index.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def audit(pdf, target, min_recall):
    target = Path(target)
    files = sorted(target.glob("*.md")) if target.is_dir() else [target]
    pages = {}
    for f in files:
        if f.name == "index.md":
            continue
        parts = ANCHOR.split(f.read_text(encoding="utf-8"))
        for i in range(1, len(parts) - 1, 2):
            pages[int(parts[i])] = pages.get(int(parts[i]), "") + parts[i + 1]
    bad, tot_ref, tot_hit = [], 0, 0
    for p in range(1, page_count(pdf) + 1):
        r, w = recall(raw_page(pdf, p), pages.get(p, ""))
        tot_ref += w
        tot_hit += r * w
        if w >= 3 and r < min_recall:
            bad.append((p, r, w))
    print(f"{len(pages)} anchored pages; word recall {tot_hit / max(tot_ref, 1):.2%} over {tot_ref} words")
    for p, r, w in bad:
        print(f"  page {p}: {r:.1%} of {w} words")
    print("PASS" if not bad else f"FAIL: {len(bad)} page(s) below {min_recall:.1%}")
    return not bad


def selftest():
    a = tokens("Hello, world! exam-\nple 3 ≤ 4 Ünï")
    assert a["example"] == 1 and a["hello"] == 1 and a["≤"] == 1 and a["ünï"] == 1, a
    r, n = recall("alpha beta gamma\ndelta", "<!-- page 1 -->\n**alpha** beta ![x](a.png) gamma\n| delta |")
    assert (r, n) == (1.0, 4), (r, n)
    r, _ = recall("alpha beta gamma delta", "alpha beta")
    assert r == 0.5
    assert lost_lines("alpha beta\ngamma delta epsilon\nzeta", "alpha beta zeta gamma") == ["gamma delta epsilon"]
    assert tokens("a <pad> b")["pad"] == 1 and "pad" in tokens(md_plain("a &lt;pad&gt; b"))
    assert tokens(md_plain("10<sup>19</sup>"))["1019"] == 1 and "td" not in tokens(md_plain("<td>x</td>"))
    assert lost_lines("alpha beta gamma delta epsilon zeta", "alpha beta gamma delta epsilon") == ["alpha beta gamma delta epsilon zeta"]
    assert tokens(md_plain("_d_<sub>_model_</sub> and snake_case"))["dmodel"] == 1 and tokens(md_plain("snake_case"))["snake"] == 1
    assert lost_lines("one solu-\ntion two\nthree", "one two three") == ["one solution two"]
    assert slug("Chapter 1: Naïve  Bayes!") == "chapter-1-naive-bayes"
    assert recall("a k < n b then c d > e", "a k < n b then c d > e <sup>2</sup>")[0] == 1.0  # "<" is text, not a tag
    assert "k < n" in md_plain("width k < n and <sup>2</sup>") and "sup" not in md_plain("x <sup>2</sup>")
    assert tidy("## **5 Training**\n**bold** text") == "## 5 Training\n**bold** text"
    toc = [(1, "Intro", 3), (1, "Body", 9), (2, "Sub", 10)]
    assert chapters(toc, 20, "auto") == [("Front matter", 1, 2), ("Intro", 3, 8), ("Body", 9, 20)]
    assert chapters([], 5, "auto") == [("Full text", 1, 5)]
    heads = ["# A\n"] + [""] * 3 + ["# B\n"] + [""] * 2 + ["# C\n"] + [""] * 3
    assert chapters([], 10, "auto", heads) == [("A", 1, 4), ("B", 5, 7), ("C", 8, 10)]
    assert chapters([], 100, "auto", [""] * 100)[:2] == [("Pages 1-25", 1, 25), ("Pages 26-50", 26, 50)]
    assert chapters([], 100, "none", [""] * 100) == [("Full text", 1, 100)]
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("convert")
    c.add_argument("pdf")
    c.add_argument("--out", required=True)
    c.add_argument("--engine", choices=["pymupdf4llm", "plain"], default="pymupdf4llm")
    c.add_argument("--tables", choices=["markdown", "html"], default="markdown", help="html keeps merged cells")
    c.add_argument("--lang", default="eng", help="tesseract language for scanned pages")
    c.add_argument("--ocr", choices=["auto", "off"], default="auto")
    c.add_argument("--split", choices=["auto", "none"], default="auto", help="one file per outline chapter")
    c.add_argument("--force", action="store_true", help="replace a previous conversion in --out")
    a = sub.add_parser("audit")
    a.add_argument("pdf")
    a.add_argument("target", help="a .md file or the folder convert wrote")
    a.add_argument("--min-recall", type=float, default=MIN_RECALL)
    sub.add_parser("selftest")
    x = ap.parse_args()
    if x.cmd == "selftest":
        return selftest()
    if x.cmd == "audit":
        sys.exit(0 if audit(x.pdf, x.target, x.min_recall) else 1)
    report, files, look = convert(x.pdf, x.out, x.engine, x.tables, x.lang, x.ocr, x.split, x.force)
    print(f"wrote {len(files)} file(s) to {x.out}; {len(look)} page(s) to look at; index.md has the audit")


if __name__ == "__main__":
    main()
