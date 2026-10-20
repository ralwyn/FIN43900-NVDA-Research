# Video 2 - code and validation (maximum 5 minutes)
Preparation notes, not a transcript. Keep model.py, analysis.py, the app and validation log open.

0:00-0:40: Open README. Run python3 analysis.py; explain standard-library setup and the output files. model.py contains inputs/statements/DCF, analysis.py contains cases, peers and tests; app.py is a driver panel around the same engine.

0:40-1:35: In model.py, trace revenue to gross profit, SG&A, R&D, EBIT and operating taxes. Then show receivables, inventory, payables, depreciation, capex and cash. Cash is computed from flows, never plugged to force balance. The first DCF column is the remaining FY2027 stub.

1:35-2:25: Explain July reported balances -> estimated September balances -> future cash flows. Show WACC weights and the operating EV-to-equity bridge. No accumulated future cash is added twice. Basic shares calculate market-cap weights; diluted proxy divides equity value.

2:25-3:40: Run the known-answer and deliberate cash-corruption guard. Show the exact $1m gap and restore base. If you completed the personal locked test, show its actual precommit/hash and result; otherwise disclose that it is missing. Do not describe an agent's automatic test as your AI-off run.

3:40-4:25: Show cold-run-log.txt: fresh venv, no packages/network; numerical comparison within 1e-6 tolerance. Explain the first exact-JSON comparison's cross-runtime rounding difference and how it was diagnosed.

4:25-5:00: State the main unresolved limitation: straight-line interim estimates and terminal/forecast uncertainty. Explain one line in your own words; do not just read the interface. Correct the actual transcript after recording.
