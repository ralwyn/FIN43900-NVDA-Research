# Lab 10 — NVIDIA (NVDA): Pro-Forma Valuation

Prepared September 24, 2026 · USD millions unless stated otherwise · AI partner: OpenAI Codex

## Check block — look here first

| Year | Assets − liabilities − equity | BS cash − cash-flow cash | Minimum cash | Revolver |
|---|---:|---:|---|---:|
| FY2027E | 0.000000 | 0.000000 | PASS | 0.0 |
| FY2028E | 0.000000 | 0.000000 | PASS | 0.0 |
| FY2029E | 0.000000 | 0.000000 | PASS | 0.0 |
| FY2030E | 0.000000 | 0.000000 | PASS | 0.0 |
| FY2031E | 0.000000 | 0.000000 | PASS | 0.0 |

**Base-case value: $148.73 per share**, using 24,100 million shares. Equity value: $3.584 trillion. Terminal value supplies 70.13% of total value. The checks use unrounded amounts and a tolerance of $0.000001 million ($1).

The executable refuses valuation when a balance, cash-flow, equity, productive-asset, earnings or debt check fails, or when cash falls below its floor. Deliberately freezing FY2027 cash at its opening amount produces a **−149,306.591691 million** balance gap and blocks valuation.

**Status:** independent work with AI assistance, following the student's report of the instructor's direction. An AI challenge and response are provided below; no human partner exchange or student-performed filing check is claimed. Judgment explanations are AI-assisted proposed rationales for the student to review and adopt or revise.

**Date convention:** the five annual statements start from the January 25, 2026 audited balance sheet. The lab-style DCF discounts FY2027–FY2031 cash flows one through five years to that opening date, using information gathered September 24. It is an updated annual teaching case, **not a contemporaneous January backtest or an exact September 24 valuation**. The current quote comparison below discloses this timing limitation rather than implying a fully current balance-sheet/stub-period model.

## D — Define

What are five years of NVIDIA's statements worth, built from assumptions we can defend?

**What makes NVIDIA different:** NVIDIA's fabless business requires R&D and supplier-related working capital, not ABG's vehicle floor-plan loans. The model therefore carries R&D separately, forecasts receivables, inventory, prepaid/current-other assets and trade payables, and sets floor-plan debt to **none**. Supplier commitments are a risk to these assumptions; they are not booked a second time as an immediate liability or cash expense. See the Manufacturing section and Note 12 of the [2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm).

## R — Represent: the three-year history

Each amount below is traced to the linked filing for its fiscal year. IS = consolidated income statement, BS = consolidated balance sheet, CF = consolidated cash-flow statement. Page numbers are printed filing pages, not browser or PDF page indices. Fiscal year labels are NVIDIA's labels.

| Metric | FY2024 — Jan 28, 2024 | FY2025 — Jan 26, 2025 | FY2026 — Jan 25, 2026 | Filing location |
|---|---:|---:|---:|---|
| Revenue | 60,922 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 130,497 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 215,938 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |
| Gross profit | 44,301 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 97,858 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 153,463 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |
| SG&A | 2,654 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 3,491 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 4,579 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |
| R&D | 8,675 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 12,914 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 18,497 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |
| Net income | 29,760 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 72,880 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 120,067 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |
| Inventory | 5,282 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 10,080 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 21,403 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | BS: pp. 52 / 54 / 53 |
| PP&E, net | 3,914 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 6,283 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 10,383 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | BS: pp. 52 / 54 / 53 |
| Shareholders’ equity | 42,978 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 79,327 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 157,293 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | BS: pp. 52 / 54 / 53 |
| Accounts receivable | 9,999 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 23,065 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 38,466 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | BS: pp. 52 / 54 / 53 |
| Accounts payable | 2,699 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 6,310 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 9,812 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | BS: pp. 52 / 54 / 53 |
| Depreciation only (2025/26 approx.) | 894 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 1,300 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 2,400 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | Balance-sheet components note |
| Depreciation and amortization | 1,508 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 1,864 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 2,843 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | CF: pp. 54 / 56 / 55 |
| Cash capex: PP&E and intangibles | 1,069 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 3,236 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 6,042 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | CF: pp. 54 / 56 / 55 |
| Operating cash flow | 28,090 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 64,089 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 102,718 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | CF: pp. 54 / 56 / 55 |
| Stock-based compensation, CF adjustment | 3,549 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 4,737 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 6,386 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | CF: pp. 54 / 56 / 55 |
| Income tax expense | 4,058 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 11,146 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 21,383 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |
| Pretax income | 33,818 ([2024 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm)) | 84,026 ([2025 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm)) | 141,450 ([2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)) | IS: pp. 50 / 52 / 51 |

The 2024 filing's per-share numbers precede the 2024 stock split; no pre-split EPS or share count is used in this model. Dollar-denominated financial statement totals do not need split adjustment. FY2025 and FY2026 depreciation-only disclosures are rounded to $1.3bn and $2.4bn, so the resulting ratios are approximate. Total D&A is separately reported and is not substituted for depreciation-only history.

### Two filing checks

| Item | Verified value | Evidence | Who checked |
|---|---:|---|---|
| FY2026 revenue | 215,938 | [2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), printed p. 51; also agrees with [NVIDIA FY2026 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/) | AI checked; student manual check not yet recorded |
| FY2026 inventory | 21,403 | [2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), printed p. 53; also agrees with [NVIDIA FY2026 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/) | AI checked; student manual check not yet recorded |

Historical reported growth uses FY2023 revenue of 26,974 for the FY2024 calculation, from the FY2024 income statement. The primary 10-K amounts required by the lab are verified; the outstanding verification step is the lab's request for the student to check two entries personally.

### Historical ratios

Ratios are computed from the figures above. Inventory days use **ending** inventory / annual cost of revenue × 365 to match the lab convention, not average inventory. Depreciation / PP&E uses ending net PP&E in this diagnostic table.

| Ratio | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Gross margin | 72.72% | 74.99% | 71.07% |
| SG&A / gross profit | 5.99% | 3.57% | 2.98% |
| R&D / revenue | 14.24% | 9.90% | 8.57% |
| Inventory days | 115.99 | 112.72 | 125.04 |
| Depreciation / net PP&E (2025/26 approx.) | 22.84% | 20.69% | 23.11% |
| Cash capex / revenue | 1.75% | 2.48% | 2.80% |
| Effective tax rate | 12.00% | 13.26% | 15.12% |
| Reported revenue growth | 125.85% | 114.20% | 65.47% |
| Organic / same-store growth | Not separately disclosed in reviewed 10-K | Not separately disclosed in reviewed 10-K | Not separately disclosed in reviewed 10-K |

**Organic growth:** growth from existing operations, excluding acquired revenue, with the precise definition depending on the issuer. NVIDIA does not provide a comparable same-store metric in the reviewed annual filings; the model does not relabel reported growth as organic. The no-new-acquisitions forecast is a judgment, not a company-disclosed organic-growth series. ABG's 1.8% existing-store assumption avoids carrying acquisition-driven reported growth of 4.7% into perpetuity.

### Capex: filing versus provider field

| Fiscal year | Filing: cash purchases of PP&E and intangibles | Provider “Capital Expenditures” | Reconciliation |
|---|---:|---:|---|
| 2024 | 1,069 | −1,069 | Same cash outflow; sign convention differs |
| 2025 | 3,236 | −3,236 | Same cash outflow; sign convention differs |
| 2026 | 6,042 | −6,042 | Same cash outflow; sign convention differs |

Filings: CF statements linked above. Provider: [StockAnalysis / S&P Global cash-flow table](https://stockanalysis.com/stocks/nvda/financials/cash-flow-statement/), accessed September 24, 2026. The field covers intangibles as well as PP&E. It excludes the separately presented Groq payment and acquisitions and excludes asset purchases not yet paid for. Provider free-cash-flow fields are not substituted for the model's FCFE.

### Recent facts and guidance used to inform judgments

- [Q2 FY2027 10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf), printed p. 3: first-half revenue **177,837**. Cover: **24.1bn shares** outstanding August 21, 2026. These are historical facts, not forecast guidance.
- [August 26 results release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/), Outlook: Q3 revenue **108,000 ±2%**, GAAP gross margin **74% ±0.5 percentage points**, and full-year tax rate **16–18%**, excluding discrete changes. These are guidance.
- Q4 revenue **118,800** is a judgment: 10% above Q3's midpoint. FY2027 revenue therefore equals **404,637**, or **87.39%** above FY2026. The full-year projection is not represented as management guidance.

### Labelled assumptions and reasons

Forecast values below apply in FY2027 → FY2031 order. “History” labels identify the source of a ratio; holding a historical ratio constant is itself a forecasting choice. Reasons are proposed economic explanations, not statements that management has promised these outcomes.

| Assumption and value | Label | Reason |
|---|---|---|
| growth: **87.39%, 35.00%, 25.00%, 15.00%, 8.00%** | judgment | FY27 = H1 actual 177837 + Q3 guidance midpoint 108000 + Q4 judgment 118800; later growth fades as the revenue base expands. |
| gross margin: **74%, 73%, 72%, 71%, 70%** | judgment | Start near Q3 guidance of 74%; fade to 70% as competition and product mix limit pricing. |
| sga gp: **2.5%, 2.7%, 2.9%, 3.0%, 3.0%** | judgment | Allow operating leverage initially, then moderately higher selling costs relative to gross profit. |
| rd revenue: **8%, 9%, 10%, 11%, 12%** | judgment | Keep R&D material and increase its revenue share as product competition intensifies. |
| tax rate: **17.0000%** | judgment | 17% is the midpoint of FY27 guidance of 16%-18%; holding it through FY31 is a judgment. |
| inventory days: **125.04 days** | history | FY26 ending inventory / cost of revenue x 365; carrying it forward assumes the same inventory intensity. |
| receivable days: **65.02 days** | history | FY26 ending receivables / revenue x 365; forecast holds collection intensity. |
| payable days: **57.33 days** | history | FY26 ending accounts payable / cost of revenue x 365; no floor-plan borrowing. |
| prepaid revenue: **1.4726%** | history | FY26 prepaid/current-other assets / revenue; scales supplier prepayments and other current assets together. |
| accrued revenue: **8.0722%** | history | FY26 accrued current liabilities less 3921 purchase consideration, divided by revenue; exclude one-off acquisition financing. |
| purchase consideration payment: **3,921.00** | judgment | Settle the FY26 accrued purchase consideration in FY27, consistent with the within-one-year disclosure; cash estimate uses carrying value. |
| depreciation opening ppe: **23.1147%** | history | Rounded FY26 depreciation 2400 / ending PP&E 10383, applied to opening forecast PP&E. |
| amortization opening intangibles: **27.9189%** | judgment | FY27 disclosed amortization 923 / opening intangibles 3306; reuse as a simplifying declining-balance rate. |
| capex revenue: **3.0000%** | judgment | 3% exceeds FY26 cash capex/revenue of about 2.8%, allowing investment as the platform grows. |
| tangible capex share: **97.0000%** | judgment | Allocate 97% of combined cash capex to PP&E and 3% to intangibles; filing does not supply this forecast split. |
| interest rate: **3.0586%** | history | FY26 interest expense / ending carrying debt; holding the rate is a refinancing simplification. |
| debt repayment: **0.00** | judgment | Refinance maturities at equal principal; debt balance held flat, no perpetual debt-paydown addback. |
| minimum cash: **5,000.00** | judgment | Keep $5bn operating liquidity; this is a model floor, not company guidance. |
| revolver limit: **0.00** | judgment | No unverified credit line assumed; fail when cash cannot meet its floor. |
| revolver rate: **6.0000%** | judgment | 6% stress-test placeholder; base-case credit limit is zero. |
| annual dividend per share: **1.00** | judgment | Annualize Q2 FY27 dividend of $0.25 to $1; freeze solely for the cash/equity bridge. |
| buyback: **0.00** | judgment | No future buyback assumed; keep the ownership denominator fixed. |
| shares: **24,100 million** | history | Latest 10-Q cover: 24.1bn actual shares at Aug 21 2026, rounded by the issuer; use post-split shares, not FY24 pre-split shares. |
| cost of equity: **12.0000%** | judgment | 12% required return for a concentrated, cyclical growth business; not a measured beta or CAPM estimate. |
| terminal growth: **3.0000%** | judgment | 3% long-run nominal growth, below 12%; normalize reinvestment to stable asset intensity. |
| private investment haircut: **25.0000%** | judgment | 25% haircut to FY26 private investment carrying value for uncertainty and liquidity; marketable securities use carrying value. |
| market price: **$224.20 on September 24, 2026 at 2:05 PM EDT** | history | FinancialContent quote: $224.20, Sep 24 2026, 2:05 PM EDT; intraday reference, not closing price. |
| Stock compensation: cash-equivalent recurring expense; no addback or dilution | judgment | Keep the cost embedded in expense ratios rather than treating employee equity as free cash while freezing shares. This is an economic model, not a forecast of reported SBC accounting. |
| Interest income and investment gains: zero | judgment | Exclude financial-asset earnings from operating cash flows and add opening financial-asset value only once. |
| New acquisitions, impairment, equity issuance and other comprehensive income: zero | judgment | No defensible schedule for these items; model organic operations and disclose exclusions. Existing purchase consideration is still paid. |
| Other noncurrent assets and liabilities: flat | judgment | Simplify deferred taxes, goodwill and lease balances; recurring lease costs remain in forecast expense ratios. |
| Terminal net capex and working capital: 3% of ending productive assets and operating NWC | judgment | Fund long-run growth rather than assuming perpetual growth with no reinvestment. |
| Floor-plan loans: none | history / structure | No ABG inventory-financing line is imported; ordinary accounts payable follows NVIDIA's cost of revenue. |

### Fresh-eyes challenge — AI review for independent work

**AI challenge:** Why assume 74% gross margin initially and still 70% by FY2031 when customers can build custom chips and supplier constraints can raise costs? What would make you lower those numbers?

**Proposed two-sentence answer:** The 74% starting margin is anchored to current Q3 guidance, while the fade to 70% explicitly allows competition and mix to reduce profitability. I would lower the forecast if successive reported margins fall below that path or if pricing, product-transition costs or customer substitution explain a lasting decline; the two-percentage-point downside test below shows the valuation effect.

**Reciprocal challenge prepared for discussion:** Your model holds inventory days flat while revenue slows; what evidence supports that assumption if capacity orders cannot be cancelled, and how does an extra 20 days change FCFE?

This is an AI challenge and a prepared question, not a fabricated classmate exchange. The student reports independent work time; whether this substitutes for the written partner-review criterion remains an instructor decision.

## I — Implement

`nvda_proforma.py` is a standalone standard-library Python file. It preserves Lab 09 separately and prints five years of income statements, balance sheets and cash flows. All dollar calculations retain full precision.

```sh
python3 nvda_proforma.py
python3 nvda_proforma.py --self-test
python3 nvda_proforma.py --break-cash
python3 nvda_proforma.py --sensitivity
```

The deliberate-break command should exit with an error. A normal run restores the base case because the flag does not edit the source.

**Order:** forecast sales and costs → net income → operating assets/liabilities and productive assets → operating/investing/financing cash flows → cash → balance and rollforward checks → valuation.

**Important accounting choices:**

- Gross margin, R&D and SG&A ratios already include D&A and employee compensation. D&A is added back once in CFO and reduces PP&E/intangibles; it is not subtracted a second time in the income statement.
- Ordinary payables finance some supplier purchases, but there is no floor-plan loan. More inventory or prepayments consumes cash; more trade payables releases cash.
- The 3,921 accrued acquisition consideration is removed from operating accruals and paid in investing cash flow in FY2027. It is not accidentally treated as recurring supplier financing or deducted twice.
- Cash stock-compensation equivalents remain an expense. No SBC addback, share issuance or buyback is forecast, so the share denominator stays constant.
- Net debt is flat under an explicit refinancing assumption. This is a simplified capital policy, not NVIDIA's actual 2026 financing activity.

### Opening FY2026 balance sheet

Source: FY2026 10-K, printed p. 53. Asset and liability groupings reconcile exactly to the filed totals.

| Assets | Amount | Liabilities and equity | Amount |
|---|---:|---|---:|
| Cash | 10,605 | Accounts payable | 9,812 |
| Marketable securities | 51,951 | Accrued/current other liabilities | 21,352 |
| Receivables | 38,466 | Short- and long-term debt | 8,468 |
| Inventory | 21,403 | Other noncurrent liabilities | 9,878 |
| Prepaid/current other assets | 3,180 | Total liabilities | 49,510 |
| PP&E | 10,383 | Equity | 157,293 |
| Intangibles | 3,306 | | |
| Non-marketable equity investments | 22,251 | | |
| Other noncurrent assets | 45,258 | | |
| **Total assets** | **206,803** | **Total liabilities + equity** | **206,803** |

Other noncurrent assets = operating lease assets 2,867 + goodwill 20,832 + deferred tax assets 13,258 + other assets 8,301. Other noncurrent liabilities = lease liabilities 2,572 + other long-term liabilities 7,306.

## V — Validate and compare

| Metric | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E |
|---|---:|---:|---:|---:|---:|
| Revenue | 404,637.0 | 546,260.0 | 682,824.9 | 785,248.7 | 848,068.6 |
| Operating income | 259,574.6 | 338,839.6 | 409,094.1 | 454,423.4 | 474,070.3 |
| Net income | 215,232.0 | 281,021.9 | 339,333.1 | 376,956.5 | 393,263.4 |
| FCFE | 173,406.6 | 246,241.6 | 303,302.1 | 345,922.4 | 369,563.9 |
| Cash | 159,911.6 | 382,053.2 | 661,255.3 | 983,077.7 | 1,328,541.6 |
| Equity | 348,425.0 | 605,346.9 | 920,580.0 | 1,273,436.4 | 1,642,599.8 |

No projected year has negative FCFE, and no revolver draw is needed. All five ending cash balances exceed the $5,000 million floor.

### Valuation bridge

| Component | USD millions |
|---|---:|
| PV of FY2027–FY2031 FCFE | 996,554.47 |
| PV of terminal equity cash flows | 2,513,571.28 |
| Opening excess cash and financial investments | 74,244.25 |
| **Equity value** | **3,584,369.99** |
| Shares, millions | 24,100.00 |
| **Value per share, USD** | **148.73** |

Terminal FCFE is **398,679.43**, computed from FY2032 earnings at 3% revenue growth, less **2,119.21** of net productive-asset investment and **4,269.12** of working-capital investment. The model divides that cash flow by 12% − 3% and discounts five years. It does not simply grow a high-growth year's FCFE or perpetually add back a scheduled debt repayment.

The nonoperating bridge equals 5,605 excess opening cash + 51,951 marketable securities + 75% × 22,251 private investments. These assets' interest and gains are excluded from forecast earnings. Do not subtract debt again from an FCFE equity valuation, and do not add accumulated future cash again: the cash flows creating it have already been valued.

**Market question:** The annual-base model says **$148.73**, while the market reference is **$224.20 on September 24, 2026 at 2:05 PM EDT**, using the same **24.1bn post-split shares** (implied market equity value $5.403tn); what stronger cash flows, lower required return, or valuation-date updates would explain the difference? [Quote source](https://www.financialcontent.com/quote/NQ:NVDA/historical). This is a question, not a buy/sell recommendation, and the annual discounting anchor differs from the quote date.

### Sensitivity — same statements, changed required return and terminal growth

| Cost of equity | Terminal growth 2% | 3% | 4% |
|---|---:|---:|---:|
| 10% | $174.66 | $193.59 | $218.82 |
| 12% | $137.87 | $148.73 | $162.30 |
| 14% | $113.49 | $120.32 | $128.52 |

Reducing every projected gross margin by two percentage points lowers value to **$143.41**. This is a scenario, not a probability-weighted forecast. The 2031 growth assumption still steps down from 8% to 3% in the terminal year; terminal uncertainty remains material.

## E / R — Evolve and reflect

**Proposed reflection to review:** The growth fade is the judgment requiring the strongest defense: initial demand is strong, but a much larger revenue base cannot keep doubling indefinitely. One striking filing figure is the increase in inventory from $10.080bn to $21.403bn while reported revenue grew about 65%, which makes supplier commitments and inventory intensity worth questioning.

**Why cash is last:** earnings, investment, working capital, debt and distributions determine cash. A separate balance check can then expose a missing or incorrectly signed flow; forcing cash to balance would conceal the error.

### Validation assessment: share with noted caveats

- All source-history arithmetic, five annual balance checks, cash and equity rollforwards, and deliberate-error tests pass. The tests also reject non-finite amounts and an invalid perpetuity denominator.
- The first-year forecast is independently recomputed from the revenue components and profit assumptions. An inventory-days stress test confirms higher inventory reduces FCFE while keeping the statements balanced.
- Annual opening balances are January 2026, while guidance, share count and the quote are later. A current investment-grade valuation would rebuild from July actual balances and model the September stub period, updated borrowing, investment portfolio, buybacks and distributions. The disclosed annual teaching result must not be mistaken for that analysis.
- Other noncurrent balances and net debt are simplified, new acquisitions are excluded, private investment values are uncertain, and taxes on realizing financial investments are not separately estimated. These affect valuation confidence even when the arithmetic balances.
- Student manual source checks and a human partner review are not recorded. AI verification does not establish those personal participation requirements. The independent-work direction is based on the student's report.

## Checkout files

- [Python engine](nvda_proforma.py)
- [Complete statements and check block](lab10-nvda-output.txt)
- [Automated validation evidence](lab10-nvda-validation.txt)
- [Sensitivity output](lab10-nvda-sensitivity.txt)
- This report: `lab10-nvda-report.md`

No Brightspace submission is made by these files. Do not reuse Lab 09's session token without confirmation that it also applies to Lab 10.
