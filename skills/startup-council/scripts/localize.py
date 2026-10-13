#!/usr/bin/env python3
"""Localize a founder-consumer panel without touching the vendored panel.py.

panel.py deals English first names and prints income as "$". For a market like
Belo Horizonte that reads as "Mason, $24,000 a year" and makes buyers stop to guess
the currency. This rewrites the panel's own output instead:

    python3 localize.py founder/panel --currency 'R$' --names 'Ana,Bruno,Camila,...'

- after `panel.py init`: renames the personas (personas.json), so `prompts` writes
  briefs with local names. Pass at least as many names as buyers, or they repeat
  with a number, the way panel.py does.
- after `panel.py prompts` and `tally`: swaps "$" for the currency in briefs/*.md
  and results.md.
Safe to run more than once. `localize.py selftest` checks it offline.
"""
import argparse
import glob
import json
import os
import re
import sys
import tempfile


def rename(personas, names):
    if not names:
        return personas
    for i, p in enumerate(personas):
        base = names[i % len(names)]
        p["name"] = base if i < len(names) else f"{base} {i // len(names) + 1}"
    return personas


def swap_currency(text, currency):
    # "$24,000" and "$48,000 and up": only a "$" directly before a digit, so JSON
    # templates and shell snippets in the brief are left alone.
    # A currency that itself ends in "$" (R$, A$, C$) must not be swapped again on
    # a second run, so skip a "$" already preceded by the currency's own prefix.
    prefix = currency[:-1] if currency.endswith("$") else ""
    guard = f"(?<!{re.escape(prefix)})" if prefix else ""
    return re.sub(guard + r"\$(?=\d)", lambda m: currency, text)


def run(d, currency, names):
    pj = os.path.join(d, "personas.json")
    if names and os.path.exists(pj):
        personas = rename(json.load(open(pj, encoding="utf-8")), names)
        json.dump(personas, open(pj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if currency:
        for f in glob.glob(os.path.join(d, "briefs", "*.md")) + glob.glob(os.path.join(d, "results.md")):
            t = open(f, encoding="utf-8").read()
            open(f, "w", encoding="utf-8").write(swap_currency(t, currency))


def selftest():
    assert swap_currency("You earn about $24,000 a year.", "R$") == "You earn about R$24,000 a year."
    assert swap_currency("| $48,000 and up |", "R$") == "| R$48,000 and up |"
    assert swap_currency("a ${placeholder} and $ alone", "R$") == "a ${placeholder} and $ alone"
    assert swap_currency(swap_currency("$5", "R$"), "R$") == "R$5"  # idempotent
    p = rename([{"name": "Mason"}, {"name": "Noah"}, {"name": "Elle"}], ["Ana", "Bruno"])
    assert [x["name"] for x in p] == ["Ana", "Bruno", "Ana 2"], p
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "briefs"))
        json.dump([{"name": "Mason"}], open(os.path.join(d, "personas.json"), "w"))
        open(os.path.join(d, "briefs", "P001.md"), "w").write("Mason earns $12,000.")
        run(d, "R$", ["Ana"])
        assert json.load(open(os.path.join(d, "personas.json")))[0]["name"] == "Ana"
        assert open(os.path.join(d, "briefs", "P001.md")).read() == "Mason earns R$12,000."
    print("selftest ok")


def main():
    if sys.argv[1:] == ["selftest"]:
        return selftest()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir", help="the panel folder, e.g. founder/panel")
    ap.add_argument("--currency", help="symbol to use instead of $, e.g. R$")
    ap.add_argument("--names", help="comma-separated local first names")
    a = ap.parse_args()
    run(a.dir, a.currency, [n.strip() for n in (a.names or "").split(",") if n.strip()])


if __name__ == "__main__":
    main()
