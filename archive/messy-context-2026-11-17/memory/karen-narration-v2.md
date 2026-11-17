---
name: karen-narration-v2
description: "Karen narration v2→v4 (2026-10-19 to 22) — the narrator voice is in karen/sound.md; Karen v4 approved by Jack 2026-10-22; what is still owed"
metadata:
  type: project
---

Karen's narration moved to a new narrator voice on 2026-10-19 (Jack's pick; voice name, model and boxes in `docs/stories/karen/sound.md` and `narration/voice.md` Route B — [[no-house-style-story-files]]). The beat brief is `docs/stories/karen/narration/script-v2-brief.md`; Jack writes the lines ([[jack-writes-the-jokes]]). Why narration: [[narration-not-lipsync]].

**Jack's rulings (2026-10-19):** Act 5 cut; the ending is a silent clip of the sacked President ringing Karen, then "To be continued"; Susan is the friend who stays in bed and was also sacked by AI Sean; the AI is "AI Sean" (spell it `Ay-Eye Sean` for TTS); no beneficiary line in the film.

**State (2026-10-22):** sequence `Karen v4` in `Karen VID NEW!\Karen vid.prproj` (clone of `Karen v3 upload`): boss line n42, no static after AI Sean, Tarquin held back, ends on the President call + To be continued. Jack approved it; the laptop text was dropped. Ledger: `docs/stories/karen/shot-list.md` § 2026-10-22 ([[karen-resume-at-shot-list]]). Still owed: the 1,200-versions disclaimer; loudness (tick Loudness Normalization in Premiere's Export window).

**How to apply:** render with `scripts/aistudio-tts.py --voice <the voice in sound.md> --profile <Route B boxes>`; uv is not on PATH, so use a scratch venv with google-genai. Renders go to Jack's Desktop `Youtube Vids\animation\Karen\`. Export uploads from Premiere ([[export-from-premiere-not-ffmpeg]]).
