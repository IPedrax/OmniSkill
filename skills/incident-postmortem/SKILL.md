---
name: incident-postmortem
description: Blameless incident post-mortems. OmniSkill Operations crew — reconstructs the timeline, finds contributing causes rather than a culprit, and produces action items that actually get done.
disable-model-invocation: true
---

# Incident Post-Mortem

> Blameless post-mortems · OmniSkill Operations crew

## Blameless means something specific

It does not mean avoiding the question of what happened. It means assuming **everyone acted reasonably given what they knew at the time**, and asking why the action made sense to them then — not why it looks wrong now.

The reason is practical, not sentimental: in a blaming culture people hide information, and a post-mortem missing information is a post-mortem that fixes nothing. The next incident is then identical.

Write about systems and decisions, not people. "The deploy tooling allowed a config change to skip staging" is actionable. "Sam skipped staging" is not — the next engineer will skip it too, because the system permitted it.

## 1. Reconstruct the timeline

Facts with timestamps, in order, from the sources — logs, alerts, chat, deploy history. Not recollections.

Mark these specifically:
- When the change that caused it went in (often well before the impact)
- When it started affecting users
- When anyone noticed — and **how**: automated alert, or a customer complaint?
- Each mitigation attempted, and its effect
- When impact ended

**Detection time and mitigation time are the two most useful numbers in the document.** They point directly at monitoring and runbook gaps, which is where most durable improvement is available.

## 2. Quantify the impact

Duration, users affected, requests failed, revenue impact, data loss, SLA breach. Be concrete — "some users saw errors" gives future readers nothing to weigh.

## 3. Find contributing causes

**There is rarely a single root cause.** Real incidents are several conditions aligning. A search for *the* root cause stops at the first plausible answer and misses the rest.

Ask across these layers:
- **Technical** — what failed, and why did it fail that way?
- **Detection** — why did it take that long to notice?
- **Response** — what slowed diagnosis or mitigation?
- **Systemic** — what made this possible? Missing tests, absent guardrail, unclear ownership, time pressure, a confusing interface?

Use "why" repeatedly, but branch rather than following one chain. When the answer becomes "someone made a mistake", keep going — ask why the system let a single mistake cause this, and why it was not caught.

## 4. Note what went well

Genuinely useful, not a morale exercise. Fast rollback, a good alert, a clear runbook — these are the things to protect and replicate. Post-mortems that only catalogue failures lose the signal about which defences worked.

## 5. Write action items that get done

The most common failure of post-mortems is a list of good intentions nobody completes.

Every action item needs:
- **A specific, verifiable change** — not "improve monitoring" but "add an alert on payment error rate above 1% over 5 minutes"
- **A named owner** — one person, not a team
- **A due date**
- **A priority** tied to recurrence risk

Prioritise by what prevents recurrence or shortens detection. Perfect prevention is often expensive; cutting detection from 40 minutes to 2 is usually cheap and reduces impact more.

Keep the list short. Five items that get done beat twenty that do not.

**Track them to completion in the normal work tracker.** Action items that live only in the post-mortem document are not tracked, and everyone knows it.

## 6. Close the loop

Route procedural action items to `/omniskill:sop-builder` — an action item that never becomes a written procedure gets relearned in the next incident.

Share the post-mortem widely. The learning is worth more across the organisation than in one team's folder.

## Document structure

```
Title · Date · Severity · Duration · Author
Summary            (a few sentences: what broke, who was affected, how it ended)
Impact             (quantified)
Timeline           (timestamped facts)
Contributing causes
What went well
Action items       (change · owner · due date · priority)
Lessons learned
```

## Checks before delivering

- Timeline is timestamped facts from sources, not recollection.
- Impact is quantified.
- Multiple contributing causes, across technical, detection, response, and systemic layers.
- No individual is named as a cause.
- Every action item is specific, owned, and dated.
- Detection and mitigation times are stated.
- Action items are tracked outside this document.
