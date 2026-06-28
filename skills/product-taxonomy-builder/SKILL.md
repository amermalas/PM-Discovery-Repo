---
name: product-taxonomy-builder
description: Use when a PM wants to build their own product taxonomy, capability map, workflow map, persona map, lifecycle stages, or glossary from product docs, onboarding material, support docs, release notes, sales decks, or internal notes. Produces a structured taxonomy that belongs to the user's company, not a copied vendor taxonomy.
---

# Product Taxonomy Builder

Use this skill to help a team build its own product brain.

The taxonomy should describe how the product works, what users do, and how feedback should be tagged. It should be grounded in the user's own sources.

## Inputs

- product docs
- support or enablement docs
- onboarding material
- release notes
- product walkthrough notes
- PM-provided product areas or modules

## Workflow

1. List candidate product areas.
2. Identify capabilities under each area.
3. Identify workflow stages and user actions.
4. Identify personas, roles, or user types.
5. Identify lifecycle stages if relevant.
6. Extract glossary terms.
7. Mark source support for each taxonomy item.
8. Flag ambiguous or overlapping terms.
9. Produce a taxonomy in a structured format.

## Output Contract

Return:

- product areas
- capabilities
- workflows
- user roles or personas
- lifecycle stages
- glossary
- aliases and ambiguous terms
- source references
- open taxonomy questions

Prefer YAML or tables that can later be used for tagging evidence.

For each taxonomy row, include:

- stable id
- label
- parent area, if any
- type: product_area, capability, workflow, persona, lifecycle_stage, glossary_term, or alias
- description
- source ids or source references
- source support: direct, inferred, weak, or unknown
- confidence: high, medium, low
- review status: draft, needs_review, accepted, rejected
- open questions

## Hard Boundaries

- Do not invent product areas without marking them as inferred.
- Do not copy proprietary taxonomy from another company.
- Do not treat a taxonomy as stable until reviewed by the PM or product expert.
- Do not merge customer painpoints into taxonomy; keep taxonomy as product context.
- Do not present the first taxonomy draft as final. Row-level normalization and PM review are required before using it as a durable tagging system.
