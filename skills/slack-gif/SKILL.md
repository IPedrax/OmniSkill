---
name: slack-gif
description: Slack-ready animated GIFs. OmniSkill Design crew — bundled copy of the Slack GIF skill.
disable-model-invocation: true
---

# Slack GIF

> Slack-ready animated GIFs · OmniSkill Design crew

**Bundled — nothing to install.** The full Slack GIF skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. That file is the authority for this capability; the notes below are the OmniSkill house rules layered on top.

Its supporting files (scripts, references, assets) sit alongside it under `${CLAUDE_SKILL_DIR}/vendor/`. Resolve any relative path in that skill against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Use it for short looping animations sized for Slack. Keep them legible at emoji scale — a GIF needing a full-size preview to read has missed the format.

## Attribution

Vendored verbatim from [anthropics/skills](https://github.com/anthropics/skills), licensed **Apache-2.0**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE.txt`. Unmodified — upstream is the place to send fixes.
