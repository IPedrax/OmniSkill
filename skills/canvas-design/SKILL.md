---
name: canvas-design
description: Visual art to PNG / PDF. OmniSkill Design crew — bundled copy of the Canvas Design skill.
disable-model-invocation: true
---

# Canvas Design

> Visual art to PNG / PDF · OmniSkill Design crew

**Bundled — nothing to install.** The full Canvas Design skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. That file is the authority for this capability; the notes below are the OmniSkill house rules layered on top.

Its supporting files (scripts, references, assets) sit alongside it under `${CLAUDE_SKILL_DIR}/vendor/`. Resolve any relative path in that skill against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Use it for static visual output — posters, covers, printable diagrams. State output dimensions and whether the target is screen or print *before* generating; retrofitting print resolution means redoing the work.

The bundled copy ships 54 fonts under `vendor/canvas-fonts/`, each with its SIL Open Font License. Reference them from that path.

## Attribution

Vendored verbatim from [anthropics/skills](https://github.com/anthropics/skills), licensed **Apache-2.0**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE.txt`. Unmodified — upstream is the place to send fixes.
