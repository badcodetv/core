# Brief: stills round 1 (portraits, then the story shots)

You write image prompts for Google Flow's image model (Nano Banana 2.1), 9:16 portrait. Each prompt is an EDIT that
receives the reference images listed for it; the prompt says what is in the new picture and points at each reference
by role ("the studio layout from the photo", "the presenter from his portrait"). Research first (how a TV weather
forecast set looks and is lit, the big weather map screen beside the presenter), then write.

Write `prompts-r1.json` in this folder: a list of `{"id", "prompt", "refs": [file names]}`, two DIFFERENT takes per id
(`<ID>-a`, `<ID>-b`; vary framing or moment, never the people or the place). Never more than 3 refs per prompt.

## The short
A comedy played straight, real-looking, ~20 seconds. A TV weather forecast where the weather is the economy. The
presenter stands beside a big screen showing a map of Great Britain with cartoon clouds and arrows. The camera pulls back
past the edge of the set: just out of shot, a man in a suit crouches with a plain desk fan, blowing the clouds across
the map. Studio lighting: bright, even, a little glossy on the set; darker and messier off-set (cables, stands, flight
cases).

## The place (Unsplash photos, used as layout only; make a new picture of the same kind of place)
- `Krkr1WhLV-4.jpg`: a news studio floor with a curved set and a studio camera. The weather set.
- `Av7fp7AqJr0.jpg`: a studio with light stands, softboxes and a desk. Off-set, where the man with the fan crouches.
- `fnjxpnaivnE.jpg`: looking past a camera operator's shoulder at the lit set. The pull-back.
The channel is invented: no real broadcaster's logo, colours, graphics or name anywhere. Readable words: ONLY these, in
plain block letters on the map's clouds: "RENT", "PRICES", "WAGES", and in the name-tag shot the tags "THE TREASURY",
"BANK RATE", "LANDLORDS' LOBBY", "ENERGY FIRMS". No other text, logo or brand anywhere.

## The people (one big portrait each first: head and shoulders, the face large and sharp)
- **PRESENTER (PR):** BadCode in a balaclava. A navy knitted balaclava with a white ring round the face and a red
  triangle over his left eye; no holes, no skin. Every prompt with him lists `mask-reference.jpg` and contains this
  sentence exactly: "The balaclava exactly as in the attached image: no holes, no skin, gloves." He wears a smart navy
  suit, a pale blue shirt buttoned to the collar with a plain tie, the shirt collar up against the mask so no neck shows,
  black gloves, a small presenter's clicker in one hand. He faces the camera; if his head turns, the triangle stays over
  his own LEFT eye. Say what he wears; never name a person, channel or show.
- **THE MAN WITH THE FAN (F):** an invented white man of about 55, slicked-back grey hair, a ruddy face, a navy
  pinstripe suit, a red-and-gold striped tie, cufflinks, polished shoes; crouched, holding a plain white desk fan.
  Ordinary, unknown face: no resemblance to any real politician or famous person. Never name him.

## The ids (two takes each)
Portraits first (ref: `Krkr1WhLV-4.jpg` for the background, plus the mask for PR): `PR`, `F`.

Story shots (refs: the layout photo named + the portraits in the shot, written as `portrait-PR.jpg`, `portrait-F.jpg`):
- `MAP` (`Krkr1WhLV-4.jpg`, PR): the presenter beside the big screen, gesturing at the map of Great Britain; a grey
  cloud labelled PRICES over the south, a blue cloud labelled WAGES over the north, a dark cloud labelled RENT drifting
  over London; cartoon arrows.
- `PULLBACK` (`fnjxpnaivnE.jpg`, PR, F): the wider view past the camera: the lit set with the presenter and the map
  on the left; on the right, just outside the lit set in the shadows, the man crouched with the desk fan pointed at the
  screen, the cable trailing.
- `FAN` (`Av7fp7AqJr0.jpg`, F): the man with the fan close, crouched off-set, blowing, caught: he looks up at the
  camera, guilty, and keeps the fan going.
- `TAGS` (`Krkr1WhLV-4.jpg`, PR): the map again, now every cloud carries a white name tag on a string: THE TREASURY,
  BANK RATE, LANDLORDS' LOBBY, ENERGY FIRMS; the presenter points at them.
- `TURN` (`Av7fp7AqJr0.jpg`, PR, F): the presenter, gloved, has taken the fan and turned it on the man in the suit; his
  slicked hair blown up, tie flying over his shoulder.

## Rules for every prompt
- Plain description of who, where, doing what, the light. No camera brand or film stock words.
- Faces from their portraits, named by role; big enough to read. No famous faces: if one could be a known person, change it.
- 9:16 vertical.
