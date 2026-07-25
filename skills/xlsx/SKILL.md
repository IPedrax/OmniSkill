---
name: xlsx
description: Excel with live formulas. OmniSkill Operations crew — adapter that delegates to the Excel Workbooks skill.
disable-model-invocation: true
---

# Excel Workbooks

> Excel with live formulas · OmniSkill Operations crew

This capability is provided by **Excel Workbooks**, bundled with Claude Code — nothing to install.

## Use it

Invoke /xlsx and follow it. That skill is the authority here — this file only routes to it and adds the OmniSkill house rules below.

## House rules

Every Finance and Operations deliverable that involves numbers should land here. Write **live formulas**, not computed constants: the point of a model is that the user can change an assumption and watch the answer move. A workbook of hardcoded values is a report, not a model.

## If it is missing

It ships with Claude Code, so absence means bundled skills are disabled. Check the `disableBundledSkills` setting.
