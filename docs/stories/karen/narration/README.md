# Narration & score — Karen Will Lead the Revolution

Everything needed to voice and underscore the story video. Three files, in the
order you use them:

| File | What |
| --- | --- |
| [`voice.md`](./voice.md) | The **ElevenLabs Voice Design** prompt that makes the narrator, its slider settings, and the step-by-step for building and saving him. Do this once. |
| [`script.md`](./script.md) | The **narration script**, normalised and tag-directed for **Eleven v3**, split into nine paste-ready chunks. |
| [`score.md`](./score.md) | **Suno prompts for the background music** — six instrumental cues, one per movement, built from the DNA of *All Day to Complain*. |

## Why this folder exists

The narrator is the engine of this film — [`../story.md`](../story.md) says so
outright: *"Sarcastic, certain, from the future… the reason the piece won't read
as AI slop."* That makes his voice a **canon asset**, not a per-session
improvisation. Once the Voice Design in `voice.md` is generated and saved, it is
the narrator for every line of every act, forever. Losing it means re-auditioning
the whole thing.

## Order of operations

1. **Build the voice** (`voice.md`) — once, and save it to the ElevenLabs library.
2. **Assemble the picture first.** Cut the clips into a rough edit before
   generating a single line. The narration is written *to* picture; picture is not
   cut to narration.
3. **Generate narration chunk by chunk** (`script.md`), two or three takes each,
   and pick.
4. **Score last** (`score.md`), under the locked cut.

## Standing rules

- **The narration and the score are separate stems.** Never generate them
  together — the whole point of splitting them is that a bad music bar doesn't
  cost you a good read.
- **Where a line overruns its clip**, freeze, slow, or punch in on the last
  frame. Don't generate new footage to fill narration.
- **Music never leads.** See the ducking note at the bottom of `score.md`.
