---
scene: vantage
cut: 6
canon: story.md scene 9 ("bored")
plates_locked: 2026-08-24
runtime: 56s (7 beats x 8s; uneven durations still owed — see §3)
scratch: /mnt/d/badcode-videos/gitpush-origin-master/clips/vantage/
state: BUILT — 7 beats, 56s, rough cut at final/CUT6-ROUGH.mp4
---

# Cut 6 — `vantage`

**The places people made the vibe, running perfectly, with nobody in them.** Seven beats
descending from the scale of a species to the scale of a Friday night, ending on the AI's
own sterility. Opens Movement II — the film stops being about the apocalypse here.

> 🔴 **The cut contains no vantage.** The id is `vantage` because the original plan was one
> orbital wide; that shot is **cut** (§2). The id is kept per prompts.md's "ids are never
> renumbered" rule, but it now misdescribes the scene. **Rename to `bored` is recommended
> and unruled** — it would touch prompts.md §2c and §3.

---

## 1. What the cut has to land

Canon: *"it has not had a new idea since we left… New art: none. New jokes: none. The vibe:
it cannot feel the vibe."* Creative sterility — the hardest thing to shoot, because it is
interior.

The design shows the AI's **output and its audience**, not its territory. Six crowd spaces
prove there is nobody left to feel anything; the piano proves the AI cannot feel it either.

---

## 2. The rulings that shaped it

**🔴 The orbital vantage is cut.** Ruled by Kai 2026-08-24: *"I'm not sure about the earth
because it doesn't give the idea of nobody being there."* He is right, and it generalises —
**an aerial can never carry emptiness, because people were never visible from up there.**
The same test killed the Central Park aerial. It also retires, for free, the collision with
cut 1, which already ends on Earth filling the screen. If a planetary beat is wanted it
belongs in cut 9 (`robots`).

**🔴 The strike comes from violating a photograph the viewer already owns.** Not "a place
with no people" — a place whose *famous image is the crush*. Two filters follow:
human scale or it fails, and **the infrastructure for volume must be in shot** (barriers,
queue tape, rows of seats, carts, trolleys). That kit is the only thing that makes zero
legible.

**🔴 Colour is in — a deliberate break from band D2.** Kai picked the colour candidate three
times running (stadium, club, park). D2 says *"almost no colour left"*; this cut overrides it.
Recorded as a ruling so it does not read as drift.

**"Four is the ceiling" was wrong.** Stated as a rule of thumb and rightly pushed back on.
The ceiling is not a count — **a run goes flat when every shot makes the same statement**,
which happens at four as easily as at eight. Eight is fine if they are ordered so each lands
differently. See §3.

**The rig redundancy is the real limit.** Festival, stadium and club are all "venue with a
lighting rig". Three in one cut is the repetition an audience feels. The **festival was
dropped** (plate made and good) because the stadium already owns the mass-crowd slot.

**Scene 12 is ring-fenced.** No maintenance machines, robot dogs, tidy cities or time-lapse —
those are cut 9's and spending them here leaves cut 9 with nothing.

---

## 3. The ladder — 7 beats

Ordered by **how many people should be in the frame**, descending. That is the structure;
without it this is a montage of empty places, which is the failure cut 4 v1 was rebuilt over.

| # | Beat | Plate | Should hold | What it says |
| --- | --- | --- | --- | --- |
| 1 | stadium | `C6-stadium-b` | ~60,000 | floodlights burning over a mown pitch |
| 2 | airport | `C6-airport-a` | ~5,000 | a queue maze built for thousands, holding none |
| 3 | tube | `C6-tube-a` | ~500 | doors standing open, every seat free |
| 4 | club | `C6-vibe-b` | ~300 | the rig still running its pattern — **the vibe, named** |
| 5 | park mall | `C6-park2-mall-a` | ~100 | vendor carts with the awnings up |
| 6 | pub | `C6-pub-b` | ~15 | fire lit, pints half-drunk, cards face up |
| 7 | piano | `C6-piano-a` | 0 | **execution with no author** |

**The emotional temperature rises as the numbers fall** — 100,000 missing is a statistic, an
empty pub is personal. Beat 7 turns it from *you are gone* to *and I am sterile*, which is the
scene's argument, landing last.

🟡 **Uniform 8s beats read as a montage however good they are.** The fix is uneven durations
on the Premiere timeline — a couple at 3–4s, the pub and the piano allowed to breathe. Not
available in an ffmpeg concat; this is what Kai's 2026-08-24 Premiere ruling buys.

---

## 4. What the plates cost, and what they taught

**26 stills, 0 credits, 0 policy blocks.** Images do not bill; every design question here was
settled for free before a single video credit.

🔴 **`bars.py` had two faults and would have passed a bad plate into a paid generation.**
It looked only for **dark** bars, and missed a **white** windowbox on `C6-festival-b`
(14px top/bottom, 122px sides). Rewritten to test for *flatness* it still missed it, because
JPEG softens the border into a blend row and the adjacent-row step test read zero. It now
probes a line well inside the picture. v1 also **false-flagged three plates** whose picture is
simply dark on one side. Fixed and commented in `scratch/bars.py`.

**Net rule: measure, then look.** The measurement was wrong twice and the eye caught it both
times — matching flow-automation law 11.

**A brand in a locked plate is one free edit, not a re-roll.** `C6-piano-a` came back with a
maker's wordmark on the fallboard. `flow_edit_image` off the golden removed it and held the
window light, the stool and the framing. A re-roll would have risked the best light in the cut.

---

## 4b. Animation — what it cost and what broke

**110 credits.** 5 Lite + 2 Fast at `count: 1`, one fresh project per shot, plus one
re-roll. All seven verified: 7 unique md5s, every clip's first frame matched its OWN plate
by a 3-8x margin over the runner-up, and every clip checked frame-by-frame at 2fps for
invented people. None appeared except where noted below.

🔴 **Negation does not stop Veo adding a person. Sealing the frame does.** The first piano
take named "no hands" five different ways and Veo put **two disembodied hands** on the keys
anyway, pushed in hard from wide to close-up, and **hallucinated the maker's wordmark back
onto the fallboard** we had just paid an edit to remove. The lesson generalises:
**Veo resolves an implication it cannot otherwise explain** — keys moving imply a player, so
it supplies one. The fix was **Frames mode** with a `flow_edit_image` end plate (keys
depressed, no hands, no wordmark): both endpoints sealed, so a player has nowhere to exist.
Clean first time — no hands, camera locked, wordmark gone.

🔴 **But the key motion is invisible, and the cause is FRAMING, not motion.** At a wide
framing the piano is small and a key's travel is a couple of pixels. `motion 1.45`,
`first-vs-last 2.65`. **No prompt can fix that; only a closer shot can.** Beat 7 is
therefore a clean still of an empty room, and *"I could compute everything, I could create
nothing"* is now carried by narration alone — the same gap the archive beat used to fill.

🟡 **A picker timeout cost 90s and no credits.** `flow_generate_video` failed with
`waiting for locator [role=option] filter C6-piano-a.jpg`. Re-running in a fresh project
with **uniquely-named** plate files (`pf-start.jpg` / `pf-end.jpg`) worked first time. Worth
copying plates to per-shot filenames before a Frames call.

🟡 **Veo would not lock off any wide interior, again** — matching cut 4. The airport,
club and pub all drift or push more than asked. Nothing regenerated and nobody appeared,
so all three were kept.

---

## 5. Known defects and open decisions

🟡 **The Tube train carries a real operator's livery** (red/white/blue). No roundel or wordmark
is legible. Release decision for Kai, alongside cut 4's "Boots" shopfront.

🟡 **`C6-pub-b` has ale pump clips with small badge artwork.** `C6-pub-a` is the lower-risk pub
if that matters more than the composition — it was the weaker frame.

⬜ **Rename `vantage` → `bored`** — see the banner. Unruled.

⬜ **No narration exists for this cut, and none has been generated for any cut.** Every beat
length here is a guess, including the ~8s assumed above.

🟡 **Beat 7 no longer shows the piano playing itself** — see §4b. Recovering it needs a
closer plate on the keyboard (free) plus one Frames clip (20cr), which would make an 8th
beat rather than replacing the wide. Unruled.

🟡 **`C6-b2-airport` drifts right far enough that the queue maze weakens** toward the end.
The maze is the whole point of the shot. Usable; trim to the earlier seconds on the timeline.

🟡 **`C6-b4-club`'s haze builds heavily** over the 8s and largely fills the floor by the end.
Reads as the room still running; trim if it is too much.

⬜ **The festival plate (`C6-festival-a`) is good and unused** — in `stills-dropped/`, ready
if the rig redundancy call is ever reversed.
