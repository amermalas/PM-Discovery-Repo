---
name: tpm-land
description: Use for Stage 5 (LAND) of the 5-stage delivery loop, getting a built feature safely into users' hands and proving it worked. Runs a go/no-go launch readiness review, plans a staged rollout with rollback, confirms support and documentation readiness, measures the result against the charter's success metric, and runs a retrospective that feeds learning back into discovery. Trigger on "launch readiness", "go/no-go", "rollout plan", "are we ready to ship", "post-launch review", or "retro". For AI or model-backed features, adds evaluation gates.
---

# TPM Land: Stage 5, ship safely and prove it worked

Part of a 5-stage delivery loop (FRAME -> PLAN -> ALIGN -> RUN -> LAND). A program is not done when the code merges. It is done when the feature is in users' hands, the organization can support it, and the success metric has been measured against the baseline from the charter.

This stage closes both loops. What was learned in delivery goes back to discovery (`pm-sense`, `pm-listen`, `pm-ground`) so the next bet starts smarter.

## Objective

A launch decision made against explicit criteria, a rollout that can be reversed, and a measured result with lessons routed to where they will be used.

## Required inputs

- The charter's success metric and baseline (`tpm-frame`, `success-metric-tree`).
- The plan, risk register, and decision log (`tpm-plan`, `tpm-run`).
- Test results, and for AI features, evaluation results against a golden set (`assistant-golden-evaluator`).
- Support, documentation, and operations readiness status.

## What to do

1. **Run the launch readiness review.** Route to `launch-readiness-review`. Every criterion is met, waived by a named owner with a reason, or blocking. A waiver is a decision; log it.
2. **Plan a staged rollout.** Internal users, then a small cohort, then wider. Define the promotion criteria between stages and the metric that would halt it. Name the rollback mechanism (feature flag, config revert, redeploy) and who can pull it.
3. **Confirm the organization is ready.** Support has been trained and has a runbook. Documentation is published or scheduled. On-call and monitoring are owned after launch, not just during build. Sales, marketing, and customer-facing teams know the date and the known limitations.
4. **Stand up launch-day operations** proportionate to risk: a named launch lead, a live channel, a decision owner for rollback, and a check-in schedule for the first hours or days.
5. **Measure against the baseline.** After the agreed interval, compare the success metric and its guardrails to the charter baseline. Report adoption, system health, and operational health separately.
6. **Run the retrospective.** Route to `program-retrospective`. Cover process, people, and technical lessons. For each lesson, name the owner and the place it will change something.
7. **Feed learning back.** Validated user insight goes to `pm-listen`. Changes to actual product behavior go to `pm-ground` and `task-card-knowledge-builder`. Market or competitive learning goes to `pm-sense`. Decide whether to expand, iterate, or stop.

## Outputs

- A go/no-go decision with every criterion's state and any waivers with owners.
- A rollout plan with stages, promotion criteria, halt metric, and rollback owner.
- A post-launch results report against the baseline.
- A retrospective with owned actions.
- Routed learnings back into the discovery loop, and an expand/iterate/stop recommendation.

## Review gate

The launch decision names who made it and on what evidence. The results report compares against the charter's baseline, not against a number chosen after the fact.

## Copy-ready prompt

> Using the charter, the decision log, test and evaluation results, and readiness status from support, docs, and operations, run a go/no-go review. List each criterion as met, waived (with owner and reason), or blocking. Propose a staged rollout with promotion criteria, a halt metric, and a named rollback owner. After launch, compare the success metric and guardrails to the charter baseline and draft a retrospective with owned actions. Do not mark a criterion met without evidence in the inputs.

## Related repo resources

- Before: `tpm-run`.
- Detail: `launch-readiness-review`, `success-metric-tree`, `program-retrospective`, `assistant-golden-evaluator`, `templates/launch-readiness-checklist.md`, `templates/program-retrospective.md`.
- Feeds back to: `pm-sense`, `pm-listen`, `pm-ground`.

## Guardrails

- Do not launch without a way to turn it off.
- Do not move the success threshold after seeing the result. If the metric was wrong, say so and set a new one for the next iteration.
- Do not treat a quiet launch as a successful one. Absence of complaints is not evidence of adoption.
