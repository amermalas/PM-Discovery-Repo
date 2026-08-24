---
name: painpoint-validation
description: Use when a PM has painpoint candidates and structured evidence and needs to validate which problems are actually supported. Scores evidence strength, source breadth, severity, recurrence, product fit, open questions, and confidence before any opportunity selection.
---

# Painpoint Validation

Use this skill to test whether a painpoint survives scrutiny.

The useful question is not "what should we build?" It is "which problem claims are supported by the evidence and worth considering?"

## Inputs

- painpoint candidates
- normalized evidence rows
- source cards
- optional product taxonomy
- optional business or strategy criteria

## Workflow

1. Normalize duplicate or overlapping painpoint claims.
2. Attach supporting evidence rows.
3. Count source breadth and recurrence.
4. Assess severity and workflow impact.
5. Identify product-area fit or ambiguity.
6. Separate validated painpoints from weak signals.
7. Flag contradictions and missing evidence.
8. Run the substitution test from `generic-claim-falsification` on every validated painpoint before handing off.
9. Produce a validation table and narrative summary.

## Output Contract

Return:

- normalized painpoint
- description
- supporting evidence ids
- evidence count
- source families
- source family count
- source breadth
- severity
- recurrence
- confidence
- representative citations
- business impact proxy, if available
- product/workflow area
- validation status:
  - validated
  - promising but under-evidenced
  - unclear
  - not supported
- specificity grade from the substitution test: `specific`, `conditional`, or `generic`
- open questions

## Hard Boundaries

- Do not select solutions in this skill.
- Do not inflate confidence because the writing is compelling.
- Do not treat AI-generated summaries as evidence unless they link back to source rows.
- Do not hide conflicting evidence.
- Do not hand a `generic` painpoint to `opportunity-selection`. A painpoint that stays true when the target organization is swapped for an unrelated one is a category description, however well evidenced, and committing to a direction on it is the expensive mistake this chain exists to prevent.
