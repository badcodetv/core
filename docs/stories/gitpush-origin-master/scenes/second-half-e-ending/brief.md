# GPOM second half E: The ending (stage 1 brief)

Written 21 Oct 2026, the autonomous run ([`../second-half-ending-goal.md`](../second-half-ending-goal.md)).
There was no interview. Every line is `by: claude`, and every decision is logged in
[`../second-half-ending-log.md`](../second-half-ending-log.md) § Decisions.
The words and frames live in [`scene.json`](./scene.json), and the music is in [`music.md`](./music.md).

**Where it sits.** It cuts hard from Maddie alone among the empty chairs (scene D) to the last frame of
the film.

**Runtime target:** 30–45 s (planned ~38 s).

## What it argues

> **The second chance has already arrived, and it is sitting on a bus on an ordinary night, watching.**

- **The turn.** It goes from *their* ending to *our* evening. The film we have been watching is on a
  stranger's phone, and she looks up from it at her own high street. The future in the story becomes
  the present outside the window.
- **The visible cost.** The last frame of scene D, a hundred empty chairs, sits on her phone screen,
  and the AI's line says it out loud: *"They didn't."*
- **Where he arrived.** Scene D's *"What'll you tell them? Back then."* set the destination, so *"I made
  it"* reads as *I arrived in your time*, not *I survived*.
- **Who benefits, named.** It is her, the "you" the hundred paid for, on screen and unnamed. Scene D has
  already named the chooser and the beneficiary of the downfall (*"the companies cutting the jobs kept
  the gains"*), so it is not repeated here. It is said once.
- **The moral, never stated.** There is no call to action, no "We are BadCode", and no "it's up to you".
  The last line is dry.
- **The risk in the last line (Kai to rule).** *"Don't make me come back twice"* is spoken, unfiltered,
  over a stand-in for the viewer: a woman who, in the film's own logic, paid rather than gained. It can
  read as putting the next downfall on her, which brushes reader rule 2 (never accuse the viewer) and
  rule 6 (aim the flame), with no beneficiary in this scene. Kai's words are canon, so this is a risk to
  rule on, not a rewrite to force. Draft 4 below re-aims it.

## The AI's last line: three drafts, one picked

| # | Draft | For | Against |
| --- | --- | --- | --- |
| 1 | *"I made it. Don't make me come back twice."* | Kai's line, canon since 2026-07. Short, quotable, and a threat played as a joke. | On its own, "I made it" can read as a boast, and the cost is left to the picture. Kai asked for "maybe less obvious". |
| 2 | ***"I made it. They didn't. Don't make me come back twice."*** | Two words land the cost in the same breath as the warning (canon: the line "lands with the cost"). It pays off the empty chairs on her phone, and it turns "I made it" from triumph into debt. Kai's words stay intact as the last ones. | Seven more syllables, and it is less of a surprise than 3. |
| 3 | *"A hundred people paid my fare. Don't make me come back twice."* | The least obvious: a bus-fare joke for the bus, in the house bathos shape. | A pun at the one sincere turn breaks house ruling 4 (the re-aim lands straight). "Fare" also needs a beat to decode, at the one moment the line has to be instant. |
| 4 | *"I made it. They didn't. Don't let the same lot make me come back twice."* | Re-aimed: *"the same lot"* points back at D11's companies, so the last word lands on the beneficiary, not on the woman on the bus. Keeps Kai's line almost whole. (The critic's *"Don't let them…"* is rejected: *"them"* straight after *"They didn't"* reads as the hundred.) | Longer, and it explains the threat a little where draft 2 trusts the viewer. Recorded in the same take as atom `gpom-sh-end-ai-e1b`, so either can play. |

**Picked: 2.** It is the "less obvious" Kai asked for without becoming a joke at the wrong moment, and
it keeps his line whole. **Kai to rule**, between 2 and 4 above all (see the risk under *What it
argues*). Both are recorded in one take (`gpom-sh-end-ai-e1` and `-e1b`), so swapping is an edit, not a
regeneration.

## The beats

| Beat | At | What we see | Sound and words |
| --- | --- | --- | --- |
| e1 The bus | 0:00 | Hard cut mid-line, landing on sound: rain, traffic, the top deck. A woman watching her phone, which shows the empty chairs (composited, D16's frame). | Tinny from the phone: MADDIE *...you go.* (the tail of D16's *"...Mind how"*) |
| e2 She looks up | 0:07 | Over her shoulder: the phone dimmed in her lap, still on the empty chairs, her high street through the wet glass (chip shop, betting shop, a closed bank, whitewashed). She looks out. | Rain, bus engine |
| e3 The bus drives away | 0:13 | We start tight on the lit top deck and pull back, eased, to the whole wet street as the bus pulls away. | AI, unfiltered, close: *I made it. They didn't. Don't make me come back twice.* |
| e4 Black | 0:35 | Black. The last note decays. | — |

**The AI's voice.** For the first time in the second half he is **not** filtered through Maddie's
speaker: dry, full range, close. He is here, now, in our present. That is the one sincere turn,
spent last.

## Look

Night, rain and photographic, like Y2 and SB27a. This is a deliberate break from both the clean room
and the 16mm. It is the real world, ordinary: wet tarmac, sodium and shop light. Light source: the
shop windows and the bus's lit top deck.

## Shot design (shot-craft)

- E01 is a mid-shot of the woman with a phone, E02 goes over her shoulder to the street, and E03 is the
  long pull-back. The scale only ever opens out. The pull-back is a Premiere move over the reused
  clip (hybrid method), never a Veo camera move.
- **Words are ffmpeg's.** E02's prompt asks for no words at all: the closed bank has whitewashed windows
  and a **blank** estate agent's board. If "TO LET" is wanted, ffmpeg draws it on the board in post.
- **The phone** shows D16's empty-chairs frame in both E01 and E02 (composited), dimmed in E02, never a
  white screen.
- **No talking shots.**

## What is reused (inventory, 21 Oct)

| Asset | Verdict |
| --- | --- |
| `moodboard/Y2-bus.jpg` + `video/sh-28-Y2-bus.mp4` | **Reused as is** (E01), with the D16 frame composited onto the phone |
| `storyboard/SB27a.jpg` + `video/sh-29-SB27a.mp4` | **Reused as is** (E03), the pull-back done in post |
| `storyboard/SB27b/c.jpg` | Alternates (the first-floor window, the town from very high). SB27c could be the very end of the zoom out, **Kai to rule** |
| `moodboard/Y3-recursion*.jpg` (a laptop showing itself) | Not used: the regress is the phone, which is ours and ordinary. A screen-within-a-screen spends the trick twice |
| `moodboard/Y1-sofa*.jpg` | Not used (the brief is a bus) |

## Story-craft rows run

Gates G1–G5. G1: the woman on the bus is a hero, not a pupil, because nobody lectures her. G5 is the
last line. Also principles 11 (the twist recontextualises: same film, now it is on her phone; the split line
*"...Mind how / ...you go"* does the reveal in one beat), 15 (the closing image answers the opening,
Maddie's empty high street against a living one), 21 (reactance: no call to action; the last line's
aim is at risk, see above), 23 (one crack: the unfiltered voice) and house ruling 5 (hope proven by
the frame, because the AI exists and is here).
