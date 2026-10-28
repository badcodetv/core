---
slug: forties-newsreel
name: 1940s British newsreel
kind: look
family: Archive and period media textures
checked: 2026-10-28, references and engine notes (see Web check)
---

# 1940s British newsreel

> Black-and-white 35mm cinema newsreel: scratched, high-contrast, shot on a few fixed lenses, with an implied booming voice-of-authority.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

The cinema newsreels (Pathe, Movietone, Gaumont British) were a weekly ritual in British cinemas from the 1910s to the 1960s, and their wartime form fixed the look most people picture: 35mm black-and-white in the 1.37:1 Academy frame, shot on a handful of prime lenses, with intertitle cards and map graphics, and cut to a confident, plummy commentary. The look carries institutional certainty: someone in charge is telling you how things are. It is also the visual language of propaganda, which is exactly why it suits a narrator who speaks with total authority about events the audience thinks they have not lived yet.

## Signature traits

- Monochrome 35mm, 1.37:1 frame with rounded-corner gate weave and slight vignette
- Hard directional daylight or flat overcast, crushed blacks, blown-out skies
- Scratches, dust specks, frame-edge flicker and occasional reel-change cue marks
- Static or slow-pan tripod shots; hand-held only for action; wide establishing shot then medium then close detail
- Intertitle cards with serif or engraved lettering and map graphics with arrows and animated lines
- Crowds seen from a raised position (balcony, truck roof), officials framed from slightly below
- Film running slightly fast (16-18 fps cranked) for comic crowd walking

## References

- *British Pathe newsreel archive (online library of the full run)* — British Pathe, 1910-1970. The primary source for the look; every texture and framing convention is visible in the originals.
- *Listen to Britain* — Humphrey Jennings and Stewart McAllister (Crown Film Unit), 1942. Wartime documentary showing the same monochrome 35mm look used for lyrical rather than purely official purposes.
- *Citizen Kane (News on the March sequence)* — Orson Welles, 1941. The best-known fake newsreel: shows how to age and degrade a clean image convincingly and how the form delivers exposition.
- *Zelig* — Woody Allen, 1983. Shows period footage fabricated and inserted into real archive, the central technique if a story wants to fake an archive.
- *The Atomic Cafe* — Kevin Rafferty, Jayne Loader and Pierce Rafferty, 1982. A compilation film that uses official footage against its own message, the closest existing model for satire done with archive voice.

## What it carries

Official, confident, quaint and faintly sinister. It can carry pomp, deadpan irony and sudden gravity; it fights against anything that needs intimacy, or a character the audience should feel for in close-up.

## What it suits, and what it would undermine

Satire of institutions and the people who run them: a Minister explaining the unaffordable, bulletins from a future government, wealth presented as national achievement. Superb for a narrator with certainty because the form is certainty. It would undermine stories about ordinary private feeling, or a present-day working-class setting where the audience needs to see itself in the picture and not in a museum.

## Asking Flow (Nano Banana stills, Veo clips) for it

Describe the medium physically: 'black and white 35mm cinema newsreel, 1.37:1 Academy ratio, 1940s, hard daylight, heavy film grain, dust and scratches, slight gate weave, tripod-mounted, slow pan'. Specify period costume, vehicles and signage, otherwise modern details creep in. For video, ask for a locked-off or slow-pan camera with 'cranked slightly fast' motion, since Veo defaults to smooth modern camera moves. Exclude: colour, lens flare, shallow depth of field, modern clothing, smartphones, digital sharpness, widescreen, text overlays. Render the intertitle cards and map graphics as separate stills or in the edit rather than asking the video model for legible text.

## How generators get it wrong

The usual failure is a clean modern image with a grey filter, grain and a sepia tint: no gate weave, no flicker, perfect resolution. The fix is to degrade after generation (grain, flicker, scratches, 4:3 crop in the edit) and to write 'low-resolution archive scan' and period-correct lenses into the prompt. Faces come out too glossy and modern-looking; ask for 'no makeup, period hairstyles, sweaty'. Period detail drift (wrong cars, signage with modern fonts, text gibberish) is common. Narration audio from Veo comes out with a modern accent, so voice and music are better made separately.

## Production cost

Low for a consistent texture, because it hides imperfections and softness; the grading is applied at the edit stage. Hard parts: keeping period detail consistent across shots (uniforms, vehicles, signage) and avoiding crowds that morph. Character consistency is easier than in colour because identity cues are lower fidelity. Legible text must be added in the edit.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Veo's API has a negativePrompt parameter, but no dedicated negative-prompt field was confirmed in the Flow UI. Google's Veo guidance says to list unwanted elements descriptively rather than with 'no' or 'don't'.

Sources:
- <https://labs.google/fx/de/tools/flow/faq>
