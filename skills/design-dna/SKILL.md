---
name: design-dna
description: Turn a reference UI into a design spec. OmniSkill Design crew — bundled copy of design-dna: reads screenshots or URLs and produces a quantified Design DNA JSON (tokens, qualitative style, visual effects), then generates from it.
disable-model-invocation: true
---

# Design DNA

> The reference, made specific · OmniSkill Design crew

**Bundled — nothing to install.**

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it.

Its references sit alongside:

- `vendor/references/schema.md` — the full three-dimension field list
- `vendor/references/generation-guide.md` — Phase 3, turning DNA JSON into a build

Resolve every relative path against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## Where it sits in the crew

This is the **front** of the Design pipeline, ahead of everything else:

```
design-dna (extract a direction)  →  ui-ux-pro-max (decide it)
        →  frontend-design (build it)  →  motion-ui (animate it)
```

Reach for it when the user already knows what they want it to look like and can point at it: a screenshot, a competitor, a site they like, a Dribbble shot. `ui-ux-pro-max` is the other door, for when they cannot point at anything and need a direction chosen for them. Running both is normal: extract the DNA, then let `ui-ux-pro-max` argue with it.

The output is a JSON file, not a vibe. Write it to the repo and commit it. That is the whole point: the next session, the next agent, and the next page all read the same spec instead of re-deriving it from the same screenshot.

## House rules

**A reference is a starting point, not a target.** Extracting spacing, type scale, and mood from a design is ordinary practice. Rebuilding someone's page pixel for pixel and shipping it is not. If the ask drifts from "in this style" toward "make me this site", say so plainly and reset the scope.

**Never pull the reference's assets into the build.** The vendored Phase 3 tells you to fetch real assets from the source URL when the user provided one. That is correct for the user's *own* site and wrong for anybody else's: logos, photography, illustration, and icon sets are the parts that actually carry rights. Extract the palette; generate or source the imagery.

**`visual_effects` is a handoff, not an instruction to freestyle.** When the DNA reports WebGL, particles, shaders, or scroll effects, that is `motion-ui`'s job. Pass the effect description and the `performance_tier` over and let the compatibility gate choose an engine, rather than hand-rolling a canvas here.

**Fill every field or say why you cannot.** A DNA profile with half its fields blank is worse than no profile, because the generation phase will invent the rest silently and confidently. When a reference genuinely does not show something (motion in a still screenshot, dark mode in a light-only capture), record that instead of guessing.

## Attribution

Vendored from [zanwei/design-dna](https://github.com/zanwei/design-dna), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`.
