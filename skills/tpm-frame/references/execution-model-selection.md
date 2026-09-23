# Execution Model Selection

Pick the execution model from the program's conditions, not from habit. Lead each answer with the one-line verdict, then the reasons.

## Five tests

| Test | Points toward iterative (agile) | Points toward plan-driven (milestone/waterfall) |
|---|---|---|
| Requirement clarity | End state unclear; learning expected | Requirements known and stable |
| Product owner availability | A decider is actually available every iteration | Decisions come in batches through formal review |
| Team size and spread | One to a few co-located or overlapping teams | Many teams across time zones; heavy integration |
| Cost of failure | A bad iteration is cheap to undo | Failure is costly or regulated (safety, finance, health) |
| Timeline rigidity | Date can move with learning | Hard external or regulatory date |

## Default: hybrid

Most real programs mix both. Use iterations inside teams for execution, and milestone gates at the program level for governance, cross-team integration, and executive visibility. Close the decision by answering: **where does this program need predictability, and where does it need adaptability?**

## Preconditions for iteration to work

Iteration only helps when the team actually has:

1. uncertain requirements that iteration can resolve
2. a dedicated product owner who is available
3. a collaborative culture that tolerates small failures
4. a habit of changing its own process after retros

If these do not hold, iteration becomes ceremony.

## Common failure modes to watch for

- Ceremonies with no outcome attached.
- Velocity turned into a target, so it stops measuring anything.
- No planning layer above the sprints, so cross-team dates are invisible to leadership.
- Requirement churn used as trial and error, which burns the team out.
- Architecture debt deferred sprint after sprint.
- Minimal documentation that makes onboarding and handoffs slow.

## AI and model-backed features

For features whose quality is probabilistic (LLM, ranking, classification), "done" is not binary. Add an evaluation threshold to the definition of done so an iteration cannot be accepted on passing unit tests alone. See `assistant-golden-evaluator` for a regression method and `launch-readiness-review` for release gates.
