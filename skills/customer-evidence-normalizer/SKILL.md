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
7. Capture absence signals: what the target's own artifacts do not say, where you looked, and what you searched for.
8. Mark confidence and ambiguity.
9. Produce a normalized evidence table.

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
- evidence basis: `presence` or `absence`
- for absence rows: what was searched, which artifacts, and what was expected but not found
- needs review: yes or no
- notes

## Hard Boundaries

- Do not rank priorities here.
- Do not merge multiple issues into one evidence item unless clearly the same point.
- Do not include personal data or real customer names in public examples.
- Do not treat one strong quote as broad validation.
- Do not let an absence row become load-bearing. Absence is admissible and often the most target-specific material available, but it is a **signal, not a finding**, and must carry that label into every downstream artifact. Documents and systems are silent for many reasons, most of them boring.
- Do not record an absence without recording the search that established it. "It is not mentioned" is only evidence if you can say where you looked.
