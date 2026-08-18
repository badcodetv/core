# Camera vocabulary

Shot, move, lens, lighting and grade terms, with how reliably Veo actually honours
each. Applies to both stills and video unless noted.

## Reliability tiers

**Tier 1 — dependable, use freely.**
Shot sizes: extreme wide / establishing, wide, medium, medium close-up, close-up,
extreme close-up, two-shot, over-the-shoulder, POV.
Moves: **push-in / dolly-in** (the safest move there is), dolly-out, pan, tilt,
tracking, static / locked-off, handheld.
Focus: shallow depth of field, bokeh, deep focus.
Angles: eye-level, low angle, high angle, Dutch angle, bird's-eye, worm's-eye.

**Tier 2 — works, expect retries.** Crane / jib, arc / orbit, rack focus, whip pan.

**Tier 3 — hero-shot only, budget failures.** Dolly zoom (vertigo), full 360° orbit,
anything requiring precise hand articulation in frame.

**Google backs the idea of tiering, without publishing tiers.** Its prompt guide carries the
same caveat twice, once over the angle list and once over the lens list: *"Some advanced camera
angles are not officially supported. The results and reliability may vary depending on the
overall prompt and your specific use case."* So the model has a supported core and a fringe;
which terms sit where is ours to measure, and the tiers above are that measurement.

## The official catalogue

Every term below is listed by name in Google's video-generation prompt guide, with the gloss
and the example it gives. Terms **not** in our tiers above are marked 🆕 — they were missing
from this file until 2026-08-18.

**Camera movements** — note that Google treats these as a *separate prompt component* from the
angle, which is why §Rules 1 asks for the camera in its own clause.

| Move | What it is | Google's example |
| --- | --- | --- |
| Static (fixed) | camera completely still | "static shot of a serene landscape" |
| Pan (left/right) | rotates horizontally **from a fixed position** | "slow pan left across a city skyline at dusk" |
| Tilt (up/down) | rotates vertically from a fixed position | "tilt down from the character's shocked face to the revealing letter in their hands" |
| Dolly (in/out) | camera **physically moves** closer or further | "dolly out from the character to emphasize their isolation" |
| 🆕 **Truck (left/right)** | camera physically moves **sideways**, often parallel to the subject | "truck right, following a character as they walk along a busy sidewalk" |
| 🆕 **Pedestal (up/down)** | camera physically moves **vertically**, keeping a level perspective | "pedestal up to reveal the full height of an ancient, towering tree" |
| Zoom (in/out) | the **lens** changes focal length; the camera does not move | "slow zoom in on a mysterious artifact on a table" |
| Crane | mounted on a crane, vertical or sweeping arcs | "crane shot revealing a vast medieval battlefield" |
| 🆕 **Aerial / drone** | high altitude, smooth flying movement | "sweeping aerial drone shot flying over a tropical island chain" |
| Handheld / shaky cam | less stable, jerky; realism, immediacy, unease | "handheld camera shot during a chaotic marketplace chase" |
| Whip pan | extremely fast pan that blurs; a transition | "whip pan from one arguing character to another" |
| Arc | circular or semi-circular path around the subject | "arc shot around a couple embracing in the rain" |

🔴 **Dolly and truck and pedestal are three different words for three different moves, and
"zoom" is none of them.** Naming the wrong one is the most common way a camera clause quietly
fails: ask for a "zoom" when you meant to travel through the space and you get a flat
magnification with no parallax. Our own scene-0 descent needed exactly this distinction — the
shot reads as a descent because it *pedestals and dollies*, and read as Google Earth when it
was written as a zoom.

**Lens and optical effects** — all officially listed: wide-angle, telephoto, shallow depth of
field (bokeh), deep depth of field, lens flare, 🆕 **rack focus**, fisheye, 🆕 **vertigo effect
(dolly zoom)**.

> **Official (rack focus):** "A medium shot of a detective's hand in the foreground, holding a
> single, spent bullet casing. The camera then performs a slow rack focus, shifting from the
> casing to reveal the anxious face of a witness in the background, now in sharp focus"

Rack focus is worth knowing precisely because it is **a move that is not a move** — it changes
what the shot is about without travelling, which makes it safe on the flat-parallel-surface
geometry Veo cannot dolly past (`video-prompting.md` §9).

⚠️ **Lens flare is officially supported and house-banned.** It is on Google's list, it works,
and `badcode-art-direction` forbids it. The GPOM orbital shots are a named exception recorded
in that story's ledger — don't generalise them.

## Rules

1. **Camera instruction goes first, as its own clause or sentence.** "The camera pulls
   back" standing alone beats the same words buried mid-description. Camera language
   appended after a long scene description gets ignored.
2. **One primary move per clip, two maximum.** Pan + tilt + orbit + zoom + handheld in
   one 8-second clip produces confusion.
3. **Describe start position, path, and end reveal.**
   > "Create a six-second smooth pan across a clean creator desk. Camera starts on a
   > notebook and coffee cup, pans right to reveal a laptop showing a video editing
   > timeline."
   > "Create a five-second slow push-in on a modern app dashboard displayed on a tablet.
   > Camera starts with the full tablet visible, then moves closer to the main analytics
   > card."
4. **Use plain speed adverbs, not seconds.** "slow", "gentle", "quick", "rapid",
   "smooth", "sharply". Second-level timing inside a movement clause ("dolly in over 0.5
   seconds") is unreliably parsed — the one source with comparative testing measured
   ~39% adherence and recommends adverbs instead. *This corrects a widely-repeated tip
   claiming exact durations improve specialty moves; they don't.*
5. **To lock the camera, say so positively:** "static shot", "fixed camera", "the camera
   is locked and still". Don't try to fight motion with negatives.
6. **Angle carries emotional register** and pairs with a shot size in one clause
   ("low-angle wide shot"): eye-level = natural, trustworthy; low = power, dominance;
   high = vulnerability; Dutch = unease; worm's-eye = mythic scale; bird's-eye =
   surveillance or flat-lay.

## Lens and focal length

18mm expansive · 24–35mm natural-wide · 50mm natural · 85mm portrait compression ·
100mm macro · telephoto isolation.

Put aperture in the same clause as the focal length: "50mm prime lens with a shallow
depth of field", "85mm lens at f/2.8", "low-angle shot with a shallow depth of field
(f/1.8)".

Fisheye recipe: "Wide-angle / fisheye lens (10mm–14mm) – Strong foreground distortion on
hands + faces – Bright, saturated colors – High contrast, punchy sunlight."

> **Compact working combo:** "Medium shot, 35mm, slow dolly-in, subject centered, shallow
> DOF; background city bokeh; handheld micro-sway for intimacy."

## Lighting

Named photographic setups transfer directly: golden hour, blue hour, chiaroscuro,
Rembrandt, high-key, low-key, three-point softbox, hard fluorescent, rim light.

**"Motivated lighting"** — light visibly coming from an in-scene source (streetlamp,
window, monitor) — reliably grounds a scene, and is the term to reach for when a shot
looks artificially lit. *(This is also the BadCode house rule: name the actual light
source in the prompt rather than letting the model invent photogenic lighting.)*

**State source, direction and colour temperature explicitly, and repeat the same
phrasing across every clip in a sequence.** That repetition is the primary defence
against colour creep down a shot chain.

> **Official:** "The scene is lit by the harsh fluorescent overhead lights and the green
> glow of the monochrome monitor."
> "Film noir cinematography with dramatic chiaroscuro lighting, deep shadows, venetian
> blind light patterns, and high contrast black and white aesthetic."
> "golden hour rim light on a dancer in a warehouse with backlight creating a halo and
> dust particles in light beams"

## Film stock, grain, grade

Composable into one dense trailing clause. Terms that land: "shot on 35mm film",
"anamorphic lens", "fine film grain", "halation", "gate weave", named stocks ("Kodak
Portra 400"), "teal-and-orange", "desaturated", "sepia", "muted teal tones".

> "Shot on 35mm anamorphic with shallow depth of field, oval bokeh from background
> lights, fine film grain, and subtle halation around the brightest highlights. Calm,
> intimate, slow-cinema mood."
> "Teal-and-orange cinema grade: warm orange skin tones against deep teal-blue shadows,
> high but smooth contrast, rolled-off highlights, anamorphic 35mm, subtle blue lens
> flare, fine grain."

⚠️ Teal-and-orange is the *opposite* of the BadCode comic register, which calls for
muted cool-neutral and bans movie-poster grading. Quoted here as vocabulary, not as a
recommendation.

## Camera hardware as a style token — low confidence

Naming hardware ("GoPro", "Fujifilm", "cheap disposable camera", "shot on iPhone,
handheld", "Arri Alexa Mini") is widely recommended as shorthand for an optical
signature. It is **documented by Google for the image side** — the Nano Banana guide
explicitly lists GoPro / Fujifilm / disposable camera as style levers — and is **absent
from Google's Veo guide**, which teaches descriptive technique language instead.
Verification found no controlled test isolating the effect on video.

**Use it for stills. On video, describe the signature itself** ("fisheye distortion,
blown highlights, on-camera flash, handheld urgency") rather than trusting a brand name
to carry it.

## Simplicity is the technique

Single-subject, single-move shots outperform crowded ones. Complexity yields weirdness.
When a shot isn't landing, the fix that works most often is **removing** a camera-movement
or lighting clause, not adding one.

---

## Sources

Read at source on **2026-08-18**. Every term in "The official catalogue" is quoted from the
first of these; the reliability tiers, the rules and the BadCode notes are ours.

- [Video generation prompt guide — Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) — camera angles, camera movements, lens and optical effects, lighting, tone, artistic style, ambiance, temporal elements, cinematic terms.
- [Generate videos with Veo 3.1 — Gemini API](https://ai.google.dev/gemini-api/docs/veo) — the shorter component list ("Camera positioning and motion", "Composition", "Focus and lens effects", "Ambiance") and its worked examples.
- [Image generation with Gemini — Gemini API](https://ai.google.dev/gemini-api/docs/image-generation) — the still-side camera guidance ("Control the camera: use photographic and cinematic language") and the camera-hardware style levers noted below.

The **camera-hardware-as-style-token** section stands as written: it is documented for the
image side and absent from every Veo page re-read in this pass.
