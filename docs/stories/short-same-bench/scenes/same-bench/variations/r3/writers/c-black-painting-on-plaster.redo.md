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

**c-black-painting-on-plaster** — Beat C, the button. Oil smeared onto a cracked plaster wall, the palette held to ochre, brown, grey and black, with a single white in his shirt front. The rich man, the same fat top-hatted figure, is pushed hard to one side of the frame and crouches forward on the bench in the dark, enormous, grinning, his hand raised in that same lazy wave-off. The rest of the frame is heavy empty darkness where the bench fades out, so it reads as if he alone has outlived the painting. The empty upper area takes the caption.

Other writers are doing the other experiments (a-fog-swallowed-park, a-gaslamp-silent-film-still, a-his-shadow-arrives-first, b-blurred-behind-the-nurse, b-crosshatched-grin-closeup, b-low-poly-short-draw-distance, c-the-only-still-thing, c-rust-dust-wasteland). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): anywhere in the
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): man in a
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): rich man in
- shares wording with other prompts in this round: Flow prompts: a black frock coat and a
- shares wording with other prompts in this round: Flow prompts: black frock coat and a tall
- shares wording with other prompts in this round: Flow prompts: in a black frock coat and
- shares wording with other prompts in this round: Flow prompts: man in a black frock coat

Your previous draft:
```json
{
  "name": "c-black-painting-on-plaster",
  "prompt": "A tall vertical mural painted in thick oil straight onto an old crumbling plaster wall, the surface split by hairline cracks, flaking at the edges, with bare patches of chalky ground showing through the paint. Squeezed against the right-hand edge of the frame, a huge, heavy-bellied rich man in a black frock coat and a tall battered top hat hunches forward on the end of a wooden park bench, so large he seems to be leaning out of the wall at us. His face is a swollen, moon-pale mask of mud-brown and grey, eyes two dark sockets with a wet glint, and a wide grin full of uneven teeth stretches far too far across it. One fat gloved hand hangs lifted beside his cheek in a slow, bored flick of dismissal, fingers drooping. The paint is laid on fast and rough with a wide brush and a knife, dragged and scraped, drips running down from his coat. The only clean white in the whole picture is the starched front of his shirt, glowing under his chin. To his left the bench dissolves into the dark after a couple of slats, and the rest of the wall is a vast, heavy, brushy blackness of umber and soot with faint grey scumbles where something was once painted over and lost. The upper half of the frame is near-empty smoky dark, quiet enough to carry a line of caption. Eye-level view, flat and close, like standing in a dim room in front of the wall; dull low light from one side catching the ridges of paint. Palette held to yellow ochre, raw umber, ash grey and black, plus that one white. No text, no lettering, no signature anywhere in the image. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/c-black-painting-on-plaster.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r3/writers/c-black-painting-on-plaster.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-black-painting-on-plaster". Reply with just the two paths.