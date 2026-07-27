# GSAP · anime.js · Three.js — Pattern Cookbook

Recipes for the three framework-agnostic libraries motion-ui can install. For Framer
Motion (React-only), see `motion-patterns.md`. All three below work in **any** JS project —
React, Vue, Svelte, Astro, or vanilla — because they animate the DOM/canvas directly, not a
component tree.

## Which library for the job

| Need | Pick | Why |
| --- | --- | --- |
| React component motion — layout, gestures, mount/unmount | **Framer Motion** | Declarative, React-native. (see `motion-patterns.md`) |
| Timeline sequencing, scroll-scrubbing/pinning, SVG, "pro" feel | **GSAP** | Best-in-class timelines + ScrollTrigger; framework-agnostic. |
| Small bundle, simple property/SVG animation, stagger | **anime.js** | Lightweight, tiny API surface. |
| 3D, WebGL, particles, shaders, product viewers | **Three.js** | The category — 3D, not 2D UI motion. |

Rule of thumb: **React UI → Framer Motion; scroll-driven or timeline-heavy → GSAP; light touch → anime.js; 3D → Three.js.** They compose — GSAP can drive a Three.js camera; Framer Motion can wrap an r3f `<Canvas>`.

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
- Palette, typography, style direction → **ui-ux-pro-max** skill.
- shadcn/ui component scaffolds → **ui-styling** skill, then layer motion on top.
