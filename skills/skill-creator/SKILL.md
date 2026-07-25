---
name: skill-creator
description: Scaffold your own skills. OmniSkill Developers crew — bundled copy of the Skill Creator skill.
disable-model-invocation: true
---

# Skill Creator

> Scaffold your own skills · OmniSkill Developers crew

**Bundled — nothing to install.** The full Skill Creator skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. That file is the authority for this capability; the notes below are the OmniSkill house rules layered on top.

Its supporting files (scripts, references, assets) sit alongside it under `${CLAUDE_SKILL_DIR}/vendor/`. Resolve any relative path in that skill against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Use it when a workflow has been repeated enough to be worth codifying. It also evaluates and improves existing skills, including the ones in this plugin.

## Attribution

Vendored verbatim from [anthropics/claude-plugins-public](https://github.com/anthropics/claude-plugins-public), licensed **Apache-2.0**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE.txt`. Unmodified — upstream is the place to send fixes.
