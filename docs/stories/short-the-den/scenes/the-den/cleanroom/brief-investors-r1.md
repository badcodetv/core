# Brief: The Den, the investors, round 1 (common to every writer)

You write prompts for Google Flow's Nano Banana 2.1 (stills, 9:16 portrait). Each prompt goes to Flow WITH a reference
photo of the set attached (named per prompt below). Read ONLY the files named here. Research the web freely for how a
TV investors' pitch show lights and frames its panel (low-key studio light in a dark warehouse loft, practical lamps,
shallow depth of field) — describe it in your own words; never name any show.

## The shot's facts first
- Five investors sit in a row of mismatched vintage leather armchairs in a dark converted warehouse loft (brick walls,
  tall factory windows with cool daylight, wooden floorboards, warm practical lamps). Each has a small round side table
  with neat stacks of banknotes on it. They face the pitcher's mark, which is off camera.
- Each prompt is ONE investor's casting portrait: a medium shot, seated, three-quarter angle, in their armchair, the
  den softly out of focus behind. Same set and light in all five so they cut together.
- Set references (look at them; they are real photos): `/home/jackt/.cache/badcode-refs/the-den/set-chairs.jpg` (the
  chairs, attached to Flow), `show-chairs-row.jpg` (how the row sits in the room), `set-window.jpg`, `set-cog.jpg`,
  `set-cash.jpg` (the cash on the side tables). Same folder.

## The five investors (all invented people; describe exactly these, add nothing that makes them look like anyone famous)
1. **INV-A**: a woman in her early sixties, Black British, close-cropped natural grey hair, gold-rimmed half-moon glasses
   on a chain, a burgundy tailored skirt suit, a heavy gold bangle. Arms folded, one eyebrow up, unimpressed.
2. **INV-B**: a man in his late forties, British Indian, neat short beard, slicked-back black hair greying at the temples,
   a navy three-piece suit with a pocket square. Leaning back, fingertips together, a polite, cold smile.
3. **INV-C**: a man of about seventy, white, bald with a fringe of white hair, ruddy cheeks, broad and heavy-set, a
   mustard cardigan over a checked shirt and a knitted tie, big hands on his knees. Leaning forward, squinting, blunt.
4. **INV-D**: a woman in her mid thirties, British Chinese, a sharp black bob with a straight fringe, a black ribbed
   polo-neck, thin silver rings, a slim tablet on her knee. Head tilted, already bored.
5. **BADCODE**: an investor in a balaclava, in a charcoal suit, white shirt and dark tie, black leather gloves, sitting
   very still, perfectly upright, hands resting on the chair arms. For this one Flow also gets the mask reference
   (`mask-reference.jpg`, same folder): include this sentence verbatim in the prompt:
   "The balaclava exactly as in the attached image: no holes, no skin, gloves." The balaclava cloth is dark charcoal
   wool; the large white ring round the whole face and the one red triangle inside the ring at its upper right
   (pointing down) are as in the image. No skin anywhere: gloves, cuffs over the wrists, the mask tucked into the collar.

## The look: one line
Real-looking photographs of a TV pitch show's set: a dark converted warehouse loft, brick, leather armchairs, warm lamps, cool window light.

## Rules for every prompt
- One paragraph, your own words, under ~170 words. 9:16 portrait.
- Describe only what should be in the picture; never name the thing to leave out.
- No readable text, no logos. No real person's name, and no show's name.
- No sign-off at the end.

## Output
Write `investors-r1.json` in this folder: a JSON array of {"id","ref","prompt"} with ids INV-A, INV-B, INV-C, INV-D,
BADCODE; "ref" = "set-chairs.jpg" (and "set-chairs.jpg+mask-reference.jpg" for BADCODE). Reply with one line each.
