---
name: email-sequences
description: Lifecycle email flows. OmniSkill Social crew — designs onboarding, nurture, and win-back sequences with trigger logic, exit conditions, and the compliance rules that apply.
disable-model-invocation: true
---

# Email Sequences

> Lifecycle email flows · OmniSkill Social crew

Automated sequences triggered by behaviour, not broadcast sends.

## Design the flow before writing a single email

Specify, in this order:

1. **Trigger** — the event that starts it (signed up, abandoned cart, went inactive 30 days)
2. **Goal** — the one action it exists to drive
3. **Exit condition** — what removes someone from the sequence
4. **Timing** — delay between each send
5. **Branches** — behaviour-based paths

**The exit condition is the most-forgotten piece and the most damaging.** Someone who converts on email 2 must stop receiving emails 3–5 telling them to convert. Nothing erodes trust faster than a sequence that ignores what the recipient already did.

## The core sequences

**Onboarding / welcome** — highest engagement email will ever get; do not waste it.

1. *Immediate:* deliver what was promised, set expectations, one clear next step
2. *Day 1–2:* the fastest path to first value — the single action correlating with retention
3. *Day 3–5:* second core use case, with proof
4. *Day 7:* address the most common blocker
5. *Day 10–14:* the conversion ask, once the product has actually been experienced

Drive to **activation**, not to a purchase. Someone who has not reached first value will not convert, and asking early costs the relationship.

**Abandoned cart / trial** — highest-ROI sequence in commerce.
1. *1 hour:* a helpful reminder, no discount
2. *24 hours:* handle the objection — shipping, returns, security
3. *72 hours:* urgency if genuine, incentive only if necessary

Never discount at step one. It teaches people to abandon deliberately.

**Nurture** — value first. A ratio of roughly four useful emails to one ask. Segment by interest, and send less to those not engaging rather than more.

**Win-back** — for genuinely inactive contacts.
1. "Here is what changed"
2. A direct incentive or a genuine question
3. A permission check: "Still want these?" — and honour the answer by removing them.

Cleaning a list improves deliverability for everyone remaining. A shrinking, engaged list outperforms a large, dead one.

## Write the emails

**Subject line** — 30–50 characters, specific, no clickbait. It sets the expectation the body must meet.

**Preview text** — extends the subject; never leave it to default to the first line of boilerplate.

**One idea, one call to action.** Multiple asks reduce all of them.

**Short.** Most lifecycle email should be under 150 words. Long-form nurture is the exception, not the default.

**Plain-text-feeling** beats heavy templates for lifecycle mail — it reads as a message rather than a campaign, and it renders reliably everywhere.

**From a person**, with a real reply-to that someone monitors.

## Compliance — not optional

- **Consent.** Opt-in only, unticked. GDPR requires a lawful basis; consent must be freely given and recorded.
- **Unsubscribe** in every message, one click, honoured within days. Never hidden, never requiring a login.
- **Physical postal address** in the footer, required by CAN-SPAM.
- **Accurate headers and subject lines.** Misleading subjects are illegal, not merely bad practice.
- **Separate transactional from marketing.** Transactional messages have different rules; do not smuggle marketing into a receipt.

Route specifics to `/omniskill:compliance`.

## Deliverability

Authenticate the domain: **SPF, DKIM, and DMARC**. Without these, mail lands in spam regardless of content quality — this is the first thing to check when a sequence underperforms.

Warm new sending domains gradually. Monitor bounce and complaint rates; above 0.1% complaints, stop and fix the source. Remove hard bounces immediately. Prune unengaged contacts on a schedule.

## Measure per email, not per sequence

Open rates are unreliable post-privacy-changes — use them directionally at best. Track click rate, conversion rate, unsubscribe rate per email, and overall sequence completion.

A single email with an elevated unsubscribe rate is a specific, fixable problem. Sequence-level averages hide it.

## Output

Flow diagram with triggers, delays, branches, and exit conditions. Full copy per email with subject and preview text. Segmentation rules. Measurement plan.

## Checks before delivering

- Every sequence has an explicit exit condition.
- Consent is opt-in and recorded.
- One-click unsubscribe and postal address present.
- SPF, DKIM, DMARC configured.
- One call to action per email.
- Onboarding drives activation before conversion.
