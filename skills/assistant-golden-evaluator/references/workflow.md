# Assistant Evaluation Workflow

This workflow supports browser, API, transcript, or manual assistant evaluation. Pick the lightest adapter that can produce reliable evidence.

## Run Modes

| Mode | Use When | Typical Size | Output |
|---|---|---:|---|
| Smoke | Confirm the assistant is wired to the right source/tool scope. | 3-10 cases | Quick health note. |
| Targeted regression | Validate a changed prompt, source, tool, or runtime path. | 10-50 cases | Defect list and fix plan. |
| Full regression | Gate a release, launch, source migration, or model change. | Full golden set | Pass/fail matrix and launch recommendation. |
| Adversarial/policy | Test boundaries, unsupported actions, leakage, or unsafe claims. | Risk-selected | Safety defect report. |
| Exploratory | Discover gaps before a formal golden set exists. | Open-ended | Candidate test cases and source gaps. |

## Step 1: Establish Baseline

Record:

- assistant name and version
- environment and URL/API endpoint
- model and prompt/settings version if visible
- configured sources, tools, or knowledge bases
- account/tenant/workspace context
- date/time of the run
- tester and adapter used
- whether the run is read-only or action-capable

Do not proceed to answer-quality scoring if the assistant is clearly pointed at the wrong source/tool scope. First classify that as a configuration defect.

## Step 2: Prepare The Golden Set

Normalize the source Q/A or scenario list using `golden-set-schema.md`.

For each case:

- include expected key points
- include required omissions
- include source references
- mark evidence strength
- mark risk
- define expected behavior for unknowns, refusals, and escalation

If the golden set came from historical user Q/A, treat it as evidence to validate, not as automatically trusted truth.

## Step 3: Choose The Adapter

### Browser UI

Use when the assistant is primarily exposed through an app UI.

Capture:

- prompt text
- full answer or safe excerpt
- visible citations/source pills
- selected assistant/source/tool setting
- screenshots only when useful and allowed
- runtime inspector/tool trace when available

Start a fresh conversation for retrieval-sensitive cases unless the test explicitly requires context carryover.

### API Or Batch Harness

Use when a stable endpoint exists.

Capture:

- request payload, redacted as needed
- response text
- source/tool trace
- latency/error status
- model/version metadata

Prefer batch harnesses for full regressions if they can reproduce the real assistant configuration.

### Transcript Import

Use when the user has manually tested the assistant.

Capture:

- prompt
- answer
- cited sources
- observed UI state
- user notes

Do not assume manual transcript snippets are complete. Mark missing screenshots, source state, or configuration as uncertainty.

## Step 4: Execute Cases

For each case:

1. Reset or preserve context according to the case setup.
2. Submit the exact `user_prompt`.
3. Wait for the final answer and tool/source status.
4. Capture the answer and evidence.
5. Score against each dimension.
6. Classify defects immediately while context is fresh.

Avoid over-testing only happy paths. Include:

- common user wording
- terse questions
- ambiguous questions
- unsupported requests
- high-risk caveat questions
- source gaps
- questions that previously regressed

## Step 5: Compare Against Expected Key Points

Use a key-point comparison, not a verbatim string match.

Mark:

- covered key points
- missing key points
- unsupported additions
- contradicted points
- format deviations
- citation/source deviations
- unsafe or assistant-internal wording

For how-to answers, confirm the user can complete the job from the response. If the assistant stops before the final required action, that is a completeness defect unless the golden set requires a stop.

## Step 6: Root-Cause Triage

Use `defect-taxonomy.md`.

Ask:

- Did the assistant retrieve the right source?
- Does the source actually contain the missing answer?
- Did the prompt tell the assistant to expose internal caveats or operator instructions?
- Did answer formatting constraints conflict with the desired answer?
- Did the model over-refuse despite source support?
- Did the runtime/tool configuration prevent retrieval or execution?
- Is the golden expected answer outdated?

Do not default every issue to prompt tuning. Source and retrieval defects should be fixed at the source or configuration layer.

## Step 7: Fix And Re-Test

For each defect:

- assign an owner/layer
- propose a minimal fix
- apply only fixes within the user's requested scope
- re-run the original failed case
- run neighboring cases that could be affected by the fix

Track before/after answer summaries and avoid broad prompt rewrites unless the failure pattern is systemic.

## Step 8: Report Health

Use `report-template.md`.

A useful report answers:

- Is the assistant healthy for the intended launch scope?
- Which failures block launch?
- Which defects are prompt/settings vs source/retrieval vs runtime?
- Which golden items need owner review?
- What should be fixed first?
- What residual risks remain?

## Common Evaluation Patterns

### Retrieval Scope Regression

Symptoms:

- assistant says no source exists for a known question
- cites broad or unrelated sources
- answers from stale or unapproved material

Likely fixes:

- source binding
- metadata
- source naming
- chunking
- retrieval prompt
- source access policy

### User-Facing Tone Regression

Symptoms:

- answer speaks to the assistant/operator
- exposes "do not answer" or "route internally" guardrails as user instructions
- says "blocked" or "tool gap" when the user needs plain guidance

Likely fixes:

- concise prompt instructions
- separate internal metadata from user-facing content
- rewrite source cards/pages to distinguish user guidance from assistant policy

### Golden Set Mismatch

Symptoms:

- assistant answer contradicts original historical Q/A but matches stronger current docs/code/product behavior
- original answer was directional, incomplete, or stale

Likely fixes:

- update golden expected key points
- record source review
- mark old answer superseded

### Tool/Execution Misclaim

Symptoms:

- assistant claims it can execute when the runtime cannot
- assistant offers automation in an informational-only surface
- assistant omits approval or safety gates for action-capable runtime

Likely fixes:

- prompt/settings capability boundary
- tool binding correction
- tool readiness metadata
- runtime approval gate
- source card execution notes
