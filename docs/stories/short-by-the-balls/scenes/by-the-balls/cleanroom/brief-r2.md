# Brief: By the Balls, stills round 2

You write prompts for Google Flow, Nano Banana 2.1, 9:16, each an EDIT of an attached still (the still is the layout and
the "vibe" to keep; the prompt says what changes). Read ONLY this brief and look at the images it names (all in this
folder). Research freely: what UK amusement-arcade staff wear at work, and what claw machines look like inside.

## The director's notes on round 1, verbatim
- On BadCode's portrait (`CAST-BADCODE.jpg`): "no skin for the badcode guy, also give him an arcade worker look and make
  the mask match whatevrer material the arcade works wears thanks."
- On the couple at the machine (`r1-PLAY-a.jpg`, `r1-PLAY-b.jpg`, neither picked): "make it only houses in the grabby
  machine, with maybe money things as well thanks"
- On `r1-GRAB-a.jpg`: "something like this yeah thanks this vibe with the changes made so its consistant thanks"
- On `r1-LIMP-a.jpg`, `r1-BADCODE-a.jpg`, `r1-WIN-a.jpg`: "this vibe with the changes made so its consistant thanks"
- `r1-FACES-b.jpg`: picked, no note.
- On the dial (`r1-DIAL-a.jpg`, `r1-DIAL-b.jpg`, neither picked): "fix the amount of hands this vibe with the changes made
  so its consistant thanks"

## What that means, as facts
- Inside every claw machine in the film: only small model houses (many, in a few plain colours, white with red roofs
  among them) and money things (coins, rolled or bundled banknotes with no readable print). No soft toys anywhere.
  The house the claw goes for is a small white two-storey model house with a red roof, the same one in every shot.
- BadCode wears what a UK arcade worker wears, and his balaclava is made of that same material and colour. The mask keeps
  its design exactly as in `mask-reference.jpg`: a large white ring round the whole face, the red triangle on the right
  of the picture, no holes. No skin anywhere: high collar or zipped to the chin, gloves, cuffs over the wrists. Read
  `mask-wording.txt` and paste its text verbatim into every prompt that shows him.
- The dial shot: count the hands and make each one whole and plainly attached to an arm coming from the frame edge:
  the couple's two hands plus two other people's (four hands, four arms, no extra fingers or floating hands).
- No readable text, logos or brand names anywhere (round 1's `r1-WIN-a.jpg` had words printed on the machine's panel:
  leave that panel plain).
- The couple are `CAST-HER.jpg` and `CAST-HIM.jpg` (keep them exactly; never describe their looks, only what they do).

## What to write
1. `CAST-BADCODE-2`: a new head-and-shoulders portrait (attach `CAST-BADCODE.jpg` and `mask-reference.jpg`), the arcade
   worker look, face-on, a dark arcade behind.
2. One or two takes per shot, each an edit of the named still (attach it first, then the portraits of who is in it,
   max 3 images; use `CAST-BADCODE-2` for him; for him attach `mask-reference.jpg` if there is room):
   `PLAY` (from r1-PLAY-a and from r1-PLAY-b, one each), `GRAB` (r1-GRAB-a), `LIMP` (r1-LIMP-a), `FACES` (r1-FACES-b),
   `BADCODE` (r1-BADCODE-a, two takes), `DIAL` (from r1-DIAL-a and from r1-DIAL-b, one each), `WIN` (r1-WIN-a).
   Ids `<SHOT>-r2a`, `<SHOT>-r2b`.

## Rules
- One paragraph each, your own words, under ~120 words. Say what changes and what stays.
- Describe only what should be in the picture; never name the thing to leave out.

## Output
Write `prompts-r2.json` in this folder: {"portraits": [{"id", "prompt", "attach": []}], "stills": [{"id", "shot",
"prompt", "attach": []}]} (attach = file names in this folder, or `CAST-BADCODE-2`). Reply with one line.
