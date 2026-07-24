---
name: how-to-video-producer
description: Use when asked to create, revise, record, QA, voice over, mux, or prepare a supplemental product how-to video from a verified task card or reviewed video script, including screen-recording capture, timed-frame QA, sensitive-data masking review, TTS narration, muxing, and handoff to a documentation or knowledge-base tool.
---

# How-To Video Producer

Use this skill to turn a verified task card or reviewed video script into a publishable supplemental how-to video artifact.

The written task card remains the source of truth. Videos are supplemental visual walkthroughs. Do not let a video introduce steps, claims, or safety language that are not represented in the verified written card or approved demo script.

## Use This Skill When

- creating or revising how-to video scripts from task cards
- planning or recording product walkthroughs with a browser-automation or screen-capture tool
- checking whether a video is too blurred, too tour-shaped, or missing a meaningful job outcome
- running timed-frame QA to catch loading lead-in, voiceover drift risk, low-clarity action frames, and assistant-only narration phrases
- generating TTS narration
- muxing voiceover audio into video with a media tool such as ffmpeg
- preparing a reviewed video for handoff into a documentation tool or knowledge base

## Hard Boundaries

- Never print API keys, auth headers, storage-state contents, cookies, or bearer tokens.
- Do not upload or link a video anywhere outside local review unless the user explicitly asks for that step after review.
- Do not mutate a shared or production demo environment unless an approved fixture or explicit mutation-safe path is in scope.
- Do not show assistant-only guardrails in overlays or narration. Avoid phrases such as "blocked", "approval gate", "stop before saving", "tool test", or internal platform/tool names in user-facing video content.
- Do not use generic recorder/placeholder naming (such as a literal tool name, "demo name", or "test record") in user-visible fields, overlays, or narration. Use realistic fictional training names that match the workflow instead.
- Do not publish a video that is mostly blur, a UI tour without a job outcome, mismatched to the card, or not backed by written card content.
- Treat all local recordings, previews, voiceovers, and muxed outputs as restricted until separately approved.
- Do not include private company names, ticket IDs, internal platform names, customer names, local file paths, or proprietary examples in public outputs.

## Required Workflow

1. Identify the card/job.
   - Confirm the card ID, user job, source written steps, and expected outcome.
   - If the card is conceptual or guardrail-only, produce written guidance or a short orientation clip only if that is useful.

2. Write or revise the script.
   - Use user-facing training language.
   - Show a coherent workflow: start point, key choices, review moment, and end state.
   - Use realistic fictional training values in visible form fields and overlays; keep "demo fixture" language only in internal reviewer notes.
   - Keep save/create/submit language aligned with the written card. Videos may use demo fixtures even when the agent itself is informational-only.

3. Record when needed.
   - Read `references/repo-map-template.md` for how to adapt this step to your own recording tool and scenario names.
   - Prefer controlled demo data and visible UI labels over heavy blur.
   - Capture review frames and metadata.

4. QA the recording.
   - Read `references/quality-gates.md`.
   - Read `references/sync-qa.md` when the video has voiceover, overlays, loading time, or step timing risk.
   - Run a timed-frame QA pass for lead-in and action-target checks whenever the video has overlays, masking, or voiceover timing risk.
   - Reject or rewrite videos that are over-masked, too generic, or do not complete a meaningful job.

5. Add voiceover when requested.
   - Read `references/voiceover.md`.
   - Use `references/sync-qa.md` to align narration starts, step beats, and final outcome timing.
   - Use reviewed narration text only.
   - Generate narration audio through your chosen TTS provider and mux with a media tool such as ffmpeg.
   - Re-run timed-frame QA on the final muxed output before upload or linking.

6. Prepare delivery.
   - If the target is a documentation tool or knowledge base with a page-level video block, attach the video to the original task-card page, copy the block link, store it in your own "video link" field, and mark "has video" only after the video exists and opens at the right place.
   - Record all changes in the appropriate backlog/eval/governance docs.

## References

- `references/repo-map-template.md` - a template for listing your own recording scripts, commands, output folders, and documentation-tool integration
- `references/workflow.md` - detailed stage-by-stage production workflow
- `references/quality-gates.md` - quality, sensitivity, and rejection criteria
- `references/sync-qa.md` - audio/video sync, lead-in trimming, and step-beat review procedure
- `references/voiceover.md` - TTS and mux procedure, provider-agnostic

## Output Contract

A completed slice should leave behind:

- script or narration source text
- source recording or existing video lineage
- review frames or preview images
- timed-frame QA report when applicable
- optional voiceover audio
- final muxed video artifact
- QA notes with pass/fail status
- governance/task-log update when the workflow, outputs, or publication state changes
