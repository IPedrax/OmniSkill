---
name: cro
description: Conversion rate optimization. OmniSkill Marketing crew — finds where visitors drop out of a page or form, prioritizes fixes, and designs tests that produce trustworthy results.
disable-model-invocation: true
---

# CRO

> Lift page + form conversion · OmniSkill Marketing crew

Traffic arrives and does not convert. Fix the leak rather than buying more traffic to pour into it.

## 1. Find the leak before proposing fixes

Guessing at CRO fixes is how teams spend a quarter redesigning a page that was never the problem.

Build the funnel and find the biggest drop:

```
Visitors → engaged → started form → completed form → activated
```

Then look at:
- **Segments** — device, source, geography, new vs. returning. Mobile converting at a third of desktop is a specific, findable bug.
- **Session recordings** — watch 10–20 sessions that failed to convert. Nothing else surfaces confusion this fast.
- **Form analytics** — per-field drop-off and error rates. One field usually dominates.
- **Speed** — measure it. Conversion falls measurably with every second of load time.

## 2. The usual causes, in rough order of frequency

**Message mismatch.** The ad promised one thing, the landing page says another. Check the actual ad copy against the actual headline — this is the most common and most fixable cause.

**Unclear value proposition.** A visitor should know what this is, who it is for, and what it does within about five seconds. If the headline is a slogan rather than a statement, that is the problem.

**Friction in the form.** Every field costs completions. Ask only for what is needed *now*; the rest can be collected later. Phone-number and company-size fields on a first-touch form are expensive.

**Missing trust.** Unfamiliar brand, asking for payment or personal data, no social proof, no security signals, no clear refund or privacy statement.

**Weak or competing calls to action.** Multiple equal-weight CTAs split attention. One primary action per page, visually dominant, in specific language ("Start free trial") rather than generic ("Submit").

**Mobile experience.** Tap targets too small, form fields triggering the wrong keyboard, fixed elements covering inputs, horizontal scroll.

**Unanswered objections.** Price, contract length, data handling, switching cost. An unanswered objection is a silent exit.

## 3. Fix the form specifically

- Cut every non-essential field. Ask for the minimum, then progressively profile.
- Correct input types (`type="email"`, `type="tel"`) so mobile keyboards match.
- Inline validation on blur, not on submit, with errors next to the field in plain language.
- Never clear a form on error.
- Autofill attributes on everything.
- Single column. Multi-column forms measurably slow completion.
- Multi-step with a progress indicator for anything long — it outperforms one intimidating page.
- Label the effort honestly: "Takes about 2 minutes".

## 4. Test properly

Calculate the sample size **before** starting, from baseline rate and the minimum lift worth detecting. Underpowered tests produce confident noise.

- Run full weeks — weekday and weekend behaviour differ.
- Do not stop early because the result looks good. Peeking and stopping at significance is the most common way teams ship changes that do nothing.
- Test one substantial change at a time unless running a proper multivariate design.
- Expect most tests to be flat. That is normal and still informative.

Below roughly 1,000 conversions per month, A/B testing will rarely reach significance. Fix obvious usability problems directly instead — that is a legitimate strategy, not a compromise.

## 5. Prioritise

Score each hypothesis on expected impact, confidence in the evidence, and effort. Start where the funnel drop is largest, not where the fix is easiest.

## Output

Funnel with drop-off rates, the top three leaks with evidence, hypotheses ranked, and a test plan with required sample size and duration for each.

## Checks before delivering

- The leak is located with data, not assumed.
- Recommendations tie to specific evidence.
- Sample size and duration calculated per test.
- Mobile examined separately.
- Where traffic is too low to test, that is stated with a direct-fix path instead.

Pair with `/omniskill:mktg-psychology` for the behavioral layer and `/omniskill:copywriting` for the rewrite.
