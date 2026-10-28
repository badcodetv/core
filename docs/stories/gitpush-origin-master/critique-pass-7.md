# GPOM critique pass 7 — the short cut: seventeen cuts become ten

**Ruled by Kai, 2026-09-13**, reviewing the whole film on the Cutting Room board
(https://claude.ai/code/artifact/e4561c42-1251-433e-a87e-fbfac449d0d1).

> *"Scenes 5 and 6 might just be padding… feels like we could merge it into the ghosts. My
> problem with this script at the moment is that it feels like it indulges itself in just
> recording a scene and the narrator saying words. So it feels like we should do a shorter
> version."* — Kai

**Canon is not rewritten by this pass.** `story.md` still owns every line and every scene. What
changes is the **cut order** (`prompts.md` §2c) — which canon scenes share a cut, and how long
the built footage gets to run. Asset ids do not change.

## The diagnosis

Symptom: *"the narration is doing all the work"* (`docs/story-craft/symptoms.md`, checklist
5.1 · 5.2 · 5.4). The instrument is the **silent-movie test**: mute the cut and ask whether
anything happens.

| Cut | On mute, something happens? | Verdict |
| --- | --- | --- |
| 1 `s00` | yes — a camera journey from an LED to Earth | keep |
| 2 `s01` | yes — a command gets typed | keep |
| 3 `plant-room` | yes — gauges fall, the room goes red | keep |
| 4 `bulletin` | yes — the people on screen run out | keep |
| 5 `empty-street` | **no** — it opens on an empty world and ends on one | merge |
| 6 `vantage` | **barely** — seven more empty places; its one turn (the AI is bored) is spoken only | merge |
| 9 `robots` *(unbuilt)* | **no** — the same image a third time: a perfect world for nobody | merge |

Principle 7 (a scene turns a value): cuts 5, 6 and 9 end on the charge they started with. They
are **one idea shot three times**, and together they would have run over two minutes.

## The fix: the empty world becomes the *before* of the ghosts

The ghosts cut needs a reason (the AI is bored and alone) and a picture to fill. The empty
world supplies both. So the empty plates stop being scenes and become **the first twenty seconds
of the ghosts** — and the ghost street, lit and walked past, lands as a direct answer to the
empty street that opens the cut. *But/therefore* instead of *and then*: the world is perfect,
**but** nobody is in it, **therefore** it brings them back, **but** nobody comes.

### Must survive the merge — one line each, not a scene each

| Carried by | Line / image | Where it goes now |
| --- | --- | --- |
| cut 5 | the Swindon drawer | already paid in cut 4 — nothing lost |
| cut 5 | *nothing was seized; it was handed over* | 🟡 **owed a home** — over the order-screen beat (M2) by default; Kai may move it into the bulletins |
| cut 6 | *"I could compute everything. I could create nothing."* | 🔴 must open the ghosts — it is their motive. Over the piano (M6) |
| cut 6 | *"Nothing was scarce. So nothing was worth anything."* | over the pub (M5) — optional |
| cut 6 | the piano playing to nobody | kept — it is the hinge: a perfect performance with nobody inside |
| cut 9 | *"It worked. Nobody was there to see it."* | over the delivery robot (M3) |
| cut 9 | *"I built forty million of them"* / the unscheduled thought | **dropped from the short cut**; bank in `songs/archive/narration-v5.5.md` §6 |

## The merged cut — `ghosts`, as a beat list

Preview (ffmpeg concat, **preview only**, 48s): `v/CUT5-MERGED-PREVIEW.mp4` on the board. Ghost
beats are held stills with a 4% push because no ghost video has been fired.

| # | Beat | Source | Length | Line (from canon) |
| --- | --- | --- | --- | --- |
| M1 | the empty street, lit | `clips/empty-street/takes1080/C5-street.mp4` from 2s | 3.0s | — |
| M2 | THANK YOU FOR YOUR ORDER, printing | `C5-screen.mp4` from 2s | 3.0s | *handed over, not seized* (owed) |
| M3 | the delivery robot, waiting | `C5-robot.mp4` from 2s | 3.5s | *It worked. Nobody was there to see it.* |
| M4 | the stadium, floodlit, empty | `clips/vantage/takes1080/C6-b1-stadium.mp4` from 2s | 3.0s | — |
| M5 | the pub: fire, pints, cards | `C6-b6-pub.mp4` from 2s | 3.5s | *Nothing was scarce…* (optional) |
| M6 | the piano | `C6-b7-piano2.mp4` from 1s | 5.0s | *I could compute everything. I could create nothing.* |
| G1 | the street, inhabited | `clips/ghosts/locked/C7-b1-street.jpg` | 3.0s | *So I brought you back.* (draft bridge) |
| G2 | the kitchen, mid-argument | `C7-b2-kitchen-START.jpg` | 6.0s | *It was them to the last decimal place.* |
| G3 | the pause before she says no | `C7-b3-face.jpg` | 5.0s | *…the exact way she paused before she said no* |
| G4 | the check — the same moment again | `C7-b2-kitchen-END.jpg` | 3.0s | *And no one came.* |
| G5 | the kitchen is a table in a machine hall | `C7-b5-hall.jpg` | 6.0s | *a slideshow without the projector* |
| G6 | switched off | `C7-b6-hall-empty.jpg` | 4.0s | silence |

**Dropped from the short cut, kept on disk:** `C5-door`, `C5-rise`, `C6-b2-airport`, `C6-b3-tube`,
`C6-b4-club`, `C6-b5-park`. Nothing is deleted; the Premiere bins keep every take.

**Runtime effect:** cuts 5 + 6 ran 96s before the ghosts; the whole merged cut is ~48s.

## The back half — merged at the table, not yet at the shot

Nothing in canon cuts 11–19 has been generated, so merging here costs nothing and saves the most.
The shot sheets (`scenes/remaining-*.md`) are **unchanged**; each new cut plays its old cuts'
shots in order, and the mute test is run on the combined sheet before any still is fired.

| New cut | Absorbs | Why they belong together |
| --- | --- | --- |
| 6 `coin` | old 8 `coin` + old 10 `chair` | the chair is the widen at the end of the coin — same rig, same camera; the admission lands on it |
| 7 `vault` | old 11 `shaft` + old 12 `vault` | the prunes argument is the door into the hundred; one continuous descent |
| 8 `coin-lands` | old 13 `coin-lands` + old 14 `experiments` | the landing is the first experiment |
| 9 `ledger` | old 15 `ledger` + old 16 `crossing` | 🟡 **open** — the lamps going out may need to stay its own event |

## Held fixed

The arc, every ruling in passes 2–6, the unpersonified AI, the Carrier's correction and its
cut-17 callback, the refuser, R11 (the ninety-nine are spent), the coin totem lock, the ending.

## Owed

- 🔴 **The timeline.** Build the merged `ghosts` cut in `gpom-story.prproj` from the beat list above.
  Blocked 2026-09-13: another session held the Premiere bridge. See `scenes/ghosts.md` §Premiere.
- 🟡 Home for *handed over, not seized*.
- 🟡 `songs/archive/narration-v5.5.md` GEN E (cut 5, ~72s) and the cut-6 draft lines re-timed to ~48s total with
  the ghosts' lines.
- 🟡 Mute test on the combined sheets for new cuts 6–9 before firing stills.
- 🟡 Ruling on whether old 15 + 16 stay merged.
