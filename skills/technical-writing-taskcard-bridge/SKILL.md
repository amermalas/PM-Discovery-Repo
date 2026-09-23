---
name: technical-writing-taskcard-bridge
description: Use when comparing your documentation platform's technical-writing pages against verified task cards, producing docs drift audits, identifying doc-only task-card candidates, finding verified-card clusters missing from docs, or drafting user-guide pages from verified task-card clusters with reviewer notes, screenshots, videos, and owner-validation caveats.
---

# Technical Writing Task-Card Bridge

## Overview

Use this skill to bridge verified task-card knowledge into technical-writing maintenance. It supports two related modes: auditing existing docs against verified cards, and drafting new documentation pages from verified task-card clusters.

This skill does not replace `task-card-knowledge-builder`. Use that skill first when source findings still need candidate disposition, source/code/browser verification, promotion, or runtime export.

## Mode Selection

1. Use **Docs Drift Audit** when the user asks whether existing technical-writing docs are outdated, incomplete, inconsistent with task cards, or missing coverage.
   - Read `references/drift-audit-workflow.md`.
2. Use **Task-Card Docs Drafting** when the user asks to create a sample docs page, user guide, or technical-writing page from verified task cards.
   - Read `references/doc-draft-workflow.md`.
3. Read `references/output-templates.md` when producing a shareable report or draft page.

## Evidence Rules And Hard Boundaries

- Treat verified task cards and their verification artifacts as the stronger internal knowledge layer for how-to behavior.
- Treat existing docs, internal Q&A, browser observations, and generated summaries as evidence to compare or ingest, not as final task-card truth.
- Phrase doc-drift findings as suggested review items unless code/browser/owner evidence proves the issue.
- Keep task-card exports as the source of truth. Doc drafts, reports, and screenshots/videos are delivery artifacts.
- Do not publish, update, or delete live documentation pages unless the user explicitly authorizes a live mutation.
- Preserve sensitivity: these artifacts are internal/restricted unless an owner explicitly approves broader sharing.

## Tooling

- Use your documentation platform's own tools (whatever wiki/docs system you use) when the user asks to inspect or update live pages.
- Use local repo artifacts when the user references prior audits, generated draft pages, task-card runtime exports, or QA files.
- Use an in-app browser for screenshot or video capture only when the user asks for visual proof or page assets and the authenticated target is already available.
- If a video or screenshot cannot be embedded directly, produce an asset manifest with exact local paths and clear manual placement notes.

## Output Contract

For a docs drift audit, return:
- suggested review items against existing docs
- doc-only candidate task-card intake items
- verified task-card clusters that appear underrepresented in docs
- evidence/proof strength and owner-review needs

For a docs draft, return:
- a publish-ready markdown draft
- reviewer notes and assumptions
- related task-card/source lineage
- asset manifest for screenshots/videos
- unresolved owner-review or browser-verification gaps
