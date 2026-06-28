---
name: disposable-prototype-builder
description: Use when a PM wants to build a neutral, public-safe, throwaway product prototype from a refined opportunity and prototype plan. Creates synthetic fixtures, UI scaffolding, interaction states, verification notes, and handoff boundaries without presenting the code as production-ready.
---

# Disposable Prototype Builder

Use this skill to build a prototype for product learning.

The prototype should help humans inspect a workflow. It should not become production code by accident.

## Inputs

- prototype plan
- refined opportunity
- synthetic data plan
- neutral UI preference or existing public template
- target runtime, if provided

## Workflow

1. Confirm prototype-only status.
2. Generate or update synthetic fixtures.
3. Build the smallest useful workflow surface.
4. Include core states and interactions.
5. Use neutral styling unless a safe public design system is provided.
6. Add handoff notes explaining what is mocked.
7. Run relevant build or visual checks when available.

## Output Contract

Return:

- prototype files or change summary
- synthetic fixture summary
- screens and interactions implemented
- states implemented
- verification results
- known limitations
- production non-goals
- next review questions

## Hard Boundaries

- Do not use internal brand assets or proprietary UI tokens for a public template.
- Do not fetch or persist real customer data.
- Do not overbuild infrastructure.
- Do not create production claims.
- Do not skip verification if a runnable app exists.
