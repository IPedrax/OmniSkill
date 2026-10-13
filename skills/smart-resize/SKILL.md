---
name: smart-resize
description: Content-aware image resizing (seam carving). OmniSkill Design crew. Change an image's width, height or aspect ratio, for example a 16:9 photo to 9:16 or a banner to a square, by removing or adding the least interesting pixel paths so subjects keep their shape instead of being squashed or cropped. Protect or remove regions with boxes. Bundled numpy and Pillow script, no model, no GPU, nothing leaves the machine.
disable-model-invocation: true
---

# smart-resize

> Reframe without squashing · OmniSkill Design crew

Plain scaling distorts a subject and a crop cuts it off. Seam carving finds the connected path of pixels, top to bottom, with the least visual change (flat sky, blurred background, floor) and removes it, over and over. Paths through busy areas cost more, so faces, products and edges survive. Enlarging runs the same search and duplicates the cheapest paths. The method is from Avidan and Shamir's 2007 paper "Seam Carving for Content-Aware Image Resizing", implemented here from scratch, with no code from any other tool.

## Run it

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/smartresize.py in.jpg out.png --aspect 9:16
python3 ${CLAUDE_SKILL_DIR}/scripts/smartresize.py in.jpg out.png --width 800
python3 ${CLAUDE_SKILL_DIR}/scripts/smartresize.py in.jpg out.png --width 1400 --height 700 --keep 300,120,400,500
python3 ${CLAUDE_SKILL_DIR}/scripts/smartresize.py in.jpg out.png --perc 30 --drop 0,0,200,900
```

Write the full path into the command; Bash does not set `CLAUDE_SKILL_DIR`. Needs `numpy` and `Pillow` (`pip install numpy pillow` or `uv run --with numpy --with pillow`).

| Option | Does |
|---|---|
| `--width N` / `--height N` | target size on that axis; carves to shrink, inserts seams to grow |
| `--aspect W:H` | reframes by carving whichever side is too long, so `--aspect 9:16` on a landscape photo narrows it |
| `--perc P` | removes P% of the width (negative adds) |
| `--keep x,y,w,h` | protect a box: a face, a product, a logo, text. Repeat for several |
| `--drop x,y,w,h` | make a box the first thing removed: a stray person, a sign |

Protection applies to the first axis carved (width, then height). Output is PNG unless the extension says otherwise; transparency is kept.

## Make it work

1. **Look at the image first** and decide what must survive. Then give `--keep` boxes in pixel coordinates (x, y from the top left). Without them the algorithm only knows edges, so it will happily slice through a face of low contrast.
2. **Change less than about 30 to 40 percent** of an axis. Beyond that, scale most of the way with an ordinary resize and carve the rest, or accept visible warping. Enlarging past 25 percent shows repeated stripes.
3. **Judge by eye.** Open the result. Straight lines that cross a seam bend, and that is the failure to look for.
4. **Keep the original.** The operation is lossy and not reversible.

## What it does badly

Measured on a 981 by 832 screenshot of a package-manager window, reframed to 9:16 (513 seams removed): the photo-like parts were fine, but every line of text came out with letters fused and clipped, because text is thin, high-frequency detail on a flat background, which is exactly what the energy map calls "cheap". So:

- **Screenshots, UI, charts, diagrams, text:** do not carve them. Crop, or pad to the new ratio.
- **Regular patterns** (fences, grids, brick) and **straight edges** wobble.
- **Crowded scenes** with no empty space have no cheap path to take.

## Speed

Pure numpy with a Python loop per row, about 40 ms a seam on a 1000 px image: 20 seconds to remove 500 seams, and it gets slower with size. Shrink a large photo with an ordinary resize first (to about 1000 px on the long side), then carve. There is no face detector: pick the box yourself with `--keep`.

## Where it sits in the crew

For reframing stills, for example a hero image to a vertical story or thumbnail. `craft-video` can call it for background frames. Anything about design direction or new imagery belongs to `ui-ux-pro-max` or `canvas-design`.

## Source

Original to OmniSkill, written from the published algorithm. The research behind it: Avidan and Shamir, ACM SIGGRAPH 2007. Prior open-source implementations exist (for example esimov/caire, MIT); none of their code is used here.
