---
name: opportunity-selection
description: Use after painpoint validation when a PM needs to turn validated problems into candidate product opportunities, compare build-now versus later options, separate workflow hardening from AI opportunities, and select a primary opportunity plus follow-on candidate.
---

# Opportunity Selection

Use this skill when the problem space has been validated and the PM needs a recommendation posture.

This skill should convert evidence-backed painpoints into opportunity options. It should not brainstorm unconstrained ideas.

## Inputs

- validated painpoints
- product taxonomy or capability map
- strategy criteria
- constraints
- optional feasibility notes
- optional AI-fit criteria

## Workflow

1. Group validated painpoints into opportunity themes.
2. Identify non-solution prerequisites and workflow hardening needs.
3. Generate candidate opportunities.
4. Score each opportunity for user value, evidence strength, feasibility, strategic fit, and risk.
5. Assess whether AI is central, helpful, or premature.
6. Choose:
   - primary selected opportunity
   - follow-on candidate
   - not-now opportunities
7. Explain the tradeoff.
8. Write the below-the-line record: every option considered and not selected, with the reason it lost.

## Output Contract

Return:

- opportunity name
- linked painpoints
- user value
- evidence strength
- feasibility
- AI posture:
  - non-AI hardening
  - AI-assisted
  - AI-premature
  - not AI-relevant
- recommendation posture:
  - build now
  - refine next
  - learn more
  - defer
- primary selected opportunity
- follow-on candidate
- below-the-line record, produced by default and not on request:
  - option considered
  - what it would have addressed
  - why it was not selected: evidence, sequencing, ownership, cost, or scope
  - what would change the answer
- capabilities deliberately conceded rather than built
- rationale
- risks
- open questions

## Hard Boundaries

- Do not select an opportunity without linking to validated painpoints.
- Do not call something an AI opportunity just because AI can be inserted.
- Do not skip PM judgment; surface tradeoffs for the PM to decide.
- Do not write a full product brief here; hand off to `opportunity-refinement`.
- Do not omit the below-the-line record. Senior reviewers reliably ask what was considered and rejected; reconstructing it afterwards is guesswork, capturing it during selection is free.
- Do not populate the below-the-line record with strawmen. An option that was never plausible teaches the reader nothing and signals that the real alternatives went unexamined.
