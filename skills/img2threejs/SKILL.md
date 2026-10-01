---
name: img2threejs
description: Image to a procedural Three.js model, built in code. OmniSkill Design crew. Drives the img2threejs pipeline (intake, quality contract, sculpt spec, pass-by-pass build, screenshot review against the reference) from one shared checkout, with its state file as the gate instead of chat memory.
disable-model-invocation: true
---

# img2threejs

> A photo in, a Three.js model in code out · OmniSkill Design crew

Point it at one image of an object or a character and it rebuilds that object as procedural Three.js: geometry, materials, pivots and sockets written as TypeScript, not a downloaded mesh and not photogrammetry. The build runs in fixed passes (blockout, structure, form, material, lighting, interaction, optimization), and each pass is screenshotted and compared against the reference before the next one starts.

Not bundled: it is a Python toolkit plus a 400-line router of its own, and upstream ships often. It lives in one checkout and this adapter points at it.

## Install once

```bash
git clone https://github.com/img2threejs/img2threejs.git ~/tools/img2threejs
```

The core (`forge/`) is Python 3.10+ stdlib, so there is nothing to pip install. `IMG2THREEJS_HOME` overrides the path. Update with `git -C ~/tools/img2threejs pull`.

Skip two things the upstream README offers. Its symlink into `~/.claude/skills/` would make the upstream router model-invocable and cost listing budget, and this adapter already does that job. Its `npx github:img2threejs/img2 install` for domain plugins runs remote code on the machine, so only use it when a domain plugin (`cs2`, `animated-character`) is actually needed, and say so first.

## Use it

1. Read `$IMG2THREEJS_HOME/SKILL.md` (default `~/tools/img2threejs/SKILL.md`) completely and follow it. It is the contract; this file only routes to it.
2. Run every script by absolute path **from the user's project directory**, so `.img2threejs/state.json`, specs and renders land in the project and not in the checkout. Upstream writes `forge/next.py`; that means:

```bash
python3 ~/tools/img2threejs/forge/next.py --state .img2threejs/state.json
```

The scripts find their own `grimoire/` and `docs/` through `__file__`, and `--workspace` defaults to the current directory, so this is the intended split.

3. `next.py` is the authority on what comes next. Exit code 3 is a hard stop: report the reason and ask. Never rebuild progress from the conversation.

## Before starting, say the cost

Upstream estimates 80k to 180k tokens for an object and 150k to 350k for a character (`docs/TOKEN_COST.md`). Tell the user before the first pass, and offer the cheaper answer when it fits: a primitive blockout under `motion-ui`, or a real GLB if one exists.

Vision adapters (SAM2, MediaPipe, Depth Anything) are optional extras in `integrations/vision/` with their own torch install. The TRELLIS reference-mesh step calls a hosted Hugging Face Space, so the reference image leaves the machine; ask before using it on anything private.

## Where it sits

Against `motion-ui`: that crew puts a Three.js scene into an interface (camera, lights, scroll, a model somebody already has). img2threejs makes the model, starting from a picture. They chain: rebuild the prop here, animate it there.

Against `vgpu`: a shader surface has no meshes. A fullscreen effect is vgpu; an object with parts you can rotate, rig or break is this.

A single view cannot show the hidden sides, so say when the result is stylized or guessed instead of implying fidelity the image cannot support.

## Source

[img2threejs](https://github.com/img2threejs/img2threejs) · **Apache-2.0**. Nothing is vendored here; the checkout is cloned on its own.
