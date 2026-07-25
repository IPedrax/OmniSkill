---
name: docx
description: Word docs, tracked changes. OmniSkill Legal crew — adapter for the docx skill, which installs separately.
disable-model-invocation: true
---

# Word Documents

> Word docs, tracked changes · OmniSkill Legal crew

**Installs separately.** One of only two parts of the workforce that is not bundled: the `docx` skill is **source-available and proprietary**, not open source, so it cannot be redistributed inside this MIT-licensed plugin.

## Use it

Invoke `/docx` and follow it. Reach for it any time a Word document is the deliverable.

## If it is not available

It ships with Claude Code in most environments — check before concluding it is missing.

If it genuinely is not there, add Anthropic's skills marketplace:

```bash
claude plugin marketplace add anthropics/skills
```

Install the document skills through `/plugin`, then restart Claude Code.

Do not reimplement it. Tracked changes in OOXML are intricate, and a hand-rolled file will not open cleanly in Word.

## House rules

Deliver contract redlines with tracked changes — the form counterparties actually review. Pair every redline with a short summary of what changed and why; a marked-up document with no rationale invites rejection.

## Attribution

By [Anthropic](https://github.com/anthropics/skills). Source-available and proprietary — deliberately not vendored.
