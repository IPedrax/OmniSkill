---
name: sop-builder
description: Write clean standard operating procedures. OmniSkill Operations crew — turns tribal knowledge into a procedure someone can follow correctly the first time.
disable-model-invocation: true
---

# SOP Builder

> Writes clean SOPs · OmniSkill Operations crew

## The test

**Could a competent new joiner follow this correctly, alone, on their first attempt?**

That is the only standard that matters. An SOP that works for the person who wrote it has documented nothing — the knowledge is still in their head, and the document merely records that it exists.

## 1. Scope it precisely

Every SOP states up front:

- **Purpose** — what this achieves and why it matters
- **Scope** — when it applies, and explicitly when it does not
- **Owner** — a role, not a person. People leave; roles persist.
- **Prerequisites** — access, tools, permissions, approvals needed *before* starting
- **Expected duration**
- **Last reviewed** date

The prerequisites line prevents the most common failure: someone gets to step 7 and discovers they never had the access required.

## 2. Write the steps

**One action per step.** If a step contains "and", it is probably two steps.

**Start each with a verb.** "Open the billing dashboard", not "The billing dashboard should be opened".

**Be specific about the interface.** Name the exact button, menu, or command. "Navigate to settings" is a hint; "Click **Settings → Billing → Payment methods**" is an instruction.

**State the expected result** after any step whose outcome is not obvious. This is how someone knows they are still on track, and it is the difference between a procedure and a list.

**Number sequentially.** Sub-steps as 3a, 3b where genuinely needed, but deep nesting means the procedure should be split.

**Include the decision points.** Real work branches: "If the invoice is over $10,000, route to finance for approval before continuing." Undocumented branches are where the process quietly diverges between people.

## 3. Cover the failure paths

Most SOPs document only the happy path, which is why they fail in practice. Add:

- What can go wrong at each risky step
- How to recognise it
- What to do about it
- Who to escalate to, and when

If a step is irreversible — deleting data, sending to customers, moving money — say so **before** the step, not after.

## 4. Show, do not only tell

Screenshots for interface steps, annotated with what to click. Copy-pasteable commands in code blocks, exactly as they should be run. A short screen recording for anything genuinely hard to describe.

Keep visuals current. A screenshot of a UI that changed two redesigns ago is worse than no screenshot — it actively misleads.

## 5. Keep it maintainable

An out-of-date SOP is more dangerous than a missing one, because it is followed with confidence.

- **Review cadence** — quarterly, or on any change to the underlying system
- **Version and date** on the document
- **Named owning role** responsible for the review
- **A feedback path** — the person who hits a wrong step is the best-placed person to fix it, so make that easy

## 6. Validate before publishing

**Have someone else follow it, without help, while you watch.** Every place they hesitate, ask a question, or take a wrong turn is a defect in the document, not in them.

This step is skipped almost universally and it is the one that determines whether the SOP works.

## Output structure

```
Title
Purpose · Scope · Owner (role) · Last reviewed
Prerequisites
Steps (numbered, verb-first, with expected results)
Decision points and branches
Troubleshooting
Escalation path
Related procedures
```

Deliver via `/omniskill:docx` where it belongs in a document system, or as markdown where it belongs in a repository.

## Checks before delivering

- A new joiner could follow it alone.
- Every step starts with a verb and contains one action.
- Prerequisites listed before step 1.
- Irreversible steps flagged in advance.
- Failure paths and escalation documented.
- Owner is a role; review date is set.
- Someone unfamiliar has walked through it.

Incident action items from `/omniskill:incident-postmortem` should land here — an action item that never becomes a written procedure gets relearned in the next incident.
