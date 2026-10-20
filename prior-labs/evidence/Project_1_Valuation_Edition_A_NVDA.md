# Project 1 Valuation — Edition A

## Decision and intended user

The intended user is an equity-research analyst deciding whether NVIDIA Corporation should advance to deeper valuation research and potential coverage initiation. The decision is whether to initiate detailed valuation work now, watch and defer pending additional evidence, or decline to initiate.

## Company and valuation date

- Company: NVIDIA Corporation
- Ticker: NVDA
- Valuation date: September 3, 2026
- Initial thesis: **Watch and defer pending valuation work.** NVIDIA's growth, cash generation, and net-cash position justify deeper research, but this evidence alone does not establish that the shares are attractively valued.

## Primary filing locator

- Filing: NVIDIA Corporation Form 10-K
- SEC accession: 0001045810-26-000021
- Reporting period: Fiscal year ended January 25, 2026
- Filing date: February 25, 2026
- SEC filing: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- SEC filing-detail page: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/0001045810-26-000021-index.htm
- Currency: U.S. dollars
- Units: Millions, except per-share data where indicated

## Known evidence

1. Fiscal 2026 revenue was $215.938 billion, up 65% from fiscal 2025. Data Center revenue increased 68%, making demand for accelerated computing and AI a central operating-value driver. Source: NVIDIA FY2026 Form 10-K, fiscal-year summary.
2. Net cash provided by operating activities was $102.718 billion in fiscal 2026. Capital expenditures were $6.1 billion. Source: NVIDIA FY2026 Form 10-K, Liquidity and Capital Resources.
3. Cash and cash equivalents were $10.605 billion, while cash, cash equivalents, and marketable securities totaled $62.556 billion as of January 25, 2026. Source: NVIDIA FY2026 Form 10-K, Liquidity and Capital Resources.
4. Debt had a net carrying amount of $8.468 billion, comprising $999 million short-term and $7.469 billion long-term. No commercial paper was outstanding as of January 25, 2026. Source: NVIDIA FY2026 Form 10-K, Outstanding Indebtedness and Commercial Paper Program.
5. Fiscal 2026 diluted weighted-average shares were 24.514 billion. This is an income-statement denominator incorporating the dilutive effect of equity awards under the treasury-stock method; it is not the period-end basic share count. Source: NVIDIA FY2026 Form 10-K, Note 4 — Net Income Per Share.
6. The Week 1 screen calculated a three-year revenue CAGR of 100.05% and a latest-year free-cash-flow margin of 44.77%. NVIDIA ranked first among the original qualifiers. Raising the revenue-CAGR threshold from 5% to 15% removed JNJ and GOOGL, but NVIDIA remained first ahead of META and MSFT. Source: Week 1 yfinance-based screening workbook, accessed September 3, 2026. These values require reconciliation to the primary filing before use in valuation.
7. Management concluded that disclosure controls and internal control over financial reporting were effective as of January 25, 2026. PricewaterhouseCoopers also gave an unqualified opinion on the financial statements and internal control. Source: NVIDIA FY2026 Form 10-K, Item 9A and auditor's report.

## Consequential assumptions

- Recent AI-infrastructure demand will normalize from its exceptional growth rate but remain structurally positive.
- Revenue growth will slow materially from fiscal 2026 rather than continue at the historical screen's three-year CAGR.
- Gross margin will remain strong despite product transitions, export restrictions, inventory charges, and increasing competition.
- Capital expenditures and ecosystem investments will rise, so historical free-cash-flow conversion should not be carried forward unchanged.
- Cash and marketable securities are treated as non-operating assets in the enterprise-to-equity bridge, subject to confirming which securities are required for operations.
- Debt is measured using the filing's carrying amount initially; a later valuation should test whether market value differs materially.
- Diluted shares must reflect equity awards and future stock-based compensation rather than relying only on the basic period-end count.

## Important unknowns

- The sustainable long-run growth rate for Data Center revenue after the current AI investment cycle.
- The effect of export controls, customer concentration, competition, and supply constraints on revenue and margins.
- A normalized operating margin and reinvestment rate across a full industry cycle.
- The appropriate weighted-average cost of capital and terminal-growth assumptions.
- The amount of stock-based compensation and future dilution that should be incorporated into valuation.
- Whether current market expectations already price in more growth than a defensible cash-flow forecast supports.

## Research plan

1. Reconcile revenue, operating cash flow, capital expenditures, cash, debt, and diluted shares to the latest 10-K and subsequent 10-Q.
2. Build historical income-statement, balance-sheet, and cash-flow series using consistent fiscal periods and units.
3. Separate operating from non-operating assets and complete the enterprise-to-equity bridge.
4. Model revenue by major platform, with particular attention to Data Center demand, customer concentration, export restrictions, and supply.
5. Forecast operating margins, taxes, reinvestment, and FCFF under base, upside, and downside cases.
6. Estimate WACC and terminal value, then test sensitivity to growth, margins, reinvestment, and discount rate.
7. Compare implied value with the market price as of the valuation date before making any coverage-initiation conclusion.

## Synthetic enterprise-to-equity bridge

The supplied mini-case uses USD millions except for the per-share result:

- NOPAT = $150 × (1 − 0.25) = **$112.50 million**
- FCFF = $112.50 + $40 − $60 − $15 = **$77.50 million**
- Common equity value = $1,000 + $100 − $250 − $20 − $10 = **$820.00 million**
- Value per diluted share = $820 ÷ 100 = **$8.20 per share**

This is a synthetic known-answer check and is not an NVIDIA valuation.

## Falsification question

**Partner-generated question:** Can hyperscalers establish a profitable, cash-generative ROI on their AI infrastructure investments before custom ASICs and merchant alternatives permanently compress NVIDIA’s Data Center gross margins?

**Why it matters:** The thesis depends on customers earning enough from AI infrastructure to sustain their capital spending while NVIDIA preserves pricing power. If hyperscalers cannot generate adequate returns, their demand may slow; if custom ASICs or merchant alternatives become economically superior first, NVIDIA could lose share or face lasting margin compression. Either outcome would undermine the growth and cash-flow assumptions supporting deeper valuation research.
