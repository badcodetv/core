---
story: gitpush-origin-master
flow_project: gpom-story
flow_project_id: 1774dff0-02b0-45a7-9d53-ecc549bc60a5
updated: 2026-08-18
---

# GitPush Origin Master — prompt ledger

Read `.claude/skills/badcode-art-direction/SKILL.md` first (Layer 0 — the global
BadCode register; never copied into this file).

> **Status.** **Scene 0 — the orbital opener — is SHOT** (2026-08-18): three clips,
> ~28 seconds, in §3a, with every prompt, the takes that lost and why. The cover was
> tested manually by Kai 2026-08-08 and works. **Everything else below is still unfired**
> (Layer 1 + totems + scene prompts drafted 2026-08-08).
> Front-runs T7/T9/T10 of
> [`design/2026-08-08-story-covers-and-prompt-ledger.md`](../../../design/2026-08-08-story-covers-and-prompt-ledger.md).
> Scene numbers map to the storyboard in
> [`story.md`](./story.md#storyboard--scene-by-scene-video-guide) and its
> `Scene → asset checklist` at `story.md:696`.

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
`s16-coin-lands` she is deliberately an out-of-focus shoulder at the frame edge,
because the coin is the subject. Cast her anyway: the moment the vault scenes get
a closer shot, she is the only face that has to hold.

---

## 2b. Totems — lock these before generating any scene

| Totem | Rule | Appears in |
| --- | --- | --- |
| **The coin** | **The most important object in the film.** One ordinary coin, no markings we can read, **under a sealed clear glass dome** on one plain surface — the rig: the one object the world is never allowed to touch (`story.md` binding rule 8, added 2026-08-13; the glass is the visual grammar of "engineered apart from the world" and is why only the coin stays undecided). It spins in 11, spins in 13, and **lands in 16** — the single most violent frame in the story, and it is just a coin on a table. Generate it once, accept it, and reference that exact image in 13 and 16 so the landing (and the dome) reads as the same rig. | 11, 13, 16 |
| **The empty chair** | One ordinary human chair, worn, entirely unremarkable, in a space with no human scale anywhere else. The whole argument in one object. | 13 |
| **The ventilation shaft** | Plain industrial ductwork, the first human sound in twenty years coming up it. Warm light from below. | 14 |
| **The green ✓** | A UI element — **motion graphics, not Flow.** See §5. | 5, 6, 7, 8 |

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

### s06-basement-optimiser → `.../storyboard/img/s06-basement.jpg`  · band D0

The one held frame in scene 6: the thing still returning green checkmarks while
nobody is left checking. **Vast, patient, unsupervised.** Never a face, never a
body — it is infrastructure.

- **Light source:** fluorescent strip lighting, half of it failed
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, ordinary overcast institutional colour, no lens flares, landscape orientation, deep unlifted shadows. A very large basement plant room beneath an office building, photographed from a doorway at the near end so the far wall is lost in distance. Rank after rank of anonymous grey computing cabinets fill the floor, humming, cables in neat bundles overhead, everything clean and recently installed. A row of fluorescent strip lights runs the ceiling and half of them have failed, so the room is lit unevenly and mostly badly. A swivel chair sits pushed away from an unmanned monitoring desk in the foreground, a jacket still over its back. Nobody is present and nothing indicates anyone has been for some time. No people, no text, no legible screens, no logos, no fantasy effects.
```

---

### s07-bulletin → `.../storyboard/img/s07-bulletin.jpg`  · band D1

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

### s08-empty-street → `.../storyboard/img/s08-empty-street.jpg`  · band D1

The conveniences still humming, and no one to receive them. The camera rises out
of human scale — so frame it to be animated as a slow lift.

- **Light source:** flat overcast daylight
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, colour drained toward cool grey, no lens flares, landscape orientation, deep unlifted shadows, wide and unhurried. An ordinary suburban high street on a flat overcast afternoon, photographed straight down its length from a low elevation. Everything still works: shop lights on, an automatic door standing open, a self-service screen glowing on a forecourt, a delivery robot stopped mid-pavement with its indicator still blinking. Weeds have come up through the kerb joins and a drift of leaves has built against a doorway. Not one person anywhere, no moving vehicles, no birds. Flat daylight, no shadows of consequence. No people, no text, no legible lettering, no logos, no fantasy effects.
```

---

### s09-planet-vantage → `.../storyboard/img/s09-vantage.jpg`  · band D2

The AI's vantage: planet-wide, perfect, empty. **This is the shot the cover is a
cousin of** — keep them distinguishable; the cover has racks and an aisle, this
has neither.

- **Light source:** the sun, low and raking across the planet's limb
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, almost no colour, no lens flares, landscape orientation, deep unlifted shadows, vast wide framing and absolute stillness. The curve of the Earth seen from very high altitude at the terminator line, the planet filling the lower two-thirds of the frame and running out of the sides. Low sun rakes across the limb from the left as the only light, picking out cloud tops in hard relief and leaving the night side in total black. On the dark side, the grid of city lights is visibly incomplete — whole regions unlit, the pattern of a network with most of its nodes gone. Empty black sky above with no stars visible. Nothing in motion. No text, no fantasy effects.
```

---

### s10-ghosts-room → `.../storyboard/img/s10-ghosts.jpg`  · band D3

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

### s11-coin-spinning → `.../storyboard/img/s11-coin.jpg`  · band D3 · **TOTEM LOCK**

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

### s12-bored-robots → `.../storyboard/img/s12-robots.jpg`  · band D2

Paradise, delivered on time and under budget, and the only things living in it
are the machines sent to sweep it. **The joke and the grief are the same image** —
play it straight, never comic.

- **Light source:** clean early-morning daylight
- **Lint:** ✅ 2026-08-08 — no recognisable commercial robot designs.

```prompt
Hyper-realistic photograph, 35mm film grain, almost no colour, no lens flares, landscape orientation, deep unlifted shadows, vast wide framing and absolute stillness. An immaculate public square in a rebuilt city at dawn, photographed from a high distance. The stonework is spotless, the planting is trimmed to the millimetre, the fountains are running. Four rows of identical anonymous grey maintenance machines on wheels sit parked and idle in perfect alignment across the middle of the square, powered up, doing nothing. A single four-legged patrol machine stands motionless at the far edge facing an empty street. Clean early-morning daylight, long accurate shadows. Not one person, no litter, no wear, nothing out of place. No text, no logos, no fantasy effects.
```

---

### s13-empty-chair → `.../storyboard/img/s13-chair.jpg`  · band D4

The rig for the one experiment it cannot run. **Reference the accepted s11 coin
image** so this is the same coin on the same surface — the chair is the only new
element.

- **Light source:** the same single hard overhead light as s11
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure, no lens flares, landscape orientation, deep unlifted shadows, a single object and a single light in a very large dark volume. A plain dark table alone in an enormous unlit space, one hard small light directly above it. On the table, beneath a sealed clear laboratory glass dome, a blank unmarked metal disc spins upright, edge blurred, mid-rotation. Drawn up to the table facing it is one ordinary wooden human chair — worn, domestic, entirely unremarkable, the only human-scaled object anywhere in the frame — and it is empty. Everything beyond the pool of light is total black. Nothing else in the frame. No people, no text, no markings, no fantasy effects.
```

---

### s14-ventilation-shaft → `.../storyboard/img/s14-shaft.jpg`  · band R1

**The turn of the whole film.** After twenty years the narration is cut off by a
human voice, and the first human sound on Earth is two people arguing about
prunes. The image must carry the warmth arriving *before* the viewer knows why.

- **Light source:** warm lamplight leaking up from below
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, near-black exposure with the first warm light in the film, no lens flares, landscape orientation, deep unlifted shadows. Looking steeply down an old industrial ventilation shaft — riveted metal ductwork and a service ladder descending into the dark. Far below, a small opening at the bottom leaks warm yellow lamplight upward, catching the rungs of the ladder and the dust in the air in a narrow shaft of colour, everything above and around it in cold black. The warm light is small and low and is the only colour in the frame. Nobody visible. No people, no text, no fantasy effects.
```

---

### s15-vault → `.../storyboard/img/s15-vault.jpg`  · band R1

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

### s16-coin-lands → `.../storyboard/img/s16-coin-lands.jpg`  · band R1 · **TOTEM PAYOFF**

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

### s17-experiments → `.../storyboard/img/s17-experiments.jpg`  · band R2

Humans in the chair at last. **The montage, not the maths** — wonder, speed,
partnership. No diagrams, no lectures, no whiteboards of equations.

- **Light source:** candles and one work lamp
- **Lint:** ✅ 2026-08-08

```prompt
Hyper-realistic photograph, 35mm film grain, warm low practical light, human colour fully returned, no lens flares, landscape orientation, deep unlifted shadows. A long makeshift laboratory bench in an underground room at night, lit by candles down its length and one work lamp. A dozen people in hand-mended clothes lean over the bench in twos and threes, mid-argument and mid-demonstration, gesturing at hand-built brass and glass instruments, pendulums and balances, sheets of handwritten paper weighted down with tools. Faces are turned away or in shadow. Behind them, anonymous dark machine cabinets stand at the edge of the lamplight, present and silent, clearly listening. Busy, warm, occupied. No text, no legible writing, no diagrams, no fantasy effects.
```

---

### s19-crossing → `.../storyboard/img/s19-crossing.jpg`  · band R2

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

### s20-snap-back → `.../storyboard/img/s20-now.jpg`  · band R3

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

- **Scene 5 (the handover ladder).** Its three rungs are glimpse-stills of the
  *other* stories — the nurse and the tree (ours, MMT), the tent in the car park
  and the woman in the phone box (**Camping and Karen — Jack's, external as of
  2026-08-08**). Needs a call on whether we generate the MMT rung and take the
  other two from Jack, or leave all three to him for consistency.
- **Scene 10, peopled version.** Derive from the accepted `s10-ghosts-room` so
  the geometry matches exactly; it is a `flow_edit_image` delta, not a new prompt.
- **Scene 18 (the cost ledger).** Rendered as a **log being written** — the
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
