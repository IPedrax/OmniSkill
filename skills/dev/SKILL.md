---
name: dev
description: This skill should be used when the user needs the OmniSkill Developers crew — stress-testing a plan before building, planning and TDD workflows, live version-exact library docs, building MCP servers, scaffolding new skills, browser-testing a web app, or persisting memory across sessions. Triggers on "/omniskill:dev", "grill me", "stress-test this plan", "set up TDD", "look up the docs for", "build an MCP server", "create a skill", "test my app in a browser".
when_to_use: Use for engineering workflow and tooling tasks. For ordinary code edits in an existing repo, work directly instead.
allowed-tools: Read Glob
---

# 01 — Developers

> Ship code faster, from scaffold to QA. **Your build team.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `grill-me` | Pressure-testing a plan or design **before** building it |
| `superpowers` | Structured planning and test-driven development on a real feature |
| `context7` | Needing the *current* API of a library — never answer library questions from memory |
| `mcp-builder` | Wiring Claude to an external tool or API as an MCP server |
| `skill-creator` | Turning a repeated workflow into a reusable skill |
| `webapp-testing` | Verifying a web app actually works in a browser |
| `claude-mem` | Carrying durable knowledge across sessions |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

`context7` is near-free and high-value: any question about a library's API, config, or version behaviour should route here before answering. Guessing at library APIs from memory is the single most common source of wrong code.

`superpowers` and `webapp-testing` compose — plan and build with the first, prove it works with the second.

`grill-me` runs *before* both. When someone arrives with an approach already in mind and the stakes are real, interrogate it first — an hour of questions is cheaper than a week down the wrong branch.
