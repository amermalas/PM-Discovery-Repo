---
name: pm-sense
description: Use for Stage 1 (SENSE) of the 5-stage AI-enabled product management loop — building or refreshing a live market and competitor radar for a product bucket. Trigger on "market scan", "competitor radar", "what changed in the market for X", "weekly signal digest", "monthly market brief", or "competitor capability matrix". Produces a reviewed market brief with sourced, dated claims — not raw AI speculation.
---

# PM Sense — Stage 1: Build a live market radar

Part of a 5-stage operating loop (SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT) for using AI across the product management lifecycle, not just for one-off drafting. This stage keeps a current view of a product bucket's competitors, adjacent solutions, market shifts, buyer expectations, and relevant technology changes.

## Objective

Maintain a current, sourced view of the product bucket's competitive landscape — not a noisy news feed.

## Required inputs

- A defined product bucket, target users, core jobs-to-be-done, and known competitors.
- Approved public sources: release notes, product pages, help centers, earnings material, reputable news, analyst coverage, job postings.
- Any existing competitor dossiers or opportunity maps you already maintain — check these before starting new research so you extend rather than duplicate.

## What to do

1. Check whether this product bucket already has a competitor dossier or opportunity map on file. Extend, don't duplicate.
2. For a full competitive-analysis study (scored capability rubric, dossiers, opportunities/threats report) rather than a quick signal scan, hand off to `competitive-analysis-intelligence` — it already implements the scoring rubric and publishing format.
3. For a lighter weekly/monthly scan: separate observed facts from interpretation. Require a link, publication date, and the date the event occurred for every claim.
4. Deduplicate recurring items and compare against the prior report.
5. Write durable findings to the product bucket's knowledge base — do not leave intelligence trapped only in a chat session.
6. Flag claims about competitor capability or intent for human review before they become shared knowledge.

## Outputs (durable, not just chat)

- **Weekly signal digest**: what changed, why it may matter, what to investigate.
- **Monthly market brief**: patterns, strategic implications, open questions, recommended follow-ups.
- **Competitor capability matrix**: with source date, confidence, and last-verified date.

## Copy-ready prompt

> Every Monday, scan approved public sources for material changes affecting [product bucket]. Report only net-new developments since the previous run. For each item include: factual summary, source and date, affected user/job, likely significance, confidence, and a proposed PM follow-up. End with "no meaningful change" when appropriate.

## Review gate

Material claims are sourced, dated, and clearly separated from interpretation before they're treated as shared knowledge.

## Related repo resources

- `competitive-analysis-intelligence` — full scored competitive study workflow.

## Guardrails

Use only your organization's approved public sources. Do not paste client-owned or confidential material into research prompts. Label competitor-intent claims as inference unless directly sourced.
