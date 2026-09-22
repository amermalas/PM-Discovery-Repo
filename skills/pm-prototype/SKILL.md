---
name: pm-prototype
description: Use for Stage 4 (PROTOTYPE) of the 5-stage AI-enabled product management loop — building a disposable interactive prototype from a grounded concept, keeping a decision log, and capturing the Business Logic Companion (the rules a prototype can't show). Trigger on "build a prototype for X", "clickable demo", "decision log", or "business logic companion". Do not use for production-ready implementation code.
---

# PM Prototype — Stage 4: Prototype and capture hidden logic

Part of a 5-stage operating loop (SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT) for using AI across the product management lifecycle, not just for one-off drafting. Converts a grounded understanding into something stakeholders can react to, then uses interaction — not abstract debate — to refine direction. A prototype shows screens; it does not make the rules behind them explicit, so every prototype moving toward delivery needs a linked Business Logic Companion.

## Objective

Produce the smallest testable interactive concept, plus a decision log and a Business Logic Companion that captures what the screens can't show.

## Required inputs

- A concise problem frame, target user, and workflow (from PM Ground / PM Listen output).
- Customer evidence and product-documentation source links.
- Known constraints, assumptions, and non-goals.

## What to do

1. For the actual disposable interactive build, hand off to `disposable-prototype-builder` and `prototype-planning` — they already implement a style-neutral prototype layout, synthetic-data plan, and verification checklist. Do not reimplement that pipeline here.
2. Start with the smallest end-to-end workflow that makes the idea testable.
3. Provide requirements, states, realistic sample data, edge cases, and the decision the prototype should unlock.
4. Iterate live in stakeholder conversations: change language, ordering, controls, and states as feedback emerges.
5. Keep a decision log: what changed, why, who requested it, whether the change is validated or still a hypothesis.
6. Label the artifact clearly as a prototype. Never imply production readiness, security posture, data completeness, or engineering estimates.

## Prototype brief template

- **User and job**: who is acting, in what context, what they're trying to accomplish.
- **Starting state**: what the user knows, sees, and has permission to do.
- **Happy path**: the smallest complete workflow.
- **Critical states**: loading, empty, error, partial data, permission, success.
- **Evidence**: calls, pages, issues that support each important choice.
- **Assumptions**: unvalidated beliefs the prototype is designed to test.
- **Non-goals**: what the prototype intentionally does not solve.
- **Decision**: what feedback or observation will change the direction.

## Business Logic Companion

| Logic area | What to document | Example question |
|---|---|---|
| Decision rules | Conditions, thresholds, calculations, precedence | What determines which result, warning, or action appears? |
| Data | Source, ownership, freshness, null/partial/conflicting behavior | What happens when data is late, incomplete, or contradictory? |
| Roles and permissions | Who may view, create, change, approve, delete | How does behavior differ by role or account configuration? |
| States and transitions | Allowed states, triggers, reversibility, terminal states | What events move this object between states? |
| Validation | Required fields, eligibility rules, invalid combinations | What prevents the action, and how is the reason explained? |
| Exceptions | Empty, error, duplicate, timeout, permission, recovery | Which non-happy paths materially change the user outcome? |
| System effects | Notifications, audit history, analytics, downstream updates | What else changes when the user completes this action? |
| Evidence and status | Source links, confirmed vs inferred, owner, open questions | Which rules are documented facts, PM decisions, or hypotheses? |

Label every row **Confirmed**, **PM decision**, **Inference**, or **Open question**. Never treat inferred behavior as established product logic — review the draft with design and engineering.

## Copy-ready prompt

> Review the prototype brief, decision log, and grounded source material in this session. Create a Business Logic Companion covering decision rules, data sources and freshness, permissions, states and transitions, validation, defaults and precedence, empty/partial/error behavior, notifications, audit history, analytics, downstream effects, and unresolved questions. For every item include its source and label it Confirmed, PM decision, Inference, or Open question. Do not infer implementation architecture.

## Outputs

- A lightweight interactive prototype (via `disposable-prototype-builder`, using synthetic data only).
- A tested workflow narrative with explicit states and edge cases.
- A decision log and a reviewed Business Logic Companion, linked from the prototype.

## Review gate

Happy path, critical states, rules, permissions, and exceptions are reviewable and each item's status (confirmed/decision/inference/open) is visible.

## Related repo resources

- `prototype-planning`, `disposable-prototype-builder` — plan, build, and verify the prototype.

## Guardrails

Prototype code is disposable and non-production; it may omit production architecture, accessibility, observability, privacy, and security requirements. Say so explicitly wherever the prototype is shared. Use only synthetic data — see `public-safety-review` before sharing anything derived from real customer or company sources.
