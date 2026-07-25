---
name: design
description: This skill should be used when the user needs the OmniSkill Design crew — building React/Tailwind UI, shadcn HTML artifacts, visual art exported to PNG or PDF, generative p5.js art, design-system and palette intelligence, or animated Slack GIFs. Triggers on "/omniskill:design", "design a landing page", "make this UI look better", "generative art", "color palette", "design system", "make a GIF".
when_to_use: Use for visual and interface work — layout, typography, color, motion, and generated visual assets.
allowed-tools: Read Glob
---

# 02 — Design

> UI that never looks templated. **Your design studio.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `ui-ux-pro-max` | Choosing the direction: style, palette, font pairing, layout system. **Start here.** |
| `frontend-design` | Building the actual React + Tailwind interface |
| `web-artifacts` | A self-contained shadcn/HTML artifact rather than a project |
| `canvas-design` | Static visual art exported to PNG or PDF (posters, covers, diagrams) |
| `algorithmic-art` | Generative, code-driven art with p5.js |
| `slack-gif` | Short animated GIFs sized for Slack |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

Decide direction before writing markup. `ui-ux-pro-max` picks style, palette, and type; `frontend-design` implements it. Reversing that order produces the templated look this crew exists to avoid.

Match the target to the artifact: a shareable one-pager is `web-artifacts`, a real app is `frontend-design`, a printed or posted image is `canvas-design`.
