#!/usr/bin/env python3
"""search / map / crawl on top of Scrapling: the parts of Firecrawl Scrapling's MCP lacks.

Run with the Python that has Scrapling installed:
    $(uv tool dir)/scrapling/bin/python web.py search "query" [-n 10] [--stealth]
    $(uv tool dir)/scrapling/bin/python web.py map https://site [-n 500] [--stealth]
    $(uv tool dir)/scrapling/bin/python web.py crawl https://site [-n 20] [--out DIR] [--css SEL] [--stealth]
    $(uv tool dir)/scrapling/bin/python web.py selftest

Every command prints JSON lines on stdout. crawl writes each page as Markdown under --out
and prints only url/title/file/chars, so a crawl never floods the context.
"""
import argparse
import base64
import json
import logging
import re
import sys
import unicodedata
from urllib.parse import parse_qs, quote_plus, urlparse

from scrapling.fetchers import AsyncStealthySession, Fetcher, StealthyFetcher
from scrapling.spiders.links import LinkExtractor
from scrapling.spiders.templates.crawler import CrawlRule
from scrapling.spiders.templates.site_to_markdown import SiteToMarkdownSpider
from scrapling.spiders.templates.sitemap import SitemapSpider

logging.getLogger("scrapling").setLevel(logging.ERROR)


def emit(obj):
    print(json.dumps(obj, ensure_ascii=False), flush=True)


# --- search -------------------------------------------------------------------------------------
# DuckDuckGo Lite first, Bing second; each tried as a plain request, then once in a real browser.
# ponytail: two HTML engines, no API keys. Add an engine here when both start refusing this IP.

def text(el):
    return " ".join(el.get_all_text(separator=" ", strip=True).split())


def unwrap(href):
    """Undo the click-tracking redirects: DDG's /l/?uddg=<url> and Bing's /ck/a?u=a1<base64url>."""
    q = parse_qs(urlparse(href).query)
    if "uddg" in q:
        return q["uddg"][0]
    if "/ck/a" in href and q.get("u", [""])[0].startswith("a1"):
        b64 = q["u"][0][2:]
        return base64.urlsafe_b64decode(b64 + "=" * (-len(b64) % 4)).decode(errors="replace")
    return href


def parse_ddg_lite(page):
    links = [a for a in page.css("a.result-link") if "/y.js" not in (a.attrib.get("href") or "")]  # y.js = ad
    snippets = page.css("td.result-snippet")
    return [{"title": text(a), "url": unwrap(a.attrib.get("href", "")),
             "snippet": text(snippets[i]) if i < len(snippets) else ""} for i, a in enumerate(links)]


def parse_bing(page):
    out = []
    for li in page.css("li.b_algo"):
        a = li.css("h2 a")
        if a:
            p = li.css(".b_caption p") or li.css("p")
            out.append({"title": text(a[0]), "url": unwrap(a[0].attrib.get("href", "")),
                        "snippet": text(p[0]) if p else ""})
    return out


def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def on_topic(results, query):
    """Bing serves decoy pages to scrapers (asked for pacman hooks, it answered with a tram in Rio), so a
    result set only counts if most of it mentions a query word. ponytail: word overlap, not semantics."""
    words = {w for w in re.findall(r"\w+", fold(query)) if len(w) > 2}
    hit = [r for r in results if any(w in fold(r["title"] + " " + r["snippet"] + " " + r["url"]) for w in words)]
    return hit if words and len(hit) * 2 >= len(results) else []


ENGINES = [
    ("https://lite.duckduckgo.com/lite/?q={}", parse_ddg_lite),
    ("https://www.bing.com/search?q={}&setlang=en", parse_bing),
]


def search(query, n, stealth):
    for url, parse in ENGINES:
        for browser in ([True] if stealth else [False, True]):
            page = (StealthyFetcher.fetch(url.format(quote_plus(query)), headless=True) if browser
                    else Fetcher.get(url.format(quote_plus(query))))
            results = on_topic([r for r in parse(page) if r["url"].startswith("http")], query)[:n]
            if results:
                for r in results:
                    emit(r)
                return
    sys.exit("no results: every engine refused or returned an empty page")


# --- map ----------------------------------------------------------------------------------------

def stealth_sessions(spider, manager, stealth):
    if stealth:
        manager.add("default", AsyncStealthySession(headless=True))
    else:
        super(type(spider), spider).configure_sessions(manager)


def site_map(url, limit, stealth):
    root = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
    found = []

    class Map(SitemapSpider):
        name = "map"
        sitemap_urls = [root + "/robots.txt", root + "/sitemap.xml"]
        logging_level = logging.ERROR

        def configure_sessions(self, manager):
            stealth_sessions(self, manager, stealth)

        def _dispatch(self, response, url, rules):  # record, never fetch: a map lists, it doesn't read
            if url not in found and len(found) < limit:
                found.append(url)
            return None

    Map().start()
    source = "sitemap"
    if not found:  # no sitemap: discover by following links instead
        source = "links"
        found = [p["url"] for p in crawl_pages(url, limit, stealth, out=None, css=None)]
    for u in found:
        emit({"url": u, "source": source})


# --- crawl --------------------------------------------------------------------------------------

def crawl_pages(url, limit, stealth, out, css):
    host = urlparse(url).netloc

    class Crawl(SiteToMarkdownSpider):
        name = "crawl"
        start_urls = [url]
        allowed_domains = {host}
        max_pages = limit
        output_dir = out
        css_selector = css
        logging_level = logging.ERROR

        def configure_sessions(self, manager):
            stealth_sessions(self, manager, stealth)

        def rules(self):
            return [CrawlRule(LinkExtractor(allow_domains=host))]

    return list(Crawl().start().items)


def crawl(url, limit, stealth, out, css):
    out = out or "crawl-" + re.sub(r"[^A-Za-z0-9.-]", "-", urlparse(url).netloc)
    pages = crawl_pages(url, limit, stealth, out, css)
    for p in pages:
        emit({"url": p["url"], "title": p["title"], "chars": len(p["markdown"]), "dir": out})


# --- self-check ---------------------------------------------------------------------------------

def selftest():
    from scrapling.parser import Selector
    assert unwrap("//duckduckgo.com/l/?uddg=https%3A%2F%2Fa.com%2Fx%3Fy%3D1&rut=z") == "https://a.com/x?y=1"
    bing = "https://www.bing.com/ck/a?!&&p=x&u=a1" + base64.urlsafe_b64encode(b"https://b.com/p?q=1").decode().rstrip("=") + "&ntb=1"
    assert unwrap(bing) == "https://b.com/p?q=1", unwrap(bing)
    assert unwrap("https://c.com/") == "https://c.com/"
    lite = Selector("""<table><tr><td><a class="result-link" href="https://duckduckgo.com/y.js?ad=1">Ad</a></td></tr>
        <tr><td><a class="result-link" href="//duckduckgo.com/l/?uddg=https%3A%2F%2Freal.com">Real <b>one</b></a></td></tr>
        <tr><td class="result-snippet">snip <b>pet</b></td></tr></table>""")
    assert parse_ddg_lite(lite) == [{"title": "Real one", "url": "https://real.com", "snippet": "snip pet"}], parse_ddg_lite(lite)
    good = [{"title": "Pacman hooks", "url": "https://wiki.archlinux.org/title/Pacman", "snippet": ""}]
    decoy = [{"title": "Bonde de Santa Teresa", "url": "https://rj.gov.br/bonde", "snippet": "passeio"}] * 3
    assert on_topic(good, "arch linux pacman hooks") == good
    assert on_topic(decoy + good, "arch linux pacman hooks") == []
    assert on_topic([{"title": "Clínica Odontológica", "url": "https://x.com", "snippet": ""}], "clinica odontologica") != []
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("-n", type=int, default=10)
    m = sub.add_parser("map"); m.add_argument("url"); m.add_argument("-n", type=int, default=500)
    c = sub.add_parser("crawl"); c.add_argument("url"); c.add_argument("-n", type=int, default=20)
    c.add_argument("--out"); c.add_argument("--css")
    for p in (s, m, c):
        p.add_argument("--stealth", action="store_true", help="real browser, for bot-protected sites")
    sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "search":
        search(a.query, a.n, a.stealth)
    elif a.cmd == "map":
        site_map(a.url, a.n, a.stealth)
    elif a.cmd == "crawl":
        crawl(a.url, a.n, a.stealth, a.out, a.css)
    else:
        selftest()


if __name__ == "__main__":
    main()
