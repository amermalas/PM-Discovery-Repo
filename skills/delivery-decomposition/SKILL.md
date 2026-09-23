---
name: delivery-decomposition
description: Use to translate a feature's design or epic into a team-level delivery structure. Maps each component to an owning team, names the interface contracts between teams, builds a cross-team dependency map, computes the critical path, and proposes phasing that retires the biggest unknown first. Use when a plan lists components but not who is waiting on whom, or when a system design needs to become a delivery plan.
---

# Delivery Decomposition

A system design describes components. A delivery plan describes **teams, the contracts between them, and the order they unblock each other.** This skill does that translation.

The critical path through a program usually runs through people and agreements, not through services. A policy threshold that legal must approve, a schema a platform team must publish, a partner team that must reprioritize: these block more programs than hard engineering does.

## Inputs

- the epic, stories, and non-functional requirements
- an architecture sketch or component list (if none exists, produce a first-cut one and label it inferred)
- the teams available and what each already owns
- the charter's fixed variable and target date, if any

## Workflow

1. **List components.** From the design or the stories. Include the non-obvious ones: the policy or permissions layer, data pipelines, observability, migration or backfill, admin tooling, documentation.
2. **Assign each component to an owning team.** Prefer the team that already owns the adjacent system. Flag any component with no natural owner; unowned work is a risk.
3. **Name the interface contracts.** For every edge where one team consumes another team's output, name the contract: API shape, event or data schema, service-level expectation, policy threshold, or UX spec. Record who publishes it, who consumes it, and the date it must be stable. These contracts are the TPM's main lever: agreed early, they let teams build in parallel against a stub.
4. **Separate decisions from build work.** Some dependencies are negotiations (for example, which actions an automated system may take without human approval). Make those explicit rows with an owner and a decide-by date. They are often on the critical path.
5. **Build the dependency map.** One row per task: id, name, owning team, duration estimate, depends-on ids, estimate source (team-provided or inferred). Use `templates/dependency-map.csv`.
6. **Compute the critical path.** Run `python scripts/critical_path.py <dependency-map.csv>`. Read the output for: the path itself, total duration, slack on each non-critical task, and cross-team edges on the path.
7. **Propose phasing.** Front-load a walking skeleton that exercises the riskiest contract end to end. Ship the lowest-risk slice that delivers user value first (for example, a read-only or answer-only mode before an acting mode). Name what each phase proves.
8. **Place buffer on the critical path** and say how much and why.

## Output Contract

Return:

- component-to-team ownership table, with unowned components flagged
- interface contract list: contract, publisher, consumers, stable-by date, status
- decision dependencies: decision, owner, decide-by date, what it blocks
- dependency map rows, each with estimate source
- critical path: task sequence, total duration, cross-team edges on the path
- slack per non-critical task
- phasing plan: phase, what ships, what it proves, exit criterion
- buffer placement and rationale
- open questions and inferred items, labelled

## Hard Boundaries

- Do not invent team names or estimates. If a team or estimate is not in the input, use a placeholder and label it inferred.
- Do not present a computed critical path as final until owning teams have confirmed their estimates.
- Do not decompose by component alone. A row with no owning team is not a plan.
- Do not assign engineering design choices. Engineering owns technical design; this skill owns who, when, and what depends on what.

## Sequencing

Run inside `tpm-plan`, after `tpm-frame`. Feed its risks to `risk-register` and its contracts to `tpm-align` as partner-team asks.
