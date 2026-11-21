# Brief: stills round 1 (portraits, then the story shots)

You write image prompts for Google Flow's image model (Nano Banana 2.1), 9:16 portrait. Each prompt is an EDIT that
receives the reference images listed for it; the prompt says what is in the new picture and points at each reference
by role. Research first (what an English car-boot sale in the rain looks like: gazebos, pasting tables, open car boots,
muddy grass; a cosy English terraced front room; a village auction in a marquee), then write.

Write `prompts-r1.json` in this folder: a list of `{"id", "prompt", "refs": [file names]}`, two DIFFERENT takes per id
(`<ID>-a`, `<ID>-b`; vary framing or moment, never the people or the place). Never more than 3 refs per prompt.

## The short
A comedy played straight, ~25 seconds, real-looking like documentary photographs. A rainy English car-boot sale where a
wheeler-dealer sells the country's institutions as framed pictures off his pasting table. A grotesque rich man arrives in
a long black car with his sweating clerk and buys the lot. The weary woman who walked past goes home; her phone says the
rich man won the election. In an auction marquee, a masked auctioneer tells the rich man the limit is now fifty pounds,
the same as everyone, and every hand in the tent goes up.

## Two kinds of reference
- **The original painted stills (`orig-*.jpg`) and character sheets (`sheet-*.jpg`)**: an earlier version of this story,
  painted. Use them ONLY for who the people are (build, hair, clothes, age, expression) and for the composition and
  moment. Never copy their painted look, colours or brushwork: every picture you describe is a real photograph.
- **Unsplash photos (`u-*.jpg`)**: real places, used as layout only; make a new photograph of the same kind of place,
  moved to England in grey drizzle.

## The people (one big portrait each first: head and shoulders, face large and sharp; invented faces, nobody real)
- **FIONA (FI)** (`sheet-Fiona.jpg`): an English woman of about 30, long untidy auburn hair, tired eyes, pale skin, an
  olive-green parka, a dark green scarf, a backpack strap; unimpressed.
- **JIM (JI)** (`sheet-Jim.jpg`): an English wheeler-dealer of about 55, round red-cheeked face, a grey flat cap, black
  jumper, dark worn jacket; a salesman's grin.
- **PHINEAS (PH)** (`sheet-Phineas.jpg`): an English man of about 65, very heavy, completely bald, jowly, small eyes, a
  three-piece navy pinstripe suit, red tie, gold signet ring, a black cane; smug.
- **LARRY (LA)** (`sheet-Larry.jpg`): his clerk, an English man of about 45, thin and stooped, big black-framed glasses,
  thinning hair, a crumpled grey suit, a lanyard, sweating in the rain, a clipboard.
- **BADCODE (BC), the auctioneer, no portrait:** a man in a balaclava. A navy knitted balaclava with a white ring round the
  face and a red triangle over his left eye; no holes, no skin. The prompt lists `mask-reference.jpg` and contains this
  sentence exactly: "The balaclava exactly as in the attached image: no holes, no skin, gloves." Tweed jacket over a navy
  roll-neck that runs up into the mask, black gloves, a gavel. If his head turns, the triangle stays over his own LEFT eye.

## Readable words: ONLY these
On Jim's framed pictures, small handwritten luggage tags: "NHS £40" (a framed photo of a hospital) and "THE COURTS –
SLIGHTLY USED" (a framed photo of a judge's gavel). Larry's clipboard: "PURCHASES". In the marquee a board: "£150,000";
paddle numbers "29"; later many paddles reading "£50". No other words, logos, brands or car badges anywhere. The car is
a long black luxury saloon with no badge and no bonnet ornament. No real party colours or logos.

## The ids (two takes each)
Portraits first (refs: the character sheet + one Unsplash layout for the background): `FI` (u-carboot), `JI` (u-stall),
`PH` (u-car), `LA` (u-car).

Story shots (refs: layout + the portraits in the shot, written `portrait-FI.jpg`, `portrait-JI.jpg`, `portrait-PH.jpg`,
`portrait-LA.jpg`; Phineas and Larry together use `cast-PHLA.jpg`, Phineas left, Larry right; the painted still named is
for the moment only and counts towards the 3):
- `CARBOOT` (`u-carboot.jpg`, `orig-1.jpg`, FI): Fiona trudging between stalls at a drizzly car-boot sale, hood half up.
- `HOSPITAL` (`u-stall.jpg`, `orig-5.jpg`, JI): Jim at his pasting table holding up a framed photo of a hospital with a
  tag "NHS £40", grinning at the camera (Fiona's point of view).
- `COURTS` (`u-stall.jpg`, `orig-7.jpg`, JI): Jim holding up a framed photo of a judge's gavel, tag "THE COURTS –
  SLIGHTLY USED", a shrug.
- `CAR` (`u-car.jpg`, `orig-9.jpg`): the long black badgeless saloon rolling slowly across the muddy field between the
  stalls, people turning to look.
- `ARRIVAL` (`u-car.jpg`, `orig-10.jpg`, cast-PHLA): Phineas stepping out of the car under a chauffeur's umbrella, Larry
  scurrying behind with the PURCHASES clipboard.
- `ALLOFIT` (`u-stall.jpg`, `orig-11.jpg`, cast-PHLA): close, Phineas's ringed hand on Larry's shoulder, Larry sweating,
  writing on the clipboard; Jim's table of framed pictures behind.
- `HOME` (`u-home.jpg`, `orig-12.jpg`, FI): Fiona on a worn sofa in a cosy small front room, rain on the window, a mug of
  tea, her phone lit in her hand (its screen not readable).
- `PADDLE` (`u-tent.jpg`, `orig-15.1.jpg`, LA): a village auction in a white marquee, rows of folding chairs, Larry
  holding up paddle "29", a board behind reading "£150,000".
- `LIMIT` (`u-tent.jpg`, `mask-reference.jpg`, cast-PHLA): the masked auctioneer (BadCode) at a small lectern, gavel
  raised, calmly shaking his head at Phineas and Larry in the front row; behind them, every ordinary person in the tent
  holding up a paddle reading "£50".

## Rules for every prompt
- Plain description of who, where, doing what, the light. No camera brand or film stock words.
- Faces from their portraits, named by role; big enough to read. No famous faces: if one could be a known person, change it.
- 9:16 vertical. English drizzle, grey daylight, wet grass, real colours.
