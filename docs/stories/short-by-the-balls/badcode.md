# By the Balls

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, about 13 s): an arcade claw machine with a little house as the prize. A coin goes in, the claw
grabs the house and goes limp at the top, again and again. The claw carries the owners' names (bank, landlord, energy
company). The line, Jack's: "It was never broken. It was set." The point: the game isn't broken, it is set by the people
who own the machine. The way out: ⬜ not decided.

## Look
Real-looking photographs of a British arcade at night (Unsplash layouts, then edits of the picked stills). Start frames
LOCKED (Jack, 2026-11-23) in the media folder's `moodboard/`: PLAY, GRAB, LIMP, FACES, BADCODE, UNLOCK, DIAL, WIN. 9:16.
Flow project: `ccce50b5-9b07-48f1-a62e-b710b6bc96e1` ("Nov 23 - 13:45"). Stills Nano Banana 2.1, 9:16.

## Sound
Music: LOCKED (Jack, 2026-11-23, clips page): `btb-music-r1-fm-cabinet-attract-loop-v6-w30` take ae605d80 (0:29), his ask
"start with arcade music too, think stranger things when they are in the arcade"; its prompt verbatim in `songs/music-r1/round.json`
(`fm-cabinet-attract-loop`); recorded to the media folder's `audio/music/`. Any Suno track is music and sound effects only (workspace `short-by-the-balls`).
Voice: LOCKED (Jack, 2026-11-23): BadCode = Google library voice `en-gb-csagent-11` (Liverpool, 36), plain read on
`gemini-3.8-flash-tts`, no style; take `audio/casting/badcode--en-gb-csagent-11.wav` (media folder).

## Cast
- **BadCode** (Jack, 2026-11-23): on screen beside the machine; says the line. An arcade worker: navy micro-fleece jacket zipped
  to the chin, change belt and keys, gloves, and the balaclava in the same navy fleece (Jack: "make the mask match whatever
  material the arcade worker wears"); no skin. Reference `cast/CAST-BADCODE-2.jpg` (media folder).
- **The young couple** (Jack, 2026-11-23): one young couple feeding the machine coins; they look like stereotypical millennials (Jack). References `cast/CAST-HER.jpg`, `cast/CAST-HIM.jpg` (media folder).

## Story-only rules
- Inside the claw machine: only small model houses and money (coins, banknotes with no readable print); the prize is the
  same small white two-storey house with a red roof in every shot (Jack, 2026-11-23).
- Jack and Kai write the jokes: beats say what each moment conveys; joke lines stay blank for them. The one line so far
  is Jack's: "It was never broken. It was set."
- Inspired by George Carlin's "The Owners": never his audio or his words read out.
- The owners on the claw are kinds of owner (bank, landlord, energy company), never a real company's name or logo.
- The fact (adjustable grip and payout settings) is read at source before it is said or shown.
- **No solution segment: go straight to the final graphic** (meeting 2026-11-24, `docs/misc/2026-11-24-meeting.md`; Gemini's notes, to be done by Jack).

## Library pieces in use
- **Real photo as the look:** find the layout on Unsplash (`python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>"`),
  give the picked photo to Flow as the reference; the prompt says only what happens. Never an AI figure pasted into a
  real photo.
- **Clean room:** every Flow or Suno prompt is written by a sealed writer (`clean-room-writer` agent) from one brief of
  raw facts in `scenes/by-the-balls/cleanroom/`; never from earlier prompts.
- **The BadCode balaclava:** anyone in it is BadCode in person. Fixed by the brand: a large white ring stitched round the
  whole face, the red triangle over the wearer's LEFT eye (on the right of the picture), no holes, no skin anywhere,
  gloves. Attach `docs/brand/balaclava/mask-reference.jpg` with `docs/brand/balaclava/shared-wording.txt` verbatim. In
  motion, write that the mask keeps facing the camera and check the triangle zoomed in at three points per clip. No
  mouth, so its lines need no lip-sync.

## State
Rough cut 2 (23.7 s) on https://claude.ai/artifact/DXKshcwZZ21LCwNniyV83x; in Premiere `short-by-the-balls-1-by-the-balls-r2`
(in sync) and on Drive (agreed cut). Outro: the logo printed on an air hockey table (`scripts/shorts/btb_hockey_logo.py`).
Cut script `scripts/shorts/btb_cut.py`. Clips https://claude.ai/artifact/KvpYixAvZKWBeRofPiLWvv; stills https://claude.ai/artifact/61dzwTLv6Yp4yALDYmFfpn.

## Where the detail is
[README.md](./README.md) · [look.md](./look.md) · [sound.md](./sound.md) · rulings [scenes/by-the-balls/picks.md](./scenes/by-the-balls/picks.md)
