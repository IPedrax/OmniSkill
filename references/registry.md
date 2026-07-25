# OmniSkill registry

Canonical map of the workforce. `scripts/check-registry.mjs` validates the tree against this file — keep them in sync.

**Disposition** — how the leaf skill is implemented:

- `authored` — a full playbook written into this plugin.
- `dependency` — adapter; the real skill installs alongside OmniSkill via `plugin.json` `dependencies`.
- `bundled` — adapter; the real skill already ships with Claude Code, nothing to install.
- `local` — adapter; the real skill lives in the user's `~/.claude/skills/`, delegated to if present.

Invoke any leaf directly as `/omniskill:<name>`. Leaves set `disable-model-invocation: true`, so Claude reaches them through `/omniskill` or a department router rather than picking them on its own. That is deliberate: it keeps 42 skills out of the global skill listing budget.

Every skill directory lives flat under `skills/`. Department routers are `dev`, `design`, `marketing`, `social-content`, `finance`, `ops`, `legal` — note the Social & Content router is `social-content` because the leaf skill `social` already owns that name.

---

## 01 — Developers · `/omniskill:dev`
> Ship code faster, from scaffold to QA. *Your build team.*

| Skill | One-liner | Disposition |
|---|---|---|
| `superpowers` | Full skill pack for planning + TDD | dependency |
| `context7` | Pulls live, version-exact docs | dependency |
| `mcp-builder` | Wire Claude to any tool | bundled |
| `skill-creator` | Scaffold your own skills | dependency |
| `webapp-testing` | Browser-tests your app | authored |
| `claude-mem` | Memory across sessions | authored |

## 02 — Design · `/omniskill:design`
> UI that never looks templated. *Your design studio.*

| Skill | One-liner | Disposition |
|---|---|---|
| `frontend-design` | Bold React + Tailwind UI | dependency |
| `web-artifacts` | shadcn HTML artifacts | bundled |
| `canvas-design` | Visual art to PNG / PDF | bundled |
| `algorithmic-art` | Generative p5.js art | authored |
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

- 7 departments × 6 skills = **42 leaves**
- Model-invocable: **8** (`omniskill` router + 7 departments)
- Authored: **31** · Adapters: **11** (4 dependency, 6 bundled, 1 local)

## Upstream targets for adapters

| Leaf | Delegates to | Install if missing |
|---|---|---|
| `superpowers` | `/superpowers` | `claude plugin install superpowers@claude-plugins-official` |
| `context7` | `mcp__context7__*` tools | `claude plugin install context7@claude-plugins-official` |
| `skill-creator` | `/skill-creator` | `claude plugin install skill-creator@claude-plugins-official` |
| `frontend-design` | `/frontend-design` | `claude plugin install frontend-design@claude-plugins-official` |
| `mcp-builder` | `/mcp-builder` | ships with Claude Code |
| `web-artifacts` | `/web-artifacts-builder` | ships with Claude Code |
| `canvas-design` | `/canvas-design` | ships with Claude Code |
| `slack-gif` | `/slack-gif-creator` | ships with Claude Code |
| `xlsx` | `/xlsx` | ships with Claude Code |
| `docx` | `/docx` | ships with Claude Code |
| `ui-ux-pro-max` | `/ui-ux-pro-max` | personal skill in `~/.claude/skills/` |
