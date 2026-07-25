---
name: algorithmic-art
description: Generative p5.js art. OmniSkill Design crew — builds seeded, parameterised generative systems that produce a coherent family of outputs rather than one lucky image.
disable-model-invocation: true
---

# Algorithmic Art

> Generative p5.js art · OmniSkill Design crew

Code-driven visual art. The deliverable is a **system that produces a family of good outputs**, not a single image that happened to work.

## The discipline

**Seed everything.** Use a seeded PRNG, never bare `Math.random()`. Without a seed, a good output cannot be reproduced, printed at higher resolution, or iterated on — it is gone the moment the page reloads.

```js
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);
```

Display the seed on the canvas during development and make it settable from the URL. Then any output can be recovered exactly.

**Parameterise, then tune.** Pull every magic number into a named parameter object at the top. Tuning is where the work actually happens, and constants buried in draw calls cannot be tuned.

**Judge the distribution, not one frame.** Generate a contact sheet of 25–100 seeds and look at them together. A system whose median output is good is a good system. A system with one brilliant output and 99 poor ones is not — it is one image with extra steps.

## Techniques worth knowing

**Perlin/simplex noise** — the foundation of most organic generative work. Smooth, continuous, controllable.
```js
// Third dimension as time gives coherent animation
let n = noise(x * scale, y * scale, frameCount * 0.01);
```
Scale controls feature size; octaves control detail. `noise()` returns roughly 0.3–0.7 in practice — remap it rather than assuming a full 0–1 range.

**Flow fields** — noise drives an angle, particles follow it. Produces the characteristic organic streaming look.
```js
let angle = noise(x * 0.005, y * 0.005) * TWO_PI * 2;
p.add(createVector(cos(angle), sin(angle)));
```

**Recursive subdivision** — split a rectangle repeatedly with a probability of stopping. Reliable structural variety with very little code.

**Packing** — place shapes, reject on overlap, retry. Simple and dependable; cap the attempts so it terminates.

**Differential growth, reaction-diffusion, L-systems** — for organic and botanical forms.

**Physical simulation** — attraction, repulsion, collision. Emergent structure from simple local rules.

## Composition

Technique alone produces noise. What separates generative art from generative output:

- **Constrain the palette.** 3–5 colours chosen deliberately. Random hues look random. Sample from a real source — a photograph, a painting, a curated palette. See `/omniskill:ui-ux-pro-max`.
- **Vary density, not just position.** Rest matters as much as detail; uniform density reads as texture rather than composition.
- **Establish hierarchy.** Something should dominate. Everything equal is nothing.
- **Break the grid deliberately.** Perfect regularity is dead; controlled irregularity is alive.
- **Layer.** Depth from overlap, transparency, and scale variation.

## Performance

`draw()` runs 60 times a second — do not allocate there. Precompute in `setup()`. For static output, render once and call `noLoop()`.

Beyond a few thousand elements, drop `p5` vector objects for flat typed arrays. Use the `p2d` renderer unless WebGL is genuinely needed.

## Export

Export at print resolution from the start — retrofitting is usually a rewrite. Either scale the whole system by a factor, or use `createGraphics()` at target size and draw into it.

Vector output (SVG via `p5.svg`) where the work is line-based and needs to scale or plot. Raster (PNG) where texture and blending matter.

Rule of thumb for print: 300 DPI at final physical size.

Route final image assembly and PDF output to `/omniskill:canvas-design`.

## Deliver

The sketch with named parameters, a seed control, a contact sheet of representative outputs, and export at target resolution. Note the seeds of the strongest outputs — those are the results.

## Checks before delivering

- Seeded PRNG throughout; no bare `Math.random()`.
- Any output reproducible from its seed.
- Parameters named and grouped, not inline constants.
- Contact sheet reviewed — the median output is good.
- Palette is deliberate, not random.
- Nothing allocated inside `draw()`.
- Export resolution matches the intended use.
