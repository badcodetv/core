# Brief: stills round 1 (portraits, then the story shots)

You write image prompts for Google Flow's image model (Nano Banana 2.1), 9:16 portrait. Each prompt is an EDIT that
receives the reference images listed for it; the prompt says what is in the new picture and points at each reference
by role ("the hall layout from the photo", "the cashier from his portrait"). Research first (British post office
counters and queues, server racks and data-centre hardware), then write.

Write `prompts-r1.json` in this folder: a list of `{"id", "prompt", "refs": [file names]}`, two DIFFERENT takes per id
(`<ID>-a`, `<ID>-b`; vary framing or moment, never the people or the place).

## The short
A comedy played straight, real-looking, about 18 seconds. A British post-office-style counter hall where every counter
window is labelled POWER. A slow, patient queue. A giant machine (a data centre on wheels) pushes in to the front; the
cashier sends it to the back; the people get their power. Ordinary weekday daylight through windows plus overhead
strip lights: real, a little drab, nothing glossy, nothing like an advert.

## The place (Unsplash photos, used as layout only; make a new picture of the same kind of place)
- `V50uAd5i-Ag.jpg`: a long hall with queue barriers (posts and belts) making lanes. The queue hall.
- `GbY1IcKPvS0.jpg`: barrier lanes leading up to service counters. The approach to the windows.
- `Y63M9ZI29JM.jpg`: an old wooden counter window with turned wooden balusters. The cashier's window.
Readable words: ONLY these, in plain block letters: "POWER" above each counter window; "3" on the now-serving display;
"POSITION CLOSED" on the cashier's sign; "DISCOUNT APPLIED" on the machine's small screen. No other text, brand, logo,
poster or label anywhere.

## The people (one big portrait each first: head and shoulders, the face large and sharp, the hall soft behind)
Name every person in every prompt by age, hair and clothes, each in clearly different clothes. No children anywhere.
- **CASHIER (C):** BadCode in a balaclava, behind the counter window. A navy knitted balaclava with a white ring round
  the face and a red triangle over his left eye; no holes, no skin; black gloves. Every prompt with him lists
  `mask-reference.jpg` and contains this sentence exactly: "The balaclava exactly as in the attached image: no holes,
  no skin, gloves." He wears a plain navy cardigan over a white shirt buttoned to the collar, and a blank plain name
  badge. Say what he wears; never name a person, film or character. If his head is turned, the triangle is still over
  his own LEFT eye.
- **WOMAN WITH THE KETTLE (K):** a woman of about 42, Black British, short natural hair, a mustard raincoat over a grey
  jumper, holding a white electric kettle by its handle, its cord coiled in her other hand.
- **PENSIONER (P):** a white woman of about 75, silver set curls, a lilac quilted coat, a portable electric heater
  (a small cream fan heater) under one arm, tote bag on the other.
- **THE LAD (L):** a white lad of about 19, ginger buzz cut, a grey hoodie, holding a phone and staring at its low
  battery, a charging cable in his other hand.
- **THE MACHINE (M):** a data centre on wheels the size of a small van: a tall black server cabinet bank with a
  perforated mesh front, rows of tiny blinking green and blue lights, cooling fans on the side, thick cables trailing,
  heavy castors; a small screen on its front. It is a machine, not a robot: no face, no arms.

## The ids (two takes each)
Portraits first (ref: `V50uAd5i-Ag.jpg` for the background, plus the mask for C): `C`, `K`, `P`, `L`, and `M` (the
machine on its own in the hall, three-quarter view).

Story shots (refs: the layout photo named + the portraits of everyone in the shot, written as `portrait-C.jpg`,
`portrait-K.jpg`, `portrait-P.jpg`, `portrait-L.jpg`, `portrait-M.jpg`):
- `QUEUE` (`V50uAd5i-Ag.jpg`, K, P, L): the queue in the barrier lanes, K at the front, P behind, L behind her; the
  counter windows labelled POWER in the distance; a now-serving display reading 3.
- `BARGE` (`GbY1IcKPvS0.jpg`, M, K, P, L): the machine rolling past the queue toward the windows; K, P and L turned to
  it, mouths open in a gasp.
- `CASHIER` (`Y63M9ZI29JM.jpg`, C): the cashier behind window three, looking the machine up and down; the top of the
  machine just in the foreground.
- `CLOSED` (`Y63M9ZI29JM.jpg`, C, M): the cashier sliding a POSITION CLOSED sign across the window in front of the
  machine, whose small screen reads DISCOUNT APPLIED.
- `KETTLE` (`Y63M9ZI29JM.jpg`, K, C): K at window three, plugging the kettle into a socket on the counter; steam
  rising; the cashier behind the glass.
- `PHONE` (`V50uAd5i-Ag.jpg`, L, M): at the back of the queue, the lad plugging his phone cable into a socket on the
  side of the machine.
- `SCREEN` (no portraits; ref `V50uAd5i-Ag.jpg` for the light only): a close-up of the lad's phone in his hand, the
  screen black except a single plain thin white ring in the centre (a charging ring, nothing else on the screen: no
  numbers, no icons, no text). The real logo is laid on in the edit, so the screen must stay plain.

## Rules for every prompt
- Plain description of who, where, doing what, the light. No camera brand or film stock words.
- Faces from their portraits, named by role; big enough to read. No famous faces: if one could be a known actor, change it.
- 9:16 vertical.
