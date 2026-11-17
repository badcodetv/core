---
name: ai-studio-key-is-paid-no-daily-cap
description: "AI Studio TTS runs on a PAID key since 2026-09-30, so there is no 10-a-day free cap; never stop or wait a day for voice calls"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e089ca24-c90e-4348-bade-c8259060c7db
  modified: 2026-11-15T12:15:25.297Z
---

The Gemini / AI Studio TTS key in `.env` (`GEMINI_API_KEY`) is a **paid key** (Kai's call, 2026-09-30; docs/ai-studio/README.md "UPDATE 2026-09-30"). The free tier's 10-calls-a-day-per-model cap does **not** apply. Keep only the ~22 s pacing between calls.

**Why:** On 2026-11-15 (Infinite Yous) I told Jack the day's voice calls were used up and offered "re-voice tomorrow", because the voice-casting skill still quoted the free cap. Jack: "why cant you use google ai studio, i thought that was paid for". He was right; 11+ calls that day had gone through with no 429. He asked me to remember it.

**How to apply:** when a voice needs re-recording (a retake, a faster read to fit a lip-sync, a new casting round), just render it. Never offer "wait for tomorrow" or ration takes for quota. A real 429 is the only evidence of a limit; check the key before believing any doc that says otherwise. The voice-casting skill was corrected the same day. Related: [[narration-whole-blocks-never-trim-in-premiere]], [[dubbed-talking-clips-recipe]].
