# GSAP · anime.js · Three.js · Lenis · morphicons — Pattern Cookbook

Recipes for the framework-agnostic libraries motion-ui can install. For Framer
Motion (React-only), see `motion-patterns.md`; for timing, easing, and choreography decisions,
see `motion-craft.md`. Everything below works in **any** JS project — React, Vue, Svelte, Astro,
or vanilla — because these animate the DOM/canvas directly, not a component tree.

## Which library for the job

| Need | Pick | Why |
| --- | --- | --- |
| React component motion — layout, gestures, mount/unmount | **Framer Motion** | Declarative, React-native. (see `motion-patterns.md`) |
| Timeline sequencing, scroll-scrubbing/pinning, SVG, "pro" feel | **GSAP** | Best-in-class timelines + ScrollTrigger; framework-agnostic. |
| Small bundle, simple property/SVG animation, stagger | **anime.js** | Lightweight, tiny API surface. |
| 3D, WebGL, particles, shaders, product viewers | **Three.js** | The category — 3D, not 2D UI motion. |
| Inertial "expensive" scroll feel under everything else | **Lenis** | A scroll *layer*, not an engine. Pairs with the above. |
| One icon becoming another (menu→close, play→pause) | **morphicons** | ~7 KB, zero deps. Too small a job for a real engine. |
| Cinematic scroll hero rendered ahead of time, not in real time | **scroll-world** (external) | Video scrubbing beats WebGL when the art has to look pre-rendered. Costs money — see below. |

Rule of thumb: **React UI → Framer Motion; scroll-driven or timeline-heavy → GSAP; light touch → anime.js; 3D → Three.js.** They compose, and Lenis sits under all of them. Worked composition recipes are at the bottom of this file.

---

## GSAP

```bash
npm install gsap            # core + all plugins (ScrollTrigger, etc.) are free
npm install gsap @gsap/react   # React: adds the useGSAP() hook
```

```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
```

### 1. Tween — to / from / fromTo
```js
gsap.to(".box", { x: 200, rotation: 360, duration: 1, ease: "power3.out" });
gsap.from(".hero", { y: 40, opacity: 0, duration: 0.6 });        // animate INTO current state
gsap.fromTo(".bar", { scaleX: 0 }, { scaleX: 1, transformOrigin: "left", duration: 0.8 });
```

### 2. Timeline (sequencing)
```js
const tl = gsap.timeline({ defaults: { ease: "power2.out", duration: 0.5 } });
tl.from(".title", { y: 30, opacity: 0 })
  .from(".subtitle", { y: 20, opacity: 0 }, "-=0.3")   // overlap 0.3s
  .from(".cta", { scale: 0.8, opacity: 0 }, "<");        // start with previous
```

### 3. Stagger
```js
gsap.from(".card", { y: 24, opacity: 0, duration: 0.5, stagger: 0.08 });
```

### 4. ScrollTrigger — reveal on scroll
```js
gsap.from(".feature", {
  scrollTrigger: { trigger: ".feature", start: "top 80%", toggleActions: "play none none reverse" },
  y: 50, opacity: 0, duration: 0.6,
});
```

### 5. ScrollTrigger — scrub + pin (parallax / progress)
```js
gsap.to(".panel", {
  scrollTrigger: { trigger: ".section", start: "top top", end: "+=1000", scrub: true, pin: true },
  xPercent: -100, ease: "none",
});
```

### 6. React — useGSAP hook (handles cleanup)
```tsx
import { useRef } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";
gsap.registerPlugin(useGSAP);

export function Hero() {
  const root = useRef<HTMLDivElement>(null);
  useGSAP(() => {
    gsap.from(".line", { y: 30, opacity: 0, stagger: 0.1 });   // selectors scoped to root
  }, { scope: root });
  return <div ref={root}><h1 className="line">…</h1></div>;
}
```
Animations created in **event handlers** must be wrapped so they get cleaned up:
```tsx
const { contextSafe } = useGSAP({ scope: root });
const onClick = contextSafe(() => gsap.to(".good", { rotation: 180 }));
```

### 7. Reduced motion — gsap.matchMedia()
```js
const mm = gsap.matchMedia();
mm.add("(prefers-reduced-motion: no-preference)", () => {
  gsap.from(".hero", { y: 40, opacity: 0, duration: 0.6 });   // only runs when motion is OK
});
```

---

## anime.js (v4)

> **v4 is a breaking change from v3.** v4 uses **named ESM exports** (`import { animate } from 'animejs'`),
> not a default export. Do not generate v3 `anime({ targets })` syntax.

```bash
npm install animejs
```

```js
import { animate, createTimeline, stagger, onScroll } from "animejs";
```

### 1. Animate
```js
animate(".box", { x: "17rem", rotate: "1turn", duration: 800, ease: "outExpo" });
// targets: CSS selector, DOM node, NodeList, or JS object.
```

### 2. Stagger
```js
import { animate, stagger } from "animejs";
animate(".square", { x: "17rem", scale: stagger([1, 0.1]), delay: stagger(100) });
```

### 3. Timeline
```js
import { createTimeline } from "animejs";
const tl = createTimeline({ defaults: { duration: 600, ease: "outQuad" } });
tl.add(".title", { y: [30, 0], opacity: [0, 1] })
  .add(".subtitle", { y: [20, 0], opacity: [0, 1] }, "-=300")   // 300ms overlap
  .add(".cta", { scale: [0.8, 1], opacity: [0, 1] });
```
(Array values like `y: [30, 0]` mean **from → to**.)

### 4. Scroll-driven
```js
import { animate, onScroll } from "animejs";
animate(".reveal", {
  y: [40, 0], opacity: [0, 1],
  autoplay: onScroll({ container: "body", enter: "bottom top", sync: true }),
});
```

### 5. SVG line-drawing
```js
import { animate, svg } from "animejs";
animate(svg.createDrawable(".path"), { draw: ["0 0", "0 1"], duration: 1500, ease: "inOutQuad" });
```

### 6. Reduced motion — gate the call
```js
const ok = !matchMedia("(prefers-reduced-motion: reduce)").matches;
if (ok) animate(".hero", { y: [40, 0], opacity: [0, 1], duration: 600 });
else document.querySelector(".hero")?.style.setProperty("opacity", "1");
```

---

## Three.js

```bash
npm install three                                         # vanilla
npm install three @react-three/fiber @react-three/drei    # React (declarative)
# add @types/three in TypeScript projects
```

### 1. Minimal scene (vanilla) — scene · camera · renderer · loop
```js
import * as THREE from "three";

const canvas = document.querySelector("#scene");
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / canvas.clientHeight, 0.1, 100);
camera.position.z = 4;

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));   // cap DPR — perf

const mesh = new THREE.Mesh(
  new THREE.IcosahedronGeometry(1, 0),
  new THREE.MeshStandardMaterial({ color: 0x6366f1, roughness: 0.3 }),
);
scene.add(mesh, new THREE.AmbientLight(0xffffff, 0.6));
const key = new THREE.DirectionalLight(0xffffff, 1.2); key.position.set(3, 3, 3); scene.add(key);

const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
renderer.setAnimationLoop(() => {
  if (!reduce) mesh.rotation.y += 0.01;   // pause idle spin for reduced-motion
  renderer.render(scene, camera);
});
```

### 2. Resize + cleanup (SPA — must dispose to avoid GPU leaks)
```js
function onResize() {
  camera.aspect = canvas.clientWidth / canvas.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
}
addEventListener("resize", onResize);

// teardown (route change / component unmount):
function dispose() {
  renderer.setAnimationLoop(null);
  removeEventListener("resize", onResize);
  mesh.geometry.dispose();
  mesh.material.dispose();
  renderer.dispose();
}
```

### 3. React — @react-three/fiber (declarative)
```tsx
"use client";                                   // Next.js App Router
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Environment } from "@react-three/drei";
import { useRef } from "react";
import type { Mesh } from "three";

function Blob() {
  const ref = useRef<Mesh>(null);
  useFrame((_, dt) => { if (ref.current) ref.current.rotation.y += dt * 0.5; });
  return (
    <mesh ref={ref}>
      <icosahedronGeometry args={[1, 0]} />
      <meshStandardMaterial color="#6366f1" roughness={0.3} />
    </mesh>
  );
}

export function Scene() {
  return (
    <Canvas camera={{ position: [0, 0, 4], fov: 50 }} dpr={[1, 2]}>
      <ambientLight intensity={0.6} />
      <directionalLight position={[3, 3, 3]} intensity={1.2} />
      <Blob />
      <OrbitControls enablePan={false} />
      <Environment preset="city" />
    </Canvas>
  );
}
```
r3f disposes geometries/materials automatically on unmount — no manual cleanup needed.

---

## Lenis (smooth scroll)

> Lenis is a **layer, not an engine**. It changes how the page scrolls; something else still does
> the animating. Install it *alongside* GSAP or Framer Motion, never instead of one.

```bash
npm install lenis
```

### 1. Standalone
```js
import Lenis from "lenis";
const lenis = new Lenis({ autoRaf: true });
lenis.on("scroll", (e) => console.log(e.scroll, e.progress));
```

### 2. With GSAP ScrollTrigger (the usual pairing)
```js
const lenis = new Lenis();                          // no autoRaf — GSAP drives the loop
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));  // GSAP ticks in seconds, Lenis in ms
gsap.ticker.lagSmoothing(0);
```
Two rAF loops fighting each other is the classic Lenis bug. Pick one owner: either `autoRaf: true`
**or** `gsap.ticker.add`, never both.

### 3. React
```tsx
import { ReactLenis } from "lenis/react";
export default function Layout({ children }) {
  return <ReactLenis root>{children}</ReactLenis>;   // add options={{ autoRaf: false }} if GSAP drives it
}
```
`lenis/vue` and `lenis/snap` (scroll snapping) ship in the same package.

### 4. Programmatic scroll
```js
lenis.scrollTo("#pricing", { offset: -80, duration: 1.2 });
lenis.stop();   // while a modal is open
lenis.start();
```

### 5. Reduced motion
Lenis already disables its own smoothing and makes programmatic scrolls instant when
`prefers-reduced-motion: reduce` is set. Read `lenis.prefersReducedMotion` to make your own
scroll-linked animations agree with it rather than duplicating the media query.

### When not to reach for it
Lenis takes over native scrolling. That is fine on a marketing page and wrong almost everywhere
else: it interferes with find-in-page landing position, native scroll restoration, and some
assistive tech. Never stack it on top of CSS `scroll-behavior: smooth` (they fight). Do not put it
on a dashboard, a docs site, or anything with long scrollable data.

---

## morphicons (icon transitions)

A micro-engine for one job: turning one icon into another. Zero dependencies, ~7 KB gzip.
Reach for it when a real engine would be overkill (a hamburger becoming a close button, play
becoming pause) and hand-tweened SVG paths would look wrong.

```bash
npm install morphicons
```

### React
```tsx
import { MorphIcon } from "morphicons/react";
import { Menu, X } from "lucide";

<button onClick={() => setOpen((o) => !o)} aria-label={open ? "Close menu" : "Open menu"}>
  <MorphIcon icon={open ? X : Menu} spring="snappy" />
</button>
```

### Vanilla / DOM
```js
import { createMorph } from "morphicons/dom";
const m = createMorph(pathEl, Menu);
m.morphTo(X, "snappy");
```

Icons from Lucide, Tabler, Heroicons (outline), Iconoir and other stroke sets share a 24×24 grid,
so any pair morphs. Rotation is solved in closed form rather than tweened blindly, which is why
`arrow-right → arrow-down` reads as a rotation instead of a smear. Morphs are interruptible, and
progress can be driven manually for drag or scroll scrubbing.

**Rules:** the icon is decoration, so the accessible name lives on the `<button>`, not the SVG.
Gate the animation yourself under reduced motion (swap the icon at full progress instead of
morphing). Pin the version — the project is young and the API is still moving.

---

## Composing: GSAP scrub → Three.js camera

The scroll-driven 3D hero is not a fifth library, it is these three cooperating: **GSAP owns
progress, Three.js owns the world, Lenis owns the feel.** The render loop only ever *reads* state.

```js
const state = { p: 0 };

gsap.to(state, {
  p: 1,
  ease: "none",
  scrollTrigger: { trigger: "#world", start: "top top", end: "+=3000", scrub: 1, pin: true },
});

renderer.setAnimationLoop(() => {
  camera.position.z = 8 - state.p * 6;      // fly in as the section scrubs
  camera.rotation.y = state.p * Math.PI * 0.25;
  renderer.render(scene, camera);
});
```

Why tween an intermediate object instead of the camera directly: ScrollTrigger fires on scroll
events, the renderer runs on rAF. Writing camera properties straight from the tween couples the
two clocks and stutters on fast scroll. Tween a number, read it in the loop.

In `@react-three/fiber`, keep the same shape — write progress into a `useRef` from ScrollTrigger
and read it in `useFrame`. Never call `setState` from a scroll handler to move a camera; that is a
React re-render per frame.

`ease: "none"` is not optional on a scrubbed tween. Any other ease double-eases against the
scroll position and feels like lag.

---

## Pre-rendered scroll (scroll-world) — external, and it costs money

When the hero has to look rendered rather than real-time (clay dioramas, product flythroughs,
Apple-style scroll journeys), the technique is not WebGL at all: generate the frames ahead of
time and scrub a video with scroll position. [`oso95/scroll-world`](https://github.com/oso95/scroll-world)
(MIT) automates that whole pipeline — AI scene stills, camera-flight clips, frame-identical
connectors between scenes, and a vanilla scrub player.

```
/plugin marketplace add oso95/scroll-world
```

**Say all of this before suggesting it**, because none of it is recoverable after the fact:

- It renders through paid AI video backends (Monid / Higgsfield credits). Real money per clip, and
  the mobile 9:16 chain roughly doubles it. Get an explicit budget approval first.
- It needs `ffmpeg`, Python 3 + Pillow, and those CLIs authenticated. Check before promising.
- The output is video, so it is heavy. Lazy-load, serve as blob URLs for seekability, and always
  ship a static poster fallback for reduced motion and for the first paint.

Real-time Three.js is the right answer whenever the scene must respond to input, carry live data,
or ship without a render budget. Reach for scroll-world only when the art direction genuinely
cannot be reached in real time.

---

## Quality bar (apply to every animation, all libraries)
- **Reduced motion** — honor `prefers-reduced-motion: reduce`: skip or shorten motion, and pause idle
  loops (Three.js auto-spin, infinite tweens). Never leave an always-moving element for these users.
- **Transform/opacity only** for 2D — animate `x/y/scale/rotate` + `opacity` (GPU-composited), not
  `width/height/top/left`.
- **Three.js perf** — cap `setPixelRatio` at ~2; dispose geometry/material/renderer on teardown; a
  static hero doesn't need a render loop (render once).
- **Accessibility** — 3D canvases and decorative SVG animation are non-semantic: add a text/`aria`
  fallback, and never hide essential content behind an animation.
- **Match the project's tokens** — read `tailwind.config.*` / global CSS for colors, don't invent them.

## Composing with sibling skills
- Duration, easing, and stagger decisions → `motion-craft.md` in this same folder.
- Palette, typography, style direction → **ui-ux-pro-max** skill.
- shadcn/ui component scaffolds → **ui-styling** skill, then layer motion on top.
