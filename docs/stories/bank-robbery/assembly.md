# The Bank Robbery — first assembly (7 October 2026)

**Asked for by Jack, 7 October 2026:** "do the narration, then put it all together in premiere."

**This is a first assembly, not a finished cut.** Everything is in script order with the narrator
laid over it. Nobody has watched it at playing speed: it was checked by measurement and by ten
frames from the render.

## The narration

- **32 lines, 3 min 25 s in all,** one WAV per line, in `Desktop\Youtube Vids\animation\bank robbery\narrator\`.
- **Voice:** the Money For Something narrator, as Jack ruled: `gemini-3.1-flash-tts-preview`, voice
  **Zubenelgenubi**, Accent **British (Brixton)**, nothing else. The prompt is word for word the one
  the AI Studio page sent when Jack chose the voice.
- **Words:** [`scripts/bank-robbery/br-narration.json`](../../../scripts/bank-robbery/br-narration.json),
  taken from [`script.md`](./script.md). Runner: `scripts/bank-robbery/br-narration.py` (plain HTTPS;
  the Google SDK is not installed on Jack's machine).
- **One take each, first time.** 🔴 **Nobody has listened.** One take in ten of this voice is reported
  to drift, so each line wants comparing with the reference take
  (`money for something\narrator\NARRATOR-VOICE-reference-zubenelgenubi-brixton.wav`).
- **Two small changes to the words as read:** line 16 ends with a full stop where the script has
  three dots, and line 18 has a full stop where the script has a semicolon.
- **Not written, so not recorded:** scene 2's optional line.
- `narrator\original-full-level\` holds a copy of each file. It was made during a levelling attempt
  that was undone; the files in `narrator\` are identical to those copies.

## Premiere

**Project:** `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/bank robbery.prproj`
**Sequence:** `bank robbery - cut 1` — 1280×720 @ 24, 510.7 s (8 min 30 s)
**Built:** 2026-10-07 by session (bridge). `bank robbery - scenes in order` (yesterday's) is untouched.

| Track | What |
| --- | --- |
| V1 | 86 clips, butted, no gaps |
| A1 | Each picture clip's own sound, same times |
| A2 | The 32 narrator lines |

**Bins:** `01-scenes` (yesterday's silent clips) · `02-clips-v3` (41 of today's clips) ·
`03-cut1-pieces` (38 rendered pieces) · `04-narrator` (32 WAVs).

**The plan the timeline was built from:** `scripts/bank-robbery/edl-cut1.json`, with a readable list
in `scripts/bank-robbery/edl-cut1.txt` (start, length, clip, kind). Rebuild both, and the rendered
pieces, with `python3 scripts/bank-robbery/build-cut1.py`. Each entry was placed by setting the
source in and out on the project item, overwriting onto V1 and A1, and clearing the in and out;
narrator lines went onto A2 whole. Twelve placements an eval, nine evals.

**How the cut was decided (all of it mine, none of it ruled):**

- **A talking clip is trimmed to its speech,** found from the sound level, with 0.8 s before and
  1.1 s after. Where the sound is loud throughout (megaphones, the bell, the hoover) nearly the
  whole clip is used.
- **A narrator line never plays over a talking clip.** It sits over a silent clip, starting 0.4 s
  in, with 0.6 s after it.
- **Where there was no silent clip for a line, a still is held with a slow push** (17 of these,
  `hold-*.mp4`). Where the line runs longer than the 8-second clip, the clip's last frame is frozen
  for the rest (7 of these, `ext-*.mp4`).
- **Scene 4's name cards** are 1.3 s of the clip and then a 1.3 s freeze with the name and job in
  white Impact (`card-*.mp4`). The jobs are the plain ones; Jack's funny tags are not written yet.
  Mr Blue and Mr Red get the old clip of them stopping at the buzzer, then the freeze with an arm
  round each other.
- **Lettering** was added with ffmpeg, since the bridge cannot write text: the title over the bank
  door, THREE WEEKS EARLIER, BANK HOLIDAY MONDAY, and the two headlines in scene 5.

**Applied in Premiere:** one thing. The narrator's 32 clips on A2 have Volume set to −9 dB
(Level 0.0631), because the narrator files measure −13 LUFS and the talking clips about −27.

**Outputs**

- Render: `renders\bank robbery - cut 1-20261007-1659.mp4` (473 MB). The earlier
  `…-1657.mp4` is the same picture with the narrator at full level; it can be deleted.
- Measured on the 1659 render: no black frames except the first third of a second of the two
  title cards; integrated loudness −22.5 LUFS; true peak 0.0 dBFS.
- Ten frames read by eye: the title, both title cards, three name cards, both headlines, the remote
  at the window and the kebab shop. All as intended.

**Needs a human**

- **Watch it.** Nobody has.
- **The voices** in the talking clips (see [`clips-v3.md`](./clips-v3.md), "The voices").
- **The narrator's 32 takes,** by ear.
- **Sound:** A1 jumps from one room to the next at every cut, and holds and frozen frames have no
  sound under the narrator. There is no music, including under the scene 4 montage, which was meant
  to have 80s music. Audio crossfades cannot be added through the bridge.
- **Seven shots freeze on their last frame** and seventeen are held stills. They are the first
  things to replace if they read as cheap.
- **The delivery check fails** (`scripts/delivery-qc.sh`): the render is untagged full range, the
  peak is at 0 dBFS and the loudness is off target. That is expected for an assembly and has to be
  fixed before anything is uploaded.
- **Length:** 8 min 30 s against the seven minutes guessed from the script.
