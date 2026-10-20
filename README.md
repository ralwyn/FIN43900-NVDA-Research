# Public project copy
Personal test records and the detailed course-only validation record are withheld from this public copy. Student reports a TA-approved exception. This repository is not the complete grading submission.

# NVIDIA decision workbench | FIN439 Project 1

**Proposed action: watch/defer initiation.** The fund owns no position. Valuation date: **September 24, 2026 close**; preparation date: October 19. USD common shares; five forecast periods through FY2031, starting with the remaining FY2027 stub.

The rounded DCF scenario span is **$100-$285/share**, with a **$158 base** versus the **$224.58** same-date closing price. This is a scenario analysis, not a statistical interval or October 19 quote. The student must review and defend the recommendation. Final submission status is recorded in `submission-manifest.csv`; recordings and the personal locked-test record are not claimed unless actually linked there.

## Start here

- `Decision-Memo.pdf`: two-page committee recommendation, evidence, range, conditions and triggers.
- `Research-Evolution.pdf`: Edition B and the unchanged recovered local Edition A artifact, with provenance limits stated.
- `Validation-and-AI-Use.pdf`: source/definition ledger, normalizations, driver challenges, checks, limitations and separate material AI-use record.
- `visible-output.md` and `visible-output.json`: executed results, full inputs, linked statements, bridge, cases, sensitivities, reverse DCF and peer references, visible without running code.

## Run from a clean checkout

Python 3.9 or newer. Standard library only: no pip packages, account, API key, runtime download or deployment is needed.

```sh
python3 analysis.py
python3 app.py
```

Open **http://127.0.0.1:8439/**. Change a bounded driver and press Recalculate. Restore base resets the inputs. Inject $1m cash error demonstrates a red valuation-blocking accounting failure; restore base to recover. Ctrl+C stops the local server. If port 8439 is already in use, stop the earlier copy of this app before starting another.

## Repository map and finance flow

`model.py`: reported inputs, assumptions, company-specific operating drivers, linked income statement/BS/CF, accounting guards, interim roll, FCFF, WACC and enterprise-equity bridge.

`analysis.py`: causal cases, WACC/g grid, one-at-a-time shocks, range-dependence test, reverse DCF, P/E and EV/sales references, automated checks, frozen output generation.

`app.py`: local bounded driver workbench around the same engine. Controls expose growth and gross-margin shifts, required equity return and terminal growth. WACC is calculated, not mislabeled as cost of equity.

`locked_test.py`: student-operated two-stage prediction/execution record. It has not been run by the agent for the student's fresh scenario. `docs/` contains content-equivalent written public summary records and recording preparation notes. Preparation notes are not transcripts of completed videos. `prior-labs/` preserves recovered historical work with its original caveats.

## Accounting and valuation conventions

Latest reported opening BS: July 26, 2026. A disclosed straight-line operating roll estimates September 24 balances. Only cash flows after September 24 enter DCF; all July-to-September estimated cash flows are excluded from future PV. The remaining FY2027 period is a stub; FY2028-31 are full modeled fiscal years. `annual_forecast_periods` also preserves the full H2 forecast and later annual periods; actual H1 financial data are locked in the input layer.

FCFF = EBIT x (1-tax) + D&A - capex - change in operating working capital. Financial gains and interest income are excluded from projected operating earnings. SBC stays a compensation cost with no free cash-flow addback. Cash follows CFO+CFI+CFF; it is never an accounting plug. Leases remain in operating expenses and are not double-counted as debt in the bridge.

WACC combines 12% required equity return, 4.5% borrowing cost, 17% tax, $33.366bn carrying debt and market equity based on 24.1bn basic shares. Financing rates are explicit judgment inputs, not a fitted beta or observed yield claim. Base WACC is about 11.95%. Equity value is divided by a 24.285bn Q2 diluted weighted-average proxy, held fixed rather than represented as a forward dilution forecast.

Terminal reinvestment funds growth in productive assets and working capital. Opening excess cash and financial investments are added once; debt is subtracted once. Accumulated future cash is not added again. Fixed private carrying values are haircut by 25%; realization tax and portfolio valuation remain risks. No future acquisitions, new financial investments or buybacks are modeled. Other noncurrent balances and current accrual composition are simplified. These assumptions can materially affect value despite balanced statements.

## Validation and reproducibility

Run `python3 analysis.py`. The published fixture gives FCFF 77.5m and $8.20/share. All five future periods pass statement and FCFF checks at 1e-6m tolerance. Discount-rate/g, inventory and share-denominator tests pass; deliberate cash corruption, unfunded distribution and incoherent terminal cases are refused. Base is restored after testing.

`cold-run-log.txt` records a fresh-venv run with no packages or network. Exact JSON comparison initially differed at floating-point last bits between Python runtimes; all text/structure matched and maximum numeric difference was 4.66e-10, well within accounting tolerance. This was an agent-operated cold run, not falsely attributed to the student. Automated tests are distinct from the required human-authored Locked Changed-Input Record.

## Peer policy and interpretation

Admit listed operating issuers with AI compute/networking exposure and positive annual GAAP EPS before looking at implied values. AMD and Broadcom are qualified for business-mix/accounting differences; industry labels alone do not establish comparability. Use the same September 24 close, annual reported EPS/revenue, carrying debt and cash/short-term investments, and dated basic-share proxies. Peer share/financial dates are stale relative to the quote. P/E and EV/sales are reference calculations, not adopted valuation ranges. No mechanical averaging with DCF; no transferable control-transaction multiple is claimed.

## Source map and monitoring

Exact URLs, availability dates, transforms and definitions are in the validation record. Core sources: NVIDIA FY2026 10-K and Q2 FY2027 release; AMD and Broadcom FY2025 10-Ks; FinancialContent NVDA history; Stock Analysis peer history. New guidance, export policy, customer investment returns, collections/inventory, capital allocation and price/value triggers require review. This dated model does not automatically ingest later information.

The separate validation record identifies material AI contributions, their checks and limits. The recovered local Edition A artifact is preserved unchanged; it is not mislabeled as a verified on-time AI-off checkpoint. Personal records, actual recordings, corrected transcripts, URLs, access checks and the final Brightspace receipt must reflect what actually occurred.
