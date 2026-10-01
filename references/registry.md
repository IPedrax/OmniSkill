# OmniSkill registry

Canonical map of the workforce. `scripts/check-registry.mjs` validates the tree against this file — keep them in sync.

**Disposition** — how the leaf skill is implemented:

- `authored` — a full playbook written into this plugin.
- `vendored` — adapter + the real upstream skill bundled verbatim under `skills/<name>/vendor/`, with its license. Nothing to install.
- `separate` — adapter only; the upstream skill cannot be redistributed (proprietary) or is not skill content (an MCP server, a CLI), so it installs on its own.

Invoke any leaf directly as `/omniskill:<name>`. Leaves set `disable-model-invocation: true`, so Claude reaches them through `/omniskill` or a department router rather than picking them on its own. That is deliberate: it keeps 50 skills out of the global skill listing budget.

Every skill directory lives flat under `skills/`. Department routers are `dev`, `design`, `marketing`, `social-content`, `finance`, `ops`, `legal` — note the Social & Content router is `social-content` because the leaf skill `social` already owns that name.

---

## 01 — Developers · `/omniskill:dev`
> Ship code faster, from scaffold to QA. *Your build team.*

| Skill | One-liner | Disposition |
|---|---|---|
| `grill-me` | Relentless interview to sharpen a plan | vendored |
| `superpowers` | Full skill pack for planning + TDD | vendored |
| `context7` | Pulls live, version-exact docs | dependency |
| `mcp-builder` | Wire Claude to any tool | bundled |
| `skill-creator` | Scaffold your own skills | dependency |
| `webapp-testing` | Browser-tests your app | authored |
| `claude-mem` | Memory across sessions | authored |

## 02 — Design · `/omniskill:design`
> UI that never looks templated. *Your design studio.*

| Skill | One-liner | Disposition |
|---|---|---|
| `anydesign` | Screenshot, URL or Figma → measured design.md + DTCG tokens | vendored |
| `frontend-design` | Bold React + Tailwind UI | dependency |
| `web-artifacts` | shadcn HTML artifacts | bundled |
| `canvas-design` | Visual art to PNG / PDF | bundled |
| `slidev` | Markdown decks with live code | vendored |
| `airship` | Visual editor over the running app | separate |
| `motion-ui` | Animation engines + animated UI | vendored |
| `uisfx` | Interface sound effects | authored |
| `algorithmic-art` | Generative p5.js art | authored |
| `vgpu` | WebGPU shaders, effects, compute | separate |
| `img2threejs` | Reference image → procedural Three.js model | separate |
| `ui-ux-pro-max` | Full design-system intel | local |
| `slack-gif` | Slack-ready animated GIFs | bundled |

## 03 — Marketing · `/omniskill:marketing`
> Copy, SEO and ads that convert. *Your growth engine.*

| Skill | One-liner | Disposition |
|---|---|---|
| `seo-audit` | Diagnoses on-page SEO | authored |
| `programmatic-seo` | Pages at scale from data | authored |
| `ai-seo` | Rank inside AI answers | authored |
| `cro` | Lift page + form conversion | authored |
| `ad-creative` | Scales ad variations | authored |
| `mktg-psychology` | Behavioral triggers | authored |

## 04 — Social & Content · `/omniskill:social-content`
> Feed the algorithm on autopilot. *Your content machine.*

| Skill | One-liner | Disposition |
|---|---|---|
| `social` | Posts for every platform | authored |
| `copywriting` | Rewrites any page copy | authored |
| `content-strategy` | Plans your topic map | authored |
| `video` | Scripts + produces video | authored |
| `pillar-content` | Hub-and-cluster authority | authored |
| `email-sequences` | Lifecycle email flows | authored |

## 05 — Finance · `/omniskill:finance`
> Model the numbers before you spend. *Your CFO on call.*

| Skill | One-liner | Disposition |
|---|---|---|
| `dcf-model` | Discounted cash-flow value | authored |
| `3-statements` | Full 3-statement model | authored |
| `lbo-model` | Leveraged-buyout math | authored |
| `comps-analysis` | Comparable-company set | authored |
| `pricing` | Packaging + monetization | authored |
| `pitch-deck` | Investor pitch decks | authored |

## 06 — Operations · `/omniskill:ops`
> Run the business like a machine. *Your ops backbone.*

| Skill | One-liner | Disposition |
|---|---|---|
| `sop-builder` | Writes clean SOPs | authored |
| `incident-postmortem` | Blameless post-mortems | authored |
| `business-case` | ROI + business cases | authored |
| `launch-runbook` | Go-live + DNS cutover | authored |
| `internal-comms` | Status reports + FAQs | authored |
| `xlsx` | Excel with live formulas | bundled |

## 07 — Legal · `/omniskill:legal`
> Read the fine print for you. *Your legal desk.*

| Skill | One-liner | Disposition |
|---|---|---|
| `contract-review` | Clause-by-clause review | authored |
| `nda-triage` | Auto-triage NDAs | authored |
| `legal-risk` | Flags legal exposure | authored |
| `compliance` | Regulatory checks | authored |
| `docx` | Word docs, tracked changes | bundled |
| `sql-queries` | Pull records with SQL | authored |

---

## Counts

- **50 leaves** across 7 departments — Design carries 13, Developers 7, the rest 6
- Model-invocable: **8** (`omniskill` router + 7 departments)
- Authored: **32** · Vendored: **12** · Separate: **6** (`xlsx`, `docx`, `context7`, `airship`, `vgpu`, `img2threejs`)

## Upstream sources

Vendored copies live at `skills/<leaf>/vendor/` and are **unmodified**. Send fixes upstream. Full attribution in [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

| Leaf | Upstream | License |
|---|---|---|
| `superpowers` | [obra/superpowers](https://github.com/obra/superpowers) @ `896224c` (14 skills) | MIT |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills) (`grill-me` + `grilling`) | MIT |
| `motion-ui` | [IPedrax/motion-ui](https://github.com/IPedrax/motion-ui) | MIT |
| `anydesign` | [uxKero/anydesign](https://github.com/uxKero/anydesign) @ `d81bd89` (without `examples/`) | MIT |
| `slidev` | [slidevjs/slidev](https://github.com/slidevjs/slidev) @ `a8d8ff7` (`skills/slidev`, 53 references) | MIT |
| `ui-ux-pro-max` | bundled by the maintainer | see `vendor/` |
| `canvas-design` | [anthropics/skills](https://github.com/anthropics/skills) + 54 OFL fonts | Apache-2.0 |
| `web-artifacts` | [anthropics/skills](https://github.com/anthropics/skills) (`web-artifacts-builder`) | Apache-2.0 |
| `slack-gif` | [anthropics/skills](https://github.com/anthropics/skills) (`slack-gif-creator`) | Apache-2.0 |
| `mcp-builder` | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| `frontend-design` | [claude-plugins-public](https://github.com/anthropics/claude-plugins-public) | Apache-2.0 |
| `skill-creator` | [claude-plugins-public](https://github.com/anthropics/claude-plugins-public) | Apache-2.0 |

### Not vendored

| Leaf | Reason | How to get it |
|---|---|---|
| `xlsx`, `docx` | Source-available and proprietary | Ship with Claude Code, else `claude plugin marketplace add anthropics/skills` |
| `context7` | An MCP server, not skill content | `claude mcp add context7 --scope user -- npx -y @upstash/context7-mcp@latest` |
| `airship` | A CLI, not skill content | `npx @airshiplabs/cli --target <port>`, or `npm i -g @airshiplabs/cli` |
| `vgpu` | An npm library, not skill content | `pnpm add vgpu` · docs offline via `npx vgpu docs` |
| `img2threejs` | A Python toolkit with its own router, shipped often | `git clone https://github.com/img2threejs/img2threejs.git ~/tools/img2threejs` |
