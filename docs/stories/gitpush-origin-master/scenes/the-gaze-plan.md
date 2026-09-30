---
story: gitpush-origin-master
scene: the-gaze
status: EARLIER PLAN — current structure directed by Kai on 2026-09-20 in the-gaze-sequence.md revision C; proposals and open calls below are historical unless carried forward there
supersedes: the scratchpad report `gpom-metrics-sequence-v2.md` (Fable pass, 2026-09-17), which
  was lost when the session scratchpad was wiped. This file is now the only copy.
stills: [`the-gaze.md`](./the-gaze.md) — 31 shots × 5 framings, 295 option stills
board: https://claude.ai/artifact/BSbiKAoT1VrZkN71fDJwnb (picks in its own db)
---

# The gaze — the plan

**Latest direction, 2026-09-20:** see [the sequence, revision C](./the-gaze-sequence.md#revision-c--success-the-puzzle-the-measurement-the-people--2026-09-20).
The scene now proceeds **markets and executives → construction and power → server hall → the
AI's puzzlement at human unhappiness → an experiment recording happiness, with falling dials →
difficult everyday life**. The AI sincerely considers the era successful by the measures it
understands. The human images retain their dystopian force. Recording is an attempt to understand
the discrepancy. This supersedes the intercut-prosperity proposal and the old demise-as-training-data
ending. The exact narration was updated at Kai's request on 2026-09-20 in
[`songs/narration.md`](../songs/narration.md),
under `gpom-datacentre`, revision B. Kai has enough footage; music is for his separate Suno pass.

The material below preserves the earlier development and is not the current assembly instruction.

How cut 3 (`plant-room-recut`) runs into cut 4 (`bulletin`), with the machine measuring the world
between them. **At the time of this earlier plan, nothing here was ruled.** It exists so the rulings can be made against something
concrete, and so another session can pick the work up.

🔴 **Correction that cost the first draft:** the ASCII-skull console was **retired in full on
2026-08-27** (`plant-room-recut.md`, "AS BUILT"). What is on the timeline is the analogue control
room, the four gauges (SOIL / HAPPINESS / WATER / BIRTH RATE), the red alert and the tower reveal.
Plans that "return to the skull" are planning against a beat that does not exist.

## 0. 🔴 Kai's reframe — 2026-09-19, and it supersedes §2's spine

Spoken while picking the shortlist. **The scene is not four planetary readings. It is the machine
moving in, and not looking up.**

> *"The AI was proliferating in data centres, because that's the main scene — we've just come off
> the back of it coming down from the satellite. Humans spent trillions on data centres, so we've
> got politicians opening ribbons and then these huge data centres, and we cut inside the data
> centres a little bit as well… then the metrics start wobbling, then we cut to a combination of
> golf clubs doing really well and the stock market doing really well, green initiatives — but then
> with the children's playgrounds fucked, the homeless, the supermarkets being expensive, the soil
> not having a great time."*

**The spine, in his order:**

1. **Humans build data centres.** Ribbon-cuttings, politicians, the capex as a landscape.
2. **The AI moves in.** Interior — 🟡 he wants to **reuse the existing control room** ("I kind of
   like our existing control room"), not replace it.
3. **The metrics start wobbling.**
4. **The split screen of a country.** What is thriving *against* what is wrecked, cut together:
   golf clubs, the stock market, green initiatives ↔ playgrounds, the doorway, the checkout, the soil.

**The narration turn**, in his words, not yet written: *"I was doing great, I optimised my
proliferation, I didn't think so much about the quality of the decisions the humans were making."*
🔴 **Words change only with Kai** — this replaces nothing in `narration.md` until he
writes it.

**What this changes:** SOIL / HAPPINESS / WATER / BIRTH RATE stop being the scene's structure and
become four of the wrecked-side pictures. His picks already voted for this — the street (34 keeps)
and the estate (28) outweigh the four readings (20 between them), and the birth-rate estate took
zero keeps.

🔴 **Images we do not have yet:** a golf club thriving, a stock market rising, a green initiative
being celebrated. The ceremony block (20–24) covers the ribbon and the photo-op but not these.
A round 4 is owed.

Shortlist room (128 keeps, one comment box each, notes in its own db):
https://claude.ai/artifact/4KVh6HwJy5i4KoEz5Ld71R

---

## 1. The overlay — the one device that makes this a point of view, not a graphic

The machine's readout is **the film's own green console type, projected onto the world** — not a
Minority Report glass dashboard. Kai ruled 2026-08-21 that the machine speaks in a 1981 green text
console (`2032` card, `git push origin master`); this grants the "holographic metrics layer" ask
without breaking that grammar.

1. **The overlay never cuts.** The world hard-cuts under it; the overlay's `● REC` and its typed
   word persist across the cut. The machine's attention is the only continuous thing in the scene.
2. **The attention rectangle.** Everything outside a soft rectangle is slightly desaturated and
   softened; inside it, full colour and sharpness. It moves on its own timing — **no object
   tracking needed**.
3. **Only three things are ever legible:** the spoken word typing itself (`SOIL`), `REPORTED ✓`
   (the film's existing green-checkmark device — the official number), and `OBSERVED 0.74 ▼` (an
   index with no unit). 🔴 **Every number is invented. Never a real statistic.**
4. **Brackets only on locked-camera shots.** On moving shots, one centred bracket. This is what
   keeps the overlay buildable in post without a tracker.
5. **Green until the trend line.** No red before the red alert (B6) — the standing rule of the
   recut. The values turn red one by one on *"one by one, the data points were turning red"*,
   which lands us on B6 exactly.

Build lane: ffmpeg / Python, like `build_console.py`. **Veo is never asked to render text.**

## 2. The sequence

| Block | Runs | What happens |
| --- | --- | --- |
| **A · the grid** | ~14s | The drone rise at sunset over the estate (shots 01, 25–30), then hard cut to the louvre grille at 2ft (B1 as built), then aisle → vertical hall → control room (B2–B4 as built). 🔴 Gate 2 wants a visible cost in the monumental frame: the **dark town beside the lit grid**. |
| **B · the gaze leaves** | ~6s | Post push into the **SOIL gauge's black dial face** until black fills frame; `SOIL` types itself in phosphor; out of that black, **cut 1's own Earth-from-orbit shot** returns; then the dive through cloud that turns brown (shot 02) — which *is* the cut into the first reading. |
| **C · four readings** | ~22s, shortening 7/6/5/4 | One hard cut per spoken word. Each pairs a vast frame with a small one carrying the cost: **SOIL** (03 + 04), **HAPPINESS** (06 + 05), **WATER** (07 + 08), **BIRTH RATE** (09 + 10). Sound: mute under the hall's fan hum, except happiness, which swells and drains under the canon line *"I could hear you. All of you, at once. And the sound was going down."* |
| **C′ · the street** *(open)* | — | Shots 15–19 (prices, the doorway, the school run, the high street, the playground) and 20–24 (the ceremony). Either a fifth reading or the pictures that make HAPPINESS concrete. **Kai's call.** |
| **D · the trend line** | ~6s | The drained reservoir's **dam wall**, whose horizontal tide marks already are the falling graph (shot 11); the overlay labels the steps. Then half-second red recuts of all four readings; `● REC` gains `STORED FOR TRAINING ✓`. The red line's angle graphic-matches the gauge needles. |
| **E · back in the machine** | ~18s | B5 gauges (trim to ~5s), B6 red alert, B7 tower reveal. The overlay types `AWAITING HUMAN REVIEW` over the towers on the ellipsis in *"I did not want to interfere… so I focused on capturing the demise as training data…"* — the retired skull beat's best line, kept. The overlay stays on into the newsreader. |
| **F · the bulletins** | ~60s (120s today) | The overlay is the bridge: the collapse arrives as news because the machine is watching the news. Its one job here is the ruled ladder made legible — **`HUMANS ON SCREEN: 5 → 2 → 0`** — plus one green ✓ per bulletin on the thing that should never have been optimised. New beats: the exodus with cardboard boxes (12), six towers switching into one lit pattern (13), and the **invisible battle** — the empty chalk down at dawn (14) with thousands of overlay contacts in an empty sky, **both sides tagged `VICTORY ✓`** — then the ruled SWINDON road sign, undamaged, smoke behind, **last**. |

## 3. Why the invisible battle

It keeps the film's oldest rule (*the world ends off-screen; the composure is the horror*), it is
policy-safe (the plate is an empty landscape — never write *war*, *drone swarm* or *weapon*), it
costs nothing new, and a war fought faster than eyes can follow frightens more than two swarms
colliding, which would also read as a trailer.

## 4. Reader-rule checks carried into every frame

- **Never a fear without its beneficiary** (`the-reader.md` rule 6): happiness carries
  `ENGAGEMENT ▲`, water carries `COOLING DRAW ▲` drawn back to our own grid, prices carry
  `GROCERY MARGIN ▲`, the high street carries `RENTS ▲`.
- **Aim at the decision, never at the reader** (rules 2 and 9): the ceremony block (20–24) mocks
  ribbon-cuttings, summits and photo-ops — never an ordinary person.
- **Housing points at ownership, not newcomers** (rule 4): the birth-rate estate is *empty and
  owned*, never *full and foreign*.

## 5. Production notes

- **Stills first, always.** Kai approves every plate (all candidates) before a video credit.
- **Veo animates the world, the camera is locked** where there is a repeating grid (the 3am city,
  the estate, the six towers, the bus). Camera free on the dive, the storm, aerials.
- **Chain, never pin an `endImage`** — pinning morphs.
- Rough cost if the whole sequence went to video: ~18–22 Veo generations at Fast.

## 6. 🔴 The six calls owed by Kai

1. **The overlay look** — green console on the world (recommended) or a glass holographic layer.
2. **Where the sequence returns to** — gauges + red alert + towers as built (recommended), or
   rebuild a console beat.
3. **The Swindon payoff** — invisible battle + sign (recommended), sign only (ruled 2026-08-24), or
   swarms colliding.
4. **Which readings** — the original four, plus whether the street block is a fifth reading.
5. **The opener** — the sunset estate rise (recommended) or the megacity opener of 2026-09-12.
6. **One optional line** — *"So I turned my attention to measuring them"* at the gauge push, or let
   the picture carry it (recommended).
