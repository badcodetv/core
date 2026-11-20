# Voices (AI Studio) and lip-sync: standing rules
> Moved out of Claude's per-machine memory on 2026-11-17 (the context reset) so both Kai and Jack have them.
> Mechanics and working habits only: no look or sound belongs here (that lives in a story's `badcode.md`).
> Originals: `archive/messy-context-2026-11-17/memory/`.

## AI Studio TTS runs on a PAID key since 2026-09-30, so there is no 10-a-day free cap; never stop or wait a day for voice calls

The Gemini / AI Studio TTS key in `.env` (`GEMINI_API_KEY`) is a **paid key** (Kai's call, 2026-09-30; docs/ai-studio/README.md "UPDATE 2026-09-30"). The free tier's 10-calls-a-day-per-model cap does **not** apply. ~~Keep only the ~22 s pacing between calls.~~
**No pacing (Jack, 2026-11-20):** the 22 s gap was the free tier's 3-requests-a-minute limit, carried over after the key
became paid. Run voice calls **in parallel**: four at once came back in 2 s with no 429 (2026-11-20). `scripts/aistudio-tts.py`
waits and retries by itself on a real 429 (20, 40, 60 s).

**The script sets itself up (2026-11-20):** it reads `GEMINI_API_KEY` from the repo's `.env` and re-runs under
`~/.venvs/genai` when `google-genai` isn't importable, so a bare `python3 scripts/aistudio-tts.py …` works from any shell.
Styled takes (`--style`) now write a recipe card too. Whisper (`~/.venvs/whisper`) needs `av<16`: av 19 broke
faster-whisper 1.2.1's file decode (`metadata_errors`); pinned 2026-11-20.

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

**How to apply:** never offer or install LatentSync, or any tool that redraws the mouth. Use the method at the top of the lip-sync-dub skill (2026-11-18, below): the whole voice take, re-voiced with pause tags to the clip's pauses, ranked by words in time. Put the exact words in the Omni prompt, size clips to the voice, never chop the take, never speed the picture; or keep the face off-screen/wide for that line.

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

---

# From Kai's machine memory (moved 2026-11-18)

> Kai's per-machine memory was archived to `archive/messy-context-2026-11-17/memory-kai/` on 2026-11-18.

## Lip-sync a Flow talking clip with flow-align.py (Kai, 2026-11-11) [flow-lipsync-not-latentsync]

Kai on LatentSync: "is not her actual natural mouth… regenerate in Flow". Omni's own audio is 0.45-0.7 s off its
picture, so never place a dub on Flow's audio or Whisper times.
- Make the clip in Flow with the spoken line in the prompt, paced to our voice take (starts ~0.5 s in, says it once,
  mouth shuts). Face front or three-quarter. Roll 2+ takes.
- On each take run `~/.cache/badcode-lips/venv/bin/python scripts/lipsync/flow-align.py <clip> <voice.wav> <out-dir> <name>`:
  it measures the mouth, places the voice phrase by phrase, eases the picture ≤12% and prints before/after offsets.
  Pick the take whose runs all land within −0.05 / +0.13 s.
- If none does, the line is heard over another shot (side-on talking is always off screen).
- Several Flow jobs sharing one start plate get their tiles mixed up: one job per plate per run.

## Jack 2026-11-18: voices must sound like real people, not performances ("uncanny valley… the accent is crazy")

Jack, on two casting rounds for Hello, I'm BadCode: "they've been sort of triggering Uncanny Valley… really exaggerated… they
sound realistic when they're subtle… they just don't sound like real people." Then: "research how to do this for Google AI
Studio specifically… check the prompts… something in the repo polluting it."

**Cause (found 2026-11-18):** we were doing what Google's current docs say not to do. We used the 30 basic voices (none of
them British) and forced an accent, an age and a personality through the prompt, on an old preview model
(`gemini-3.1-flash-tts-preview`) with a long prompt wrapper. The first fix attempt copied another story's narrator note,
which is itself pollution (a story's recipe is that story's).

**Google's method** ([speech generation](https://aistudio.google.com/docs/speech-generation), [voice design](https://aistudio.google.com/docs/voice-design)):
- **Model `gemini-3.8-flash-tts`** (GA; our key has it). The 3.1 preview is the old one.
- **The accent comes from the voice, never the prompt.** "Avoid putting age, gender, names, or permanent accent changes in
  `style`… pick a regional voice from the Extended Voice Library or create one with Voice design." The library has 2,140
  voices, 117 of them British (Manchester, Liverpool, Newcastle, Glasgow, Bristol, Winchester), ids like `en-gb-tutor-8`;
  list them with `GET /v1beta/voices` (they carry age, accent and a description).
- **"Test plain TTS first":** the transcript alone, empty style. "Most requests need no style." Add a short style
  (`"casual, friendly"`) only for a line that needs it.
- **Write the transcript as real speech:** contractions, commas, dashes, ellipses, the odd hesitation.
- **Voice design** makes a reusable `voice_…` from a 1-2 sentence description, when no library voice fits
  (`POST /v1beta/voices`, `type: prompted`, `language_code: en-GB`; the id then works as `--voice`). Jack, 2026-11-18: the
  library's British voices sounded "posh and too high pitched" (they're cast as lawyers, advisers, presenters); for an
  ordinary voice, design one: who, where from, low voice, speaks plainly. One sentence, nothing about performing.

**How to apply:** casting = pick 4-6 library voices by their metadata (region, age, gender), render each plain on 3.8
(`scripts/aistudio-tts.py --plain --model gemini-3.8-flash-tts --voice en-gb-…`), then let Jack or Kai pick. No accent or
personality adjectives in any prompt. Never copy another story's voice note or profile.
Trim take silence gently (`silenceremove` at -55 dB, 0.12 s): -45 dB cut a soft "I'm" off a line.


## Kai 2026-11-18 — the lip-sync breakthrough: re-voice to the clip with pause tags

Kai, on GPOM scene A round 3: *"the lip-syncing is much better… a magnificent improvement… in every case, the lips and the
voice lined up… whatever that breakthrough is, document it throughout the repository."*

**What it was:** a per-word table (each word's start against the clip's own word, window 45 ms early to 125 ms late)
showed lines were off because a pause sat in a different place, not because of speed. Re-voicing the SAME words with
Gemini's `<short pause>` / `<long pause>` tags (or a comma to shorten a pause) at the spots where the clip pauses, then
ranking every take × clip by words inside the window, took line 7-2 from 2/12 words in time to 10/12, 7-0 from 5/11 to
9/11. Procedure: the top of `.claude/skills/lip-sync-dub/SKILL.md`. Record: `docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/lipsync-2026-11-18.md`.

**Why:** Flow takes no audio and Omni sets its own rhythm, so a voice made blind to the clip can only be slid and evenly
stretched, which never moves a pause. Moving the pause in the voice can.

**How to apply:**
- Every dubbed talking line: clips first, per-word table, re-voice with pause tags, rank by words in time, picks page.
- Tags only, never new words ("words change only with Kai/Jack").
- **Kai picks by voice as well as sync**: takes vary a lot in sound. Keep every take on the character's locked model and
  profile; show the pairs that are in time and let him choose the one that sounds like the character.
- Gemini 3.8 with a long profile sometimes reads the profile aloud (4 of 18 takes, 2026-11-18): fail any take whose
  transcript is longer than its line.

## A short style for one line on 3.8 goes in speech_metadata.style, never in the text (2026-11-19, Priority Lane)

A "Say angrily: …" prefix is SPOKEN on `gemini-3.8-flash-tts` (all four test takes read it out). Google's 3.8 docs: the
text is a verbatim transcript; turn-level delivery goes in `speech_metadata.style`, momentary sounds inline in angle
brackets (`<shout>`, `<gasp>`, `<short pause>`). The google-genai SDK has no field for it, so `scripts/aistudio-tts.py
--plain --style "angry, shouting"` sends it through `POST v1beta/interactions` (text part + `speech_metadata` annotation).
Use it only for a line that needs it (Jack: "this needs to be said angrily"), a few words, never an accent or persona.
