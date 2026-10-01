---
name: slidev
description: Developer slide decks from Markdown. OmniSkill Design crew — Slidev's own Claude Code skill, bundled: slide syntax, layouts, click animations, live code with Monaco and Magic Move, Mermaid and LaTeX, presenter mode, and export to PDF, PPTX or a hosted SPA.
disable-model-invocation: true
---

# Slidev

> A deck that can run the code it is talking about · OmniSkill Design crew

A presentation framework built on Vite, Vue and Markdown. The deck is a `slides.md` file, which is the whole point: it diffs, it reviews, and code samples come from the real files rather than a screenshot taken three refactors ago.

The upstream skill is vendored **unmodified** at `vendor/`, maintained by the Slidev team.

## Load it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. Its reference tables point at `vendor/references/<topic>.md` — 53 of them, one per feature. Read the one you need; do not read the directory.

## Reach for it when

The deck has **code, diagrams or math** in it. That is the whole selection rule. Slidev's edge is `twoslash` type-checking a snippet as it renders, `magic-move` animating one version of a function into the next, `monaco-run` executing a sample live, and `<<< @/src/thing.ts` importing from the actual file so the slide cannot drift from the codebase.

For a deck with none of that — a client pitch, a board update, an all-hands — Slidev is a Vite project standing where a document should be. `pitch-deck` in the Finance crew writes the investor narrative and `canvas-design` produces a designed image; either beats a build step you have to explain to the person editing it.

## What the adapter adds

**Export needs a browser.** `pnpm add -D playwright-chromium` before `slidev export`, or PDF, PPTX and PNG all fail on a missing-browser error that reads like a Slidev bug and is not one. The vendored skill states this once, at the bottom of the export section; it is the single most common way a first deck fails.

**Pick the theme before writing slides, not after.** Themes redefine layouts, and a `two-cols` or `image-right` that was carrying a slide can land differently under a new one. Set `theme:` in the headmatter on slide one, and treat a later swap as a review pass over every slide, not a config change.

**Live code is a promise made to a room.** `monaco-run` executes in the browser during the talk, so anything it touches — network, timing, a package that assumes Node — is a failure with an audience watching. Keep runnable samples pure and fast, and put anything else in a plain highlighted block.

**The deck is a web app, so treat it like one.** It has a dev server, dependencies and a build. When it needs to look designed rather than default, that is the rest of this crew's job: `anydesign` to extract a direction from a reference deck, `ui-ux-pro-max` to choose type and palette, and the theme's own CSS to apply it. Slidev renders; it does not art-direct.

**Hosting is `slidev build` and static files.** It exports an SPA — any static host takes it. `seoMeta:` and `og-image.png` matter for a link that will be shared, and they are set in the headmatter, before the build, not after.

## Where it sits in the crew

Alongside `canvas-design`: both produce a finished visual artifact rather than an interface. Match the target — a printed or posted image is `canvas-design`, a shareable one-pager is `web-artifacts`, a talk is `slidev`.

The handoff worth knowing is from Finance: `pitch-deck` decides what the slides say and in what order, and stops there. If that deck is going to be delivered by a developer to developers, `slidev` is what renders it.

## Attribution

[Slidev](https://github.com/slidevjs/slidev) by Anthony Fu and contributors · [sli.dev](https://sli.dev) · **MIT**. The skill at `vendor/` is upstream's own, copied verbatim from `skills/slidev/` @ `a8d8ff7`. Send fixes upstream.
