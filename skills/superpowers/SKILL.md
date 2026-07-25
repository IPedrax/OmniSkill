---
name: superpowers
description: Full skill pack for planning + TDD. OmniSkill Developers crew — bundled copy of the Superpowers library (14 skills).
disable-model-invocation: true
---

# Superpowers

> Full skill pack for planning + TDD · OmniSkill Developers crew

**Bundled — nothing to install.** All 14 Superpowers skills ship inside this plugin.

## Pick the one you need

| Skill | Use when |
|---|---|
| `brainstorming` | turning a vague idea into a concrete plan |
| `writing-plans` | writing an implementation plan worth following |
| `executing-plans` | working through a plan already written |
| `test-driven-development` | red/green TDD on a real feature |
| `systematic-debugging` | a bug that has resisted the obvious fixes |
| `verification-before-completion` | confirming work is actually done |
| `requesting-code-review` | getting a change reviewed |
| `receiving-code-review` | acting on review feedback |
| `subagent-driven-development` | splitting work across subagents |
| `dispatching-parallel-agents` | running agents concurrently |
| `using-git-worktrees` | isolating parallel work in worktrees |
| `finishing-a-development-branch` | landing and cleaning up a branch |
| `writing-skills` | authoring a new skill |
| `using-superpowers` | the index of the whole library |

## Load it

Read `${CLAUDE_SKILL_DIR}/vendor/<skill>/SKILL.md` and follow it — for example `vendor/test-driven-development/SKILL.md`.

Start at `vendor/using-superpowers/SKILL.md` if unsure which applies; it is the library's own index.

Resolve any relative path inside those skills against `${CLAUDE_SKILL_DIR}/vendor/`, not the working directory.

## House rules

Use this for feature work that deserves a plan and a test before code. Each skill carries its own workflow — follow it rather than improvising a parallel one.

`brainstorming` → `writing-plans` → `executing-plans` is the intended spine for anything substantial. TDD and debugging are the two most reached-for on their own.

## Attribution

Vendored verbatim from [obra/superpowers](https://github.com/obra/superpowers) at commit `896224c`, by Jesse Vincent, licensed **MIT**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`. Unmodified — upstream is the place to send fixes.
