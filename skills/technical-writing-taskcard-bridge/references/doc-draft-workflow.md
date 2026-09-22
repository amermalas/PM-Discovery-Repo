# Task-Card Docs Drafting Workflow

Use this workflow to draft a user-guide page from verified task-card clusters that are not yet well represented in technical-writing docs.

## Inputs

- One verified task-card cluster or a bounded product area.
- Existing documentation pages to use as style and structure references.
- Optional screenshots or videos captured from an authenticated browser session.

## Procedure

1. Define the page job.
   - Identify audience: customer-facing user, internal implementation, admin, support, or technical writer review.
   - State whether the page is a draft, sample, or publish-ready candidate.
2. Select card scope.
   - Group cards into a coherent page-level workflow.
   - Merge supporting details into sections instead of creating a page per small card.
   - Exclude candidate/unverified cards unless clearly marked as reviewer notes.
3. Mirror the documentation pattern.
   - Inspect comparable technical-writing pages for heading order, tone, prerequisite style, related-links style, and media placement.
   - Keep the page user-facing; move task-card lineage, uncertainty, and owner-review notes to the bottom or a separate reviewer section.
4. Draft the page.
   - Start with a short purpose statement.
   - Include "Before you start" for permissions, source data, tenant-specific setup, and prerequisites.
   - Provide complete steps through the user-visible outcome, including save/submit/publish when that is the normal manual path.
   - Add expected results and validation checks after important actions.
   - Add "Limits and notes" only for details that help the user act safely.
5. Handle visuals.
   - Capture screenshots only from approved demo/sandbox contexts.
   - Avoid sensitive data, secrets, customer names, raw identifiers, and internal notes.
   - If a video exists, link or embed it as supplemental help after the written steps, not as a replacement.
   - If upload/embed fails, provide exact local file paths and manual placement notes.
6. Add reviewer notes.
   - List source task cards and verification artifacts.
   - Call out any browser-proof, owner-review, screenshot, video, or publication gaps.
   - Make review needs explicit before a draft is treated as customer-facing documentation.

## Suggested Page Structure

1. Draft status / reviewer note.
2. What this page covers.
3. Before you start.
4. Main workflow sections with numbered steps.
5. Expected results / validation checks.
6. Related configuration or admin dependencies.
7. Limits, gotchas, or owner-review areas.
8. Related pages.
9. Source notes for reviewers.

## Boundaries

- Do not include execution-tool readiness, internal platform implementation gaps, or assistant-only guardrails in the user-facing body.
- Do not create customer-facing legal, source-coverage, roadmap, or entitlement claims from task cards unless the owner-approved wording is already present.
- Do not mutate live documentation unless the user explicitly asks to create or update the page.
