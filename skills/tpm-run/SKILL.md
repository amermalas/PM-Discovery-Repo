---
name: tpm-run
description: Use for Stage 4 (RUN) of the 5-stage delivery loop, operating a program week to week once it is planned and aligned. Runs the status cadence, reviews the risk register, converts overdue risks into issues, runs change control against the baseline, keeps the decision log, and brings tradeoffs to the decider with options when the plan breaks. Trigger on "weekly status", "we're slipping", "a team pulled out", "scope creep", "leadership wants to add X", "re-plan", or "is this program on track". Routes a program that is badly off plan to program-recovery.
---

# TPM Run: Stage 4, operate the program and handle what breaks

Part of a 5-stage delivery loop (FRAME -> PLAN -> ALIGN -> RUN -> LAND). Plans break. This stage is about noticing early, making the tradeoff visible, getting the right person to decide it, and recording the decision so nobody re-litigates it next week.

The TPM's job during execution is not to absorb problems quietly. It is to turn surprises into decisions.

## Objective

Keep the program's real state visible, and turn every material change into an explicit, recorded decision against the baseline.

## Required inputs

- The baselined plan and dependency map (`tpm-plan`).
- The risk register (`risk-register`).
- The decision forum and communication plan (`tpm-align`).
- This week's signals: milestone status, burn or velocity, open blockers, new requests, incidents.

## What to do

1. **Update status from evidence, not from optimism.** Milestone state, critical-path float, risk changes, open decisions. Route to `program-status-report` and `scripts/status_report.py`.
2. **Review the risk register.** Re-score changed risks. Any risk not resolved by its resolve-by date becomes an **issue** with a written explanation and an owner. Run `scripts/risk_register.py` to flag these.
3. **Run change control against the baseline.** Every new request, including an executive one, gets a cost attached: what slips, what it risks, and what cheaper alternative engineering can offer. Bring **the cost of yes** to the decider rather than saying yes or no yourself.
4. **When the plan breaks, bring options, not a problem.** Route to `tradeoff-decision-brief`. Use the four knobs (date, scope, resources, quality). The knob fixed in the charter stays fixed unless the decider changes it; flex the others. Always offer at least two options with consequences and a recommendation.
5. **Protect the critical path first.** A slip off the critical path may be absorbed. A slip on it moves the date unless something else changes.
6. **Record every decision** in `templates/decision-log.md`: what was decided, by whom, the options considered, and what it changes in the plan. Then update the plan, dashboard, and register.
7. **Turn repeated conflicts into system fixes.** If the same kind of blocker recurs (capacity, unclear ownership, a missing interface), fix the process that produces it, not just the instance.
8. **Recognize when a program needs recovery.** If most of the budget or time is spent with much less of the scope done, or the plan has been changed so often nobody trusts it, stop incremental patching and route to `program-recovery`.

## Outputs

- A weekly status report per stream (see `program-status-report`).
- An updated risk register with overdue risks converted to issues.
- Decision log entries for every material change.
- Tradeoff briefs for decisions that need the decider.
- A re-baselined plan when the decider approves a change.

## Review gate

Nothing material changes in scope, date, resources, or quality without a decision log entry naming the decider. If the status report and the decision log disagree, the program's real state is unknown.

## Copy-ready prompt

> Using the baselined plan, risk register, and this week's updates, produce the weekly program status. Lead with the overall status color and, for yellow or red, the business impact rather than just the slip. List critical-path changes, risks re-scored, risks past their resolve-by date (convert them to issues), new change requests with the cost of yes and a cheaper alternative, and the decisions needed this week with a deadline for each. Do not mark anything green without evidence in the inputs.

## Related repo resources

- Before: `tpm-align`.
- Detail: `program-status-report`, `risk-register`, `tradeoff-decision-brief`, `program-recovery`, `templates/decision-log.md`, `scripts/status_report.py`, `scripts/risk_register.py`.
- Next: `tpm-land`.

## Guardrails

- Do not promise the same scope on less time or fewer people by "working harder." That is the answer that burns teams and misses anyway.
- Do not change the fixed variable without the decider.
- Do not let a status color hide an unmade decision. Yellow with no decision requested is not a status.
