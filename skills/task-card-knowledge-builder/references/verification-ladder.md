# Verification Ladder

Use this reference when deciding whether card claims are strong enough to promote, publish, or leave blocked.

## Evidence Layers

| Layer | What it proves | Use for |
|---|---|---|
| Source documentation review | A documented how-to, concept, or product statement exists. | Candidate drafting and low-risk conceptual guidance. |
| Repo/code review | UI route, labels, request shape, service behavior, validation, permissions, persistence, or audit behavior are source-visible. | Procedural claims and tool-readiness mapping. |
| Browser read-only check | Visible UI path, labels, and navigation exist in a test/demo environment without mutation. | High-risk UI guidance and label reconciliation. |
| Controlled preview/dry-run | Preview, validation, or sample result can be produced without persistence. | Preview/dry-run cards and configuration planning. |
| Fixture mutation | A safe, named fixture proves save/update behavior. | Only when explicitly approved and recorded. |
| Tool inventory | A tool/resource exists, can be configured, or is missing. | Tool-readiness classification. |
| Live tool test | A configured tool works with safe inputs and expected audit behavior. | Future execution promotion only when explicitly authorized. |
| Owner/legal/security review | Wording and action posture are approved. | Sensitive claims, legal/security, package/SKU, roadmap, external sends, and coverage claims. |

## Verification Outcomes

Use consistent outcomes:

- `passed_read_only`: UI/source claim verified without mutation.
- `pass_with_notes`: mostly verified, with minor label/config/caveat differences.
- `passed_fixture_mutation`: verified with an approved safe fixture.
- `not_applicable_conceptual`: no browser path needed because the card is conceptual.
- `not_applicable_guardrail`: card is a refusal/routing/blocked-action guardrail.
- `pressure_blocked`: verification would expose restricted data, require unsafe mutation, or lacks a safe fixture.
- `pending_enablement`: feature is gated/off in the current environment.
- `owner_review_needed`: wording, policy, or supported path needs owner approval.
- `rejected`: not suitable for verified task-card knowledge.

## Browser Safety Rules

- Prefer read-only route and label proof.
- Do not open live rows, files, notes, messages, attachments, exports, external portals, hidden debug payloads, or identity-bearing URLs unless explicitly authorized.
- Do not click destructive, outbound, send, import, export, activation, archive, delete, batch, or external-handoff controls during verification.
- For forms, inspect labels and required fields where safe; do not save unless using an approved fixture.
- If a button/action has unclear side effects, classify as pressure-blocked and record why.

## Code Review Rules

When checking code:

1. Locate the route, component, action menu, service, controller, or mutation path.
2. Identify required fields, validation, permission gates, audit events, and persistence behavior.
3. Separate frontend-only affordances from backend-supported operations.
4. Record file paths and high-level findings, not secrets or raw restricted payloads.
5. Promote only what the code proves. Do not infer user-facing steps from backend helper names alone.

## Owner Review Triggers

Require owner review for:

- legal, security, entitlement, package/SKU, pricing, roadmap, or coverage claims
- unsupported workflow boundaries
- external reporting/sends/submissions
- identity, access, retention, regulatory-compliance, or destructive actions
- ambiguous customer-facing wording
- any instruction that could be interpreted as operational advice outside product how-to guidance
