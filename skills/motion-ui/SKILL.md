---
name: motion-ui
description: Animation engines and animated UI. OmniSkill Design crew — bundled copy of motion-ui: picks Framer Motion, GSAP, anime.js, or Three.js to fit the stack, then builds polished animated components.
disable-model-invocation: true
---

# Motion UI

> Animation that fits the stack · OmniSkill Design crew

**Bundled — nothing to install.**

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it.

Its cookbooks and the stack detector sit alongside:

- `vendor/references/motion-patterns.md` — Framer Motion recipes
- `vendor/references/animation-libraries.md` — GSAP, anime.js, Three.js
- `vendor/references/21st-components.md` — sourcing and fallback components
- `vendor/scripts/detect-stack.mjs` — the compatibility gate

Resolve every relative path against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

**Detect before installing.** The compatibility gate is the point of this skill: it reports which engines the project can actually use before anything is written to `package.json`. Framer Motion is React-only; GSAP, anime.js, and Three.js run in any JS project.

Pick by the job, not by habit — Framer Motion for React component motion, GSAP for scroll and timeline work, anime.js for a light touch, Three.js for 3D.

**Direction first.** Settle style, palette, and typography with `/omniskill:ui-ux-pro-max`, build the interface with `/omniskill:frontend-design`, then animate here. Motion applied to an undecided design amplifies the indecision.

**Confirm mode is the default and should stay that way.** `--auto` hands the whole job over end to end; it is opt-in precisely so that never happens by accident.

Accessibility is not optional here: every component honors `prefers-reduced-motion`, animates transform and opacity only for 2D, and disposes GPU resources for Three.js.

## Attribution

Vendored from [IPedrax/motion-ui](https://github.com/IPedrax/motion-ui), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`.
