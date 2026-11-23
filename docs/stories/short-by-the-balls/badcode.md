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
Not decided — run story-style (or a quick pick on the mood board). Each still's layout comes from a real Unsplash photo
given to Flow as the reference (Library pieces below). 9:16.
Flow project: `ccce50b5-9b07-48f1-a62e-b710b6bc96e1` ("Nov 23 - 13:45"). Stills Nano Banana 2.1, 9:16.

## Sound
Not decided — run story-style. Any Suno track is music and sound effects only (workspace `short-by-the-balls`); every
spoken line is an AI Studio voice, cast with voice-casting (English, with a named region).

## Cast
- **BadCode** (Jack, 2026-11-23): on screen in the BadCode balaclava (below), beside the machine; says the line.
- **The young couple** (Jack, 2026-11-23): one young couple feeding the machine coins; they look like stereotypical millennials (Jack). Not cast yet.

## Story-only rules
- Jack and Kai write the jokes: beats say what each moment conveys; joke lines stay blank for them. The one line so far
  is Jack's: "It was never broken. It was set."
- Inspired by George Carlin's "The Owners": never his audio or his words read out.
- The owners on the claw are kinds of owner (bank, landlord, energy company), never a real company's name or logo.
- The fact (adjustable grip and payout settings) is read at source before it is said or shown.

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

## Where the detail is
[README.md](./README.md) · [look.md](./look.md) · [sound.md](./sound.md) · rulings [scenes/by-the-balls/picks.md](./scenes/by-the-balls/picks.md)
