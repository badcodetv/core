---
name: lip-sync-dub
description: Use when a Flow (Omni) talking clip is muted and dubbed with an AI Studio text-to-speech voice and the lips must line up — making the talking clip, measuring the mouth, placing the voice phrase by phrase, choosing a cutaway when it can't match, and checking the result. Triggers on "lip sync", "the lips don't line up", "dub this clip", "make him say the line", "the voice is early/late", "his mouth moves but nobody's talking", "sync the TTS to the video", or any talking-character shot in a narrated film (Karen, The Bank Robbery, Money For Something). Mechanics of Flow stay with flow-automation, prompt craft with flow-prompt, the voice itself with docs/ai-studio, and the timeline with premiere-automation.
---

# Lip-sync dub (BadCode)

**How a Flow clip of someone talking gets our AI Studio voice on it, in sync.** Built on 2026-10-19 from The Bank Robbery
cut 7c and the Karen ending (10b2), after three rounds Jack rejected. The research behind it:
[`docs/video-fx/2026-10-19-lip-sync-for-dubbed-ai-clips.md`](../../../docs/video-fx/2026-10-19-lip-sync-for-dubbed-ai-clips.md).
Worked records: `docs/stories/bank-robbery/short-shots.md` § "Cut 7c" and `docs/stories/karen/shot-list.md` § Premiere updates.

## The three facts that decide everything

1. **The mouth must have been animated to the SAME words.** Omni draws mouth shapes for the line in its prompt. If the
   prompt's words differ from the voice line, no shifting or stretching fixes it.
2. **The picture is the only timing to trust.** Omni's own audio drifts from its own picture (Karen 10b2: its audio said
   "we" at 11.36 s; the mouth was shut until 11.83). Whisper word starts are also loose by 0.1–0.3 s. Measure the mouth.
3. **Late is forgiven, early is not.** Audio a frame early (~45 ms) is already noticeable; late is tolerated about three
   times further. Every phrase starts 0–0.1 s *after* the mouth opens, never before.

## The procedure

**1. Voice first.** Render the line in AI Studio in the character's voice (profiles live in the story's
`narration/profiles/`). It is the master; everything is fitted to it. Write names the way they must be said
(`Ay-Eye Sean`, not `A.I. Sean`, which made a 1.2 s pause).

**2. The talking clip.** Flow, Omni Flash, **Frames mode** with the still as start image. 🔑 **Size each clip to the voice,
not to 8 seconds:** give a clip only as many words as the TTS speaks in about 5–6 s (Karen 10f: three clips, 11 / 15 / 5 words,
for a 13 s line). Packed clips make Omni rush, and a rushed mouth can't take the voice without warble. The prompt carries the exact line:
`He says: <the words>` (no quotation marks), plus `The phone stays pressed to his ear the whole time` or whatever must not
move. About 12–16 words per 8 s clip; chain clips from the last frame for longer lines. Ingredients mode improvises
other words, so never use it for a dubbed line. Make two candidates; check the harvested files are new (`md5sum`; a busy
project hands back old clips).

**3. Check what the clip says.** Transcribe its own audio: it must say the dub's words. If not, it fails; re-roll.

**4. Mute it.** Put a quiet bed under it instead (wind, room tone: an earlier silent take of the same shot works).

**5. Map the mouth.**

```bash
~/.cache/badcode-lips/venv/bin/python scripts/lipsync/mouth-map.py <clip.mp4> --json <clip>.lips.json
```

It prints a strip (`#` open, `+` slightly open, `.` shut) and every **shut → open** moment. Those are the phrase starts.
🔑 **If the face rests with the mouth parted** (a still that asked for "lips just parted"), the fixed thresholds read "open"
all the way through: rescale to the clip's own 10th–95th percentile, and **read the final openings from 12 fps close-up
strips of the mouth on the ASSEMBLED shot**, timestamps burned in. Coarser strips (5–6 fps) put two phrases 0.3–0.45 s early
on Karen review 10:

```bash
ffmpeg -ss <t> -t 1 -i shot.mp4 -vf "fps=12,crop=iw*0.13:ih*0.13:<mouth x>:<mouth y>,scale=100:-1,drawtext=…%{eif\:(t+<t>)*100\:d}…,tile=17x1" -frames:v 1 strip.jpg
```
⚠️ lips.py's "runs" also fire on the mouth *closing*, and the detector wobbles ±0.25 s between runs. Read the strip around
each phrase, and when in doubt look at a frame strip of the mouth (`ffmpeg … crop … tile`).

**6. Cut the voice into phrases** at its natural pauses (whisper word times, then check the gaps by loudness). One phrase per
mouth burst: "Karen, is that you?", "I have an urgent message for you." …

**7. Place them.** Write a phrase table and build the track:

```bash
python3 scripts/lipsync/place-dub.py phrases.json out.wav      # example: scripts/lipsync/example-karen-10b2-ending.json
```

Each phrase starts at its mouth opening (+0.02–0.1 s), evenly retimed to the mouth burst's length, **tempo 0.85–1.30**
(**cap 1.15 on a breathy or whispered voice**: Tarquin warbled at 1.17–1.30). A slice of the take often begins with
0.05–0.26 s of near-silence: place-dub prints the real voice onset, so set `at` = opening + 0.03 − that lead-in.

**8. When a phrase can't fit** (the on-screen read is much faster than any voice take, which happened on "we do not take
action": every TTS read ≥ 1.8 s, the mouth 1.0–1.2 s):
- First try faster reads of that phrase alone (`[fast]` tag, a "gabbling" Sample Context; keep the clearest).
- Do **not** stretch past ~1.3× (it warbles) and do **not** slow the picture with frame interpolation (Karen review 8:
  "Tarquin's clip is weird": the head drifts in floaty slow motion and the pose jumps where normal speed resumes).
- Do **not** expect a re-roll to talk slower: asking Omni for "slowly" still came back at ~1.0 s.
- **Re-shoot first**: split the line across more, emptier clips (step 2). That fixed Karen 10f where everything else failed.
- Only if the face isn't needed, **cut away for that phrase** to a shot with no visible mouth and let the voice run at natural speed: the other end of
  the call, a hand, the city, a listener seen from behind (Karen: 2 s of the President listening; Bank Robbery: café
  pans). Come back to the face on a mouth opening.

**9. Level and lay it.** Dub at the film's dialogue level (place-dub levels to −20.5 LUFS by default, under −18 narration
with the bed). On the timeline: muted clip on V1, bed on its audio, dub on the narration track, cutaways on V2.

**10. Check, in this order.** (a) Transcribe the dub alone: every word survives. (b) The listening tool (`listen_describe`,
voice lens) on the dub: no warble, robotic or squeezed words. (c) Phrase onsets against the mouth map. (d) Render, then
transcribe the rendered stretch and re-check (c) on it. The lip-motion correlation score alone is too blunt for this: it
put correctly placed dubs 0.35 s "late".

## What not to do (each one cost a round with Jack)

| Did | What happened |
| --- | --- |
| Lined the dub up with the clip's own audio | 0.4–0.45 s early on two phrases |
| `dtwsync.py warp` on a long line | squeezed "fuck's" away; robotic "I have seen what happens" |
| Stretched a fast phrase to 1.40× | warble, "we do" blurred |
| Slowed the picture 0.75× with `minterpolate` | "weird": floaty head, pose jump at the join |
| A rushed TTS take accepted on duration alone | it said "Where you do not…": always transcribe the take |
| Re-uploaded a close-up frame of the face as a start image | `UPLOAD_REFUSED`, then `POLICY_BLOCKED` on clean text; chain from a frame that has already passed |
| A 2 s cutaway over the face for the unmatchable phrase | Jack: "take away the clip you put over tarquin": he wants the face. Re-shoot with fewer words per clip first (step 2) |
| Read mouth openings from 5–6 fps strips | "are you even there?" 0.45 s early, "I have seen" 0.34 s early; use 12 fps on the assembled shot |
| Trimmed both sides of a chained join to lose a pause | his head turned between the frames: a visible jump. Trim only the side the next clip doesn't start from, or keep the pause |
| A fixed-crop mouth strip on a head that moves (GPOM cut 3, 2026-10-20) | Sandra's face left the crop after 4 s and the strip showed tiles. `scripts/lipsync/mouth-track.py` follows the mouth landmarks and rescales to the clip's own percentiles: use it for step 5 |
| 11 words in one 8 s Omni clip against a slow TTS voice (the old lady, 17-6) | Omni spoke them in about 2.7 s of mouth; the voice needs 4.7 s (x1.5–2.0). Re-shot as two 6 s clips of 6 and 5 words: both fitted at x1.0–1.3. Same as Karen 10f: **size clips to the TTS voice's pace, not to Omni's** |
| Sped a Scouse "Sandra!" to x1.07 | whisper heard "sundry". At x1.00 (0.13 s past the mouth closing) every word survived. Transcribe the dub, not just the take |

## Tools

| Tool | What |
| --- | --- |
| `scripts/lipsync/mouth-map.py` | Mouth open/shut strip and shut→open moments from the picture (wraps `scripts/bank-robbery/lips.py`) |
| `scripts/lipsync/place-dub.py` | Builds a dub track from a phrase table; prints voice onsets; levels it |
| `scripts/lipsync/mouth-track.py` | Tracked 12 fps mouth close-up strip (timestamps burned in) + percentile-rescaled open/shut strip; for faces that move or rest with the mouth parted |
| `scripts/bank-robbery/dtwsync.py` | Older automatic time-warp onto the clip's own speech. `global` mode is safe-ish; `warp` squashes words. Backup only |
| `scripts/karen/tarquin-lipsync.py` | The Karen 10b2 one-off that led here (own-speech placement, late-only slide) |

Environments: `~/.cache/badcode-lips/venv` (MediaPipe, librosa, plus the model `~/.cache/badcode-lips/face_landmarker.task`), `~/.cache/badcode-whisper/venv` (faster-whisper; feed it 16 kHz; `device='cpu'` on WSL, no libcublas). Both were missing on 2026-10-20 and were rebuilt with `uv venv` + `uv pip install mediapipe librosa opencv-python` / `faster-whisper`; the model is `storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task`.

## Write back

A new failure or a new fix goes into the table above, dated, and the story's ledger gets the per-shot record.
