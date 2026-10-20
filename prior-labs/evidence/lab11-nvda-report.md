# Lab 11 — NVIDIA operating-driver sensitivity

Prepared September 29, 2026 using the existing September 24 Lab 10 model. AI-assisted analysis; personal prediction and partner evidence remain to be supplied. No submission has been made.

## Question and method

Which assumptions drive NVIDIA’s forecast and modeled equity value, and what explains their effects? Each scenario starts from a fresh independent copy of the same base assumptions. The entire five-year linked model is rerun. Only one operating assumption path changes; dependent statement balances recalculate. Outputs are FY2031 operating profit, FY2031 FCFE, and modeled USD/share. Financial statement figures are USD millions.

## Input ranges

These are **AI-proposed judgment ranges**, not management guidance, confidence intervals, or student-selected ranges already confirmed in class. They can be replaced in `DRIVERS` in the script. All five forecast years are affected.

| Driver / case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---:|---:|---:|---:|---:|
| Revenue growth — Lower | 82.3857% | 30.0000% | 20.0000% | 10.0000% | 3.0000% |
| Revenue growth — Base | 87.3857% | 35.0000% | 25.0000% | 15.0000% | 8.0000% |
| Revenue growth — Higher | 92.3857% | 40.0000% | 30.0000% | 20.0000% | 13.0000% |
| Gross margin — Lower | 72.0000% | 71.0000% | 70.0000% | 69.0000% | 68.0000% |
| Gross margin — Base | 74.0000% | 73.0000% | 72.0000% | 71.0000% | 70.0000% |
| Gross margin — Higher | 76.0000% | 75.0000% | 74.0000% | 73.0000% | 72.0000% |

**Growth range rationale:** ±5 percentage points tests a faster or slower fade in demand growth, applied to the existing judgment path. The same annual shift compounds across five years. This is a deliberately chosen stress range, not an empirically estimated probability band. FY2027 also shifts even though part of that year was already actual in the original model; it therefore represents a changed full-year outcome driven by the remaining forecast portion.

**Gross-margin range rationale:** ±2 percentage points extends the existing Lab 10 downside margin scenario symmetrically. It tests product mix, pricing, competition, and cost pressure around the existing margin fade. Historical margins in the saved Lab 10 report were about 72.72%, 74.99%, and 71.07%; those provide context but do not statistically establish these endpoints.

A move from 70% to 72% is +2 percentage points (0.02 in the Python model), not a 2% relative increase. Cost of equity stays 12%, terminal growth stays 3%, and shares stay 24,100 million in every run.

## Visible results

| Case | Operating profit ($m) | Change ($m) | FCFE ($m) | Change ($m) | Value/share ($) | Change ($/share) |
|---|---:|---:|---:|---:|---:|---:|
| Revenue growth — Lower | 389,122.42 | -84,947.92 | 309,653.43 | -59,910.44 | 126.1064 | -22.6226 |
| Revenue growth — Base | 474,070.33 | +0.00 | 369,563.87 | +0.00 | 148.7290 | +0.0000 |
| Revenue growth — Higher | 573,119.02 | +99,048.68 | 438,404.48 | +68,840.61 | 174.8502 | +26.1212 |
| Gross margin — Lower | 457,617.80 | -16,452.53 | 355,675.17 | -13,888.70 | 143.4068 | -5.3223 |
| Gross margin — Base | 474,070.33 | +0.00 | 369,563.87 | +0.00 | 148.7290 | +0.0000 |
| Gross margin — Higher | 490,522.86 | +16,452.53 | 383,452.57 | +13,888.70 | 154.0513 | +5.3223 |

Differences and spans use unrounded calculations; displayed figures may differ in the last decimal when subtracted.

| Driver | Operating-profit span ($m) | FCFE span ($m) | Value span ($/share) |
|---|---:|---:|---:|
| Revenue growth | 183,996.6000 | 128,751.0485 | 48.7438 |
| Gross margin | 32,905.0606 | 27,777.3998 | 10.6445 |

**AI analysis to review and explain:** Revenue growth has the larger span for all three outputs **over these ranges**. Increasing growth each year compounds revenue, raising gross profit and earnings. It also raises receivables, inventory, capital spending, and other linked balances, so part of the profit gain is absorbed by investment. The FCFE span is therefore smaller than the operating-profit span. This result does not prove growth always matters more: the ranking depends on both the chosen range and the model.

## Trace one result through the statements

For higher gross margin, growth and revenue stay at base. The following FY2031 bridge isolates the causal link. All amounts are USD millions.

| Statement line | Base | Higher margin | Signed difference |
|---|---:|---:|---:|
| revenue | 848,068.572375 | 848,068.572375 | +0.000000 |
| gross_profit | 593,648.000663 | 610,609.372110 | +16,961.371447 |
| cogs | 254,420.571713 | 237,459.200265 | -16,961.371447 |
| sga | 17,809.440020 | 18,318.281163 | +508.841143 |
| rd | 101,768.228685 | 101,768.228685 | +0.000000 |
| operating_income | 474,070.331958 | 490,522.862262 | +16,452.530304 |
| interest | 259.000000 | 259.000000 | +0.000000 |
| tax | 80,547.926433 | 83,344.856584 | +2,796.930152 |
| net_income | 393,263.405525 | 406,919.005677 | +13,655.600152 |
| depreciation | 13,060.890436 | 13,060.890436 | +0.000000 |
| amortization | 679.539644 | 679.539644 | +0.000000 |
| delta_nwc | 11,997.909384 | 11,764.809618 | -233.099766 |
| cfo | 395,005.926221 | 408,894.626139 | +13,888.699918 |
| capex | 25,442.057171 | 25,442.057171 | +0.000000 |
| fcfe | 369,563.869049 | 383,452.568968 | +13,888.699918 |

At unchanged revenue, the two-point gross-margin increase raises gross profit. SG&A increases because the model expresses it as a share of gross profit; R&D stays constant because it is a share of unchanged revenue. Taxes absorb 17% of the operating-profit gain. Lower cost of revenue reduces inventory and payables; the net change in working-capital investment also affects FCFE. Capex and D&A stay unchanged in this margin test.

Independent arithmetic checks: final-year operating-profit gain = base FY2031 revenue × 0.02 × (1 − 0.03). FCFE gain = change in net income + change in D&A − change in working-capital investment − change in capex; financing is unchanged.

## Verification

- Every scenario passes the original model’s accounting and funding checks in all five years. Visible check blocks are in `lab11-nvda-output.txt`.
- The script asserts that only the selected independent assumption changed. Complete input snapshots and full statements for every run are in `lab11-nvda-details.json`.
- All signed changes are changed output minus the original base. Each span is maximum minus minimum across lower/base/higher valid outputs.
- Restored base passes: all statement fields match within 0.000001 USD million, with identical independent inputs and valuation outputs.
- The original Lab 10 self-tests also pass, including deliberate accounting corruption, invalid discount-rate, and funding-shortfall rejection.
- Invalid accounting runs are labeled and excluded. Valuation errors preserve usable operating profit and signed FCFE. Each span records the number of valid runs; an incomplete range cannot establish the full three-case ranking.

## Valuation interpretation and limitation

The existing annual teaching valuation gives $148.73/share at base. The tested growth cases give $126.11–$174.85; the margin cases give $143.41–$154.05. All remain below the **saved September 24 reference** of $224.20, so these individual tests do not reverse that model-versus-reference comparison. This is not a current quote or same-day investment recommendation.

The original annual model discounts to FY2026 end while using information assembled later. It retains simplified financing, fixed shares, a 12% cost of equity, and a 3% terminal growth assumption. A changed final forecast margin also carries into terminal profitability under the existing valuation function. Growth scenarios keep terminal growth at 3% but change the revenue base entering the terminal period. These are internally consistent teaching-model values, not an updated valuation as of today.

**Possible research priority to discuss:** investigate evidence supporting the revenue-growth fade because it produces the largest tested output spans. Sensitivity alone does not establish which input is least certain; weigh range evidence too.

## Personal evidence — not yet recorded

**Locked Changed-Input Record:** No student-authored, timestamped pre-run prediction was supplied in this task. The tables above were already generated. Do not describe a prediction written after seeing them as locked beforehand. If you already saved one in class, insert its original timestamp or commit, old → new input and units, predicted direction and rough size, actual result, prediction error, and explanation. Otherwise a genuinely new, not-yet-run scenario is needed for a fresh prediction; explain any process change to your instructor.

- Original prediction and timestamp/commit: **[supply actual record]**
- Actual matching result and calculation: **[match to the original prediction]**
- Prediction error and explanation: **[complete after comparing]**
- Does the result change your conclusion or research priority, and why?: **[your reviewed response]**

**Partner evidence:** record actual exchanges, not the illustrative prompts below.

- Partner Purdue email: **[needed]**
- Range/unit question received and your answer: **[needed]**
- Check you performed on your partner’s analysis, including their figures and your recomputed difference: **[needed]**
- Result-tracing question or correction and your response: **[needed]**
- Range-ranking question received and your response: **[needed]**

Discussion prompt you can use: “Could growth rank first partly because we tested a ten-percentage-point growth range but only a four-percentage-point margin range?” The analysis supports answering that the range matters and growth also compounds across years, so the conclusion is limited to these specific tests. This is a prepared prompt, not a completed partner exchange.

## Learn-on-your-own answers

1. One-at-a-time sensitivity changes one independent assumption while resetting all others to base and recalculating the linked model.
2. A wider input range can create a larger output span and change the ranking; always say “over these ranges.”
3. A sensitivity table maps assumptions to outcomes. It assigns no probabilities to the assumptions and is not a forecast probability distribution.

## Run and checkout

Keep the Python files together and run:

```sh
python3 lab11_nvda_sensitivity.py
```

Question 1 details: teammate Purdue email **[needed]**; AI partner **OpenAI Codex (ChatGPT)**; today’s session token **[needed]**. Make the requested in-person statement only if it accurately describes your participation.

Question 2: upload the package if using the file-upload option shown in Brightspace, or put the files in your existing course GitHub repository and submit their actual links. No repository URL was supplied here and no GitHub links are fabricated. The technical work is prepared; the personal evidence above remains incomplete.

Files: [sensitivity script](lab11_nvda_sensitivity.py), [unchanged model](nvda_proforma.py), [visible output](lab11-nvda-output.txt), [complete run details](lab11-nvda-details.json), and [prior source/assumption report](lab10-nvda-report.md).
