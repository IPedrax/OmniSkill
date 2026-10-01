---
name: design
description: This skill should be used when the user needs the OmniSkill Design crew — extracting a design system or one element from a screenshot, URL or Figma file, building React/Tailwind UI, shadcn HTML artifacts, visual art exported to PNG or PDF, developer slide decks, generative p5.js art, WebGPU shaders and effects, image-to-Three.js model reconstruction, design-system and palette intelligence, editing the running app visually, UI animation with Framer Motion/GSAP/anime.js/Three.js/Lenis, interface sound effects, or animated Slack GIFs. Triggers on "/omniskill:design", "design a landing page", "make this UI look better", "make it look like this site", "extract the design from this screenshot", "copy this navbar", "edit my app visually", "point and click at my UI", "visual editor", "slide deck", "conference talk", "presentation with code", "shader", "WebGPU", "image to 3D model", "add animations", "scroll animation", "smooth scrolling", "add sound effects", "color palette", "design system", "make a GIF".
when_to_use: Use for visual and interface work — layout, typography, color, motion, and generated visual assets.
allowed-tools: Read Glob
---

# 02 — Design

> UI that never looks templated. **Your design studio.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `anydesign` | The user can point at a reference: screenshot, URL, Figma, competitor. Measures it into design.md + tokens, or copies one element. |
| `ui-ux-pro-max` | Choosing the direction from scratch: style, palette, font pairing, layout system. **Start here** when there is no reference. |
| `frontend-design` | Building the actual React + Tailwind interface |
| `web-artifacts` | A self-contained shadcn/HTML artifact rather than a project |
| `canvas-design` | Static visual art exported to PNG or PDF (posters, covers, diagrams) |
| `slidev` | A talk, not a page — Markdown slide decks with live code, diagrams and math |
| `airship` | The app is already running and the remaining work is pointing at it — visual editing that lands in the source |
| `motion-ui` | Animating an interface — scroll effects, transitions, smooth scroll, 3D |
| `uisfx` | Interface sound: semantic cues tied to state changes, off by default |
| `algorithmic-art` | Generative, code-driven art with p5.js |
| `vgpu` | The GPU: WebGPU shaders, fullscreen effects, compute — testable headless |
| `img2threejs` | One reference image rebuilt as a procedural Three.js model, in code, gated pass by pass |
| `slack-gif` | Short animated GIFs sized for Slack |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

Decide direction before writing markup. Two doors lead in: `anydesign` when the user can point at something they want it to look like, `ui-ux-pro-max` when they cannot and need the direction chosen. Running both is normal — extract the spec, then argue with it. `frontend-design` implements whatever comes out. Reversing that order produces the templated look this crew exists to avoid.

Match the target to the artifact: a shareable one-pager is `web-artifacts`, a real app is `frontend-design`, a printed or posted image is `canvas-design`, a talk is `slidev`. Reach for `slidev` when the deck contains code, diagrams or math — that is what it is for. A pitch with none of that is Finance's `pitch-deck` for the narrative and `canvas-design` for the image; a Vite project is the wrong shape for a board update.

Generative visuals split by runtime, not by look: `algorithmic-art` is a p5.js sketch on the CPU, `vgpu` is WebGPU when the work is a fullscreen effect, a shader background, a particle count p5 cannot reach, or a compute pass. A 3D scene with meshes and a camera is still `motion-ui` and Three.js; when the scene needs a model that only exists as a picture, `img2threejs` builds it first and hands it over. It is expensive (six figures of tokens for one object), so quote the cost before starting. Check WebGPU support against the target before committing to it — there is no shader-level fallback.

`airship` is the iteration pass, not a third door in. Once the interface exists and the dev server is up, it turns a click on the running page into the file and line that drew it, which beats describing a spacing problem in prose. Reaching for it before the direction is settled just produces uncommitted adjustments faster. It also spawns its own agent against the same files, so hand the working tree over cleanly — commit first, and let the user run the CLI themselves.

`motion-ui` comes last, and `uisfx` after that. Animating a design that is still undecided amplifies the indecision — settle direction and structure first, then add motion, then sound the moments that already earned an animation. Sound ships off by default; see that skill's house rules before wiring a single cue.
