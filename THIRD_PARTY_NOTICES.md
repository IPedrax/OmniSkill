# Third-party notices

OmniSkill itself is MIT (see [LICENSE](LICENSE)). Thirteen skills are **vendored verbatim** from upstream projects and remain under their own licenses. Each ships its license file alongside the code.

## Vendored

| Skill | Upstream | License | Location |
|---|---|---|---|
| `superpowers` | [obra/superpowers](https://github.com/obra/superpowers) @ `896224c` — Jesse Vincent | MIT | `skills/superpowers/vendor/` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills) — Matt Pocock (`grill-me` + `grilling`) | MIT | `skills/grill-me/vendor/` |
| `motion-ui` | [IPedrax/motion-ui](https://github.com/IPedrax/motion-ui) | MIT | `skills/motion-ui/vendor/` |
| `anydesign` | [uxKero/anydesign](https://github.com/uxKero/anydesign) @ `d81bd89` — Alan Ponce (v0.6.0, `examples/` omitted) | MIT | `skills/anydesign/vendor/` |
| `brag` | [latent-spaces/brag](https://github.com/latent-spaces/brag) @ `d06a77f` — Shunit Haviv Hakimi (`skills/brag-slim` only; the full `/brag` and its ende.app music are not included) | MIT | `skills/brag/vendor/` |
| `slidev` | [slidevjs/slidev](https://github.com/slidevjs/slidev) @ `a8d8ff7` — Anthony Fu (`skills/slidev`, 53 references) | MIT | `skills/slidev/vendor/` |
| `canvas-design` | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 | `skills/canvas-design/vendor/` |
| `web-artifacts` | [anthropics/skills](https://github.com/anthropics/skills) (`web-artifacts-builder`) | Apache-2.0 | `skills/web-artifacts/vendor/` |
| `slack-gif` | [anthropics/skills](https://github.com/anthropics/skills) (`slack-gif-creator`) | Apache-2.0 | `skills/slack-gif/vendor/` |
| `mcp-builder` | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 | `skills/mcp-builder/vendor/` |
| `frontend-design` | [anthropics/claude-plugins-public](https://github.com/anthropics/claude-plugins-public) | Apache-2.0 | `skills/frontend-design/vendor/` |
| `skill-creator` | [anthropics/claude-plugins-public](https://github.com/anthropics/claude-plugins-public) | Apache-2.0 | `skills/skill-creator/vendor/` |
| `ui-ux-pro-max` | bundled by the maintainer | see `skills/ui-ux-pro-max/vendor/` | `skills/ui-ux-pro-max/vendor/` |

All vendored copies are **unmodified**. Send fixes upstream, not here. OmniSkill's own adapter `SKILL.md` sits beside each `vendor/` directory and is the only file added.

### Fonts

`skills/canvas-design/vendor/canvas-fonts/` contains 54 TrueType fonts, each accompanied by its **SIL Open Font License (OFL)** text file. The OFL permits redistribution provided the license accompanies the fonts, which it does. The fonts are not sold or distributed standalone.

## Deliberately not vendored

| Skill | Reason |
|---|---|
| `xlsx`, `docx` | **Source-available and proprietary**, per [anthropics/skills](https://github.com/anthropics/skills). Redistribution inside an MIT plugin is not permitted, so these install separately. |
| `context7` | An MCP server rather than skill content. Cannot be bundled; the adapter offers to set it up. |
| `uisfx` | An npm **library**, not a skill. OmniSkill's `skills/uisfx/SKILL.md` is original work that teaches its use; [`uisfx`](https://github.com/romainsimon/uisfx) itself installs from npm (code MIT, the 936 generated sounds CC0 1.0). |
| `scrapling` | A **Python library and MCP server**, not skill content. OmniSkill's `skills/scrapling/SKILL.md` and `scripts/web.py` are original work that build on it; [Scrapling](https://github.com/D4Vinci/Scrapling) by Karim Shoair (**BSD-3-Clause**) installs separately with uv. |
| `airship` | A **CLI**, not skill content. OmniSkill's `skills/airship/SKILL.md` is original work that teaches its use; [Airship](https://github.com/0xnyn/airship) by Nayan Kumar (**MIT**) runs from npm as [`@airshiplabs/cli`](https://www.npmjs.com/package/@airshiplabs/cli). |
| `vgpu` | An npm **library**, not skill content. OmniSkill's `skills/vgpu/SKILL.md` is original work that teaches its use; [vgpu](https://github.com/vercel-labs/vgpu) by Vercel Labs (**MIT**) installs from npm, and its own docs ship inside the package. |
| `local-leads` | A **Go binary**, not skill content. OmniSkill's `skills/local-leads/SKILL.md` is original work that teaches its use; [google-maps-scraper](https://github.com/gosom/google-maps-scraper) by gosom (**MIT**) installs from its GitHub release. |
| `logo-design` | Ships **1,432 trademarks** as reference material, which its MIT license expressly excludes, so it cannot be bundled in an MIT plugin. OmniSkill's `skills/logo-design/SKILL.md` is original work that routes to [logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) (**MIT** code), cloned separately. |
| `img2threejs` | A **Python toolkit** with its own router, not skill content to copy. OmniSkill's `skills/img2threejs/SKILL.md` is original work that routes to it; [img2threejs](https://github.com/img2threejs/img2threejs) (**Apache-2.0**) is cloned separately. |

### Named but not bundled

`skills/motion-ui/` recommends third-party packages and component registries it does not ship: [Lenis](https://github.com/darkroomengineering/lenis) (MIT), [morphicons](https://github.com/guillermolg00/morphicons) (MIT), [Cult UI](https://github.com/nolly-studio/cult-ui) (MIT), [Watermelon UI](https://ui.watermelon.sh) (MIT), [Skiper UI](https://skiper-ui.com) (**freemium**, paid tier licensed), and the external [scroll-world](https://github.com/oso95/scroll-world) plugin (MIT, but bills real credits to paid render backends). Each installs from its own source under its own terms. The cookbooks flag the two that cost money or rights.

## Attribution

Apache-2.0 requires retaining copyright, license, and NOTICE text — satisfied by the per-skill `LICENSE.txt` files shipped in each `vendor/` directory. MIT requires the copyright and permission notice, satisfied by `skills/superpowers/vendor/LICENSE`.

Nothing here is claimed as original work by OmniSkill.
