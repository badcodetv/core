# The Bank Robbery — review of cut 5, and cut 6 (9 October 2026)

**Asked for by Jack, 9 October 2026:** "i like the last cut… there are a few error, sometimes objects morph and
change, sometimes they randomley have an american accent, sometimes they say the same thing at the same time,
there are elements of ai slop. i love the weird twin peaks elements to it, the weird dialogue is cool, i like the
intro that was great. Please fix watch and listen to it to spot the errors and fix them."

**Kept, on his word:** the opening, the strange angles, the odd dialogue. Nothing below touches them.

## How it was reviewed

- **Picture:** the whole 6:22 render at two frames a second (764 frames, read by eye), then the suspect shots
  at up to five frames a second, then each suspect shot's full source clip to find a clean stretch.
- **Sound:** the soundtrack through the listening tool (Gemini 3.5 Flash) in eight 48 s parts, every spoken
  line logged with voice and accent. Then the twenty talking clips with a doubt on them, alone, through two
  models (3.5 Flash and 3 Flash preview).
- 🔴 **Nobody has heard it with human ears in this session.** On accent the two models flatly disagree (see
  below), so the accent list is Jack's to make, not mine.

## Objects that change (seen, frame by frame)

| # | Where | Shot | What happens | In cut 6 |
| --- | --- | --- | --- | --- |
| 1 | 0:06 | `s00d-fry` | The egg lifts with bacon stuck under it, flips, and the bacon is gone | ✅ Uses the last second of the clip: the egg is down and steaming |
| 2 | 0:09 | `s00e-pint` | The head swells into a solid blob and pours down the glass | ✅ Uses the first second: the pull |
| 3 | 0:32 | `s01-breakfast` (second use) | Denise drinks from a mug while holding the plates, and the mug ends up in Mr Blue's hand | ✅ Starts after the mug has changed hands; Denise's hold starts 2.2 s early to fill |
| 4 | 0:39 | `s01b-remote` | The remote slides off and vanishes, an egg plate becomes toast, a mug appears | ✅ Uses the second half, after it settles. 🟡 The remote is no longer seen, so the shot is now "three men watch the telly" |
| 5 | 2:14 | the four "Nothing. We put it in." shots | A flat black band across the bottom fifth of the frame (my own shading from cut 5, hiding the model). It reads as a broken file | ✅ Re-cropped from the clean clips to fill the frame, no shading. 🟡 Softer: it is a 1.4× blow-up |
| 6 | 4:11 | `c4-s09-walk` | The heavy man passes through the Ex and comes out on his other side | ✅ Out at 2.75 s, before it. The eating walk before it runs half a second longer |
| 7 | 5:41 | `s11e-cafe-for-sale` | The keyring changes shape four times and the shop lights go off and on | ✅ Only the settled 6.2 s is used, slowed to fill the slot |

## Seen and not fixed (need a new still or clip)

| # | Where | What | Why it is not fixed |
| --- | --- | --- | --- |
| 8 | 3:17 | Two hand-painted placards with word-for-word the same lettering | Needs a new still |
| 9 | 4:12 | The two protesters filming each other is a frozen still with a push | Flow refused the clip three times (cut 5 ledger) |
| 10 | 5:06 | In "Why am I drilling?" neither mouth moves much | Needs a new clip |
| 11 | 5:50 | The guns shot is a still | Jack ruled it stays |
| 12 | 2:32 | The garage argument replays its plate: the men walk out twice | Needs a re-cut of scene 6, and his ruling on the cut lines there |
| 13 | 0:05, 1:18, 2:53, 3:45 | A clip's own sound stops dead at a cut | Twelve-frame crossfades by hand in Premiere; there is no API for them |

## Voices

**What two machine listeners agree on:**

- **In every clip where two characters speak, both lines sound like one voice.** "And how much do we take? /
  Nothing. We put it in.", "Why am I drilling? / It looks better.", "You're putting it in? / Count it in the
  morning.", "So nobody's coming? / Why would anybody come?", the standoff, the list ("Mr Turquoise. / Why am I
  Mr Turquoise?"), the table ("I am the security. / The problem is eyes."), and "Thirteen years! / Fourteen!"
  That is eight clips. **My reading, not his words:** this may be what Jack hears as "they say the same thing at
  the same time".
- **Nothing is spoken in unison except the megaphone line,** "And I'll tell you whose fault it is", which the
  script asks for (the narrator sets it up: "They agree on the first line").

**What they disagree on: accent.** Gemini 3 Flash preview called fourteen of the twenty clips General American.
Gemini 3.5 Flash called all twenty London or Estuary, on the same file. In the full-film pass 3.5 Flash itself
called these American: Mr Red at breakfast, the plan table, the papers, the twist, the list, both Presenter
lines, the vault and "Count it in the morning". **So a machine cannot settle it.** 🔴 Jack: the timecodes of the
lines you hear as American would turn this from a guess into a list.

**One American voice is written that way.** The Platform (the face on the laptop, "I don't need them to believe
it") was cast on 6 October as "an American technology founder… from the West Coast". If that is one of the
voices that jars, say so and he becomes English.

**The likely cause (read, not proven by us).** Every talking clip was made in Frames mode, to keep the still's
framing. Google's Flow help says a custom voice attaches only to Ingredients generations. So in Frames the
twelve voices made on 6 October were probably never used, and the model invented a voice per clip from the
picture. That fits both faults: one voice for two men, and an accent that wanders. The same was seen on Money
For Something (`docs/google-flow/omni-flash.md`, "heard as one voice saying both lines", 6 of 10).

**The test (9 October):** `s05h-table-b` re-made in Ingredients mode with The Governor and The Ex attached, the
still as the scene reference, the accent written into each speech clause, and the listener given "lips closed".
Result: see the foot of this file.

## Cut 6

- **Render to watch:** `renders\bank robbery - cut 6-20261009-patch.mp4`, 6:22, same length as cut 5.
- **What it is:** cut 5's render with rows 1 to 7 above swapped in as picture, and **cut 5's sound untouched.**
- 🟡 **It is not a Premiere sequence.** The Premiere panel was not connected. The same changes as timeline
  edits are in `scripts/bank-robbery/edl-cut6-changes.txt`; the patch is `scripts/bank-robbery/patch-cut6.sh`.
- **Checked by eye:** sixteen frames, one inside every patch and one either side of each join.

## What the research adds (web, 9 October; none of it tested by us)

Full notes: [`docs/google-flow/2026-10-09-dialogue-and-morph-sweep.md`](../../google-flow/2026-10-09-dialogue-and-morph-sweep.md).

- **Morphing:** describe only what changes; one action a clip; one plain sentence on what holds ("the mug stays
  in her hand"); keep the prop out from behind hands; four to six seconds for a prop shot. No Google page
  addresses it.
- **Accent:** put it in the Character's Voice Performance text **and** in the speech clause; keep the picture
  visibly British, because the accent tends to follow the picture; budget re-rolls. One five-run test found
  wording alone made no difference.
- **Two speakers:** one speaker a clip is the safe form. If two, name the speaker by clothing, give the
  listener a job ("lips closed"), and make the two voices far apart in pitch and pace.

## The voice test: result (9 October 2026, one clip)

`vids\v7\s05h-table-b-ingr.mp4`: Omni 1.1 Flash, **Ingredients**, 8 s, the `s05h-table` still plus The Governor
and The Ex attached. Prompt: `~/.cache/badcode-bank-robbery/v7c/prompts/s05h-table-b-ingr.txt`, copied below.
Old take for comparison: `vids\v6\s05h-table-b.mp4` (Frames).

| | Old (Frames) | New (Ingredients) |
| --- | --- | --- |
| Two voices? | One voice for both lines (both listeners) | 3 Flash preview: "two clearly different voices", the second higher and smoother. 3.5 Flash: more different than the old take, "still sounds like a single actor" |
| Right mouth on each line | Yes | Yes (seen: the seated man, then the man leaning) |
| Words | As written | 🟡 A stumble: "I… I am the security" |
| Framing | The still's | 🟡 **Re-staged:** a wider, squarer profile two-shot, a mug moved. Same room, same light, same two men |
| Accent | Not judged | Not judged (machines cannot, see above) |

**Reading:** one clip, so a lead and not a finding. Ingredients with both Characters attached pulled the two
voices apart, at the price of the still's exact framing and one stumble. 🔴 **Jack: play the two files back to
back.** If the new one sounds like two Englishmen to you, the eight two-voice clips get re-made this way; if the
framing change costs more than the voice gains, the other route is one speaker a clip, cut back and forth.

```text
Use the image as the scene: keep its framing, the bare table, the two men and the single bare bulb exactly as they are. A locked-off shot from a scripted feature film, a slow dark drama with made-up characters played by actors on a closed set. One continuous shot with no cuts. No camera movement. The Governor, the seated man, says, in a soft, dry, educated London English accent: Security isn't a problem. I am the security. While he speaks, The Ex listens with his lips closed. After a pause The Ex, the man leaning on the table, says, in a warm, unhurried, privately educated southern English accent: The problem is eyes. While he speaks, The Governor keeps his lips closed and blinks once. Each man speaks in his own voice, and the two voices are clearly different. Then nobody moves. The bare bulb sways very slightly. Sound: their two voices, a bare bulb buzzing and rain on a metal roof. No music. Thanks.
```
