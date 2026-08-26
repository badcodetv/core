---
scene: bulletin
cut: 4
canon: story.md scene 7
built: 2026-08-23
rebuilt: 2026-08-24
runtime: 120s (15 beats × 8s)
scratch: /mnt/d/badcode-videos/gitpush-origin-master/clips/bulletin-v2/
supersedes: the 13-beat build of 2026-08-23 (/mnt/d/badcode-videos/gitpush-origin-master/clips/bulletin/)
---

# Cut 4 — `bulletin`

**The collapse, told entirely as news.** Three stories from the song — the redundancies, the
banks, the autonomous army — reported across years we never date on screen.

> 🔴 **Rebuilt 2026-08-24.** The first build put all three bulletins over *unrelated* pictures.
> Kai: *"it's not dramatic enough… what we have is sort of abstract background art."* He was
> right, and the craft toolkit names it: run **McKee's VO test** on the original and muting
> bulletin 2 costs the picture nothing, because an emptying railway station never carried
> information about banks. Mamet's **silent-movie test** fails outright on phases 2 and 3.
> We had reached for **Curtis's two tracks** — illustrative narration over a free-riff image
> layer — which `toolbox.md` lists *with a warning attached*.

---

## 1. The shape — three packages, one grammar, degrading

Each bulletin gets a **real news package**, and what degrades is **the news's ability to
report** — not the furniture. Iannucci's rule: the drama is in the institutional response,
not the crisis.

| | Bulletin 1 — redundancies | Bulletin 2 — the banks | Bulletin 3 — the armies |
| --- | --- | --- | --- |
| **Anchor** | live, composed, full studio | live but alone — no crew | gone — an automated caption |
| **Footage** | a proper cut package | one static feed | grainy aerial, no edit |
| **On the ground** | reporter + crowds | none | nobody at all |
| **Beneficiary** | the market rising | the government thanking it | nobody left to benefit |

🔴 **The ladder is measured in humans on screen: five, then two, then none.** The thing running
out is people, not production values. That is the whole device.

| # | Beat | Source | Package |
| --- | --- | --- | --- |
| 1 | `C4-p0-newsreader` | v1, kept | **1 — the redundancies** |
| 2 | `C4V2-workers` | new | 1 |
| 3 | `C4V2-exchange-alive` | new | 1 |
| 4 | `C4V2-trading-floor` | new | 1 |
| 5–7 | `C4-p1-london-a/-b`, `C4-p1-shibuya` | v1, kept | 1 |
| 8 | `C4V2-anchor-alone` | new | **2 — the banks** |
| 9 | `C4V2-presser` | new | 2 |
| 10 | `C4V2-bank-empty` | new | 2 |
| 11 | `C4V2-exchange-empty` | new | 2 |
| — | ⬜ automated caption over a held frame | **post job, no credits — held frame unruled** | **3 — the armies** |
| 12 | `C4V2-aerial` | new | 3 |
| 13 | `C4V2-swindon` | new | 3 |
| 14 | `C4-studio-empty` | v1, kept | 3 |
| 15 | `C4-p4-london` | v1, kept | 3 |

Rebuild: `assemble.sh` in the scratch folder. ⚠️ **The concat is preview only** — per Kai's
2026-08-24 ruling the deliverable is the individual clips on a Premiere timeline, and the
`BEATS` list is the canonical import order.

---

## 2. The rulings that shaped it

**The world still ends off-screen.** `story.md`'s device list says *"the world ends off-screen;
the composure is the horror."* The rebuild shows **the coverage, never the event** — a press
conference is not a takeover, an aerial of the aftermath is not the battle. The constraint cost
nothing and made every shot more specific.

**The aerial is a feed, not a movie shot** — and nobody is flying it. In a story about
autonomous machines the camera being autonomous too is thematically exact, and it dodges the
"who is up there?" question, because nobody is. It also keeps the degradation honest: a
collapsing newsroom cannot afford a helicopter, but it can rebroadcast a drone.

**Swindon is a plant, not a punchline.** Ruled by Kai 2026-08-24: the drawer-in-Swindon joke
belongs to the song. The film gets one deadpan road sign after the battlefield, undamaged and
ordinary, with a column of smoke on the horizon behind it — the implication that the battle was
*there*, and nothing said. Damaging the sign would explain the joke. 🟡 Consequence for cut 5:
its draft line *"It was in a drawer. In Swindon."* would make the plant explicit one scene later.
**Recommended cut; not yet ruled.**

**The exchange floor is the cut's anchor.** The same hall alive in bulletin 1 and empty in
bulletin 2, so the audience re-recognises the room and clocks what changed. Two anonymous
open-plan offices cannot do that. 🟡 The plates came back **period** (CRTs, 80s jackets) — kept,
because it reads as archive and matches the house film register, but it is a visible choice.
🟡 The two halls are separate generations and do not match exactly; deriving the empty one from
the alive plate with `flow_edit_image` would fix that for free.

**The beneficiary is on screen, benefiting.** Gate G3 wants the beneficiary named; beat 4 shows
traders laughing with their feet up under a climbing green line, cut against beat 2's workers
carrying boxes out. That pairing is the thesis in two shots.

**The phase-1 newsreader is the phase-2 studio, intact.** Same slatted wall, round columns,
square softboxes, domed pendant lamp — so beat 8 is *that room, later*, at no extra cost.

---

## 3. Load-bearing text goes in the PLATE

Proven twice now. **Nano Banana Pro sets the type; Veo holds it.**

- `200,000 OFFICE WORKERS FIRED` — correct first try, correctly curved to a curved screen.
- `ACTUALLY GOOD FOR THE MARKETS` on a teleprompter — measured identical, sharp and correctly
  oriented at 0s, 2.5s, 5s and 7.5s.
- `SWINDON` on a road sign — held.

**Images do not bill.** Never ask Veo to render text and never reach for post-compositing first.

🔴 **The mirroring trap.** Asked for a teleprompter from the audience side, Nano Banana rendered
the text **reversed** — physically correct, and useless for a joke the viewer must read. The fix
is a **three-quarter angle** so the glass faces partly to camera, not a request to break physics.

🔴 **~1 in 5 Nano Banana Pro 16:9 outputs come back with letterbox or windowbox bars baked into
the pixels**, and it is invisible in the returned dimensions — everything reports 1376×768.
Measured: 3 of 14 in one batch, 1 of 10 in another. Check before animating, not after.

---

## 4. Holding a screen — the technique

Name the real-world motion first and hard → hold the screen explicitly (*"the screen keeps
showing exactly the same picture from the first frame to the last: the same size, the same
brightness, no flicker, no flare, no blowing out, no cut to another shot, no change of
channel"*) → *"the camera stays where it is."*

Measured across the rebuild: **screen swing 0–3/255 on every shot with a screen.** For a screen
meant to read as **dead**, invert the clause and name what must not appear.

---

## 5. What cost the most, and why

🔴 **Veo will not lock off a wide interior or an aerial.** Three shots in this rebuild drifted
into a slow push despite an explicit lock-off clause, across both tiers — matching v1's
`p4-london`, which drifted across four takes and three prompts. **Ask for the move you want
rather than fighting for stillness.** Nothing regenerated and no one appeared, so all three
were kept.

🔴 **An unmapped failure card burns the full 480s clock.** The presser died on *"Audio generation
failed. Please try a different prompt or send feedback. You have not been charged for this
generation."* That is a **retry-unchanged** condition with credits refunded — but its wording is
not in `failure-card.ts`, so it timed out instead of aborting in seconds. The retry worked first
time, unchanged. **Read the timeout dump before retrying; it names the cause.**

🔴 **Flow now offers silent videos.** The same card said *"You can update your settings to return
silent videos."* Our toolkit records that Veo audio is always on and cannot be disabled — **that
is out of date.** Enabling it would kill this failure class and remove the `-an` step. Not yet
enabled; it is global project state.

**A plate with an ambiguous bright patch is a paid re-roll** (v1: 80 credits on `p4-london`,
killed for free by one `flow_edit_image`). **A cluttered project hands back old media as if it
were new** — one fresh project per shot. **Never generate a diagnostic image into the project you
are about to animate in** (v1: 40 credits). **Upload from the WSL filesystem, never `/mnt/c`.**

**Cost of the rebuild: 150 credits** — 6 Fast + 3 Lite, `count: 1` throughout, one refunded
failure.

---

## 6. Grade and finish

Screen swing measured 0–3 on every held screen, so there was nothing to correct and all nine
went straight to the plain upscale:

```bash
ffmpeg -i in.mp4 -vf "scale=1920:1080:flags=lanczos,setsar=1" \
       -c:v libx264 -crf 17 -pix_fmt yuv420p -an out.mp4
```

🔴 `hold_grade.py` **fails when the brightest object in frame is a screen that legitimately
changes**, because it then measures content rather than lighting (v1: 3 of 7 clips tripped it;
`p3-dark` reported 97.2/255 of "drift" that was static). **Still owed:** a monotonicity guard so
a non-monotonic "drift" refuses the correction rather than clamping.

---

## 7. Superseded — do not re-run

| Dropped | Why |
| --- | --- |
| `C4-p2-station`, `C4-airport1`, `C4-airport2` | The abstraction — emptying transit carrying no information about the story being read |
| `C4-p3-studio-man`, `C4-p3-collapse`, `C4-p3-dark` | Set-decay as degradation; replaced by the package degrading |
| `C4-p4-shibuya` | Cut for length; the London callback carries the ending alone |
| `C4-mall*`, `C4-tokyo*`, `b3-wide`, `b1-*` | v1-era, already superseded |

---

## 8. Known defects, unresolved

🔴 **`C4V2-bank-empty` has a chair that morphs into another chair.** Spotted by Kai 2026-08-24.
He will cut around it on the timeline; not worth a re-roll.

🟡 **Three clips drift into a slow push** (`bank-empty`, `exchange-empty`, and v1's `p4-london`)
where a lock-off was specified. Kept — see §5.

🟡 **Beat 14 (`C4-studio-empty`, inherited from v1) no longer matches.** It is a small CRT-ish
monitor shot and sits oddly against the new anchor studio. Re-shoot or drop.

🟡 **A "Boots" shopfront is visible** in the `p1-london-b` plate. A release decision for Kai,
separate from whether it generated.

⬜ **The automated-caption beat that opens bulletin 3 has not been made.** Free in post; what it
sits over is unruled — candidates are the frozen last frame of `bank-empty`, the empty studio,
or colour bars.

⬜ **No narration exists for this cut, and none has been generated for any cut.**
[`songs/narration.md`](../songs/narration.md) carries written boxes for cuts 1–3 only, still at
`status: draft`. Every beat length in every cut — including the 8s assumed here — is a guess.

⬜ **Year cards** (2033/34/35) are still unruled, as is cut 3's `2032` card.
