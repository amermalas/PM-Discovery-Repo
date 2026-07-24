# Sync QA

Use this reference whenever a how-to video has narration, overlays, loading time, or scripted step timing.

## Required Checks

- The first spoken instruction must begin only after the product screen for that step is loaded and stable.
- The narrated action should match the visible action within about one second. A lag or lead of two seconds or more is a rewrite or remux issue.
- Each major narration beat should have a matching visible UI state: menu opened, field selected, value entered, form reviewed, submit clicked, or resulting record shown.
- The final narration should not keep explaining a previous screen after the video has moved on to another workflow branch.
- The audio duration should be close to, but not longer than, the usable video duration unless intentional silence or outro time is planned.

## Review Procedure

1. Inspect the source video before muxing.
   - Confirm the first stable UI frame.
   - Trim blank loading lead-in from the source recording before adding voiceover.
   - Keep a short visual lead-in only when narration is intentionally delayed.

2. Create a timing map.
   - List the expected seconds for major steps.
   - Include the first loaded screen, the first menu/form action, each branch transition, and the final outcome.
   - Use these times as input to your own timed-frame QA tooling.

3. Mux voiceover.
   - If the voiceover starts too early, trim the source recording or add intentional silence before narration.
   - If the voiceover lags behind, shorten narration or slow the visual pacing by adding holds at the relevant action states.
   - If only one branch is out of sync, fix the source script timing rather than globally shifting the whole audio track.

4. Run final QA.
   - Run your recording-inspection tooling on the final video.
   - Run your timed-frame QA tooling with the narration script and step timing map.
   - Manually review the final video at normal speed and spot-check the timing map frames.

## Failure Patterns

- Audio explains a loaded screen while the video is still loading.
- Audio names a menu before the menu is visible.
- Audio describes field entry after the field was already filled several seconds earlier.
- Audio describes a save/review outcome before the confirmation or record view appears.
- A multi-branch walkthrough switches branches while narration is still explaining the prior branch.

## Fix Patterns

- Trim the source video to the first stable UI frame before muxing.
- Add a deliberate silent pad before narration when the video needs visual context first.
- Shorten narration for fast UI sections.
- Add short visual holds on important menus, forms, or outcomes.
- Re-record only the branch that is out of sync when the rest of the video is sound.
