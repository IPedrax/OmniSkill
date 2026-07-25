---
name: skill-creator
description: Scaffold your own skills. OmniSkill Developers crew — adapter that delegates to the Skill Creator skill.
disable-model-invocation: true
---

# Skill Creator

> Scaffold your own skills · OmniSkill Developers crew

This capability is provided by **Skill Creator**, installed alongside OmniSkill as a plugin dependency.

## Use it

Invoke /skill-creator and follow it. That skill is the authority here — this file only routes to it and adds the OmniSkill house rules below.

## House rules

Use it when a workflow has been repeated enough to be worth codifying. It also evaluates and improves existing skills, including the ones in this plugin.

## If it is missing

Install it with:

```bash
claude plugin install skill-creator@claude-plugins-official
```

It is declared in this plugin's `dependencies`, so a reinstall of OmniSkill also restores it.
