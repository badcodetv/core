# Voices (AI Studio) and lip-sync: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.

## AI Studio TTS runs on a PAID key since 2026-09-30, so there is no 10-a-day free cap; never stop or wait a day for voice calls

The Gemini / AI Studio TTS key in `.env` (`GEMINI_API_KEY`) is a **paid key** (Kai's call, 2026-09-30; docs/ai-studio/README.md "UPDATE 2026-09-30"). The free tier's 10-calls-a-day-per-model cap does **not** apply. Keep only the ~22 s pacing between calls.

**Why:** On 2026-11-15 (Infinite Yous) I told Jack the day's voice calls were used up and offered "re-voice tomorrow", because the voice-casting skill still quoted the free cap. Jack: "why cant you use google ai studio, i thought that was paid for". He was right; 11+ calls that day had gone through with no 429. He asked me to remember it.

**How to apply:** when a voice needs re-recording (a retake, a faster read to fit a lip-sync, a new casting round), just render it. Never offer "wait for tomorrow" or ration takes for quota. A real 429 is the only evidence of a limit; check the key before believing any doc that says otherwise. The voice-casting skill was corrected the same day. Related: `narration-whole-blocks-never-trim-in-premiere`, `dubbed-talking-clips-recipe`.

## Placing narration on a timeline — cut one file per speaker block at word boundaries outside Premiere, place whole; never split at pauses or trim in Premiere.

When putting narration on a Premiere timeline, cut **one WAV per script block** (a speaker's whole
turn) at word boundaries found by transcription (faster-whisper word timestamps + an energy map),
keep every internal pause exactly, and place each file **whole** with `premiere_insert_clip`
overwrite — no in/out points.

**Why:** Jack, 2026-09-11, after the 2026-09-10 build split at every ≥0.45s pause (including commas),
squeezed pauses, and mislabelled a piece so wrong words played over the wrong shot: *"keep the full
sentences and only cut them when they are done speaking, do not cut mid sentence… keep small pauses
and make it sound natural."* Premiere's in/out trim actions are also unreliable (in-point moves the
clip; out-point origin reported wrong).

**How to apply:** match lines to the script + what the clips visibly show, not repo shot lists.
Transcribe every render before trusting any line label. Re-transcribe each cut file to prove it
starts/ends on whole words. If words don't fit the picture, ask — never shorten pauses to force it.
Record in `docs/stories/<story>/narration/timeline-build.md`. See `mark-unverified-claims-as-unverified`.

## Jack 2026-11-16 — don't install or use LatentSync (the lip-sync-dub skill's "redraw" lane): "it does not work

Jack, 2026-11-16 (True Scale, when asked whether to install it for lip sync): "dont install that lip syncing tool it does not work rememeber that please thanks".

Then: "you said you wanted to use the new tool for the lip syncing, do not do that, kai said that new one does not work. just use the skill we have been using for things like bank robbery story".

**Why:** Kai has judged it doesn't work for our clips (see `latentsync-oom-kills-wsl` for the earlier crash too).

**How to apply:** never offer or install LatentSync, even though the lip-sync-dub skill opens with it. Use the Bank Robbery method in that skill: re-shoot with the exact words, read mouth openings by eye from 12 fps mouth strips (mouth-track.py), place phrases with place-dub.py 0-0.1 s late, tempo 0.85-1.30. Never anchor on the clip's own audio or Whisper times (0.4 s early). For talking shots use the skill's other lanes: put the exact words in the Omni prompt so the mouth is drawn to them, size clips to the voice, fit the voice to the measured mouth; or keep the face off-screen/wide for that line. See `dubbed-talking-clips-recipe`.

## How to lip-sync a muted Flow talking clip to a TTS dub — Frames mode with the exact line, test, then time-warp to the clip's own speech; mouthless pans for failures.

Rule (worked out 2026-10-19 on Jack's Bank Robbery notes, "some are perfect and some completely messed around"):
1. Make every talking clip that will be dubbed in **Frames mode with the exact dub line in the prompt** (Ingredients improvises words).
2. **Test** each clip: its own speech must say the dub's words and sit on the moving lips (`scripts/bank-robbery/lips.py`, MediaPipe; ≥85% / correlation ≥0.5).
3. Passing clips: **time-warp the TTS onto the clip's own speech** (`dtwsync.py`, called by `ownsync()` in `build-short7.py`), plus the measured lag; err late.
4. Failing clips: never show the mouth — play the line over **mouthless café/detail pans** (Jack's idea), not a listener whose lips move.

**Why:** Omni's own audio and picture disagree on some clips; aligning to transcripts or lip runs alone left lines visibly off.
**How to apply:** any film where Flow talking clips are muted and dubbed (`narration-not-lipsync`, `bank-robbery-talking-clips-ingredients` — the latter's Ingredients advice is superseded for dubbed clips).

**Added 2026-10-19 (Karen 10b2):** `dtwsync.py warp` can squeeze a word away (*"fuck's"*) and sound robotic on long lines (heard on review). Fix that worked: `global` mode, or split the take at the clip's own on-screen pause and place each piece by a plain uniform stretch (0.85–1.15×) at the matching lip start. Check the dub alone with a transcriber, then the mix by ear or the listen tool.

**Added 2026-10-19 late (Karen 10b2, Jack: "the lip syncing does not line up"):** measure the mouth with `lips.py` FIRST, check the clip's own speech scores on it (0.58 here), then place the take phrase by phrase on the own-speech spans with even stretches, late-only slides, and check each phrase onset against the lip-run onset (+0.0–0.1 s late). The lip-motion correlation score is too blunt to judge sub-0.4 s offsets; trust onsets. Tool: `scripts/karen/tarquin-lipsync.py`.

**Added 2026-10-19 night (Karen review 8):** Omni's own audio was 0.45 s off its picture on the last line, so own-speech word times are NOT safe either; read lips.py's per-frame inner-lip gap (mouth shut ~0, open >0.02) around each phrase and place the dub on the visible opening. When TTS can't match a fast on-screen read without warble (>~1.3×), slow the PICTURE for that stretch (ffmpeg minterpolate mci, 0.75×) and trim a silent tail.

**Now a skill (2026-10-19): `.claude/skills/lip-sync-dub/` with `scripts/lipsync/mouth-map.py` and `place-dub.py`.** Superseded advice above: do NOT slow the picture (Jack: "weird"); a phrase too fast to match plays over a mouthless cutaway instead.
