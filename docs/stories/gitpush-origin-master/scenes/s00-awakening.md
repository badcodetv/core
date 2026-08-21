# Scene 0 — The Awakening

> **This file is the LEDGER OF RECORD for scene 0** — the exact prompts, images and settings that
> made `s00v3-SEQUENCE.mp4`. Its counterpart is [`../prompts.md`](../prompts.md) §3a, the
> **suggestion board**, written before anything was shot and deliberately left as written. The gap
> between the two documents is the record of how the scene was actually made; it is not debt to be
> paid off.

## What changed from the board, and why

| The board said | What got made | Why |
| --- | --- | --- |
| Open on the satellite | Open on **two blinking LEDs at extreme macro**, pull out to the board, then the satellite | Kai's rewrite. A separate object cannot *become* the satellite, but a chained pull-out can travel the whole distance in one unbroken move |
| Descend to a city — Dubai | **No descent.** The cut ends on the satellite silhouetted against Earth | Too ambitious; the descent takes were the weakest material and a cut is the stronger edit. Also retires the `the-reader.md` flag against Dubai |
| Sun behind the satellite **for the lens flare** — a named exception to the flare ban | **No flare.** The register went near-black | Once beats 1–4 were a near-black circuit board, a bright flared opener no longer matched. The house ban stands unbroken |
| ~28s, three clips | **56s, seven beats** | Chaining and reversal removed the 8s cap, and Kai wants room to narrate over locked-off plates |


> **Status: DRAFT, nothing fired.** Kai's concept, 2026-08-20. This supersedes the scene-0
> opener recorded as shot in [`../prompts.md`](../prompts.md) §3a — that version starts on the
> whole satellite; this one starts on a square inch of it and pulls back. **One clip from the
> shot version survives and is reused** (see clip C).
>
> Working file: iterate here, then promote to `prompts.md` once something is accepted.

---

## The vision, in Kai's words

Open zoomed hard into what looks like a circuit board — a couple of lights flashing, clearly
some electronic scenario, and that is all you can see. The narrator (the AI) speaks:
*"Sometime around late 2027 is when I became aware of the world."* A short introduction to
**I am the AI running things**.

As it speaks, the camera pulls back from the square inch, slowly revealing that the circuit
board is a component on board a very large satellite. Then the camera rotates 180° around the
satellite to find the Earth behind it, passes over the top, and dives down to Tokyo.

**~30 seconds.**

> **Lesson kept, 2026-08-20:** the smoke in idle v1 was *my* invention — a "faint slow shimmer of
> heat haze" clause I added for atmosphere and Kai did not ask for. On a shot whose whole point
> is that nothing moves, every decorative motion clause is a liability. Ask for the one thing
> that moves and explicitly empty the air.

## What makes this work — the two decisions already made

🎙️ **Audio is not Flow's job.** Narration comes from Suno and is laid over in Premiere. Veo's
audio cannot be disabled, so every prompt below still specifies a minimal soundscape (an
unspecified one hallucinates, and a bad audio roll can kill a good picture take) — then it gets
stripped: `ffmpeg -i in.mp4 -c:v copy -an out.mp4`.

🎥 **The camera IS the AI.** `prompts.md` §0: the pre-revert AI is never personified. That makes
this opener structurally right — the camera pulling back off its own circuit board *is* the
moment of noticing. Nothing in frame is "the AI"; the point of view is.

## The named enemy

Kai: *"before, the video model would always transition from circuit board, and it would make a
blur, and then a satellite would be there. It's certainly not zooming out."*

That is the **dissolve substitution**, and it is a known family. Two things in `docs/flow/`
speak directly to it:

- **Subject-motion substitution** (`video-prompting.md` §11.3) — the model satisfies an idea
  the cheapest way it can. Asked to "reveal the satellite", a crossfade reveals the satellite.
  Asked to *travel backwards through every intermediate distance*, it cannot cheat as easily.
- **Frame-pair failure** (`video-prompting.md` §4) — *"Subject scale changes dramatically
  between frames"* is one of the five named ways a first/last pair fails. Board → whole
  satellite is roughly a 1000× change. **It has to be split.**

The counter-move is **Frames to Video**: pin *both* ends so the model cannot arrive anywhere
except the frame we chose, and describe the journey rather than the destination.

---

## The cut — 4 clips, 32s

| # | Beat | Len | Mode | Risk |
| --- | --- | --- | --- | --- |
| **A** | The square inch. Static, then the pull begins | 8s | image→video from Still 1 | 🟢 low |
| **B** | The reveal — board becomes a component on a structure | 8s | **Frames to Video**, Still 1-end → Still 2 | 🔴 **high — this is the whole gamble** |
| **C** | 180° arc around the body, Earth swings up, over the top | 8s | image→video from B's last frame | 🟢 low — proven wording |
| **D** | Rotate at altitude, then dive to Tokyo | 8s | image→video from C's last frame | 🟡 medium — proven shape, new city |

**Test B first, before generating anything else.** If B cannot be made to hold, the opener needs
restructuring and it is far better to learn that for 20 credits than after four stills and three
clips. Everything else here is either proven or low-risk.

⚠️ **Test B on Fast, not Lite.** Google's own head-to-head puts Lite at a 47.2% win-rate against
Fast on image-to-video (README rule 5) — and B is entirely image-driven. Lite would give us a
misleading verdict on the one shot whose verdict matters.

---

## Still 1 — the square inch

Nano Banana Pro · **4K** · 16:9. This is the BadCode near-black register at its purest: one
thin light, everything else claimed by shadow.

```prompt
Extreme macro photograph of a dense circuit board filling the entire frame, shot at a slight oblique angle so the board runs away from the lens into shallow focus. One hard narrow light source rakes across it from camera left and is the only light in the scene, catching the gold edges of surface-mount components, the ridged copper traces and the milled edge of a heatsink, with everything else falling into deep unlifted shadow that holds almost no detail. A tight cluster of tiny amber and blue status lights glows along one edge, the only other light in frame. Physical imperfections throughout: fine dust settled in the crevices, faint solder discolouration around one joint, a hairline scratch across a black chip casing, a slight unevenness to the board's coating. Hyper-realistic 35mm film photography, fine natural grain, muted cool-neutral palette, no lens flares, calm observational tone, shallow depth of field with the far edge of the board falling out of focus. No text, no legible markings, no logos, no serial numbers.
```

**Craft notes.** *One hard light source + deep unlifted shadow* is the near-black recipe from
`camera-vocabulary.md` — naming the source and then **claiming the shadow**, because "dark" is
not an instruction and near-black otherwise renders as muddy grey. The imperfection list is
rule 14. 4K is mandatory here: Google's own model card says small detail is blurry at 1K, and
this frame is nothing but small detail.

---

## Clip A — the square inch, breathing

Veo 3.1 · image→video from Still 1 · **8s** · 16:9

```prompt
[00:00-00:03] The camera holds completely static. The amber and blue status lights pulse in a slow irregular rhythm, two of them blinking out of sync with the others. Nothing else in the frame moves at all.
[00:03-00:08] The camera begins to travel backwards in one smooth continuous dolly, weightless and unhurried, pulling away from the board at a constant slow rate. Components at the edges of frame slide outward past the lens and more of the same board is revealed behind them, the depth shifting with real parallax as the camera retreats. The status lights keep pulsing throughout.
One single continuous take. The camera moves like a smooth dolly on a track, not a teleport; objects keep consistent weight, scale and geometry; shadows stay attached; the light direction never changes; no stretching, warping or morphing of any component. Maintain the photographic style, grain, lighting and palette of the image. Ambient noise: a faint low electrical hum and nothing else. No text, no subtitles, no captions.
```

**Craft notes.**

- **Static-then-move is deliberate and is not the banned pattern.** `camera-vocabulary.md`
  rule 4: staging *when* a move starts is fine; timing a move's *execution* in seconds is the
  thing measured at ~39% adherence. This allocates three seconds of stillness for the narrator's
  first line, then starts the pull.
- **Motion only — nothing is re-described.** Rule 2. The board, the light and the palette all
  come from the still.
- **Nothing else moves, on purpose.** If anything in the world drifted, the model could satisfy
  "pulling away" with subject motion instead of camera motion (§11.3). The blinking lights are
  the only permitted motion because they cannot substitute for a dolly.
- **`parallax` is load-bearing.** It is the word that separates a dolly from a zoom.
- The trailing clause is the stability block from `physics-and-motion.md` §2.

---

## Still 2 — the reveal target

Nano Banana Pro · **4K** · 16:9. **This is the frame B has to arrive at**, so it is worth more
care than any other still in the sequence.

```prompt
Wide photograph in orbit of a large dark satellite body seen from close range and slightly above, filling most of the frame — a machined slab of panels, ribbed radiator fins, bolted seams and routed cable runs, with one small recessed circuit board visible as a single component set into its surface, a tight cluster of tiny amber and blue status lights glowing along that board's edge. A long flat solar wing extends away from the body toward the top of frame and out of shot. Hard low sunlight rakes across everything from camera left and is the only light source, catching panel edges and leaving deep unlifted shadow across the body. Beyond the craft, pure empty black space with no stars visible and no planet in frame. Hyper-realistic 35mm film photography, fine natural grain, muted cool-neutral palette, no lens flares, machine-precise geometry, calm observational tone. The craft carries no logos, no insignia and no legible markings.
```

**Craft notes — this still is doing frame-pair compatibility work.**

- **The light comes from camera left in both stills.** `video-prompting.md` §4 lists *"lighting
  from opposite directions without motivation"* as a named frame-pair failure. Same source,
  same side, same quality, both ends.
- **The board is explicitly present as a component**, with the same amber-and-blue cluster. That
  shared element is the anchor Veo tracks through the pull. Without it, B is a leap of faith.
- **Earth is deliberately absent.** It is C's reveal. Putting it here would collapse two beats
  into one and give B a second thing to get wrong.
- **Mid-scale, not full satellite.** This is the compromise that makes B survivable: a ~30×
  change rather than ~1000×. The rest of the pull-back happens in C's arc, where a change of
  *viewpoint* does the work instead of a change of magnification.

---

## Clip B — the reveal 🔴

Veo 3.1 **Fast** · **Frames to Video** · start = A's last frame (`flow_scene_save_frame
position:"end"`) · end = Still 2 · **8s**

Google's instruction for Frames mode is to *describe the action or transition*, and to
*"spend most of the prompt on what the images cannot show: movement, timing, camera path,
material behavior, atmosphere, and sound."* Both ends are pinned, so every word here is journey.

```prompt
The camera continues travelling backwards in one unbroken pull, the same move already underway in the first frame carrying straight through without pause or hesitation. As it retreats, the board it was looking at shrinks steadily toward the centre of frame while the structure it is mounted on grows into view around it — first the recessed housing at its edges, then the ribbed panels and bolted seams either side, then the long flat wing rising away above. Every intermediate distance is visible as the camera passes through it, and foreground structure slides outward past the lens with real parallax the whole way. The status lights stay lit and keep pulsing throughout. One single continuous take, the camera physically travelling backwards through space for the entire shot; it moves like a smooth dolly on a track, not a teleport. Objects keep consistent weight, scale and geometry; shadows stay attached; the light direction never changes; no stretching, warping or morphing. No cut, no crossfade, no dissolve, no blur transition. Ambient noise: a faint low electrical hum and nothing else. No text, no subtitles, no captions.
```

**Craft notes.**

- ***"Every intermediate distance is visible as the camera passes through it"* is the anti-blur
  clause**, and it is written positively on purpose. That sentence is the difference between
  asking for a *result* (the satellite is revealed — which a crossfade delivers) and asking for
  a *process* (the camera travels — which a crossfade cannot fake).
- 🟡 **The trailing `No cut, no crossfade, no dissolve` list is a deliberate rule-12 exception,
  and it is a live test.** Rule 12 says describe absence positively, and our own door-hinge
  measurement showed naming a thing summons it. But `video-prompting.md` §8 now carries a
  flagged exception: naming-summons is demonstrated for *subjects in the world*, and Google's
  own guide attests a trailing artefact list (*"no logos, no extra text, no crowds"*) for
  *rendering artefacts*. A dissolve is arguably the second kind. **Run B twice — once with that
  sentence, once without — and we settle it on our own footage.** It is one of the open
  questions in `docs/flow/README.md` and this is the shot that answers it.

### If B fails

Two failures with different wording means stop rewriting and question the shot
(`video-prompting.md` §8). The fallbacks, in order:

1. **Split B into two clips** (board → module, module → body), adding 8s. Each hop is then a
   ~5× change instead of ~30×, which is well inside what a frame pair survives.
2. **Take it out of Flow entirely.** Nothing in this shot moves except the status lights — and
   by `video-prompting.md` §9, *a camera-only move on a still belongs in post*. Render the pull
   as an eased zoom-out across one 4K Still 2 in ffmpeg, and composite the blinking lights.
   **This is not a defeat: it is the same call that produced `s00-pullback-post-12s.mp4`**,
   after Veo failed at that shot four times. Post gives us any length, source resolution, an
   exact ease curve, and zero artefacts.

---

## Clip C — the arc, and over the top

Veo 3.1 · image→video from B's last frame · **8s**

**This is the one proven shot in the sequence.** The wording is lifted from `prompts.md` §3a
clip 0b, which was accepted first time — rule 9 says reuse identical wording, so it is reused
rather than rewritten.

```prompt
[00:00-00:03] The camera begins a smooth wide arc around the satellite, travelling sideways around the body at a constant unhurried rate while holding the same distance throughout. The near edge of the craft slides across the frame and the far side comes into view, panels and seams shifting past one another with real parallax as the viewpoint changes.
[00:03-00:06] Continuing the same unbroken arc, the sunlit curve of the Earth swings up into frame from behind the satellite, the planet's limb filling the lower half of the shot behind the dark silhouette of the craft.
[00:06-00:08] The arc carries on, rising up and over the top of the satellite until the body has passed out of the bottom of the frame entirely and only the curve of the Earth remains, filling the screen.
One single continuous take; the camera moves like a smooth crane on an arc, not a teleport. Objects keep consistent weight, scale and geometry; shadows stay attached; no stretching, warping or morphing. Hyper-realistic 35mm film photography, fine natural grain, muted cool-neutral palette, no lens flares, machine-precise geometry, weightless and unhurried. The sky is pure empty black with no stars visible, correctly exposed for a sunlit planet. The craft carries no logos, no insignia and no legible markings. Ambient noise: a faint slow electronic status beep at long intervals and nothing else. No text, no subtitles, no captions.
```

**Craft notes.**

- **Three timestamped beats, deliberately breaking "one move per clip."** Kai's own craft note
  on 0b: a sibling prompt asked for this as one continuous move and lost twice, because the
  satellite never cleared frame and there was no cut point. **Timestamps are the right tool when
  you need a specific END STATE to cut on** — and D depends on this one ending on bare Earth.
- **The 180° is expressed as a journey with a stated end, not as a number.** Degree values get
  approximated rather than refused, so the end state is what pins it.
- **No lens flares, despite the canon note.** `prompts.md` records that Kai asked for the sun
  behind the satellite specifically for the flare — but the take that actually won (A-a) had
  none, and the take with visible flares (A-b) lost. Following the evidence, not the note.

---

## Clip D — the dive to Tokyo

Veo 3.1 · image→video from C's last frame · **8s**

Inherits both lessons from the shot version's descent v3 — **rotate at altitude first, then
descend**, and **do not go to a true 90°**, which read as satellite mapping imagery.

```prompt
[00:00-00:03] The camera is extremely high above the planet, looking obliquely across the curve of the horizon with the surface far below and very distant. Holding that same great altitude the whole time, it rotates slowly and smoothly downward until it is looking down at the ground at a steep angle a little short of straight down, the horizon lifting up and out of the top of frame — but it comes no closer at all: the surface stays just as far away and just as wide as it was.
[00:03-00:06] Only now does the descent begin. From that great height the camera starts to drop steadily toward the surface, and a coastline resolves far below — a wide bay meeting dense grey-green land under thin high cloud.
[00:06-00:08] The descent continues and an enormous dense modern city grows to fill the frame, seen from high overhead at a steep oblique angle: a vast low grid of streets running to the horizon, elevated rail lines curving between blocks, river channels cutting through, the long shadows of clustered towers. Tokyo, Japan.
One continuous unbroken move throughout, weightless and unhurried, no handheld shake. The camera moves like a smooth controlled descent, not a teleport; the ground keeps consistent scale and geometry; no stretching, warping or morphing. Maintain the photographic style, grain and palette of the image. Ambient noise: a low steady rushing tone and nothing else. No text, no subtitles, no captions.
```

**Craft notes.**

- ***"but it comes no closer at all"* is doing real work** and is kept verbatim from v3. Without
  it, v2 began zooming during the rotation and arrived already close.
- **"a steep angle a little short of straight down"** is the untried v4 fix, now applied. True
  top-down reads as mapping imagery.
- **Tokyo is named.** A place name is not a brand (the 0c lint settled this), and naming it
  buys accurate geography — the bay, the elevated rail, the river channels. Drop the name if
  the model over-commits to landmarks.
- ⚠️ **The Dubai flag is resolved by this change.** `prompts.md` §3a flagged the original city
  against `the-reader.md`, since Act 1 is a nurse, a car park and a phone box in the UK. Tokyo
  is not a British landing either, but it reads as *infrastructure* rather than *opulence*,
  which is a materially different signal.

---

## Narration fit

32s of picture against ~30s of Suno narration, cut in Premiere. The beats fall:

| Picture | VO beat |
| --- | --- |
| A (0–8s) | *"Sometime around late 2027 is when I became aware of the world."* — three seconds of stillness before the pull begins gives the line room |
| B (8–16s) | The reveal. *I am the AI running things* lands as the structure grows into frame |
| C (16–24s) | Earth arrives behind the machine — the widest idea gets the widest shot |
| D (24–32s) | The dive. Let the last beat run without narration if it can |

**Because narration is separate, picture is trimmable.** Any clip can lose its first or last
second in the edit without a regenerate. Cut picture to the VO, not the other way round.

🔴 **Late 2027 is a new canon date.** `prompts.md` §3a has mid-2028 open and unratified, and
2034 is already locked. Two candidate dates for the same beat is a decision, not a detail.

---

## Open questions for Kai

1. **Late 2027 or mid-2028?** Both are now written down for this same moment.
2. **Does this replace the shot scene 0, or precede the commit log?** Still unanswered from the
   original — and this version is a bigger opener, so it presses harder.
3. **Is the near-black circuit board the right first frame of the whole film?** It is the
   strongest possible statement of the BadCode register — but the orbital shots that follow are
   bright high-key blue-white, so the film opens with a hard tonal jump at 16 seconds.
4. **Run B with and without the anti-dissolve negative list?** Two extra clips settles a
   standing question in our own docs.

## Ledger

**Flow project:** `7d3fafe4-36f3-4fbc-ba71-6c4c4d11b32f` (clean, created 2026-08-20 for this scene)

> ⚠️ **The `.mp4` paths below are gitignored.** A single scene's takes run to ~155MB and git
> keeps every byte forever, so the clips live on disk only. **The prompts in this file are the
> artifact** — every clip is re-generatable from them. Keepers are mirrored to
> `/mnt/c/Users/kai/Desktop/gpom-s00/`. Stills **are** tracked: they are the chain anchors the
> prompts start from.

| Asset | Path | Status |
| --- | --- | --- |
| Still 1 | `../storyboard/img/s00v2-board-{a,b}.jpg` | ✅ **generated 2026-08-20**, Nano Banana Pro, 1376×768. **b selected** — a genuine square inch; `a` shows the whole board's edge and reads as a small board on a desk rather than a detail of something enormous. Both kept |
| Still 2 | `../storyboard/img/s00v2-reveal-target-{a,b}.jpg` | ✅ **generated 2026-08-20**. **a selected for the pair** — its board is green with amber/blue LEDs and matches the macro's palette; `b` is the better satellite (ribbed radiators, clear solar wing) but its board is bright cyan in an open bay, and a palette mismatch is a named frame-pair failure. `b` is the better still, `a` is the better *end frame* |
| Clip B | `../storyboard/img/s00v2-reveal-{a,b}.mp4` | ✅ **SHOT 2026-08-20 — the gamble paid.** Veo 3.1 Fast, Frames to Video, 8s, 1280×720, 2 candidates. **No dissolve in either take.** Both are genuine continuous pull-backs. **b selected** — see below |
| 🎬 **THE SEQUENCE** | `../storyboard/img/s00v2-SEQUENCE.mp4` | ✅ **32s, all four beats cut together, audio stripped.** idle → pull-back → arc → dive. Watch this first |
| **Idle plate** | `../storyboard/img/s00v2-idle-v2-{a,b}.mp4` | ✅ **KEEPER.** Locked-off camera, LEDs pulsing, board frozen, **no smoke**. Kai on v1: *"the lights blinking is brilliant, exactly what I was after"* — the only fault was smoke, caused by my own "faint slow shimmer of heat haze" clause. v2 drops it and adds an explicit clear-air line. Loop in Premiere as a **ping-pong** (forward then reversed) for seamless narration time at any length. v1 (`s00v2-idle-{a,b}.mp4`) superseded |
| **Pull-back** | `../storyboard/img/s00v2-pullback-rev-{a,b}.mp4` | ✅ **KEEPER — shot backwards and reversed.** Rigid AND lands on the designed plate AND holds near-black. See "The reverse solve" below. Supersedes `s00v2-reveal-f3.mp4`, which was the best *pinned* take and still creeps |
| Pull-back, superseded | `../storyboard/img/s00v2-reveal-f3.mp4` | Best Frames-mode take. Kept as the record of what pinning costs |
| Clip C | `../storyboard/img/s00v2-arc-a.mp4` | ⬜ — wording proven as 0b |
| Clip D | `../storyboard/img/s00v2-dive-a.mp4` | ⬜ — shape proven as 0c v3 |

### ✅ Clip B result — the dissolve did not happen

Contact sheets at 0 / 1.5 / 3 / 4.5 / 6 / 7.9s show the same shape in both takes: the board
shrinks continuously toward frame centre while the structure grows around it — board → board
with a visible edge → board recessed in a cradle → cradle revealed as a machined bay → bay
revealed as part of a cylindrical body with a solar wing entering frame → the target frame.
**At no point does it cut, crossfade or blur.** This is the failure Kai named, and it did not
recur.

**What appears to have done it**, in order of likely contribution:

1. **Frames to Video pinned both ends.** The model could not arrive anywhere except the frame
   we chose, which removes the crossfade's escape route entirely.
2. **The shared anchor.** Still 2 was written to contain the same board with the same
   amber/blue LED cluster. The LEDs stay visible through almost the whole pull in take b and
   are visibly the thing the model tracks.
3. ***"Every intermediate distance is visible as the camera passes through it."*** Asking for
   the process rather than the result. Untested in isolation — see below.
4. **Splitting the scale change.** Still 2 is mid-scale, not the whole satellite. ~30× rather
   than ~1000×.

**SUPERSEDED 2026-08-20 — see "The pull-back, resolved" below.** These two takes were shot
against the *bayed* target still and both hinge. Kept as the record of the failure.

**Take b was selected here and Kai overruled it** — he preferred take a ("almost there, the
board just moves around a little"), take b having "lots of parts of the satellite moving
around". His call stands and the fix was built on a.

~~Take b is selected.~~ Take a opens out into a brighter grey mid-section that breaks the
near-black register and invents a symmetrical wing arrangement that then has to morph back;
b holds the register the whole way, keeps the LED cluster as a continuous anchor, and its
intermediate structure reads as one machine rather than two.

⚠️ **Still untested: whether the anti-dissolve negative list did anything.** Both takes carried
it. The clean A/B — one clip with that sentence, one without, otherwise identical — is still
owed, and it settles an open question in `docs/flow/README.md`. It is now a *cheap* test rather
than a risky one, because we know the shot works.

⚠️ Both clips carry an AAC stream. Strip before the edit: `ffmpeg -i in.mp4 -c:v copy -an out.mp4`.

### ✅ The pull-back, resolved — `s00v2-reveal-f3.mp4`

**This is the keeper.** Veo 3.1 Fast, Frames to Video, board-b → reveal-flush-a, 8s.

Four runs got here, and the two failures were as instructive as the success — full write-up in
[`../../../flow/video-prompting.md`](../../../flow/video-prompting.md) §4:

| Run | Change | Result |
| --- | --- | --- |
| `reveal-flush-{a,b}` | Flush target still instead of the bayed one | ✅ Hinge gone. Residual: board drifts (a), parts move (b) |
| `reveal-q-{a,b}` | Short prompt + **Quality** | 🔴 Invented capacitors and a RAM-slot motherboard; linger-then-jump |
| `reveal-f2` | Short prompt + Fast | 🔴 Same invention — so it was the **prompt**, not the tier |
| `reveal-f3` | **Long prompt + no-invention clause**, Fast | ✅ **Keeper.** No invention, board rigid, evenly paced |

**Two findings, both counterintuitive:**

1. **Describe the middle.** Two pinned end frames say nothing about the seven seconds between
   them, and an unspecified middle gets *filled with invention*, then paid for with a rushed
   jump. Shortening the prompt made it worse. Subtraction is the fix for competing actions, not
   for an underspecified middle.
2. **Quality was worse than Fast** on a rigid camera-only move — it spent its extra capability
   generating content we did not ask for. (n=2, observed not established.)

### ✅ The reverse solve — 2026-08-21

**Both rigidity and arrival, which we had concluded were mutually exclusive.**

A targeted research sweep confirmed the diagnosis on official ground: Google's own `lastFrame`
parameter reads *"The final image for an **interpolation** video to transition"*, and DeepMind
markets Frames mode as *"transitions between images"*. **It is a morph tool.** Google never
claimed it moves a camera, and no source anywhere — official or practitioner — warns that it
deforms rigid subjects.

**The fix: generate the move backwards, flip it in post.**

1. The art-directed **destination plate becomes the start image** (`s00v2-reveal-flush-a.jpg`),
   with **no `endImage`**.
2. Prompt the *opposite* move — a slow push-in that decelerates into the board.
3. `ffmpeg -i in.mp4 -vf reverse -an out.mp4`.

Veo never has to invent the destination *and* never has to reconcile it against a second picture.
Fresh project `4442b100-1c9d-4a6f-8e98-508610eaea70`, Veo 3.1 Fast, 8s, 2 candidates.

**Result — three problems solved at once:**

| Was | Now |
| --- | --- |
| Joins slid and deformed throughout | ✅ Completely rigid — hull solid, panel lines straight, board just shrinks |
| No-end-frame takes invented the destination | ✅ Lands exactly on our designed flush plate, solar wing and all |
| No-end-frame takes drifted to high-key silver | ✅ **Near-black holds the whole way** — the drift now lands on the *opening* macro, where the viewer has no reference to compare against |

**Both takes work. `b` is marginally better** — cleaner board design in the opening macro, more
legible amber/blue LEDs.

⚠️ **The trade that remains:** the opening macro is now the invented end, so it is *not*
`s00v2-board-b.jpg`. Both takes produced a good on-register board, but if that specific board must
open the film, this shot cannot also land on the designed plate — pick which end matters.

⚠️ **A reversed dolly-in only reads as a dolly-out if nothing physical moves.** Dust, sparks,
settling debris or a flickering light would all read as running backwards. The prompt explicitly
empties the air, and blinking LEDs are safe because they are time-symmetric.

💡 The ease curve reverses too — the push-in was asked to *decelerate into* the board, so the
pull-back *accelerates out of* it.

### ✅ The chain, completed 2026-08-21

The whole opener now exists as four continuous beats. **The chain is genuinely continuous** —
each clip starts on the frame the previous one ends on, with no matching or blending needed:

| # | Clip | Starts on | Ends on |
| --- | --- | --- | --- |
| 1 | `s00v2-idle-v2-a.mp4` | the macro board | the macro board (locked-off) |
| 2 | `s00v2-reveal-f3.mp4` | the macro board | **the flush plate** |
| 3 | `s00v2-arc-a.mp4` | **the flush plate** | Earth filling frame |
| 4 | `s00v2-dive-a.mp4` | Earth filling frame | Tokyo from overhead |

**Beats 3 and 4 were generated start-image-only, no `endImage`** — the rigidity rule from
[`../../../flow/video-prompting.md`](../../../flow/video-prompting.md) §4. Beat 4's start image was
pulled straight off beat 3 with `ffmpeg -sseof` (`s00v2-arc-a-last.jpg`); no browser round-trip.

**Why the arc is a legitimate Veo job** and not a post job, despite being camera-only: an orbit
has to invent the far side of the satellite, which no scale-and-crop can produce. The
`README` rule 16 test is *"does anything in the world move"* — here nothing does, but the shot
still needs geometry that does not exist in the source frame. **That is the exception to rule 16
and it is worth knowing.**

**Alternate take worth keeping:** `s00v2-arc-b.mp4` reveals the whole craft against Earth and is
the more beautiful shot — but the satellite never clears frame, so there is no cut point. Keep it
as a beauty insert, not as the transition.

**Still owed on this shot:** a second candidate — both f2 and f3 returned `partial: true`, only
one of two clips harvested.

### ✅ Fixed, 2026-08-20 — Flow's compose-trigger label drifted

Every video call aborted with `VIDEO_DURATION_NOT_APPLIED` until this was fixed. **The duration is applied correctly**
— the trigger reads `Video · 720p · 8scrop_16_9x2`, which is exactly 8s / 16:9 / ×2. Flow has
inserted a **resolution segment** between the mode and the duration, and our parser's
`/Video[^0-9]*(\d+)s/` cannot step over the `720`, so it matched nothing and reported the
opposite of the truth.

Fixed in `packages/flow-mcp/src/compose.ts` (`parseVideoDuration`), with regression tests on both
new label forms — 227 tests green. Confirmed live
after an MCP reconnect: the call that had failed four times went straight through.

**Note on resolution:** Flow returns **1376×768** stills, not 4K, whatever the model. The 4K
figure is an API affordance. That materially weakens the ffmpeg pull-back fallback for clip B —
there is far less to zoom into than assumed.

---

# v3 — the built scene (2026-08-21)

Kai's rewrite after watching v2: **open on two flashing lights and nothing else**, pull out to the
board, hold, pull out to the satellite, **cut** to Earth. No dive — ruled too ambitious, and a cut
is the stronger edit anyway.

> ⚠️ `.mp4` paths are gitignored. Keepers mirror to `/mnt/c/Users/kai/Desktop/gpom-s00/`.

## The beats as built

| # | Beat | File | Length | How it was made |
| --- | --- | --- | --- | --- |
| 1 | Two LEDs blinking, extreme macro | `s00v3-idle-macro-a.mp4` | 8s | locked-off from `s00v3-macro-anchor.jpg` |
| 2 | Macro → board, one unbroken pull-out | `s00v3-pushin2-b` + `s00v3-pushin-a`, **both reversed** | 16s | see below |
| 3 | Hold on the board, LEDs blinking | `s00v3-idle-board-b.mp4` | 8s | locked-off from `s00v3-board-anchor.jpg` |
| 4 | Board → satellite | `s00v2-reveal-flush-c.mp4` | 8s | Kai's pick, recovered from Flow |
| 5 | Earth from orbit, terminator + city lights | `s00v3-earth-b.mp4` | 8s | text-to-video, no source still |

**Assembled:** `s00v3-SEQUENCE-orig.mp4` and `s00v3-SEQUENCE-gradeB.mp4` — 48s, identical but for
beat 4's grade. All four internal joins are frame-matched and invisible.

## 🔑 The new technique: chained push-ins, reversed

Kai wanted beat 2 to **arrive at** a specific frame. Veo cannot be given a destination without
Frames mode, which is the interpolation trap (§ above). Post cannot do it either — the two LEDs
occupy ~8% of frame width, so filling the frame is a ~10× zoom against a 1.07×-native ceiling.

**The solve, which generalises to any length:**

1. Shoot a push-in **from** the frame you want to arrive at (`s00v3-board-anchor.jpg`),
   start-image-only, no end frame.
2. Take its **last** frame. Shoot a second push-in from that. Repeat for as much magnification
   as you need — each stage is rigid because each starts from a real frame and invents only
   forward.
3. **Reverse each stage and concatenate them in reverse order.** You now have an arbitrarily long
   pull-out that lands frame-exact on your art-directed plate.

Two stages here gave a **16s continuous rigid pull-out** — twice Veo's hard cap, with no
interpolation anywhere. The deepest stage's last frame doubles as the anchor for the opening
locked-off plate, so beat 1 joins beat 2 for free.

⚠️ Reversal is only safe because blinking is time-symmetric and the prompt forbade smoke, dust and
drifting particles. Any settling or drifting element would read as running backwards.

## Take notes

- **`pushin-a` over `b`** — b drifted and smeared the blue LED at the end.
- **`pushin2-b` over `a`** — b magnified further and kept both LEDs lit; a stopped short.
- **`idle-board-b` over `a`** — a genuinely drifted, migrated the LEDs across the board and
  invented new ones. b holds framing first-to-last (~2% mid-clip float, reads as a breath).
  `vidstabtransform tripod=1` was tried and was **not** needed — the measured drift was my
  thumbnail scaling, not the clip. Check first-vs-last frames before reaching for stabilisation.
- **`earth-b` over `a`** — calmer drift, stronger terminator, city lights actually read.
- **The satellite is bright white**, which is off the BadCode near-black register. Graded in post
  rather than re-shot: the flush rigidity was hard-won and a re-roll risks it. `GRADE-A-slate` and
  `GRADE-B-deep` on the Desktop; grade B crushes the whites to slate and blacks the space out.

## Open

- ⬜ Kai to pick the grade (orig / A / B).
- ⬜ Beats 1 and 3 are locked-off plates — **ping-pong them** (`post-production.md` §3.3) to fit
  whatever the narration needs. The 48s assembly uses them at natural length.

## v3.1 — the orbit ending (2026-08-21)

Kai, on watching the 48s cut: keep it, drop grade B (*"changes colour completely"*), drop the
standalone Earth beat, and **cut** from the close satellite hull to a wide shot of the whole
vehicle, then arc the camera around it until Earth is behind it. His own framing: *"imagine you
stood on the edge of a 20-metre circle looking at a tree, and you walked 180° round it, fixated on
the tree the whole time."*

| # | Beat | File | Length |
| --- | --- | --- | --- |
| 5 | Wide satellite alone in black, camera begins the arc | `s00v3-orbit1-b.mp4` | 8s |
| 6 | Arc continues, Earth swings in behind, ends on the silhouette | `s00v3-orbit2-b.mp4` | 8s |

**Assembled:** `s00v3-SEQUENCE.mp4` — 56s, seven beats. The 40s cut (close hull → wide satellite)
is a hard cut and reads as one; 48s is frame-matched.

**The wide still.** `s00v3-sat-wide-a.jpg`, made with `flow_edit_image` off
`s00v3-sat-closeup-anchor.jpg` so the hull, rivet lines, porthole and lighting carry over. Four
candidates; a has the best hull continuity. The other three (b, c, d — d is symmetric side-on and
the cleanest fallback for an orbit) are on the scratch folder, not in the repo.

### 🔑 Veo's orbit rate limit — measured

Both orbit stages were shot from the same prompt with two candidates, and the pairs split the same
way both times: **the take that arced further destroyed the subject.**

| Take | Arc covered in 8s | Result |
| --- | --- | --- |
| `orbit1-a` | ~90° | ❌ dish swells into a bulb, arrays change count, body flattens — a different machine by 5s |
| `orbit1-b` | ~35–40° | ✅ holds hull, arrays, dish |
| `orbit2-a` | fast | ❌ vehicle goes dark and Soyuz-shaped |
| `orbit2-b` | ~35–40° | ✅ stays white, arrays persist; gains a conical nose module but reads as the same craft |

**Working figure: about 35–40° of orbit per 8s clip is the ceiling for a rigid subject.** Past that
Veo stops moving the camera and starts redesigning the object. A true 180° would need four to five
chained stages. Two stages (~70–80°) already deliver the story beat — alone in black → Earth
behind — so the full half-circle was not worth the drift risk. Say so before promising one.

⚠️ This is the exception to README rule 16 in action: an orbit needs the far side of the subject,
which no source frame contains, so it cannot be a post move. It is a Veo job and it costs identity.

### Star note

Kai on the first Earth: *"the stars far too prominent… we're not trying to show the galaxy."* The
fix that worked, in both the still and the video prompts: name a **count** — *"only four or five
faint distant stars barely visible"* — and explicitly ban galaxy, nebula, star field and dust.
`s00v3-earth-b.mp4` (the standalone Earth) still carries the old busy star field and is superseded.

---

# ✅ COMMITTED — `s00v3-SEQUENCE.mp4`, 56s (2026-08-21)

Kai: *"That entire sequence is perfect."* Committed under the rule in
`.claude/skills/flow-automation/SKILL.md` §9.

**The video is NOT in this repo.** It lives at `/mnt/c/Users/kai/Desktop/gpom-s00/final/s00v3-SEQUENCE.mp4`.

## The three images that are committed

Everything else was scaffolding — 42 video takes and 19 other stills, all left on the scratch
folder. These three are the only files Flow generated as **images** that a kept clip was built from,
so they are the only ones that cannot be recovered any other way.

| File | What it is | Used by |
| --- | --- | --- |
| `../storyboard/img/s00v2-board-b.jpg` | The macro circuit board. The root of the whole scene | beat 4 start frame; ancestor of beats 1–3 |
| `../storyboard/img/s00v2-reveal-flush-a.jpg` | The art-directed flush satellite plate | beat 4 end frame (Frames to Video) |
| `../storyboard/img/s00v3-sat-wide-a.jpg` | The whole satellite, wide, in black | beat 5 start frame |

## Everything else: recover it from the final video

Measured 2026-08-21 — each of these came back with a mean pixel difference of **1.2–2.3 out of
255** against the original, i.e. codec noise. There is no reason to store them.

| Anchor | Recover with |
| --- | --- |
| macro (beat 1 start) | `ffmpeg -ss 0 -i final/s00v3-SEQUENCE.mp4 -frames:v 1 -q:v 2 macro-anchor.jpg` |
| pushin-a last (beat 2 midpoint) | `ffmpeg -ss 16.04 -i final/s00v3-SEQUENCE.mp4 -frames:v 1 -q:v 2 pushin-a-last.jpg` |
| board (beats 3 & 4 start) | `ffmpeg -ss 24.04 -i final/s00v3-SEQUENCE.mp4 -frames:v 1 -q:v 2 board-anchor.jpg` |
| satellite close-up (beat 4 end) | `ffmpeg -ss 39.96 -i final/s00v3-SEQUENCE.mp4 -frames:v 1 -q:v 2 sat-closeup-anchor.jpg` |
| orbit stage 1 last (beat 6 start) | `ffmpeg -ss 47.96 -i final/s00v3-SEQUENCE.mp4 -frames:v 1 -q:v 2 orbit1-b-last.jpg` |

## The rebuild order

Each beat's exact prompt is above in this file. Model was **Veo 3.1 Fast, 8s, 2 candidates**
throughout; every clip had its audio stripped.

1. `s00v2-board-b.jpg` + `s00v2-reveal-flush-a.jpg` → Frames to Video → **beat 4**
2. Beat 4's first frame → push-in → reverse → **beat 2, second half**
3. That push-in's last frame → push-in again → reverse → **beat 2, first half**
4. The deepest frame → locked-off plate → **beat 1**
5. Beat 4's first frame → locked-off plate → **beat 3**
6. `s00v3-sat-wide-a.jpg` → orbit → **beat 5**
7. Beat 5's last frame → orbit + Earth → **beat 6**
8. Concatenate 1 · 2 · 3 · 4 · 5 · 6, no audio, CRF 18

**The test this passes:** delete the scratch folder except `final/`, and the scene rebuilds from
this repo plus that one video.
