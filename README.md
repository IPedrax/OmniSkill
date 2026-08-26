<div align="center">
  <img src="assets/icons/users.svg" width="56" alt="" />
  <h1>OmniSkill</h1>
  <p><strong>Your Claude workforce — 46 specialist skills across 7 departments, behind one router. Ship code, design interfaces, rank in search, model the numbers, run ops, read the contract.</strong></p>
</div>

Most skill collections do one of two things badly: they cover a single domain and leave you switching tools for everything else, or they dump a hundred skills into your session and quietly wreck the context budget every other skill depends on. **OmniSkill** does neither. It gives you a **real specialist for each of the seven functions a small company actually runs on**, routed from a single entry point — and it costs your skill listing **8 entries, not 46**. Invoke it yourself with `/omniskill`, or let it offer itself when you start a new project. It never activates without your say-so.

Built for **Claude Code** (Windows / macOS / Linux).

---

## <img src="assets/icons/layers.svg" width="20" align="absmiddle" alt="" /> The crews

| # | Department | Covers | Skills |
|---|---|---|---|
| 01 | **Developers** | Ship code faster, from scaffold to QA | `grill-me` · `superpowers` · `context7` · `mcp-builder` · `skill-creator` · `webapp-testing` · `claude-mem` |
| 02 | **Design** | UI that never looks templated | `design-dna` · `ui-ux-pro-max` · `frontend-design` · `web-artifacts` · `motion-ui` · `uisfx` · `canvas-design` · `algorithmic-art` · `slack-gif` |
| 03 | **Marketing** | Copy, SEO and ads that convert | `seo-audit` · `programmatic-seo` · `ai-seo` · `cro` · `ad-creative` · `mktg-psychology` |
| 04 | **Social & Content** | Feed the algorithm on autopilot | `social` · `copywriting` · `content-strategy` · `video` · `pillar-content` · `email-sequences` |
| 05 | **Finance** | Model the numbers before you spend | `dcf-model` · `3-statements` · `lbo-model` · `comps-analysis` · `pricing` · `pitch-deck` |
| 06 | **Operations** | Run the business like a machine | `sop-builder` · `incident-postmortem` · `business-case` · `launch-runbook` · `internal-comms` · `xlsx` |
| 07 | **Legal** | Read the fine print for you | `contract-review` · `nda-triage` · `legal-risk` · `compliance` · `docx` · `sql-queries` |

Full map with one-liners: [`references/registry.md`](references/registry.md).

---

## <img src="assets/icons/sparkles.svg" width="20" align="absmiddle" alt="" /> What it does

- **Seven departments, one door** — `/omniskill` reads the job, recommends a crew, and loads only that specialist. Real projects cross crews, so it sequences them (Finance → Design → Marketing → Legal → Ops) and loads each only when it gets there.
- **Costs 8 skill-listing entries, not 46** — the routers carry descriptions; all 46 leaves are `disable-model-invocation: true`. They cost **zero** listing budget and stay fully invocable by name. On a machine already running several plugins, this is the difference between adding a workforce and degrading every skill you own.
- **Playbooks, not prompt-shapers** — 32 skills are full working methods. DCF enforces *unlevered means unlevered* and sanity-bands the terminal value. LBO attributes IRR across deleveraging, EBITDA growth, and multiple expansion. Contract review ranks findings by severity against deal size. These are methods you'd actually follow.
- **Nothing mature gets re-implemented** — 32 skills are written here; the other 14 wrap real upstream work. Eleven of those ride along in the box, vendored **unmodified** with their licenses intact, so a fresh machine gets the whole workforce from one install and fixes still go upstream.
- **Offers itself, never assumes** — a hook notices new-project intent and *suggests*. Claude then asks. Every activation goes through a question you answer.
- **Safety is not an upsell** — Finance and Legal state plainly that they are analysis, not licensed advice. Marketing refuses to build dark patterns regardless of measured lift.

---

## <img src="assets/icons/download.svg" width="20" align="absmiddle" alt="" /> Install

### <img src="assets/icons/terminal.svg" width="17" align="absmiddle" alt="" /> Claude Code — any platform

```bash
claude plugin marketplace add IPedrax/OmniSkill
```

```bash
claude plugin install omniskill@omniskill
```

### <img src="assets/icons/monitor.svg" width="17" align="absmiddle" alt="" /> From a local clone

```bash
claude plugin marketplace add ./OmniSkill && claude plugin install omniskill@omniskill
```

That single install is the whole workforce. **Eleven upstream skills ship inside it** — `superpowers` (all 14), `grill-me`, `motion-ui`, `design-dna`, `ui-ux-pro-max`, `canvas-design` (with its 54 OFL fonts), `web-artifacts`, `slack-gif`, `mcp-builder`, `frontend-design`, and `skill-creator`. Nothing to chase down.

### <img src="assets/icons/layers.svg" width="17" align="absmiddle" alt="" /> The three exceptions

| Skill | Why | What to do |
|---|---|---|
| `xlsx`, `docx` | **Source-available and proprietary** — cannot be redistributed in an MIT plugin | Ship with Claude Code in most setups. Otherwise `claude plugin marketplace add anthropics/skills` |
| `context7` | An MCP server, not skill content | The adapter offers to set it up when you first need it |

> **Restart Claude Code after installing.** Hooks load at session start, so new-project detection stays dormant until you do.

> **Requires Claude Code ≥ 2.1.71**, the version this is built and tested against.

> **Prefer to let Claude install it?** Paste this into a new chat:
> *"Install this Claude Code plugin for me from https://github.com/IPedrax/OmniSkill and walk me through anything you need."*

---

## <img src="assets/icons/chat.svg" width="20" align="absmiddle" alt="" /> How to use it

Just ask, and let it route:

- *"build me a landing page for a new SaaS"*
- *"what is this company worth"*
- *"review this contract before I sign"*
- *"why isn't this page ranking"*
- *"write the go-live runbook, we cut over Friday"*

Or go straight to what you want:

```
/omniskill                 pick a crew for what you are doing
/omniskill:finance         jump to a department
/omniskill:dcf-model       jump to a specialist
```

All 46 leaves are directly invocable by name.

---

## <img src="assets/icons/settings.svg" width="20" align="absmiddle" alt="" /> How it works

**Detect intent → offer the crew → you approve → load the department → load the one specialist → work.**

When you start a new project, a `UserPromptSubmit` hook notices and injects a *suggestion* — nothing more. It cannot load a skill and it cannot act; Claude asks you via a real question and waits. It fires **at most once per session**, only on wording that implies building something new (`"build me a new app"`, `"from scratch"`), and never on existing-codebase work (`"fix this bug"`, `"refactor this"`). Vague requests only trigger it in a directory that is genuinely empty.

To turn it off entirely, set `OMNISKILL_AUTO_SUGGEST=false` in your environment, or in the `env` block of `~/.claude/settings.json`:

```json
{ "env": { "OMNISKILL_AUTO_SUGGEST": "false" } }
```

---

## <img src="assets/icons/gauge.svg" width="20" align="absmiddle" alt="" /> Why only 8 skills are model-invocable

Claude Code loads every skill's description into context, capped at roughly **1% of the context window**. On a machine with several plugins installed that budget is already tight, and when it overflows Claude Code starts dropping descriptions — from *every* skill you have, not just the new ones.

So OmniSkill spends 8 entries and no more. The routers carry descriptions; all 46 leaves set `disable-model-invocation: true`, which costs zero listing budget while leaving them fully invocable by name. Routing reaches them by reading their `SKILL.md` directly.

**The trade:** Claude won't spontaneously reach for `dcf-model` — it gets there through `/omniskill` or a department router. Want a specific leaf auto-triggering? Delete one line from its frontmatter.

---

## <img src="assets/icons/check.svg" width="20" align="absmiddle" alt="" /> Verify

```bash
node scripts/check-registry.mjs
```

Checks the tree against the registry, confirms all 46 leaves exist, and asserts **exactly 8 skills are model-invocable** — the context-budget guarantee. It fails loudly if the architecture ever regresses.

```bash
node hooks/detect-new-project.mjs --selftest
```

Checks that new-project wording fires, existing-codebase wording stays silent, the output shape is right, and the once-per-session dedupe holds.

```bash
claude plugin validate .
```

---

## <img src="assets/icons/shield.svg" width="20" align="absmiddle" alt="" /> Scope

The **Finance** and **Legal** crews are analytical tools. They produce models, reviews, and checklists to inform a decision — **not licensed financial or legal advice**. Every output states its assumptions and warrants professional review before anyone relies on it.

The **Marketing** crew will not build dark patterns. Fake countdowns, confirmshaming, obstructed cancellation, and pre-ticked consent are out of scope regardless of measured lift — they are illegal in a growing number of jurisdictions and they cost more than they earn. Ask for one and you get the legitimate version that achieves the same goal.

---

## <img src="assets/icons/file.svg" width="20" align="absmiddle" alt="" /> License

OmniSkill is [MIT](LICENSE).

Eleven bundled skills stay under their own licenses — MIT for [superpowers](https://github.com/obra/superpowers), [grill-me](https://github.com/mattpocock/skills), [motion-ui](https://github.com/IPedrax/motion-ui), and [design-dna](https://github.com/zanwei/design-dna); Apache-2.0 for the [anthropics/skills](https://github.com/anthropics/skills) and [claude-plugins-public](https://github.com/anthropics/claude-plugins-public) skills; SIL OFL for the 54 fonts in `canvas-design`. Every copy is unmodified and ships its license file. Full attribution: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

`xlsx` and `docx` are deliberately **not** bundled — they are source-available and proprietary, so redistribution here would not be permitted.

---

Built by [Pedro Medeiros](https://ipedrax.com.br). I build production LLM applications for companies too: multi-provider backends, the infrastructure under them, and the billing on top. Available for contract work, remote from Brazil on US hours. [pedro.medeiros@ipedrax.com.br](mailto:pedro.medeiros@ipedrax.com.br)
