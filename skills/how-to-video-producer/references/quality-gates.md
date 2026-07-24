# Quality Gates

Use these gates before treating a video as publishable or attachable to a task card.

## Must Pass

- The video maps to a real user job, not only a list of UI areas to inspect.
- The viewer can tell what is being selected, reviewed, entered, saved, or confirmed.
- The video reaches a meaningful outcome: created draft, saved record, opened details, narrowed search result, reviewed form state, or confirmed row/status.
- The visible overlay and narration are directed to the user, not the AI assistant.
- The video does not rely on written overlay text alone while the UI is unusably blurred.
- The first narrated or overlay action starts after the product UI is loaded and stable; loading lead-in should be trimmed from the source video before voiceover muxing or covered by intentional silence.
- Narration and visible UI actions stay aligned within about one second at the first action, each major branch transition, and the final outcome.
- Timed review frames for each scripted action show the selected menu, button, field label, or form state clearly enough for the viewer to follow the job.
- User-visible field values look like realistic fictional workflow data, not a literal recorder-tool name, "demo name", "test record", or other placeholder text.
- Any save/create/submit behavior matches an approved demo fixture or explicit user approval.
- The written task card already covers the user-facing steps shown or narrated.

## Reject Or Rewrite

Reject, rewrite, or demote the video when:

- sensitive blur covers the main action for most of the run
- the first seconds show blank/loading UI while the narration is already explaining a loaded screen
- the voiceover leads or lags the visible workflow by two seconds or more at a major action or branch transition
- a scripted action frame is too blurred to see what the overlay means
- the video is a dashboard tour with no user outcome
- the narration says to stop before save when the user-facing how-to should include save/create/submit
- the video shows a different job than the linked card
- a card is marked as having a video but no actual same-page video block exists
- the documentation-tool video link opens the top of the card instead of focusing the video block
- the content exposes live customer data, credentials, raw IDs, sensitive notes, or unapproved row details

## Voiceover Criteria

- Narration should be shorter than or close to the video duration.
- Narration should describe the visible workflow, not the project history.
- Narration should be timed to visible step beats; if it drifts, fix the source recording, script pacing, or audio offset before publishing.
- Avoid implementation phrases: "blocked", "pressure test", "tool test", internal platform names, "approval gate", "wrapper", "agent instructions".
- Use product-training language: "choose", "review", "confirm", "save the draft", "open the record".

## Sensitivity Criteria

- Prefer demo fixture data over blur.
- Use blur or shielding only where it protects sensitive lists, feed content, names, images, or row data.
- Do not blur the selected menu, form label, button, or status that teaches the user what to do.
- Reviewed mock data can stay visible when it is needed to teach the user and has been reviewed as acceptable; use targeted masks instead of full-screen blur.
- Treat generated previews and muxed outputs as restricted until separately approved.

## Recording Learnings Log

Keep a running internal log of what has and hasn't worked for your own video library — for example, which pattern was strongest for a given workflow, which recordings failed QA because of sync or over-masking, and what the fix was. This reference file intentionally ships without example entries; start your own log here as you produce videos, and do not include real internal project names or customer-identifying details even in an internal log.
