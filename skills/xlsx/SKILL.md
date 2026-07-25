---
name: xlsx
description: Excel with live formulas. OmniSkill Operations crew — adapter for the xlsx skill, which installs separately.
disable-model-invocation: true
---

# Excel Workbooks

> Excel with live formulas · OmniSkill Operations crew

**Installs separately.** One of only two parts of the workforce that is not bundled: the `xlsx` skill is **source-available and proprietary**, not open source, so it cannot be redistributed inside this MIT-licensed plugin.

## Use it

Invoke `/xlsx` and follow it. Reach for it any time a spreadsheet is the primary input or output.

## If it is not available

It ships with Claude Code in most environments — check before concluding it is missing.

If it genuinely is not there, add Anthropic's skills marketplace:

```bash
claude plugin marketplace add anthropics/skills
```

Install the document skills through `/plugin`, then restart Claude Code.

Do not reimplement it. Writing a valid `.xlsx` by hand is a large job full of format traps, and the result will not round-trip cleanly in Excel.

## House rules

Every Finance and Operations deliverable involving numbers should land here. Write **live formulas, not computed constants** — the point of a model is that the user changes an assumption and watches the answer move. A workbook of hardcoded values is a report, not a model.

## Attribution

By [Anthropic](https://github.com/anthropics/skills). Source-available and proprietary — deliberately not vendored.
