---
name: grill-me
description: A relentless interview to sharpen a plan or design. OmniSkill Developers crew — bundled copy of Matt Pocock's grilling skill.
disable-model-invocation: true
---

# Grill Me

> Stress-tests a plan before you build it · OmniSkill Developers crew

**Bundled — nothing to install.**

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/grilling/SKILL.md` and follow it. That file is the method; `vendor/grill-me/SKILL.md` is just its trigger alias.

## House rules

Use it **before** committing to an approach — a plan, an architecture, a schema, a migration strategy. It is cheapest at the point where changing your mind is still free.

The discipline that makes it work:

- **One question at a time.** Wait for the answer before the next. A batch of five questions gets one vague reply and the interview has already failed.
- **Look up facts; ask about decisions.** Anything discoverable in the filesystem, the code, or a tool is not a question — go find it. Reserve the user's attention for judgement calls only they can make.
- **Recommend an answer with each question.** "Postgres or SQLite? I'd say Postgres, because X" moves faster than an open prompt and gives them something to push against.
- **Do not start building until they confirm shared understanding.** Ending the interview early is the main way this gets wasted.

Pairs naturally with `/omniskill:superpowers` — grill the idea here, then take the sharpened version into `vendor/brainstorming` and `vendor/writing-plans`.

Reach for it when someone says *"grill me"*, *"stress-test this"*, *"poke holes in this"*, or *"am I missing something"*.

## Attribution

Vendored verbatim from [mattpocock/skills](https://github.com/mattpocock/skills) by Matt Pocock, licensed **MIT**. The upstream license ships at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`. Unmodified — upstream is the place to send fixes.
