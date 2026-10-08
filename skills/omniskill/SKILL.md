---
name: omniskill
description: This skill should be used when the user starts a new project or asks for the OmniSkill workforce. Triggers on "build me a", "create a new app", "start a new project", "from scratch", "scaffold a", "new SaaS/site/landing page", "/omniskill", "what crews do I have", or any request that spans business functions (code, design, marketing, content, finance, ops, legal). Routes to 54 specialist skills across 7 departments.
when_to_use: Use at the start of a new project to pick the right crew, or whenever a task belongs to a specialist department rather than general coding. Do not use for a small edit inside an existing codebase.
allowed-tools: Read Glob
---

# OmniSkill — your Claude workforce

54 skills. 7 crews. One workspace.

## Step 0 — the approval gate (mandatory)

**If the user did not type `/omniskill` explicitly, do not proceed past this step.**

When this skill loads on its own — because a new project was detected, or because the request matched the description — stop and ask permission with `AskUserQuestion` before doing any work. Offer three options: bring in the recommended crew, see all 7 departments first, or skip and continue normally.

Name the specific department being recommended and why. A concrete offer ("this looks like a new SaaS landing page — the Design and Marketing crews cover it") is answerable; a generic one is not.

If the user declines, drop it and handle the request normally. Do not re-offer in the same session.

When the user typed `/omniskill` themselves, skip this step entirely — they already asked.

## Step 1 — route to a department

| Department | Router | Covers | Crew |
|---|---|---|---|
| 01 Developers | `/omniskill:dev` | Ship code faster, from scaffold to QA | Your build team |
| 02 Design | `/omniskill:design` | UI that never looks templated | Your design studio |
| 03 Marketing | `/omniskill:marketing` | Copy, SEO and ads that convert | Your growth engine |
| 04 Social & Content | `/omniskill:social-content` | Feed the algorithm on autopilot | Your content machine |
| 05 Finance | `/omniskill:finance` | Model the numbers before you spend | Your CFO on call |
| 06 Operations | `/omniskill:ops` | Run the business like a machine | Your ops backbone |
| 07 Legal | `/omniskill:legal` | Read the fine print for you | Your legal desk |

To see the full 54-skill map with one-liners, read `${CLAUDE_SKILL_DIR}/../../references/registry.md`.

## Step 2 — load the specialist

Read the department router's `SKILL.md` at `${CLAUDE_SKILL_DIR}/../<department>/SKILL.md`, then follow it to the right leaf skill.

To jump straight to a known specialist, read `${CLAUDE_SKILL_DIR}/../<skill-name>/SKILL.md` — for example `../dcf-model/SKILL.md`.

**Read leaf skills rather than invoking them.** Leaves set `disable-model-invocation: true`, so they cannot be auto-invoked; that is what keeps 54 skills out of the global skill-listing budget. The user can still run any leaf directly as `/omniskill:dcf-model`.

## Step 3 — work

Follow the leaf skill's playbook. It is the authority for its domain — prefer its method over improvising.

## Multi-department work

Real projects cross crews. A product launch is Finance (pricing) → Design (landing page) → Marketing (SEO) → Legal (terms) → Ops (runbook).

Sequence the departments, state the order, and work through them one at a time. Load a department only when reaching it — loading all 7 up front wastes context and buys nothing.

## Scope

The Finance and Legal crews are analytical tools. They produce models, reviews, and checklists to inform a decision — not licensed financial or legal advice. Their output warrants professional review before anyone relies on it.
