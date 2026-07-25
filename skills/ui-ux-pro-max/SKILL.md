---
name: ui-ux-pro-max
description: Full design-system intel. OmniSkill Design crew — bundled design intelligence: styles, palettes, font pairings, and stack-specific guidance.
disable-model-invocation: true
---

# UI/UX Pro Max

> Full design-system intel · OmniSkill Design crew

**Bundled — nothing to install.** The full skill ships inside this plugin.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. Its data tables and scripts sit under `${CLAUDE_SKILL_DIR}/vendor/data/` and `${CLAUDE_SKILL_DIR}/vendor/scripts/` — resolve any relative path against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

**Start every design task here.** It carries the style catalogue, palettes, font pairings, and per-stack guidance. Decide style, palette, and typography *before* any markup exists — reversing that order is what produces the templated look the Design crew exists to avoid.

Hand the chosen direction to `/omniskill:frontend-design` to implement, or `/omniskill:web-artifacts` for a self-contained page.

## Related

For animation and motion work, the companion [motion-ui](https://github.com/IPedrax/motion-ui) skill installs separately and picks an engine (Framer Motion, GSAP, anime.js, Three.js) that fits the detected stack:

```powershell
irm https://raw.githubusercontent.com/IPedrax/motion-ui/main/install.ps1 | iex
```
