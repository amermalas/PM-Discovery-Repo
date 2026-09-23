---
name: tpm-plan
description: Use for Stage 2 (PLAN) of the 5-stage delivery loop, turning a chartered program into a delivery plan. Decomposes the work into team-owned workstreams, names the interface contracts between teams, maps cross-team dependencies and the critical path, sets milestones that end in demos, checks staffing against estimates, and seeds the risk register with a pre-mortem. Trigger on "build the program plan", "who builds what", "what's the critical path", "break this into workstreams", "delivery plan for X", or "4-month plan". Requires a charter from tpm-frame.
---

# TPM Plan: Stage 2, decompose the work and find the critical path

Part of a 5-stage delivery loop (FRAME -> PLAN -> ALIGN -> RUN -> LAND). This stage turns the charter into a plan that teams can commit to and that leadership can read.

The most useful thing a plan does is show **which team is waiting on which other team, and what they are waiting for.** A plan that lists tasks without that is a to-do list.

## Objective

A baselined delivery plan: workstreams with owners, agreed interfaces between teams, milestones, a critical path, a staffing check, and a first risk register.

## Required inputs

- The signed charter from `tpm-frame` (goal, metric, fixed variable, scope in and out, decider).
- The epic and stories from `pm-commit`, including non-functional requirements.
- Architecture or design notes, if engineering has them. If not, the first milestone may be a design review.
- Team rosters and any known availability constraints (freeze windows, holidays, competing launches).

## What to do

1. **Walk the program-strategy checklist** in `references/program-strategy-checklist.md` and pick the aspects that dominate this program. Do not fill in all of them for the sake of it.
2. **Decompose by team, not by component.** Route to `delivery-decomposition`. For each component, name the owning team. Then name the **interface contract** between teams (API shape, event schema, data contract, service-level expectation). Agreeing contracts early is what lets teams build in parallel instead of in sequence.
3. **Run a design review per contributing team.** This is where most risks are found: scale assumptions, security, deprecated dependencies, single points of failure, regional or market expansion. Aim to surface most risks and dependencies here rather than during execution.
4. **Check for reuse before building.** Existing components, prior patterns, a platform another team already runs. Name what you checked.
5. **Estimate with the people doing the work,** then sanity-check against historical velocity or a comparable past project. Where the two disagree, say so rather than averaging.
6. **Map dependencies and compute the critical path.** Use `templates/dependency-map.csv` and `scripts/critical_path.py`. Put buffer on the critical path, not spread evenly. Color or flag cross-team edges; those are where slips cascade.
7. **Set milestones that end in a demo, not a document.** Front-load the milestone that retires the biggest unknown (a walking skeleton or a prototype against the real dependency). For a fixed date, work backwards and deliver value in increments along the way, not in one drop at the end.
8. **Check staffing against the plan.** Headcount and skills per workstream, including the roles that are often forgotten: design, analytics, documentation, support readiness, on-call ownership after launch.
9. **Run a pre-mortem and seed the risk register.** "It is three months from now and this failed. Why?" Route to `risk-register`.
10. **Get the plan reviewed with each workstream owner, then baseline it.** After baseline, changes go through change control in `tpm-run`.

## Outputs

- Workstream and ownership map with interface contracts (from `delivery-decomposition`).
- Dependency map, critical path, and milestone plan with buffer placement stated.
- Staffing check, including non-engineering roles.
- Risk register seeded from the pre-mortem and design reviews.
- A baselined plan with the date it was baselined.

## Review gate

Every workstream owner has seen the plan and agreed their milestones and interface commitments. The critical path is named out loud. Every risk has an owner. If a workstream has no owner, that is the first risk.

## Copy-ready prompt

> Using the program charter and the epic/stories, produce a delivery plan. Decompose the work by owning team, name every interface contract between teams, list cross-team dependencies as rows (task, owner team, duration estimate, depends-on), identify the critical path, propose milestones that each end in a demo, check staffing including design/analytics/docs/support, and run a pre-mortem to seed a risk register. Mark every estimate as team-provided or inferred. Do not invent team names, headcount, or dates that are not in the inputs.

## Related repo resources

- Before: `tpm-frame`.
- Detail: `delivery-decomposition`, `risk-register`, `scripts/critical_path.py`, `templates/dependency-map.csv`, `templates/risk-register.csv`.
- Next: `tpm-align`.

## Guardrails

- Do not present an estimate as a commitment until the owning team has agreed it.
- Do not hide the critical path inside a long task list. Name it.
- Do not treat non-functional requirements (latency, scale, availability, security, privacy, accessibility) as later work. Late NFRs are the most common cause of unpredictable launch delays.
