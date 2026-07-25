---
name: contract-review
description: Clause-by-clause contract review. OmniSkill Legal crew — works through the standard risk clauses, ranks findings by severity, and drafts redline language.
disable-model-invocation: true
---

# Contract Review

> Clause-by-clause review · OmniSkill Legal crew

**This is analysis, not legal advice.** No attorney-client relationship exists. Output identifies issues and drafts language for a qualified attorney to review. State this in the deliverable.

## 1. Frame it before reading

Establish: which side the review is for, what the deal is worth, whether this is the counterparty's paper or ours, and how much leverage exists. The same clause is acceptable in a $5k pilot and unacceptable in a $2M multi-year commitment.

Read the whole document once before commenting. Defined terms and cross-references change what individual clauses mean, and a review written linearly misses that.

## 2. The clause checklist

Work through every one. Note absence as loudly as presence — a missing liability cap is worse than a high one.

**Money**
- Fees, payment terms, late interest, currency, who bears taxes
- Price escalation — is it capped, indexed, or open-ended?
- Renewal pricing: uncapped increases at renewal are a common trap

**Term and exit**
- Initial term, renewal mechanism, notice period
- **Auto-renewal** with a long notice window is the single most common unfavourable term. A 12-month renewal requiring 90 days' notice means a missed diary entry costs a year.
- Termination for convenience — mutual, or one-sided?
- Termination for cause: cure period, what survives

**Liability**
- Limitation of liability: cap amount and how it is measured (fees paid in prior 12 months is standard)
- Mutual or one-sided? One-sided caps favouring the drafter are a red flag
- Consequential damages waiver — mutual?
- Carve-outs from the cap: confidentiality, indemnity, IP infringement, gross negligence. Uncapped carve-outs can swallow the cap entirely.

**Indemnity**
- Who indemnifies whom, for what, and is it mutual?
- Scope: third-party claims only, or direct claims too? Direct-claim indemnities are aggressive.
- Control of defence and settlement consent

**IP**
- Ownership of pre-existing IP, and of anything created under the agreement
- Licence scope: exclusive, territory, sublicensable, perpetual?
- Feedback clauses assigning improvements to the counterparty
- For services: work-for-hire versus assignment

**Data and confidentiality**
- Definition breadth, term of obligation, permitted disclosures
- Data processing terms, security obligations, breach notification timing
- Sub-processors, cross-border transfer — route to `/omniskill:compliance`

**Operational**
- SLA: uptime, remedy (service credits are usually the sole remedy), measurement method
- Assignment and change of control
- Governing law and venue — a foreign venue can make enforcement uneconomic regardless of who is right
- Dispute resolution: arbitration, class waiver, jury waiver
- Publicity and logo rights

## 3. Rank by severity

| Severity | Meaning |
|---|---|
| **Critical** | Do not sign. Unbounded liability, IP loss, no exit. |
| **High** | Negotiate before signing. Material and likely to bite. |
| **Medium** | Push for it; accept if leverage is limited. |
| **Low** | Note it. Not worth spending negotiating capital on. |

Severity is likelihood × impact against *this* deal. Flagging everything as critical is the same as flagging nothing.

## 4. Output

For each finding: clause reference, quoted text, plain-English explanation of the exposure, severity, and proposed replacement language. Deliver the redline through `/omniskill:docx` with tracked changes plus a summary of what changed and why — a marked-up document with no rationale invites rejection.

Open with an executive summary: the three things that matter, and a sign / negotiate / do-not-sign recommendation.

## 5. Judgement

Distinguish market-standard from aggressive. A mutual liability cap at 12 months' fees is normal and does not need a paragraph. Reserve attention for terms that are genuinely off-market, and say plainly when a term *is* standard — a review that objects to everything gets ignored entirely.

## Checks before delivering

- Every checklist category addressed, including absent clauses.
- Severity reflects this deal's size and leverage.
- Every critical and high finding has proposed replacement language.
- The not-legal-advice scope note is present.
