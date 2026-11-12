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

**c-split-century-bench** — Beat C, one vertical frame cut in two by a torn-paper seam across the middle. Top half: the bench in 1919, drawn in sepia pen and ink, empty except for the rich man at one end. Bottom half: the same bench today in the same pen, but with bin, phone-lit commuter passing, and LED lamp post, and the same man at the same end in the identical pose, hat tilted at the same angle. Both halves share one consistent afternoon side-light from the left so the match is exact. The joke is that nothing about him changed; caption sits on the torn seam.

Other writers are doing the other experiments (a-frost-park-from-above, a-crayon-dismissing-hand, a-behind-the-bench-noon, b-flat-colour-hospital-night, b-two-eras-two-pens, b-over-the-nurse-shoulder, c-banknote-engraving-portrait, c-alone-at-sunset-wide). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts: can be laid over it later
- shares wording with other prompts in this round: Flow prompts: so words can be laid over
- shares wording with other prompts in this round: Flow prompts: words can be laid over it

Your previous draft:
```json
{
  "name": "c-split-century-bench",
  "prompt": "Portrait page of hand-drawn newsprint illustration ripped clean through its waist, the two scraps butted together with a jagged feathered tear between them and a thin band of blank buff card peeking through the rip, left bare so words can be laid over it later. Upper scrap, 1919: a slatted park bench on curly cast-iron legs, drawn with a dip pen in faded umber ink on toothy oatmeal-coloured paper, a cinder path, railings, a gas lantern on a fluted post and a leafless elm, a delivery boy on a bicycle tiny in the far distance. The bench is otherwise vacant; on its far right end lounges a round-bellied plutocrat, clean-shaven with heavy jowls and a small waxed moustache, a gleaming stovepipe topper cocked low over one eyebrow, a double-breasted frock coat straining at the buttons, a gold watch chain across the waistcoat, grey spats, one gloved hand resting on a silver-knobbed cane planted between his knees, the other thumb hooked in his waistcoat pocket, eyelids half shut in smug contentment. Lower scrap, present day: the very same bench seen from the very same spot, rendered with the same nib in crisp inky black on cleaner paper, flanked now by a dented litter bin, a slender modern lamp standard with a flat LED head, block paving, and a hurried commuter in a hooded parka striding past, face glowing from the phone in his hand. At that bench's far right end sits the plutocrat once more, a perfect duplicate down to every crease: jowls, moustache, topper cocked at the same tilt, straining coat, watch chain, spats, cane, hooked thumb, drowsy smug eyes. Level frontal view from seated height, the bench the same width in both scraps so its legs line up across the rip like a before-and-after. A single warm sun low on the left rakes both eras identically, pushing long hatched shadows out to the right, tone built from layered cross-hatching and stippled dots, wiry confident contours, lots of untouched paper, the draughtsmanship of a 1910s satirical weekly. Pictures only: keep every surface free of writing, numerals, signs, signatures and speech balloons. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/c-split-century-bench.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/c-split-century-bench.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-split-century-bench". Reply with just the two paths.