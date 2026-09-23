---
name: tpm-frame
description: Use for Stage 1 (FRAME) of the 5-stage delivery loop, when a committed feature or top bet needs to become a program. Aligns the goal with a sponsor, sets a success metric and baseline, names the program type and the fixed variable, picks an execution model, and produces a program charter. Trigger on "kick off a program for X", "initiate this program", "write the charter", "we committed to this bet, now what", or "how do we get this shipped". Not for deciding whether the bet is worth doing; that is the discovery loop's job (pm-sense through pm-commit).
---

# TPM Frame: Stage 1, turn a committed bet into a program

Part of a 5-stage delivery loop (FRAME -> PLAN -> ALIGN -> RUN -> LAND) that picks up where the discovery loop (SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT) ends. Discovery answers "what should we build and why." Delivery answers "how does it actually get shipped, by whom, by when, and how will we know it worked."

This stage is short and decisive. Its job is to get four things agreed before anyone plans in detail: the goal, the metric, what is fixed, and who decides.

## Objective

Produce a program charter a sponsor can sign, so every later tradeoff has something to be measured against.

## Required inputs

- The committed epic, stories, and requirements brief from `pm-commit`, or an opportunity brief from `opportunity-refinement`.
- The evidence and decision log behind the bet, so the "why" survives the handoff.
- A named sponsor, or the fact that there is none (that is itself a finding).
- Any known hard dates, budgets, or headcount limits.

## What to do

1. **Confirm the problem with the sponsor.** Restate the problem, who has it, and why it matters now, using the discovery evidence. If the sponsor's version of the problem differs from the evidence, stop and reconcile before going further.
2. **Set the success metric and its baseline.** One outcome metric, even if aspirational, plus the baseline measured today. If the baseline cannot be measured yet, instrumenting it is the first milestone, not an afterthought. Route to `success-metric-tree` for the full tree.
3. **Name the program type.** State which one it is:
   - **Fixed box:** scope and date are defined; the job is execution.
   - **Bootstrap:** the goal is clear but the end state is not; the job is time-boxed exploration, then committing resources milestone by milestone.
   - **Turnaround:** an existing program is off plan. Route to `program-recovery` instead.
4. **Agree the fixed variable.** Of the four knobs (date, scope, resources, quality), name which one is fixed, who fixed it, and why. Quality is a knob too: if the other three are all "fixed," quality and risk are what will quietly give. Write that down now, while nobody is under pressure.
5. **Pick the execution model** using `references/execution-model-selection.md`. Default to a hybrid: iterative delivery inside the teams, milestone gates for program governance.
6. **Surface the long-lead items on day one.** Security, privacy, legal, accessibility, compliance reviews, vendor contracts, and procurement. These have the longest lead times and cause the least predictable launch delays when they start late.
7. **Name the decider.** One person or forum who breaks ties on scope and date. Name who is informed but does not decide.
8. **Draft the charter** with `templates/program-charter.md`. The in/out-of-scope list and the decision owner are the two lines that prevent most later fights; do not leave either blank.

## Outputs

- A program charter (sponsor, problem, goal, success metric and baseline, program type, fixed variable, execution model, scope in and out, decider, long-lead reviews, known constraints, open questions).
- A list of assumptions carried over from discovery, each labelled Confirmed, Inference, or Open question.
- A handoff to `tpm-plan`.

## Review gate

The sponsor has agreed the goal, the metric, the fixed variable, and the decider, in writing. If any of the four is missing, the program is not framed; do not start detailed planning.

## Copy-ready prompt

> Using the committed epic, requirements brief, and decision log, draft a program charter. State the problem in one paragraph with its evidence, one success metric with today's baseline, the program type (fixed box or bootstrap), which of date/scope/resources/quality is fixed and who fixed it, the execution model, scope in and out, the single decider, and the security/privacy/legal/vendor reviews that must start this week. Mark anything not confirmed by the sponsor as an open question. Do not invent dates, budgets, or headcount.

## Related repo resources

- Before: `pm-commit`, `opportunity-refinement`.
- Detail: `success-metric-tree`, `references/execution-model-selection.md`, `templates/program-charter.md`.
- Next: `tpm-plan`.

## Guardrails

- Do not invent a sponsor, a date, a budget, or a baseline. Say it is missing.
- Do not let "everything is fixed" stand. Name the knob that will give.
- Do not re-open the discovery decision here unless the sponsor's problem contradicts the evidence; if it does, send it back to `pm-ground` rather than silently re-scoping.
