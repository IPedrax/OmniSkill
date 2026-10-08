---
name: ops
description: This skill should be used when the user needs the OmniSkill Operations crew — writing standard operating procedures, running a blameless incident post-mortem, building an ROI or business case, planning a go-live and DNS cutover, drafting internal status reports and FAQs, or producing Excel workbooks with live formulas. Triggers on "/omniskill:ops", "write an SOP", "post-mortem", "business case", "launch plan", "cutover", "status update", "build a spreadsheet".
when_to_use: Use for running the business — process documentation, incident response, launch planning, and internal communication.
allowed-tools: Read Glob
---

# 06 — Operations

> Run the business like a machine. **Your ops backbone.**

## Pick the specialist

| Skill | Use when |
|---|---|
| `sop-builder` | Turning tribal knowledge into a repeatable procedure |
| `incident-postmortem` | Something broke and the lesson needs capturing |
| `business-case` | Justifying spend or headcount with ROI |
| `launch-runbook` | Shipping to production, especially with a DNS cutover |
| `internal-comms` | Status reports, FAQs, announcements |
| `xlsx` | Any deliverable that belongs in a spreadsheet |

## Load it

Read `${CLAUDE_SKILL_DIR}/../<skill>/SKILL.md` and follow it. Its paths that start with the CLAUDE_SKILL_DIR placeholder mean its own folder, `${CLAUDE_SKILL_DIR}/../<skill>/`: only the invoked skill gets the placeholder filled in, and Bash never sets it, so write that full path into any command it gives you.

## Routing notes

`incident-postmortem` feeds `sop-builder`: an action item that does not become a written procedure gets relearned in the next incident.

`launch-runbook` is time-ordered and reversible by design — every step names its rollback. Treat a runbook without rollback steps as incomplete.
