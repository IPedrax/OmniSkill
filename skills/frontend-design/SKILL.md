---
name: frontend-design
description: Bold React + Tailwind UI. OmniSkill Design crew — bundled copy of the Frontend Design skill.
disable-model-invocation: true
---

# Frontend Design

> Bold React + Tailwind UI · OmniSkill Design crew

**Bundled — nothing to install.** The full Frontend Design skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. That file is the authority for this capability; the notes below are the OmniSkill house rules layered on top.

Its supporting files (scripts, references, assets) sit alongside it under `${CLAUDE_SKILL_DIR}/vendor/`. Resolve any relative path in that skill against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Settle direction with `/omniskill:ui-ux-pro-max` first, then build here. Implementing before the palette and type system are chosen is what produces generic-looking output.

## Attribution

Vendored verbatim from [anthropics/claude-plugins-public](https://github.com/anthropics/claude-plugins-public), licensed **Apache-2.0**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE.txt`. Unmodified — upstream is the place to send fixes.
