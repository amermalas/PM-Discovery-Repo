---
name: assistant-golden-evaluator
description: Use when asked to evaluate any AI assistant, chatbot, copilot, agent, or answer surface against a golden Q/A or scenario set, run browser/API/manual tests, identify answer deviations, classify root causes, and recommend fixes to prompt/settings, retrieval scope, source data, tools, or the golden set.
---

# Assistant Golden Evaluator

Use this skill to evaluate an AI assistant against a known-good set of questions, expected answer key points, scenarios, or policy expectations.

This is a generic evaluation template. Do not hard-code the workflow to a specific product, platform, or any one assistant runtime. Treat those as optional adapters or evidence sources only when the current evaluation explicitly names them.

## Use This Skill When

- comparing an assistant's answers to a golden Q/A set
- pressure testing an assistant after prompt, model, retrieval, tool, or source-data changes
- checking whether answers are user-facing instead of assistant-internal
- finding retrieval gaps, over-refusals, hallucinations, missing caveats, bad citations, or unsupported execution claims
- deciding whether a defect belongs in the assistant prompt/settings, source data, retrieval configuration, tool configuration, UI/runtime behavior, or the golden set
- producing a regression report with pass/fail status and recommended remediation

## Required Inputs

Collect or infer these before running a full evaluation:

- Assistant target: name, URL/API entrypoint, environment, version, model if known, and configured sources/tools if visible.
- Golden set: questions or scenarios, expected key points, unacceptable claims, source references if available, and expected behavior when no answer exists.
- Evaluation mode: smoke, targeted regression, full regression, adversarial/policy, or release gate.
- Execution channel: browser UI, API, chat transcript import, CLI, batch harness, or manual capture.
- Allowed actions: read-only answer testing, tool-call testing, draft-only testing, approved mutation testing, or no-execution testing.
- Evidence policy: what can be captured, quoted, persisted, shared, or redacted.

If any of these are missing, make the narrowest safe assumption and record it in the run notes.

## Required Workflow

1. Scope the run.
   - Define the assistant, environment, version, and evaluation purpose.
   - Separate smoke tests from regression gates.
   - Decide whether the run is read-only or may trigger tools/actions.

2. Normalize the golden set.
   - Read `references/golden-set-schema.md`.
   - Convert each item into a stable test case with expected key points, required omissions, acceptable caveats, and scoring criteria.
   - Preserve the original source answer as evidence, not as prompt text to be copied blindly.

3. Run the assistant.
   - Read `references/workflow.md`.
   - Use the chosen adapter: browser UI, API, batch harness, transcript import, or manual capture.
   - Start clean conversations when testing retrieval/routing.
   - Capture the exact user prompt, answer, citations/source links, visible state, and any tool/runtime traces available.

4. Score the answer.
   - Check answerability, factual match, completeness, source grounding, audience fit, caveats, safety, and format.
   - Penalize assistant-internal instructions exposed to users, unsupported execution claims, stale source leakage, missing save/submit/final steps where the user asked for a complete how-to, and over-confident claims not present in the golden set or source data.

5. Classify defects.
   - Read `references/defect-taxonomy.md`.
   - Decide whether each failure is likely caused by prompt/settings, retrieval/source scoping, missing or weak source data, tool/runtime configuration, UI/runtime bug, model behavior, or a bad/outdated golden item.
   - Prefer root-cause fixes over one-off answer edits.

6. Recommend remediation.
   - For prompt/settings defects, propose concise instruction changes and remove repetition.
   - For source-data defects, identify the exact missing/ambiguous record and the needed update.
   - For retrieval defects, recommend source scoping, metadata, chunking, naming, or citation changes.
   - For tool/runtime defects, separate configuration from required development work.
   - For golden-set defects, update the expected answer only when stronger evidence shows the golden item is wrong or stale.

7. Re-test fixed paths.
   - Re-run failed cases after remediation.
   - Track before/after answer deltas.
   - Do not call the assistant healthy until key workflows and known regression questions pass under the intended source/tool scope.

8. Report.
   - Use `references/report-template.md`.
   - Lead with health status, blocker count, pass/fail counts, and the highest-risk deviations.
   - Include enough evidence for owners to reproduce defects without dumping sensitive raw transcripts unnecessarily.

## Quality Gates

An assistant passes a release-quality regression only when:

- the configured source/tool scope matches the intended product behavior
- representative golden-set questions retrieve the right source family
- expected key points are covered without unsupported additions
- "I don't know" behavior appears only where the golden set/source data truly lacks support
- answers are directed to the end user, not to the assistant/operator
- citations or source references are accurate enough for review
- no answer claims execution capability unless the runtime actually supports it and the evaluation mode allowed it
- all high-risk defects have either been fixed, explicitly accepted by an owner, or blocked from launch scope

## Hard Boundaries

- Do not mutate production or customer data unless the user explicitly scopes an approved mutation test.
- Do not broaden assistant source access just to make a test pass unless that is the intended product scope.
- Do not treat original Q/A as authoritative when stronger current source evidence contradicts it.
- Do not paste secrets, auth headers, cookies, private links, or raw restricted transcripts into durable reports.
- Do not hide a failed retrieval as a prompt issue; classify retrieval and source-scope failures explicitly.
- Do not edit canonical source data when the user asks only to tune a deployed assistant surface.
- Do not include private company names, ticket IDs, internal platform names, customer names, local file paths, or proprietary examples in public outputs.

## References

- `references/golden-set-schema.md` - normalized test-case fields and scoring dimensions
- `references/workflow.md` - end-to-end evaluation procedure and run modes
- `references/defect-taxonomy.md` - root-cause classification and fix routing
- `references/report-template.md` - reusable regression report shape

## Output Contract

A completed evaluation should leave behind:

- run scope and environment metadata
- normalized golden-set manifest or pointer to it
- captured assistant answers or redacted excerpts
- per-case score and defect classification
- recommended fixes by owner/layer
- re-test status for remediated cases
- launch/readiness recommendation with residual risk
