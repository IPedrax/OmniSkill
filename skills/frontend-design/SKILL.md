---
name: frontend-design
description: Bold React + Tailwind UI. OmniSkill Design crew — adapter that delegates to the Frontend Design skill.
disable-model-invocation: true
---

# Frontend Design

> Bold React + Tailwind UI · OmniSkill Design crew

This capability is provided by **Frontend Design**, installed alongside OmniSkill as a plugin dependency.

## Use it

Invoke /frontend-design and follow it. That skill is the authority here — this file only routes to it and adds the OmniSkill house rules below.

## House rules

Settle direction with `/omniskill:ui-ux-pro-max` first, then build here. Implementing before the palette and type system are chosen is what produces generic-looking output.

## If it is missing

Install it with:

```bash
claude plugin install frontend-design@claude-plugins-official
```

It is declared in this plugin's `dependencies`, so a reinstall of OmniSkill also restores it.
