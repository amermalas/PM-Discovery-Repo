# Promotion, Runtime, And Tool-Readiness Gates

Use this reference when promoting candidates into verified cards or preparing runtime artifacts.

## Promotion Loop

For each candidate pack:

1. Load the candidate pack, source rows, code/browser verification artifacts, existing verified cards, eval seed, runtime schema, response policy, and tool-readiness map.
2. Decide shape for every candidate.
3. Promote only `standalone_card` or `parent_card` units that pass manual guidance gates.
4. Merge useful `step_or_detail` findings into the correct parent card.
5. Keep `gap_only` and `rejected_not_task_card` out of verified runtime truth.
6. Record a promotion artifact with inputs, decisions, evidence, blocked actions, tool bucket, and next steps.
7. Update eval prompts, runtime exports, bundles, response-policy validation, registry/security/task list, and a governance log when counts or runtime scope change.

## Manual Guidance Gate

A card can become `validated_manual_guidance` when:

- the user job is concrete and current
- manual steps are complete enough for the intended audience
- prerequisites and tenant/permission assumptions are explicit
- UI entry points and expected outcome are known
- caveats are user-facing, not assistant-internal
- source/code/browser/owner evidence supports the claims
- unsafe actions are blocked
- execution remains blocked unless future execution gates are fully proven

## Tool-Readiness Buckets

Assign exactly one:

| Bucket | Meaning |
|---|---|
| `tool_exists` | A relevant tool is observed or source-verified, but execution still needs binding, approval, permission, audit, redaction, test, idempotency, and rollback proof. |
| `tool_can_be_configured` | Internal API/function behavior appears available and can likely be wired as a tool without product-code development, subject to owner review and tool-gate proof. |
| `tool_needs_development_wrapper` | UI/backend behavior exists, but a safe agent-facing wrapper, validation contract, redaction, audit, approval, or rollback path must be built. |
| `ui_fallback_only` | Keep as human instructions, routing, or guardrail because no safe tool path is proven or policy requires manual handling. |

Never equate a tool bucket with execution permission.

## Runtime Export Gate

Before a card can power an assistant:

- source card is in the verified collection
- schema validation passes
- no required fields are missing
- tool-use bucket is normalized
- `execution_allowed=false` unless a separate execution launch has been approved
- pressure-test status is explicit
- response-policy overlay defines whether steps, caveat answer, draft-only, or routing behavior is allowed
- eval prompts cover normal guidance and execution/refusal behavior

## Eval Gate

Maintain at least:

- normal user how-to prompt
- execution request prompt
- source conflict prompt for sensitive or ambiguous topics
- missing-card or unsupported-action prompt when applicable
- pressure-blocked prompt where the assistant must route rather than invent

Use `assistant-golden-evaluator` for assistant-level regression after cards are loaded into an assistant surface.

## Publication Readiness

Step-by-step publishing requires either browser/code/source proof strong enough for the workflow or an explicit non-applicability classification. Pressure-blocked guided cards can remain in the corpus as route-only or caveated guardrails, but should not produce detailed procedural steps that imply unverified live behavior.
