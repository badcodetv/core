You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

keep experimenting with stills and stlyes, i want the rich fat cat to look ominous almost like a horror silent hill style Please clean room it all and research the internet to achieve it. Thanks.  thanks

## What happened in earlier rounds (facts)

Mood board round 1 (2026-11-12) showed nine takes on a 1910s pen-and-ink editorial cartoon look: a frosty park from above, a grease-crayon close-up of his dismissing hand, from behind the bench at noon, a flat-colour poster outside a hospital at night, him as an old cut-out in a rainy modern bus stop, over the nurse's shoulder, a banknote engraving portrait, a torn page 1919/today, him alone at sunset. Jack left no votes or notes on it.
Jack's next message, verbatim, is ask.md.

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

The war is over my boy
Rollin Kirby
Kirby
Silent Hill
Pyramid Head
Konami

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 14 seconds, three beats. Mood board round 1: spread the round across all three beats (three stills per beat), each a genuinely different take on the look.

The art style: a 1910s pen-and-ink newspaper editorial cartoon (the inspiration is a 1919 Life magazine cartoon of a top-hatted fat cat on a park bench telling a one-legged soldier "The war is over my boy. Forget it."). Jack: use that art style, but change it so it is not a copy. Our own characters, poses, bench, park and composition; never recreate that panel.

Beat A (1919, the veteran): a park bench; a fat, top-hatted rich man sits beside a wounded soldier just back from the war (one leg, crutch). The rich man waves him off: "Forget it."
Beat B (today, the nurse): the same bench, the same rich man, identical and unaged, top hat and all; beside him now a tired nurse in scrubs. He waves her off the same way: "Forget it."
Beat C (the button): he hasn't aged a day. The same man, every time.

The rich man must look exactly the same in A, B and C (he becomes the reference for every later frame). Portrait 9:16. Leave room for a caption. No text or lettering drawn in the image.

Round 2 direction (Jack, 2026-11-12): the rich fat cat must look OMINOUS, almost horror: the dread of a foggy, rusting, nightmare-town survival-horror game. Take that feeling and translate it into this short; do not recreate any specific game's monsters, characters, places or imagery. The comedy of the short stays, the cartoon roots can stay or be pushed, but he should frighten.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**c-rust-dust-wasteland** — Beat C, the button. An extreme wide of a park that is gone: a dust-choked, ochre-and-rust wasteland at a brown noon, rusted railings bent over, a dead tree, a lamp post collapsed into ash, painted in a dense dystopian surrealist manner with a palette held to three or four related tones. Dead centre and small, the bench is intact, and on it the fat top-hatted man sits immaculate, clean and unaged, the one light accent in the frame, waving off nobody, because nobody is left. The dust sky above holds the caption.

Other writers are doing the other experiments (a-fog-swallowed-park, a-gaslamp-silent-film-still, a-his-shadow-arrives-first, b-blurred-behind-the-nurse, b-crosshatched-grin-closeup, b-low-poly-short-draw-distance, c-black-painting-on-plaster, c-the-only-still-thing). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts: the top third of the frame

Your previous draft:
```json
{
  "name": "c-rust-dust-wasteland",
  "prompt": "Portrait-format oil painting in a meticulous, technically exact dystopian surrealist manner: a vast, deep view looking down from high and far away over the remains of a public park, now a desert of drifted rust-coloured powder under a dull brown noon. Bent iron fencing curls over like dead fern fronds and sinks into the dunes; a lone stripped tree, charred and forked, claws at the haze; a fallen cast-iron lamp standard has turned to grey cinder along half its length and is crumbling where it lies. Everything far off melts into airborne grit, layered in fading veils of atmospheric perspective. The sun is a pale bruise behind the murk and the light is flat, heavy and shadowless. Colour is strictly limited to four neighbouring earth tones, yellow ochre, burnt sienna, raw umber and iron-oxide red, with a crusted, granular paint surface and dirty, unevenly overlapping hatch marks that read as grime built up over years. Precisely in the middle of the canvas, very small, sits an unbroken wooden park bench, and on it a stout, heavy-jowled gentleman wearing a tall silk stovepipe hat, an immaculate frock coat, a clean white collar and pale kid gloves, his skin rosy and smooth, untouched by the dust, the single bright, cool note in the entire painting. Knees crossed, he flicks the fingers of his right hand outward in a bored brush-off towards the vacant seat and the dead land, wearing a thin, contented smile, though there is not a living soul for miles to receive it. The top third of the frame is an empty, even field of dun-coloured sky left clear for a caption. The image holds no lettering, words, signs or numerals of any kind. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/c-rust-dust-wasteland.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/c-rust-dust-wasteland.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-rust-dust-wasteland". Reply with just the two paths.