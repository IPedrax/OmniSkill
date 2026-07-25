---
name: lbo-model
description: Leveraged-buyout model. OmniSkill Finance crew — sources and uses, debt tranching, cash sweep, covenant headroom, and IRR attribution across deleveraging, multiple expansion, and EBITDA growth.
disable-model-invocation: true
---

# LBO Model

> Leveraged-buyout math · OmniSkill Finance crew

Returns to a sponsor acquiring with debt. Deliver as an `xlsx` workbook with live formulas.

## The question

An LBO does not ask what a business is worth. It asks: *at what entry price does this deal clear the sponsor's return hurdle?* Often the model is run backwards from a target IRR to solve for the price.

## 1. Entry: sources and uses

**Uses** — purchase equity value + refinanced debt + transaction fees + financing fees.
**Sources** — new debt by tranche + sponsor equity (the plug) + any rollover equity.

Sources must equal uses exactly.

Entry EV = entry multiple × LTM EBITDA. State whether the multiple is on LTM or forward EBITDA — mixing them silently misprices the deal.

## 2. Debt structure

Stack tranches cheapest and most senior first:

| Tranche | Typical | Amortisation | Pricing |
|---|---|---|---|
| Revolver | liquidity only | none | SOFR + 250–350, undrawn fee |
| Term Loan A | 1–2× EBITDA | 5–10%/yr | SOFR + 250–350 |
| Term Loan B | 2–4× EBITDA | 1%/yr, bullet | SOFR + 350–500 |
| Senior notes | 1–2× EBITDA | bullet | fixed 6–9% |
| Mezzanine / PIK | as needed | bullet | 10–14%, often accrues |

Total leverage typically 4–6× EBITDA; above 6× needs justification. Sponsor equity is usually 30–50% of capitalisation.

## 3. Operating model and cash sweep

Project 5 years of EBITDA from `/omniskill:3-statements`, then:

```
EBITDA − cash interest − cash taxes − capex − Δ working capital − mandatory amortisation
= cash available for sweep
```

Sweep pays down the most senior tranche first, subject to the sweep percentage (75–100% of excess cash, often stepping down as leverage falls). Maintain a minimum cash balance — do not sweep the company to zero.

Interest on average balances creates the same circularity as any levered model; resolve it the same way (iterative calculation, or opening-balance interest).

## 4. Covenants

Track headroom every period, not just at entry:

- **Leverage:** net debt / EBITDA below the stepping-down maximum.
- **Interest coverage:** EBITDA / cash interest above the minimum.
- **Fixed-charge coverage** where the facility requires it.

Flag any period that breaches. A deal that trips a covenant in year 2 is not a deal, regardless of its IRR.

## 5. Exit and returns

Exit EV = exit multiple × exit-year EBITDA. **Default to exit multiple = entry multiple.** Assuming expansion is assuming the market rerates in the sponsor's favour — if the model needs that to work, the deal depends on luck.

```
Exit equity = exit EV − net debt at exit
MoIC        = exit equity / sponsor equity
IRR         = (MoIC)^(1/years) − 1        (use XIRR for uneven timing)
```

## 6. Attribution — the part that matters

Split the equity gain into its three sources:

1. **Deleveraging** — debt repaid with operating cash.
2. **EBITDA growth** — entry multiple × EBITDA increase.
3. **Multiple expansion** — EBITDA at exit × multiple change.

This is the most useful output of the whole model. A deal carried by deleveraging and EBITDA growth is underwritable. A deal carried by multiple expansion is a bet on the market, and should be labelled as one.

## 7. Sensitivities

Grid IRR against entry multiple × exit multiple, and against leverage × EBITDA growth. Report the entry price at which IRR hits the hurdle (typically 20–25%).

## Checks before delivering

- Sources = uses exactly.
- No covenant breach in any period, or breaches flagged explicitly.
- Cash never negative; revolver draws when needed.
- Exit multiple ≤ entry multiple unless expansion is argued for in writing.
- Attribution sums to the total equity gain.

## Scope

Analytical support, not investment advice. Structure and pricing assumptions must be stated and professionally reviewed.
