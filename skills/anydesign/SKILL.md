---
name: anydesign
description: Turn a reference into a design spec. OmniSkill Design crew. Bundled copy of anydesign, which reads a screenshot, URL or Figma file and writes a design.md plus DTCG design-tokens.json from measured values (real CSS variables, pixel-sampled colors, WCAG contrast), or copies one element into a rebuild prompt.
disable-model-invocation: true
---

# anydesign

> The reference, measured · OmniSkill Design crew

**Bundled.** The skill itself needs nothing; its scripts need Python and, for two of them, a package or a browser (below).

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. Resolve every relative path, `scripts/` and `references/` alike, against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory, and write the outputs (`design.md`, `design-tokens.json`, `design-a11y.md`) into the user's project.

Upstream says `python scripts/...`. Run the stdlib ones with plain `python3`. For the two that need packages, let uv supply them per call instead of installing anything:

```bash
uv run --with playwright python "${CLAUDE_SKILL_DIR}/vendor/scripts/capture_site.py" <URL> --viewports desktop,mobile
uv run --with pillow python "${CLAUDE_SKILL_DIR}/vendor/scripts/extract_colors.py" <image>
```

`capture_site.py` also needs a Chromium: `uv run --with playwright playwright install chromium` once, if `~/.cache/ms-playwright` has none. Without it, upstream falls back to WebFetch and marks typography ⚠️. That is acceptable; say so.

## Where it sits in the crew

The **front** of the Design pipeline:

```
anydesign (extract a direction)  →  ui-ux-pro-max (decide it)
        →  frontend-design (build it)  →  motion-ui (animate it)
```

Reach for it when the user can point at what they want: a screenshot, a competitor, a site they like, a Figma frame. `ui-ux-pro-max` is the other door, for when they cannot point at anything. Running both is normal: extract the spec, then let `ui-ux-pro-max` argue with it.

Its **element mode** ("copy this navbar", "a prompt for this 3D graphic") is the narrow version and skips the rest of the pipeline: the `element.md` goes straight to `frontend-design`, or to an image generator when it is art.

The output is files, not a vibe. Commit `design.md` and `design-tokens.json` so the next session reads the same spec instead of re-deriving it from the same screenshot. `verify_design.py` later reports drift between those tokens and the live site.

## House rules

**A reference is a starting point, not a target.** Extracting spacing, type scale and mood is ordinary practice. Rebuilding someone's page pixel for pixel and shipping it is not, and element mode makes that easy to slide into. If the ask drifts from "in this style" toward "make me this site", say so plainly and reset the scope.

**Never pull the reference's assets into the build.** Logos, photography, illustration and icon sets carry the rights. Extract the palette; generate or source the imagery. The user's own site is the exception.

**Effects are a handoff.** When the spec records WebGL, particles, shaders or scroll effects, pass the description to `motion-ui` (or `vgpu` for a shader surface) instead of hand-rolling a canvas here.

**Unknown beats invented.** Upstream already marks every inference ✅ ⚠️ ❓ and treats a made-up token as worse than "not enough info". Keep it that way when summarizing for the user: carry the ❓s forward instead of smoothing them over.

## Attribution

Vendored from [uxKero/anydesign](https://github.com/uxKero/anydesign) @ `d81bd89` (v0.6.0, without `examples/`), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`.
