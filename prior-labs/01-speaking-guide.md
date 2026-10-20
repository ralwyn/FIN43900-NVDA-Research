# Lab 12 — NVIDIA speaking guide

Prepared October 1, 2026. This is an AI-assisted preparation guide built from saved coursework, not a record that the presentation or partner review has occurred. Review and adapt the wording to your own understanding. The class worksheet asks you to keep AI closed during the live presentation and questioning. The 15-minute plan below includes opening evidence and walking through calculations; it is not 15 minutes of scripted reading.

## Start with the conclusion — 45 seconds

> My conclusion is still watch and defer. NVIDIA has a strong business, but that does not automatically make the stock a good value. My model gives about $149 per share, compared with the saved price of about $224. Revenue growth has the biggest effect over the ranges I tested. Before making a stronger investment call, I would investigate whether the growth assumptions are realistic and update the valuation to a consistent date.

**Keep the basis beside the number:** $148.73 USD/share; Lab 10 prepared September 24, 2026; annual cash flows discounted to FY2026 end, not a precise September 24 or October 1 valuation. Shares: 24.1 billion, post-split. Saved comparison: $224.20 intraday September 24 at 2:05 PM EDT. Do not call that today's stock price.

## 1. Why NVIDIA? — 1 minute 15 seconds

Open [original target-selection rationale](evidence/Project_1_Valuation_Edition_A_NVDA.md), “Company and valuation date” and “Known evidence.”

> I selected NVIDIA because it stood out for growth and cash generation in my original screen. It also gave me a clear business question: how long can AI demand support its growth? I did not want to assume that a strong company was automatically a cheap stock. My original view was watch and defer until I had a valuation.

The saved screening rationale says NVIDIA remained first when the revenue-growth threshold increased from 5% to 15%. Treat that as a saved screening result, not a newly rerun screen. Its provider metrics required reconciliation before valuation.

**Show ownership:** point to the original “watch and defer” conclusion, then explain that the later model adds quantitative evidence without turning the early screen into a buy recommendation.

## 2. What earns the money, and what evidence supports it? — 2 minutes

Open [company research](evidence/NVIDIA_2026-09-03_report.md) and [Lab 10 source table](evidence/lab10-nvda-report.md).

> NVIDIA sells chips, networking, systems, and software used for accelerated computing. The main business question in my analysis is spending on AI infrastructure. If customers keep buying more computing capacity and NVIDIA keeps winning that spending, revenue can grow. If customers cut spending or choose alternatives, growth can fall below my forecast.

Use these saved annual figures, all **USD millions**:

| FY2026 item | Amount | Evidence to show |
|---|---:|---|
| Revenue | 215,938 | FY2026 10-K, income statement, printed p. 51 |
| Operating cash flow | 102,718 | FY2026 10-K, cash-flow statement, printed p. 55 |
| Cash purchases of PP&E and intangibles | 6,042 | Same cash-flow statement |
| Inventory | 21,403 | FY2026 10-K, balance sheet, printed p. 53 |

[FY2026 filing](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), year ended January 25, 2026. These figures are carried from the saved Lab 10 evidence; no October 1 market-data refresh is claimed.

**Precision correction:** early research used a rounded $6.1bn capex figure from its liquidity discussion. The implemented model's historical cash-flow measure is $6.042bn for purchases of PP&E and intangibles. Use the specific cash-flow line when explaining the model; do not mix definitions casually.

> The risk I focus on is growth coming in below expectations. Customers may slow AI spending, competitors may win sales, and export restrictions may limit markets. That matters because my valuation depends heavily on the revenue path.

## 3. How history becomes the pro-forma — 3 minutes

Open [assumption table](evidence/lab10-nvda-report.md), then [visible statements and checks](evidence/lab10-nvda-output.txt).

| Input | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---:|---:|---:|---:|---:|
| Revenue growth | 87.39% | 35% | 25% | 15% | 8% |
| Gross margin | 74% | 73% | 72% | 71% | 70% |
| R&D / revenue | 8% | 9% | 10% | 11% | 12% |

> I start with the company's history, but I do not assume the unusually high historical growth continues forever. Growth slows as the revenue base gets larger. Margins also decline gradually to allow for competition and changes in the business. These are forecast judgments, not facts guaranteed by management.

FY2027 revenue uses saved H1 actual revenue of 177,837 + Q3 guidance midpoint of 108,000 + Q4 judgment of 118,800 = **404,637**. The Q4 figure and later growth fade are judgments. Holding 17% taxes and 3% capex/revenue through the forecast is also judgment.

> Revenue determines gross profit. SG&A and R&D reduce that to operating profit. Interest and tax lead to net income. Then I adjust for noncash expenses, working capital, investment, and financing to get cash flow to equity. Cash is the result of those flows. I do not force cash to make the balance sheet balance.

Point to one year's balance-sheet gap and cash-reconciliation gap: both print zero within the $0.000001m tolerance. Checks also cover equity, PP&E, intangibles, income statement, debt, the FCFE bridge, minimum cash, and borrowing limits.

**If asked about depreciation:** D&A is already embedded in the expense ratios. It is added back in operating cash flow and reduces the relevant asset balances. It must not be subtracted twice from profit.

**If asked about compensation:** the model treats stock compensation as a cash-equivalent expense and does not add it back while keeping shares fixed. This is a simplifying economic treatment, not a full forecast of reported stock compensation and dilution.

## 4. Valuation, peers, and reverse DCF — 4 minutes

### Explain the DCF

> My implemented model values cash flow to equity, or FCFE. I discount the cash available to shareholders at a 12% cost of equity and use 3% long-run growth. Those rates are assumptions. The model gives $148.73 per share.

The September 3 research plan proposed FCFF and WACC. The later implemented Lab 10 model uses **FCFE and cost of equity**. Explain that change openly: these are different frameworks, and the rate and cash-flow definition must match.

| Bridge component | USD millions |
|---|---:|
| Present value of five explicit forecast years | 996,554.47 |
| Present value of terminal cash flows | 2,513,571.28 |
| Opening excess cash and financial investments | 74,244.25 |
| Equity value | 3,584,369.99 |
| Shares, millions | 24,100 |
| Value, USD/share | 148.73 |

Totals are rounded for display. Terminal value contributes about **70%** of equity value. That makes terminal margins, growth, reinvestment, and the required return consequential.

> Because this is already an equity cash-flow valuation, I do not subtract debt a second time. I add the opening nonoperating financial assets once. I also do not add future accumulated cash again, because the cash flows that create it are already valued.

Terminal growth is supported by reinvestment: terminal net capex = 3% × ending productive assets; terminal working-capital investment = 3% × ending operating working capital. The terminal model does not assume free growth.

### Explain the peer disagreement

Open [Lab 08 peer analysis](evidence/lab08_nvda_research_and_reflection.md).

> I used AMD and Broadcom because they overlap with NVIDIA in AI computing or networking. But neither is a perfect match. AMD has other chip businesses, and Broadcom has a large software business. Applying their reported P/E ratios gives very high and very different results. I treat those as a warning to check comparability, not as proof that my DCF is wrong.

| Saved peer reference | Calculation | NVIDIA implied price |
|---|---|---:|
| AMD | $456.16 / $2.65 × NVIDIA EPS $4.90 | $843.47 |
| Broadcom | $357.16 / $4.77 × NVIDIA EPS $4.90 | $366.89 |

These use **September 3, 2026 closing prices and reported annual diluted EPS**, not the September 24 quote or the model's fixed 24.1bn share count. Business mix, annual reporting periods, tax effects, and future-growth expectations weaken comparability. Do not average these references with the DCF to produce a price target.

### Explain the reverse DCF

Open [new reverse-DCF output](reverse-dcf-output.txt).

> I also asked what growth path would make the existing model reach the saved $224.20 price. Holding the other assumptions fixed, it takes about 12.9 extra percentage points of growth in every forecast year. That is a much stronger path than my base case. It is one way to explain that price within this model, not proof of what every investor expects.

Implied growth: **100.28%, 47.89%, 37.89%, 27.89%, 20.89%** in FY2027–FY2031. Fixed: margin path, cost ratios, taxes, working-capital ratios, reinvestment policy, financing, 12% cost of equity, 3% terminal growth, and 24,100m shares. Linked quantities still recalculate.

**Provenance and limits:** this is a new October 1 preparation supplement, not a recovered Week 3 run. The original Week 3 DCF/reverse result was not found. The annual valuation anchor differs from the quote date; shifting FY2027 growth also changes a full-year outcome when part of that year was already known. It is a diagnostic, not an updated market valuation. It passes accounting checks and restores base.

## 5. Which assumptions matter? — 2 minutes 15 seconds

Open [Lab 11 visible results](evidence/lab11-nvda-output.txt).

> I changed one assumption at a time. Growth moved five percentage points up or down in each forecast year. Gross margin moved two points up or down. Growth had the larger effect on profit, cash flow, and value over those ranges. That is partly because growth compounds across years.

| Tested driver | FY2031 operating-profit span | FY2031 FCFE span | Value/share span |
|---|---:|---:|---:|
| Growth ±5 percentage points/year | $184.00bn | $128.75bn | $48.74 |
| Margin ±2 percentage points/year | $32.91bn | $27.78bn | $10.64 |

FCFE impact is about **4.64×** as large for growth over these ranges. A span is maximum minus minimum across lower/base/higher valid results. It does not assign a likelihood to either endpoint. These ranges were proposed as judgments during AI-assisted preparation; explain and defend them rather than calling them company guidance.

**Trace this result:** higher gross-margin path 76/75/74/73/72%, compared with base 74/73/72/71/70%. Final-year revenue remains $848,068.57m. Operating profit rises **$16,452.53m**, FCFE rises **$13,888.70m**, and value rises from **$148.7290 to $154.0513/share**.

> Higher margin gives more gross profit from the same sales. SG&A and taxes take some of that increase. Inventory and payables also change because the cost of revenue changes. The cash-flow gain is therefore different from the profit gain.

Hand check: operating-profit change = $848,068.57m × 0.02 × (1 − 0.03) ≈ **$16,452.53m**. SG&A is 3% of gross profit in FY2031. Final-year FCFE difference = $383,452.568968m − $369,563.869049m = **+$13,888.699919m**, subject to displayed rounding.

> A larger sensitivity does not automatically mean an input is more uncertain. Sensitivity tells me how much an assumption matters; evidence tells me how well I know it. In real life, growth and margin could weaken together, which these individual tests do not measure.

## 6. End with interpretation — 1 minute

> My view started as watch and defer, and that remains the conclusion I can support. I now have a model showing why I am cautious: the base value is below the saved price, and even my higher-growth sensitivity does not reach it. But the valuation dates are not fully aligned, so I would not turn that comparison into a precise trading claim.
>
> My next research priority is the growth path: will customers keep earning enough from AI to support their purchases, and can NVIDIA keep winning those sales? I would also update the starting balance sheet and valuation date. Stronger evidence for durable growth and cash flow could change my conclusion. Weaker spending or lasting competitive pressure would make me more cautious.

The higher-growth Lab 11 case is **$174.85/share**. The reverse-DCF supplement is a stronger, separate case, not one of Lab 11's endpoints.

## Quick answers if asked

- **Why 12%?** “It is a judgment about the return equity investors require, not a measured CAPM estimate. I should test and defend it.”
- **Why 3% terminal growth?** “It assumes slower long-run growth with reinvestment. It is below my discount rate, but that alone does not prove it is right.”
- **Why not average the peer values?** “They use different economics and earnings bases. Averaging would hide the disagreement rather than explain it.”
- **Does the stock have to decline for the thesis to fail?** “No. My forecast can be too optimistic even if NVIDIA keeps growing—just more slowly than I assumed.”
- **Are these today's values and prices?** “No. They are saved classroom results with stated dates and a disclosed annual valuation convention.”
- **What if I cannot answer?** “That is a gap in my analysis. I will record the specific assumption or source I need to check.”

After presenting, complete [the actual review record](02-review-record.md). The guide prepares your explanation; it does not replace the live exchange.
