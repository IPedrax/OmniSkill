---
name: better-interfaces
description: The small details that make an interface feel finished. OmniSkill Design crew. Bundled copy of Jakub Krehel's make-interfaces-feel-better skill: 19 concrete rules (concentric radius, optical alignment, shadows over borders, text-wrap balance, tabular numbers, scale on press, interruptible motion, icon stroke, hit areas) plus a review mode that returns severity-ranked, file-and-line findings.
disable-model-invocation: true
---

# better-interfaces

> The last 10% of an interface · OmniSkill Design crew

**Bundled, nothing to install.** Upstream's skill folder sits in `${CLAUDE_SKILL_DIR}/vendor/`, unmodified.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. Its five detail files (`typography.md`, `surfaces.md`, `animations.md`, `icons.md`, `performance.md`) are in the same folder; open the one a rule points to rather than all of them. A path in those files means `${CLAUDE_SKILL_DIR}/vendor/<file>`, so write that full path into any command.

Two ways to use it:

- **While building:** apply the principles as the component is written, after `frontend-design` has settled structure and before `motion-ui` adds anything heavier.
- **As a review:** upstream defines `quick` (primary path, HIGH and MEDIUM only, at most 5 findings) and `full` (all five categories, at most 15, with the categories it did not inspect named). Both end in a verdict: Block, Needs changes or Approve. Default to `full` unless the user asks for a quick pass.

The skill's own first rule is to find the project's existing styling system and follow it before suggesting anything; keep it that way when the project uses Tailwind, CSS modules or a component library.

## Where it sits in the crew

After `frontend-design` and `web-artifacts` produce an interface, this is the polish pass; `ui-ux-pro-max` and `anydesign` settle direction first. Its icon rules (match stroke to text weight, one `currentColor` SVG recolored per state, outline by default and filled for active) pair with `tabler-icons`. For anything that needs a library (springs, scroll scrubbing, 3D) hand over to `motion-ui`; this skill is the restraint that keeps that motion honest.

ECC ships a condensed copy of this skill under its upstream name, `make-interfaces-feel-better`. That one is a shorter rewrite, by its own note salvaged from a stale community pull request, without the reference files, the icon rules or the review format; when both exist, use this one.

## Attribution

Vendored from [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) @ `35545ea` (the `skills/make-interfaces-feel-better` folder), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`.
