---
name: 3-statements
description: Full 3-statement financial model. OmniSkill Finance crew — links income statement, balance sheet, and cash flow so the balance sheet ties to zero.
disable-model-invocation: true
---

# 3-Statement Model

> Full 3-statement model · OmniSkill Finance crew

The operating model every other finance skill feeds from. Deliver as an `xlsx` workbook with live formulas.

## The discipline

Three statements, fully linked, balancing every period. If the balance sheet does not tie, the model is broken — there is no partial credit and no "close enough".

## 1. Assumptions tab first

One tab, every driver, nothing hardcoded elsewhere. Colour inputs differently from formulas. Every hardcoded number buried in a formula is a bug waiting for the user who tries to change an assumption.

Drivers: revenue growth or volume × price, gross margin, opex as % of revenue or fixed + step, capex, depreciation life, working-capital days (DSO / DIO / DPO), tax rate, interest rates, dividend policy.

## 2. Income statement

```
Revenue → COGS → Gross profit → Opex → EBITDA
→ D&A → EBIT → Interest → EBT → Tax → Net income
```

Drive revenue off units and price where possible. A single growth percentage hides the operating story.

## 3. Supporting schedules

Build these before the balance sheet — they are what makes it tie.

- **Debt schedule** — opening balance, draws, repayments, closing. Interest on average balance.
- **PP&E schedule** — opening, + capex, − depreciation, closing.
- **Working capital** — from days: `AR = DSO/365 × revenue`, `Inventory = DIO/365 × COGS`, `AP = DPO/365 × COGS`.
- **Equity** — opening, + net income, − dividends, +/− issuance, closing.

## 4. Cash flow statement

```
Net income
+ D&A                            (non-cash add-back)
− Increase in working capital    (growth consumes cash)
= Cash from operations
− Capex                          = Cash from investing
+ Debt draws − repayments − dividends + equity issued = Cash from financing
= Net change in cash
+ Opening cash = Closing cash
```

## 5. The linkages

These four are the whole model. Get them right and it balances; get one wrong and it never will.

1. Net income → retained earnings on the balance sheet.
2. Closing cash on the cash flow → cash on the balance sheet.
3. Closing balances from every schedule → their balance sheet lines.
4. D&A appears in both the income statement and as a cash-flow add-back.

## 6. Balance and circularity

```
Assets = Liabilities + Equity        (difference must be exactly 0)
```

Put a check row on every model tab, every period. Make it loud — conditional formatting that goes red on any non-zero.

**Circularity:** interest depends on debt, debt depends on cash, cash depends on interest. Two options:

- Enable iterative calculation (Excel: File → Options → Formulas, max 100 iterations, 0.001 precision).
- Or compute interest on the *opening* balance, which breaks the loop with a defensible simplification. Prefer this when the model will be handed to others — iterative calculation silently returns zeros when the setting is off on their machine.

## 7. Sanity checks

- Balance check = 0 in every period.
- Margins trend plausibly — no silent expansion to 90% gross margin.
- Cash never goes negative without a revolver drawing to cover it.
- Working capital days stay near historicals unless a change is deliberate and stated.
- Debt paydown respects the actual amortisation schedule.

## Downstream

Feeds `/omniskill:dcf-model` (FCFF), `/omniskill:lbo-model` (EBITDA and cash sweep), and `/omniskill:business-case`.

## Scope

Analytical support, not investment or accounting advice. Assumptions must be stated and professionally reviewed.
