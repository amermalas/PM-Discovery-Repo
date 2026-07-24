# Voiceover

Use this reference when adding TTS narration to reviewed how-to videos.

## Provider

This workflow is provider-agnostic. Wire it to whichever TTS API you use (for example, a cloud TTS/text-to-speech API). Whatever you choose:

- read the API key from a local env file, never hard-coded
- send only reviewed narration text
- prefer a "do not store/log" option if the provider offers one
- write a standard audio format (for example, mono WAV) that your mux tool accepts
- use a media tool such as ffmpeg to mux audio with video

## Required Safety

- Never print the API key.
- Do not send raw task-card internals, chat/support content, customer data, or live UI text unless it has been reviewed and approved for narration.
- Keep narration user-facing.
- Do not upload generated media automatically.

## Suggested Command Shape

Adapt these to your own tooling; the pattern is the important part.

Dry run (no audio generated, just validates inputs):

```bash
your-tts-tool --dry-run --script <narration.txt> --input-video <video-file>
```

Generate audio and mux:

```bash
your-tts-tool --script <narration.txt> --input-video <video-file>
```

Generate audio only:

```bash
your-tts-tool --skip-mux --script <narration.txt> --input-video <video-file>
```

Mux an existing audio file:

```bash
your-tts-tool --skip-tts --audio-input <voiceover-audio> --input-video <video-file>
```

## Output Review

After generation, run your inspection and timed-frame QA tooling and check:

- video duration and dimensions
- generated preview frames
- audio duration versus video duration
- whether voiceover timing matches visible action
- whether voiceover leads or lags the visible action by two seconds or more at first action, branch transitions, or final outcome
- whether the first narration starts after the UI is loaded; if not, trim the source video before muxing instead of cutting the first seconds from the final voiced output
- whether scripted action frames are readable without broad blur covering the target control
- whether any internal guardrail wording was spoken

For any sync concern, read `sync-qa.md` and create a timing map before remuxing.

Use ffmpeg (or your media tool's equivalent) stream inspection when you need to confirm codec, duration, or channel details on the final file.
