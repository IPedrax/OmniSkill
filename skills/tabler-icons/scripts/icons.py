#!/usr/bin/env python3
"""Find a Tabler icon by meaning and get it as SVG or a component name.

    python3 icons.py search "parking car" [-n 15] [--category Map] [--filled]
    python3 icons.py svg car [--filled] [--size 20] [--stroke 1.5]
    python3 icons.py selftest

The icon set lives in $TABLER_ICONS_HOME (default ~/tools/tabler-icons): the
@tabler/icons npm package unpacked, with icons.json and icons/{outline,filled}.
search ranks exact name, then name words, then tags, then category, and prints one
line per icon: name, category, styles, and the component name the framework
packages export (IconCar, IconHeartFilled). svg prints the file ready to inline,
with size and stroke applied and the decorative "icon icon-tabler" class kept.
"""
import argparse
import json
import os
import re
import sys

HOME = os.path.expanduser(os.environ.get("TABLER_ICONS_HOME", "~/tools/tabler-icons"))


def component(name, filled=False):
    """car -> IconCar, a-b-2 -> IconAB2, heart filled -> IconHeartFilled."""
    return "Icon" + "".join(p[:1].upper() + p[1:] for p in name.split("-")) + ("Filled" if filled else "")


def score(name, meta, words):
    parts = set(name.split("-"))
    tags = {str(t).lower() for t in meta.get("tags", [])}
    cat = (meta.get("category") or "").lower()
    s = 0
    if name == "-".join(words):
        s += 100
    for w in words:
        if w in parts:
            s += 10
        elif any(p.startswith(w) for p in parts):
            s += 6
        if w in tags:
            s += 5
        elif any(w in t for t in tags):
            s += 2
        if w == cat:
            s += 1
    # every word must hit somewhere, so "parking car" doesn't list every car icon
    hit = all(w in name or any(w in t for t in tags) or w == cat for w in words)
    return s if hit else 0


def search(index, query, n=15, category=None, filled=False):
    words = [w for w in re.findall(r"[a-z0-9]+", query.lower())]
    rows = []
    for name, meta in index.items():
        if category and (meta.get("category") or "").lower() != category.lower():
            continue
        if filled and "filled" not in meta.get("styles", {}):
            continue
        s = score(name, meta, words)
        if s:
            rows.append((-s, len(name), name))
    return [name for _, _, name in sorted(rows)[:n]]


def svg(name, filled=False, size=None, stroke=None):
    path = os.path.join(HOME, "icons", "filled" if filled else "outline", name + ".svg")
    if not os.path.exists(path):
        sys.exit(f"no {'filled' if filled else 'outline'} icon named {name!r}")
    text = open(path, encoding="utf-8").read()
    if size:
        text = re.sub(r'(width|height)="24"', lambda m: f'{m.group(1)}="{size}"', text, count=2)
    if stroke is not None and not filled:
        text = re.sub(r'stroke-width="[\d.]+"', f'stroke-width="{stroke}"', text, count=1)
    return re.sub(r"\n\s*", " ", text).replace("> <", "><").strip()


def selftest():
    idx = {
        "car": {"category": "Vehicles", "tags": ["vehicle", "drive", 4], "styles": {"outline": {}, "filled": {}}},
        "parking": {"category": "Map", "tags": ["car", "park"], "styles": {"outline": {}}},
        "car-garage": {"category": "Vehicles", "tags": ["parking"], "styles": {"outline": {}}},
        "heart": {"category": "Health", "tags": ["love"], "styles": {"outline": {}, "filled": {}}},
    }
    assert search(idx, "car")[0] == "car"
    assert set(search(idx, "parking car")) == {"parking", "car-garage"}, search(idx, "parking car")
    assert search(idx, "car", filled=True) == ["car"]
    assert search(idx, "love") == ["heart"]
    assert search(idx, "zzz") == []
    assert component("car") == "IconCar" and component("a-b-2") == "IconAB2"
    assert component("heart", filled=True) == "IconHeartFilled"
    print("selftest ok")


def main():
    if sys.argv[1:] == ["selftest"]:
        return selftest()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("-n", type=int, default=15)
    s.add_argument("--category")
    s.add_argument("--filled", action="store_true", help="only icons that have a filled style")
    v = sub.add_parser("svg")
    v.add_argument("name")
    v.add_argument("--filled", action="store_true")
    v.add_argument("--size", type=int)
    v.add_argument("--stroke", type=float)
    a = ap.parse_args()
    if a.cmd == "svg":
        print(svg(a.name, a.filled, a.size, a.stroke))
        return
    idx_path = os.path.join(HOME, "icons.json")
    if not os.path.exists(idx_path):
        sys.exit(f"icon set not found at {HOME}; see the skill's install step")
    index = json.load(open(idx_path, encoding="utf-8"))
    for name in search(index, a.query, a.n, a.category, a.filled):
        m = index[name]
        styles = ",".join(m.get("styles", {}))
        print(f"{name}\t{m.get('category') or '-'}\t{styles}\t{component(name, a.filled)}")


if __name__ == "__main__":
    main()
