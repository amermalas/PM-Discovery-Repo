---
name: risk-register
description: Use to identify, score, own, and track program risks over time. Runs a pre-mortem, scores risks as probability times impact, assigns an owner, trigger, response, and resolve-by date to each, converts overdue risks into issues, and writes a calculated-risk decision record when leadership chooses to accept a risk. Use when starting a plan, during weekly program review, or when someone proposes shipping with a known risk.
---

# Risk Register

Risk management is a running activity, not a document written once at kickoff. The goal is **calculated risk**: knowing which risks are being taken, who accepted them, until when, and what would make you stop. The goal is not to avoid all risk; a team that avoids every risk ships nothing.

## Inputs

- the charter, plan, and dependency map
- design review notes
- the current register, if one exists
- this period's signals (slips, incidents, staffing changes, new dependencies)

## Workflow

### Identify

1. **Pre-mortem.** "It is [target date] and this program failed. What happened?" Collect answers from each workstream independently before discussing.
2. **Walk the usual sources.** The dependency map's cross-team edges; non-functional requirements; security, privacy, legal, and compliance reviews; vendors and procurement; staffing and single points of knowledge; data availability and quality; for AI features, evaluation coverage and failure modes.

### Score and own

3. **Score each risk** on probability (1-5) and impact (1-5). Score = probability x impact. State what impact means for this program (date, scope, cost, quality, customer trust, compliance) rather than using an abstract scale.
4. **Assign an owner, a trigger, and a resolve-by date.** The owner is a person, not a team. The trigger is the early-warning signal that the risk is materializing.
5. **Choose a response:** avoid, reduce, transfer, or accept. A good mitigation lowers probability **and** limits impact. Write what the mitigation actually is and who is doing it.

### Track

6. **Review on a cadence** (weekly for active programs). Re-score changed risks. Close resolved ones with a note.
7. **Convert overdue risks to issues.** A risk not resolved by its resolve-by date becomes an issue, with a written explanation of why and a new plan. Run `python scripts/risk_register.py <register.csv> --today YYYY-MM-DD` to rank risks and flag overdue ones.
8. **Share risks with affected partners.** Telling a cross-functional partner early is itself a mitigation.

### Accept a risk deliberately

9. When the program chooses to ship with a known risk, write a **calculated-risk decision record**:
   - the risk, and the options considered (for example: fix first and slip, descope, or ship with a controlled mitigation)
   - the exposure, quantified as minimum, likely, and maximum where possible
   - the controls: detection, monitoring, manual handling, rollback, kill criteria
   - who accepted it, and the date the acceptance expires
   - the permanent fix and when it lands
   Accepting a risk that touches safety, security, privacy, or data integrity needs the relevant owner's explicit sign-off, not only the program sponsor's.

## Output Contract

Return, per risk:

- risk id, description, category (scope, schedule, cost, quality, compliance, security, dependency, staffing)
- probability, impact, score
- owner (a person), trigger, response type, mitigation
- resolve-by date, status (open, mitigating, closed, issue)
- effect on scope, date, or cost if it materializes

And for the register as a whole:

- top risks by score
- overdue risks converted to issues, each with explanation
- calculated-risk decision records, if any
- risks shared with partners this period

## Hard Boundaries

- Do not assign a risk to a team without a named person.
- Do not treat a quality shortcut as a calculated risk unless the quality guardrails are written down.
- Do not let an accepted risk stay accepted forever. Every acceptance has an expiry.
- Do not score risks to make the status look green. The score is for decisions, not for reporting.

## Sequencing

Seed in `tpm-plan`. Review in every `tpm-run` cycle. Feed the top risks into `program-status-report`. Check open accepted risks in `launch-readiness-review`.
