---
name: business-case
description: ROI and business cases. OmniSkill Operations crew — quantifies costs and benefits honestly, computes NPV, payback, and IRR, and states what would have to be true.
disable-model-invocation: true
---

# Business Case

> ROI + business cases · OmniSkill Operations crew

Justifying spend — a tool, a hire, a project — with numbers that survive scrutiny.

## The failure mode to avoid

Most business cases are advocacy dressed as analysis: the conclusion is chosen first, then benefits are inflated and costs omitted until the number works.

This is obvious to reviewers, and it destroys credibility for every future case. Build the honest version. If the honest version does not clear the bar, that is the finding — and delivering it is worth more than winning one approval.

## 1. State the decision

What is being decided, what happens if nothing is decided, and by when. A business case without a decision date is a document nobody has to act on.

## 2. Count every cost

Omitted costs are the most common defect.

**One-time:** licences or purchase, implementation, migration, integration, training, hardware, consultants.

**Ongoing (annual):** subscription, maintenance, support, hosting, and the **internal labour to operate it** — the cost most often left out.

**Hidden:** productivity dip during transition, opportunity cost of the team's time, switching cost if it fails, contract exit cost.

Use fully loaded labour rates — salary plus benefits, taxes, and overhead, typically 1.25–1.4× salary. Using base salary understates every people cost in the model.

## 3. Quantify benefits conservatively

**Hard benefits** — direct and measurable: cost reduction, revenue increase, avoided hire, reduced error cost.

**Soft benefits** — real but hard to measure: morale, risk reduction, optionality. **List them separately and do not put them in the ROI number.** Mixing them is what makes a case unbelievable.

For time savings, be honest about conversion. Ten people saving 2 hours a week is 1,040 hours a year — but that only becomes money if those hours go to something valuable or a hire is genuinely avoided. Saying so plainly is what makes the rest of the case credible.

Apply a realisation factor. Benefits rarely arrive at 100% on day one: ramp 50% in year 1, 80% in year 2, 100% thereafter is a defensible default.

## 4. Do the math

```
Net benefit (per year) = benefits − costs

NPV = Σ [ net benefit(t) / (1 + r)^t ] − initial investment
      r = the organisation's discount rate or hurdle rate

Payback period = time until cumulative net benefit turns positive
IRR = discount rate at which NPV = 0
ROI = (total benefit − total cost) / total cost
```

Use a 3-year horizon for software, 5 for infrastructure. Longer horizons make anything look good and nobody believes them.

**NPV is the decision metric.** ROI ignores timing; payback ignores everything after it. Report all three, decide on NPV.

## 5. Compare real alternatives

Always include:
- **Do nothing** — the baseline, with its own cost. Doing nothing is never free.
- **The cheapest workable option**
- **The proposed option**
- **A build-versus-buy comparison** where relevant

A case with one option is a proposal, not an analysis.

## 6. Be explicit about uncertainty

State the two or three assumptions the answer depends on. Run a pessimistic case: benefits at 50%, costs at 130%. If it still clears the hurdle, the case is strong. If it collapses, say so — that is the most valuable sentence in the document.

**Invert it:** state what would have to be true for this to be the wrong decision. That framing surfaces the real risk faster than any sensitivity table.

## 7. Deliver

One page for the decision-maker: the ask, the NPV and payback, the top risk, and the recommendation. The model behind it, in `/omniskill:xlsx` with live formulas, so a reviewer can change an assumption and see the result move.

## Checks before delivering

- Internal labour cost included, fully loaded.
- Soft benefits listed separately, excluded from ROI.
- Realisation ramp applied to benefits.
- "Do nothing" costed as an option.
- NPV, payback, and IRR all reported.
- Pessimistic case run and stated.
- Key assumptions named explicitly.

Financial modelling detail belongs in `/omniskill:3-statements`.
