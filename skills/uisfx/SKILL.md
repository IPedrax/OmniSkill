---
name: uisfx
description: Interface sound effects. OmniSkill Design crew — wires the uisfx library into a project: 78 semantic cues across 12 sonic packs, synthesized locally, with the consent, autoplay, and accessibility rules that keep UI sound from being hostile.
disable-model-invocation: true
---

# UI SFX

> The one channel nobody designs · OmniSkill Design crew

Sound is the last unclaimed dimension in most interfaces, and the easiest one to get badly wrong. This skill adds it deliberately: semantic cues tied to real state changes, off by default, and never the only way something is communicated.

Not bundled — it installs [`uisfx`](https://github.com/romainsimon/uisfx) (MIT code, CC0 audio) into the project.

## Use it

```bash
npm install uisfx
```

```ts
import { createUISFX } from 'uisfx'

const ui = createUISFX({ pack: 'minimal' })

// Browsers block audio until the user has interacted. Call this from a real
// click or tap, never on load, never from an effect that runs at mount.
await ui.unlock()

ui.play('success')

const task = ui.play('loading')   // loops keep going until you stop them
task?.stop()
```

Other API worth knowing: `ui.setPack(name)` swaps the whole personality without touching a single call site, `ui.setVolume(0–1)`, `ui.setEnabled(boolean)` for the user's mute toggle, `ui.preload(signal?)`, and `ui.stopAll()`.

For markup-driven wiring rather than imperative calls:

```ts
import { bindUISFX } from 'uisfx'
const { player, unbind } = bindUISFX()
```
```html
<button data-uisfx="success" data-uisfx-pack="soft">Save</button>
```

The Web runtime is ~12 kB and synthesizes locally, so a normal web install downloads **no audio at all**. The 936 rendered MP3/Ogg files at `uisfx/sounds/{pack}/{cue}.ogg` exist for React Native, Swift, Kotlin, and anywhere else without Web Audio. Do not copy that directory into a web bundle; the whole library is 3.8 MB of Ogg and you need none of it.

## Picking cues and a pack

**Cues are semantic, not literal.** Call `play('success')`, never `play('the-nice-ding')`. There are 78 across 13 categories (input, selection, navigation, editing, movement, communication, feedback, progress, loops, media, system, reward, commerce), and six of them are loops: `loading`, `processing`, `recording`, `connecting`, `scanning`, `streaming`.

Because the naming is semantic, choosing a pack is a **branding** decision made once, not a per-sound decision made 40 times. Twelve ship: `minimal`, `soft`, `glass`, `arcade`, `mechanical`, `organic`, `dreamy`, `scifi`, `rubber`, `cinematic`, `studio`, `zen`. Pick from the product's voice, not from what sounds nice in isolation:

| Product | Reasonable packs |
| --- | --- |
| SaaS, dashboard, B2B tool | `minimal`, `soft`, `studio` |
| Consumer app, onboarding, gamified | `arcade`, `rubber`, `organic` |
| Editorial, premium, portfolio | `glass`, `cinematic`, `zen` |
| Developer tooling, terminal-adjacent | `mechanical`, `scifi` |

Audition against the existing visual personality. A `cinematic` pack under a dense settings table is the audio equivalent of a bounce easing on a form control.

## House rules

**Off by default. Always.** Sound is the only interface channel that reaches people who are not looking at the screen: someone in a meeting, on a call, next to a sleeping baby, in a shared office. Ship it disabled, expose a visible toggle, persist the choice, and read it before the first `play()`. "Opt out" is the wrong default here even though it is the right default almost everywhere else.

**Unlock from a gesture, never at mount.** `await ui.unlock()` inside a `useEffect` on page load fails silently in every browser and leaves the first few cues mute. Tie it to the same interaction that turns sound on.

**Only sound things the user caused, or things that finished.** A click, a submit, a completed upload, an error, a purchase. Never an arrival, never a scroll position, never a component mounting, never an ambient loop. If the user did not act and nothing resolved, there is nothing to say.

**Hover is the trap.** A hover cue fires continuously as the pointer crosses a dense layout, and keyboard users get focus *and* hover on the same control. Use one or the other, and prefer skipping hover entirely outside of a deliberately playful product.

**Stop every loop you start.** A `loading` loop that outlives its request is this library's worst failure mode, and it happens on the error path, not the happy one. Stop it in `finally`, and on unmount, and on route change.

**Sound is never the only channel.** Anything a cue communicates must also be visible: the error toast, the checkmark, the disabled state. This is not only accessibility, it is the muted majority of your users. Screen reader users in particular already have a full audio channel in use, and competing with it is worse than silence.

**Keep it quiet.** Default around `0.3`. Interface sound sits under speech and media, not beside it. If a cue is audible over a video the user is watching, it is too loud.

**One cue per interaction.** Success plus selection plus navigation on a single confirm button reads as a malfunction.

## Where it sits in the crew

Last, alongside `motion-ui`. Direction comes from `ui-ux-pro-max`, the interface from `frontend-design`, motion from `motion-ui`, and sound after all of it. Cues should map onto the same moments that already have motion: the states worth animating are exactly the states worth sounding, and the ones that are not worth animating are not worth sounding either.

If motion has not been settled yet, settle it first. Sound layered over an interface with no rhythm just makes the arrhythmia audible.

## Attribution

[`uisfx`](https://github.com/romainsimon/uisfx) by Romain Simon. Runtime code **MIT**; the 936 generated sounds are **CC0 1.0** (public domain), so shipping them commercially needs no attribution. Nothing is vendored here; the package installs from npm.
