You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

" #2 Same Bench: the 1919 fat cat tells a veteran "Forget it", then says it to a nurse on the same bench today. He hasn't aged a day." lets do this, using the art style, but lets change it slightly so it doesnt get copywrighted. THanks

please show me stills of this in the new scene skill and the dialogue skill thing thanks.

## What happened in earlier rounds (facts)

Round r1 (2026-11-12): nine separate writers, one prompt each. The sameness gate still failed after two rewrites, so nothing ran and no stills were made.
Phrases it flagged as shared between prompts included: "no words letters numbers signature or speech", "on the bench's left end lounges", "end of the bench sits a", "a tall portrait drawing in black", "signature anywhere in the image thanks".
Jack, asked whether to run r1 anyway or start fresh: "Fresh round".

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

The war is over my boy
Rollin Kirby
Kirby

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

## Your experiment

Write ONE prompt for this experiment, and only this one:

**c-banknote-engraving-portrait** — Beat C, the reference frame. A frontal, chest-up portrait of the rich man alone, rendered like a steel engraving on old currency: fine parallel and curved hatching lines building every fold of jowl, waistcoat and hat, set inside a plain oval vignette on cream paper, no ornament words or numerals. He looks straight out with a small satisfied smile, one hand at his watch chain. Even, flat studio light so every feature reads clearly for reuse as the character reference. Large blank paper above and below the oval for the caption.

Other writers are doing the other experiments (a-frost-park-from-above, a-crayon-dismissing-hand, a-behind-the-bench-noon, b-flat-colour-hospital-night, b-two-eras-two-pens, b-over-the-nurse-shoulder, c-split-century-bench, c-alone-at-sunset-wide). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): for a caption
- shares wording with other prompts in this round: Flow prompts: a caption to be added later
- shares wording with other prompts in this round: Flow prompts: for a caption to be added

Your previous draft:
```json
{
  "name": "c-banknote-engraving-portrait",
  "prompt": "A tall cream sheet of heavy rag paper, and floating in its middle a plain oval frame holding an invented man rendered as an old intaglio currency portrait, printed in a single deep green-black ink. He is a stout, well-fed financier of about sixty, seen square-on from the chest up: a polished silk stovepipe hat, heavy jowls folding over a stiff winged collar, a clipped moustache, small contented eyes looking directly at the viewer and the corners of his mouth lifted in a quiet, pleased smile. His plump right hand rests against his belly, two fingers hooked through a gold fob chain that loops across a buttoned brocade waistcoat under a dark frock coat. Everything is built from burin cuts: the cheeks and brow modelled by fine curved lines that wrap around the forms, crossing into dense cross-hatching in the shadows under the hat brim and chin and breaking into tiny flicks and dots where the light falls on the nose and forehead; the hat's sheen made of long tight parallel strokes; the coat in deep ruled crosshatch. Inside the oval the background is a soft field of even horizontal lines that fades out at the edge, with no border ornament, no rosettes, no lettering, no digits, no seal anywhere. Light is flat and even from the front so every feature of his face reads clearly, like a reference sheet. Generous empty paper above and below the oval, untouched, for a caption to be added later. Slight ink plate tone and the faint emboss of the press on the paper. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/c-banknote-engraving-portrait.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/c-banknote-engraving-portrait.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-banknote-engraving-portrait". Reply with just the two paths.