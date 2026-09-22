# Docs Drift Audit Workflow

Use this workflow to compare an existing technical-writing documentation scope against verified task cards.

## Inputs

- Documentation root page, page list, export bundle, or local markdown folder.
- Verified task-card export or local QA artifacts that identify card IDs, user jobs, steps, caveats, validation status, and source lineage.
- Optional scope constraint such as one program, feature family, admin area, or release.

## Procedure

1. Establish the audit scope.
   - Record the documentation root URL/page ID, included descendants, excluded pages, and task-card bundle used.
   - If the scope is broad, sample first by high-risk/high-traffic pages and obvious task-card clusters.
2. Pull the docs corpus.
   - Prefer live descendant/page fetches when live access is requested.
   - Use local markdown snapshots when the user points to repo artifacts.
   - Keep raw page text restricted and avoid copying long bodies into the final report.
3. Build a comparison map.
   - Normalize page titles, headings, feature names, card titles, aliases, and user jobs.
   - Match by user job first, then product area, then feature labels.
   - Keep ambiguous matches in an `owner_check` bucket.
4. Identify suggested drift.
   - Docs appear to conflict with verified task-card steps.
   - Docs omit material prerequisites, limits, caveats, permissions, or save/submit end states.
   - Docs describe UI labels or workflows that task-card/browser evidence suggests may have changed.
   - Docs include placeholder/TBD/outdated sections or screenshot-only instructions without durable steps.
5. Identify doc-only candidate intake.
   - Capture docs-only workflows that look like user jobs but do not map to verified cards.
   - Classify each as `candidate_card`, `step_or_detail`, `guardrail_only`, `reference_only`, or `needs_owner_review`.
   - Route actual promotion and verification back through `task-card-knowledge-builder`.
6. Identify task-card-only documentation opportunities.
   - Find verified card clusters that have no clear equivalent technical-writing page.
   - Group them by likely docs page or section, not one page per card by default.
7. Write the report as suggestive.
   - Use phrasing such as "suggested review item", "appears underrepresented", and "to check with owners".
   - Do not state that documentation is wrong unless the report includes direct source/code/browser/owner proof.

## Recommended Checks

- Search for placeholders: `TBD`, `TODO`, `PENDING`, `CHECK`, `old`, `legacy`, `v1`, `edit-v2`.
- Search for incomplete user outcomes: steps that stop before `Save`, `Submit`, `Activate`, `Publish`, `Upload`, or `Review`.
- Search for assistant-internal language in user docs: `blocked`, `tool`, `AI assistant`, `guardrail`, `owner-approved` when not user-facing.
- Search for source-only language that belongs in reviewer notes, not user steps.

## Output Shape

Use `references/output-templates.md` for the report skeleton. Keep findings concise enough that technical writers can triage them without reading the full task-card corpus.
