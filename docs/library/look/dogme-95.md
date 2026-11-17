---
slug: dogme-95
name: Dogme 95
kind: look
family: Film movements and national cinemas
checked: 2026-10-28, references and engine notes (see Web check)
---

# Dogme 95

> Ugly-on-purpose handheld digital video: no lights, no props, no score, raw performance.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

A 1995 manifesto by Lars von Trier and Thomas Vinterberg (the 'Vow of Chastity') requiring location shooting, handheld camera, natural light, only sound recorded on set, and no special effects or genre trappings. The first films, Festen and The Idiots (both 1998), found a raw, shaky, exposed digital-video look that made drama feel like documentary. Its rules were part sincere, part provocation, and it was broken in practice as often as kept. It remains the reference for deliberately unpolished, performance-first film.

## Signature traits

- Handheld camera that moves with the actors and sometimes misses them; shakiness is visible
- Natural or existing light only, windows and lamps, mixed colour temperatures with blown highlights
- Early digital video: low resolution feel, noise in shadows, flat contrast, slightly smeared motion
- Colour film only, no filters, no optical effects; grading looks accidental
- Close, intrusive framing; faces filling the frame in dinner or party scenes; awkward cuts and focus hunts
- Sound as recorded: room tone, clinks and overlapping talk; no score
- Real locations and household props; no set dressing
- Long takes of difficult scenes: confrontation, toast, family argument

## References

- *Festen (The Celebration)* — Thomas Vinterberg, 1998. A birthday speech exposes a family's secret; the canonical Dogme dinner-table confrontation.
- *The Idiots (Idioterne)* — Lars von Trier, 1998. Handheld provocation about a group pretending disability; shows the aggressive end of the style.
- *Mifune's Last Song (Mifunes sidste sang)* — Søren Kragh-Jacobsen, 1999. A gentler Dogme film about a man returning to a farm; proves the style can carry warmth.
- *Julien Donkey-Boy* — Harmony Korine, 1999. American Dogme entry in lo-fi video, a rough and fragmentary take on the rules.

## What it carries

Exposure, discomfort, immediacy, truthfulness and public embarrassment. It makes speeches, confessions and arguments feel dangerous. It fights against beauty, stylisation, long fantasy and anything that needs polish; the audience may associate the look with low production values.

## What it suits, and what it would undermine

Confrontation stories: a dinner, a shareholder meeting, a doorstep, a cornered boss making a statement, a whistleblower. It can make a satirical monologue feel like a live hostage video. It suits the 'inside the room' beats of a story. It would undermine epic, historical or futuristic spectacle, and a deliberately ugly look can read as cheap if the audience does not know the movement, so use it where roughness reads as honesty.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana: 'frame from a 1998 standard-definition digital video drama, handheld, available light only, mixed fluorescent and window light, slightly overexposed highlights, noisy shadows, flat colour, close framing, family dinner table, no film grain, 4:3'. Ask explicitly for early-DV look, interlacing softness and imperfect focus. For Veo: 'handheld camera hunts for the speaker, abrupt reframing, focus drifts, shaky, documentary, available light'. Exclude: 'cinematic, color grade, shallow depth of field bokeh, dramatic lighting, lens flare, 35mm film grain, smooth gimbal, symmetrical composition, soundtrack'. Put sound as a separate step: room tone and dialogue only.

## How generators get it wrong

Both models are trained toward clean, sharp, well-exposed images, so 'lo-fi video' tends to come out as a tidy image with a noise overlay or a retro filter. Specify low resolution, blown highlights, wrong white balance and imperfect framing. Veo has a strong tendency to smooth camera motion, so true handheld shake and focus hunting are weak; it often produces gentle floaty wobble instead. Close-up faces in crowded dinner scenes risk duplicated or melted background guests. Crowd talk and overlapping dialogue cannot be generated reliably in one clip. Performance may look too polished and 'acted'.

## Production cost

Appears cheap but is awkward: the look relies on imperfection that models fight against. Shot-to-shot character consistency in tight faces is demanding. Savings come from no set dressing, no lighting plan and tolerance for flaws; you can add shake, noise and downscale in post (ffmpeg or Premiere) to push a clean clip into the look, which is often more reliable than prompting.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Nano Banana supports 4:3. Flow has no separate exclude field; write exclusions into the main prompt. Veo's handheld shake is weakly controllable; guides say to name the camera movement explicitly.

Sources:
- <https://ltx.studio/blog/veo-prompt-guide>
