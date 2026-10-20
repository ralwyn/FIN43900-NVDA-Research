# NVIDIA decision workbench - executed output

Valuation: September 24, 2026 close. Latest reported BS: July 26; interim balances estimated. Prepared October 19. USD/share below.

Proposed committee action: WATCH / DEFER, subject to student review. Same-date market close: $224.58.

| Scenario | Value/share | WACC | Terminal share of EV |
|---|---:|---:|---:|
| Downside: AI spending slows and pricing weakens | $99.65 | 13.94% | 65.0% |
| Base: demand growth fades as scale expands | $157.96 | 11.95% | 73.6% |
| Upside: durable demand and pricing | $284.35 | 9.96% | 82.4% |

## WACC / terminal-growth sensitivity

| WACC | g=2% | g=3% | g=4% |
|---|---:|---:|---:|
| 10% | $182.61 | $202.62 | $229.30 |
| 12% | $145.44 | $157.06 | $171.57 |
| 14% | $120.75 | $128.15 | $137.03 |

## Reverse DCF

{"target": 224.58, "status": "No growth solution inside bounded +/-10pp domain", "low": 112.30704859499251, "high": 218.94443908509007, "implied_required_equity_return": 0.09358393725416125, "implied_wacc": 0.09323939267945808, "solved_per_share": 224.57999999999998, "qualifier": "Fixed base operating forecast and bridge; a conditional market-implied discount rate, not a measured cost of capital."}

## Definitions and limits

Full inputs, statements, bridge, dates, peer calculations and tests are in visible-output.json. Peer EV/Sales uses annual historical revenue and dated basic shares; P/E uses annual GAAP diluted EPS. Stale share/balance dates, business mix and transitory earnings weaken comparability. Do not average the mechanical peer references into DCF. Straight-line interim balances, simplified taxes, no new acquisitions/investments/buybacks and cash-equivalent SBC constrain the model. WACC inputs and bounds are judgment ranges, not confidence intervals.

## Validation

PASS: Published synthetic FCFF 77.5m and enterprise-equity result $8.20/share.
PASS: Q2 reported assets and liabilities match the primary release.
PASS: All five future periods reconcile BS, cash, equity, productive assets, income, financing and FCFF.
PASS: Elapsed July-to-September flows excluded; estimated valuation-date bridge separate.
PASS: WACC and terminal-growth monotonicity over tested grid.
PASS: Additional inventory investment reduces first-period FCFF.
PASS: Diluted denominator doubles -> per-share value halves; basic market-cap weight unchanged.
PASS: cash corruption refused: FY2027 balance sheet: gap 1.000000; valuation refused
PASS: funding shortfall refused: Cash below liquidity floor; no invented borrowing facility.
PASS: invalid terminal refused: Invalid terminal growth or tax rate.
PASS: Peer EV identities and positive annual denominators.
PASS: Restored base exactly matches before automated tests. These are AI-run tests, not the student locked record.
