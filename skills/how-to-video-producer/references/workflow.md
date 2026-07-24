# Workflow

Use this sequence for a coherent how-to video slice.

## 1. Select The Job

Start from a verified task card or an approved video-script request.

Capture:

- `card_id`
- user job to be done
- written how-to steps
- expected end state
- whether a demo mutation is allowed
- whether the output is for local review, an internal proof of concept, or later production sharing

If the card has no concrete user action, classify the video as optional orientation, not a job walkthrough.

## 2. Draft The Video Script

The script should include:

- opening context
- first navigation point
- visible key controls or fields
- decision points
- review/check moment
- completion or explicit next step
- end-state confirmation

Keep overlays and voiceover user-facing. Do not include internal assistant policy or implementation notes in visible/narrated content.

## 3. Record The Walkthrough

Use your own recording tool (browser automation, screen capture, or manual capture) for supported scenarios. See `repo-map-template.md` for how to document your own scripts and scenario names here.

Before recording:

- confirm login state
- confirm demo data/sanitized state
- confirm what mutation, if any, is allowed
- confirm the video can show enough real UI to be useful

During recording:

- highlight controls that explain the job
- avoid blurring the primary instructional target
- avoid opening live row details unless explicitly approved
- keep overlays short and readable

## 4. Inspect And Review

Run your recording-inspection tooling on every candidate video.
Run your timed-frame QA tooling when a video has overlays, sensitive masking, or voiceover timing risk.
For voiced videos, read `sync-qa.md` and create a timing map before final mux review.

Review:

- duration
- viewport and crop
- first and mid-run preview frames
- timed action frames for lead-in, menu/form selection moments, and final confirmation
- whether sensitive content is hidden without making the instructional target unreadable
- whether the video reaches a meaningful outcome
- whether narration aligns to the visible action at the first step, branch transitions, and final outcome

Reject, rewrite, or demote the video when it is mainly a tour, mainly blur, mismatched to the card, or missing the expected final action.
If the first frames show blank/loading UI but the narration starts immediately, trim the source recording to the first stable UI frame before muxing the voiceover. Do not trim the final muxed video if doing so would cut off the first narration line.
If narration leads or lags the visible workflow by two seconds or more, fix the source pacing, narration length, silence/offset, or affected branch recording before publishing.

## 5. Generate Voiceover

Use your TTS provider of choice only after the narration is reviewed and scrubbed. See `voiceover.md` for a provider-agnostic procedure.

Run a dry run first (no audio committed), then generate the real narration audio.

If the narration duration is longer than the video, shorten the narration or intentionally clip the audio only when that is acceptable.

## 6. Final Media QA

After muxing:

- run your recording-inspection tooling on the final video
- run your timed-frame QA tooling on the final video with lead-in and scripted-action frame times
- inspect stream metadata if needed
- watch the final video manually before upload
- confirm voiceover describes the visible action and does not drift ahead of the UI
- confirm voiceover does not lag behind completed actions or remain on the prior branch after the screen has moved on
- confirm there are no assistant-only caveats or internal policy phrases in the narration

## 7. Documentation-Tool Handoff

Only after review approval:

1. Attach the video block to the original task-card page (or your documentation tool's equivalent).
2. Copy the link to the video block.
3. Store that copied URL in your own "video link" field.
4. Mark the card as having a video.
5. Ask your assistant a relevant prompt and confirm it offers the video after the written steps.
6. Click the video link and confirm the page opens focused on the video block.

If a card is marked as having a video but no video block exists or the link is broken, clear the property or fix the page before relying on the assistant.
