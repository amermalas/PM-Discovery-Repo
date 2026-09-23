---
name: launch-readiness-review
description: Use before a feature ships to run a go/no-go review against explicit criteria. Checks functional and non-functional readiness, security, privacy, compliance and accessibility sign-offs, rollout and rollback, monitoring and on-call, support and documentation, and for AI or model-backed features, evaluation gates and action-safety controls. Each criterion ends as met, waived by a named owner, or blocking. Trigger on "go/no-go", "launch readiness", "are we ready to ship", or "rollout plan".
---

# Launch Readiness Review

A go/no-go decision is only as good as its criteria. This skill makes the criteria explicit, forces every one into a clear state, and makes sure the launch can be reversed.

## Inputs

- the charter, success metric tree, and decision log
- test results and open defects
- for AI or model-backed features: evaluation results against a golden set (see `assistant-golden-evaluator`)
- readiness status from support, documentation, operations, security, privacy, legal
- the open risk register, including accepted risks and their expiry dates

## Workflow

1. **Load the checklist** from `templates/launch-readiness-checklist.md`. Remove items that genuinely do not apply, and say why.
2. **Set each criterion's state:**
   - **Met:** with the evidence (link, test run, sign-off).
   - **Waived:** with a named owner, the reason, and the follow-up date. A waiver is a decision; log it.
   - **Blocking:** with the owner and what would unblock it.
3. **Check the rollout plan.** Stages (internal, small cohort, wider), promotion criteria between stages, the halt metric, the rollback mechanism, and the person authorized to pull it. A launch with no rollback path is blocking unless the decider explicitly waives it.
4. **Check operational ownership after launch.** Monitoring and alerting are live; on-call is named; runbooks exist. Build ownership ending at launch is a common gap.
5. **Check organizational readiness.** Support is trained and has a runbook; documentation and release notes are ready; customer-facing teams know the date and the known limitations.
6. **For AI or model-backed features, add:**
   - evaluation scores at or above the agreed threshold on the golden set, and no unreviewed regressions since the last passing run
   - a prompt, model, or retrieval change is treated as a deploy and has passed the same gate
   - actions tiered by reversibility: read-only, reversible writes, consequential writes within policy limits, and irreversible or high-value actions that always require human approval
   - policy limits enforced in code or configuration, not only in prompt instructions
   - mutating actions are idempotent, so a retry cannot apply an action twice
   - loop or cost budgets (steps, tokens, time, spend) with a defined behavior when a budget is hit
   - graceful handling of "no relevant information found," with escalation instead of a guessed answer
   - escalation triggers and a handoff that carries the context already gathered
   - traces retained so a bad outcome can be replayed
   - the honest success metric (resolution, not deflection) is instrumented
7. **Check accepted risks.** Any accepted risk expiring before or shortly after launch needs a decision now.
8. **Make the call.** The decider states go, go with conditions, or no-go, and the decision is logged with the evidence.

## Output Contract

Return:

- criteria table: area, criterion, state (met, waived, blocking), evidence or reason, owner, follow-up date
- rollout plan: stages, promotion criteria, halt metric, rollback mechanism, rollback owner
- post-launch ownership: monitoring, on-call, runbooks
- AI-specific checks (if applicable), each with state and evidence
- accepted risks reviewed
- recommendation: go, go with conditions, or no-go, and the decider
- decision log entry

## Hard Boundaries

- Do not mark a criterion met without evidence.
- Do not accept a waiver from someone who does not own the area (for example, a program sponsor waiving a privacy review).
- Do not approve a launch with no way to turn it off unless the decider waives that explicitly and in writing.
- Do not treat a passing golden-set score as proof of production behavior; plan online monitoring too.

## Sequencing

Run inside `tpm-land`. Uses results from `assistant-golden-evaluator` for AI features and from `risk-register` for accepted risks. After launch, hand off to `program-retrospective`.
