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
- why the secondary candidates were not selected now
- rationale
- risks
- open questions

## Hard Boundaries

- Do not select an opportunity without linking to validated painpoints.
- Do not call something an AI opportunity just because AI can be inserted.
- Do not skip PM judgment; surface tradeoffs for the PM to decide.
- Do not write a full product brief here; hand off to `opportunity-refinement`.
