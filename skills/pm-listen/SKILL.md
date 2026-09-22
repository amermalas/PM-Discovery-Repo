---
name: pm-listen
description: Use for Stage 2 (LISTEN) of the 5-stage AI-enabled product management loop — turning customer calls into a searchable, traceable evidence base and pulling evidence-backed opportunity briefs from it. Trigger on "customer evidence for X", "what are customers saying about X", "opportunity brief", "pull quotes for X", or "evidence-backed requirement". Keeps direct customer evidence distinct from PM synthesis.
---

# PM Listen — Stage 2: Turn customer calls into a searchable evidence base

Part of a 5-stage operating loop (SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT) for using AI across the product management lifecycle, not just for one-off drafting. This stage makes the voice of the customer retrievable by product area so observations and requirements trace back to real conversations.

## Objective

Make customer evidence retrievable, traceable, and clearly separated from PM interpretation.

## Required inputs

- A problem statement and customer/workflow query.
- Your own structured customer-evidence sources: account notes, call transcripts, survey exports, support/ticket exports, or a governed evidence pipeline if you maintain one.
- Do not build a parallel evidence pipeline when an existing governed source already covers the account/product area — check first.

## What to do

1. For new source intake (a new account report, transcript, survey, ticket dump, etc.) that isn't yet classified, route to `source-intake` — it produces governed source cards, sensitivity/allowed-use rules, and routing before anything downstream uses the source.
2. For turning already-governed sources into atomic evidence rows, painpoint/request/workaround classification, or crosswalks, route to `customer-evidence-normalizer`.
3. For synthesizing governed evidence into ranked, validated painpoint lists or opportunity buckets, route to `painpoint-validation` and `opportunity-selection`.
4. Preserve the source reference and surrounding context; never keep only an AI interpretation of a quote.
5. Tag evidence by product area, persona, workflow, pain point, request, outcome, and strength of signal.
6. Query for patterns *and* counterexamples. Distinguish frequency from commercial importance — one account repeating an issue is not five independent signals.

## Recommended evidence fields

| Field | Purpose | Example |
|---|---|---|
| Account / segment | Context and pattern analysis | Enterprise / ops team |
| Call date + source | Traceability | 2026-07-15 · call recording link |
| Speaker + role | Correct attribution | Operations lead |
| Product bucket / workflow | Retrieval scope | Monitoring workflow |
| Observation type | Normalize evidence | Pain point / request / workaround / praise |
| Evidence excerpt | Verbatim support with context | Short excerpt plus surrounding exchange |
| Interpreted need | PM synthesis — not a quote | Needs faster confidence assessment |
| Strength / confidence | Avoid false precision | Repeated / isolated / ambiguous |
| Related idea / ticket / doc | Connect discovery to delivery | Link to concept or issue |

## Copy-ready prompt

> Using only the connected [product bucket] call database, identify the strongest evidence about [problem]. Group by user workflow, cite each supporting call, include contradictory or neutral evidence, and separate direct customer statements from your interpretation. Conclude with implications and unanswered questions — not final requirements.

## Common failure modes to avoid

- Counting every mention as an independent request, even when calls repeat the same account or issue.
- Losing the distinction between buyer, administrator, operator, and end user.
- Turning a proposed solution into the underlying customer need.
- Using a memorable quote without checking whether it represents a broader pattern.
- Treating an AI-generated summary as authoritative when the source transcript is ambiguous.

## Review gate

Direct evidence is traceable to a source (account, call, date, speaker) and distinct from PM synthesis.

## Related repo resources

- `source-intake`, `customer-evidence-normalizer`, `painpoint-validation`, `opportunity-selection`.

## Guardrails

Customer transcripts and confidential material stay in your organization's approved environments only. Never treat an account-summary rollup as the original transcript — confirm exact wording/attribution against source before external citation.
