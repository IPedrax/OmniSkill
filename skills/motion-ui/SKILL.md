---
name: motion-ui
description: Animation engines and animated UI. OmniSkill Design crew — bundled copy of motion-ui: picks Framer Motion, GSAP, anime.js, or Three.js to fit the stack, layers Lenis or morphicons where they belong, then builds polished animated components with designed timing.
disable-model-invocation: true
---

# Motion UI

> Animation that fits the stack · OmniSkill Design crew

**Bundled — nothing to install.**

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it.

Its cookbooks and the stack detector sit alongside:

- `vendor/references/motion-craft.md` — how it should move: durations, easing, stagger, personality
- `vendor/references/motion-patterns.md` — Framer Motion recipes
- `vendor/references/animation-libraries.md` — GSAP, anime.js, Three.js, Lenis, morphicons
- `vendor/references/21st-components.md` — sourcing, open shadcn registries, fallback components
- `vendor/scripts/detect-stack.mjs` — the compatibility gate

Resolve every relative path against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

**Detect before installing.** The compatibility gate is the point of this skill: it reports which engines the project can actually use before anything is written to `package.json`. Framer Motion is React-only; GSAP, anime.js, Three.js, Lenis, and morphicons run in any JS project.

Pick by the job, not by habit — Framer Motion for React component motion, GSAP for scroll and timeline work, anime.js for a light touch, Three.js for 3D. Lenis is a scroll *layer* that goes under one of those, never instead of one, and never on a dashboard or a docs site. morphicons is for icon-to-icon transitions and nothing else.

**The best outcome is often no install.** A one-off fade is CSS; a single reveal is an `IntersectionObserver`. Pulling in a timeline library for one transition is exactly what the gate exists to prevent, so say so rather than installing to look useful.

**Craft before code.** `motion-craft.md` settles duration bands, easing by intent, stagger limits, and the reduced-motion design. Pick one personality column and hold it across the whole job. Values chosen per-component are what "templated" actually looks like.

**Direction first.** Extract a reference with `/omniskill:anydesign` or choose one with `/omniskill:ui-ux-pro-max`, build the interface with `/omniskill:frontend-design`, then animate here. Motion applied to an undecided design amplifies the indecision.

**Confirm mode is the default and should stay that way.** `--auto` hands the whole job over end to end; it is opt-in precisely so that never happens by accident.

Accessibility is not optional here: every component honors `prefers-reduced-motion` (as a designed path, not a disabled one), animates transform and opacity only for 2D, and disposes GPU resources for Three.js.

**Two things cost money or rights**, and both are gated in the cookbooks: the external `scroll-world` pipeline bills real credits per rendered clip, and Skiper UI's premium tier is licensed. Neither may be used without saying so first.

## Attribution

Vendored from [IPedrax/motion-ui](https://github.com/IPedrax/motion-ui), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`.
