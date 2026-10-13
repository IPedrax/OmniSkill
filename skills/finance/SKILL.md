---
name: finance
description: This skill should be used when the user needs the OmniSkill Finance crew — building a discounted cash-flow valuation, a linked 3-statement model, leveraged-buyout math, a comparable-company set, pricing and packaging, an investor pitch deck, or a board-style verdict on whether a business idea is worth starting. Triggers on "/omniskill:finance", "what is this company worth", "build a DCF", "financial model", "LBO", "trading comps", "how should I price this", "pitch deck", "is this business idea good", "test my business idea", "startup council".
when_to_use: Use for valuation, financial modeling, pricing, and fundraising materials.
allowed-tools: Read Glob
---

# 05 — Finance

> Model the numbers before you spend. **Your CFO on call.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `3-statements` | Building the operating model everything else feeds from. **Start here.** |
| `dcf-model` | Intrinsic value from projected cash flows |
| `comps-analysis` | Relative value against peers |
| `lbo-model` | Returns under a debt-financed acquisition |
| `pricing` | Setting price, packaging, and tiers |
| `pitch-deck` | Raising money |
| `startup-council` | Is this business worth starting? Unit economics and a buyer panel first, then seven advisors on mixed models, peer review, and a fund / fund if / pass verdict |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it. Its paths that start with the CLAUDE_SKILL_DIR placeholder mean its own folder, `${CLAUDE_SKILL_DIR}/../<skill>/`: only the invoked skill gets the placeholder filled in, and Bash never sets it, so write that full path into any command it gives you.

## Routing notes

`startup-council` comes before everything else here: it decides whether there is a business worth modelling. Its bundled founder pack then carries a FUND IF through competitors, pricing, offer and launch.

Valuation runs on projections, and projections come from `3-statements`. Building a DCF on invented free cash flow produces a precise number with no support behind it.

Triangulate: `dcf-model` and `comps-analysis` answer the same question by different routes. A wide gap between them is a finding worth reporting, not an error to hide.

Deliver models through the bundled `xlsx` skill so the workbook carries live formulas and the user can change assumptions themselves. A hardcoded number is not a model.

## Scope

These are analytical tools, not licensed investment advice. Every output rests on assumptions that must be stated plainly and reviewed by a professional before anyone acts on it.
