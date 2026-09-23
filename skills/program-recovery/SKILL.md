---
name: program-recovery
description: Use when a program is badly off plan and incremental fixes are no longer working. Diagnoses the variance (bad estimates, scope creep, dependency slips, team issues), re-baselines the remaining work bottom-up, takes descope, re-phase, fund, or stop options to the sponsor, and resets controls so trust can be rebuilt. Trigger on "most of the budget is spent and a fraction is done", "this program keeps changing", "restructure this program", "take over a troubled program", or "turnaround".
---

# Program Recovery

A troubled program usually does not need more effort. It needs an honest diagnosis, a plan people believe, and a first win on that plan. Adding people reflexively to a late program tends to make it later.

## Inputs

- the original charter and baseline (if they exist)
- actuals: time and budget spent, scope completed, current forecast
- the change history: what was added, removed, or re-scoped, and when
- the risk register and decision log (if they exist)
- conversations with the working teams

## Workflow

1. **Pause new commitments.** Briefly freeze scope additions while you diagnose. Do not add people yet.
2. **Measure the variance.** Compare planned against actual for schedule and cost. Express how far off the program is in the same units the sponsor uses.
3. **Diagnose the cause.** Each has a different fix:
   - **Estimates were wrong:** re-estimate bottom-up with the team.
   - **Scope crept:** list every addition since baseline and who approved it.
   - **Dependencies slipped:** identify which partner and why, and whether the commitment was ever real.
   - **Team issues:** capacity, skills, turnover, unclear ownership, morale.
   - **The goal changed:** the program may be solving a problem nobody has anymore.
4. **Re-confirm the goal and the decider** with the sponsor. A troubled program often has lost one or both.
5. **Re-baseline the remaining work** bottom-up with the people doing it, using `tpm-plan` and `delivery-decomposition`.
6. **Take options to the sponsor** (using `tradeoff-decision-brief`):
   - descope to what matters most
   - re-phase into smaller releases that deliver value sooner
   - fund the gap, with the ramp-up cost stated
   - stop the program; this is a legitimate recommendation when the goal no longer justifies the cost
7. **Submit the change formally** and get the new baseline approved.
8. **Reset controls:** change control with a cost attached to every change, milestone reviews, a visible dashboard, and a reset communication cadence.
9. **Plan an early win.** Ship one milestone on the new plan quickly to rebuild trust.
10. **Fix the system that produced the problem,** not just this instance, and record it for the retrospective.

## Output Contract

Return:

- variance summary: planned vs actual, schedule and cost
- diagnosis: cause categories with evidence
- goal and decider, re-confirmed or flagged missing
- re-baselined plan for remaining work, with estimate sources
- options to the sponsor with a recommendation (including whether to stop)
- reset controls: change control, cadence, dashboard
- early-win milestone and date
- systemic fixes

## Hard Boundaries

- Do not add people as the first move.
- Do not re-baseline without the working teams' estimates.
- Do not rule out stopping the program.
- Do not assign blame to individuals in the diagnosis; describe causes and conditions.

## Sequencing

Entered from `tpm-run` when incremental fixes are not working, or directly when taking over a program. Returns to `tpm-run` once the new baseline is approved.
