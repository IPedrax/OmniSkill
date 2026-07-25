---
name: web-artifacts
description: shadcn HTML artifacts. OmniSkill Design crew — bundled copy of the Web Artifacts skill.
disable-model-invocation: true
---

# Web Artifacts

> shadcn HTML artifacts · OmniSkill Design crew

**Bundled — nothing to install.** The full Web Artifacts skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. That file is the authority for this capability; the notes below are the OmniSkill house rules layered on top.

Its supporting files (scripts, references, assets) sit alongside it under `${CLAUDE_SKILL_DIR}/vendor/`. Resolve any relative path in that skill against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Use it for a self-contained shareable page — a dashboard, calculator, or one-pager. For a real application with routing and a build step, use `/omniskill:frontend-design` instead.

## Attribution

Vendored verbatim from [anthropics/skills](https://github.com/anthropics/skills), licensed **Apache-2.0**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE.txt`. Unmodified — upstream is the place to send fixes.
