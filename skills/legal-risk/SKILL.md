---
name: legal-risk
description: Legal exposure review for a product or business plan. OmniSkill Legal crew — sweeps the standard exposure categories before building, ranks by likelihood and impact, and proposes mitigations.
disable-model-invocation: true
---

# Legal Risk

> Flags legal exposure · OmniSkill Legal crew

**This is analysis, not legal advice.** No attorney-client relationship exists. Material findings need a qualified attorney.

Run this **before building**, not after. Exposure found at design time is a design change; the same exposure found at launch is a rewrite, and sometimes a recall.

## Sweep these categories

**Data and privacy**
What personal data is collected, why, where it is stored, who it is shared with, how long it is kept. Cross-border transfer. Children's data (a hard line — under 13 triggers COPPA in the US, and similar rules elsewhere). Biometrics carry their own statutes with statutory damages. Route specifics to `/omniskill:compliance`.

**Intellectual property**
Freedom to operate: does this infringe anything known? Ownership of what is built — contractor agreements without written assignment leave IP with the contractor. Open-source licence obligations, especially copyleft in distributed software. Trademark clearance before committing to a name. Training data provenance for any model.

**Consumer protection**
Advertising claims must be substantiated before publication. Dark patterns in signup or cancellation flows are actively enforced. Auto-renewal disclosure and easy cancellation are statutory in many jurisdictions. Pricing transparency, including all mandatory fees.

**Contracts and commitments**
Terms of service and privacy policy actually fit for the product. Liability caps and disclaimers that survive. SLAs the business can meet. Existing agreements that constrain this plan — exclusivity, non-competes, MFN clauses.

**Employment**
Worker classification (contractor versus employee) is a frequent and expensive error. Non-competes are unenforceable or restricted in a growing number of jurisdictions. Equity and compensation compliance.

**Sector-specific**
Financial services, health, insurance, legal, education, and children's products each carry licensing and disclosure regimes. Identify early whether the product touches a regulated activity — retrofitting a licence is rarely possible.

**Platform and distribution**
App-store rules, API terms of service, and scraping restrictions. Building a business on a platform whose terms forbid it is an existential risk, not a legal footnote.

## Rank the findings

Score likelihood × impact:

| Rating | Meaning | Response |
|---|---|---|
| **Critical** | Likely, and existential | Do not proceed without counsel |
| **High** | Probable and material | Mitigate before launch |
| **Medium** | Possible, manageable | Plan a mitigation |
| **Low** | Unlikely or immaterial | Note and monitor |

Concentrate on what is both likely *and* material. A register where everything is critical gets ignored, and then the genuinely critical item is ignored with it.

## Output

For each finding: what the exposure is, what triggers it, the realistic consequence, likelihood and impact, and a concrete mitigation with an owner.

Mitigations must be actionable. "Consult counsel" is not a mitigation — "add explicit consent before collecting location data, and confirm the wording with counsel" is.

Open with the three things that would actually stop the launch.

## Judgement

Distinguish legal risk from business risk. Most decisions carry some legal exposure, and the answer is rarely "do not do it" — it is "do it this way instead". The value here is in finding the version that works, not in listing reasons to stop.

## Checks before delivering

- Every category swept, including ones that turned out not to apply.
- Jurisdictions named explicitly — answers differ by country and by US state.
- Each finding has a concrete, owned mitigation.
- The three launch-blocking items lead the document.
- The not-legal-advice scope note is present.
