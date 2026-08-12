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
