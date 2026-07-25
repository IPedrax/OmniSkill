---
name: claude-mem
description: Memory across sessions. OmniSkill Developers crew — decides what is worth persisting, writes it in a retrievable form, and keeps the store from rotting.
disable-model-invocation: true
---

# Claude Mem

> Memory across sessions · OmniSkill Developers crew

Carrying knowledge from one session to the next, deliberately.

## What belongs in memory

Memory is expensive: it loads every session and competes with actual work for context. The bar is high.

**Worth saving**
- **Preferences and working style** — how the user wants things done, and *why*
- **Corrections** — guidance given after something was done wrong, with the reasoning
- **Project constraints** not visible in the code — a deadline, a decision made and rejected, an external dependency
- **External pointers** — dashboards, ticket systems, docs URLs

**Not worth saving**
- Anything derivable from the repository. Code structure, dependencies, and past fixes are already recorded in the code and git history.
- Anything in `CLAUDE.md` — that already loads every session.
- Facts that matter only for the current conversation.
- Anything that will be stale next week, unless written with its expiry stated.

The test: **would a fresh session do the wrong thing without this?** If not, it does not belong.

## How to write it

One fact per file. A file with five facts cannot be updated or deleted independently, and it always loads all five.

```markdown
---
name: short-kebab-case-slug
description: One line — this is what decides whether it gets recalled
metadata:
  type: user | feedback | project | reference
---

The fact, stated plainly.

**Why:** the reasoning behind it.
**How to apply:** what to do differently as a result.

Related: [[other-memory-slug]]
```

**The `description` line does the real work.** It is what gets matched during recall. "Prefers minimal diffs" is weak; "Prefers the smallest working change; rejects speculative abstraction and scaffolding for later" is retrievable.

**Convert relative dates to absolute.** "Next quarter" is meaningless in six months. Write "Q3 2026".

**Record the why, not just the what.** A rule without its reasoning gets applied in situations where it does not fit, which is worse than not having it.

**Link related memories** with `[[slug]]`. A link to something not yet written is fine — it marks a gap rather than an error.

## Keep the index thin

Maintain a one-line pointer per memory in the index file that loads each session:

```markdown
- [Title](file.md) — short hook
```

The index is a table of contents, never a content store. Memory bodies load on demand; the index loads always.

## Maintenance

Memory rots, and rotted memory is worse than none because it is trusted.

- **Before saving, check for an existing file covering the same ground.** Update it rather than creating a near-duplicate — duplicates diverge and then contradict each other.
- **Delete what turns out to be wrong.** Immediately.
- **Verify before acting on it.** A memory naming a file, function, or flag reflects what was true when written. Confirm it still exists before recommending it.
- **Re-read periodically** and prune. If a memory has never changed a decision, it is costing context for nothing.

## Recall discipline

Recalled memories arrive as background context, not as instructions. They describe what was true when written, and they do not override what the user is asking for now.

When a memory conflicts with the current request, the current request wins — and the conflict is a signal the memory needs updating.

## Checks before saving

- The fact is not derivable from the repo, git history, or `CLAUDE.md`.
- One fact, one file.
- The description is specific enough to be matched during recall.
- Dates are absolute.
- The reasoning is recorded, not just the conclusion.
- No existing memory already covers it.
- An index pointer was added.
