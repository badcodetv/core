# The Bank Robbery — Jack's notes on cut 7, why it still read as AI, and the plan for cut 8 (9 October 2026)

**Asked for by Jack, 9 October 2026,** with fourteen frames from cut 7 in Premiere.

## His notes, frame by frame

| # | Where in cut 7 | Clip | Jack's words | What cut 8 does |
| --- | --- | --- | --- | --- |
| 1 | 1:06 to 1:22 | the hearing (`s03a-hearing`) | "American accents for the whole scene, including the women asking him stuff" | The panel's question is spoken in AI Studio speech (she is seen from behind) and laid over the same picture. The Ex's answer is re-made in Ingredients with his Character |
| 2 | 2:24 to 2:36 | the garage (`s06a-list`, `s06-colours-talk`) | "same here" | Five one-speaker clips in Ingredients, each with the speaker's Character |
| 3 | 2:58 to 3:06 | the whisper at the party (`s07b-off-record`) | "remove this part" | Removed, with the narrator line that sat on it ("Very balanced man") |
| 4 | 3:06 to 3:10 | Denise in the hall (`s07c-denise-hall`) | "denise counting does not work, remove this, just show her hoovering" | The counting is removed. A new clip from the same still has her hoovering |
| 5 | 4:11 to 4:18 | two phones from above (`s08f-above`) | "remove this part is it too ai slop like, also makes no sense" | Removed. The narrator's "Nobody films it" stays, over a new shot from inside the crowd |
| 6 | 4:18 to 4:25 | two men and one pallet (`s09c-pallet`) | "same for this remove this" | Removed, with its narrator line ("Left end. Right end. Same pallet") |
| 7 | 4:25 to 4:34 | the door (`s09d-door2`) | "it looks terrible when they put the masks on" | Re-made: the four are already masked and standing in the doorway |
| 8 | 4:34 to 4:41 | Mr Turquoise (`s09e-turquoise`) | "there is no gun in his hand, change it please" | Re-made with the pistol in his raised hand in the first frame |
| 9 | 4:41 to 4:44 | Denise comes in (`s10a-enter`) | "denise's face look weird and morphed" | Re-made from behind her, so there is no small face to break |
| 10 | 4:44 to 4:48 | the hoover (`s10-hoover-talk`) | "they are just balencing on one leg, change it so she just hoovers round them… flow clearly struggles with stuff like this" | Re-made at floor level: planted shoes, the hoover steers round them. Her "Lift your feet" is gone |
| 11 | 4:48 to 4:52 | the bleach (`s10e-bleach`) | "the bottle of bleach turns into a rag" | Re-made: the cloth is already under her hand, the bottle stands on the counter and nobody touches it |
| 12 | 4:52 to 5:00 | "It's about that much" (`s10c-that-much`) | "remove this part it is too preachy and on the nose" | Removed. This was the film's only line about immigration; the open ruling on it (Jack and Kai) no longer applies |
| 13 | 5:06 to 5:32 | the vault (`s11*`, v7) | "this whole scene looks weird and ai slop like change it please" | Re-made in a new place: a brick basement with a green iron strongroom door |
| 13 | narrator line 29 | | "every pound shes got a bit smaller" should be "every pound she has, worth less" | Re-recorded as `n29b` |
| 14 | 5:50 to 5:55 | "Who talked?" (`s12j`, `s12k`) | "they argue for no reason at least make it funny or something" | New lines (mine, below) |

**Also from Jack:** "why is there so much ai slop, is the stuff in the repo not working out in flow, or the research
not being saved properly… it might be in the prompts or the layout of them that is messing it up or contradiciting
itself. keep up with the david lynch, interesting angles, cinematic, funny and pretty to look at, whilst being
gritty. maybe it is a tad too grey as well, there should be more colour."

## Why it still read as AI

Found by reading every prompt sent (88 stills, 115 clips) against the repo's own research. Three causes, in order
of how much they cost.

**1. The shots asked the video model for things our own notes say it cannot do.** Every clip Jack called slop is
on this list, and each item was already written down in `docs/google-flow/` before the clip was made.

| The model cannot do | The clip that asked for it |
| --- | --- |
| Put something on over a face | the masks at the door |
| Use a hand prop on a surface (spray then wipe) | the bleach |
| Hold a one-leg balance | the hoover |
| Keep a small far-off face when it moves | Denise coming in |
| Move four or more people, or two people moving one load | the door, the pallet, the vault from above |
| Speak in a saved voice in Frames mode | the hearing, the garage |

**2. The prompts ordered the grey.** "Muted colour: stone grey, black and navy" is in 56 of 88 stills, "grey" in
77, "the only strong colour" in 78. In the seventh pass "cold" is in 13 of 15 stills and "Deep shadows with no
detail" in 11. The same lighting sentence ("One light source only, no fill") is in 74 of 88, and the same camera
(lens on the floor, a blurred thing in front) in most. An odd angle used every time is one angle.

**3. The prompts were long and argued with themselves.** Seventh-pass stills averaged 244 words and clips 120.
Each vault still opened with 40 words about a reference image, then told the model the place was different from
that reference. Attached Characters were described again ("silver hair", "in his black suit") after a line
saying they keep their own faces and clothes. Riot stills said "a feature film, shot on 35mm" and ended
"Documentary photography". Clips carried four or five "does not move" sentences each, and opened with 30 to 45
words of boilerplate before the action.

**Was the research saved?** Yes. **Was it used?** Not reliably, because the two skills that write prompts
(`flow-prompt`, `shot-craft`) did not point at `docs/google-flow/` at all. Both now do, and the list of moves to
design around is at the top of `docs/google-flow/README.md`.

**One more cause, about checking:** clips were passed by looking at one frame every two seconds, which is how the
masks clip was logged "stable". A mask going on takes less than two seconds.

## What changes in how prompts are written (eighth pass)

- **A still is about 115 words, a clip about 60.** The action is the first sentence of a clip.
- **Colour is named for each place, and it is saturated.** The hall: bottle green, oxblood red, brass, cream. The
  basement: the same four plus warm tungsten. The street: deep blue, pink-red flare, amber lamps.
- **Every still names two lights of different colours** (a green lamp and pink smoke; tungsten and a green glow).
- **One short line for a reference:** "Same room as the reference image."
- **An attached Character is named and placed, never described.**
- **Each shot is designed round what the model can do.** The mask is already on. The cloth is already under the
  hand. The pistol is already raised. A face that matters is chest-up or closer, or it is turned away.
- **Anyone who is not a Flow Character and has a line is seen from behind,** and the line is made in AI Studio
  speech, where the accent is set by a written note and has held for every narrator line.

## The new standoff lines (mine; Jack writes the jokes, so swap freely)

The alarm goes off and they drop straight back into the fake fight from the garage:

| Who | Line |
| --- | --- |
| Mr Blue | This is your mess! |
| Mr Red | We inherited it! |
| Mr Blue | Thirteen years! |
| Mr Red | Fourteen! |

It calls back to scene 6 and to the narrator's "eventually it's just your personality".

Shots, prompts and results: [`stills-v8.md`](./stills-v8.md). What went into the cut: "Cut 8" in
[`assembly.md`](./assembly.md).
