---
name: tradeoff-decision-brief
description: Use when a program's plan no longer fits its constraints and someone has to choose what gives. Frames the decision around the four knobs (date, scope, resources, quality), lays out two or three options with consequences, prices the cost of yes for new requests, recommends one, and records the decision. Trigger on "half the time", "half the team", "leadership added a must-have", "a dependency slipped", "new requirement vs bugs", or "we can't do all of it".
---

# Tradeoff Decision Brief

When a plan breaks, the TPM's job is to make the tradeoff visible and get the right person to decide it. Not to absorb it quietly, and not to decide it alone.

The recurring failure: resources or time get cut, while scope, date, and cost are all declared "fixed." Something still gives, and it is usually quality and risk, discovered later by users. The brief exists to name that before it happens.

## Inputs

- the charter's fixed variable and decider
- the baselined plan and critical path
- what changed (a cut, a slip, a new request, an incident)
- estimates for the affected work, with their source

## The four knobs

| Knob | What flexing it looks like |
|---|---|
| Date | Move the launch, or split it into phased releases |
| Scope | Cut, defer, or simplify features; ship an MVP version first |
| Resources | Add or borrow people, buy a vendor or service, reuse a component |
| Quality | Launch with known limitations, a narrower rollout, or tighter guardrails; never silently |

The knob fixed in the charter stays fixed unless the decider changes it. Ask explicitly whether quality is negotiable; the answer is usually no, which means one of the other three must move.

## Workflow

1. **State what changed and why, in one paragraph.** Include the evidence.
2. **Test the constraint.** What exactly is fixed, and why? Often it is one launch moment or one must-have feature, not everything.
3. **Quantify the gap** using estimates and historical velocity, not opinion.
4. **Look for leverage before cutting:** reuse, parallelization, removing non-essential process, automation, borrowing from another team with a give-back.
5. **Write two or three options.** For each: which knobs move, by how much, what it costs, what it risks, and who it affects. Common shapes:
   - phased delivery (1.0, 1.1, 2.0) with the MVP approved first
   - descope to a ranked cut list agreed with the PM
   - add resources, with the ramp-up cost stated
   - ship on time with a controlled, time-bound risk (see `risk-register`)
6. **For new requests, price the cost of yes.** What slips, what it risks, and a cheaper alternative engineering can offer (a partial launch, a limited cohort, a manual workaround). Bring this to the decider instead of saying yes or no yourself.
7. **For "new requirement vs recurring bugs,"** say both sides aloud: "if we delay the bugs, X happens; if we delay the requirement, Y happens." Recurring bugs often share a root cause; one person on the root cause while others build is a common third option.
8. **Recommend one option** and say why. Separate reversible choices (decide fast) from irreversible ones (decide carefully).
9. **Name the decider and the decide-by date.** A decision needed "soon" is not scheduled.
10. **Record the outcome** in `templates/decision-log.md` and update the plan, register, and status.

## Output Contract

Return:

- what changed, with evidence
- the fixed knob and who fixed it
- the gap, quantified, with estimate sources
- leverage checked before cutting
- options (two or three), each with knobs moved, cost, risk, affected parties
- cost of yes and cheaper alternative, for new requests
- recommendation and rationale
- reversible or irreversible
- decider and decide-by date
- decision log entry (after the decision)

## Hard Boundaries

- Do not offer "the team will work harder" as an option.
- Do not present only one option. A single option is an announcement, not a decision.
- Do not flex the fixed knob without the decider.
- Do not hide a quality reduction inside a scope or date option. Name it.

## Sequencing

Called from `tpm-run` when a plan breaks, or from `program-recovery` during re-planning. Use the template at `templates/tradeoff-decision-brief.md`.
