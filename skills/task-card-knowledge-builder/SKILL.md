---
name: task-card-knowledge-builder
description: Use when asked to create, normalize, verify, promote, audit, backfill, export, or govern task cards / how-to cards from product knowledge, Q/A, documentation, code, browser testing, customer evidence, tool inventories, or runtime eval results. Use for source-to-card disposition, card schema decisions, demo/browser pressure testing, source/code verification, tool-readiness mapping, verified-card runtime export gates, and deciding whether a finding becomes a standalone task card, a step/detail, a gap-only note, or a rejected candidate.
---

# Task Card Knowledge Builder

Use this skill to turn messy product knowledge into verified task cards that can safely power how-to agents, product copilots, video scripts, QA scenario stitching, and future execution planning.

This skill captures a full task-card lifecycle: source harvest, candidate cardization, evidence review, source/code/browser verification, promotion, tool-readiness classification, runtime export, eval gating, and publication readiness.

## Start Here

1. Identify the current task-card job:
   - source harvest or gap sweep
   - candidate card drafting
   - candidate promotion/disposition
   - source/code/browser verification
   - demo/browser pressure audit
   - runtime export or response-policy validation
   - tool-readiness mapping
   - backfill of old cards
2. Read only the relevant references:
   - `references/source-intake.md` for source harvesting, manifesting, and source-to-card disposition.
   - `references/card-shape.md` for deciding whether something is a card, a step/detail, a gap, or a reject.
   - `references/verification-ladder.md` for source/code/browser/tool/owner verification gates.
   - `references/promotion-runtime.md` for promotion, runtime export, response policy, eval gates, and tool-readiness buckets.
3. Keep candidate content separate from verified runtime truth.
4. Never treat directional Q/A, source-code findings, UI labels, or generated summaries as final answer text without stronger verification.

## Core Workflow

1. **Harvest sources.** Capture source rows with lineage, sensitivity, product/program area, likely user job, and evidence strength.
2. **Normalize candidate jobs.** Convert findings into user jobs, not implementation trivia. Use verb-object phrasing such as create incident, review tasks, configure topic, or troubleshoot import.
3. **Decide shape.** Classify each finding as `standalone_card`, `parent_card`, `step_or_detail`, `gap_only`, or `rejected_not_task_card`.
4. **Draft cautiously.** Write user-facing how-to steps only when source evidence supports them. Keep assistant-internal guardrails, implementation notes, and execution gaps out of the user-facing body.
5. **Verify.** Use the verification ladder: source docs, code review, browser/UI check, non-mutating preview, tool inventory, a live tool test only if explicitly authorized, and owner/legal/security review where needed.
6. **Promote only verified cards.** Add to verified knowledge only when the manual path, boundaries, prerequisites, and blocked actions are clear enough for a human user.
7. **Map tool readiness.** Assign exactly one execution bucket: `tool_exists`, `tool_can_be_configured`, `tool_needs_development_wrapper`, or `ui_fallback_only`. Do not imply execution readiness from tool existence.
8. **Gate runtime publication.** Export, validate, bundle, and eval cards before using them in an assistant. Pressure-blocked guided cards should route or caveat rather than invent untested procedural steps.

## Hard Boundaries

- Do not mutate demo/product environments unless an explicitly approved fixture or mutation-safe path is in scope.
- Do not configure a tool platform, run live tool tests, bind tools, call product APIs, or publish customer-facing content unless the current task explicitly authorizes it.
- Do not promote raw support-channel answers, internal walkthrough scripts, help-desk docs, code observations, browser observations, or customer evidence directly into runtime truth.
- Do not create standalone task cards for internal-only mechanics, source-code helper functions, UI implementation details, or unsafe/unsupported actions.
- Do not mark any card execution-ready until approval, permission, validation, audit, idempotency, redaction, rollback/correction, and live-tool-test gates are proven.
- Do not persist secrets, auth headers, cookies, raw restricted payloads, customer data, or live row/file/message contents in card artifacts.
- Do not include private company names, ticket IDs, internal platform names, customer names, local file paths, or proprietary examples in public outputs.

## Output Contract

A task-card lifecycle pass should produce or update the appropriate artifacts:

- source manifest or source-to-card disposition
- candidate card pack or gap inventory
- promotion/verification artifact with decisions and evidence
- verified card updates only for promoted units
- tool-readiness notes and blocked actions
- runtime export / bundle / response-policy / eval updates when publication scope changes
- a governance log entry for repo/process changes

State what was verified by source, code, browser, owner review, or runtime checks, and what remains blocked or inferred.
