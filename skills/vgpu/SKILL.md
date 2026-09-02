---
name: vgpu
description: WebGPU without the boilerplate. OmniSkill Design crew — wires Vercel's vgpu into a project: typed WGSL imports, one explicit Gpu context, fullscreen effects and compute passes, and the same shader code running in the browser, in headless Node, and against a deterministic mock in CI.
disable-model-invocation: true
---

# vgpu

> Shaders you can unit-test · OmniSkill Design crew

WebGPU's own API is a pile of adapters, devices, bind group layouts and pipeline descriptors before a single pixel moves. vgpu keeps the explicitness and removes the ceremony: one `Gpu` handle passed to every entry point, `.wgsl` files that import and export like TypeScript modules, and frames where passes and draws are calls you can read.

Not bundled — it installs [`vgpu`](https://www.npmjs.com/package/vgpu) from npm (MIT, Vercel Labs).

## Use it

```bash
pnpm add vgpu
pnpm add -D @webgpu/types
```

```ts
import { clock, effect, frameLoop, init, surface } from 'vgpu'
import waveShader from './wave.wgsl'

const gpu = await init()
const view = surface(gpu, canvas, { dpr: [1, 2] })
const wave = effect(gpu, waveShader, { set: { speed: 2 } })
const time = clock(gpu)

frameLoop(gpu, (frame) => {
  wave.set({ time: time.time })       // uniforms addressed by their WGSL names
  frame.pass(view, wave)
})
```

`init()` acquires the adapter and device and returns the single context; everything else takes it first. `surface` wraps a canvas and keeps its size current, clamping DPR. `effect` compiles a shader into a fullscreen pass. There is no hidden global state and no scene graph — `frame.pass(target, thing)` is the whole model.

Shaders compose as modules, resolved at build time with no codegen:

```wgsl
import { hash2 } from "@vgpu/wgsl-std/hash";

export fn grain(uv: vec2f, time: f32) -> f32 {
  return hash2(uv * time).x;
}
```

`@vgpu/wgsl-std` ships math, color, sampling, noise and hash as named exports.

## Three runtimes, one API

This is the reason to pick it over writing WebGPU by hand:

| Import | Runs on | For |
| --- | --- | --- |
| `vgpu` | The browser | Production |
| `vgpu/node` | Headless Dawn | Rendering to a buffer, `await target.read()` for pixels |
| `vgpu/mock` | A deterministic software adapter | Tests and CI, no GPU present |

So a shader can have a test that asserts on actual pixel values, and that test runs on a CI box with no graphics hardware. Write it — the whole point of the mock adapter is that "the shader still compiles and still outputs what it did last week" becomes a normal assertion instead of a screenshot someone eyeballs.

## The CLI is agent-facing

Docs and the example gallery ship inside the package and answer offline. Prefer these over guessing at an API:

```bash
npx vgpu docs find effect        # search the shipped reference
npx vgpu docs cat getting-started.md
npx vgpu examples search "raymarching"
npx vgpu examples pull <id> --out ./example   # complete source, no clone
npx vgpu check                   # validate shaders
npx vgpu doctor                  # diagnose the environment
```

There is also `npx vgpu mcp` for a local stdio MCP server versioned to the installed package, and a public read-only endpoint at `https://vgpu.sh/api/mcp`. `vgpu.sh/llms.txt` and `agents.md` exist for the same reason.

## House rules

**Check the target before writing the shader.** WebGPU is not universal — Safari and older browsers need a fallback, and there is no shader-level workaround for its absence. Decide up front whether this is an enhancement over a static image or a hard requirement, and say which.

**Reach for the playbook's defaults on the first draft, not after profiling.** `npx vgpu docs cat performance-playbook.docs.md` is written as default shapes: `bundle()` static draws once and replay with `p.bundles(...)`, pre-warm pipelines with `compile()` before the first visible frame, `set()` in place rather than rebuilding uniforms, instance instead of looping draws. Retrofitting these costs more than starting with them.

**Verifying visual output in a headless environment is its own problem.** Headless Chrome does not expose WebGPU by default and silently gives you a black canvas, which reads as a broken shader. On Linux use SwiftShader through `agent-browser --webgpu --headed` (it starts Xvfb when `DISPLAY` is missing), allow several seconds and a couple of frames before capturing anything heavy, and confirm with `agent-browser doctor --webgpu --headed` before believing a black frame. Or skip the browser: render in `vgpu/node` and read the pixels back.

**Mind the budget you are spending.** A complete fullscreen effect is ~25 KB gzipped and unused declarations are pruned — that is a real number, enforced in CI upstream, and it is worth not undoing with a dependency that pulls in a whole engine beside it.

## Where it sits in the crew

Next to `algorithmic-art`, and the choice between them is the runtime, not the aesthetic. p5.js is a sketch — fast to write, CPU-bound, right for generative work whose output is an image or a loop. vgpu is the GPU: fullscreen effects, post-processing, particle counts that p5 cannot reach, and compute passes that are not drawing at all.

Against `motion-ui`: that crew animates an interface, and Three.js there is for a 3D *scene* — meshes, cameras, lights. vgpu is a shader surface. A hero background, a transition effect, a fluid or noise field is vgpu; a product model the user orbits is Three.js. The two do meet — vgpu's WGSL modules can be flattened into three.js TSL node materials via the `three-tsl` example's helper, which is copied into the project rather than imported.

Direction still comes first. A shader is the most expensive way to discover that the design was undecided.

## Attribution

[vgpu](https://github.com/vercel-labs/vgpu) by Vercel Labs · [vgpu.sh](https://vgpu.sh) · **MIT**. Nothing is vendored here; the package installs from npm.
