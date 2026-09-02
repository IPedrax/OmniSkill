---
name: design
description: This skill should be used when the user needs the OmniSkill Design crew — extracting a design direction from a reference screenshot or URL, building React/Tailwind UI, shadcn HTML artifacts, visual art exported to PNG or PDF, generative p5.js art, design-system and palette intelligence, editing the running app visually, UI animation with Framer Motion/GSAP/anime.js/Three.js/Lenis, interface sound effects, or animated Slack GIFs. Triggers on "/omniskill:design", "design a landing page", "make this UI look better", "make it look like this site", "extract the design from this screenshot", "edit my app visually", "point and click at my UI", "visual editor", "add animations", "scroll animation", "smooth scrolling", "add sound effects", "color palette", "design system", "make a GIF".
when_to_use: Use for visual and interface work — layout, typography, color, motion, and generated visual assets.
allowed-tools: Read Glob
---

# 02 — Design

> UI that never looks templated. **Your design studio.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `design-dna` | The user can point at a reference — screenshot, URL, competitor. Extracts it into a spec. |
| `ui-ux-pro-max` | Choosing the direction from scratch: style, palette, font pairing, layout system. **Start here** when there is no reference. |
| `frontend-design` | Building the actual React + Tailwind interface |
| `web-artifacts` | A self-contained shadcn/HTML artifact rather than a project |
| `canvas-design` | Static visual art exported to PNG or PDF (posters, covers, diagrams) |
| `airship` | The app is already running and the remaining work is pointing at it — visual editing that lands in the source |
| `motion-ui` | Animating an interface — scroll effects, transitions, smooth scroll, 3D |
| `uisfx` | Interface sound: semantic cues tied to state changes, off by default |
| `algorithmic-art` | Generative, code-driven art with p5.js |
| `slack-gif` | Short animated GIFs sized for Slack |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

Decide direction before writing markup. Two doors lead in: `design-dna` when the user can point at something they want it to look like, `ui-ux-pro-max` when they cannot and need the direction chosen. Running both is normal — extract the DNA, then argue with it. `frontend-design` implements whatever comes out. Reversing that order produces the templated look this crew exists to avoid.

Match the target to the artifact: a shareable one-pager is `web-artifacts`, a real app is `frontend-design`, a printed or posted image is `canvas-design`.

`airship` is the iteration pass, not a third door in. Once the interface exists and the dev server is up, it turns a click on the running page into the file and line that drew it, which beats describing a spacing problem in prose. Reaching for it before the direction is settled just produces uncommitted adjustments faster. It also spawns its own agent against the same files, so hand the working tree over cleanly — commit first, and let the user run the CLI themselves.

`motion-ui` comes last, and `uisfx` after that. Animating a design that is still undecided amplifies the indecision — settle direction and structure first, then add motion, then sound the moments that already earned an animation. Sound ships off by default; see that skill's house rules before wiring a single cue.
