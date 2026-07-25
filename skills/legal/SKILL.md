---
name: legal
description: This skill should be used when the user needs the OmniSkill Legal crew — clause-by-clause contract review, triaging an NDA, flagging legal exposure in a plan or product, checking regulatory obligations (GDPR, CCPA, accessibility, sector rules), producing Word documents with tracked changes, or pulling records with SQL. Triggers on "/omniskill:legal", "review this contract", "is this NDA ok", "what are the legal risks", "GDPR", "compliance check", "redline this".
when_to_use: Use for contract analysis, regulatory questions, and risk review. Always paired with the scope caveat below.
allowed-tools: Read Glob
---

# 07 — Legal

> Read the fine print for you. **Your legal desk.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `contract-review` | A full agreement needs clause-by-clause analysis |
| `nda-triage` | An NDA needs a fast accept / negotiate / escalate verdict |
| `legal-risk` | A product or business plan needs exposure flagged before building |
| `compliance` | A specific regulation applies and obligations need mapping |
| `docx` | Delivering a redline with tracked changes |
| `sql-queries` | Pulling the records a review or audit depends on |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it.

## Routing notes

Match depth to stakes. A standard mutual NDA is `nda-triage` and takes minutes; a master services agreement is `contract-review` and does not.

Run `legal-risk` before building, not after. Exposure found at design time is a design change; the same exposure found at launch is a rewrite.

Deliver redlines through the bundled `docx` skill — tracked changes are what counterparties actually review.

## Scope

**This is analysis, not legal advice.** No attorney-client relationship exists here. Output identifies issues, explains standard market positions, and drafts language for a qualified attorney to review. Say this plainly in the deliverable — never let a review read as clearance to sign.
