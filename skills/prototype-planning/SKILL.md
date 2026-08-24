---
name: prototype-planning
description: Use before building a PM prototype. Defines the prototype question, target reviewer, workflow moments, states, synthetic data plan, interaction assumptions, success criteria, non-goals, and PROTOTYPE.md contract so prototype code stays disposable.
---

# Prototype Planning

Use this skill before generating UI or code.

The goal is to decide what the prototype must prove. A prototype without a question becomes a demo, and a demo often hides weak product thinking.

## The one-variable discipline

The most common way a prototype cheats is to compare a good version against a strawman. It improves the thing being demonstrated, and so proves nothing, because the objection **"you just made it better"** is always available and always fatal.

Before building a comparison prototype, write a held-constant table and put it in `PROTOTYPE.md`:

| Held constant | Changed |
|---|---|
| the user | |
| the input, word for word | |
| the underlying system | |
| the output, word for word | |
| the outcome for that user | |
| | the one thing under test |

The strongest form of a comparison is: **the same system, failing in exactly the same way, with the difference under test layered on top.** If the "after" state produces a better output, you have confounded the demo and the reviewer cannot tell which change caused the improvement.

Stage additional changes as separate modes, one variable each, rather than bundling them. A three-mode prototype where each step isolates one change is far more persuasive than a two-mode prototype where everything moves at once.

State the variable in one sentence before building. If it cannot be stated in one sentence, it is more than one variable.

## Inputs

- selected or refined opportunity
- target user or reviewer
- workflow description
- evidence or product context
- constraints
- desired review outcome

## Workflow

1. Define the prototype question.
2. Define the one variable under test and write the held-constant table.
3. Identify the target reviewer and user role.
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
- the one variable under test, in a sentence
- held-constant table
- the objection the design makes unavailable
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
- Do not improve the thing under test between comparison modes. Same system, same failure, one added variable.
- Do not bundle several changes into one mode and describe it as a comparison.
- Do not use real customer data by default.
- Do not imply prototype architecture is production architecture.
- Do not hide mocked behavior.
