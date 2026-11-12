You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

" #2 Same Bench: the 1919 fat cat tells a veteran "Forget it", then says it to a nurse on the same bench today. He hasn't aged a day." lets do this, using the art style, but lets change it slightly so it doesnt get copywrighted. THanks

please show me stills of this in the new scene skill and the dialogue skill thing thanks.

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

**b-crayon-closeup-hands** — Beat B, today. A tight medium close-up on the two of them from the waist up, in black grease crayon and ink wash, framed so the rich man's dismissive raised hand sits in the middle of the picture, sharp, while the nurse's face behind it is softer. She is mid-sentence, a hand on her chest, hospital ID badge on her scrubs; he does not even turn his head, chin up under the top hat. Strong side light from the left, deep crayon blacks on the right. Plain wall of hedge at the bottom for the caption.

Other writers are doing the other experiments (a-crosshatch-wide-autumn, a-grease-crayon-low-angle, a-two-colour-overhead, b-crosshatch-hospital-dusk, b-laid-paper-rain, c-split-diptych, c-portrait-straight-to-camera, c-red-spot-repeated-benches). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): a tall silk
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): anywhere in the
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): in the image
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): in the picture
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): silk top hat
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): tall silk top
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): the image thanks
- shares wording with other prompts in this round: Flow prompts: in a tall silk top hat
- shares wording with other prompts in this round: Flow prompts: the bottom fifth of the frame

Your previous draft:
```json
{
  "name": "b-crayon-closeup-hands",
  "prompt": "A hand-drawn editorial newspaper illustration in soft black grease crayon dragged across textured cream newsprint, with loose brushed washes of diluted black ink, the grainy broken strokes and multi-shade greys of an old lithographic press drawing. Tall portrait frame, a tight medium close-up of two people seated side by side on a slatted park bench, both cut off at the waist. In the near foreground and dead centre of the frame floats a plump rich man's gloved hand, raised palm-out and flicking away, drawn crisp and heavy with confident dark contour lines; it is the sharpest thing in the picture. Behind that hand, slightly further back and drawn softer and lighter, with smudged blurred crayon edges, is a weary nurse of today in wrinkled scrubs, a laminated hospital ID badge clipped at her chest, one hand pressed flat over her heart, her mouth open in the middle of a sentence, brow knotted, looking straight at him. On the right, the rich man himself: a portly figure in a tall silk top hat, wing collar and buttoned waistcoat over a round belly, chin lifted, eyes half shut, face turned forward and away from her, not even glancing her way. Hard raking light from the left catches the nurse's cheek and the back of his hand in bare untouched paper, while the right side of the picture sinks into dense, waxy crayon black that swallows his coat. Along the bottom fifth of the frame, a flat dark band of clipped hedge drawn in simple scribbled crayon texture, quiet and empty. Strictly black, grey and paper-cream only, no colour. No words, letters, captions, speech balloons or signature anywhere in the image. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/b-crayon-closeup-hands.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r1/writers/b-crayon-closeup-hands.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-crayon-closeup-hands". Reply with just the two paths.