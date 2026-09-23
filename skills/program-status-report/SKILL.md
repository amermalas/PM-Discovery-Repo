---
name: program-status-report
description: Use to write a program status update for a specific audience. Produces an executive update (status color, business impact, options, decisions needed), a partner-org update, and a working-team update from the same underlying plan, risk register, and decision log. Trigger on "weekly status", "exec update", "status report", "program update", or "what do I tell leadership". Can be seeded by scripts/status_report.py.
---

# Program Status Report

One program, three audiences, three different reports. Executives need to know whether to act. Partner orgs need to know what to plan around. The working team needs to know what changed and what is next. A single report written for everyone serves none of them.

## Inputs

- the baselined plan and milestone status (`templates/dependency-map.csv`)
- the risk register (`templates/risk-register.csv`)
- the decision log (`templates/decision-log.md`)
- this period's changes, blockers, and wins

## Workflow

1. **Generate the factual core.** Run `python scripts/status_report.py --plan <dependency-map.csv> --risks <risk-register.csv> --today YYYY-MM-DD` to get milestone state, critical-path float, top risks, and overdue risks. Treat the script's output as a draft; the TPM owns the judgment.
2. **Set the status color from evidence:**
   - **Green:** on track against the baseline; no decision needed.
   - **Yellow:** at risk; a mitigation is in progress or a decision may be needed.
   - **Red:** off baseline; a decision is needed to recover.
3. **Write the executive update:**
   - one line: status color and the single most important thing
   - for yellow or red: the **business impact**, not only the slip (a week's delay and losing a launch commitment to a key customer are different problems)
   - options, usually plan A and plan B, with a recommendation, so the executive can choose rather than design
   - decisions needed, each with a decide-by date
   - at most three bullets of progress
4. **Write the partner-org update:** what shipped, what dates changed, what partners need to plan around, and upcoming asks of them.
5. **Write the working-team update:** changes to the plan, new decisions and why, risks the team should watch, and next milestones with owners.
6. **Check consistency.** The color must agree with the risk register and the decision log. If a risk is past its resolve-by date, the program is not green.

## Output Contract

Return:

- status color with a one-line justification
- executive update: headline, business impact (if yellow or red), options with recommendation, decisions needed with dates, key progress
- partner-org update: changes and upcoming asks
- working-team update: plan changes, decisions, watch items, next milestones
- consistency check: register and decision log agree with the color (yes or no, with discrepancies)

## Hard Boundaries

- Do not mark green without evidence.
- Do not report a yellow or red without either a mitigation in progress or a decision requested.
- Do not bury a slip in the progress section.
- Do not include customer names, individual performance, or sensitive incident detail in broadly distributed updates.

## Sequencing

Run every cycle inside `tpm-run`. Use `templates/weekly-status.md` for the layout.
