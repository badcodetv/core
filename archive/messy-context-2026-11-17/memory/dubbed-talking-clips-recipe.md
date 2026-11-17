---
name: dubbed-talking-clips-recipe
description: How to lip-sync a muted Flow talking clip to a TTS dub — Frames mode with the exact line, test, then time-warp to the clip's own speech; mouthless pans for failures.
metadata:
  type: project
---

Rule (worked out 2026-10-19 on Jack's Bank Robbery notes, "some are perfect and some completely messed around"):
1. Make every talking clip that will be dubbed in **Frames mode with the exact dub line in the prompt** (Ingredients improvises words).
2. **Test** each clip: its own speech must say the dub's words and sit on the moving lips (`scripts/bank-robbery/lips.py`, MediaPipe; ≥85% / correlation ≥0.5).
3. Passing clips: **time-warp the TTS onto the clip's own speech** (`dtwsync.py`, called by `ownsync()` in `build-short7.py`), plus the measured lag; err late.
4. Failing clips: never show the mouth — play the line over **mouthless café/detail pans** (Jack's idea), not a listener whose lips move.

**Why:** Omni's own audio and picture disagree on some clips; aligning to transcripts or lip runs alone left lines visibly off.
**How to apply:** any film where Flow talking clips are muted and dubbed ([[narration-not-lipsync]], [[bank-robbery-talking-clips-ingredients]] — the latter's Ingredients advice is superseded for dubbed clips).

**Added 2026-10-19 (Karen 10b2):** `dtwsync.py warp` can squeeze a word away (*"fuck's"*) and sound robotic on long lines (heard on review). Fix that worked: `global` mode, or split the take at the clip's own on-screen pause and place each piece by a plain uniform stretch (0.85–1.15×) at the matching lip start. Check the dub alone with a transcriber, then the mix by ear or the listen tool.

**Added 2026-10-19 late (Karen 10b2, Jack: "the lip syncing does not line up"):** measure the mouth with `lips.py` FIRST, check the clip's own speech scores on it (0.58 here), then place the take phrase by phrase on the own-speech spans with even stretches, late-only slides, and check each phrase onset against the lip-run onset (+0.0–0.1 s late). The lip-motion correlation score is too blunt to judge sub-0.4 s offsets; trust onsets. Tool: `scripts/karen/tarquin-lipsync.py`.

**Added 2026-10-19 night (Karen review 8):** Omni's own audio was 0.45 s off its picture on the last line, so own-speech word times are NOT safe either; read lips.py's per-frame inner-lip gap (mouth shut ~0, open >0.02) around each phrase and place the dub on the visible opening. When TTS can't match a fast on-screen read without warble (>~1.3×), slow the PICTURE for that stretch (ffmpeg minterpolate mci, 0.75×) and trim a silent tail.

**Now a skill (2026-10-19): `.claude/skills/lip-sync-dub/` with `scripts/lipsync/mouth-map.py` and `place-dub.py`.** Superseded advice above: do NOT slow the picture (Jack: "weird"); a phrase too fast to match plays over a mouthless cutaway instead.
