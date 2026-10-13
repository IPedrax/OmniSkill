---
name: tabler-icons
description: Icons for any interface, picked by meaning. OmniSkill Design crew. Searches the 5,184 MIT Tabler icons (outline, 1,054 also filled) by name, tag and category, then hands back clean inline SVG or the right component from @tabler/icons-react, -vue, -svelte and the other packages, so an interface gets one consistent icon set instead of hand-drawn or mixed ones.
disable-model-invocation: true
---

# tabler-icons

> One icon set, found by what it means · OmniSkill Design crew

[Tabler Icons](https://github.com/tabler/tabler-icons): 5,184 icons on a 24 px grid with a 2 px stroke, all `currentColor`, so they inherit text colour and dark mode for free. Not bundled: the set is the `@tabler/icons` npm package, unpacked once.

## Install once

```bash
mkdir -p ~/tools/tabler-icons
npm pack @tabler/icons --pack-destination /tmp
tar xzf /tmp/tabler-icons-*.tgz -C ~/tools/tabler-icons --strip-components=1
```

`TABLER_ICONS_HOME` overrides the path. Update by repeating it; `package.json` there holds the installed version.

## Find the icon

```bash
I="python3 ${CLAUDE_SKILL_DIR}/scripts/icons.py"
$I search "parking car"           # every word must match; best first
$I search "heart" --filled        # only icons that also come filled
$I search "chart" --category Charts
$I svg car --size 20 --stroke 1.5  # inline SVG, ready to paste
$I selftest
```

Each result line is `name  category  styles  component`. Search by what the icon must mean, not what it looks like ("download", not "arrow pointing down"), then look at two or three candidates before choosing; Tabler often has several near-matches (`trash`, `trash-x`, `trash-off`).

## Put it in the project

Use the package for the project's framework so only the icons used get bundled:

| Stack | Package | Usage |
|---|---|---|
| React / Next | `@tabler/icons-react` | `import { IconCar } from '@tabler/icons-react'` then `<IconCar size={20} stroke={1.5} />` |
| Vue | `@tabler/icons-vue` | same component names |
| Svelte | `@tabler/icons-svelte` (or `-svelte-runes`) | same component names |
| Solid, Preact, React Native, Astro | `@tabler/icons-solidjs`, `-preact`, `-react-native`, `-astro` | same component names |
| Plain HTML, email, a one-off page | none | paste the output of `icons.py svg` |
| Many icons on a static site | `@tabler/icons-sprite` | one `<use href>` per icon |

Filled variants are `Icon<Name>Filled` (`IconHeartFilled`). Install with the project's own package manager, not globally.

## House rules

**One set, one weight.** Pick a stroke (1.5 or 2) and a size scale once per project and keep it. Mixing Tabler with another icon family, or 1.5 with 2 strokes, is the fastest way to make an interface look assembled.

**Icons need words.** A button that is only an icon gets an accessible name (`aria-label` on the button); a decorative icon next to text gets `aria-hidden="true"`. Don't make users guess what an unlabelled icon means.

**`brand-*` icons are other companies' logos.** There are 376 (WhatsApp, Instagram, Pinterest and so on). Use them only to link to that service, as their brand guidelines allow; never as a project's own mark. A project's own logo is `logo-design`'s job.

## Where it sits in the crew

Inside `frontend-design` and `web-artifacts` builds, and `anydesign` specs that call for icons. `motion-ui` can animate them; `logo-design` makes marks, not icons.

## Source

[Tabler Icons](https://github.com/tabler/tabler-icons) by Paweł Kuna · **MIT**, installed from npm. `scripts/icons.py` is original to OmniSkill.
