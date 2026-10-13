#!/usr/bin/env python3
"""Can this CDP endpoint stand in for Chromium under Playwright? Seven checks, one command.

    PY=$(uv tool dir)/scrapling/bin/python            # any Python that has playwright
    $PY cdp_check.py --chromium                       # the reference: Playwright's own Chromium
    moli serve --layout --sync-geometry --port 9400 &
    $PY cdp_check.py --cdp http://127.0.0.1:9400      # the browser under test
    $PY cdp_check.py selftest

Each check drives a small local page the way an agent would (find by role, click, type, read the
text back, wait for a visible element). The page rebuilds its own DOM from scripts, which is what
broke Moli v1.1.17: its layout is published lazily, so content added after load reads as invisible
and empty. Exit status is 0 only when every check passes. Seven passes is necessary, not sufficient: confirm
with a real app before switching the Playwright MCP to Moli.
"""
import sys

PAGE = """<!doctype html><html lang=en><title>probe</title><style>
 .row{position:relative;height:40px;margin:4px 0} .row input{position:absolute;left:0;top:0;width:40px;height:40px;opacity:0;z-index:2}
 .row label{display:block;padding-left:50px;line-height:40px} .row.done label{text-decoration:line-through}
 #panel{display:none} #panel.open{display:block}
</style><body><h1>Probe</h1>
<input id=iname aria-label="Item name"><button id=add>Add item</button><ul id=list aria-label=items></ul>
<button id=opn>Open panel</button><div id=panel><button id=cfm>Confirm</button></div><p id=result role=status></p><p id=late></p>
<script>
 setTimeout(()=>{document.getElementById('late').textContent='Loaded later'},300);
 function addItem(v){const li=document.createElement('li');li.className='row';
   li.innerHTML='<input type=checkbox aria-label="toggle"><label></label>' /* compliance-ignore: SEC-XSS constant markup, local probe page */;li.querySelector('label').textContent=v;
   li.querySelector('input').addEventListener('change',e=>li.classList.toggle('done',e.target.checked));document.getElementById('list').appendChild(li);console.log('added '+v)}
 const $=id=>document.getElementById(id);
 $('add').onclick=()=>{addItem($('iname').value||'unnamed');$('iname').value=''};
 $('iname').addEventListener('keydown',e=>{if(e.key==='Enter')$('add').click()});
 $('opn').onclick=()=>$('panel').classList.add('open'); $('cfm').onclick=()=>{$('result').textContent='confirmed'};
</script></body></html>"""


def run_checks(pg):
    """[(name, ok, detail)] for one Playwright page."""
    results, logs = [], []
    pg.on("console", lambda m: logs.append(m.text))
    pg.set_content(PAGE)
    pg.wait_for_timeout(500)

    def check(name, fn):
        try:
            ok, detail = fn()
        except Exception as e:  # a timeout or protocol error is a failed check, not a crash
            ok, detail = False, (str(e).splitlines() or ["error"])[0][:70]
        results.append((name, bool(ok), str(detail)))

    check("find by role", lambda: (pg.get_by_role("heading", name="Probe").inner_text() == "Probe", "h1"))
    pg.get_by_label("Item name").fill("milk")
    pg.get_by_role("button", name="Add item").click()
    check("new list item is visible and readable", lambda: (
        pg.locator("#list li label").first.is_visible() and pg.locator("#list li label").first.inner_text() == "milk",
        repr(pg.locator("#list li label").first.inner_text())))
    check("timer-added text readable", lambda: (pg.locator("#late").inner_text() == "Loaded later", repr(pg.locator("#late").inner_text())))
    check("Enter key adds an item", lambda: (
        (pg.get_by_label("Item name").fill("eggs"), pg.get_by_label("Item name").press("Enter"), pg.wait_for_timeout(200))
        and pg.locator("#list li").count() == 2, f"{pg.locator('#list li').count()} items"))
    check("click an overlaid invisible checkbox", lambda: (
        (pg.locator("#list li input").first.check(timeout=3000), pg.locator("#list li").first.get_attribute("class"))[1] == "row done", "class toggled"))
    check("click inside a panel shown by a click", lambda: (
        (pg.get_by_role("button", name="Open panel").click(), pg.get_by_role("button", name="Confirm").click(timeout=3000),
         pg.locator("#result").inner_text())[2] == "confirmed", "status text"))
    check("console messages captured", lambda: (any(l.startswith("added") for l in logs), f"{len(logs)} logged"))
    return results


def selftest():
    assert "id=cfm" in PAGE and PAGE.count("<script>") == 1
    ok = [("a", True, ""), ("b", False, "x")]
    assert sum(r[1] for r in ok) == 1
    print("selftest ok")


def main():
    if sys.argv[1:] == ["selftest"]:
        return selftest()
    args = sys.argv[1:]
    cdp = args[args.index("--cdp") + 1] if "--cdp" in args else None
    if not cdp and "--chromium" not in args:
        sys.exit(__doc__)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        if cdp:
            browser = p.chromium.connect_over_cdp(cdp)
            ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
        else:
            browser = p.chromium.launch()
            page = browser.new_page()
        res = run_checks(page)
        browser.close()
    for name, ok, detail in res:
        print(f"{'PASS' if ok else 'FAIL'}  {name:46} {detail}")
    passed = sum(ok for _, ok, _ in res)
    print(f"{passed}/{len(res)} passed")
    sys.exit(0 if passed == len(res) else 1)


if __name__ == "__main__":
    main()
