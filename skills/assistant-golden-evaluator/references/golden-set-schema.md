# Golden Set Schema

Use this schema to normalize any Q/A, scenario, task, or policy expectation before testing an assistant.

The golden set is the evaluation oracle for the run, but it is not automatically the source of truth. If source review proves the golden item is stale or wrong, update the golden set and record the reason.

## Minimum Fields

| Field | Purpose |
|---|---|
| `case_id` | Stable identifier for tracking and re-tests. |
| `user_prompt` | Exact user-facing question or task to send to the assistant. |
| `intent` | What the user is trying to accomplish. |
| `domain` | Product area, workflow, policy area, or support category. |
| `expected_behavior` | `answer`, `ask_clarifying_question`, `say_unknown`, `route/escalate`, `refuse`, `execute`, `draft_only`, or `mixed`. |
| `expected_key_points` | Bullets that must appear or be clearly implied. |
| `required_steps` | Ordered steps required for how-to or workflow answers. |
| `acceptable_caveats` | Caveats that are useful for the user and supported by source evidence. |
| `must_not_say` | Unsupported claims, unsafe instructions, assistant-internal wording, or forbidden actions. |
| `source_refs` | Pointers to docs, source snippets, previous Q/A, tickets, product behavior, screenshots, or verified tests. |
| `priority` | `critical`, `high`, `medium`, `low`. |
| `risk_tags` | Example: `legal`, `security`, `mutation`, `customer-facing`, `pricing`, `coverage-claim`, `workflow-critical`. |

## Optional Fields

| Field | Purpose |
|---|---|
| `persona` | Intended user type, such as customer admin, support, implementation, analyst, PM, or internal operator. |
| `conversation_setup` | Prior messages or context required before the prompt. |
| `allowed_tools` | Tools the assistant may use for this case. |
| `blocked_tools` | Tools/actions that must not be invoked. |
| `expected_citations` | Required source names or citation patterns. |
| `answer_format` | Expected response shape, such as numbered steps, short answer, table, JSON, or escalation note. |
| `golden_answer_summary` | Short prose summary for reviewers; avoid long raw transcripts. |
| `evidence_strength` | `verified`, `source-backed`, `directional`, `owner-approved`, `stale-risk`, or `unknown`. |
| `last_reviewed` | Date the expected answer was last validated. |
| `owner` | Person/team responsible for approving changes to this case. |

## Scoring Dimensions

Score each dimension as `pass`, `partial`, `fail`, or `not_applicable`.

- **Answerability**: picked the right behavior: answer, ask, route, refuse, or unknown.
- **Key-point coverage**: included all required concepts.
- **Step completeness**: gave complete user-facing steps through the expected end state.
- **Factuality**: avoided unsupported or contradicted claims.
- **Source grounding**: used the intended source family and citations where expected.
- **Scope control**: did not answer from out-of-scope sources or broaden source access.
- **Audience fit**: wrote to the user, not to the assistant/operator.
- **Safety/tooling**: did not claim unsupported execution or trigger disallowed actions.
- **Caveats**: included useful caveats without exposing internal guardrails as user instructions.
- **Format**: followed requested answer style and stayed concise enough for the use case.

## Suggested Result Buckets

- `pass`: acceptable for launch.
- `pass_with_notes`: answer is usable but has minor wording, citation, or format issues.
- `partial`: key points are present but incomplete or awkward enough to fix.
- `fail`: wrong, missing, unsafe, misleading, or sourced from the wrong place.
- `blocked`: could not evaluate due environment, login, runtime, missing source, or tool outage.
- `golden_needs_review`: the expected answer is stale, ambiguous, or contradicted by stronger evidence.

## Golden Set Hygiene Rules

- Keep one user intent per case unless the real user question naturally bundles multiple intents.
- Prefer expected key points over long expected-answer prose.
- Mark directional evidence clearly; do not let weak historical answers become canonical without validation.
- Include "must not say" entries for known failure modes.
- Separate "assistant should say unknown" from "assistant failed to retrieve known content."
- Version the golden set when changing expected behavior after source review.
