---
scene: bulletin (scene 3 / cut 4)
sequence: gpom-s03-bulletin-cut
built: 2026-09-21
runtime: 94.6s, 18 beats, 1920x1080 @ 24fps, picture only
status: PROPOSED CUT — awaiting Kai
---

# Scene 3 — the proposed cut

**Built autonomously 2026-09-21** while Kai was out, to his brief: *"cut a proposed version of
this scene, having absorbed all of the cinematography advice that we have… the important thing
about the third bit is that it has to have the sign in Swindon."*

## The argument

> **The collapse arrives as news, the news runs out of people before the world does — and all
> the way through, the people it stopped counting are still shouting.**

Two ladders running in opposite directions, which is what makes this a scene rather than a pile
of clips:

| | Bulletin 1 | Bulletin 2 | Bulletin 3 |
| --- | --- | --- | --- |
| **The news** | anchor + full studio | anchor alone, no crew | **nobody — an automated caption** |
| **humans on screen** | 5 | 2 | **0** |
| **The chorus answers with** | one man | a dozen | thousands |

The news empties. The terrace fills. Neither is stated.

## The cut

| # | Beat | s | Job |
| --- | --- | --- | --- |
| 1 | `01-newsreader` | 6 | Establish. The plate carries `200,000 OFFICE WORKERS FIRED` |
| 2 | `02-workers` | 3.7 | The cost — men leaving with boxes |
| 3 | `03-exchange-alive` | 3 | Establish the hall (pays off at 11) |
| 4 | `04-trading-floor` | 5 | **The thesis.** Traders with their feet up under a climbing green line — gate G3's beneficiary, on screen, benefiting |
| 5 | `05-london` | 3 | The public reading it |
| 6 | `06-shibuya` | 3 | …everywhere |
| 7 | **`07-CH1-one-man`** | 8 | **Chorus 1.** One man, empty terrace |
| 8 | `08-anchor-alone` | 5 | Same studio, no crew |
| 9 | `09-presser` | 5 | The plate carries `ACTUALLY GOOD FOR THE MARKETS` |
| 10 | `10-bank-empty` | 3 | Short **deliberately** — cuts before the known morphing-chair defect |
| 11 | `11-exchange-empty` | 5 | **The reveal.** Shot 3's hall, now litter |
| 12 | **`12-CH2-pub`** | 8 | **Chorus 2.** A dozen |
| 13 | `13-caption` | 8 | **The 0-humans beat.** New — see below |
| 14 | `14-aerial` | 5 | A drone feed; nobody is flying it |
| 15 | **`15-SWINDON`** | 6 | 🔴 **The sign. Kai's requirement.** Undamaged, ordinary, smoke on the horizon. Held long enough to read, short enough not to explain itself |
| 16 | `16-CH3-stand` | 6 | **Final chorus.** Thousands |
| 17 | `17-CH3-face` | 6 | One face inside the mass — **the only close-up in the scene** |
| 18 | `18-powerdown` | 6 | **The button.** Empty Piccadilly, dead screen |

**Why that button.** Shot 1 is a lit screen telling us the news; shot 18 is that screen dead in
an empty city. The last shot closes what the first opened. It also *is* the lyric's
`[power-off drop: sudden silence, electrical hum dying]`.

**The pattern, broken once.** Every bulletin runs medium → wide as the world empties, and every
chorus answers with people. The final chorus breaks it by going to a close-up — the one time the
film looks a single person in the face. A pattern exists so the break reads as a break.

## What was made new (6 clips)

| Clip | Why |
| --- | --- |
| `ch1-one-man`, `ch2-pub`, `ch3-stand-v2`, `ch4-face` | The choruses. **Nothing existed for any drop** — all 15 inherited clips were bulletin material |
| `studio-empty-new` | Derived from the `anchor-alone` frame with `flow_edit_image`: the same studio, same lamp, same softboxes, nobody there. Completes the 5→2→0 ladder |
| `b3-caption` | ffmpeg captions over that empty studio. **ffmpeg is the only lane that can write text** |

## 🔴 The salute problem — caught and fixed, do not undo

The first crowd take (`ch3-stand`) resolved at 2–4s into **rows of stiff raised arms in unison —
an unmistakable fascist salute.** In a film aimed at a working-class reader drifting right, that
frame makes them the thing the far right says they are. Unshippable.

Fixed by re-rolling with the gesture named out of the prompt — *"their arms stay down at their
sides or clap; a few hold scarves stretched between their hands at chest height; nobody raises a
straight arm and no arms point upward"* — then cutting from t=1.8s, after the still's inherited
raised arms settle. **Any future crowd shot in this film gets the same clause.**

## Two other fixes made on review

- **`02-workers` was cut from the wrong end.** The first 4s are a car sweeping across and
  blocking the workers entirely. The clean window is 4.3–8s. Re-cut from there.
- **`C4-p1-london-b` dropped** — it repeated `london-a`'s job, and it is the plate with the
  visible "Boots" shopfront. Two reasons, one answer.
- **`C4-studio-empty` (v1) dropped** — the small CRT shot never matched the new anchor studio.
  `studio-empty-new` replaces it properly.

## 🔴 What this cut does NOT have

**The music.** No take of either song is anywhere on `D:`, so every duration here is designed
from the lyric structure, not measured against a track. **Expect all of it to move** once the
track exists — the choruses especially, which are currently 8s guesses.

Beat lengths are baked into trimmed files in `clips/bulletin-v2/cut/`. **The full-length
originals are untouched** in `takes/`, `takes1080/` and `chorus1080/`, so any beat can be
re-extended rather than re-rendered.

## Owed

- Kai's verdict on the chorus device (the counter-ladder) — it is the one real invention here.
- The track, then a re-time.
- Narration: none exists for this cut.
