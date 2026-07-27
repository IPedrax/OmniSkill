---
name: motion-ui
description: "Install the right animation library into a compatible project and build professional, animated UI/UX. Supports four engines: Framer Motion (the `motion` package, React declarative motion), GSAP (timelines + ScrollTrigger, any framework), anime.js v4 (lightweight, any framework), and Three.js (3D/WebGL, `@react-three/fiber` in React). Detects stack + package manager and picks a usable engine before installing — GSAP/anime.js/Three.js work in React, Next, Vite, Vue, Svelte, Astro, or vanilla; Framer Motion is React-only. Sources components in hybrid mode: 21st.dev Magic MCP when connected, otherwise built-in recipes. Two control modes: confirm-each-step (default) and --auto (opt-in end-to-end). Actions: animate, add motion, add framer motion, add gsap, add anime.js, add three.js, scroll animation, 3D scene, WebGL, make it professional, polish UI, design landing page, build animated components, motion-ui. Triggers: 'add animations', 'install framer motion', 'install gsap', 'use anime.js', 'add three.js / a 3D scene', 'scroll-triggered animation', 'make this look professional', 'animate this', 'use 21st.dev', '--auto'."
---

# motion-ui — Animated, Professional UI with Framer Motion · GSAP · anime.js · Three.js

Turns a plain JS project into a polished, animated interface. It (1) verifies the project can host
the right animation engine, (2) installs it, and (3) builds professional components, sourcing from
**21st.dev** (Magic MCP when available, built-in patterns otherwise). Four engines are supported so
the skill fits any stack and any job — 2D UI motion, scroll storytelling, or 3D. The user stays in
control by default; a single `--auto` flag hands the whole job to the AI.

## The four engines

| Engine | Package(s) | Stack | Best for |
| --- | --- | --- | --- |
| **Framer Motion** | `motion` | **React only** | Declarative component motion — layout, gestures, mount/unmount. |
| **GSAP** | `gsap` (+ `@gsap/react`) | Any JS project | Timelines, scroll-scrubbing/pinning (ScrollTrigger), SVG, "pro" sequencing. |
| **anime.js** | `animejs` (v4) | Any JS project | Lightweight property/SVG animation, stagger, small bundle. |
| **Three.js** | `three` (+ `@react-three/fiber`, `@react-three/drei`) | Any JS project | 3D / WebGL scenes, particles, shaders, product viewers. |

They compose (GSAP driving a Three.js camera; Framer Motion wrapping an r3f `<Canvas>`). Full recipes:
`references/motion-patterns.md` (Framer Motion) and `references/animation-libraries.md` (GSAP · anime.js · Three.js).

## When to use

Use when the user wants to add motion/animation, "make it look professional," build a polished landing
page or component, add a scroll-triggered effect or a 3D scene, or explicitly names Framer Motion,
GSAP, anime.js, Three.js, or 21st.dev. Also triggers on `--auto` for end-to-end autonomous UI work.

**Skip** for: pure backend work and non-JS projects (no `package.json`).

## Control modes

| Mode | How to enter | Behavior |
| --- | --- | --- |
| **Confirm** (default) | normal request | Propose each step — engine choice, install, design direction, every component — and **wait for approval** before acting. |
| **Auto** | user includes `--auto` (or says "full auto / you decide everything") | No stops: detect → pick engine → install → design → generate & apply → report. Still respects the compatibility gate and reduced-motion. |

Always state which mode you're in at the start. In Confirm mode, never install or write files without an
explicit yes. Switching to Auto requires the user's flag/phrase — never assume it.

## Workflow

### Step 1 — Detect compatibility (always, both modes)
Run the detector and read its JSON verdict:

```bash
node "<skills>/motion-ui/scripts/detect-stack.mjs" "<projectDir>"
```

It reports: `compatible`, `framework` (next / remix / astro / vue / svelte / angular / vite / react /
vanilla), `hasReact`, `hasTypeScript`, `hasTailwind`, `packageManager`, `warnings`, and a **`libraries`**
map. Each entry (`framer-motion`, `gsap`, `anime`, `three`) has `usable`, `installed`, `install` (the
exact command for this project's package manager, or `null` if already installed), `import`, and a `note`.

- If `compatible: false` → **stop**: there's no `package.json` (not a JS project). Don't install.
- `framer-motion.usable` is `false` on non-React stacks — steer the user to GSAP or anime.js instead.
- If the chosen engine's `installed: true` → skip Step 3, note its `import`, go to Step 4.

### Step 2 — Choose the engine
Pick from the user's ask; if unspecified, choose by the job (see the table above and the decision matrix
in `references/animation-libraries.md`):

- React component motion (layout/gesture/mount) → **Framer Motion** (if `hasReact`).
- Scroll-triggered, pinned, or timeline-heavy → **GSAP**.
- Simple, lightweight property/SVG animation → **anime.js**.
- 3D / WebGL → **Three.js**.

Only `usable: true` engines are eligible. In Confirm mode, state your pick and why, and confirm before
installing. Multiple engines can be installed if the design needs both (e.g. Framer Motion for UI +
Three.js for a hero).

### Step 3 — Install the chosen engine
Use that library's `install` string from the detector **verbatim** — it already includes the right
package manager and the React extras (`@gsap/react`, `@react-three/fiber`+`drei`, `@types/*`).

- **Confirm mode:** show the exact command and the detected stack; ask before running.
- **Auto mode:** run it directly.

Notes baked into the detector: `motion` imports from `motion/react` (legacy `framer-motion` keeps its
path); `animejs` is **v4** (named exports — `import { animate } from 'animejs'`, not v3's default export).
Verify the install succeeded (dependency appears in `package.json`) before proceeding.

### Step 4 — Source professional components (hybrid 21st.dev)
1. Detect the **Magic MCP**: `ToolSearch` query `magic 21st component ui`. If relevant tools exist, use
   them to fetch/generate components, then adapt the result to the project's stack, Tailwind tokens, and
   the chosen engine's import path.
2. If no Magic MCP: announce the fallback and build from the reference cookbooks —
   `references/animation-libraries.md` (GSAP · anime.js · Three.js) or `references/21st-components.md`
   + `references/motion-patterns.md` (Framer Motion).
3. For palette / typography / overall style direction, compose with the **ui-ux-pro-max** and
   **ui-styling** skills rather than re-deriving them.

### Step 5 — Apply & verify
- **Confirm mode:** present each component (or a small batch) for approval before writing.
- **Auto mode:** write the files, wire them in, and report what changed.
- Always: honor `prefers-reduced-motion` (pause idle loops too — Three.js auto-spin, infinite tweens),
  animate transform/opacity for 2D, match existing tokens, keep components accessible (3D/decorative SVG
  needs a text/`aria` fallback). For Three.js, dispose GPU resources on teardown and cap pixel ratio.
  Run the project's typecheck/lint if available; offer to start the dev server (or use the `/run` skill).

## Hard rules
- **Never skip Step 1.** No install without reading the detector's verdict.
- **Never install in Confirm mode without explicit approval.**
- **Auto mode is opt-in only** — require the `--auto` flag or an explicit "you decide everything."
- **Match engine to stack** — only install an engine whose `usable: true`. Framer Motion never goes into
  a non-React project; offer GSAP/anime.js/Three.js there instead.
- Respect reduced-motion in every component, in both modes.
- Don't invent colors/fonts — read `tailwind.config.*` and global CSS first, or pull from sibling skills.

## Files
- `scripts/detect-stack.mjs` — stack + per-engine usability + package-manager detector (run first).
- `references/motion-patterns.md` — Framer Motion recipe cookbook + accessibility + perf rules.
- `references/animation-libraries.md` — GSAP · anime.js · Three.js recipe cookbook + which-engine matrix.
- `references/21st-components.md` — Magic MCP sourcing flow + built-in 21st-style fallback components.
