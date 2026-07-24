# Repo Map Template

This skill assumes you will wire it to your own recording, QA, and voiceover tooling. Use this template to document those once, so the skill can point to concrete commands instead of generic prose.

Fill in for your own workspace:

```text
Recording tool / script: <e.g. a browser-automation recording script, or manual screen capture>
Recording output folder: <where raw recordings land>
Recording-inspection tool: <script or command that reports duration, dimensions, preview frames>
Timed-frame QA tool: <script or command that checks lead-in, sync, and action-frame clarity>
TTS provider + script: <see voiceover.md>
Mux tool: <e.g. ffmpeg command or wrapper script>
Documentation-tool handoff: <e.g. your knowledge-base's video-block or attachment pattern>
```

Keep this file local to your own fork if the concrete paths or commands are private; the public version of this skill intentionally ships without example values.
