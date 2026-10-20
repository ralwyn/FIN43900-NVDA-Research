# Lab 08 — NVIDIA peer P/E research and reflection draft

**Scope and attribution.** This analysis was prepared with AI assistance after the request in this chat. The student confirmed NVIDIA as the target and said they worked alone. The materials supplied were the Lab 08 instructions and Session 08 slides, not a record of completed class work. A prior NVIDIA note dated September 3, 2026 supplies the comparison date used here; the actual Week 3 DCF value was not supplied. This is a research draft, not a verified account of actions taken during class.

## Research question and peer policy

What NVIDIA share price is implied by comparable listed operating companies' annual reported diluted P/E multiples at the September 3, 2026 close? The boundary is a **historical reported earnings** cross-check, not a forecast or an intrinsic-value estimate. Candidates need exposure to data-center AI compute or networking; material differences in CPU, software, customer mix, margins, or accounting must be qualified. Both candidates have positive reported annual diluted EPS. Success means a source-traceable comparison that helps assess the earlier DCF, if that DCF is available.

## Sources and candidate decisions

All prices below are U.S.-listed common-share **closing prices in USD on September 3, 2026**, from [Stock Analysis historical prices for NVDA](https://stockanalysis.com/stocks/nvda/history/), [AMD](https://stockanalysis.com/stocks/amd/history/), and [AVGO](https://stockanalysis.com/stocks/avgo/history/). That service attributes its historical prices to S&P Global Market Intelligence. EPS figures are **reported annual diluted USD per share**, not adjusted EPS or a quarter's EPS.

| Company | September 3 close | Annual diluted EPS; fiscal year-end; filing date | Decision and business reason |
|---|---:|---|---|
| NVIDIA (target) | $228.45 | $4.90; Jan. 25, 2026; Feb. 25, 2026. [FY2026 10-K, Note 4](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) | Its Data Center platform combines GPUs, networking, systems, and software; see 10-K Item 1 Business. |
| AMD | $456.16 | $2.65; Dec. 27, 2025; Feb. 4, 2026. [FY2025 10-K, statements and EPS note](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm) | **Qualify.** Its Data Center segment sells AI accelerators and server CPUs and competes with NVIDIA, but it also has substantial client, gaming, and embedded businesses. See 10-K Item 1 Business and segment results. |
| Broadcom | $357.16 | $4.77; Nov. 2, 2025; Dec. 18, 2025. [FY2025 10-K, EPS note](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm) | **Qualify.** Its custom AI accelerators and networking overlap with NVIDIA, but 42% of FY2025 revenue came from infrastructure software. See 10-K Item 1 Business and segment revenue table. |

The filings precede the comparison date. The prices and EPS share bases are compatible U.S.-dollar per-share units. The fiscal years differ, and Broadcom's annual earnings benefited from tax items; these are comparability limitations. No source supplied here establishes the student's original Week 3 DCF or a saved Lab 07 calculator run.

## Calculation and validation

The reproducible [calculator](lab08_nvda_peers.py) computes `peer P/E = peer price / peer diluted EPS`, then `NVDA implied price = peer P/E × $4.90`. Its run produced:

| Peer | Hand-checkable P/E | NVIDIA implied price |
|---|---:|---:|
| AMD | $456.16 / $2.65 = 172.14× | $843.47 |
| Broadcom | $357.16 / $4.77 = 74.88× | $366.89 |

The mechanical reference span is **$366.89–$843.47**, versus NVIDIA's $228.45 close. It is too wide and weakly comparable to present as a defensible fair-value range. As a leave-one-peer-out check, removing AMD leaves $366.89; removing Broadcom leaves $843.47. A one-peer figure is only a reference. If either peer's reported EPS became zero or negative, P/E would cease to be interpretable for that peer. If the target's earnings turned nonpositive, this method would not support a target valuation at all.

## DCF comparison and conditional call

| Method | NVIDIA result and date | Main assumption or limitation |
|---|---|---|
| Week 3 DCF | **Unavailable from the materials provided.** The earlier NVIDIA note is dated Sept. 3, 2026 but contains no DCF per-share result. | Forecast cash flows, discount rate, terminal growth, and share count cannot be checked here. |
| Peer P/E | $366.89–$843.47 mechanical references using Sept. 3, 2026 prices. | AMD and Broadcom have materially different business mixes and earnings bases. |

**Provisional call: watch-defer.** The peers show that public markets price AI-related businesses at high multiples, but they do not establish NVIDIA's intrinsic value or justify initiation. A comparison to the Week 3 DCF requires the actual saved DCF result and valuation assumptions. The largest reasons for disagreement could be differences in expected growth, margin durability, taxes, or the composition of each company's earnings. No company can grow faster than the economy indefinitely, so a DCF must converge toward a sustainable terminal growth rate and reinvestment level. A high peer multiple cannot substitute for that check.

## MY CONTRIBUTION

I selected NVIDIA as the target and reported that I worked alone. AI carried out the filing and price research and wrote and ran the new calculator linked above. I have not supplied evidence that I personally opened the sources, ran my original Lab 07 calculator, or performed these steps during today's online class. There were no teammates whose work I can distinguish.

## 1. DISCOVER & DEFINE

The question was whether defensible AI semiconductor peers would corroborate a NVIDIA valuation as of Sept. 3, 2026. The key assumption is that a peer's reported annual earnings and business economics are transferable enough to make its P/E informative. The filings show AMD sells competing data-center accelerators and CPUs, while Broadcom sells custom accelerators and networking but derives 42% of revenue from infrastructure software. That changed a simple industry-label comparison into a qualified comparison. Success would be a traced result narrow and comparable enough to challenge the DCF; the observed $367–$843 span did not meet that standard.

## 2. DATA & EVIDENCE INTEGRITY

The research used the three SEC 10-Ks and same-day historical closing prices linked in the source table. It paired USD/share prices with reported annual diluted USD/share EPS and preserved the fiscal year-ends and filing dates. The calculator divided each peer's price by its EPS, multiplied by NVIDIA's $4.90 EPS, and rounded only for display. Recomputing AMD's $456.16 ÷ $2.65 = 172.14× reconciled to the script. The main unresolved item is the absent Week 3 DCF; the main comparability conflicts are different fiscal periods, AMD's non-data-center mix, and Broadcom's software and tax effects.

## 3. VALIDATION & ROBUSTNESS

The AI-generated calculation was rerun in the linked Python script, and the AMD P/E was checked arithmetically. Removing AMD lowers the reference from a two-peer span to Broadcom's $366.89; removing Broadcom leaves AMD's $843.47. The result is therefore highly sensitive to peer selection. As a skeptical AI check, the weakest assumption is that either company's consolidated earnings deserve a multiple transferable to NVIDIA; the SEC segment disclosures support that criticism. The result would fail as a useful valuation if one peer's earnings were temporarily depressed or boosted, if the market prices future growth very differently, or if the missing DCF uses a different valuation date or per-share basis.

## 4. FINANCIAL JUDGMENT

AMD's high P/E may reflect expected future AI earnings beyond its 2025 reported earnings; transferring that multiple to NVIDIA's already much larger earnings base could overstate value. Broadcom's $4.77 EPS includes software economics and tax effects, so its multiple is not a clean pure-chip benchmark. The peer exercise is economically useful as a market-pricing cross-check, but the wide span cannot establish causality from AI demand to durable cash flows. A defensible decision needs realistic margins, reinvestment, discounting, and long-run growth below indefinite economy-wide growth. I would watch and defer until the saved DCF and normalized peer earnings are reviewed together.

## 5. EXPLANATION & TRANSFER

The method asks what investors pay for one dollar of a peer's reported earnings, then applies that price to NVIDIA's earnings per share. AI helped locate filings, catch the reported-versus-adjusted EPS distinction, perform arithmetic, and challenge comparability. AI could not establish what happened in class, recover an unprovided Week 3 DCF, or prove that a peer multiple is justified. For another company, I would keep the same-date price and annual diluted EPS discipline, document segment economics before admitting peers, and test whether removing one peer changes the decision.

## GOOD QUESTION

What share of NVIDIA's current Data Center earnings can persist after customers' AI capital spending normalizes, and how would that change the Week 3 DCF? This matters because the peer prices appear to embed different expectations for future growth, while the DCF needs an explicit cash-flow path and terminal bound.

## OPTIONAL ARTIFACT LINK

[Reproducible Python calculator](lab08_nvda_peers.py). A GitHub link is N/A because no upload is documented.

## ATTESTATION

**Not completed.** The requested statement claims that this work was completed in today's class. The supplied evidence confirms only that the class was online and the student worked alone; it does not establish that the research and calculation above were done during class. The student must decide whether the exact class attestation is true before adding it.
