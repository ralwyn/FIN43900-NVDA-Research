# Lab 09 — ABG Pro-Forma Build

AI partner: OpenAI Codex. This model was built with AI from the supplied Lab 09 instructions and executed to verify the known answer. The student reports watching all four assigned videos and completing the assignment at home without a teammate, per the instructor's direction. No human partner swap is claimed.

## Question

What are five years of a company's statements worth, built from assumptions you can defend, and how do you know the statements are right?

## Run and verify

```sh
python3 proforma.py
python3 proforma.py --break-2026-cash
```

The first command prints the checks, all three statements, and valuation. The second deliberately sets FY2026E cash to 40.4 and exits with an error before printing a valuation. Run the first command again for the restored base case; the demonstration does not edit the file.

## Results

All amounts are USD millions except value per share. Calculations retain full precision; statement display is rounded to one decimal.

| Line | FY2026E | FY2030E |
|---|---:|---:|
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| FCFE | 211.4 | 342.3 |
| Ending cash | 101.8 | 719.8 |
| Assets minus liabilities minus equity | 0.0 | 0.0 |

Equity value: **5,237.34 million**. Value per share: **$291.75**. Share of value after 2030: **79.76%**. No revolver draw is required in the base case.

Every projected year balances, reconciles balance-sheet cash to the cash-flow statement, and meets the 25 minimum cash balance. `assert_balanced` is called inside the valuation function before discounting. It also rejects a revolver balance outside the stated limit.

Observed deliberate-break error:

```text
ValueError: FY2026E: assets minus liabilities minus equity gap -61.4; valuation refused
```

See `lab09-model-output.txt` for the complete run and `lab09-validation.txt` for the automated benchmark and refusal checks.

## Labelled assumptions

Source: supplied `lab-09-proforma-build.md`. Labels below reproduce the instructor's classifications; historical numbers, guidance and the share count have not been independently checked against filings in this exercise. Judgment values are adopted to reproduce the assigned ABG case, not presented as independent investment forecasts.

| Assumption | Value | Label | Basis / role in the assigned case |
|---|---|---|---|
| Organic growth | 1.8% annually | judgment | Project recurring growth of existing operations. |
| Gross margin | 17.05% | judgment | Hold gross profit per dollar of revenue constant. |
| SG&A / gross profit | 66.5%, 65.5%, 64.5%, 64.5%, 64.5% | judgment | Model a gradual improvement in expense efficiency, then stability. |
| Depreciation / opening PP&E | 82.4 / 3,070.4 | history | Preserve exact supplied FY2025 ratio. |
| Non-cash impairment | 120 annually | judgment | Reduce earnings and other assets; add back in cash flow. |
| Capital spending | 250 annually | guidance | Use the course's guidance input. |
| Tax rate | 25.5% | judgment | Apply to positive pretax income. |
| Inventory days | 2,135.8 / (17,999.0 - 3,071.7) × 365 | history | Link inventory to forecast cost of sales. |
| Floor plan / inventory | 2,027.0 / 2,135.8 | history | Inventory financing grows with inventory. |
| Other working capital | 0.8% of change in revenue | judgment | Capture incremental operating investment as sales grow. |
| Minimum cash | 25 | history | Maintain the course's cash floor. |
| Revolver limit | 850 | judgment | Bound available liquidity support. |
| Revolver interest | 6% | judgment | Charge interest on opening revolver balance. |
| Debt repayment | 150 annually | judgment | Follow the prescribed explicit-period debt reduction. |
| Share buyback | 150 annually | judgment | Reduce cash and equity after FCFE. |
| Floor-plan interest | 4.67% | history | Apply to opening floor-plan balance. |
| Term-debt interest | 5.44% | history | Apply to opening term debt. |
| Cost of equity | 10% | judgment | Assigned return used to discount equity cash flows. |
| Terminal growth | 2.5% | judgment | Assigned perpetual growth rate, below cost of equity. |
| Shares outstanding | 17.951349 million | fact, as labelled in course | Course cites the June 30, 2026 10-Q; denominator held constant as instructed. |

Opening FY2025 balance sheet: cash 40.4; inventory 2,135.8; PP&E 3,070.4; other assets 6,371.6; floor plan 2,027.0; term debt 3,572.0; other liabilities 2,127.5; equity 3,891.7. Opening revolver is zero. Opening revenue is 17,999.0. Assets and liabilities plus equity both total 11,618.2.

## Explanation to review and discuss

**Three operating judgments:** organic revenue growth, gross margin, and SG&A as a share of gross profit determine the operating earnings path. The discount rate and terminal growth also matter greatly: approximately 80% of this valuation comes from after 2030.

**Why cash comes last:** cash is the consequence of earnings, non-cash adjustments, investment, working capital, borrowing and distributions. Computing cash through those flows permits an independent balance-sheet check. It is not an arbitrary number inserted to force the balance sheet to balance.

**What the -61.4 gap means:** actual computed 2026 ending cash is 101.8, an increase of 61.4 from opening cash of 40.4. Holding cash at its opening amount understates assets by 61.4 while the other balances still reflect the year's activity. The sign and size identify the missing cash increase.

**Floor plan:** these are loans financing vehicle inventory. The model charges interest on the opening loan balance and includes the change in floor-plan financing in the operating cash-flow bridge, following the lab's convention. Removing that financing while retaining the inventory investment creates a cash shortfall; it is not free inventory. This submission does not independently reproduce the video's separate approximately -1.1 billion removal scenario.

**Terminal value:** the lab adds back the final year's 150 repayment before applying 2.5% perpetual growth, then divides by 10% minus 2.5%. This avoids assuming that the fixed annual debt repayment continues forever. Terminal value and the five explicit FCFE amounts are discounted at 10%; no additional debt subtraction is applied because the model values equity cash flows directly.

This is the prescribed teaching case, not an investment recommendation. Automated validation is documented; a human partner discussion or swap is not represented as completed.
