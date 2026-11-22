# Brief: The Starting Gate, stills round 1 (common to every shot)

You write prompts for Google Flow's Nano Banana 2 (stills), 9:16 portrait. Read ONLY the files named in your task:
this brief, `geometry.md`, and the reference photos it lists. Research the web freely for how the real thing looks
(British flat racing, starting stalls, saddlecloths, commentary boxes, winners' enclosures).

## The story's facts first
A 17-second comedy short. A horse race where new money is the starting gun: two horses, SHARES and HOUSES, fly out of
the stalls; the third, WAGES, stays shut in its stall for years, chewing hay, while a commentator calls the race. At the
end, the next race has one long gate for everyone. Where everything is: read `geometry.md`, and write those facts plainly
into every prompt.

## The look: one line
Real-looking photographs of an English racecourse on a grey, wet day (Jack: "use unsplash").

## Reference photos (real photos from Unsplash: layout and light only)
Where a shot names one, say in your output that it is attached as the layout; the prompt then says what is in the picture.

## Rules for every prompt
- One paragraph, your own words, under ~150 words. 9:16 portrait.
- Describe only what should be in the picture; never name the thing to leave out.
- No real person's, racecourse's, sponsor's or broadcaster's name; no logos. Readable text only where the shot says.
- The commentator (shot BOX only) is in a BadCode balaclava. Use this exact sentence for it, and the mask image will be
  attached: "The balaclava exactly as in the attached image: no holes, no skin, gloves." Say what he wears besides the
  mask (your choice: a racing commentator's clothes); never leave it unsaid.
- End every prompt with "Thanks."

## The shots (two genuinely different prompts each, ids <SHOT>-a and <SHOT>-b)
1. **GATE**: the three horses in the starting stalls just before the off, from the front, the saddlecloths SHARES,
   HOUSES, WAGES readable. Layout: `ref-gate.jpg` (horses side by side looking out of their boxes).
2. **BOX**: the masked commentator in the commentary box, binoculars raised, the course below through the glass. Mask
   image attached (`mask-reference.jpg`).
3. **BREAK**: SHARES and HOUSES bursting out towards the camera, turf flying; behind them one stall still shut.
   Layout: `ref-break.jpg` (two horses galloping head-on).
4. **STALL**: close on WAGES in its shut stall, head over the closed front gate, calmly chewing a mouthful of hay; the
   word WAGES on its cloth. Layout: `ref-stall.jpg` (a horse's head through stall bars, eating hay).
5. **WINNERS**: HOUSES in the winners' enclosure, rosette on the bridle, its well-dressed owners celebrating with
   champagne. Only the word HOUSES readable.
6. **TROT**: much later: the WAGES stall gate finally open, the horse trotting out alone onto an empty course in the rain,
   the stands empty. Only the word WAGES readable.
7. **ONEGATE**: the next race: one single long starting gate stretched across the whole width of the course, many horses
   standing level in one line behind it, seen wide from above. No words readable.

## Output
Write a JSON array of {"id","look","ref","prompt"} (ref = the attached file name or "") to the file your task names.
Reply with one line per prompt.
