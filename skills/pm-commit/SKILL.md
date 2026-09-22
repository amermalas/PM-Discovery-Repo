---
name: pm-commit
description: Use for Stage 5 (COMMIT) of the 5-stage AI-enabled product management loop — converting a validated prototype and decision log into requirements, an epic, and testable stories without losing rationale or traceability. Trigger on "prepare for delivery", "draft requirements for X", "turn this into delivery tickets", or "epic breakdown". Not for the prototype build itself — that's pm-prototype.
---

# PM Commit — Stage 5: Convert the validated concept into delivery-ready work

Part of a 5-stage operating loop (SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT) for using AI across the product management lifecycle, not just for one-off drafting. Translates prototype decisions and source evidence into requirements and delivery-ready work without losing rationale or traceability. This is the final stage of the loop; validated insights and decisions should also feed back into the market brief (PM Sense), the customer evidence base (PM Listen), and product documentation (PM Ground).

## Objective

Turn a reviewed prototype + decision log + Business Logic Companion into requirements and delivery tickets that PM, design, engineering, and QA can review against the same traceable definition.

## Required inputs

- The current prototype and decision log (from PM Prototype).
- Customer-call evidence, documentation pages, and related tickets (from PM Listen / PM Ground).
- Known technical, data, security, and operational constraints.

## What to do

1. For turning one selected opportunity into a full product brief, refined JTBD, MVP scope, below-the-line rationale, or engineering open-questions package, route to `opportunity-refinement` — it already implements this handoff-scaffold pattern.
2. For AI assistant/chatbot/copilot features specifically (conversation paths, prompt chips, platform gaps, interaction stories), route to `ai-assistant-flow-planner`.
3. If the work involves creating or updating task/how-to cards rather than a new feature, route to `task-card-knowledge-builder`.
4. Draft the requirement set from the final prototype state, decision log, and reviewed Business Logic Companion in the same session — don't restart context.
5. For each requirement: include rationale, evidence, assumptions, dependencies, edge cases, acceptance criteria.
6. Separate product requirements from implementation suggestions — engineering owns technical design.
7. Break work into an epic and independently valuable stories; include discovery spikes where uncertainty is material.
8. Review for testability, duplication, hidden scope, missing failure states, and unsupported claims before filing tickets.

## QA-ready extension

When the concept is moving into delivery, include where relevant:
- Product Brief and reviewed Business Logic Companion.
- Verified task cards or workflow references.
- Prototype or recorded walkthrough.
- Any manual verification results already available.
- Epic/stories and explicit test-data assumptions.

QA owns edge-case coverage, test data, automation design, release risk, and the final test plan — these inputs seed scenarios, they don't replace QA's judgment.

## Ticket-generation prompt

> Using the final prototype state and decision log from this session, draft an epic and a minimal set of independently valuable stories. For each story include user outcome, rationale, linked evidence, in-scope behavior, non-goals, acceptance criteria, edge/error states, dependencies, analytics or audit needs, and open questions. Flag anything inferred rather than confirmed. Do not invent implementation details.

## Definition of ready for AI-assisted tickets

- [ ] The user and outcome are explicit.
- [ ] Important behavior is supported by evidence or labeled as a hypothesis.
- [ ] Acceptance criteria describe observable behavior.
- [ ] Permissions, empty/loading/error states, and data freshness are addressed where relevant.
- [ ] Dependencies and related work are linked.
- [ ] Non-goals constrain scope.
- [ ] A human PM and engineering/design partner have reviewed the issue.

## Outputs

- A concise requirements brief or PRD.
- An epic with scoped, testable stories and acceptance criteria.
- Traceability from delivery work back to evidence, decisions, and prototype states.

## Review gate

PM, design, engineering, and QA can review the same traceable definition — nothing important lives only in chat history.

## Related repo resources

- `opportunity-refinement`, `ai-assistant-flow-planner`, `task-card-knowledge-builder`.

## Guardrails

Do not invent sources, customer claims, existing behavior, or implementation details. Say when evidence is missing or conflicting rather than filling the gap. This stage is the last human-review checkpoint before work becomes delivery commitments — flag anything touching auth, production config, customer data, or security controls for human review before filing.
