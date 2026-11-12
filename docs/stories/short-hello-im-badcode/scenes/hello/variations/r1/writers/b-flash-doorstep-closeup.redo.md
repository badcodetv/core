You are writing Google Flow prompts (Nano Banana stills or Veo/Omni clips). Research the internet first (search and read pages) and base your work on what you find. Do not read files in this repository: everything you are meant to know is in this brief.

## The request, word for word

"Hello, I'm BadCode: "I'm from the future. It didn't go well."" lets mess around with this. THanks

Answers to the questions: who is BadCode on screen = "Mix of both" (open on the future that went wrong, then cut to the balaclava figure for the punchline); angle = "Deadpan intro" (polite and calm, the understatement is the joke); shape and look = "9:16, explore looks".

## This story's standing rules (the round is finding a new style, so only these bind)

## Never
- AI likeness of a real person.

## Never write these

robot
cyborg

## Settings the story fixes for this part

Use exactly these values for these keys (choose the others yourself):

```json
{
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

## What the picture shows

A BadCode Short, about 9 seconds, three beats. Mood board round 1: spread the round across the beats (about four stills for A, four for B, one or two for C), each a genuinely different look. BadCode presents itself as a superintelligence from a future where humanity careered into disaster (greed, runaway inequality, politics that could not keep up with AI); it has come back to warn us. Dark humour, total authority, deadpan.

Beat A (the future, voice over "Hello. I'm from the future."): the future that went wrong, glimpsed and never explained. Show the aftermath of a society that failed itself, not monsters or robots attacking: what is left when greed won.
Beat B ("It didn't go well."): cut to BadCode itself: a figure in a balaclava looking straight into the camera, deadpan, calm, a little polite. The balaclava is a plain knitted ski mask; on it, around the LEFT eye hole (the wearer's left), a thin white ring, and a small red triangle with rounded corners pointing down, sitting inside the ring at about 2 o'clock. No skin visible, gloved hands, no robot parts. Where they are and how they are shot is yours to choose.
Beat C ("Watch this space."): the button; the BadCode logo is added afterwards in the edit, so leave a calm, uncluttered frame.

Portrait 9:16. No text, signs or lettering drawn in the image.

## Your experiment

Write ONE prompt for this experiment, and only this one:

**b-flash-doorstep-closeup** — Beat B. A tight close-up at night, lit only by a harsh direct camera flash, saturated and slightly overexposed in the centre: the masked face fills most of the vertical frame, dark knitted balaclava with every fibre visible, a thin white ring around the wearer's left eye hole and a small rounded red triangle inside it at about 2 o'clock, pointing down, the white and red catching the flash. Background falls to near black, with only the edge of a front-door frame and a doorbell light visible. Eyes level with the lens, unblinking, the stillness of a polite caller who knows exactly what happens next. One gloved hand raised in a small, courteous wave at the edge of frame.

Other writers are doing the other experiments (a-aerial-wall-between, a-flash-banquet-left-standing, a-painted-bored-suburb, a-kerbside-furniture-deadpan, b-grey-tableau-office, b-fireside-public-information, b-standing-in-the-drained-pool, c-blue-hour-empty-horizon). Make yours its own thing, in your own words: do not reuse the wording of the listening pass or of any earlier prompt.

Write the prompt as one paragraph of plain description: what is in the frame, the camera, the light, the palette. No film titles, no artist names.

Settings you choose for your prompt, guided by the story's look above (if it names a model or
aspect for this part, use that): "model" — the Flow model, e.g. "Nano Banana 2", "Nano Banana Pro" (stills) or
"Omni 1.2 Flash" (clips; our video model from 2026-11-09), "Veo 3.1 Lite"; "aspect" — "16:9", "9:16", "1:1", "4:3", "3:4", "4:5", "21:9" (stills; clips
are "16:9" or "9:16"). Unless the story fixes them (see above), the round's prompts must not all share one set of settings.

## Your previous draft failed an automatic check — rewrite it

Whenever prompts in a round share wording, the results come out the same. Problems:
- shares wording with other prompts in this round: Flow prompts (shared by most of the round): of the frame
- shares wording with other prompts in this round: Flow prompts: a small red triangle with softly
- shares wording with other prompts in this round: Flow prompts: about two o'clock sits a small
- shares wording with other prompts in this round: Flow prompts: and inside that ring at about
- shares wording with other prompts in this round: Flow prompts: at about two o'clock sits a
- shares wording with other prompts in this round: Flow prompts: inside that ring at about two
- shares wording with other prompts in this round: Flow prompts: o'clock sits a small red triangle
- shares wording with other prompts in this round: Flow prompts: red triangle with softly rounded corners
- shares wording with other prompts in this round: Flow prompts: ring at about two o'clock sits
- shares wording with other prompts in this round: Flow prompts: sits a small red triangle with
- shares wording with other prompts in this round: Flow prompts: small red triangle with softly rounded
- shares wording with other prompts in this round: Flow prompts: softly rounded corners point downward the
- shares wording with other prompts in this round: Flow prompts: that ring at about two o'clock
- shares wording with other prompts in this round: Flow prompts: the eyes inside the holes look
- shares wording with other prompts in this round: Flow prompts: triangle with softly rounded corners point
- shares wording with other prompts in this round: Flow prompts: two o'clock sits a small red
- shares wording with other prompts in this round: Flow prompts: with softly rounded corners point downward

Your previous draft:
```json
{
  "name": "b-flash-doorstep-closeup",
  "prompt": "Portrait-format night photograph, a tight close-up of a figure standing on a front doorstep, shot from a short wide lens held at eye height, almost too close, with a bare flash fired straight from the camera. The head and shoulders fill most of the tall frame. They wear a plain charcoal knitted ski mask, every loop of yarn and stray fibre pin-sharp under the flash, with a small hard shadow tucked behind the head. Around the eye hole on the wearer's own left side (the right side of the picture) a thin white ring is stitched into the knit, and inside that ring, at about two o'clock, sits a small red triangle with softly rounded corners, point downward; the white and red flare bright in the flash. The eyes inside the holes look dead level into the lens, unblinking, patient, like a courteous visitor who already knows how this conversation ends. At the bottom edge of the frame one black-gloved hand is lifted to shoulder height in a small, polite wave. The flash is hottest in the centre, the mask's front slightly blown out, colours punchy and saturated, then falls off fast into near-black at the edges: all that survives behind them is a sliver of painted door frame catching the light and the tiny glowing ring of a doorbell button. Crisp, snapshot-like, a touch of flash vignette, no motion blur, no lettering or numbers anywhere in the picture. Thanks.",
  "model": "Nano Banana 2",
  "aspect": "9:16"
}
```

Write a short note on what shaped it (with source URLs) to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/b-flash-doorstep-closeup.notes.md`,
and write ONLY a single JSON object to `/home/jackt/projects/badcode/badcode/docs/stories/short-hello-im-badcode/scenes/hello/variations/r1/writers/b-flash-doorstep-closeup.json`
with exactly these keys: name, prompt, model, aspect. "name" must be "b-flash-doorstep-closeup". Reply with just the two paths.