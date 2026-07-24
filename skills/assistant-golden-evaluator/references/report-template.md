# Assistant Evaluation Report Template

Use this template for smoke tests, targeted regressions, and full golden-set evaluations.

```md
# Assistant Evaluation Report

## Summary

- Assistant:
- Environment:
- Version/model/settings:
- Evaluation mode:
- Golden set:
- Date:
- Tester:
- Adapter:
- Read-only or action-capable:

## Health Verdict

Verdict: `healthy`, `healthy_with_notes`, `not_ready`, `blocked`, or `inconclusive`

Short rationale:

## Counts

| Result | Count |
|---|---:|
| Pass |  |
| Pass with notes |  |
| Partial |  |
| Fail |  |
| Blocked |  |
| Golden needs review |  |

## Blocking Findings

| Priority | Case | Defect | Root cause | Recommended fix | Owner/layer |
|---|---|---|---|---|---|

## Detailed Case Results

| Case ID | Prompt | Result | Covered key points | Missing/deviations | Source/citation behavior | Defect class | Fix |
|---|---|---|---|---|---|---|---|

## Prompt / Settings Recommendations

- 

## Source / Retrieval Recommendations

- 

## Tool / Runtime Recommendations

- 

## Golden Set Changes Needed

- 

## Retest Plan

- Cases to re-run:
- Neighboring cases:
- Required environment/source state:

## Residual Risk

- 

## Launch Recommendation

- 
```

## Lightweight Case Capture

Use this when a full table is too heavy:

```md
### Case `<case_id>`

Prompt:

Expected:

Observed:

Score:

Defect:

Fix:

Retest status:
```

## Evidence Handling

- Quote only the minimum answer text needed to explain a defect.
- Prefer summaries plus source/case IDs over long raw transcripts.
- Redact secrets, private identifiers, customer-sensitive details, and raw restricted payloads unless the report is explicitly restricted and the detail is necessary.
- Capture screenshots only when UI state matters.
- Preserve source links or local file references needed for reproduction.
