---
name: superpowers
description: Full skill pack for planning + TDD. OmniSkill Developers crew — adapter that delegates to the Superpowers skill.
disable-model-invocation: true
---

# Superpowers

> Full skill pack for planning + TDD · OmniSkill Developers crew

This capability is provided by **Superpowers**, installed alongside OmniSkill as a plugin dependency.

## Use it

Invoke /superpowers and follow it. That skill is the authority here — this file only routes to it and adds the OmniSkill house rules below.

## House rules

Use it for feature work that deserves a plan and a test before code. It carries its own planning and TDD workflow — follow that, do not improvise a parallel one.

## If it is missing

Install it with:

```bash
claude plugin install superpowers@claude-plugins-official
```

It is declared in this plugin's `dependencies`, so a reinstall of OmniSkill also restores it.
