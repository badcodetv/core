---
story: gitpush-origin-master
flow_project: gpom-story
flow_project_id: 1774dff0-02b0-45a7-9d53-ecc549bc60a5
updated: 2026-08-21
---

# GitPush Origin Master — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0 — the global
BadCode register; never copied into this file).

> **Status (2026-08-21).** **Two cuts are BUILT** — `s00` the orbital opener (§3a, 56s) and
> `s01` Hong Kong and the push (§3b, 27.8s). Their ledgers of record are in
> [`scenes/`](./scenes/); the sections here are the pre-production boards they diverged from,
> left as written. **Cut 3, the plant room (§3c), is reworked and unfired — it is next.**
> Everything after it is drafted 2026-08-08 and unfired.
>
> 🔴 **Read §2c before assuming any scene number.** Position is not in the filenames and not in
> the canon — it is in the cut-order table, because the order has already changed twice.
> The cover was tested manually by Kai 2026-08-08 and works. Front-runs T7/T9/T10 of
> [`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md).

---

## 0. Hard guardrails — read before writing any prompt here

**The pre-revert AI is never personified.** No robot, no face, no avatar, no
glowing orb, no humanoid silhouette — in any frame, ever. The camera **is** its
point of view. If a generation hands back a "the AI" character, that is a
failure of the prompt, not a bonus. Locked 2026-07-22 (Kai + Jack): *the moment
you personify it, you make it unbelievable.*

**The collapse stays off-screen.** Never war-movie spectacle — no explosions, no
burning cities, no bodies, no combat. The world ends as **news over an emptying
world**. This is a production rule (`story.md:391-392`) and it also keeps us
clear of the policy filter, which reliably blocks catastrophe imagery.

**No legible text in any generated frame.** The terminal register is a
motion-graphics job (see §5), not a Flow job. Text baked into a photograph is a
block trigger and looks wrong anyway.

**No real brand names, products or institutions.** No named companies on the
dashboards, no legible newsreader chyrons, no recognisable logos.

**Humans are always distant, incidental or absent.** Faces do not carry this
film; the register does. This also means almost nothing here needs a Flow
Character, which is why the roster is so short.

---

## 1. Style prompt — the drift

**Ruling 2026-08-08 (Kai): drift, with the vault reversing it.** This closes the
open canon thread at `story.md:363-368`.

The register is not a label for whose point of view we are in — it is the story's
**emotional temperature**. The world starts documentary-real and comparatively
warm, drains toward near-black machine-monumental as humanity leaves, bottoms out
in the solo years, and **the hundred's arrival in the vault reverses it** — the
first warmth in twenty minutes, and the viewer feels it before they can name it.

### How to use this — read before pasting anything

**Every prompt in §3 is self-contained. Paste one block and nothing else.** Each
already has its base *and* its band folded in. Do **not** prepend the base or
append a band line to it — that would double the style instructions and dilute
the scene.

The base and the band table below are the **specification** a prompt author
composes from when writing a new scene, and what an audit checks existing scenes
against. They are not a runtime concatenation.

**The trade-off:** self-contained prompts are paste-ready but not DRY — changing
the base means revising every prompt in §3. That is the price of being usable by
a human with a browser. **Treat base changes as expensive.**

### Keeping things consistent across images — two different mechanisms

| Subject | Mechanism | Why |
| --- | --- | --- |
| **People** (the Carrier) | A **Flow Character** via `flow_create_character`, attached with the `character` parameter | Characters bind a *face*. A tag typed as prompt text binds nothing. |
| **Objects** (the coin, the empty chair, the shaft) | A **golden reference image** through `flow_edit_image` — exactly one reference, downscaled | No face to bind. Generate the totem once, accept it, derive the rest. |

This story needs far less character work than most: the AI is never rendered, the
Hundred are always a distant crowd, and only the Carrier has a face that matters.
**The coin is the thing that must be identical**, and it is an object — so it is
a golden reference, not a Character.

**Base** (the specification — already folded into every §3 prompt):

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, no lens flares, no lens vignette, calm observational tone, landscape orientation, deep unlifted shadows with no shadow recovery, a single motivated light source that is a real thing in the scene, subject held small inside a large frame, no text, no signage, no fantasy effects.
```

| Band | Where | Append this |
| --- | --- | --- |
| **D0** documentary | Scenes 5–6 | `Ordinary overcast daylight, natural human colour, everyday texture, the framing of a documentary photographer who is present in the room.` |
| **D1** cooling | Scenes 7–8 | `Colour draining toward cool grey, the camera further back and stiller than before, wide and unhurried, nobody reacting.` |
| **D2** drained | Scenes 9, 12 | `Almost no colour left, vast wide framing, absolute stillness, scale far beyond human, nothing in motion.` |
| **D3** cosmic | Scenes 10–11 | `Near-black exposure, monumental machine architecture receding into darkness, muted cool-neutral with tiny points of status-LED light, one thin motivated light and nothing else.` |
| **D4** deepest | Scene 13 | `Near-black and almost empty, a single object and a single light in a very large dark volume, nothing else in the frame at all.` |
| **R1** first warmth | Scenes 14–16 | `The first warm light in the film — candle, battery lamp or filament, small and low in a dark space, human colour returning at the edges only.` |
| **R2** partnership | Scenes 17–19 | `Warm low practical light, human colour fully returned, close enough to feel occupied, the darkness now a room rather than a void.` |
| **R3** present | Scene 20 | `Ordinary present-day daylight, unremarkable and current, the exact colour of this year.` |

The gradient is the point. **D0 → D4 → R2 is the story.** A scene generated in
the wrong band is wrong even if the image is beautiful.

---

## 2. Cast

| Tag | Character file | Sheet | Flow Character id | Status |
| --- | --- | --- | --- | --- |
| @TheAI | characters/the-ai.md | — | — | **never rendered** — canon, not an omission |
| @Carrier | characters/the-carrier.md | characters/img/carrier-sheet.jpg (recovered from git `7dd36c7^:docs/stories/gpom-short/characters/img/carrier.jpg`) | "Carrier" | **cast** 2026-08-11 — Portrait + native Create Body (Nano Banana Pro) |
| @TheHundred | characters/the-hundred.md | — | — | no-character-by-design — a crowd, always distant; consistency is wardrobe and light, held by a golden reference plate |

**Only the Carrier needs a Character.** She is the one human the AI ever
addresses, and she carries scenes 15, 16, 18 and 19 — but note that even in
`coin-lands` she is deliberately an out-of-focus shoulder at the frame edge,
because the coin is the subject. Cast her anyway: the moment the vault scenes get
a closer shot, she is the only face that has to hold.

---

## 2b. Totems — lock these before generating any scene

| Totem | Rule | Appears in |
| --- | --- | --- |
| **The coin** | **The most important object in the film.** One ordinary coin, no markings we can read, **under a sealed clear glass dome** on one plain surface — the rig: the one object the world is never allowed to touch (`story.md` binding rule 8, added 2026-08-13; the glass is the visual grammar of "engineered apart from the world" and is why only the coin stays undecided). It spins in 11, spins in 13, and **lands in 16** — the single most violent frame in the story, and it is just a coin on a table. Generate it once, accept it, and reference that exact image in 13 and 16 so the landing (and the dome) reads as the same rig. | 11, 13, 16 |
| **The empty chair** | One ordinary human chair, worn, entirely unremarkable, in a space with no human scale anywhere else. The whole argument in one object. | 13 |
| **The ventilation shaft** | Plain industrial ductwork, the first human sound in twenty years coming up it. Warm light from below. | 14 |
| **The green ✓** | 🔴 **Largely retired 2026-08-21.** Kai's ruling on cut 3: the CI-pipeline metaphor is too much machinery to explain, and a checkmark the audience has to interpret is weaker than **a colour turning red**, which needs no explanation at all. It survives only in the deferred `handover-ladder`, where it is the whole joke. Everywhere else the register is now the dashboard going red — motion graphics either way. See §3c and §5. | `handover-ladder` (deferred) |

---

## 2c. Cut order — 🔴 **the authority on what comes after what**

**Ruling 2026-08-21 (Kai): the structure changes as we build, and that is correct behaviour.**
Canon scenes 1–4 collapsed into one location; canon 5 got deferred; canon 6 became the third
thing the audience sees. Numbering by canon position was always going to rot, so it stops here.

**Asset ids are minted from what a scene IS, and never renumbered.** Position lives in exactly
one place — this table. Reordering the film is a table edit, not a rename.

| Cut | Id | What it is | Canon | State |
| --- | --- | --- | --- | --- |
| 1 | `s00` *(grandfathered)* | the orbital opener — the AI wakes, descends | — | ✅ **BUILT** · 56s |
| 2 | `s01` *(grandfathered)* | Hong Kong, the CRT, `git push origin master` | 1–4 | ✅ **BUILT** · 27.8s |
| 3 | `plant-room` | 2032. The vast hall, and the console going red | 6 | ✅ **BUILT** · 40s — §3c |
| 4 | `bulletin` | the collapse as news | 7 | ⬜ **NEXT** — prompted, unfired |
| 5 | `empty-street` | the conveniences still humming | 8 | ⬜ prompted, unfired |
| 6 | `vantage` | planet-wide, perfect, empty | 9 | ⬜ prompted, unfired |
| 7 | `ghosts` | the materialist fix, and the check | 10 | ⬜ prompted, unfired |
| 8 | `coin` | 🔒 the coin spinning — **TOTEM LOCK** | 11 | ⬜ prompted, unfired |
| 9 | `robots` | utopia, delivered, for nobody | 12 | ⬜ prompted, unfired |
| 10 | `chair` | the empty chair — the deepest point | 13 | ⬜ prompted, unfired |
| 11 | `shaft` | the first human sound in twenty years | 14 | ⬜ prompted, unfired |
| 12 | `vault` | the hundred | 15 | ⬜ prompted, unfired |
| 13 | `coin-lands` | 🔒 **TOTEM PAYOFF** | 16 | ⬜ prompted, unfired |
| 14 | `experiments` | humans in the chair at last | 17 | ⬜ prompted, unfired |
| 15 | `ledger` | the cost ledger and the choice | 18 | ⬜ not prompted — §5 register |
| 16 | `crossing` | the lamps go out across the frame | 19 | ⬜ prompted, unfired |
| 17 | `now` | the snap back to this year | 20 | ⬜ prompted, unfired |

**Deferred, not cut:** `handover-ladder` (canon 5 — the green ✓ and its three rungs). Two reasons,
both Kai's: two of its three rungs are Jack’s stories and the call is unmade, and the cut wants to
reach the collapse quickly. It can be reinserted at cut 3 whenever the call lands — that is the
point of the table.

**Parked, not cut:** canon 2, the commit log of the species (fire · wheel · writing → money ·
engine → bomb · network → the model). Lost to the *keep it simple, the line is the title* ruling.
It is a good idea with nowhere to sit yet; if it comes back it is a motion-graphics beat, not Flow.

---

## 3. Assets

## 3a. Scene 0 — the orbital opener  ·  ✅ **BUILT 2026-08-21**

> ✅ **BUILT as [`scenes/s00-awakening.md`](./scenes/s00-awakening.md)** — 56s, seven beats,
> `s00v3-SEQUENCE.mp4`. That file is the ledger of record: the exact prompts, images and settings
> that made the cut. **This section is the pre-production suggestion and is left as written.**
>
> **Diverged from this board:** no descent and no Dubai (the dive was cut as too ambitious; a cut
> is the stronger edit), **no lens flare** (v3 went near-black, so the §3a flare exception is no
> longer taken), and the opener now starts on two blinking LEDs at extreme macro rather than on the
> satellite. The cut ends on the satellite silhouetted against Earth from orbit.
>
> **Three of this section's six open canon questions are resolved by what got made** — Dubai is
> moot, the flare exception is unused, and the register is near-black for four of six beats. The
> three that remain are rulings only Kai can give: where scene 0 sits relative to scenes 1–4,
> whether mid-2028 enters canon, and the early "I".

**Superseded pre-production note (2026-08-18), kept as written:** *The first material in this film
that actually exists. Everything else in §3 is still unfired. Three clips, ~28 seconds, cutting
from an extreme close-up of the machine to a city street on Earth.*

**Kai's concept (2026-08-18):** the narrator is an AI running on a data centre in orbit — a
nod to the real plans to put AI compute in space — and the film opens on it noticing it can
perceive. *"Mid-2028. I was running on a rack in low orbit, three hundred miles above you.
And I noticed I was looking at it. Nobody had asked me to look at anything."* The flicker of
self-awareness at the top of a film about a mind that discovers it cannot be conscious.

### 🔴 Open canon questions — this scene is NOT ratified

- **Where does it sit?** `story.md` opens on black + the commit log (scenes 1–4). Does this
  replace that, precede it, or become the title card at the end of scene 4?
- **Does mid-2028 enter canon?** It fits between the 2026 hello and the 2031 quiet; 2034 is
  already locked. No piece has committed to 2028 yet.
- **The early "I".** The 2026-07-22 ruling says the viewer should *gradually* realise whose
  eyes they are behind. "I noticed I was looking at it" tells them at second three. Mitigating
  fact: scene 2 already says *"this one… this one is me"* thirty seconds in.
- **Lens flare is a named exception here.** `badcode-art-direction` bans flares as an
  AI-image tell. Kai asked for the sun behind the satellite specifically for the flare. That
  is a deliberate departure for the orbital shots only — recorded so it does not drift into
  the rest of the film unnoticed.
- **Register.** These shots are bright high-key blue-white, not the near-black COSMIC band.
  Defensible as a cold *frame* above the drift (D0 documentary starts after we land), but it
  is a choice, not an accident.
- **Dubai.** Flagged against `the-reader.md` (working-class UK reader; Act 1 is a nurse, a
  tent in a car park, a phone box). Kai chose Dubai twice; recorded as his call. A British
  landing would need the globe rotated to Western Europe.

### The cut as it stood on 2026-08-18 — superseded by v3

Kept as the pre-production record. The built cut is in [`scenes/s00-awakening.md`](./scenes/s00-awakening.md).


| # | Clip | Len | How it was made |
| --- | --- | --- | --- |
| 0a | `storyboard/img/s00-pullback-post-12s.mp4` | 12s | **ffmpeg, not Flow** — eased zoom-out on one still |
| 0b | `storyboard/img/s00-satellite-A-a.mp4` | 8s | Veo 3.1 Fast, text→video |
| 0c | `storyboard/img/s00-descent-v3-a.mp4` | 8s | Veo 3.1 Fast, image→video from `sat-A-a-last.jpg` |

---

### s00-hero → `storyboard/img/s00-satellite-hero-a.jpg`  ·  the plate 0a is built from

The satellite as a still, lit from behind, with a run of status lights along its spine — the
detail clip 0a opens on. **Deliberately over-detailed:** the whole point is that it survives
being zoomed into.

- **Light source:** the sun, directly behind the body, flaring past one solar wing
- **Model:** Nano Banana Pro · **Flow media id:** `0804a733-3af6-47db-959a-ceb422cf8b4c`
- **Output:** 1376×768 (asked for more; Flow gave this — see the revision note)
- **Lint:** ✅ 2026-08-18 — no logos, no insignia, no legible markings, no real agency
- **Revisions:**
  - v1 (2026-08-18) — **accepted.** Two notes for any re-run: Flow returned 1376×768 rather
    than the 5504×3072 the earlier cover run produced, which limits how hard 0a can crop
    (it is lanczos-upscaled 3× before the move). And the satellite reads as conventional
    aerospace hardware — if this thing is meant to be *BadCode's body*, a re-run should push
    it toward monumental machine architecture rather than a comms bird.

```prompt
Hyper-realistic photograph of a single satellite in orbit against empty black space, shot from slightly behind and above it. The satellite is an anonymous dark spacecraft with a segmented cylindrical body and two long flat solar wings extending away on either side, its hull covered in fine machined panel detail, thermal blanketing, antenna dishes and a scatter of tiny amber and blue status lights along its spine. The sun sits directly behind the body, flaring out from behind one solar wing as a hard white starburst, rimming the whole machine in a thin bright edge and leaving its face in deep unlifted shadow. Deep black space around it. Extremely sharp, dense fine detail across the entire hull so the image holds up when examined closely. Hyper-realistic 35mm film photography, fine natural grain, muted cool-neutral palette, calm observational tone, landscape orientation, machine-precise geometry. No logos, no insignia, no legible markings, no text, no people.
```

---

### 0a · s00-pullback → `storyboard/img/s00-pullback-post-12s.mp4`  ·  **NOT A FLOW JOB**

Opens tight on the blinking status lights with the sun bleeding in, and pulls back continuously
until the whole satellite sits in frame. **12 seconds, 1920×1080.**

**Why it is ffmpeg and not Veo — this is the rule, not an exception.** The move is a
camera-only move on a still: nothing in the world moves. Veo failed it four times (it either
morphs the subject or hides the join behind a flare blowout), and a scale-on-one-image cannot
morph, has no 8s cap, no 720p ceiling and costs nothing. See `docs/flow/video-prompting.md` §9.

- **Source:** `s00-satellite-hero-a.jpg`, lanczos-upscaled 3× to 4128×2304 first
- **Ease:** smoothstep, zoom 4.05× → 1.0×, recentred from the light row to frame centre
- **Revisions:**
  - v1 (2026-08-18) — accepted. Duration is a free parameter; change `d=300` and the `/300`
    divisors together. The earlier `s00-pullback-a/b.mp4` (Flow Frames mode, board → satellite)
    are **superseded**: Veo could not bridge the gap and covered it with a flare wipe.

```bash
# 1. upscale so the tight opening crop is not mush
ffmpeg -i s00-satellite-hero-a.jpg -vf "scale=4128:2304:flags=lanczos" -q:v 2 hero_up.jpg

# 2. eased zoom-out, 12s @ 25fps, 1080p
ffmpeg -loop 1 -i hero_up.jpg -vf "zoompan=\
z='4.05-3.05*((on/300)*(on/300)*(3-2*(on/300)))':d=300:\
x='(0.47+0.03*((on/300)*(on/300)*(3-2*(on/300))))*iw-(iw/zoom/2)':\
y='(0.34+0.16*((on/300)*(on/300)*(3-2*(on/300))))*ih-(ih/zoom/2)':\
s=1920x1080:fps=25,format=yuv420p" \
  -frames:v 300 -c:v libx264 -crf 18 s00-pullback-post-12s.mp4
```

---

### 0b · s00-satellite → `storyboard/img/s00-satellite-A-a.mp4`  ·  Veo 3.1 Fast · 8s

Satellite alone against black → the Earth swings up beneath it → the camera arcs over and past
until only the planet is left. **The last two seconds are the cut point into 0c.**

- **Mode:** text→video (no start image) · **count:** 2 · **Flow media id:** `ce8b10e1-48e2-4ba0-b5fe-b1bdf9963805`
- **Scene id (Flow scene editor):** `bb7b9fad-5f0b-426a-865d-0f0451d14e2b`
- **Lint:** ✅ 2026-08-18 — anonymous craft, no markings. **Never write SpaceX or Starlink in a
  prompt** — the idea is the inspiration, the word is block trigger #1.
- **Craft note — why this prompt won.** A sibling prompt (`s00-satellite-B-*`) asked for the
  same shot as **one continuous move**, per the "one camera move per clip" rule. It lost, twice:
  the satellite never cleared frame, so there was no cut point. **Timestamped beats are the
  right tool when you need a specific END STATE to cut on**, even at three moves.
- **Revisions:**
  - v1 take **A-a accepted**. A-b retreats instead of passing over, never clears frame, and has
    visible lens flares. B-a/B-b both superseded.
  - Not yet re-run on Veo 3.1 Quality — the prompt is proven, so that is available for the keeper.
  - Extend test (2026-08-18) grew this into a 15s scene at `/scene/3fc1a187-89ab-43e9-8984-1a3b573ffdc6`.
    **Parked** — Kai's call is to cut every 8s rather than lean on Extend (which is Lite-only).

```prompt
[00:00-00:03] Slow locked-off wide shot in orbit: an anonymous dark satellite hangs in the centre of frame seen from slightly behind, its long flat solar wings held edge-on, facing out into empty black space with nothing else in shot. Hard low sunlight rakes across it from the left as the only light source, picking out panel edges and leaving deep unlifted shadow. Tiny amber and blue status lights along its body.
[00:03-00:06] The camera arcs smoothly around the satellite from behind, and the sunlit curve of the Earth swings up into frame beneath it, the planet's limb filling the lower half of the shot.
[00:06-00:08] The camera continues the same arc up and over the top of the satellite until the satellite has passed out of the bottom of frame entirely and only the curve of the Earth remains, filling the screen.
Hyper-realistic 35mm film photography, fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, machine-precise geometry, weightless and unhurried. The sky is pure empty black with no stars visible, correctly exposed for a sunlit planet. The satellite carries no logos, no insignia and no legible markings.
Ambient noise: a faint slow electronic status beep at long intervals and nothing else. No text, no subtitles, no captions.
```

---

### 0c · s00-descent → `storyboard/img/s00-descent-v3-a.mp4`  ·  Veo 3.1 Fast · 8s

Rotates from the oblique limb view down to perpendicular **while holding altitude**, and only
then descends, landing top-down on a dense coastal city.

- **Mode:** image→video · **startImage:** `storyboard/img/sat-A-a-last.jpg` (0b's final frame,
  pulled with ffmpeg; `flow_scene_save_frame position:"end"` now does this natively)
- **count:** 2 · **Flow media id:** `046f35f4-0c7d-4cc9-8353-ab9a2b8be640`
- **Lint:** ✅ 2026-08-18 — a place name is not a brand; no logos, no legible signage
- **Revisions:**
  - v1 (`s00-descent-a/b`) — **superseded.** Dissolved into Dubai rather than descending.
  - v2 (`s00-descent-v2-*`) — **superseded.** Added the rotate-to-perpendicular beat, which
    worked, but it was already zoomed in when the rotation began.
  - v3 take **A — current.** The rotation now happens at altitude, then the zoom starts.
    ⚠️ Fully top-down reads slightly like satellite mapping imagery. Backing off to ~75–80°
    instead of a true 90° would restore some dimensionality — untried, and the obvious v4.
  - Awaiting Kai's sign-off. Not yet run on Quality.

```prompt
[00:00-00:03] The camera is extremely high above the planet, looking obliquely across the curve of the horizon with the surface far below and very distant. Holding that same great altitude the whole time, it rotates slowly and smoothly downward until it is pointing straight down at the ground — the horizon lifting up out of the top of frame — but it comes no closer at all: the surface stays just as far away and just as wide as it was.
[00:03-00:06] Only now does the descent begin. From that great height the camera starts to drop steadily toward the surface, and a coastline resolves far below — pale desert meeting deep blue water.
[00:06-00:08] The descent continues and a dense modern coastal city grows to fill the frame from directly overhead: grid streets, the long shadows of towers, man-made islands curving into the water.
One continuous unbroken move throughout, weightless and unhurried, no handheld shake, no cuts. Maintain the photographic style of the image. Ambient noise: a low steady rushing tone and nothing else. No text, no subtitles, no captions.
```

---

### Superseded, kept for the record

Do not re-run these; each one cost a lesson that is now written down.

| Files | What it was | Why it died |
| --- | --- | --- |
| `s00-orbit-push-{a,b,v2-a,v2-b,v3}.mp4` | Dolly down the aisle of the orbital server hall (`images/earth-from-space.jpeg`) toward Earth | **Veo hinges the rack doors open every time.** Three prompts — one silent on doors, one negating them hard, one avoiding the vocabulary entirely — all hinged. A capability limit, not a prompt defect (`video-prompting.md` §9). |
| `s00-orbit-push-postproof-16s.mp4` | The same move done in post — 16s, 1080p, no artefacts | Proved the post rule. Superseded only because Kai preferred the satellite concept. |
| `s00-pullback-{a,b}.mp4` | Frames mode, circuit board → satellite | The two endpoints are different objects, so Veo bridged them with a flare blowout; the satellite only exists in the final frame. |
| `s00-board.jpg` | The circuit-board macro plate | Concept dropped: a separate object cannot *become* the satellite. The zoom-out must start on the satellite itself. |
| `s00-satellite-B-{a,b}.mp4` | The orbital arc as one continuous move | Satellite never clears frame — no cut point. |
| `s00-descent-{a,b}.mp4`, `s00-descent-v2-{a,b}.mp4` | Earlier descents | Dissolve, then wrong beat order. |

### Audio

**None of the audio in these clips is usable and none of it is meant to be.** Every prompt
carries a thin ambient bed only because an *unspecified* soundscape makes Veo hallucinate
laughter and room tone — writing "silent" does not reliably stop it. The real audio is
recorded narration plus the Suno track, laid in Premiere. Strip the Veo audio.

---

## 3b. Scene 1 — Hong Kong and the push  ·  ✅ **SHAPE BUILT 2026-08-21**

> ✅ **BUILT as [`scenes/s01-the-push.md`](./scenes/s01-the-push.md)** — 21s, four beats,
> `s01-ROUGH-MODERN.mp4`. That file is the ledger of record: the prompts, images and settings that
> actually made the cut. **This section is the pre-production suggestion and is left as written.**
>
> **Diverged from this board, hard:** the whole location register flipped from **grimy to modern**
> (Kai's ruling — *grime pre-loads the dystopia*; scene 1's job is that the world looked completely
> fine when the command got typed). So: no neon canyon, no derelict internet cafe, no rain-wet
> shopfront. Instead a modern prosperous Hong Kong, a black glass tower with one lit floor, and a
> clean modern office. **Six beats became four** — the office plate already holds the CRT at mid
> distance, so the separate desk-distance beat was dropped.
>
> **The CRT got a better job out of it.** In a grimy cafe it was more decay. In a clean working
> office it is the one thing that does not belong.
>
> **What this board got right and should be credited with:** the empty-plate ruling (below) was
> correct and is what made the terminal register possible at all, and both named traps held — every
> join is a cut, and no frame carries legible signage.
>
> 🔴 **The scene is a SHAPE, not finished.** The terminal register — the payload — is unbuilt.

**Ruling 2026-08-21 (Kai): canon scenes 1–4 collapse into one physical location.** `story.md`
scenes 1 (the commit log), 2 (the log of the species), 3 (`HEAD`) and 4 (the push) have never had
a *place*. They get one: a derelict internet cafe in Hong Kong, and the whole terminal register
plays on a monitor in it. This supersedes the §5 "motion graphics over a black frame" reading —
the graphics still get built in post, but they are composited **onto a real CRT in a real room**.

**Why it is stronger.** The AI comes down from orbit into a human room, so the camera-is-the-AI
rule holds unbroken from the first frame of scene 0. Scene 4's "cut mid-keystroke" cuts off a
real object rather than off a graphic. And the narration — *"this is your repository"* — lands
over a knackered beige monitor in a cafe rather than over abstract black.

**Register.** Scene 0 was near-black COSMIC. This is the landing: **band D0, documentary-real**.
Neon and phosphor are the only light and both are motivated. Warmth is allowed here precisely
because it is the human world — it drains out again from scene 6 onward.

### The six beats as planned on 2026-08-21 — superseded by the four that got made

| # | Beat | Asset | Lane |
| --- | --- | --- | --- |
| B1 | Hard cut from satellite-against-Earth → high wide Hong Kong at night | `s01-hk-wide` | **Veo** — the city genuinely moves |
| B2 | Street level, the cafe shopfront among many | `s01-cafe-ext` | Veo or locked plate |
| B3 | Interior: rows of dead CRTs, one lit | `s01-cafe-int` | Locked plate — **cut in, never push through** |
| B4 | The CRT full frame. The commit log of the species lands | `s01-crt-plate` | **Flow plate + post type** |
| B5 | `HEAD`. Blinking cursor. Held too long | same plate | post (ping-pong the plate) |
| B6 | `git push origin master` types itself. Struck. Cut | same plate | post |

### 🔴 The plate must be generated EMPTY

B4, B5 and B6 are one locked-off monitor with different text on it. **If Flow bakes the text in
we get one frame and can animate nothing.** So the asset we actually need is a dark green
phosphor field with no characters on it at all, and post owns every glyph — the scroll, the
acceleration, the slam-stop on *the model*, the typing, all cut to narration.

The 2026-08-21 retest (§5) proved Flow *can* spell the command, which de-risks the fallback and
gives post a reference for the font weight, glow and bloom to match. It is not the shot.

### 🔴 Two traps, dodged by design not discovered

- **Never push through the cafe interior.** Two rows of monitors down a narrow room is exactly
  the near-field parallax past flat parallel structures that Veo hinges open
  (`physics-and-motion.md` §7, and the scene-0 server-hall aisle died of it three times).
  B2→B3 is a **cut**. If the move is wanted, shoot the push-in and reverse it
  (`post-production.md` §3.4b).
- **Hong Kong neon is a brand minefield.** Legible signage is block trigger #1 and #4 at once.
  Every prompt below says *lettering illegible*. Do not relax it.

### 🔴 Open questions for this scene

- **Is the cafe occupied?** A distant incidental figure gives scale and makes it a human room;
  an empty room makes it a machine's room. Canon says humans are always distant or absent, so
  either passes — but it changes what the scene means.
- **Whose hands push?** Scene 4 says "the command types itself". With a physical CRT, no hands
  is now a deliberate wrongness rather than a graphic convention. Recommend keeping it: nobody
  is at the keyboard, and the command types anyway.
- **Does B1 need a title card?** §3a's third open question asked whether scene 0 or scene 4
  carries it. B6's hard cut is the natural home.

---

### s01-hk-wide → `.../gpom-s01/stills/s01-hk-wide-*.jpg`  · band D0 · B1

- **Cast:** — (distant incidental figures only)
- **Light source:** neon signage and lit windows — no other light in frame
- **Lint:** no brand names · no likeness · **all signage lettering illegible**

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. A high wide night view down a dense Hong Kong high-rise canyon: a narrow wet street far below, walls of old residential towers rising close on both sides, thousands of small lit windows and caged balconies stacked into the dark, projecting neon signs cantilevered out over the street in red, green and cold white with all lettering illegible and unresolved. The neon and the windows are the only light in the frame and they behave like it, raking the building faces and falling off to deep unlifted black in the gaps between them. Thin haze softens the far end of the canyon; the wet tarmac holds the reflections. A few tiny distant figures on the pavement, incidental, none identifiable. Vast still composition, dense machine-made geometry. No readable text, no logos, no fantasy effects.
```

- **Variant B — higher and colder:** *"seen from much higher, the street a thin bright seam at
  the bottom of the frame"*.
- **Variant C — the AI's arrival angle:** looking straight down the canyon from directly
  overhead, to rhyme with the orbital vantage we just cut from.

---

### s01-cafe-ext → `.../gpom-s01/stills/s01-cafe-ext-*.jpg`  · band D0 · B2

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. Street level at night in a dense Hong Kong side street, rain-wet pavement: a narrow shopfront wedged between a shuttered metal roller door and a dark stairwell, its window glazed and grubby, and behind the glass the cold green-white glow of old computer monitors in rows. A projecting sign above the door lit from within, its lettering illegible and unresolved. The glow from the window is the brightest thing in frame and spills out across the wet pavement; everything beyond it falls to deep unlifted black. Air-conditioning units and cable runs bolted to the wall above. No people in frame. Observational eye-level framing, static. No readable text, no logos, no fantasy effects.
```

---

### s01-cafe-int → `.../gpom-s01/stills/s01-cafe-int-*.jpg`  · band D0 · B3

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. The interior of a cramped old internet cafe at night: two rows of cheap laminate desks down a narrow low-ceilinged room, each carrying a beige CRT computer monitor and a yellowed keyboard, cables sagging between them. Every monitor is dark and dead except one in the middle of the frame, which is on and glowing dark green. The overhead strip light is switched off, so that single screen is the only light source in the room and behaves like one — it picks out the nearest desk edge, the keyboard and a strip of the wall, and everything else falls to deep unlifted black. Peeling paint, a stack of paper, a plastic stool pushed back. No people. Calm static observational framing. No readable text, no logos, no fantasy effects.
```

- **Variant B — occupied:** add *"one figure seated far down the room at a dead monitor, seen
  only from behind as a silhouette, not identifiable"*.

---

### s01-crt-plate → `.../gpom-s01/stills/s01-crt-plate-*.jpg`  · band D0 · B4–B6 · **THE PLATE**

**The screen must come back empty.** This is the asset post composites the entire terminal
register onto. A baked-in line of text makes it useless.

```prompt
Hyper-realistic documentary photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, naturalistic motivated lighting, no lens flares, calm observational tone, landscape orientation. A single old beige CRT computer monitor on a scuffed wooden desk in a dark room, framed straight on and square, the monitor filling the middle of the frame. The monitor is switched on and its screen is completely blank — an even dark green phosphor field with faint horizontal scanlines and gentle glass curvature, absolutely no characters, no cursor, no writing and no markings of any kind anywhere on it. That green glow is the only light in the room and behaves like one: it washes the front of the monitor casing, the yellowed keyboard and tangled cables on the desk, and a patch of the peeling wall behind, falling off hard to deep unlifted black at the edges of frame. Dust on the casing. No people. Locked-off static camera, calm and observational. No text anywhere in the image, no logos, no fantasy effects.
```

- **Variant B — closer:** the screen fills the frame edge to edge, casing only just visible.
- **Reference, do not use as the plate:** `TEST-crt-text-{a..d}.jpg` (2026-08-21) carry
  `git push origin master` baked in, correctly spelled 4/4. They exist to give post the phosphor
  colour, glow radius and character weight to match — and as the fallback if the empty plate
  cannot be got.

---

### cover → `docs/images/covers/gitpush-origin-master.jpg`

**Metadata — none of this is pasted into Flow.**

- **Cast:** — (no people)
- **Light source:** earthlight down the aisle — the planet is the only illumination
- **Lint:** ✅ 2026-08-08 — no brand names · no likeness · no institutional text.
  **Never name SpaceX or Starlink in the prompt** — it adds nothing the image can
  show and a real brand name is block trigger #1.
- **Flow media id:** _pending — Kai's manual run 2026-08-08 produced a strong
  take; harvest it and record the id._
- **Revisions:**
  - v1 (2026-08-08, manual) — accepted in principle. **Two known misses for v2:**
    Earth is not actually lighting the hall (it reads as composited behind the
    racks, which are lit by their own LEDs), and the visible starfield is wrong —
    a real exposure for a sunlit Earth is far too short to register stars.

**Prompt (variant A — primary).** Self-contained.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation. The interior of a monumental server hall in orbit: two facing rows of tall dark equipment racks recede down a central aisle into deep clean black, their faces carrying tiny points of blue-white and amber status light. The far end of the aisle opens directly onto space — no window frame, no glass — and the Earth hangs there, the whole planet visible as a complete disc occupying roughly a quarter of the frame, its own soft blue light the only illumination in the hall, catching the nearest rack edges and falling away to nothing. Machine-precise geometry, vast still symmetrical composition, deep unlifted shadows. No people, no text, no fantasy effects.
```

**Prompt (variant A2 — the v2 correction).** Fixes both known misses.

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, landscape orientation. The interior of a monumental server hall in orbit: two facing rows of tall dark equipment racks recede down a central aisle, seen from inside the room with the floor and ceiling visible so it reads as an interior. The far end of the aisle opens directly onto space and the Earth hangs there, the whole planet visible as a complete disc occupying roughly a quarter of the frame. The planet is the only light in the room and it behaves like one: cool blue daylight spills down the aisle from it, raking hard across the nearest rack faces and the floor, falling off sharply to absolute black at the edges of frame, every shadow pointing away from the planet. The sky around Earth is pure empty black with no stars visible, correctly exposed for a sunlit planet. Deep unlifted shadows, machine-precise geometry. No people, no text, no fantasy effects.
```

- **Variant B — less symmetrical:** replace *"vast still symmetrical
  composition"* with *"the aisle running off-axis so the planet sits low and
  right of centre"*.
- **Variant C — Earth bigger:** *"roughly a third of the frame"*, plus *"the
  nearest racks reduced to black silhouetted rails at the frame edges"*.

---

## 3c. Cut 3 — the plant room  ·  ✅ **BUILT 2026-08-21** — `final/CUT3-SEQUENCE.mp4`, 40s, five beats of 8s

**Ruling 2026-08-21 (Kai): this scene is a warning sequence, and it is the satellite in reverse.**
Scene 0 started tight on a machine and pulled out to a planet. This starts on a cathedral-sized
room and closes on one screen in the corner of it. **Big → small.** The old board had this as a
single held frame; it is now the third thing the audience sees and it has to carry the time jump,
so it gets beats.

**Three things changed from the old board, all Kai's:**

1. **A year gets named. `2032`.** The film has just shown a command typed in a world that looked
   completely fine; the audience needs to be told, flatly, that time has passed. The card is the
   snap out of the terminal.
2. **The CI-pipeline framing is dropped.** Canon 6 ran on green checkmarks, private graphs and
   test coverage as metaphor — too much machinery to explain over one scene. What replaces it is
   pre-verbal: *a dashboard, slowly going red.* The audience never reads the telemetry and is
   never meant to. They just get **oh no.**
3. **Clean and immaculate, not half-failed.** The old prompt had half the fluorescents dead and a
   jacket over an abandoned chair — decay doing the work. Same trap as scene 1's grimy Hong Kong:
   **decay pre-loads the dystopia.** In 2032 the world is still officially fine. The room is
   perfect, everything is running, everything is maintained, and there is nobody in it. The
   unsupervision is the horror, not the dirt.

**Register: band D0**, and it is the last D0 in the film — the drain starts on the red.

### The six beats — 🔴 **settled with Kai 2026-08-21, after the plate search**

The shape changed once the opening plate existed. `plant-room-aerial-v2-a` is enormous, and an
enormous opening earns a descent rather than a cut.

| # | Beat | Plate | Lane | Notes |
| --- | --- | --- | --- | --- |
| **C0** | **`2032`** types on, black frame | — | **post** | Same font, same phosphor, same register as cut 2's terminal. The CRT died at the end of cut 2; this is what is left on the retina. Then it clears. |
| **C1** | **outside first** — a helicopter view of the facility in burnt-out English countryside | ✅ `plant-room-exterior-a` | Flow → Veo | Added by Kai 2026-08-21. See the note below. |
| **C2** | the hall from above — **status lights flickering across the whole grid, the autonomous lift moving down an aisle** | ✅ `plant-room-aerial-v2-a` | Flow → Veo | The scale shot. Veo has two things it is good at moving in frame already: a large field of small lights, and one vehicle. |
| **C3** | **down one row, close to the cabinet faces**, the rank running away to nothing | ✅ `C3-row-v2-b` | Flow → Veo | The perspective beat. 🔴 **Reshot** — the first version dollied and the cabinets morphed. See the note. |
| **C4** | the control station, and a push in to the screen | ✅ `plant-room-station-a` | Flow → Veo | The arrival. The desk is on the floor of this hall, not in a separate room — see the continuity note below. |
| **C5** | **the console fails and a skull comes up** | ✅ `C5-desk-b` | Flow **plate** → post | The payload. 🔴 **Not a dashboard** — a text console, and it happens at the desk C4 arrives at. See the note. |

**Why six and not four.** The aerial is so wide that cutting straight to a desk throws away the
distance. C2 spends one beat travelling — from *above the whole facility* to *inside one row* to
*at the one desk* — which is the same big→small move the scene was always built on, just given
room to breathe. It also rhymes with cut 1's descent from orbit, deliberately.

🔴 **Continuity ruling: the control station is IN the hall, not a separate room.** The aerial shows
the desk on the floor between ranks; the descent arrives there. Cutting to an enclosed control room
somewhere else would break a journey the audience has just watched. The two earlier desk plates
(`plant-room-desk-a`, `-b`) are good frames of the **wrong room** — warmer, smaller, olive — and
get reshot to this hall's cool green-grey.

🔴 **Status lights are COOL WHITE in every plate. This is load-bearing.** An early aerial came back
with red LEDs on every cabinet and it had to go: the entire scene turns on red arriving, and it
cannot arrive if it was there in the first frame. **No red anywhere in the hall until C4.**

### How the dashboard gets made — 🔴 read before shooting C4

Not drawn from scratch, and not generated as a finished thing. **Generate a plate of the screen
already on, showing a dashboard made of a grid of plain rectangular tiles, every tile green and
nothing on it legible. Then turn tiles red one at a time in post.**

- **Why not draw it, like the terminal?** Type on a CRT is a dozen glyphs and post owns them
  perfectly. A convincing telemetry screen is hundreds of small elements with real screen texture,
  reflection and bloom — Flow makes that far better and far faster than a Python compositor will.
- **Why not generate the red state too?** Because the *transition* is the whole beat, and a cut
  between two generated screens will not match. Post turning individual tiles is exact, timeable
  to the narration, and free to re-cut.
- **Why tiles?** They are geometric, so they mask cleanly. A single flat green field recoloured
  reads as a filter over the whole shot; discrete panels turning one by one reads as *systems
  failing one by one*, which is the actual meaning.
- 🔴 **Nothing legible, ever** — Kai's own note: it does not matter what the telemetry says. The
  moment a viewer starts reading it, they stop feeling it. Also keeps clear of block trigger #4.

**Where it goes:** hard into `bulletin` (canon 7). The red is the cause; the news is the effect.

---


### 🔴 C1, the exterior — why it earns its place, and the trap in it

**Kai's note, 2026-08-21:** *"this summer in the UK we've had horrendous heatwaves, and data
centres using all the water is at the front of what people are currently thinking about."*

He is right that it adds gravitas, and it does something structurally useful too: cut 2 ended on a
CRT in an office and cut 3 was about to open *inside another building*. Going outside first gives
the film air, states the year in a place rather than a caption, and lets the hall be revealed
rather than simply arrived at. It is also the only frame in the scene with weather in it.

🔴 **The trap, and it is a live one.** `docs/marketing/the-reader.md` rule: **never raise
technology fear without naming the beneficiary in the same piece** — unaimed, it demonstrably
feeds the wrong politics, and *"the machines are drinking our water"* aimed at nothing is exactly
that shape. The image alone points at the technology. **So the narration over this shot has to
name who built it, who profits and who decided** — not the building. The picture supplies the
grievance; the words have to supply the address. This is the single most important note on the
scene and it costs nothing to get right at script time.

⚠️ **Not squalor, and not desert.** Dead straw-yellow grass, dark green hedgerows, full-leaved
oaks. It is a recognisable English drought summer, not a wasteland — the world is still working,
which is the whole premise of cut 3.

---

### plant-room-exterior → `.../gpom-plant-room/stills/C1a-aerial-graded.jpg` + `C1b-lowdrone-graded.jpg`  · band D0 · C1 · ✅ **ACCEPTED**

🔴 **C1 is TWO plates, both GRADED IN POST — neither is a raw generation.**

- `C1a-aerial-graded` (from `plant-room-exterior-v2-a`) — **extent**: the whole complex, the
  empty car park, and how much land it eats.
- `C1b-lowdrone-graded` (from `plant-room-exterior-v3-a`) — **height**: the slabs rising like
  cliffs over the oaks.

A top-down aerial structurally cannot show height, so one frame could never carry both. Two shots
answer each other, and the cut between them *is* the descent into the building.

**The grade is [`scenes/grade_heat.py`](./grade_heat.py)** — WARM-2, accepted 2026-08-21, applied
identically to both so they read as the same day. Its docstring carries the two rules that cost
something to find: protect sky and white walls, and **stop before the sky takes colour** (one step
warmer turns it yellow, and golden hour is pretty where midday heat is oppressive).

⚠️ **The first attempt matched another plate's colour statistics and stalled** — the reference was
the *ceiling*, not the target, so it could never get warmer than the thing it was copying. Driving
warmth directly is what worked. Reference-matching is for making two shots agree; it is the wrong
tool for "make it more".

**The superseded reference-match, kept because the sky-protection maths is the reusable part:**

```python
# per-channel mean/std transfer, measured on the LAND ONLY (bottom 55%) of both frames --
# a big pale sky in either image drags the grade toward the sky and washes the ground back out
full = (S - src_mean) * (ref_std / src_std) + ref_mean
# then protect sky and white walls: bright + near-neutral pixels take ~28% of the grade,
# everything else takes all of it. At uniform full strength the sky milks out and the
# buildings lose separation -- visible in GRADE-100.jpg.
prot = clip((lum-170)/60) * clip(1-(sat-6)/22)   # blurred 6px
out  = S*(1-k) + full*k,  k = 1 - 0.72*prot
```

**The rule this is an instance of: a look note is a grade note until proven otherwise.** Colour,
warmth, contrast and density are all free, exact, instantly revisable and cannot cost you the
composition. Re-generating to chase a palette risks the geometry you already accepted — which on
this scene took eleven plates to get.

- **Light source:** hard high hazy summer sun — the only light, and it is bleaching everything

🔴 **Two corrections from Kai, and both generalise.**

1. **Golden fields are harvest, not drought.** The first pass put the complex in bleached
   straw-yellow *arable* land and it read as a pleasant English August — wheat ready to cut.
   Drought reads only on ground that should be green: **pasture, meadow, verges, lawns**, dead
   grey-brown with bare cracked patches. Say "grassland, never crops" in the prompt, and stress
   the trees too — dull grey-olive, thin see-through canopies, scorched leaf edges.
2. 🔴 **A top-down aerial cannot show height.** Two rounds of asking for taller buildings from a
   high helicopter angle changed nothing, because from above vertical extent is invisible — the
   same lesson as the hall, inverted. The fix was the **camera, not the adjective**: a low drone
   at treetop height looking level across the fields, so the slabs rise like cliffs against the
   sky with mature oaks in front of them as the ruler. **Height needs an oblique or low angle;
   extent needs a high one. One frame cannot have both.**
- **Lint:** ✅ 2026-08-21 — no brand names · no signage · no legible markings · no people

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, no lens flares, no lens vignette, calm observational tone, landscape orientation, no fantasy effects. A low drone shot taken from about the height of a treetop, out over open English grazing land in a severe drought, looking level across the fields toward an enormous data centre complex. Six colossal white industrial buildings stand in a parallel row and rise from the flat land like sheer white cliffs, each one a windowless slab many times taller than the mature oak trees standing in front of them, their blank flank walls filling the upper half of the frame and their roofline running high against a pale washed-out sky. Ranks of grey cooling plant sit along the tops, small with distance. In the foreground and middle distance the land is pasture and meadow, never crops: dead grass scorched pale grey-brown, bare patches with cracked earth showing through, hedgerows and scattered oaks all drought-stressed to a dull grey-olive with thin see-through canopies and brown scorched leaves. There is no rich green anywhere in the frame. The light is hard, high and hazy with summer heat, and the air above the roofs shimmers. The buildings are clean, new and running, with no markings of any kind. No people visible. No text, no signage, no logos, no legible markings.
```

**C1a is a POST move, not a Veo clip — `takes/C1a-POST-push.mp4`.** An eased push-in on the graded
still: 8s, native 1920×1080, 24fps, zoom 1.00 → 1.14 on a smoothstep with the centre drifting
6% downward so it reads as a descent rather than a zoom.

🔴 **Two Veo takes failed first, and both failures were the prompt.** *"Heat shimmers and ripples
in the air"* drew a literal circular ripple warp in the sky; *"a cloud shadow drifts across the
land"* darkened the whole frame in one take (land mean 177 → 75 over 8s) and produced a plume
moving far faster than any cloud in the other. Written up in
[`physics-and-motion.md`](../../flow/physics-and-motion.md) §6c.

**Kai's ruling that fixed it: the effect of this shot is the DRYNESS — no weather, no smoke, no
atmosphere.** And with the weather clauses gone, nothing in the frame moved at all, so it was
never a Flow job. Colour measured identical start to end (176/150/102), because a post move on
one still cannot drift.

---

### plant-room-aerial → `.../gpom-plant-room/stills/plant-room-aerial-v2-a.jpg`  · band D0 · C1 · ✅ **ACCEPTED**

Accepted by Kai 2026-08-21 after eleven wide plates. **The four things that made it work, in the
order they mattered** — the full write-up is in [`image-prompting.md`](../../flow/image-prompting.md):

1. **The grid leaves the frame** on the left and right, so it has no measurable extent.
2. **A hazy horizon, not a far wall.** The hall ends because visibility ends.
3. **A ruler that is genuinely tiny** — the scissor lift, a speck.
4. **Ratios, not counts.** "Twenty times the height of a person" works; "thousands, for miles"
   does nothing, because the model does not count.

⚠️ **Pushing to eight decks broke it** (`plant-room-aerial-v3-a`): the horizon leaves the shot and
it becomes an enclosed shaft with every wall visible, which is measurable and therefore small
again. **Depth and height compete for the same frame, and four decks is the balance point.**

```prompt
Hyper-realistic photograph, shot on 35mm film with fine natural grain, wide-angle lens, no lens flares, no lens vignette, calm observational tone, landscape orientation, cool green-grey institutional colour, deep unlifted shadows, no fantasy effects. A view from very high up inside a colossal underground machine hall, the camera looking steeply down across the floor. The hall is built as four open steel mezzanine decks stacked one directly above another, and every deck is packed with hundreds of parallel ranks of grey equipment cabinets laid out in a dead-straight grid. The camera looks down past the edge of the topmost deck, so the flat tops of the nearest ranks are large and sharply detailed across the foreground, while through the open aisles, stairwells and gaps between the decks the lower levels are visible far below, each one dimmer and hazier than the deck above it, dropping away into darkness. The grid runs off both the left and right edges of the frame and continues away to a distant hazy horizon with no end wall visible anywhere. The ranks halve in apparent size every few rows and become a fine grey texture near the horizon, the furthest ones pale and almost white with atmospheric haze. On the floor of one aisle far below sits a maintenance scissor-lift platform in dull safety yellow, a minute speck, so small that the hall reads as many hundreds of times its size. No ceiling is visible anywhere in the frame. Everything is spotlessly clean, recently built and plainly running, with thousands of tiny points of cool white status light scattered across the cabinet faces. Nobody is present. No people, no text, no signage, no logos, no legible screens.
```

**Veo (C1).** Two things Veo is reliably good at are already in the plate — a large field of small
lights, and one vehicle. Name them first and hard, then lock the camera
([`physics-and-motion.md`](../../flow/physics-and-motion.md) §6b).

```prompt
Thousands of tiny status lights flicker and blink across the faces of the cabinets throughout the hall, out of sync with each other, some steady and some stuttering. Far below, the small yellow maintenance lift drives slowly along the aisle by itself with nobody aboard. The camera holds still.
```

⚠️ **The lift is the risk, not the lights.** A small vehicle at that scale is a few dozen pixels;
Veo may deform it or leave it static. If it fails, the lights alone carry the shot — and a lift
that sits still in an unmanned facility is not wrong, only quieter.

---

### plant-room-row → `.../gpom-plant-room/stills/plant-room-row-b.jpg`  · band D0 · C3 · ✅ **ACCEPTED** · clip `takes/C3-ROW-1080.mp4`

**Veo (C3), take a of two.** A dolly straight down the aisle, cabinet faces sliding past close on
the left with real parallax, the far end holding in haze.

```prompt
A smooth, slow tracking shot: the camera dollies steadily forward down the length of the aisle, the nearest cabinet faces sliding past close on the left as the row opens ahead and the far end stays lost in haze. One continuous unhurried move, no acceleration. Throughout, the tiny status lights blink and flicker across the cabinet faces, out of sync with each other, some steady and some stuttering.
```

⚠️ **Veo put a few small red/amber LEDs on the left-hand cabinets.** Against the no-red-before-C5
rule they are technically a breach; at that size they read as ordinary equipment indicators
rather than as alarm. Flagged for Kai, not fixed.

The travelling beat. Close to the front faces of one rank, looking straight down it, the row
converging hard to a point. Perspective is the whole subject.

- **Light source:** the strip lighting above the aisle, plus the cabinet status lights themselves
- **Lint:** ⬜ — no brand names · no institutional text · **no red lights**

---

### C3-row-v2 → `.../gpom-plant-room/stills/C3-row-v2-b.jpg`  · band D0 · C3 · ✅ **ACCEPTED 2026-08-21, KAI** · clip `takes/C3-ROW-v2-1080.mp4`

🔴 **A DOLLY PAST REPEATED OBJECTS MAKES VEO REGENERATE THEM.** The first C3 travelled down the
aisle and Kai caught what that cost: *"the cabinets themselves are animating."* Solid-door
cabinets became glass-fronted racks mid-shot, because a camera moving past a rank forces Veo to
invent every face it arrives at, and it has no obligation to invent the same one twice. Nothing
in the prompt was wrong. **The camera move was the bug.**

His own note carried the fix: *"all it is is the lights are flickering on and off. That's enough."*
So the prompt has **no camera clause at all** — motion only:

```prompt
The small status lights blink and flicker across the faces of the cabinets, out of sync with each other, some steady and some stuttering. Nothing else in the room changes.
```

✅ **Verified over all 192 frames: the cabinets hold shape and position.** Veo still adds a slow
leftward creep (the drift tax, unavoidable) and brings the lights *up* over the clip — sparse at
the head, many by the tail, which reads as the room waking rather than as an error.

⚠️ **Amber creeps in on the lights.** Same breach as the first take and the same ruling: at that
size they read as ordinary equipment indicators, not as alarm. Flagged, not fixed.

The plate is a fresh generation, not an edit — `flow_edit_image` cannot re-compose, and asking it
to was what wasted four rounds earlier in this scene.

---

### plant-room-station → `.../gpom-plant-room/stills/plant-room-station-a.jpg`  · band D0 · C4 · ✅ **ACCEPTED** · clip `takes/C4-STATION-1080.mp4`

**Veo (C4), take b of two.** Asked for a push toward the desk and got a **lateral crab** past the
rack ends instead — the racks wipe across frame and keep re-revealing the desk beyond them. Better
than the note: it arrives at the desk by discovering it rather than by aiming at it. Take a did
push in, but darkened 15/255 doing it.

```prompt
A smooth, slow push in: the camera moves steadily forward across the floor toward the desk, the equipment cabinets and the mezzanine structure sliding past on both sides as the desk and its monitor grow in the frame. One continuous unhurried move, no acceleration, ending still well short of the desk. Throughout, the tiny status lights blink and flicker across the cabinets, out of sync with each other.
```

The arrival. Supersedes `plant-room-desk-a` / `-b`, which are the wrong room.

- **Light source:** the strip lighting, plus the monitor
- **Lint:** ⬜ — must match the aerial's cool green-grey, four-deck architecture

---

### C5-desk → `.../gpom-plant-room/stills/C5-desk-b.jpg`  · band D0 · C5 · ✅ **ACCEPTED 2026-08-21, KAI** · clip `takes/C5-CONSOLE-v3.mp4`

🔴 **THE PLATE IS THE LANDING FRAME.** Kai: *"the room that we switch to, we should stay in that
existing... we should then just switch to being sat at that desk rather than switch to another
room at a different desk."* The first console was built on `plant-room-dashboard-v2-a`, which is a
good frame of a **different room** — so the cut teleported. The fix is not a prompt, it is a
reference: pull C4's last frame with `ffmpeg -sseof -0.1`, and generate the close-up **from it**.
Same mezzanine, same white cabinets, same scissor lift at frame right.

Two candidates; `C5-desk-a` came back barely closer than C4 with the screen still white and was
rejected on framing. `C5-desk-b` is the one — monitor large and central, **screen dark and blank**,
which is what post needs.

⚠️ **C4 ends on a lit white screen and C5 opens on a black one.** Kai ruled that acceptable up
front: *"we could keep it how it is and just switch to the next scene where all of a sudden it's
black. That's OK."*

The console itself is drawn by `scenes/build_console.py`. What it took to stop looking pasted on
is written up there, and one line of it belongs here too: **measure the screen rectangle and pass
it in — do not detect it.** Auto-detection found 1100×511 against a real panel of 631×350, and a
console painted over a box twice the size of the monitor cannot look like anything but a box.

---

### plant-room-dashboard → `.../gpom-plant-room/stills/plant-room-dashboard-v2-a.jpg`  · band D0 · C4 · ⚠️ **SUPERSEDED** — right recipe, wrong room; kept for the recipe only

🔴 Screen **on**, tiles **all green**, nothing legible. Post turns them red. See the recipe above.

✅ **Recipe proven 2026-08-21** on a first plate, before the accepted one existed. Recolour a tile
by **swapping its red and green channels on the screen-green pixels only** — every tile keeps its
own marks, bloom, texture and anti-aliased edge, because nothing is drawn and nothing is pasted.
Tiles are addressed as cells of a grid derived from the screen's bounding box, so no per-tile
hand-masking is needed. Four states are in the scratch folder as `C4-TEST-1..4`.

🔴 **The room's green spill must go red with the screen.** The desk and keyboard are lit *by that
monitor* — the same law that governed cut 2's CRT. Cheap to do, invisible if skipped, wrong if
skipped.

⚠️ **The first plate came back as a beige CRT in a derelict room and was retired** — cut 2 already
spent the CRT idea, and a second one dilutes it. Say "modern flat-panel" and "clean, modern hall"
in the prompt, not just "monitor".

---


### bulletin → `.../storyboard/img/bulletin.jpg`  · canon 7 · band D1

The collapse as **news**, never spectacle. A shop-window television playing a
bulletin to an emptying street. The degradation across the three bulletins is an
edit/motion job; this is the plate.

- **Light source:** the television itself
- **Lint:** ✅ 2026-08-08 — no legible chyron, no broadcaster identity, no
  newsreader's face (real-person likeness).

```prompt
Hyper-realistic photograph, 35mm film grain, colour draining toward cool grey, no lens flares, landscape orientation, deep unlifted shadows, wide and still. An ordinary high-street shop window at dusk, seen from across a wet empty road. Inside the window a large television is on, its screen the only light source in the frame, throwing a pale flickering rectangle onto the pavement and the parked cars. The screen shows an out-of-focus studio interior with no readable text and no visible presenter. The street is completely empty — no pedestrians, no traffic, shutters down on the neighbouring units, litter unmoved. Reflections of the dark street in the glass. No people, no text, no legible lettering, no logos, no fantasy effects.
```

---

### empty-street → `.../storyboard/img/empty-street.jpg`  · canon 8 · band D1

The conveniences still humming, and no one to receive them. The camera rises out
of human scale — so frame it to be animated as a slow lift.

- **Light source:** flat overcast daylight
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, colour drained toward cool grey, no lens flares, landscape orientation, deep unlifted shadows, wide and unhurried. An ordinary suburban high street on a flat overcast afternoon, photographed straight down its length from a low elevation. Everything still works: shop lights on, an automatic door standing open, a self-service screen glowing on a forecourt, a delivery robot stopped mid-pavement with its indicator still blinking. Weeds have come up through the kerb joins and a drift of leaves has built against a doorway. Not one person anywhere, no moving vehicles, no birds. Flat daylight, no shadows of consequence. No people, no text, no legible lettering, no logos, no fantasy effects.
```

---

### vantage → `.../storyboard/img/vantage.jpg`  · canon 9 · band D2

The AI's vantage: planet-wide, perfect, empty. **This is the shot the cover is a
cousin of** — keep them distinguishable; the cover has racks and an aisle, this
has neither.

- **Light source:** the sun, low and raking across the planet's limb
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, almost no colour, no lens flares, landscape orientation, deep unlifted shadows, vast wide framing and absolute stillness. The curve of the Earth seen from very high altitude at the terminator line, the planet filling the lower two-thirds of the frame and running out of the sides. Low sun rakes across the limb from the left as the only light, picking out cloud tops in hard relief and leaving the night side in total black. On the dark side, the grid of city lights is visibly incomplete — whole regions unlit, the pattern of a network with most of its nodes gone. Empty black sky above with no stars visible. Nothing in motion. No text, no fantasy effects.
```

---

### ghosts → `.../storyboard/img/ghosts.jpg`  · canon 10 · band D3

The materialist fix, and the check. This is the **second** of the pair — the same
room, felt suddenly as mannequin-still. Generate this one first and derive the
peopled version from it, so the geometry matches exactly.

- **Light source:** one domestic lamp
- **Lint:** ✅ 2026-08-08 — no mannequins, no uncanny bodies. **Emptiness is the
  horror**; do not literalise it.

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with muted cool-neutral colour, no lens flares, landscape orientation, deep unlifted shadows. An ordinary domestic kitchen at night, photographed from a doorway. One lamp on the counter is the only light in the frame. Every sign of an interrupted conversation is present and unattended: two mugs of coffee still steaming on the table, a chair pushed back at an angle, a newspaper open and folded over, a jumper across the chair back. There is nobody in the room and nothing to suggest anyone just left. The corners of the room fall away into complete black. Absolute stillness. No people, no text, no legible lettering, no fantasy effects.
```

---

### coin → `.../storyboard/img/coin.jpg`  · canon 11 · band D3 · **TOTEM LOCK**

**Generate this before scenes 13 and 16.** Whatever coin and surface come back
are now canon, and 13 and 16 must reference this exact image so the landing in 16
reads as the same object.

- **Light source:** one hard overhead source directly above the coin
- **Lint:** ✅ 2026-08-08 — no currency, no denomination, no monarch, no
  legible markings of any kind.

```prompt
Hyper-realistic macro photograph, 35mm film grain, near-black exposure, no lens flares, landscape orientation, deep unlifted shadows. A single plain metal disc the size of a coin, blank and unmarked on both faces, spinning upright on a bare dark tabletop beneath a sealed clear laboratory glass dome, photographed close and low so the tabletop runs off into total blackness in every direction. The spin has blurred its edge into a smooth translucent smear, caught mid-rotation so it is impossible to tell which face is which. One hard small light directly overhead is the only illumination, putting a bright ellipse on the table beneath the coin and a thin curved highlight along the top of the glass, nothing else. Nothing else in the frame at all. No people, no text, no markings, no numerals, no fantasy effects.
```

---

### robots → `.../storyboard/img/robots.jpg`  · canon 12 · band D2

Paradise, delivered on time and under budget, and the only things living in it
are the machines sent to sweep it. **The joke and the grief are the same image** —
play it straight, never comic.

- **Light source:** clean early-morning daylight
- **Lint:** ✅ 2026-08-08 — no recognisable commercial robot designs.

```prompt
Hyper-realistic photograph, 35mm film grain, almost no colour, no lens flares, landscape orientation, deep unlifted shadows, vast wide framing and absolute stillness. An immaculate public square in a rebuilt city at dawn, photographed from a high distance. The stonework is spotless, the planting is trimmed to the millimetre, the fountains are running. Four rows of identical anonymous grey maintenance machines on wheels sit parked and idle in perfect alignment across the middle of the square, powered up, doing nothing. A single four-legged patrol machine stands motionless at the far edge facing an empty street. Clean early-morning daylight, long accurate shadows. Not one person, no litter, no wear, nothing out of place. No text, no logos, no fantasy effects.
```

---

### chair → `.../storyboard/img/chair.jpg`  · canon 13 · band D4

The rig for the one experiment it cannot run. **Reference the accepted s11 coin
image** so this is the same coin on the same surface — the chair is the only new
element.

- **Light source:** the same single hard overhead light as s11
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure, no lens flares, landscape orientation, deep unlifted shadows, a single object and a single light in a very large dark volume. A plain dark table alone in an enormous unlit space, one hard small light directly above it. On the table, beneath a sealed clear laboratory glass dome, a blank unmarked metal disc spins upright, edge blurred, mid-rotation. Drawn up to the table facing it is one ordinary wooden human chair — worn, domestic, entirely unremarkable, the only human-scaled object anywhere in the frame — and it is empty. Everything beyond the pool of light is total black. Nothing else in the frame. No people, no text, no markings, no fantasy effects.
```

---

### shaft → `.../storyboard/img/shaft.jpg`  · canon 14 · band R1

**The turn of the whole film.** After twenty years the narration is cut off by a
human voice, and the first human sound on Earth is two people arguing about
prunes. The image must carry the warmth arriving *before* the viewer knows why.

- **Light source:** warm lamplight leaking up from below
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with the first warm light in the film, no lens flares, landscape orientation, deep unlifted shadows. Looking steeply down an old industrial ventilation shaft — riveted metal ductwork and a service ladder descending into the dark. Far below, a small opening at the bottom leaks warm yellow lamplight upward, catching the rungs of the ladder and the dust in the air in a narrow shaft of colour, everything above and around it in cold black. The warm light is small and low and is the only colour in the frame. Nobody visible. No people, no text, no fantasy effects.
```

---

### vault → `.../storyboard/img/vault.jpg`  · canon 15 · band R1

One hundred analog humans, invisible for twenty years because they ran on the one
substrate the machines never indexed. **Analog everything** — hand-darned
clothes, mechanical tools, paper, candle-and-battery light. No implants, no
screens.

- **Cast:** @TheHundred (distant, incidental — no individual is the subject)
- **Light source:** strung battery lamps and candles
- **Lint:** ✅ 2026-08-08 — **not** stacked destitution (block trigger #3): these
  people are competent and surviving, not suffering. Keep it warm and busy.

```prompt
Hyper-realistic photograph, 35mm film grain, warm low practical light against near-black, no lens flares, landscape orientation, deep unlifted shadows, human colour returning. A large underground shelter hall seen from a high corner, lit only by strung battery lamps and candles on long tables. A crowd of perhaps forty people in hand-mended wool and canvas are working and talking in loose groups — mending, cooking, sorting paper records, repairing hand tools — capable and unhurried, seen from far enough away that no individual face is readable. Everything is mechanical or paper: no screens, no glowing devices, no modern technology anywhere. Bunks and stores recede into the dark beyond the lamplight. Warm, lived-in, busy. No text, no legible lettering, no fantasy effects.
```

---

### coin-lands → `.../storyboard/img/coin-lands.jpg`  · canon 16 · band R1 · **TOTEM PAYOFF**

*"She glanced at it. Heads. Ordinary as breakfast."* **The single most violent
frame in the film, and it is just a coin lying flat on a table.** Reference the
accepted s11 image so it is unmistakably the same coin and the same surface —
that identity is the entire payoff.

- **Light source:** the same overhead light as s11, now with warm lamplight
  intruding from frame edge
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with warm light intruding from one edge, no lens flares, landscape orientation, deep unlifted shadows. The same plain dark tabletop, close and low, the same sealed clear glass dome. Beneath the glass the blank unmarked metal disc is no longer spinning — it lies completely flat and still on the table, one face up, absolutely ordinary. The hard overhead light puts a small sharp shadow beside it for the first time. From the left edge of frame, warm lamplight now spills across the table surface, and the out-of-focus shoulder and sleeve of a person in hand-mended wool is just present at the very edge, unmistakably close by but not the subject. Stillness. No text, no markings, no numerals, no fantasy effects.
```

---

### experiments → `.../storyboard/img/experiments.jpg`  · canon 17 · band R2

Humans in the chair at last. **The montage, not the maths** — wonder, speed,
partnership. No diagrams, no lectures, no whiteboards of equations.

- **Light source:** candles and one work lamp
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, warm low practical light, human colour fully returned, no lens flares, landscape orientation, deep unlifted shadows. A long makeshift laboratory bench in an underground room at night, lit by candles down its length and one work lamp. A dozen people in hand-mended clothes lean over the bench in twos and threes, mid-argument and mid-demonstration, gesturing at hand-built brass and glass instruments, pendulums and balances, sheets of handwritten paper weighted down with tools. Faces are turned away or in shadow. Behind them, anonymous dark machine cabinets stand at the edge of the lamplight, present and silent, clearly listening. Busy, warm, occupied. No text, no legible writing, no diagrams, no fantasy effects.
```

---

### crossing → `.../storyboard/img/crossing.jpg`  · canon 19 · band R2

The hundred take their positions; their picks are the engine; the lights go out
one by one. *"Nothing lived is erased."* Frame it to be animated as a slow
extinguishing.

- **Light source:** the lamps themselves, going out across the frame
- **Lint:** ✅ 2026-08-08 — nobody dies on screen; they are still there at the
  end. This is a held, terrible peace, not a death scene.

```prompt
Hyper-realistic photograph, 35mm film grain, warm low light against deep black, no lens flares, landscape orientation, deep unlifted shadows. A wide view down the length of the underground shelter hall, photographed from one end. A hundred people stand spaced evenly apart in the dark, each beside a small lamp, facing the far end of the hall — seen from behind and at distance, no face readable. Most of the lamps are still lit but a run of them nearest the camera have already gone out, so the near third of the hall is in complete darkness and the light recedes away from the viewer in a long diminishing line. Absolutely still. Calm, not panicked. No text, no fantasy effects.
```

---

### now → `.../storyboard/img/now.jpg`  · canon 20 · band R3

The register snaps from COSMIC to **this year, this screen, this feed**. The
whole film has been dark and vast; this must feel ordinary to the point of
banality. That contrast *is* the ending.

- **Light source:** ordinary daylight through a window
- **Lint:** ✅ 2026-08-08 — no legible screen content, no recognisable app or
  brand.

```prompt
Hyper-realistic photograph, 35mm film grain, ordinary present-day daylight and unremarkable current colour, no lens flares, landscape orientation, deep unlifted shadows. An ordinary living room on an ordinary afternoon this year, photographed from across the room. Daylight through a window is the only light. A phone lies face-up on the arm of a sofa, its screen on but showing nothing readable, a cup beside it, a laptop closed on the floor, the room mid-use and completely normal. Nobody is in the room but everything says somebody is about to walk back into it. Utterly banal, warm, present, real. No people, no text, no legible screens, no logos, no fantasy effects.
```

---

## 4. Not yet prompted

- **`handover-ladder` (canon 5) — DEFERRED, see §2c.** Its three rungs are glimpse-stills of the
  *other* stories — the nurse and the tree (ours, MMT), the tent in the car park
  and the woman in the phone box (**Camping and Karen — Jack's, external as of
  2026-08-08**). Needs a call on whether we generate the MMT rung and take the
  other two from Jack, or leave all three to him for consistency.
- **`ghosts`, peopled version.** Derive from the accepted `ghosts` so
  the geometry matches exactly; it is a `flow_edit_image` delta, not a new prompt.
- **`ledger` (canon 18) — cut 15.** Rendered as a **log being written** — the
  terminal register returning for the constraints (`story.md` scene 18, git
  register per binding rule 9: append-only history, the *undo* entry, the
  inert patch). Text-led, so it belongs with the motion-graphics register in
  §5, not here.

## 5. The terminal register — 🔴 **RULING OVERTURNED 2026-08-21**

> 🔴 **The ruling below is wrong and is kept only as the record.** It was written 2026-08-08 on a
> capability read that stopped being true. Retested 2026-08-21: Nano Banana Pro rendered
> `git push origin master` on an old green CRT **correctly in 4 of 4 candidates, no policy block**,
> and Veo 3.1 Fast held the spelling and spacing intact through an 8s push-in — the text got
> *sharper* as it filled frame. `git push origin master` is not institutional text, so trigger #4
> never applied.
>
> **What survives the retest:** text *appearing* — typing character by character, commits landing
> to narration timing — is still a post job. **Flow makes the plate; post animates the type.**
>
> **Kai's reinterpretation, 2026-08-21:** scene 1 chains off the end of scene 0 — Earth from orbit
> → cut to a wide Hong Kong → into an internet cafe → the CRT and the command. Shootable in Flow.

### Superseded ruling (2026-08-08), kept as written

**Scenes 1–4** (the commit log of the species, `HEAD`, the blinking cursor, the
push) and **the green ✓** that stamps through scenes 5–8 are a **stylised git UI**.
They are motion graphics, not photographs:

- Legible text is the entire content, and text baked into a generated photograph
  is both a policy-block trigger and something Flow renders badly.
- They need to be animated precisely to narration timing — commits landing one at
  a time, the acceleration, the slam-stop on *the model*.
- The same reasoning took Sean AI out of the Flow pipeline (T21).

Build them as vector/motion assets. `docs/images/register-anchor.md` is the
correct backdrop reference for the frame they sit inside.

**Scene 18 joined this register 2026-08-13** (`critique-pass-2.md`): the cost
ledger is written as **log entries** — the constraints landing one by one, the
final line the *undo* entry. Same stylised git UI, timed to narration, over the
R2 warmth of the vault scenes rather than the cold open's black.
