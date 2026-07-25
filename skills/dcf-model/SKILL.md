---
name: dcf-model
description: Discounted cash-flow valuation. OmniSkill Finance crew — builds unlevered free cash flow, WACC, terminal value, and the enterprise-to-equity bridge with a sensitivity grid.
disable-model-invocation: true
---

# DCF Model

> Discounted cash-flow value · OmniSkill Finance crew

Intrinsic value from projected cash flows. Deliver as an `xlsx` workbook with live formulas.

## Before starting

Projections come from `/omniskill:3-statements`. If no operating model exists, build one first — a DCF on invented cash flows is a precise number with nothing behind it.

Establish and write down: valuation date, currency, fiscal year end, forecast horizon (5 years typical, 10 for pre-maturity businesses), and whether the target is enterprise or equity value.

## 1. Unlevered free cash flow

Forecast FCFF for each explicit year:

```
EBIT
− Cash taxes on EBIT        (EBIT × effective tax rate — NOT the reported tax line)
= NOPAT
+ D&A
− Capex
− Increase in net working capital
= Unlevered FCF
```

Rules that decide whether the model is right:

- **Unlevered means unlevered.** No interest expense anywhere. Financing enters through WACC only. Subtracting interest here double-counts the cost of debt.
- Tax on EBIT, not on pre-tax income. The reported tax line already reflects the interest shield.
- Working capital is the *change*, and it is a use of cash when it grows. Drive it off days (DSO, DIO, DPO) against revenue and COGS rather than a flat percentage.
- Capex should converge toward D&A by the terminal year. A business cannot grow forever on capex below depreciation.

## 2. WACC

```
WACC = E/(D+E) × Re  +  D/(D+E) × Rd × (1 − t)
Re   = Rf + β × ERP        (add size or country premium where it applies)
```

- **Rf** — current long-bond yield in the cash flows' currency.
- **β** — unlever peer betas at each peer's own D/E, average, relever at the target's structure. Using a raw peer beta imports that peer's leverage.
- **ERP** — 4.5–6% for developed markets. State the number used.
- **Weights at market value**, not book. Use target capital structure if the current one is temporary.
- **Rd** — the yield the company would issue at today, not the coupon on legacy debt.

## 3. Terminal value

Compute both ways and reconcile:

```
Gordon growth:   TV = FCF(n) × (1 + g) / (WACC − g)
Exit multiple:   TV = EBITDA(n) × peer exit multiple
```

- `g` must not exceed long-run nominal GDP (2–3%). Above that the business eventually becomes the economy.
- `WACC − g` in the denominator makes TV explosive as they converge. If `WACC − g < 2%`, say so.
- Back out the implied exit multiple from the Gordon result. If it is far from peers, an assumption is wrong.
- Expect TV to be 60–80% of total value. Above ~85%, the explicit forecast is doing no work — extend the horizon.

## 4. Discount and bridge

Discount each year and the TV at WACC. Use the **mid-year convention** (`t − 0.5`) when cash flows arrive evenly through the year; it raises value a few percent and is standard for operating businesses.

```
Enterprise value
− Total debt
− Preferred, minority interest, unfunded pension
+ Cash and equivalents
= Equity value
÷ Diluted shares (treasury method on options)
= Value per share
```

## 5. Sensitivity and honesty

Always output a WACC × `g` grid (±1% WACC, ±0.5% `g`). One number implies false precision; the grid shows how load-bearing the assumptions are.

State the two or three assumptions the answer actually hinges on. Where the range is wide, say it is wide — that is the finding, not a failure.

## Checks before delivering

- Interest expense appears nowhere in FCFF.
- Terminal `g` ≤ long-run GDP, and `WACC − g` ≥ 2%.
- Implied exit multiple is within peer range.
- TV is 60–85% of enterprise value.
- Capex ≈ D&A in the terminal year.
- Cross-check against `/omniskill:comps-analysis`; a wide gap is a finding to report.

## Scope

Analytical support, not investment advice. Every figure rests on stated assumptions and warrants professional review before anyone acts on it.
