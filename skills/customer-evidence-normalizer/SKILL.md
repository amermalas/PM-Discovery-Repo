---
name: customer-evidence-normalizer
description: Use when a PM has messy customer feedback, interview notes, support tickets, surveys, sales notes, or field observations and needs to turn them into structured evidence items with source references, snippets, user roles, product areas, themes, painpoint candidates, and confidence notes.
---

# Customer Evidence Normalizer

Use this skill to convert messy feedback into evidence items that can be validated later.

The goal is structure, not recommendation. Recommendations come after validation.

## Inputs

- customer or user feedback
- interview notes
- support tickets
- survey responses
- field notes
- source cards
- optional product taxonomy

## Workflow

1. Preserve source identity.
2. Split the material into atomic evidence items.
3. For each item, capture who, what, source, and context.
4. Tag product area or workflow if a taxonomy exists.
5. Extract painpoint candidates without overstating them.
6. Capture useful short snippets only when safe.
7. Mark confidence and ambiguity.
8. Produce a normalized evidence table.

## Output Contract

Return evidence rows with:

- evidence id
- source id
- source family
- source location or citation placeholder
- user/account/persona placeholder
- product area
- workflow stage
- evidence type
- short snippet or paraphrase
- public-safe paraphrase
- source quote allowed: yes, no, or unknown
- theme candidate
- painpoint candidate
- sentiment or severity
- evidence strength
- confidence
- needs review: yes or no
- notes

## Hard Boundaries

- Do not rank priorities here.
- Do not merge multiple issues into one evidence item unless clearly the same point.
- Do not include personal data or real customer names in public examples.
- Do not treat one strong quote as broad validation.
