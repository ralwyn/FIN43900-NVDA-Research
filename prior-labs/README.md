# Lab 12 — NVIDIA presentation and review kit

**Start with [the speaking guide](01-speaking-guide.md).** It follows the six required stops and gives plain-language phrasing plus the evidence to open. Plan for 15 minutes of explanation and showing evidence, 10 minutes of questions/checks, and 5 minutes of explanation back and feedback. Then swap.

**Complete [the review record](02-review-record.md) from your actual exchange.** It covers both presenter and reviewer roles, the evidence check, feedback, and the keep/revise/investigate decision.

## Ready for use

- Original company selection and research, saved peer analysis, Lab 10 model/valuation, and Lab 11 sensitivity evidence are collected in `evidence/`.
- A clearly labeled new reverse-DCF supplement solves for a uniform annual growth shift matching the saved September 24 price, with all other independent assumptions fixed. It does not recreate the missing original Week 3 work.
- The speaking guide distinguishes FCFE/cost of equity from the original FCFF research plan, explains peer disagreement, and records date/share-basis limitations.

## Reproduce the new supplement

```sh
python3 reverse_dcf.py
```

Uses the unchanged Lab 10 engine in `evidence/`. No third-party packages needed. It writes `reverse-dcf-results.json` and `reverse-dcf-output.txt` and verifies accounting, the target price, and restoration of the base.

## What remains yours to complete

The live presentation, actual questions/answers, review of your partner's company, the source/calculation checked together, and response to feedback. The notes template does not claim these happened. Your class worksheet asks for AI to stay closed during presentation and questioning.

The optional third-driver challenge is ungraded and separate; it is not required for this checkout. No slide deck, new app, or recording is necessary.

## Checkout and five grading criteria

Use actual GitHub file links after publication, especially the completed review record and relevant evidence. The five criteria are: full analysis/ownership; valuation reasoning; sensitivity interpretation; reviewing the partner; response/revision. Prepared technical evidence supports the first three, but the last two require the actual exchange.

No GitHub push or Brightspace submission is claimed. The earlier Lab 11 push was blocked by missing GitHub authentication.
