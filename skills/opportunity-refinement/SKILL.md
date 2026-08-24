---
name: opportunity-refinement
description: Use when a PM has selected one product opportunity and needs to refine it into jobs to be done, MVP behavior, guardrails, non-goals, assumptions, risks, open questions, and a design/engineering handoff package. Generic public version that does not depend on private company sources.
---

# Opportunity Refinement

Use this skill after opportunity selection.

The goal is to make one opportunity clear enough for review, prototyping, or handoff. It is not to create a production implementation plan.

## Unit-of-analysis interrogation

Before defining behaviors, ask two questions about whatever the opportunity proposes to measure or improve:

1. **What is the unit being measured?**
2. **Does that unit contain the outcome anyone actually cares about?**

These are worth asking explicitly because a mismatch is invisible from inside the existing metric. A system can score perfectly on every unit it records while failing at the thing the user came to do, and no amount of improvement at the recorded unit will surface it. The recorded unit is not wrong; it is too small to hold the outcome.

The diagnostic is to find a case where **every recorded unit succeeds and the user still fails.** If such a case exists and is common, the unit is the problem, and the opportunity is to establish a larger unit rather than to improve performance within the small one.

Then ask what has to exist before the larger unit can be recorded at all. A unit that nothing in the system represents cannot be measured by better analysis; something has to be built to make it expressible. That prerequisite is usually the real opportunity, and it is usually mistaken for a reporting project.

Where the unit is already correct, say so and move on. This is a check, not a mandate to reframe.

## Inputs

- selected opportunity
- linked validated painpoints
- supporting evidence
- target users
- constraints
- PM judgment notes

## Workflow

1. Freeze the selected opportunity.
2. Restate the problem and why now.
3. Run the unit-of-analysis interrogation and record the result.
4. Define target users and workflow moments.
5. Write detailed jobs to be done.
5. Define MVP behaviors.
6. Define guardrails and non-goals.
7. Capture assumptions, risks, and open questions.
8. Create a handoff package for design, engineering, and prototype planning.

## Output Contract

Return:

- opportunity summary
- problem statement
- unit currently measured
- unit that contains the outcome
- worked case where every recorded unit succeeds and the user still fails, or a statement that none was found
- prerequisite that must exist before the larger unit is expressible
- target users
- JTBD sections
- supporting evidence ids under each JTBD section
- MVP behavior list
- guardrails
- non-goals
- assumptions
- evidence gap notes
- open questions
- design review questions
- engineering review questions
- handoff notes
- prototype candidates

## Hard Boundaries

- Do not reopen broad opportunity discovery.
- Do not invent evidence.
- Do not blur MVP with later-phase ambition.
- Do not reframe the unit of analysis without a worked case showing the current unit hides a real failure.
- Do not imply prototype or handoff notes are production requirements.
