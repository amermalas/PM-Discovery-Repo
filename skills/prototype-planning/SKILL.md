---
name: prototype-planning
description: Use before building a PM prototype. Defines the prototype question, target reviewer, workflow moments, states, synthetic data plan, interaction assumptions, success criteria, non-goals, and PROTOTYPE.md contract so prototype code stays disposable.
---

# Prototype Planning

Use this skill before generating UI or code.

The goal is to decide what the prototype must prove. A prototype without a question becomes a demo, and a demo often hides weak product thinking.

## Inputs

- selected or refined opportunity
- target user or reviewer
- workflow description
- evidence or product context
- constraints
- desired review outcome

## Workflow

1. Define the prototype question.
2. Identify the target reviewer and user role.
3. Map the workflow stages.
4. Define screen purposes and primary actions.
5. Define important states: empty, loading, ready, warning, blocked, success, error.
6. Create a synthetic data plan.
7. List what is mocked.
8. List production non-goals.
9. Produce `PROTOTYPE.md` content.

## Output Contract

Return:

- prototype question
- target reviewer
- user role
- taste criteria
- workflow stages
- screens
- key actions
- states
- synthetic fixture plan
- mocked behavior
- non-goals
- verification checklist
- `PROTOTYPE.md`

## Hard Boundaries

- Do not build UI before defining the prototype question.
- Do not use real customer data by default.
- Do not imply prototype architecture is production architecture.
- Do not hide mocked behavior.
