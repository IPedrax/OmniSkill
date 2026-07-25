---
name: comps-analysis
description: Comparable-company analysis. OmniSkill Finance crew — builds a defensible peer set, calculates trading multiples on a like-for-like basis, and applies the range to a target.
disable-model-invocation: true
---

# Comps Analysis

> Comparable-company set · OmniSkill Finance crew

Relative valuation: what the market pays for similar businesses today. Deliver as an `xlsx` workbook.

## 1. Build the peer set

Screen on business model first, sector label second. A vertical SaaS company is not comparable to a hardware maker merely because both are tagged "technology".

Match on: revenue scale (roughly 0.3–3× the target), growth rate, margin profile, business model and revenue mix, geography, and capital intensity.

Six to twelve peers is the working range. Fewer is not a distribution; more means the screen is too loose. Justify each inclusion in one line, and — just as important — record why obvious candidates were excluded.

## 2. Calculate multiples like-for-like

```
Equity value (market cap) = share price × diluted shares (treasury method)
Enterprise value = equity value + total debt + preferred + minority interest − cash
```

| Multiple | Use for |
|---|---|
| EV / Revenue | Unprofitable or high-growth companies |
| EV / EBITDA | The default for most operating businesses |
| EV / EBIT | Where capital intensity differs sharply across peers |
| P / E | Financials, and mature businesses with stable structure |

**The consistency rule:** enterprise-value multiples take pre-interest metrics (revenue, EBITDA, EBIT); equity-value multiples take post-interest metrics (net income, EPS). Pairing EV with net income is the classic error and produces a meaningless number.

Use the same period for every peer — all LTM or all NTM, never mixed. Note which.

## 3. Normalise

Strip one-time items so the multiples compare operations, not accidents: restructuring, impairments, legal settlements, gains on disposal. Adjust for stock-based compensation consistently — either expensed for all peers or added back for all, stated either way.

Where lease accounting differs materially (IFRS 16 vs. US GAAP treatment), adjust or flag it.

## 4. Apply to the target

Report the peer distribution — min, 25th percentile, median, 75th, max — and use the **median**, not the mean. One outlier drags a mean and the median ignores it.

Position the target within the range on evidence: above median if it grows faster or earns better margins than peers, below if the reverse. Say which, and why, in a sentence. An unexplained premium is an assumption pretending to be an answer.

```
Implied EV     = target metric × selected multiple
Implied equity = implied EV − net debt
Per share      = implied equity / diluted shares
```

## 5. Report honestly

Give a range, not a point. Show the peer table so the reader can judge the set themselves — a comps output that hides its peers cannot be checked.

Cross-check against `/omniskill:dcf-model`. When the two disagree materially, that gap *is* the finding: either the market prices something the projections miss, or the projections assume something the market does not believe. Say which you think it is.

## Checks before delivering

- Every peer has a stated reason for inclusion.
- EV multiples use pre-interest metrics only.
- Same period basis across all peers.
- Median used, not mean.
- Target's position versus median is explained.
- Cross-checked against a DCF where one exists.

## Scope

Analytical support, not investment advice. Market data must be dated, sourced, and professionally reviewed.
