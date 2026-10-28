---
slug: italian-neorealism
name: Italian neorealism
kind: look
family: Film movements and national cinemas
checked: 2026-10-28, references and engine notes (see Web check)
---

# Italian neorealism

> Ordinary people in real streets in flat daylight, shot like a witness not a stylist.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Postwar Italian cinema (c.1945-1952) that left the ruined studios for bombed streets, using non-professional actors and stories about unemployment, housing and hunger. Rossellini, De Sica and Visconti made it; screenwriter Zavattini pushed the idea that a film should follow an ordinary person through ordinary hours. Light is natural, sets are real, endings refuse neat resolution. Its moral claim is that a working man's small loss is a large event.

## Signature traits

- Natural overcast or hard midday sun, no obvious lighting rig, soft grey-white skies
- Black-and-white 35mm with visible grain and mid-grey tonality rather than deep studio contrast
- Real locations: tenement stairwells, pawnshops, bomb-damaged streets, tram stops, with passers-by in background
- Eye-level, medium and wide shots at roughly 1.37:1, camera follows the walking figure rather than posing them
- Unglamorous faces, worn clothes, real dirt on hands and shoes
- Long takes of a person waiting, searching or walking; very few close-up flourishes
- Small object carries the plot (a bicycle, a pair of shoes), shown plainly
- Open or deflating ending, no heroic music cue

## References

- *Bicycle Thieves (Ladri di biciclette)* — Vittorio De Sica, 1948. A man needs his bike to keep a job that bike-posting depends on; pure economic stakes in one object.
- *Rome, Open City* — Roberto Rossellini, 1945. Shot in the rubble with scavenged film stock; the template for urgency and rough texture.
- *La Terra Trema* — Luchino Visconti, 1948. Sicilian fishermen cast as themselves against the wholesale middlemen; an explicit argument about exploitation.
- *Umberto D.* — Vittorio De Sica, 1952. A pensioner priced out of his room; the quietest and most devastating treatment of a fixed income.

## What it carries

Compassion, dignity, quiet dread, the sting of small humiliations. It carries sadness and anger well. It fights against irony, speed, spectacle and punchlines: it is a poor engine for jokes unless the joke is deadpan and cruel.

## What it suits, and what it would undermine

Stories about a single worker, a family or a benefits office where the point is that the system's damage lands on someone ordinary: rent, zero-hours, a failed claim, a sacked man. It makes a satire's victim feel real, so a joke at the powerful lands harder in contrast. It would undermine fast absurdist sketches, future-tech spectacle, or anything where the narrator's omniscient swagger needs a big visual.

## Asking Flow (Nano Banana stills, Veo clips) for it

Nano Banana responds well to concrete photographic descriptions: 'black and white 35mm photograph, overcast flat daylight, 1948 Rome street, non-actor working man in worn jacket, eye-level medium shot, visible film grain, no dramatic lighting'. Name the location, time of day and specific wear on clothes and objects. Ask for a 4:3 or 1.37:1 frame, and if the model returns 16:9 crop or pillarbox in post. For Veo, describe a slow lateral follow or a locked-off long take with people moving through the background, and say 'handheld, unhurried'. Put 'monochrome' in the prompt and in negative or exclude terms 'colour, saturated, cinematic teal and orange, glossy, studio lighting, lens flare, beauty retouching, dramatic rim light'. Avoid naming a living director. Prefer a real street's materials (cobbles, laundry, tram wires) to a general 'Italian city'.

## How generators get it wrong

Generators default to 'cinematic' beauty: dramatic rim light, film-noir contrast, and handsome models, which kills the plainness. Fix by naming flat overcast light and ordinary faces, and by stating what is NOT lit. Faces tend to be too symmetrical and clean; ask for specific age, weight and wear. Veo adds smooth heroic camera moves and slow motion; state 'no slow motion, no push-in, stable observational framing'. Backgrounds can become generically picturesque Mediterranean postcards; specify bomb damage, laundry, queues. Grain is sometimes painted on as a filter over a digital-clean image; ask for tonal softness and lens limits, not just 'grain'. Monochrome may drift into sepia.

## Production cost

Cheap to look at and cheap to keep consistent because plain light and real settings reduce things to re-roll, and a monochrome palette hides colour drift between shots. Character consistency of an ordinary face is still the hard part: ordinary faces have fewer distinguishing features to lock, so use a reference image and a distinctive garment. Long takes are limited by 8-second Veo clips, so cut on movement and let sound carry across.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Nano Banana image generation supports fixed aspect ratios including 4:3 but not 1.37:1; Veo outputs only 16:9 or 9:16, so crop or pillarbox in post. Flow has no separate negative-prompt field; the 'exclude' terms must be written into the main prompt as positive description (e.g. 'flat overcast light, ordinary faces'), though the Veo API does have a negativePrompt parameter. Secondary guides report that listing unwanted elements works better than 'no/don't' phrasing; this is unverified against Google's own page.

Sources:
- <https://ulazai.com/veo3-prompt-guide/>
