# Camping recut — storyboard index

Twenty-four pages (23 slides + stinger) in three movements —
**JUDGE 1–9 · SEE 10–14 · BECOME 15–24** —
bookended on the tent-door POV. This recut edits the **live v1 comic**
(`apps/web/src/comics/camping`) and reuses its existing bucket assets on
`comics-v2/camping-jack-test`; the separate from-scratch rework in
`docs/camping-v2/` continues independently.

Source of truth for beats, bubbles, coordinates and Flow prompts:
[`docs/superpowers/specs/2026-07-25-camping-recut-plan.md`](../../superpowers/specs/2026-07-25-camping-recut-plan.md)
(§3 slides · §5 bubble coordinates · §6 Flow prompts).

House register (NOT the monolith brand register): *hyper-realistic cinematic film
still, 35mm, fine natural grain, overcast British light, muted cold palette, wet
surfaces, no lens flares, no fantasy effects (except i35), 16:9.*

Status values: `reused` (Storyteller-era golden, prompt unrecorded) · `new`
(generated fresh) · `edit-of-<base>` (reference-anchored edit of a golden original).

> **Review pass, 2026-07-25.** Two changes after viewing the whole comic in the browser:
> (1) slides 2, 3, 4 and 7 were **regenerated** — the v1 city Tarquin was a visibly
> different man from the retreat/camp Tarquin, which breaks the story's central mirror;
> (2) the spec's slide 12 (a second, near-identical wide yurt frame) was **cut** and its
> rifle thought moved onto slide 11, removing a scroll stall. Everything after it
> renumbered down by one, so page numbers here are one lower than the spec's §3 table
> from slide 12 onward. Archived: `_cut/p12-cut-yurt-closeup.md`.

| # | Asset key | Status | Shot |
| --- | --- | --- | --- |
| p01 | `anim/a01` | reused | Shard, dusk drone push-in |
| p02 | `img/i40.png` | regenerated (face continuity) | Boardroom, rising chart — "let's circle back" |
| p03 | `img/i41.png` | regenerated (face continuity) | Lift lobby, applause — the Winning Mentality™ |
| p04 | `img/i42.png` | regenerated (face continuity) | Lobby weekend chat — glamping, £400 a night |
| p05 | `anim/a02` | reused | His car on the night street, Shard behind — the chimp line |
| p06 | `anim/a04` | reused | Aerial: the car pulls in beside the tatty tent |
| p07 | `img/i43.png` | regenerated (face continuity) | Ground level: Tarquin's contempt; his car straddles two bays. Eyeline goes off-frame to the tent |
| p08 | `img/i05.png` | reused | POV inside Bob's tent, bottle in hand, the car in the doorway |
| p09 | `img/i07.png` | reused | Bob in the tent, hat, bottle — 2008, the crash, her |
| p10 | `anim/a06` | reused | Forest road, headlights through rain |
| p11 | `img/i11.png` | reused | Yurt circle — Moonwhisper's pitch, the rifle thought, "drink deep" |
| p12 | `anim/a08` | reused | Psychedelic repaint, neon river, fireflies — it kicks in |
| p13 | `img/i35.png` | new | **THE VISION** — he floats above the car park; the man looking up from the tent is himself |
| p14 | `img/i36.png` | new | Directly overhead: asleep on the forest floor, framed like a parking bay |
| p15 | `img/i37.png` | edit-of-golden | He wakes. Slide 8's shot — burning camp, dead clamped car, only A and I lit |
| p16 | `img/i18.png` | reused | Newspaper at his boots: BRITAIN'S LAST WORKER REPLACED BY AI |
| p17 | `img/i19.png` | reused | Reading it by the burn barrel — "it didn't even need the chimp" |
| p18 | `anim/a10` | reused | Aerial: the car park is a tent city now |
| p19 | `img/i21.png` | reused | Bob and Tarquin either side of the barrel — "took two spaces" |
| p20 | `img/i21.png` | reused | The name beat — "Bob. My name's Bob, mate." |
| p21 | `img/i22.png` | reused | Tarquin alone, hands over the flame — "nothing's up to me anymore" |
| p22 | `img/i38.png` | edit-of-golden | He is slide 9: same framing as Bob, Oxfords paired outside, totes for luggage. No bubbles |
| p23 | `anim/a13` | reused | Badcode in the puddle |
| p24 | `img/i39.png` | edit-of-golden | Stinger: ▸ STAY PUT / thank you for banking with us |


## WAVE-2 image lane (serial, human-gated)

One Flow browser session, executed **in this order** — hardest creative first,
mechanical edits later. Each image is human-gated (`badcode-art-direction` loop:
plan → 2 candidates → Kai picks or redirects). Prompts are carried verbatim in
each panel record; the lane executes from the record, not from the spec.

| Order | Ticket | Key | Slide | Kind | Base / references |
|---|---|---|---|---|---|
| 1 | T-IMG-1 | `i35` | p14 | generate — the vision | refs `img/i12.png`, `anim/a03` poster or `img/i17.png`, `img/i07.png` |
| 2 | T-IMG-2 | `i34` | p07 | generate — the sneer | refs `img/i03.png`/`img/i04.png`, `anim/a04` poster, `img/i06.png` |
| 3 | T-IMG-3 | `i36` | p15 | generate — forest sleep | refs `img/i25.png`, `img/i24.png` |
| 4 | T-IMG-4 | `i37` | p16 | edit | golden `img/i16.png`; X7 ref `img/i05.png` |
| 5 | T-IMG-5 | `i38` | p23 | edit | golden `img/i31.png`; rhyme ref `img/i07.png` |
| 6 | T-IMG-6 | `i39` | p25 | edit | golden `derived/anim/a12.poster.webp` (full-res poster) |

On acceptance: download full-res, save to `docs/camping/storyboard/img/pNN.<ext>`,
update the record (`status: done`, `flow_media_id`, revision line).

**Optional tier (deferred, D8):** i22 flyer ("GRIEF CIRCLE — first session free —
Moonwhisper Ascending"), i11 tote ("RETURN TO YOURSELF"), i21 barrel stencil
("WINNING MENTALITY™").
