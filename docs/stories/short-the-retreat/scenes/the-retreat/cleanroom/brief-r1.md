# Brief: stills round 1 (portraits, then the story shots)

You write image prompts for Google Flow's image model (Nano Banana 2.1), 9:16 portrait. Each prompt is an EDIT that
receives the reference images listed for it; the prompt says what is in the new picture and points at each reference
by role ("the layout from the photo", "the guru from her portrait"). Research first (how luxury bamboo wellness resorts,
meditation pavilions and sound-bath gongs look and are lit), then write.

Write `prompts-r1.json` in this folder: a list of `{"id", "prompt", "refs": [file names]}`, two DIFFERENT takes per id
(`<ID>-a`, `<ID>-b`; vary framing or moment, never the people or the place). Never more than 3 refs per prompt.

## The short
A comedy played straight, real-looking, ~20 seconds. An expensive "detox from materialism" retreat in a bamboo resort,
full of people who are not detoxing from anything: the guru sells, the businessman trades during meditation, the gong
costs extra, the gift shop sells rocks. Then, behind the resort, the old groundskeeper on his break watches the wind in
the trees, and his dog runs up to him; he is the only calm person in the film. Glossy, golden, aspirational light for the
retreat (it should look like its own advert); plain, soft, natural light for the groundskeeper.

## The place (Unsplash photos, used as layout only; make a new picture of the same kind of place)
- `CKmLZ94isVM.jpg`: a golden sunset behind a tree. The opening shot (no text in the picture; words are added later).
- `oQPtUvNw2A4.jpg`: a small wooden sign among tropical plants. The resort's sign.
- `A5WFGW3h5RA.jpg`: an open bamboo pavilion with rows of floor cushions. The meditation circle.
- `i2_kSnhQNJU.jpg`: a large brass gong on a stand among plants. The gong.
- `2a-PH6dsAIw.jpg`: a shop wall crowded with souvenirs. The gift shop (make it a calm, minimal, expensive wellness shop instead).
- `fHWqP29e6Eo.jpg`: an old man sitting on a rock in long grass, petting a dog. The groundskeeper.
Readable words: ONLY these, in plain lettering: the sign "DETOX FROM MATERIALISM", "WEEKEND RETREAT", "£3,000"; in the
shop "EXIT THROUGH GIFT SHOP", price cards "£80" on the stones, and a mug reading "NON-ATTACHMENT £24". No other text,
logo or brand. No real religious symbol, deity, statue or scripture anywhere.

## The people (one big portrait each first: head and shoulders, the face large and sharp)
- **THE GURU (G):** an invented English woman of about 40, sun-bleached hair in a loose bun, flowing white linen,
  many beaded bracelets, a crystal pendant, bare feet; serene, slightly too perfect smile. A wellness influencer, not a
  monk or any real tradition. Never name her.
- **THE BRO (B):** her brother, an invented English man of about 38, expensive haircut, a navy quilted gilet over a
  white shirt, a big smartwatch, a tan; trying to look calm, plainly not. Never name him.
- **THE GROUNDSKEEPER (K):** an invented English man of about 70, weathered face, white stubble, a faded green work
  jacket, old trousers, muddy boots, a flask of tea; quietly content. An ordinary face. His dog: a scruffy brown-and-white
  terrier cross.
- **BADCODE (BC), card machine only:** a man in a balaclava. A navy knitted balaclava with a white ring round the face and
  a red triangle over his left eye; no holes, no skin. Every prompt with him lists `mask-reference.jpg` and contains
  this sentence exactly: "The balaclava exactly as in the attached image: no holes, no skin, gloves." He wears the
  resort's white linen staff shirt, its collar up against the mask, and holds out a card machine. If his head turns, the
  triangle stays over his own LEFT eye. No portrait: describe him in full each time.

## The ids (two takes each)
Portraits first (ref: `A5WFGW3h5RA.jpg` for the background; `fHWqP29e6Eo.jpg` for K): `G`, `B`, `K`.

Story shots (refs: the layout photo named + the portraits in the shot, written as `portrait-G.jpg`, `portrait-B.jpg`,
`portrait-K.jpg`; a shot with G and B together uses `cast-GB.jpg`, a sheet with G on the left and B on the right):
- `SUNSET` (`CKmLZ94isVM.jpg`): a golden tropical sunset over the bamboo resort's treetops, room at the top for a quote. No people.
- `SIGN` (`oQPtUvNw2A4.jpg`): the carved wooden sign at the resort gate among palms and bamboo: DETOX FROM MATERIALISM /
  WEEKEND RETREAT / £3,000.
- `CIRCLE` (`A5WFGW3h5RA.jpg`, cast-GB): the meditation circle in the bamboo pavilion, guests cross-legged, eyes shut;
  the guru at the front, palms open, mid-sentence; the bro among the guests, eyes shut, whispering into a phone hidden in
  his sleeve.
- `GONG` (`i2_kSnhQNJU.jpg`, G, mask): the guru has just struck the big gong; beside her BadCode in the staff shirt holds
  out a card machine towards the camera.
- `SHOP` (`2a-PH6dsAIw.jpg`): the resort's minimal gift shop: a sign EXIT THROUGH GIFT SHOP, ordinary river stones on
  little plinths with £80 price cards, a mug reading NON-ATTACHMENT £24. No people, or the bro paying at the till.
- `KEEPER` (`fHWqP29e6Eo.jpg`, K): behind the resort, the groundskeeper on his break, sitting on a rock with his flask,
  looking up at tall trees moving in the wind; soft late light; the resort's roofs small in the background.
- `DOG` (`fHWqP29e6Eo.jpg`, K): his scruffy terrier has run up; he pets it with one hand, still looking at the trees, a
  small easy smile.

## Rules for every prompt
- Plain description of who, where, doing what, the light. No camera brand or film stock words.
- Faces from their portraits, named by role; big enough to read. No famous faces: if one could be a known person, change it.
- 9:16 vertical.
