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

## Troubleshooting

**Test an unchanged control before bisecting your own change.** When a prototype renders blank, hangs, or fails after an edit, the instinct is to disassemble the edit. Open a known-good artifact that you did not touch first. If it fails too, the problem is the runtime, the viewer, or the environment, and every minute spent bisecting your own work is wasted. This check costs seconds and routinely saves an hour of self-directed debugging on a change that was fine.

Order of elimination:

1. an unchanged control artifact
2. the same artifact in a different viewer or browser session
3. the change itself, bisected
4. structural verification: tag balance, brace balance, syntax check

**Merging two independently-styled pages.** When combining a prototype into a longer document, scope the incoming page's styles under a single container class rather than merging the two stylesheets. Redefine the incoming page's variables on `.container-class` instead of `:root`, prefix every incoming rule, and verify afterwards that no incoming selector leaked to the top level. This keeps both designs intact and makes the merge reversible.

Verify a merged single-file artifact structurally before publishing: open and close tag counts match, CSS brace delta is zero, scripts pass a syntax check, and the scoped rule count matches the number of rules that came in.

## Hard Boundaries

- Do not use internal brand assets or proprietary UI tokens for a public template.
- Do not fetch or persist real customer data.
- Do not overbuild infrastructure.
- Do not create production claims.
- Do not skip verification if a runnable app exists.
- Do not diagnose a failure as your own before testing an unchanged control.
- Do not report a suspected defect in your own work as confirmed until the control test has ruled out the environment.
