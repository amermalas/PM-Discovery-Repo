---
name: source-intake
description: Use when a PM wants to add their own research notes, customer interviews, tickets, surveys, docs, call transcripts, support notes, sales notes, or product knowledge into a public-safe PM discovery repo. Produces structured source cards, use rules, summaries, extraction recommendations, and sensitivity notes without assuming the source is safe to publish.
---

# Source Intake

Use this skill to turn a messy source into a governed discovery input.

The job is not to analyze the source fully. The job is to decide what it is, how it may be used, what should be extracted, and what safety boundaries apply.

## Inputs

- source file, note, transcript, ticket export, survey, product doc, or URL summary
- source owner or team, if known
- original system, if known
- intended discovery use
- public, internal, or restricted sharing goal

## Workflow

1. Identify the source family: customer feedback, interview, ticket, survey, product doc, internal note, market research, beta feedback, or other.
2. Classify sensitivity conservatively.
3. Separate raw source from derived summary.
4. Extract a short neutral summary.
5. Identify useful downstream extraction targets:
   - evidence items
   - product taxonomy candidates
   - workflow steps
   - user roles
   - painpoint candidates
   - direct quotes or snippets, if allowed
6. State allowed consumers and unsafe uses.
7. Produce a source card.

## Output Contract

Return a source card with:

- source id
- title
- source family
- source owner
- original system
- local path or placeholder path
- sensitivity
- raw or derived status
- allowed uses
- unsafe uses
- refresh expectation
- public release status: not_public, public_safe_after_review, or public_safe_now
- summary
- extraction recommendations
- downstream skills to run next

## Hard Boundaries

- Do not assume raw customer content is public-safe.
- Do not paste long source excerpts unless the user explicitly asks and the source is safe.
- Do not treat a summary as source truth.
- Do not normalize or rank painpoints in this skill; hand off to `customer-evidence-normalizer` or `painpoint-validation`.
