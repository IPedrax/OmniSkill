---
name: compliance
description: Regulatory compliance mapping. OmniSkill Legal crew — determines which regimes apply (GDPR, CCPA, HIPAA, PCI, SOC 2, accessibility, AI rules) and maps obligations to concrete controls.
disable-model-invocation: true
---

# Compliance

> Regulatory checks · OmniSkill Legal crew

**This is analysis, not legal advice.** No attorney-client relationship exists. Compliance positions need a qualified attorney and, for certification, a qualified auditor.

## 1. Determine what applies

Scope is driven by data, users, and activity — not by where the company is incorporated.

| Regime | Triggered by |
|---|---|
| **GDPR / UK GDPR** | Personal data of people in the EU/UK, regardless of company location |
| **CCPA / CPRA** | California residents' data above revenue or volume thresholds |
| **HIPAA** | Protected health information as a covered entity or business associate |
| **PCI DSS** | Storing, processing, or transmitting card data |
| **SOC 2** | Not a law — a customer requirement. Enterprise buyers demand it. |
| **COPPA** | Users under 13. A hard line, not a spectrum. |
| **WCAG / ADA / EAA** | Public-facing digital services |
| **EU AI Act** | AI systems placed on the EU market, tiered by risk |

Sector regimes stack on top: financial services, insurance, education, telecoms each add their own.

## 2. Map obligations to controls

An obligation is not compliance until it is a control someone owns and evidence exists that it runs.

**GDPR core obligations**
- Lawful basis for each processing purpose — consent is only one of six, and often the weakest choice
- Data subject rights: access, deletion, portability, objection, with a one-month response window
- Records of processing activities
- DPIA for high-risk processing
- Breach notification to the supervisory authority within 72 hours
- Data processing agreements with every processor
- Transfer mechanism for data leaving the EEA
- Privacy by design and by default, and data minimisation

**CCPA/CPRA** — notice at collection, opt-out of sale or sharing (including the Global Privacy Control signal), deletion and correction rights, no discrimination for exercising rights.

**SOC 2** — pick trust criteria (security is mandatory), define controls, then run them for the observation window. Type I is a point in time; Type II covers 3–12 months. There is no shortcut: the evidence period must actually elapse.

**Accessibility** — WCAG 2.2 AA is the working standard. Route implementation to `/omniskill:design`; keyboard navigation, contrast, focus visibility, and form labelling catch most of it.

## 3. Gap analysis

For each obligation: current state, required state, gap, remediation, owner, target date.

Rank by regulatory exposure, not by ease. Fixing five easy gaps while leaving an unlawful basis for the core product is motion without progress.

## 4. Evidence

Auditors and regulators test evidence, not intent. Every control needs a record that it operated: policy documents, access review logs, training completion, vendor assessments, incident records, change approvals.

Build evidence collection into the process from the start. Reconstructing twelve months of it retroactively is the most expensive way to run an audit, and often impossible.

## 5. Ongoing

Compliance is a state that decays. Assign owners and review cadence: annual policy review, quarterly access reviews, vendor reassessment on renewal, DPIA on material processing changes, and a breach response plan that has been rehearsed.

## Output

A register: obligation, source regime, applicability, current state, gap, remediation, owner, date, evidence location. Deliver via `/omniskill:xlsx` so it stays a living document rather than a snapshot.

Lead with the gaps that carry real regulatory exposure today.

## Checks before delivering

- Applicability justified per regime, including ones ruled out.
- Jurisdictions named explicitly.
- Every obligation maps to an owned control with evidence.
- Ranked by exposure, not by effort.
- The not-legal-advice scope note is present.
