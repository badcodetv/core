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

**c-alone-at-sunset-wide** — Beat C, the button. A long, low, almost ground-level view along the path to the bench at sunset, the rich man alone in the exact centre, both sides of the bench empty, long ink shadow stretched toward the viewer. Brush and ink wash in warm sepia and grey, the sky a graded wash with nothing in it, leaving the top half free for the caption. Pigeons peck at his polished shoes; he looks relaxed, patient, waiting for the next person to sit down. The focus is on him; the foreground path softens.

Other writers are doing the other experiments (a-frost-park-from-above, a-crayon-dismissing-hand, a-behind-the-bench-noon, b-flat-colour-hospital-night, b-two-eras-two-pens, b-over-the-nurse-shoulder, c-banknote-engraving-portrait, c-split-century-bench). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): a tall silk
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): for a caption
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): no lettering captions
- shares wording with other prompts in this round: Flow prompts: a tall silk hat frock coat
- shares wording with other prompts in this round: Flow prompts: clear for a caption added later
- shares wording with other prompts in this round: Flow prompts: gentleman in a tall silk hat
- shares wording with other prompts in this round: Flow prompts: in a tall silk hat frock
- shares wording with other prompts in this round: Flow prompts: kept clear for a caption added

Your previous draft:
```json
{
  "name": "c-alone-at-sunset-wide",
  "prompt": "Brush-and-India-ink wash drawing in the manner of a hand-made newspaper cartoon from about 1919, laid on with a loaded brush over rough textured paper, warm sepia and cool grey tones only, the paper grain showing through the lighter washes. The viewpoint is a few inches above a gravel park path, looking straight down its length toward a single wooden slatted bench set dead centre in the far middle distance, the path's edges converging on it. On the bench, perfectly centred, rests a stout wealthy gentleman in a tall silk hat, frock coat, waistcoat with watch chain and spats, one arm stretched along the backrest, legs crossed, a small contented smile, eyes half-lidded, patient as a spider, plainly waiting for somebody new to sit down. Both halves of the bench beside him are bare. The sun is setting low behind the viewer, so his shadow and the bench's shadow pour forward along the gravel in one long dark ink stroke that reaches almost to the bottom edge of the frame. Three or four pigeons peck around his glossy black shoes, drawn with quick confident strokes. The nearest stretch of path is loose, wet, soft-edged wash, slightly blurred, while the man and bench are drawn in crisp, decisive pen line with light crosshatching in the coat folds. The upper half of the tall portrait frame is open sky: one smooth graded wash, warm ochre-sepia near the horizon fading to pale grey at the top, completely empty of birds, clouds, branches or marks, kept clear for a caption added later. A few bare tree trunks and park railings stand faint and pale at the far horizon. Quiet, warm, faintly sinister, the light of a day ending with him still there. The picture holds pure image only, with no lettering, captions, labels or artist's initials drawn into it. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/c-alone-at-sunset-wide.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-same-bench/scenes/same-bench/variations/r2/writers/c-alone-at-sunset-wide.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "c-alone-at-sunset-wide". Reply with just the two paths.