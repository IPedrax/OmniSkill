# Third-party notices

OmniSkill itself is MIT (see [LICENSE](LICENSE)). Eleven skills are **vendored verbatim** from upstream projects and remain under their own licenses. Each ships its license file alongside the code.

## Vendored

| Skill | Upstream | License | Location |
|---|---|---|---|
| `superpowers` | [obra/superpowers](https://github.com/obra/superpowers) @ `896224c` — Jesse Vincent | MIT | `skills/superpowers/vendor/` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills) — Matt Pocock (`grill-me` + `grilling`) | MIT | `skills/grill-me/vendor/` |
| `motion-ui` | [IPedrax/motion-ui](https://github.com/IPedrax/motion-ui) | MIT | `skills/motion-ui/vendor/` |
| `design-dna` | [zanwei/design-dna](https://github.com/zanwei/design-dna) @ `9d9d795` — zanwei.guo | MIT | `skills/design-dna/vendor/` |
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
| `airship` | A **CLI**, not skill content. OmniSkill's `skills/airship/SKILL.md` is original work that teaches its use; [Airship](https://github.com/0xnyn/airship) by Nayan Kumar (**MIT**) runs from npm as [`@airshiplabs/cli`](https://www.npmjs.com/package/@airshiplabs/cli). |

### Named but not bundled

`skills/motion-ui/` recommends third-party packages and component registries it does not ship: [Lenis](https://github.com/darkroomengineering/lenis) (MIT), [morphicons](https://github.com/guillermolg00/morphicons) (MIT), [Cult UI](https://github.com/nolly-studio/cult-ui) (MIT), [Watermelon UI](https://ui.watermelon.sh) (MIT), [Skiper UI](https://skiper-ui.com) (**freemium**, paid tier licensed), and the external [scroll-world](https://github.com/oso95/scroll-world) plugin (MIT, but bills real credits to paid render backends). Each installs from its own source under its own terms. The cookbooks flag the two that cost money or rights.

## Attribution

Apache-2.0 requires retaining copyright, license, and NOTICE text — satisfied by the per-skill `LICENSE.txt` files shipped in each `vendor/` directory. MIT requires the copyright and permission notice, satisfied by `skills/superpowers/vendor/LICENSE`.

Nothing here is claimed as original work by OmniSkill.
