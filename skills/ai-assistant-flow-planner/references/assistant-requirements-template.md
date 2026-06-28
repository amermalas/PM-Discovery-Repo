# AI Assistant Requirements Template

Use this template when producing a complete PM planning artifact for an AI assistant, chatbot, copilot, or conversational workflow.

## 1. Product Framing

Feature name:

Primary user:

Workflow family:

Business outcome:

User workflow outcome:

One-line framing:

> When a user needs to [workflow job], the assistant helps them [resolve, retrieve, synthesize, review, prepare, or act] using [grounded evidence or context], while preserving [guardrail, approval rule, source visibility, or non-goal].

## 2. Source Evidence

| Source | What it contributes | Status |
|---|---|---|
| Product brief | | |
| Research notes | | |
| Existing product surface | | |
| Existing data or tool capability | | |
| Open assumptions | | |

## 3. Conversation Paths

| Path / interaction | Trigger | Required state | Inputs to resolve | Data/tool/context steps | Assistant output | Artifact updated | Gate / follow-up behavior |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Default path pattern:

```text
resolve scope -> retrieve primary evidence -> retrieve overlays/context -> synthesize -> render evidence -> support follow-ups
```

Operational path pattern:

```text
resolve scope -> profile inputs -> review source/state -> draft artifact -> human review -> stakeholder gate -> generate handoff/output -> validate -> handoff
```

## 4. Suggested Prompt Chips

| Interaction | Suggested user prompts / action chips | When shown | Expected assistant action |
|---|---|---|---|
| | | | |

Treat these as user-facing affordances, not backend system prompts.

## 5. Top-Down Scope Audit

| Level | Decision | Current understanding | Open gap |
|---|---|---|---|
| Business goal | | | |
| Workflow outcome | | | |
| Assistant mission | | | |
| MVP boundary | | | |
| Out-of-scope boundary | | | |

| Stage | Goal | Required tasks | Deliverables | Gate |
|---|---|---|---|---|
| | | | | |

## 6. Ownership Layer Map

| Layer | Requirement | Owner | Existing capability | Gap |
|---|---|---|---|---|
| Assistant runtime | Conversation, history, state, tool calls, traces | | | |
| Agent configuration | Instructions, starter prompts, model, tools, deployment, eval metadata | | | |
| Product backend | Retrieval, deterministic services, permissions, persistence, mutations | | | |
| Product UI | Chat surface, cards, tables, maps, drawers, approvals, exports | | | |
| Output contract | Markdown, structured sections, typed artifacts, citations, unknowns | | | |
| Evaluation | Scenarios, grounding checks, quality checks, cost bounds | | | |
| Governance | Review gates, audit, access, retention, safety language | | | |

## 7. Durable Artifacts And Gates

| Artifact | Purpose | Owner | Draft/reviewed/approved states | Downstream dependency |
|---|---|---|---|---|
| | | | | |

| Gate | Required evidence | Who approves | What it unlocks | What invalidates it |
|---|---|---|---|---|
| | | | | |

Rules:

- Chat history is not workflow state.
- AI-generated artifacts remain drafts until a human review or approval gate promotes them.
- Every downstream file, record, recommendation, or handoff should reference the reviewed artifact version it depends on.
- If an approved artifact changes, dependent sign-offs and generated outputs should be invalidated or reapproved.

## 8. Tool And Data Source Map

| User need | Required data | Existing source/tool | New source/tool needed | Fallback / limits |
|---|---|---|---|---|
| | | | | |

## 9. Output And Rendering Contract

| Output element | Markdown text | Structured artifact | UI component | Required evidence |
|---|---|---|---|---|
| Bottom line | | | | |
| Evidence checked | | | | |
| Key findings | | | | |
| Gaps and limits | | | | |
| Recommended next questions | | | | |
| Export or handoff artifact | | | | |

## 10. Recommendations And Actions

Allowed recommendations:

-

Disallowed recommendations:

-

Actions requiring approval:

-

## 11. Scenario And Evaluation Plan

| Scenario | Expected behavior | Evidence requirement | Failure mode tested | Owner |
|---|---|---|---|---|
| Happy path with strong data | | | | |
| No matching data | | | | |
| Partial evidence | | | | |
| Ambiguous prompt | | | | |
| Broad/high-cost prompt | | | | |
| Malformed prompt | | | | |
| Follow-up question | | | | |
| Source grounding check | | | | |

## 12. Open PM Decisions

-

