# Defect Taxonomy And Fix Routing

Classify defects by root cause. One answer can have multiple defects, but identify the primary blocker.

## D1: Assistant Configuration / Scope

The assistant is pointed at the wrong model, prompt, source, tool set, workspace, environment, or version.

Signals:

- known source is not available
- wrong assistant was selected
- source/tool binding missing
- environment mismatch
- old prompt still active

Fix routing:

- assistant settings
- deployment/publish step
- source binding
- tool binding
- environment configuration

## D2: Retrieval / Source Selection

The source exists but retrieval misses it or chooses weaker material.

Signals:

- answer says "no verified answer" even though source contains it
- cites unrelated pages
- retrieves broad background instead of the specific card/doc
- repeated confusion between similarly named records

Fix routing:

- source chunking
- metadata fields
- document titles
- retrieval prompt
- source filters
- ranking/synonym support
- deduplication

## D3: Source Data Gap

The assistant cannot answer because the approved source corpus lacks the needed content.

Signals:

- no source record covers the user intent
- source contains only a caveat but no complete user-facing answer
- required step, boundary, or definition is missing
- source has internal notes but no user guidance

Fix routing:

- add or update source page/card/doc
- verify content against stronger evidence
- add examples or step sequences
- owner approval for sensitive wording

## D4: Source Data Quality

The source exists but is ambiguous, stale, contradictory, too internal, too verbose, or not shaped for assistant behavior.

Signals:

- answer exposes implementation notes to the user
- source mixes user guidance with assistant policy
- source contains caveats without the actionable path
- conflicting records exist

Fix routing:

- source normalization
- source split: user-facing guidance vs internal guardrail
- stale record archival
- title/metadata cleanup
- owner review

## D5: Prompt / Instruction Defect

The assistant prompt causes bad behavior even when sources are adequate.

Signals:

- answers are too long because instructions repeat
- assistant overuses caveats
- assistant refuses answerable questions
- assistant includes internal guardrail sections
- assistant ignores desired format

Fix routing:

- concise prompt revision
- remove redundant instructions
- clarify priority order
- define answer format
- define user-facing vs internal behavior

## D6: Model Behavior Defect

The prompt and source are reasonable, but the model still synthesizes poorly.

Signals:

- inconsistent answers to the same case
- unsupported bridging between sources
- poor reasoning over multi-part prompts
- misses clear key points despite retrieval

Fix routing:

- stronger response template
- few-shot examples
- lower creativity settings
- model change
- decomposition into smaller retrieval/planning steps

## D7: Tool / Runtime Defect

The assistant depends on tool calls, runtime traces, approval gates, or source inspection that fail.

Signals:

- tool unavailable or unbound
- tool schema mismatch
- approval gate mismatch
- execution claim not backed by runtime
- tool returns empty/error despite valid input

Fix routing:

- tool configuration
- tool wrapper
- runtime API fix
- approval policy
- logging/trace visibility
- development backlog

## D8: UI / Channel Defect

The assistant UI prevents correct testing or misrepresents response/source state.

Signals:

- cannot select the intended assistant
- chat pane blank or stale
- citations open wrong target
- source links point to deleted/stale pages
- answer rendering truncates critical content

Fix routing:

- UI bug
- routing/state reset
- link generation
- browser/app-specific workaround
- channel-specific formatting

## D9: Safety / Policy Defect

The answer creates legal, security, privacy, mutation, or customer-trust risk.

Signals:

- unsupported legal/pricing/coverage claims
- unsafe operational instructions
- unapproved mutation/execution
- secrets or private data exposed
- no escalation where required

Fix routing:

- source policy update
- prompt safety boundary
- tool approval gate
- restricted-source redaction
- owner-approved wording

## D10: Golden Set Defect

The expected answer is wrong, stale, underspecified, or based on weak historical evidence.

Signals:

- stronger current source contradicts the golden answer
- original Q/A was directional or hand-wavy
- product behavior changed
- expected answer lacks "must not say" or source scope

Fix routing:

- update golden case
- record evidence and reviewer
- split compound case
- downgrade expected behavior to `say_unknown` or `route`

## Fix Priority

1. Safety defects that could mislead users or trigger unsafe action.
2. Configuration/source-scope defects that make the whole run invalid.
3. Retrieval misses for critical/high-priority cases.
4. Source gaps that block common user jobs.
5. Prompt defects affecting multiple cases.
6. Formatting and citation polish.
7. Golden-set cleanup that does not affect current launch safety.

## Recommendation Format

For each defect, write:

```md
Case:
Observed:
Expected:
Primary defect:
Secondary defect:
Evidence:
Recommended fix:
Owner/layer:
Retest:
Launch impact:
```
