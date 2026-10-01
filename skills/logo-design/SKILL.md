---
name: logo-design
description: Logos as real SVG, from brief to delivery. OmniSkill Design crew. Drives the logo-design skill: brief, three concepts across different mark types, hand-built geometric SVG, scripted audits at 16 px and in one colour, a presentation board, then favicons, lockups and guidelines, with a 1,400-logo reference library to study first.
disable-model-invocation: true
---

# logo-design

> A mark that survives 16 px · OmniSkill Design crew

Claude builds the logo itself as clean SVG geometry, then proves it: `svg_audit.py` and the preview sheets test it small, in one colour, reversed and next to competitors before anyone sees a concept. No image model is involved, so nothing needs a key and nothing leaves the machine. The result is a vector file you can ship, not a raster mockup that someone still has to redraw.

Not bundled, for one reason: its reference library is 1,432 real trademarks (14 MB). Its MIT license explicitly does not cover them, so they cannot ride inside an MIT plugin. The skill lives in one checkout and this adapter points at it.

## Install once

```bash
git clone https://github.com/kaankiziltug/logo-design-skill.git ~/tools/logo-design-skill
```

Every script is stdlib Python. Rendering PNGs wants one of `rsvg-convert`, `cairosvg`, Inkscape or Chromium, and upstream picks whichever exists. Update with `git -C ~/tools/logo-design-skill pull`.

## Use it

Read `~/tools/logo-design-skill/skills/logo-design/SKILL.md` completely and follow it. Wherever it says `${CLAUDE_SKILL_DIR}` or `<skill-dir>`, that folder is `~/tools/logo-design-skill/skills/logo-design`, so scripts run as:

```bash
python3 ~/tools/logo-design-skill/skills/logo-design/scripts/svg_audit.py concept-a.svg
```

Write the concepts, sheets and exports into the user's project, never into the checkout.

Upstream ends the concept round at a checkpoint and waits for the user to pick a direction. Keep that stop. Refining all three concepts to production before anyone chooses is the most expensive way to get a logo wrong.

## House rules

**The library is for studying, never for tracing.** Search it to learn how a category is usually built, then build something that does not look like those marks. A concept that reads as a near-copy of a library entry fails, however clean the SVG is.

**Name the registry for the clearance search.** Upstream already says it cannot clear a mark and recommends a search; make that concrete for the user's market (INPI in Brazil, USPTO, EUIPO), because three geometric shapes collide easily.

## Where it sits in the crew

After direction, before the interface: `ui-ux-pro-max` or `anydesign` settles palette and type, this makes the mark inside them, and `frontend-design` places it. The finished SVG is also a fair `motion-ui` input for a logo reveal.

Against `canvas-design`: that makes an image, a poster or a cover. A logo must be a vector that holds at 16 px and on a building, which is this skill's whole method. For moodboards and photographic brand imagery, `canvas-design` is still the one.

## Source

[logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) by kaankiziltug · code **MIT**; the library logos remain their owners' trademarks (`TRADEMARKS.md`). Nothing is vendored here.
