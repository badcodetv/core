# Brief: The Starting Gate, clips round 1 (image to video)

You write motion prompts for Google Flow video (Omni, "Frames" mode: the still is the first frame), 9:16, 8-second clips.
Read ONLY this brief, `geometry.md` and the stills it names (`still-<SHOT>.jpg`). Research the web freely for how real
racing footage moves (the stalls opening at the off, a head-on gallop, a winners' enclosure, a horse trotting in rain).

## The story's facts first
A 17-second comedy short: a horse race where new money is the starting gun. SHARES and HOUSES fly out of the stalls; WAGES
stays shut in its stall for years, chewing hay; HOUSES wins and is celebrated; much later WAGES trots out alone; the next
race starts everyone from one line. A masked commentator calls it from the box; his voice is added later.

## The look: one line
Real-looking footage of an English racecourse on a grey, wet day.

## Rules for every prompt
- One paragraph, your own words, under ~120 words. Describe the motion and the camera from the first frame on; keep every
  horse, silk, cloth word and the setting exactly as in the still.
- **Nobody speaks.** Say what the sound is (rain, hooves, the stalls' clang, a crowd) and that there is no talking.
- The masked man (BOX): his mask, gloves and clothes stay exactly as in the still; no skin appears; he moves only his
  arms and head (binoculars, a small lean forward).
- Describe only what should happen; never name what to leave out.
- End every prompt with "Thanks."

## The shots (two genuinely different prompts each, ids <SHOT>-a and <SHOT>-b)
1. **GATE**: the three in the stalls; a beat of stillness, then the front gates spring open together.
2. **BOX**: the commentator follows the race through his binoculars, leaning in as it starts.
3. **BREAK**: SHARES and HOUSES gallop out towards the camera; behind them WAGES stays in its shut stall.
4. **STALL**: WAGES chews hay behind its shut gate, unbothered; time passes (the light shifts).
5. **WINNERS**: HOUSES celebrated in the winners' enclosure, champagne spraying.
6. **TROT**: WAGES finally trots alone along the flooded, empty course.
7. **ONEGATE**: the line of horses at the start; the gates open and every horse goes at once, level.

## Output
Write a JSON array of {"id","still","motion"} (still = GATE, BOX, BREAK, STALL, WINNERS, TROT or ONEGATE) to the file your
task names. Reply with one line per prompt.
