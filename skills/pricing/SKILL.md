---
name: pricing
description: Pricing and packaging strategy. OmniSkill Finance crew — picks a value metric, designs tiers, sets price points, and models the revenue impact of a change.
disable-model-invocation: true
---

# Pricing

> Packaging + monetization · OmniSkill Finance crew

Pricing is the highest-leverage number in a business. A 1% price increase typically moves operating profit more than a 1% volume increase, because it carries no additional cost.

## 1. Choose the value metric first

Packaging follows from what the customer is charged *per*. Get this wrong and no amount of tier design rescues it.

A good value metric: scales with the value the customer receives, is predictable enough to budget, is something they can count, and grows as they succeed.

| Metric | Fits | Risk |
|---|---|---|
| Per seat | Collaboration tools | Breaks when AI reduces headcount |
| Per usage | Infrastructure, APIs | Unpredictable bills cause churn |
| Per outcome | Payments, ads | Hard to attribute cleanly |
| Flat platform | Simple, low variance | Leaves money on the table at the top |
| Hybrid (platform + usage) | Most modern SaaS | More complex to explain |

Test it: when the customer gets more value, does the bill rise? If not, growth is being given away.

## 2. Anchor on value, not cost

Cost-plus pricing sets a floor and ignores the ceiling. Instead, quantify the economic value delivered — revenue gained, cost avoided, time saved × loaded labour rate — and price at a fraction of it (10–25% is a common capture band).

Cost still matters as a constraint: gross margin must support CAC payback. It just should not set the price.

## 3. Design the tiers

Three tiers is the reliable default. More creates paralysis; fewer forfeits segmentation.

- **Entry** — solves one real problem completely. Not a crippled trial.
- **Core** — where most customers should land. Make it the obvious choice.
- **Enterprise** — security, control, support, SLA. Often "contact us".

Differentiate on *dimensions the customer self-selects into* (volume, seats, advanced capability), not on arbitrary feature removal. Withholding a feature that costs nothing to serve is a tax on trust.

Price ratios of roughly 1 : 3 : 10 across tiers work well. A decoy that makes the middle tier look correct is legitimate design; a decoy nobody could ever want is noise.

**Never gate security behind a tier.** SSO, audit logs, and MFA as upsells push the customers who most need them into the least safe configuration.

## 4. Set the numbers

Willingness to pay is measurable. Van Westendorp's four questions (too cheap / cheap / expensive / too expensive) bracket an acceptable range from as few as 30–50 responses. Conjoint analysis is better where budget allows.

Where no research is possible, triangulate: competitor price points, value-capture fraction, and current discount behaviour. Heavy discounting in practice means list price is above what the market bears.

## 5. Model the change

Never ship a price change unmodelled. Build the scenario in `/omniskill:3-statements` or a standalone `xlsx`:

```
New revenue = existing base × (1 − churn from increase) × new price
            + new customers × conversion change × new price
```

Estimate elasticity honestly, then model a pessimistic case. A 10% increase that loses 5% of customers is strongly accretive; one that loses 25% is not.

Grandfather existing customers, or give at least 60–90 days' notice. Surprise price rises cost more in trust and churn than they collect.

## 6. Test and roll out

Prefer testing on new customers only — price A/B tests on existing accounts create fairness problems that outlive the experiment. Hold the test long enough to capture a full sales cycle.

## Checks before delivering

- The value metric scales with delivered value.
- No security feature is gated behind a paid tier.
- Tier differentiation is on self-selecting dimensions.
- Revenue impact modelled, including a pessimistic elasticity case.
- Migration path for existing customers is stated.

## Scope

Analytical support, not investment or legal advice. Price changes may carry contractual and consumer-protection obligations — route those to `/omniskill:legal`.
