# Card Shape And Content Rules

Use this reference when deciding what becomes a task card and how to write it.

## Card Acceptance Test

A standalone task card should have:

- a recognizable user job-to-be-done
- a supported product area or workflow
- clear entry point or prerequisite
- complete manual steps or a clear conceptual answer
- expected outcome
- known caveats and limits
- blocked or unsafe actions
- source/code/browser/owner evidence, or an explicit proof gap
- tool-readiness category if future execution may matter

Do not promote a card just because a source mentions a feature. The card must teach, route, caveat, or safely refuse a real user task.

## Shape Decisions

| Shape | Use when |
|---|---|
| `standalone_card` | The finding is a complete user-facing job with steps, boundaries, and outcome. |
| `parent_card` | Multiple findings are variants of the same job and should be merged under one card. |
| `step_or_detail` | The finding is true but only belongs inside another card. |
| `gap_only` | Demand exists, but current evidence does not prove a supported user-facing path. |
| `rejected_not_task_card` | The finding is stale, unsafe, internal-only, unsupported, duplicate, or not a user task. |

## User-Facing Content

Include:

- what this helps with
- when to use it
- prerequisites or permissions
- step-by-step how-to, if procedural
- expected outcome or confirmation state
- useful caveats phrased for the user
- what to do when the path differs by tenant/configuration
- source/verification summary

Avoid:

- assistant-internal policy language
- "do not reveal" / "route as internal" phrasing unless translated into user-facing support guidance
- raw implementation notes
- tool IDs, opaque internal payloads, hidden route enumeration, or auth details
- unverified workaround steps
- incomplete how-to steps that stop before the user's valid end state, unless the action is explicitly unsupported or unsafe

## Required Runtime Fields

When promoting into the verified corpus, preserve or backfill:

- `card_id`
- `card_title`
- `card_status`
- `trust_level`
- `primary_audience`
- `sensitivity`
- `program_area`
- `product_area`
- `user_job`
- `user_question_patterns`
- `trigger_conditions`
- `does_not_apply_when`
- `clarifying_questions`
- `answer_mode`
- `runtime_allowed`
- `short_answer`
- `guidance_steps` for procedural cards
- `known_caveats`
- `safe_now`
- `blocked_until_verified`
- `never_do_from_this_card`
- `tool_use_category`
- `tool_readiness_notes`
- `verification_artifact`
- `last_verified`
- `pressure_test_status`

Candidate packs can be looser. Verified runtime cards cannot.
