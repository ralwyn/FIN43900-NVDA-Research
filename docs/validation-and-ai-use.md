# Public validation summary
This public copy omits personal test records. It is not the complete course submission.

# Validation and AI use
Rohan Alwyn | FIN439 Project 1 | Prepared October 19, 2026

## Version and evidence boundary
Valuation: September 24 close, using information published by that date. Source pages rechecked October 19. Forecast years end January 31, 2027 through January 26, 2031 under the modeled fiscal-calendar convention. All model figures are USD millions, shares millions, and values/share USD. The first forecast period in DCF is a remaining stub; later periods are annual. Preserve the final repository commit and manifest separately when published.

## Source and convention ledger
| Input | Date / basis | Source and treatment |
|---|---|---|
| FY2026 history and H20 | January 25, 2026; filed February 25 | NVIDIA 10-K, income/BS/CF tables and gross-margin discussion; reported history retained, normalization separately shown. |
| Latest opening BS | July 26; released August 26 | NVIDIA Q2 FY27 release, condensed BS; assets 320,272, liabilities 91,288, equity 228,984. |
| H1 / Q3 / shares | H1 actual and Q3 outlook | Q2 release income/EPS/outlook; Q4 is independent forecast judgment; diluted and basic counts kept distinct. |
| NVIDIA quote | September 24 close, $224.58 | FinancialContent historical Close, not Adjusted Close; replaces saved $224.20 intraday reference. |
| Peer financials | AMD FY2025 / Broadcom FY2025 | SEC 10-Ks; annual GAAP EPS/revenue, carrying debt, cash and marketable short-term investments; dated basic share proxies. |
| Peer prices | September 24 close: AMD 629.26; AVGO 350.36 | Stock Analysis historical Close; same date and USD/share. |

Exact primary and price URLs are below. The company release is an authoritative issuer source; SEC filings are primary financial statements. Provider price labels are reconciled to Close rather than adjusted total-return prices. No paid API or runtime credential is needed.

## Base-year contamination and normalization
Reported FY2026 revenue 215,938, gross profit 153,463 and EBIT 130,387 are retained. Add the 4,500 H20 inventory/purchase-obligation charge only in an analytical normalization column: gross profit 157,963, EBIT 134,887, gross margin 73.15% versus 71.07% reported. This does not restate inventory, cash or equity, and the charge is not added again to forecast FCFF. Other inventory provisions are not all assumed nonrecurring; export-control risk remains in the downside.

Q2/H1 other income includes investment gains; the forecast excludes nonoperating gains and interest income, then values financial assets separately. SBC is treated as cash-equivalent compensation without an addback, which is a conservative economic convention rather than GAAP CFO. The diluted proxy is post-split; pre-split share/EPS fields are not mixed. July debt of 33,366 replaces the old January carrying debt of 8,468. Deferred taxes, leases and other noncurrent accounts are aggregated/fixed, a limitation rather than a solved reconciliation of every subaccount.

## Accounting, valuation and failure tests
| Claim / risk | Expected outcome | Actual and disposition |
|---|---|---|
| Published mini-case | FCFF 77.5m; equity/share 8.20 | Matches independent published fixture. |
| Opening BS | Assets 320,272; liabilities 91,288; equity 228,984 | Primary-source totals matched and balanced. |
| Pro-forma articulation | BS, CF cash, equity, assets, NI, debt and FCFF reconcile | All five future periods pass at 1e-6m tolerance; computed cash is not a balancing plug. |
| Timing | Elapsed cash flows excluded from DCF | July-to-September estimates appear only in the rolled opening balances, not as future PV cash flows. |
| Discount-rate / g boundaries | Higher WACC lowers value; higher g raises value on tested domain | Passed; invalid terminal input rejected. No claim of global monotonicity for every exotic input. |
| Operating changed input | More inventory investment lowers first-period FCFF | +20 inventory days test passes; this automated result is not the student locked record. |
| Share bridge | Doubling diluted denominator halves value/share | Passed while basic market-cap weighting held fixed. |
| Highest-risk missing-flow test | Injecting $1m extra cash must block valuation | Red failure: first forecast BS gap 1.000000m; recovery restores base. |
| Funding | Unfunded distributions must not create an invented credit line | $1,000 annual dividend stress refused at the cash floor. |
| Peer definitions | EV = basic market-cap proxy + carrying debt - cash/investments | Both identities pass; annual positive denominators checked; comparability remains qualified. |
| Restored base | All fields unchanged after automated tests | Exact in the same runtime. |
| Clean environment | Run from README in fresh venv without network/packages | Passed. First exact-JSON comparison differed across runtimes; maximum numeric difference 4.66e-10, below 1e-6m tolerance. Structural/text comparison matches. |

The directional expectations above were encoded before the automated checks in this build. They are AI-authored test specifications, not a student AI-off prediction. Full actual logs: validation-log.txt and cold-run-log.txt. Python standard library only; a fresh bundled-Python venv reproduced the output. The clean run was agent-operated, not falsely attributed to the student.

## Assumption challenge register
| Driver | Value | Basis | Challenge / evidence that changes it |
|---|---|---|---|
| Q3 / Q4 revenue | 108,000 / 118,800m | Q3 guidance; Q4 +10% sequential judgment | Customer spending may slow; update with orders and next results. |
| Revenue growth FY28-31 | 35%,25%,15%,8% | Judgment fade as installed base expands | Custom ASICs, export limits, and customer returns may weaken demand; revise with segment results. |
| Gross margin FY27-31 | 74%,73%,72%,71%,70% | Near guidance initially; competition/mix fade | Persistent pricing power or cost pressure changes this; verify reported margins and inventory charges. |
| SG&A / gross profit | 2.5%,2.7%,2.9%,3%,3% | Lab operating leverage convention | Costs may track revenue differently; revise on expense mix. |
| R&D / revenue | 8%,9%,10%,11%,12% | Judgment for product and software competition | Compute/cloud and payroll growth may outrun revenue; update on disclosed spending. |
| Tax rate | 17% | Midpoint of 16-18% company FY27 outlook; extended by judgment | Discrete items and geography can change cash tax; separate them from operating tax. |
| AR / inventory / AP days | 64.7 / 129.4 / 61.7 | July balances / annualized H1 flow | Not average-balance turnover; seasonality/customer concentration may distort; revise on next filing. |
| Prepaid / accrued intensity | 0.96% / 7.58% | July balance / annualized H1 revenue | All current accruals treated as operating; acquisition/nonrecurring components may require separation. |
| Depreciation / amortization | 23% / 28% of opening assets, time scaled | Simplified asset run-off judgments, informed by prior lab history | Lives/acquisitions can change rates; compare with asset notes and subsequent D&A. |
| Capex / revenue; split | 3%; 97% tangible / 3% intangible | Judgment above prior annual intensity; allocation simplification | Infrastructure expansion may increase investment; revise with cash-flow statements. |
| Required equity return / debt cost | 12% / 4.5% | Judgment ranges; no fitted beta or measured current yield claimed | Equity duration/cyclicality and borrowing yields may change; test 10-14% equity return and recalibrate. |
| Capital structure weights | Debt 0.61%; remainder equity | Quote x 24.1bn basic shares; reported debt proxy | Debt market value and basic shares can move; recheck outstanding securities. |
| Terminal growth / reinvestment | 3%; stable productive-asset and WC intensity | Nominal steady-state judgment; capital investment funds growth | Margin/duration and capital needs may not converge; use 2-4% grid and compare terminal EV share. |
| Shares | 24,285m diluted; 24,100m basic market-cap proxy | Q2 diluted EPS denominator; prior 10-Q basic cover count | Neither is a forward dilution forecast; revise on awards, issuance and buybacks. |
| Private investments / haircut | 51,157m / 25% | Reported carrying value; liquidity/uncertainty judgment | Impairment, realization tax, concentration and commitments may lower proceeds; independently value portfolio. |
| Cash floor / dividends | 5,000m / $1 annual per basic share | Liquidity judgment; annualized declared quarterly dividend | Liquidity needs and capital returns can change; do not treat policy as guaranteed. |
| Other balances / acquisitions | Fixed nonoperating balances; no future acquisitions/investments/buybacks | Explicit simplifying exclusions; leases stay in operating expense | Material investments/commitments or capital allocation changes require model revision. |
| Interim operating roll | Linear July 26 to September 24; first stub prorated | Estimated calendar allocation, not reported interim accounts | Seasonality and capital flows can invalidate the bridge; replace with actuals or a quarterly model. |


Partner challenges are not fabricated. The recovered Edition A artifact contains a partner-question label, but this session does not establish a new Weeks 5-6 exchange. Confirm actual attribution if supplying one.

## Method disagreement and range dependence
AMD/Broadcom are qualified because of AI compute/networking exposure, not just an industry label. CPUs/client/gaming, software mix, tax items, acquisition amortization, stale basic-share dates and differing fiscal years limit comparisons. Current price times dated shares gives a market-cap proxy; do not call it verified current diluted EV. EV/sales retains operating leases in expenses and excludes preferred/NCI by assumption; it is not EV/EBITDA. P/E uses GAAP annual diluted EPS, not adjusted or forward earnings. Applying peer multiples to NVIDIA's annual historical definitions is mechanical and is not averaged into the DCF.

At +/-5pp revenue growth versus +/-2pp margin, growth produces the larger value span. With growth narrowed to +/-1pp, its span is $10.55 versus $11.45 for margin, reversing the ranking. Sensitivity assigns no probabilities. A growth-only reverse DCF cannot reach the market inside the admitted +/-10pp domain; fixed base cash flows imply 9.32% WACC to match the $224.58 quote. Do not expand bounds solely to force a convenient answer.

## Locked Changed-Input Record
Student reports a TA-approved exception. Personal prediction and execution records are withheld from this public copy. The detailed validation record is reserved for the course submission. This public summary does not certify independent AI-off completion or constitute the complete grading package.

## Named AI-use register
| Tool / date | Material contribution | Independent check / disposition |
|---|---|---|
| OpenAI Codex, September lab records | Company/peer research, lab code, explanations and sensitivity drafts | Preserved earlier disclosures; personal activities and original checkpoint receipt not inferred. |
| OpenAI Codex, October 19 | Recovered files, read assignment/professor clarification, organized package | Cross-checked Brightspace records and preserved local artifact hash; qualified baseline status. |
| OpenAI Codex, October 19 | Built revised FCFF/stub/WACC/bridge and workbench | Source BS totals, hand-checkable FCFF identity, published fixture and deliberate errors support the correction. Old annual timing and basic-as-diluted interpretation corrected. |
| OpenAI Codex, October 19 | Generated scenario/range/peer analyses, documents and recording preparation | Recomputed from exposed inputs; forecasts and judgment ranges require student review; comparison limitations retained. |
| OpenAI Codex, October 19 | Prepared two-stage locked-test utility | Utility preparation was AI-assisted. Detailed personal evidence and its provenance are reserved for the course-only validation record. |

The exposed tool identifies a GPT-6-based Codex agent; an exact backend model version is not independently exposed. Material AI assistance is disclosed here rather than repeated as labels throughout the memo. No source or output is accepted merely because a model agrees. The student remains responsible for understanding, reviewing, recording and defending the recommendation. No attendance, partner dialogue, AI-off authorship, on-time checkpoint, video, upload or receipt is invented.

## Limits and monitoring
The estimated interim roll, historical balance and share proxies, private-asset values, simplified taxes and constant other balances can materially affect value despite accounting consistency. Three causal cases are not a statistical interval. Rebuild on new guidance, a material customer/export event, capital allocation change, or new filing. The proposed committee action is watch/defer; do not initiate on model arithmetic alone. Compare new price/value to the disclosed 20% margin-of-safety gate and reconsider risk at each review.

## Source URLs
- NVIDIA 10-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- NVIDIA Q2 release: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/
- NVIDIA historical price: https://www.financialcontent.com/quote/NQ:NVDA/historical
- AMD 10-K: https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm
- Broadcom 10-K: https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm
- Peer prices: https://stockanalysis.com/stocks/amd/history/ and https://stockanalysis.com/stocks/avgo/history/
- Project: https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-1-corporate-finance-application.md
