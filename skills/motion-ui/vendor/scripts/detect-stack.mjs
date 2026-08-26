#!/usr/bin/env node
/**
 * motion-ui stack detector.
 * Inspects the project at CWD (or argv[2]) and prints a JSON report describing
 * which animation libraries can be installed and how.
 *
 * Libraries covered:
 *   - framer-motion (`motion`)  — React only.
 *   - gsap                      — any JS project (extra `@gsap/react` hook in React).
 *   - anime  (`animejs` v4)     — any JS project.
 *   - three                     — any JS project (extra r3f + drei in React).
 *   - lenis                     — any JS project. Smooth-scroll layer, not an engine on its own.
 *   - morphicons                — any JS project. Icon-to-icon SVG morphing (micro-engine).
 *
 * Usage: node detect-stack.mjs [projectDir]
 * Exit codes: 0 = report printed (check JSON `.compatible`), 1 = no/invalid package.json.
 */
import { readFileSync, existsSync } from "node:fs";
import { join, resolve } from "node:path";

const dir = resolve(process.argv[2] || process.cwd());
const pkgPath = join(dir, "package.json");

if (!existsSync(pkgPath)) {
  console.log(JSON.stringify({
    compatible: false,
    reason: "No package.json found — not a JS/TS project. These libraries install via npm.",
    dir,
  }, null, 2));
  process.exit(1);
}

let pkg;
try {
  pkg = JSON.parse(readFileSync(pkgPath, "utf8"));
} catch (e) {
  console.log(JSON.stringify({ compatible: false, reason: `package.json is not valid JSON: ${e.message}`, dir }, null, 2));
  process.exit(1);
}

const deps = { ...(pkg.dependencies || {}), ...(pkg.devDependencies || {}) };
const has = (name) => Object.prototype.hasOwnProperty.call(deps, name);

// --- Package manager (by lockfile, then packageManager field) ---
let pm = "npm";
if (existsSync(join(dir, "pnpm-lock.yaml"))) pm = "pnpm";
else if (existsSync(join(dir, "yarn.lock"))) pm = "yarn";
else if (existsSync(join(dir, "bun.lockb")) || existsSync(join(dir, "bun.lock"))) pm = "bun";
else if (existsSync(join(dir, "package-lock.json"))) pm = "npm";
else if (typeof pkg.packageManager === "string") pm = pkg.packageManager.split("@")[0];

// `add <pkgs>` for the detected package manager.
const add = (pkgs) => `${{ npm: "npm install", pnpm: "pnpm add", yarn: "yarn add", bun: "bun add" }[pm] || "npm install"} ${pkgs}`;

// --- Stack signals ---
const hasReact = has("react") || has("react-dom");
const hasTypeScript = has("typescript") || existsSync(join(dir, "tsconfig.json"));
const hasTailwind = has("tailwindcss");

// --- Framework detection (label only; every framework can host gsap/anime/three) ---
let framework = null;
if (has("next")) framework = "next";
else if (has("@remix-run/react") || has("@remix-run/node")) framework = "remix";
else if (has("astro")) framework = "astro";
else if (has("nuxt") || has("vue")) framework = "vue";
else if (has("@sveltejs/kit") || has("svelte")) framework = "svelte";
else if (has("@angular/core")) framework = "angular";
else if (has("vite")) framework = "vite";
else if (hasReact) framework = "react";
else framework = "vanilla";

// --- Per-library plans ---------------------------------------------------
// framer-motion: React-only. Legacy `framer-motion` import differs from current `motion`.
const framerInstalled = has("motion") || has("framer-motion");
const framerLegacy = has("framer-motion") && !has("motion");
const framer = {
  usable: hasReact,
  installed: framerInstalled,
  install: hasReact ? (framerInstalled ? null : add("motion")) : null,
  import: framerLegacy ? "framer-motion" : "motion/react",
  note: hasReact
    ? "Declarative React motion: layout, gestures, AnimatePresence."
    : "React-only — not usable here. Use gsap or anime instead for this stack.",
};

// gsap: framework-agnostic. `@gsap/react` adds the useGSAP() hook in React.
const gsapInstalled = has("gsap");
const gsapPkgs = ["gsap", ...(hasReact && !has("@gsap/react") ? ["@gsap/react"] : [])];
const gsap = {
  usable: true,
  installed: gsapInstalled,
  install: gsapInstalled ? (hasReact && !has("@gsap/react") ? add("@gsap/react") : null) : add(gsapPkgs.join(" ")),
  import: "gsap",
  reactHook: hasReact ? "@gsap/react → useGSAP()" : null,
  note: "Timelines, ScrollTrigger, SVG. Best for complex sequencing / scroll work. Plugins (ScrollTrigger, etc.) ship free in the core package.",
};

// anime v4: framework-agnostic, named ESM exports.
const animeInstalled = has("animejs");
const anime = {
  usable: true,
  installed: animeInstalled,
  install: animeInstalled ? null : add(hasTypeScript ? "animejs @types/animejs" : "animejs"),
  import: "animejs",
  note: "v4 named exports: import { animate, createTimeline, stagger, onScroll } from 'animejs'. Lightweight; great for simple property/SVG animation.",
};

// three: framework-agnostic. React uses @react-three/fiber + drei.
const threeInstalled = has("three");
const threePkgs = hasReact
  ? ["three", "@react-three/fiber", "@react-three/drei", ...(hasTypeScript ? ["@types/three"] : [])]
  : ["three", ...(hasTypeScript ? ["@types/three"] : [])];
const three = {
  usable: true,
  installed: threeInstalled,
  install: threeInstalled ? null : add(threePkgs.join(" ")),
  import: "three",
  reactRenderer: hasReact ? "@react-three/fiber (<Canvas>, useFrame) + @react-three/drei" : null,
  note: "3D / WebGL scenes, particles, shaders. Different category from 2D UI motion.",
};

// lenis: framework-agnostic smooth-scroll layer. Pairs with an engine, never replaces one.
const lenisInstalled = has("lenis");
const lenis = {
  usable: true,
  installed: lenisInstalled,
  install: lenisInstalled ? null : add("lenis"),
  import: hasReact ? "lenis/react" : "lenis",
  note: "Smooth-scroll layer, not a standalone engine — install alongside gsap/framer-motion, not instead of. Subpaths: lenis/react, lenis/vue, lenis/snap. Disables its own smoothing under prefers-reduced-motion.",
};

// morphicons: framework-agnostic icon-to-icon SVG morphing. Zero deps, ~7 KB gzip.
const morphiconsInstalled = has("morphicons");
const morphicons = {
  usable: true,
  installed: morphiconsInstalled,
  install: morphiconsInstalled ? null : add("morphicons"),
  import: hasReact ? "morphicons/react" : "morphicons/dom",
  note: "Micro-engine for icon transitions only (menu→close, play→pause). Works with Lucide/Tabler/Heroicons/Iconoir paths. Pin the version — the project is young.",
};

const libraries = { "framer-motion": framer, gsap, anime, three, lenis, morphicons };

// --- Compatibility verdict ----------------------------------------------
// Any valid JS project can host gsap/anime/three, so it's always compatible.
const compatible = true;
const warnings = [];
if (!hasReact) {
  warnings.push(`No React detected (${framework}). Framer Motion is unavailable — gsap, anime, three, lenis, and morphicons all work here.`);
}
if (framework === "astro" && !hasReact) {
  warnings.push("Astro without React: run gsap/anime/three inside a client-side script or island (client:load).");
}
const reason = hasReact
  ? `Detected ${framework}${framework === "react" ? "" : " + React"}. Every library is available.`
  : `Detected ${framework}. gsap, anime, three, lenis, and morphicons are available; Framer Motion is React-only.`;

console.log(JSON.stringify({
  compatible,
  reason,
  dir,
  framework,
  hasReact,
  hasTypeScript,
  hasTailwind,
  packageManager: pm,
  libraries,
  warnings,
}, null, 2));
