# Camping — music video v2: the storyboard ("Signs")

Ruled 2026-09-27 by Jack. Background, research and superseded ideas:
[`music-video-v2.md`](./music-video-v2.md). Story canon: [`story.md`](./story.md).

## 🔑 Signs are BLANK in Flow, and the text goes on in post (ruled 2026-09-27, Jack)

*"We will add text to the blank signs in post, like in Premiere Pro, after the video is made in Flow."*

**Every sign in the video is generated blank:** Bob's cardboard, the signs held up around the world, and
Tarquin's plaques, railing notices, gate and gantry. **The lyric words are typed on in Premiere by hand, after the
clip exists.** This removes three risks in one move: misspelt AI text, Flow's profanity filter on "FUCKIN", and
video's inability to hold lettering steady.

**What this asks of every sign shot, from design through prompt to video:**
- **The sign faces the lens squarely and flat.** Little perspective and no curl, so a flat text layer (or a Corner
  Pin) sits on it convincingly.
- **Hands grip the edges, never the face of the card.** Fingers across the middle would have to be masked round
  every frame.
- **The sign holds still in the clip.** Flow video is **Omni Flash with the camera locked**, and the person moves,
  breathes and looks, while the card stays put. Any push-in is done in Premiere on a **nest of clip + text**, so the
  words move with the picture.
- **The prompt describes the card as an object**, bare corrugated cardboard with its plain brown face toward us, and
  **never as an absence** ("no writing" risks coming back inverted: `nano-banana-2.md` §27). Keep the existing
  constraint that nothing in frame carries readable lettering.

**How it's done in Premiere (handwork, from our own notes):**
- 🔴 **The bridge cannot type the words.** Simple Text and MOGRT text parameters are unwritable from the API
  (`Illegal Parameter type`, measured 2026-08-22, [`effects-catalogue.md`](../../premiere/effects-catalogue.md)).
  **A human types each sign.** The bridge can still place, scale and rotate a text layer once it exists.
- **Fit the text to the card with Corner Pin** (`AE.ADBE Corner Pin`), placed by hand.
- **No planar tracking.** After Effects isn't installed and Mocha isn't owned, so a sign that moves means
  hand-keyframing. That's why the sign holds still.
- **Make it look written, not typed:**
  - one marker-style font for the cardboard and a formal serif or engraved face for Tarquin's signs
  - a slight rotation per word
  - Multiply blend so the card's grain shows through
  - a touch of the clip's own grain on top
- ⬜ **Fonts:** a free marker font with a commercial licence (e.g. *Permanent Marker* on Google Fonts, from memory,
  **licence not checked**).
- **The stat cards** are separate full-frame black cards, typed the same way (or with ffmpeg `drawtext`).


**Jack picked:** the cardboard signs (B), the caption stats, and the spikes (D), plus homeless people
meeting the public around the world, Jamaicans on beaches, Asian rainy night streets, and Bob and Tarquin
in England. The look is **photoreal**. **This supersedes the switch, soundclash and coin ideas above**, which
stay as a record.

### The through-line: two kinds of sign

| | Who | What it is | Job |
| --- | --- | --- | --- |
| **The ask** | Bob, and the people in every city | Torn cardboard, **generated blank**. One lyric line per sign, **typed on in post** in a marker font | Carries the lyric, so nobody's mouth moves |
| **The refusal** | Tarquin | His lyric lines set in **official property signage**: a brass plaque, enamel railings signs, a club board, a hotel gate, a motorway gantry, **all generated blank, with the words typed on in post** | Names the beneficiary: his words are the signs that keep people out |
| **The spikes** | Every city | Steel studs, bench dividers, boulders under flyovers | The refusal made physical. In the bridge they keep **Tarquin** out |
| **The stats** | Caption cards | Black card, white type, source and date | Typed in post: by hand in Premiere, or ffmpeg `drawtext` |

**Faces are allowed now.** A silent, closed-mouth stare into the lens while holding a sign is the device (as
in Dylan's "Subterranean Homesick Blues" cue cards, cited from memory and not researched). No mouth ever moves:
no lip sync, and no dialogue in Flow video.

### 🔴 Rules that came out of the research (2026-09-27)

- **No neon-drenched cyberpunk street.** It's the AI default. Liam Wong's *TO:KY:OO*, the source of the look, is
  itself Blade Runner-derived. Real streets are **fluorescent lightboxes going green on film**, with a few surviving
  neons (Greg Girard's Kowloon). Hong Kong issued 1,119 neon removal orders in one year.
- **Tokyo: no begging sign.** Begging is illegal (Minor Offenses Act, art. 22), and in Bangkok too. Tokyo is
  blue-tarp shelters on the Sumida and bench dividers only.
- **Hong Kong: Sham Shui Po.** Divided benches, boulders under the flyovers, the 24-hour fast-food window
  ("McRefugees": 334 a night in 2018, 57% of them working). ✅ **Checked 2026-09-28: begging is illegal in Hong
  Kong** (Summary Offences Ordinance s26A, up to HK$2,000 and one month's jail for a first offence; 79 arrests in the
  five years to November 2023, [LegCo reply, 2024-01-24](https://www.info.gov.hk/gia/general/202401/24/P2024012400324.htm)).
  So the Asia sign went to the fast-food window (s12). A sign with no cup and no ask is a statement, not alms. That
  reading is *our inference, not legal advice*.
- **Jamaica: the fence is the image.** Public beach access is being lost to hotels, the Beach Control Act dates
  from 1956, and JaBBEM is campaigning. Show **working and joy**: Negril vendors, Hellshire fish cookshops with
  the sea at the door, fishermen. Kingston: 2,442 street people in 2025 (PIOJ).
- **Sign text is NOT generated.** It was the plan (Nano Banana Pro can render short text, but handwriting is its
  least accurate style for spelling). **Superseded 2026-09-27: every sign is blank in Flow, and the words go on in
  post** (see the top of this file). Check each returned card for stray marks or pseudo-letters. It must be a clean
  surface.
- **The people abroad are invented, not real individuals.** Upright, working, meeting the public, and paired
  with the beneficiary, never in visible distress. Mitigations for the red line recorded above; Jack has ruled on photoreal.
- **Swearing is written in full** on the post-typed signs. Flow never sees the words, so its filter can't touch them.

### The shots (lyrics = `r81`, the words every reggae round since uses)

| # | Section | Sign text (typed on in post) | Shot | Job |
| --- | --- | --- | --- | --- |
| 1 | Intro | — · 🃏 *"318 million people have no home. — UN-Habitat, 2026"* | Macro: steel studs on a luxury block's window ledge, rain beading, a glass lobby lit behind | Plants the spikes and the scale |
| 2 | Intro | "ONCE AGAIN" being written | Bob's hands, a thick marker moving over a blank torn box flap on his knee. The letters appear behind the pen by a hand-keyframed wipe in Premiere; drop the shot if that reads fake | Reveals the device, hands only |
| 3 | V1 | **"ONCE AGAIN"** | Bob outside Waitrose, stares into the lens with the sign at his chest; a woman in red glances and turns her head away | The device plus *"looking to the side in shame"* |
| 4 | V1 | "HOW I'M JUST POOR" | Close: the sign and his paper cup with three coins, shoppers' legs passing | The ask, plainly |
| 5 | V1 | "YOU KEEP ON WALKING" | From behind Bob at seated height: Tarquin's back going through the sliding doors (mv2-2's geometry) | The refusal, walking |
| 6 | V1 | "PAID FOR YOUR WHEELS ON TICK" | The sign held up beside the X8's flank in the car park; Bob's reflection in the black paint | The car named |
| 7 | V1 | "FOUR TONNES OF STEEL" / "FOR A MEAL DEAL" | Wide: the X8 parked across two bays; Tarquin walks back carrying one meal deal | The joke lands on a picture |
| 8 | V1 | "I DO WANT CHANGE" | Bob's hand shakes the cup; the coins blur | The pun planted |
| 9 | V1 | "PLEASE SIR" / "CAN I FUCKIN HAVE SOME MORE?" | Bob holds the door for a shopper, the sign under his arm | Mock-polite |
| 10 | Hook 1 | **"I CAN'T LIVE LIKE THIS FOREVER"** | Kingston, King Street, day: an upright man in his fifties in a clean shirt holds the hook; shoppers pass, one woman stops to read it (no kids, Jack 2026-09-28) | The hook goes global, with dignity |
| 11 | Hook 1 | "I DO WANT CHANGE" (on the vendor's hand-painted cooler board) | Negril beach: a vendor walks the sand with a coconut cooler; behind him a hotel's fence and a guard | Working, not begging; the fence |
| 12 | Hook 1 | "I CAN'T LIVE LIKE THIS FOREVER" (pressed to the inside of the glass) | Sham Shui Po, rain, night: **moved to the 24-hour fast-food window** (begging is illegal in HK, checked 2026-09-28). A working man at the window counter at 3am holds the sign against the glass facing the street; umbrellas pass | Asia, without the cliché |
| 13 | Hook 1 | "I CAN'T LIVE LIKE THIS FOREVER" · 🃏 *"1 in 153 people in England are homeless tonight. — Shelter, Dec 2025"* | Back to Bob: the same hook, both hands | The rhyme closes the hook |
| 14 | V2 | "YOU ARE INTENT ON LIVING IN A TENT" (white enamel sign bolted to railings) | Tarquin's building: studs on the ledge, the enamel sign above them, Tarquin passing in | The refusal family introduced |
| 15 | V2 | "PROSPECTS EXIST" (engraved brass plaque) | Close: his hand touches the brass plaque by the door as he enters; the doorman holds it | His words on money's surfaces |
| 16 | V2 | "I WORK HARD" (the golf club's green-and-gold board) | The caddie shot (mv2-3): the old man carrying the bag in the foreground, the club board by the tee | The cost in frame |
| 17 | V2 | "MY POCKETS ARE EMPTY" (the hotel beach gate) | Jamaica resort: Tarquin on a lounger inside the fence; outside, the vendor from shot 11 passes a coconut through the bars | The beneficiary, paired |
| 18 | V2 | "THE ONLY THING I'M CHANGING IS THE LANE" (motorway gantry sign) | Night motorway, the X8 under an overhead gantry | The pun paid |
| 19 | V2 | "WEALTH GAP?" / "WHAT A LOAD OF CRAP" (the wine label) | Yacht deck, a bottle poured, the label turned to the lens | The sneer |
| 20 | Hook 2 | — | Tokyo, dawn: blue tarp shelters along the Sumida river wall; a bench with steel dividers, a rolled bedroll beneath | The refusal is global |
| 21 | Hook 2 | "I CAN'T LIVE LIKE THIS FOREVER" | Hong Kong: ⚠️ *re-staged with s12:* the window seat from shot 12 now empty at dawn, his sign left propped against the glass; the divided bench under the flyover can carry it instead | Moved on |
| 22 | Hook 2 | — | Hellshire: a woman frying fish in a cookshop with the sea at its door; fishermen haul a boat; ⚠️ *was "kids flip off the bow": no kids (Jack 2026-09-28), so re-stage with adults* | Joy, and the sea taking it |
| 23 | Hook 2 | "I MIGHT BE INSANE" | Bob again, looking straight into the lens | Home |
| 24 | Bridge | "HERE WE BOTH ARE" + "LIVING IN A CAR PARK" | The ruined car park, five years on: both men side by side facing the lens, one sign each | The jump, with no narration |
| 25 | Bridge | "THE AI DOES THE FAST PART" | Tarquin tries to sit on his own building's ledge; the studs stop him | Locked out by his own spikes |
| 26 | Bridge | "WE WERE ON THE SAME SIDE ALL ALONG" | Their two signs turned to face each other, over the drum fire | The turn |
| 27 | Final hook | "I CAN'T LIVE LIKE THIS FOREVER" ×5 · 🃏 *"Billionaire wealth rose $2.5tn in 2025 — about the wealth of the poorest 4.1 billion people. — Oxfam, Jan 2026"* | Beat-cut: Kingston man, Negril vendor, Hong Kong sign, Bob, Tarquin, each holding the hook | Everyone, same words |
| 28 | Outro | — | Every sign on the fire; the embers become bad code | The film's own ending |

### ▶ Resume here (updated 2026-09-28)

- **Stills, in progress.** Prompts for **s1–s19** are written below, each under its own `### sN` heading, with
  every round kept.
- **s19 is on round 3**, the steward on the yacht, with no reference attached. The result hasn't been seen yet.
- **Next up is s20** (Tokyo, the blue tarps on the Sumida), then s21–s28.
- **No result is logged for s1–s18.** Jack generated as he went, and only s7 (round 2), s10 (round 2, no kids),
  s12 (moved to the fast-food window) and s19 got feedback.
- **Standing rules for this film:**
  - one prompt per turn, no batches
  - every sign blank in Flow
  - Nano Banana Pro · 16:9 · x2 · 2K
  - no kids
  - no readable lettering except the X8's `BAD C0DE` plate and badge
- **Re-staging owed:** s21 (it follows s12's move to the window) and s22 (no kids).
- **After all 28 stills:** the video prompts (Omni Flash, camera locked), one per turn, each written against its
  accepted still.

**Order re-ruled 2026-09-28 (Jack): all 28 stills first, then the videos.** Still one prompt at a time, in shot
order, starting at shot 1. Each video prompt is written later against its own accepted still.

### s1 — the studs · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the film's first image. It plants the refusal as an object before any person appears, so the viewer
  asks "what are those for?" The cardboard answers it, and the stat card (318 million) lands on it in post.
- **Register:** documentary, human scale. Continuity with the mv2 stills: Portra 800, single handheld exposure.
- **Gate 2, visible cost:** a sodden, flattened cardboard bed pushed off the ledge onto the wet pavement below,
  plain brown and blank. It is the same material as every sign that follows, so it plants the device too.
- **Camera:** crouched at ledge height, which is the height of someone sitting (Bob's eye line), a hand's width
  above the ledge and tilted a few degrees down, looking along it on a diagonal. A close-up on a 90mm at f/5.6 with
  the near three studs sharp. Never "macro", which summons the dew-drop hero shot and front-to-back sharpness
  (`nano-banana-2.md`, thirteenth pass).
- **The object:** squat one-inch stainless studs bolted into stone, as at Southwark Bridge Road in 2014, never
  "spikes", which likely returns pigeon wire.
- **The drops:** uneven, each a tiny lens holding an upside-down warm window, not glass marbles.
- **Depth:** FG nearest studs large and sharp · MG the studs receding along the ledge, soft · BG the lobby through
  the glass, warm and out of focus, one concierge figure behind a desk.
- **Light:** the lobby's warm interior light through the glass is the one bright anchor, backlighting the drops on
  the studs. Everything else is dim blue-grey November dusk. Both ends of the exposure are named.
- **Rain (§32):** it only reads against something dark. The beads sit on the steel, backlit by the lobby. Rings
  and splashes land in the puddle, and no falling streaks are asked for against the bright glass.
- **Anti-advert (§ "advert vocabulary"):** grime between the studs, a rust bloom at the bolt heads, a crooked
  sealant line, a cigarette end, an uneven scatter of drops. No "luxury", "glossy" or "pristine".
- **Withheld:** any face. The lobby person is a soft shape.
- **For the later video:** camera locked; drops fall from the stud tips, rings in the puddle, the lobby figure
  moves. It is framed slightly wide so Premiere can push in.

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference (there is no face in the shot).

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure at dusk on a wet November evening in central London. Fine grain, muted colour, unposed and imperfect.

Camera and framing: A 90mm lens at f/5.6. The photographer crouches on the pavement with the lens a hand's width above a stone window ledge at sitting height, about thirty centimetres from its near end, tilted a few degrees down and looking along the ledge on a diagonal from the lower left of the frame toward the upper right. The frame is not quite level. The nearest three studs are sharp, and the rest soften as they recede along the ledge.

Subject: A strip of anti-homeless studs fixed along the ledge: squat stainless-steel cones about an inch tall with blunt tips, bolted in three staggered rows into the pale stone. The steel is dull, brushed and water-spotted. A line of grey sealant is squeezed out crookedly along the base of the strip, orange rust blooms around two of the bolt heads, and there is black grime and one flattened cigarette end in the gaps between them.

The rain: It has just rained and is still spitting. The water sits on the studs unevenly: a fat drop hanging from one tip, small drops clustered on the shaded sides, two drops merged into a run down one flank, and a few studs almost dry. Each drop is a tiny lens holding a small upside-down image of the warm window behind it, with one crisp point of highlight.

Background: Beyond the ledge, through a tall plate-glass window, the lobby of an apartment block, thrown out of focus into soft shapes: warm pools of light, a long pale desk, and the blurred figure of a concierge in a dark jacket standing behind it.

Foreground, below the ledge: Along the bottom edge of the frame, on the wet paving under the ledge, lies the corner of a sodden flattened cardboard box where it has been pushed off. It is plain brown card, darkened by the rain.

Light: The warm interior light of the lobby, coming through the glass from behind the studs, is the only strong light. It catches the drops and edges the tops of the cones. Outside, the dusk is dim and blue-grey, soft and without direction. The steel, stone and cardboard in front stay dark but keep their texture, and the brightest lamps in the lobby are allowed to burn out to white.

Details: Real surface texture, weathered stone, fine natural grain, ordinary and unstyled.

Constraints: The steel is dull and never mirror-bright. No signs, logos, labels or door lettering anywhere in the frame carry readable lettering.

Compose for a 16:9 frame, a little wider than the studs need.

Thanks.
```

### s2 — the pen on the card · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** it reveals the device. These signs are written by the man holding them, by hand, one line at a time.
  The viewer asks what he is about to write, and s3 answers it.
- **Unresolved question:** the felt tip is pressed to the top-left of the card where the first letter will start.
  The card is still bare, and the words arrive in post by a hand-keyframed wipe.
- **Camera:** his own eye line, looking straight down onto the card on his knees, so the card is flat and square to
  the lens for Corner Pin. It's a 35mm at f/4, the same lens as s3. Written as geometry, never "POV" or "over the
  shoulder" (twelfth pass).
- **Depth:** the card and hands are sharp · his knees and coat hem are at the frame edges · beyond his knees, soft,
  are the wet paving, the puddle and one passer-by's shoes crossing the top of the frame.
- **Light:** the same as s3. The overcast sky is flat and soft, and the shop's white interior light spills from one
  side.
- **Visible cost:** the hands. They are chapped and grimed, the fingerless gloves are unravelling, and they are cold.
- **No Character:** there's no face, so nothing binds (§12). The hands are an unbound body part, so they're described
  (§25), from `characters/bob.md`.
- **The card:** the same object as s3 (a torn flap, one corner mended with parcel tape), so the two cut together.
- ⚠️ **Continuity risk:** the coat sleeve is described in prose here and is carried by `@Bob` in s3. If the two
  disagree, match the sleeve to s3's accepted still.

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/4, held at the eye height of a man sitting on the pavement with his knees drawn up, pointing straight down at a piece of cardboard lying flat across his knees, so that the card faces the lens squarely and fills the middle of the frame. The frame is not quite level.

Action: His left hand holds the card still, fingers pressed flat along its left edge. His right hand grips a thick black marker pen with its cap off, the felt tip pressed onto the card at the top-left corner, where the first letter is about to begin. The card is still plain bare card from edge to edge.

The hands: A man's hands in his fifties, chapped red at the knuckles, with grime worked into the creases and short, broken nails. He wears grey wool fingerless gloves, unravelling at the cuffs, under the frayed sleeves of an old dark coat that is a size too big.

The card: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through.

Environment: At the edges of the frame, his knees in worn dark trousers, and the flattened cardboard he sits on. Beyond his knees, soft and out of focus, the wet paving outside a supermarket entrance, a shallow puddle, and a pair of women's ankle boots walking past across the top of the frame.

Light: Flat grey daylight from an overcast sky, soft and even, and the white light of the shop's interior spilling across the card from the right. The shadows are soft, and the darkest parts of the frame keep their detail.

Details: Real skin texture, the fibres of the torn cardboard edge, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard is plain bare card from edge to edge. No labels, logos or markings on the pen, the tape or anywhere else in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s3 — "ONCE AGAIN" · still · written 2026-09-27, re-checked and handed over 2026-09-28 (result not yet logged)

**Job:** prove the device and the look in one frame, and hand post a clean card to type on. Bob stares into the lens and the public looks away.
- **Unresolved question:** the woman's head is mid-turn.
- **Depth:** a passer-by's shoulder in the foreground, soft; Bob in the midground; the doors behind.
- **Light:** overcast sky plus the shop's spill.
- **Anti-slop:** a film stock and one named light; an off-centre frame, not quite level; a named foreground occluder;
  individuated passers-by (age, coat, action); no kill-list words.
- **The card:** blank, flat, square to the lens, held by its edges, and large in frame. The words `ONCE AGAIN` go on in Premiere. It is described as an object, bare brown corrugated cardboard, never as an absence.
- **Face:** muscle description only. No appearance words for `@Bob`.

Cast `@Bob`. Nano Banana Pro · 16:9 · x2 · 2K (a bigger card surface for post).

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon. Fine grain, muted colour, the green of the shop front and one red coat the only strong colours, unposed and imperfect.

Camera and framing: 35mm lens at f/4, standing on the pavement about three metres from the man from the character reference, slightly to his right, the lens level with his face as he sits. He sits a little left of centre, turned square to the camera, against the brick wall beside the supermarket's sliding glass doors. The frame is not quite level. Across the right edge of the frame, close to the lens and soft out of focus, passes the shoulder and swinging shopping bag of a passer-by.

Action: He sits on a flattened cardboard box with his knees drawn up, holding a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. He looks straight into the lens, calm and level: his lips are pressed together, his brows are relaxed, his eyes are steady and unblinking. Just behind him, a woman in her forties in a red wool coat, walking out of the shop with a carrier bag, has glanced down at the sign and is turning her head sharply away toward the car park, her eyes already aimed past him.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: The entrance of a British supermarket: sliding glass doors, a stack of green wire baskets just inside, a bay of wet steel trolleys, a shallow puddle on the paving, and a paper cup with a few coins in it beside his foot.

Light: Flat grey daylight from an overcast sky, soft and even, and the white light of the shop's interior spilling out through the doors onto his right side. The shadows are soft, and the darkest parts of the frame keep their detail.

Details: Real skin texture, damp paving drying in patches, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. No signs, logos, labels or shop fascia anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s4 — "HOW I'M JUST POOR" · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the ask, stated plainly. It's the first time the sign and the cup share a frame, the words and what
  they're asking for.
- **Camera:** pavement height, the level of the cup, about a metre in front, tilted slightly up so the card sits
  square to the lens. It's lower than s3, so the film steps down from his eye line to the ground. 35mm at f/5.6,
  so the cup and the card both hold.
- **Withheld:** the face. The top of the frame cuts at his collarbone, which is geometry and not a "face hidden"
  clause (§18).
- **Depth:** the cup and coins sharp in the lower left · the sign on his knees behind it · a passing shopper's
  legs and a trolley wheel at the right edge, blurred by movement.
- **Unresolved question:** a foot mid-stride right beside the cup, not stopping.
- **Coins:** exactly three, a small pile (models miscount, eighth pass). Two coppers and one silver.
- **No Character:** there's no face to bind. The hands and sleeves reuse s2's sentence word for word, so the two
  shots match.
- **Light:** the same as s2 and s3, overcast plus the shop's white spill from the right.

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at pavement level about a metre in front of a man sitting against a brick wall, tilted slightly upward. The top edge of the frame cuts across his collarbone. In the lower left of the frame, close to the lens and sharp, stands a paper coffee cup on the wet paving. Behind it, filling the middle of the frame, is the cardboard sign he holds upright on his knees, facing the lens squarely. The frame is not quite level.

Action: He holds the sign still with both hands, his fingers gripping only its outer edges. On the right edge of the frame a shopper walks past without slowing: a pair of legs in grey jogging bottoms and scuffed white trainers, one foot planted on the paving right beside the cup and the other lifting away, blurred by movement, followed by the front wheel of a shopping trolley. The man, the sign and the cup are still.

The hands: A man's hands in his fifties, chapped red at the knuckles, with grime worked into the creases and short, broken nails. He wears grey wool fingerless gloves, unravelling at the cuffs, under the frayed sleeves of an old dark coat that is a size too big.

The cup: a creased white paper coffee cup with its rim bent in on one side, and exactly three coins lying in the bottom of it, two small copper coins and one silver.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: The wet paving outside a supermarket entrance, a flattened cardboard box under him, the brick wall behind, and at the right a bay of wet steel trolleys, soft out of focus.

Light: Flat grey daylight from an overcast sky, soft and even, and the white light of the shop's interior spilling across the sign and the cup from the right. The shadows are soft, and the darkest parts of the frame keep their detail.

Details: Real skin texture, damp paving drying in patches, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. No labels, logos or markings on the cup, the trainers or anywhere else in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s5 — "YOU KEEP ON WALKING" · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the refusal, walking. The words on the sign are addressed to a back going through the doors.
- ⚠️ **Geometry changed from the table ("from behind Bob", mv2-2).** From behind, the sign faces away and post has no
  card to type on. The blank-sign ruling wins, so the camera is in front: Bob on the right holds the sign square to
  the lens, and the doors are further along the same wall on the left, with Tarquin's back going through them. It's
  the same axis as s3, so it differs in size and focus. Bob is larger and cropped at the right edge, and the eye is
  on Tarquin.
- **Unresolved question:** Bob's eyes follow the back. He's not looking at the lens this time, so the stare is
  spent in s3 and saved for later.
- **Two Characters:** each is anchored to a named side (§26), Bob on the right and Tarquin on the left. Tarquin binds
  by body and outfit from behind (§12, `9-walk`).
- **The doors:** wide open, not mid-slide (§38, an in-progress state returns fully open or shut anyway).
- **The stride:** heel lifting, foot planted (ninth pass).
- **Depth:** a trolley handle soft in the left foreground · Bob and the sign on the right · Tarquin and the doors at
  the wall.
- **Light:** continuous with s2–s4, overcast plus the shop's white spill. No readable fascia (the storyboard
  constraint, stricter than mv2-2).

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Bob` (slot 1), `@Tarquin-new` (slot 2).

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, the camera low, at the eye height of a man sitting on the pavement, about two and a half metres out from a brick shop wall and facing it straight on. On the right of the frame, large and close, sits the man from the first character reference, cut off by the right edge at his shoulder. On the left of the frame, further along the same wall, are the supermarket's glass doors. Across the bottom-left corner, close to the lens and soft out of focus, runs the curved grey handle of a shopping trolley. The frame is not quite level.

Action: The man on the right sits on a flattened cardboard box with his knees drawn up, holding a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. His head is turned toward the doors on the left of the frame, and his eyes follow the back of the man walking into the shop; his lips are pressed together and his jaw is set. On the left of the frame, the man from the second character reference walks away from us through the wide-open glass doors into the shop, his back to the camera, his rear heel lifting off the doormat and his front foot planted, his head facing straight ahead into the shop.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: The entrance of a British supermarket: the brick wall, the glass doors standing wide open, a stack of green wire baskets just inside, the bright aisles beyond, a shallow puddle on the paving and a paper cup beside the seated man's foot.

Light: Flat grey daylight from an overcast sky, soft and even, and the white light of the shop's interior pouring out through the open doors around the walking man. The shadows are soft, and the darkest parts of the frame keep their detail.

Details: Real skin texture, damp paving drying in patches, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the cardboard sign is plain bare card from edge to edge. No signs, logos, labels or shop fascia anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s6 — "PAID FOR YOUR WHEELS ON TICK" · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the car is named. The sign stands right beside the thing it's talking about, and for the first time Bob
  is on his feet.
- **Camera:** chest height at the X8's front corner, looking back along the flank on a diagonal. The nose (the
  kidney grille edge, the split headlight strip, the `BAD C0DE` plate) sits soft in the right foreground. That's
  the car's identifying angle (`wank-tank.md`), and it gives the foreground layer for free. Bob stands at the
  rear door, midground left, with the sign square to the lens.
- **Face:** Bob stares into the lens. It's the device from s3, used again now that he's standing.
- **Scale:** the car's roof is above his head, so his size against it is the class map.
- 🔴 **The reflection is NOT named.** The storyboard wants Bob reflected in the paint, but a named reflection came
  back as a double exposure over a face (§10). Black paint next to a man reflects him unasked. If it doesn't, the
  fix is to move the camera, never to add words.
- **Anti-advert:** the paint is spotless (canon) but the ground is not. There's a drain, faded bay lines and a
  trolley. No "glossy", "valeted" or "beading".
- **Lettering:** the plate reads `BAD C0DE` (ruled 2026-09-17) and the car's own badge is allowed. Nothing else is
  readable.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Bob`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon in a British supermarket car park. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/4, held at chest height beside the front corner of a blacked-out BMW X8 and looking back along its left flank on a diagonal. The front of the car fills the right edge of the frame, close to the lens and soft out of focus: the edge of its enormous vertical stacked double-kidney grille, a thin LED daytime-running strip set high on the front wing, and its front number plate reading "BAD C0DE", spelled B, A, D, space, C, zero, D, E. The long black slab flank runs away from the lens toward the left. The frame is not quite level.

Action: The man from the character reference stands on the tarmac beside the car's rear door, in the left half of the frame, the roof of the car higher than his head. He holds a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. He looks straight into the lens, calm and level: his lips are pressed together, his brows are relaxed, his eyes are steady.

The car: a very large black BMW SUV with a tall, flat, upright front end, a high beltline, a shallow band of dark privacy glass and huge dark wheels. Its paint is spotless and deep black, freckled with fresh raindrops.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: A wet supermarket car park: faded white bay lines, a drain grate by the rear wheel, a lone shopping trolley left against a kerb behind him, a row of ordinary small hatchbacks further back, and the grey brick side of the shop in the distance.

Light: Flat grey daylight from an overcast sky, soft and even, with no other light. The shadows are soft, and the darkest parts of the frame, the car's black paint included, keep their detail.

Details: Real skin texture, wet tarmac drying in patches, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. The number plate reading "BAD C0DE" and the car's own badge are the only readable lettering; every other sign, label and number plate carries no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s7 — "FOUR TONNES OF STEEL" / "FOR A MEAL DEAL" · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the joke lands on a picture. Four tonnes of car across two bays, and the reason for the trip is one
  sandwich in one hand.
- **One card, two lines:** because the words are typed on in post, the same card carries "FOUR TONNES OF STEEL" and
  then swaps to "FOR A MEAL DEAL" on the beat. One still serves both.
- **Camera:** a 28mm at f/8 (deep focus, tenth pass), chest height. Bob in the left foreground is cropped at the
  chin by the top edge, so his face is withheld by geometry (§18) and the eye goes to Tarquin. The sign is large and
  sharp for Corner Pin.
- **Depth:** Bob and the sign in the foreground on the left · the X8 in the midground right, front three-quarter to
  the lens, straddling the line between two bays · Tarquin walking toward it from the shop · the shop front at the
  back.
- **Scale:** ordinary hatchbacks in single bays either side, so the car's size is the joke, stated by comparison and
  not by adjective.
- **The meal deal:** named as three objects in one hand, because models miscount (eighth pass). The other hand holds
  the key fob.
- **Two Characters:** anchored left and right (§26). Tarquin is small, so he's held by silhouette and outfit (tenth
  pass).
- **Plate:** `BAD C0DE`, small, front three-quarter.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Bob` (slot 1), `@Tarquin-new` (slot 2).

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon in a British supermarket car park. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 28mm lens at f/8, held at chest height, everything from the near foreground to the shop front sharp. On the left of the frame, close to the lens, stands the man from the first character reference, facing the camera; the top edge of the frame cuts across his chin. In the middle distance on the right of the frame, a blacked-out BMW X8 is parked badly across two bays, its front three-quarter toward the lens. Beyond it is the shop. The frame is not quite level.

Action: The man on the left holds a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. On the right of the frame, about fifteen metres away, the man from the second character reference walks from the shop toward the car, his left foot planted and his right heel lifting, his head up, his eyes on the car. In one hand he carries a single meal deal: one sandwich in a triangular plastic pack, one small packet of crisps and one small bottle of water, held together against his fingers. In his other hand is a car key fob, held out toward the car.

The car: a very large black BMW SUV with an enormous vertical stacked double-kidney grille filling its tall, flat, upright front, thin LED daytime-running strips set high on the front wings, a long slab flank, a high beltline and huge dark wheels. Its front number plate reads "BAD C0DE", spelled B, A, D, space, C, zero, D, E. It straddles the white line between two bays, one pair of wheels in each.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: A wet supermarket car park: faded white bay lines, a small silver hatchback and a small red hatchback each parked neatly in a single bay either side of the black car and dwarfed by it, a trolley shelter, and the long low shop front with its glass doors in the background.

Light: Flat grey daylight from an overcast sky, soft and even, with no other light. The shadows are soft, and the darkest parts of the frame, the car's black paint included, keep their detail.

Details: Wet tarmac drying in patches, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the cardboard sign is plain bare card from edge to edge. The number plate reading "BAD C0DE" and the car's own badge are the only readable lettering; every other sign, label, packet and number plate carries no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

**Round 2 · 2026-09-28.** Jack: *"it does not look like Tarquin is approaching the car door, it looks like he is walking in front of it."*
- **Cause:** "walks from the shop toward the car" plus a car facing the lens put his path straight across the grille.
  The prompt never named the door.
- **One change:** the car shows its right-hand side with the driver's door toward us. He is stopped at the door, one
  step away, side-on, reaching for the handle, which is still shut (§38: a mid-action state returns fully open or
  shut, so design the stillness in). "Nobody in front of the grille" is scoped to a named thing.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon in a British supermarket car park. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 28mm lens at f/8, held at chest height, everything from the near foreground to the shop front sharp. On the left of the frame, close to the lens, stands the man from the first character reference, facing the camera; the top edge of the frame cuts across his chin. In the middle distance on the right of the frame, a blacked-out BMW X8 is parked badly across two bays, its front three-quarter toward the lens, so that we see its nose and its right-hand side, with the driver's door facing us. Beyond it is the shop. The frame is not quite level.

Action: The man on the left holds a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. On the right of the frame, about fifteen metres away, the man from the second character reference has walked down the right-hand side of the car and stands beside its driver's door, one step from it, his body turned toward the door and side-on to us, his eyes on the handle. His right hand reaches for the door handle with a car key fob in it, his fingers just short of touching it; the door is still shut. In his left hand he carries a single meal deal, held low by his thigh: one sandwich in a triangular plastic pack, one small packet of crisps and one small bottle of water, held together against his fingers. The front of the car, with its grille and number plate, is clear of him, with nobody standing in front of it.

The car: a very large black BMW SUV with an enormous vertical stacked double-kidney grille filling its tall, flat, upright front, thin LED daytime-running strips set high on the front wings, a long slab flank, a high beltline and huge dark wheels. Its front number plate reads "BAD C0DE", spelled B, A, D, space, C, zero, D, E. It straddles the white line between two bays, one pair of wheels in each.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: A wet supermarket car park: faded white bay lines, a small silver hatchback and a small red hatchback each parked neatly in a single bay either side of the black car and dwarfed by it, a trolley shelter, and the long low shop front with its glass doors in the background.

Light: Flat grey daylight from an overcast sky, soft and even, with no other light. The shadows are soft, and the darkest parts of the frame, the car's black paint included, keep their detail.

Details: Wet tarmac drying in patches, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the cardboard sign is plain bare card from edge to edge. The number plate reading "BAD C0DE" and the car's own badge are the only readable lettering; every other sign, label, packet and number plate carries no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s8 — "I DO WANT CHANGE" · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the pun is planted. The cup is shaken at us, the passer-by, so the ask is aimed at the viewer for the
  first time.
- **Camera:** standing eye height looking down on him. This is the passer-by's view and the first high angle of the
  film, after s2–s7 were all at or below his level. It's a 35mm at f/5.6, focused on the sign and his face.
- **Depth:** his hand and the cup, thrust toward the lens in the lower right, close and blurred by the shaking ·
  the sign tilted back on his knees, square to the high lens · his face above it, looking up · the wet paving.
- **Blurred or frozen?** Stated for each part (ninth pass): the cup, the coins and the hand blur, while the sign and
  the face are still and sharp.
- **Coins:** three, matching s4.
- **Face:** looking up into the lens, described by muscle only.
- **Not a repeat of s4:** s4 was the cup on the ground from the level of the coins, with his face withheld. This
  is from above, and it's the face and the gesture.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Bob`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at the eye height of a standing passer-by, a little over a metre away, looking down at the man from the character reference as he sits on the pavement against a brick wall. He sits a little left of centre. His outstretched arm comes toward the lens from the left, and his hand and the paper cup it holds are in the lower right of the frame, closest to the camera. The frame is not quite level.

Action: He sits on a flattened cardboard box with his knees drawn up. His left hand holds a large cardboard sign propped against his knees and tilted back, gripping only its outer edge, so that the card faces straight up into the lens and is held perfectly still. His right arm is stretched out toward the camera, shaking a creased white paper coffee cup, and the cup, the three coins inside it and his hand are blurred by the shaking. His face is tipped up toward the lens and he looks straight into it: his brows are lifted a little, his lips are pressed together, his eyes are steady. The sign and his face are sharp and still.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: The wet paving outside a supermarket entrance, the brick wall behind him, a shallow puddle beside his boots, and the edge of the shop's glass doors at the top of the frame.

Light: Flat grey daylight from an overcast sky, soft and even, and the white light of the shop's interior spilling across him from the right. The shadows are soft, and the darkest parts of the frame keep their detail.

Details: Real skin texture, damp paving drying in patches, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. No labels, logos or markings on the cup or anywhere else in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s9 — "PLEASE SIR" / "CAN I FUCKIN HAVE SOME MORE?" · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** mock-polite. He plays the doorman, and the "sir" walks through without a glance.
- **The doors are automatic,** so he ushers a man through doors that open themselves. That keeps continuity with
  s2–s8, and it's the joke: a man doing a job the machine already does, for nothing. (A mild automation echo, and
  the bridge pays it off.)
- **The sign under his arm:** clamped flat against his left side, face outward. Bob is side-on to the camera,
  turned toward the doors, so the card sits square to the lens. One card carries both lines (swapped in post, as
  in s7).
- **The "sir":** an uncast extra, described in full (a man in his sixties in a camel overcoat, a leather glove,
  eyes ahead). He's the comfortable class, not an ordinary shopper, per the-reader.md's rule on aiming the
  contempt.
- **Face:** a small courtly bow, head dipped, brows raised, a thin closed-mouth smile. Anatomy, not "sarcastic".
- **Depth:** the trolley bay rail soft in the left foreground · Bob · the doors and the man.
- **Light:** continuous. The doors are open, so the shop's white light pours out.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Bob`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a cold overcast afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at chest height about three metres to the left of the man from the character reference, so that we see him side-on as he stands beside a supermarket's sliding glass doors, which are on the right of the frame. He stands a little left of centre. Across the bottom-left corner, close to the lens and soft out of focus, runs the steel rail of a trolley bay. The frame is not quite level.

Action: He stands turned toward the doors, playing a doorman. His right arm sweeps out toward the open doors, palm up, ushering a customer in, and he dips his head in a small courtly bow; his brows are raised and his mouth is a thin, closed-lipped smile. Under his left arm, clamped flat against his side with its face turned outward, he holds a large cardboard sign, facing the lens squarely and held perfectly still. Stepping through the open doors past his outstretched hand, on the right of the frame, is a man in his sixties in a long camel overcoat and leather gloves, carrying a folded newspaper, his chin up and his eyes fixed ahead into the shop, not looking at him.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: The entrance of a British supermarket: the brick wall, the glass doors standing wide open, a stack of green wire baskets just inside, the bright aisles beyond, and a shallow puddle on the paving.

Light: Flat grey daylight from an overcast sky, soft and even, and the white light of the shop's interior pouring out through the open doors across both men. The shadows are soft, and the darkest parts of the frame keep their detail.

Details: Real skin texture, damp paving drying in patches, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the cardboard sign is plain bare card from edge to edge. No signs, logos, labels, newspaper headlines or shop fascia anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s10 — "I CAN'T LIVE LIKE THIS FOREVER" · Kingston · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the hook goes global, with dignity. The same words on another continent, and somebody stops to read them.
- **Red line (the storyboard's mitigations, Jack ruled photoreal 2026-09-27):** an invented man, upright and
  working, not in visible distress, meeting the public. He is a vendor standing beside his handcart, in a pressed
  shirt. His city's beneficiary is paired later (s17, the resort).
- **Camera:** a democratic eye level, 35mm at f/5.6, straight on, with the sign square to the lens.
- **Unresolved question:** a schoolboy has stopped and is reading the sign. What will he make of it?
- **Stopping versus passing:** the man and the boy are sharp and still, and the shoppers behind blur with movement.
  That's the cheapest crowd-realism lever (sixth pass), and it's the argument too.
- **Light (hard sun fails in generated shadows, ninth pass):** he stands in the shade of the covered walkway. The
  sunlit street beyond is the bright anchor and may burn out, while the shade keeps detail.
- **Place, named concretely against the global default (sixth pass):**
  - the covered walkways along old two-storey shop buildings
  - a white route taxi
  - a boy's khaki school uniform
  - ⬜ These are from memory and unverified for King Street specifically. Check them against real photos if the
    result looks off.
- **No Characters:** both are extras, described in full, with age, build and skin stated (seventh pass: an
  unreferenced person defaults to young and attractive).

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a hot weekday afternoon on King Street in downtown Kingston, Jamaica. Fine grain, natural colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at eye level about three metres from a man standing under a covered walkway, facing him straight on. He stands a little right of centre. Across the left edge of the frame, close to the lens and soft out of focus, rises one of the walkway's square concrete columns, its paint chipped. The frame is not quite level.

Action: The man is a Black Jamaican street vendor in his fifties, lean and upright, with grey in his short hair and moustache and deep lines at the corners of his eyes. He wears a pressed pale-blue short-sleeved shirt tucked into dark trousers, and old polished black shoes. He stands beside his wooden handcart of sweets and bottled drinks and holds a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. He looks straight into the lens, calm and level: his lips are pressed together, his chin is up, his eyes are steady. On the left of the frame, a schoolboy of about twelve in a khaki school shirt and trousers, a backpack on one shoulder, has stopped on the pavement a metre from him and is reading the sign, his head tilted, his eyes on the card. Behind them, shoppers pass along the walkway and the street, blurred by their movement. The man and the boy are sharp and still.

The sign: a flap cut from a brown cardboard carton, about the size of a newspaper, with one straight edge and three torn ones. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: A busy downtown shopping street: the covered walkway running along the fronts of old two-storey concrete shop buildings, their paint faded pastel, shop doorways with goods hung outside, and beyond the columns the street in full sun, with a white route taxi and people crossing.

Light: He and the boy stand in the deep shade of the walkway, lit softly by daylight bouncing off the bright street. Beyond the columns the street is in hard tropical sun and is the brightest part of the frame, and its highlights are allowed to burn out to white. The shade keeps its detail.

Details: Real skin texture, sweat at his temples, the worn paving of the walkway, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. No shop signs, labels, bottles or vehicle markings anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

**Round 2 · 2026-09-28.** Jack: *"no kids."* The schoolboy is replaced by an adult who stops to read, a woman in her
forties in a nurse's tunic on her way home. The passers-by are stated as adults. Nothing else changed.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a hot weekday afternoon on King Street in downtown Kingston, Jamaica. Fine grain, natural colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at eye level about three metres from a man standing under a covered walkway, facing him straight on. He stands a little right of centre. Across the left edge of the frame, close to the lens and soft out of focus, rises one of the walkway's square concrete columns, its paint chipped. The frame is not quite level.

Action: The man is a Black Jamaican street vendor in his fifties, lean and upright, with grey in his short hair and moustache and deep lines at the corners of his eyes. He wears a pressed pale-blue short-sleeved shirt tucked into dark trousers, and old polished black shoes. He stands beside his wooden handcart of sweets and bottled drinks and holds a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. He looks straight into the lens, calm and level: his lips are pressed together, his chin is up, his eyes are steady. On the left of the frame, a Black Jamaican woman in her forties, heavy-set, in a green nurse's tunic with a cardigan over it and a shopping bag on her forearm, has stopped on the pavement a metre from him and is reading the sign, her head tilted, her eyes on the card. Behind them, adult shoppers pass along the walkway and the street, blurred by their movement. The man and the woman are sharp and still.

The sign: a flap cut from a brown cardboard carton, about the size of a newspaper, with one straight edge and three torn ones. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: A busy downtown shopping street: the covered walkway running along the fronts of old two-storey concrete shop buildings, their paint faded pastel, shop doorways with goods hung outside, and beyond the columns the street in full sun, with a white route taxi and people crossing.

Light: He and the woman stand in the deep shade of the walkway, lit softly by daylight bouncing off the bright street. Beyond the columns the street is in hard tropical sun and is the brightest part of the frame, and its highlights are allowed to burn out to white. The shade keeps its detail.

Details: Real skin texture, sweat at his temples, the worn paving of the walkway, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. No shop signs, labels, bottles or vehicle markings anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s11 — "I DO WANT CHANGE" · Negril · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** working, not begging, and the fence. The pun comes back from s8 on a board that sells coconuts, while the
  beach behind him is being sold off.
- **The board holds still:** the vendor has stopped and parked his cart. The board is fixed upright to the cart,
  square to the lens, and painted one flat colour, with the words added in post in a sign-painter face. He doesn't
  hold it, so it can't move in the clip.
- **Unresolved question:** he looks along the fence at the guard, who is watching him. The two workers are on
  either side of a line neither of them drew.
- **Anti-postcard (the resort-advert trap, the same family as advert vocabulary):**
  - a hazy white post-shower sky, not blue
  - a brown wrack line of sargassum seaweed across the sand, footprints, a bottle cap
  - no golden hour
- **Depth:** the seaweed in the foreground, soft · the vendor, the cart and the board · the fence running
  diagonally to the sea, the guard behind it, empty loungers with folded towels beyond.
- **Adults only** (Jack, 2026-09-28). Everyone is invented and described in full.
- ⬜ **Unverified:** the vendor carts and the fence type are from memory, not checked against Negril photos.

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure in the early afternoon on the long beach at Negril, Jamaica, just after a rain shower. Fine grain, natural colour, unposed and imperfect.

Camera and framing: 35mm lens at f/8, held at eye level on the public sand about four metres from a beach vendor, everything from the near sand to the sea sharp. He stands a little left of centre. Across the bottom of the frame, close to the lens, runs a ragged brown line of washed-up sargassum seaweed. Behind him, a tall hotel fence runs diagonally down the beach from the right of the frame to the water's edge. The frame is not quite level.

Action: The vendor is a Black Jamaican man in his forties, wiry and sunburnt dark, with a short grey-flecked beard, a battered straw hat, a faded plain orange T-shirt and cut-off trousers, barefoot in the sand. He has stopped beside his two-wheeled wooden cart, one hand resting on the lid of a scuffed white cooler box strapped to it, three green coconuts on top. His head is turned toward the fence and his eyes are on the guard behind it; his lips are pressed together. Inside the fence, on the right of the frame, a security guard in his thirties in a grey uniform shirt and cap stands with his arms folded, watching the vendor.

The board: a flat rectangle of plywood about the size of a newspaper, fixed upright to the cart's handle and facing the lens squarely. Its face is painted one flat, even coat of pale yellow, matt and slightly chalky, with the grain of the wood faintly showing through, and it is held perfectly still.

Environment: On the vendor's side, open public sand with footprints, a bottle cap and the seaweed line. The fence is tall grey steel railings with green shade cloth tied along its lower half. Beyond it, the hotel's raked sand, rows of empty white sun loungers with folded towels, closed parasols, and a low hotel building among palms. The sea is flat and pale.

Light: A hazy white sky after the shower, bright and soft, with no hard shadows. The sky is the brightest part of the frame and may burn out to white at the top; the faces, the board and the sand keep their detail.

Details: Real skin texture, damp sand, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the board is plain yellow paint from edge to edge. No signs, logos, labels or uniform badges anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s12 — "I CAN'T LIVE LIKE THIS FOREVER" · Hong Kong · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** Asia, without the cliché. The hook in a third city, from a man with a job and nowhere to sleep.
- **Why the window and not the bench:** begging is illegal in Hong Kong (s26A, checked 2026-09-28). The storyboard's
  fallback applies. He is one of the working "McRefugees" at a 24-hour fast-food counter, with a cleaner's uniform
  and a bag of belongings. There's no cup, so it isn't an ask.
- **The sign:** pressed flat against the inside of the window, facing the street, square to the lens, held at its
  edge by one hand.
- **Camera:** outside in the rain, facing the glass squarely, about a metre off it, at eye level with him seated.
  Reflections are **not named** (§10). Glass reflects unasked, and a named reflection smears over faces.
- **Depth:** one passing umbrella soft at the left edge in the foreground · the glass and him · the bright empty
  restaurant behind him.
- **Light:** the restaurant's white fluorescent interior is the source and the bright anchor. It goes slightly green
  on film. The street behind the camera shows only as the dark it throws. No neon (twelfth pass).
- **Rain (§32):** the streaks are visible only against the dark umbrella and the dark pavement, never against the
  bright window.
- **Adults only,** described in full.

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800 pushed one stop, a single handheld night exposure at three in the morning in Sham Shui Po, Hong Kong, in steady rain. Heavy grain in the shadows, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/2.8, held outside on the wet pavement about a metre from the plate-glass window of a 24-hour fast-food restaurant, facing the glass squarely, at the eye height of a man sitting just inside it. He sits a little right of centre. Across the left edge of the frame, close to the lens and soft out of focus, passes the dark wet canopy of a black umbrella carried by someone walking by. The frame is not quite level.

Action: Inside, on a high stool at the narrow counter that runs along the window, sits a thin Hong Kong Chinese man in his late fifties, with close-cropped grey hair and hollow cheeks, wearing a cleaner's grey polo shirt under an old navy windbreaker. A paper cup of hot water stands on the counter in front of him, and a bulging plastic bag of belongings sits on the stool beside him. With his left hand he holds a large cardboard sign pressed flat against the inside of the glass, facing out to the street, his fingers only at its edge, the card facing the lens squarely and held perfectly still. He looks straight out through the glass into the lens, tired and level: his lips are closed, his eyelids are heavy, his eyes are steady.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: Behind him, the restaurant's bright interior, almost empty: rows of plastic tables and fixed seats, a tray left on one of them, and a single figure asleep with his head on his folded arms at a far table. Outside, raindrops run down the glass and the pavement at the bottom of the frame is black and wet.

Light: The only light is the hard white fluorescent light of the restaurant's interior, which goes slightly green on the film. It lights him and the sign through the glass and spills out onto the wet pavement. Everything outside the window falls to near-dark but keeps a trace of detail. The rain shows as fine streaks only where it falls across the dark umbrella and the black pavement.

Details: Real skin texture, water on the glass, fine natural grain, ordinary and unstyled.

Constraints: The face of the cardboard sign is plain bare card from edge to edge. No signs, menus, logos, labels or window lettering anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s13 — "I CAN'T LIVE LIKE THIS FOREVER" · back to Bob · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the rhyme closes the hook. Bob holds the same words in the same frame as the Kingston man (s10), so the
  cut says one sentence in three cities. The stat card (1 in 153, Shelter) follows in post.
- **The rhyme is built from geometry, not asked for:** standing, straight on, eye level, about three metres, a
  little right of centre, a soft vertical at the left edge. It's s10's framing exactly. Pro can't see s10, so the
  layout is restated rather than "rhyme with".
- **Not a repeat of s3:** s3 had him seated, off-level, with a woman turning away. Here he's standing, alone, level,
  and the day has moved on to dusk. That takes the film toward s14's night at Tarquin's building.
- **Light:** blue dusk, with the shop's white interior light as the key from the right. That's the bright anchor, and
  the dusk side keeps a trace of detail.
- **Depth:** the brick pier of the shop front soft on the left · Bob · the car park and the wet tarmac behind.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Bob`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure at dusk on a cold, wet November evening outside a British supermarket. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at eye level about three metres from the man from the character reference, facing him straight on. He stands a little right of centre, his whole upper body and the sign in frame, cut at the thighs by the bottom edge. Across the left edge of the frame, close to the lens and soft out of focus, rises the brick pier at the corner of the shop front. The frame is level.

Action: He stands alone on the wet paving and holds a large cardboard sign flat against his chest with both hands, his fingers gripping only its outer edges, the card facing the lens squarely and held perfectly still. He looks straight into the lens, calm and level: his lips are pressed together, his brows are relaxed, his eyes are steady.

The sign: a torn flap of brown corrugated cardboard about the size of a newspaper, with ragged edges and one corner mended with brown parcel tape. Its front is plain, bare brown card: an even, flat, matt surface with the faint ridges of the corrugation showing through, facing the camera flat so the whole face of it is in view.

Environment: Behind him, the supermarket car park at dusk: wet tarmac, faded bay lines, a trolley shelter, a few parked cars with their lights off, and a row of street lamps just coming on in the distance.

Light: The white light of the shop's interior falls across him and the sign from the right of the frame and is the brightest thing in the picture. The rest of the frame is blue dusk, darker toward the left, where his coat and the brick fall into shadow that still keeps a trace of detail.

Details: Real skin texture, wet paving, fine natural grain, ordinary and unstyled.

Constraints: Only this one man is in the frame. The face of the cardboard sign is plain bare card from edge to edge. No signs, logos, labels, shop fascia or number plates anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s14 — "YOU ARE INTENT ON LIVING IN A TENT" · the enamel sign · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** it introduces the refusal family. Verse 2's words stop being cardboard held by a man and become official
  signage bolted to money's property, and it's Tarquin's line on Tarquin's building.
- **It returns to s1:** the same building, the same studs on the stone ledge, the same warm lobby, now at night and
  seen wider. The viewer finally learns whose ledge it was.
- **The sign:** a white vitreous-enamel plate bolted to black railings, square to the lens, blank, described as an
  object. There's no border, so nothing inside it can turn into pseudo-letters. It's typed in post in a formal
  serif.
- **Tarquin:** passing in, in profile, mid-stride toward the door, not looking at the sign. The stride is written as
  a shape.
- **Depth:** the studded ledge along the lower foreground, soft at the near end · the railings and the sign · Tarquin
  · the lit lobby through the glass.
- **Light:** the lobby's warm interior light is the one source (continuous with s1). The white plate catches its
  spill and must keep its texture, not burn out, because post needs its surface.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Tarquin-new`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld night exposure on a wet November evening in central London. Heavy grain in the shadows, muted colour, unposed and imperfect.

Camera and framing: 35mm lens at f/5.6, held at chest height on the pavement about four metres from the front of an apartment block, facing a run of black iron railings straight on. Bolted to the railings, a little left of centre, is a white enamel sign, facing the lens squarely. Along the bottom of the frame, closest to the lens and soft at its near end, runs a low stone window ledge fitted with a strip of squat stainless-steel anti-homeless studs. The frame is not quite level.

Action: On the right of the frame, the man from the character reference walks past the railings toward the building's glass entrance, seen in profile, his front foot planted and his rear heel lifting, his head facing straight ahead toward the door. He does not look at the sign.

The sign: a rectangular plate of white vitreous enamel about the size of a newspaper, with rounded corners, fixed to the railings by a steel bolt at each corner. Its face is plain, bare white enamel from edge to edge: an even, flat, slightly glossy surface, with one small chip at the lower corner showing dark steel beneath and a faint streak of rust running down from one bolt. It is held perfectly still.

Environment: Behind the railings, the tall plate-glass front of the building's lobby: warm pools of lamplight, a long pale reception desk and a concierge behind it, all slightly out of focus. The pavement is wet and the stone of the building is pale and clean.

Light: The only light is the warm interior light of the lobby, coming out through the glass. It lights the man from the side, catches the white enamel sign and the tips of the steel studs, and spills across the wet pavement. The white of the sign keeps its surface texture and does not burn out. Everything outside the reach of the lobby light falls into dark blue night that keeps a trace of detail.

Details: Real surface texture, wet stone, fine natural grain, ordinary and unstyled.

Constraints: Only this one man and the concierge are in the frame. The face of the enamel sign is plain white enamel from edge to edge. No signs, logos, labels, door numbers or window lettering anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s15 — "PROSPECTS EXIST" · the brass plaque · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** his words on money's surfaces. A clean, easy hand brushes the brass on the way in, while an older man
  holds the door in the cold.
- **Visible cost:** the doorman. He's in his sixties, standing out in the rain, and he's the working body that the
  building's ease runs on.
- **The plaque:** engraved in post in a formal serif. Brushed brass, square to the lens, blank. The hand touches
  **only the plaque's edge** (the rule for signs: never the face). The brass is dulled by polishing, never
  mirror-bright. There was no metal-shine counter in the research, so the finish is named (thirteenth pass).
- **Tarquin's hand:** it's an unbound body part, so it's described (§25) from `characters/tarquin.md`: a signet
  ring, the old scuffed steel watch, the charcoal overcoat cuff. No Character, because there's no face.
- **Depth:** the plaque on the wall, sharp and centre-left · the hand entering from the right · the doorman soft
  behind, holding the brass handle, with the lobby glowing past him.
- **Light:** the lobby's warm light through the open door (continuous with s1 and s14). It warms the brass and the
  hand, and the doorman stands at the edge of it, half in the blue night.

Nano Banana Pro · 16:9 · x2 · 2K. No Character, no reference.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld night exposure on a wet November evening in central London. Heavy grain in the shadows, muted colour, unposed and imperfect.

Camera and framing: 50mm lens at f/4, held at shoulder height about a metre from the pale stone wall beside the entrance of an apartment block, facing the wall straight on. A brass plaque is fixed to the wall a little left of centre, facing the lens squarely and sharp. The open glass door of the entrance is on the right of the frame. The frame is not quite level.

Action: A man's hand comes in from the right of the frame as he walks through the door, and the tips of his first two fingers brush the right-hand edge of the plaque in passing, touching only its edge. It is a smooth, well-kept hand in its thirties with a plain heavy gold signet ring on the little finger and an old scuffed steel watch showing beneath the cuff of an expensive charcoal overcoat. Just beyond, soft and out of focus, a doorman in his sixties holds the door open by its brass handle: a tall, heavy-set man with a grey moustache, in a long dark grey coat and peaked cap beaded with rain, standing straight and looking ahead into the street, not at the man going in.

The plaque: a rectangular plate of brass about the size of a large book, fixed to the stone by a round-headed brass screw at each corner. Its face is plain brushed brass from edge to edge: an even, flat surface, dulled and softly scratched by years of polishing, with a faint dark bloom of tarnish at the corners. It is held perfectly still.

Environment: Pale, clean Portland stone, wet at its base. Through the open door behind the doorman, the warm, bright lobby: lamplight, a pale marble floor, the edge of a reception desk.

Light: The only light is the warm interior light of the lobby, coming out through the open door. It warms the brass plaque and the passing hand. The doorman stands at the edge of it, lit on one side, the other side of his face and coat falling into the dark blue night, which keeps a trace of detail. The brass glows softly and never flares.

Details: Real skin texture, the grain of the stone, rain on the doorman's cap, fine natural grain, ordinary and unstyled.

Constraints: The face of the plaque is plain brushed brass from edge to edge. No signs, logos, labels, badges or door numbers anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s16 — "I WORK HARD" · the golf-club board · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the cost in frame. "I WORK HARD" is set on the club's own board, while the man actually working is bent
  double in the foreground.
- **Built on mv2-3's caddie shot (2026-09-27, unrun),** moved to the tee so the board can stand in it. The caddie,
  Tarquin's waiting hand and the council towers are kept word for word.
- **The board:** a tee board on two posts at the back of the tee, facing players arriving, which means facing us.
  It's square to the lens, dark green paint with a gold-painted moulding round its edge, and the face is plain. The
  moulding is described as a frame, never as a border with anything inside it. It's typed in post in a gold serif.
- **Depth:** the caddie's back soft in the left foreground · the board sharp, right of centre · Tarquin on the tee
  · the oaks · the towers.
- **Light:** flat overcast, unchanged from mv2-3.
- 🔴 **Time of day:** s13–s15 run dusk into night. This is a different day (verse 2 is Tarquin's rounds), so the cut
  signals a new place, not a continuity break.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Tarquin-new`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on a flat grey October afternoon. Fine grain, muted colour, low saturation, unposed and imperfect.

Camera and framing: 50mm lens at f/5.6, standing on the path at the back of a tee, directly behind a caddie, at his shoulder height, about a metre behind him. The caddie fills the left third of the frame in the foreground, soft and out of focus, his back squarely toward us: the back of his head hides the rest of his head, and the picture holds his wet grey hair, his collar and his back. Four metres ahead, right of centre and sharp, a painted wooden tee board stands on two short posts at the edge of the tee, facing the lens squarely. Six metres ahead, on the tee beyond the board, the man from the character reference walks away from us toward the tee markers.

Action: The caddie is a thin, stooped man in his sixties in a cheap navy waterproof jacket, bent under a heavy leather golf bag slung on his right shoulder, the strap dragging the jacket tight across his back, his left hand pressed into the small of his back. The man from the character reference walks with empty hands, mid-stride, and holds his right hand out behind him at hip height, palm open and fingers spread, waiting for a club to be put into it, without turning his head. His head faces down the fairway.

The board: a flat rectangular wooden board about the size of a newspaper, its face painted one even coat of dark bottle green, matt and slightly weathered, framed by a raised moulding painted gold round its outer edge. The green face inside the moulding is plain from edge to edge. It is held perfectly still.

Environment: A private members' golf course on the edge of London: a close-mown tee with two white tee markers, the fairway beyond striped by the mower, a line of bare oaks, and beyond the trees at the far edge of the course, grey above the branches, the tops of three 1960s concrete council tower blocks.

Light: A flat overcast sky and no sun, soft light from everywhere above, the grass a dull green and the shadows short and soft under their feet. The sky is pale but keeps its cloud texture, and the caddie's dark back keeps its detail.

Details: Wet grass stuck to the caddie's shoes, a broken wooden tee lying in the turf, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are on the course. The green face of the board is plain paint from edge to edge. No signs, logos, labels or readable text anywhere in the frame.

Compose for a 16:9 frame.

Thanks.
```

### s17 — "MY POCKETS ARE EMPTY" · the hotel beach gate · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the beneficiary, paired. Jamaica's beneficiary is sitting inside the fence being served, and the man who
  is working is outside it. The sign is his line, "MY POCKETS ARE EMPTY", on the gate that keeps the beach private.
- **The handover rhymes with s16:** Tarquin's hand is raised back over his shoulder without looking, the same
  gesture as waiting for a club. The vendor pushes a coconut through the bars into it, and the palm is just short of
  the shell. That's the stillness designed in (§38).
- **The vendor is s11's man, re-described word for word** (no reference, per the one-reference house rule, because
  `@Tarquin-new` is already attached). If he drifts, attach s11's accepted still instead and drop his description.
- **The gate sign:** a navy aluminium plate with a brass-coloured rim, bolted to the gate, square to the lens, the
  face plain. It's typed in post in the hotel's serif. The gate itself is bare railings (the shade cloth is on the
  fence only), so the lounger stays visible.
- **Depth:** s11's seaweed line soft along the bottom · the gate and the sign · the hands at the bars · Tarquin on the
  lounger · the empty loungers and the sea.
- **Light:** s11's hazy post-shower sky, the same afternoon.
- **Adults only.**

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Tarquin-new`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure in the early afternoon on the long beach at Negril, Jamaica, just after a rain shower. Fine grain, natural colour, unposed and imperfect.

Camera and framing: 35mm lens at f/8, held at chest height on the public sand about two metres outside a hotel's beach gate, facing the gate squarely, everything from the near sand to the sea sharp. Across the bottom of the frame, close to the lens, runs a ragged brown line of washed-up sargassum seaweed. A sign is bolted to the left half of the gate, facing the lens squarely. The frame is not quite level.

Action: Just inside the gate, on a white sun lounger pushed up against the bars, the man from the character reference reclines with his head turned toward the sea. Without looking round, he has raised his right hand back over his shoulder toward the bars, palm open, waiting. On the right of the frame, outside the gate, a beach vendor pushes a green coconut with a straw in it through the gap between two bars toward that hand; the open palm is just short of the shell, not yet touching it. The vendor is a Black Jamaican man in his forties, wiry and sunburnt dark, with a short grey-flecked beard, a battered straw hat, a faded plain orange T-shirt and cut-off trousers, barefoot in the sand, seen side-on, his eyes on the coconut. His two-wheeled wooden cart with a scuffed white cooler box stands behind him.

The sign: a rectangular plate of navy-blue painted aluminium about the size of a newspaper, with a thin brass-coloured metal rim round its edge, fixed to the gate by a bolt at each corner. Inside the rim its face is plain navy blue from edge to edge: an even, flat, matt surface with a faint salt bloom. It is held perfectly still.

Environment: The gate is a pair of tall grey steel railing panels with a heavy padlocked bolt; the fence running away on either side has green shade cloth tied along its lower half. Beyond the gate, the hotel's raked sand, rows of empty white sun loungers with folded towels, closed parasols, and a low hotel building among palms. The sea is flat and pale.

Light: A hazy white sky after the shower, bright and soft, with no hard shadows. The sky is the brightest part of the frame and may burn out to white at the top; the faces, the hands, the sign and the sand keep their detail.

Details: Real skin texture, damp sand, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the sign is plain navy blue from edge to edge. No signs, logos, labels or towels anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s18 — "THE ONLY THING I'M CHANGING IS THE LANE" · the gantry · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the pun is paid. The only change he makes is to swing the X8 into the outside lane, under a sign that
  says so.
- **The sign:** a motorway variable-message panel, **switched off**. It's a dark matrix rectangle, and post types
  the line in amber LED dots, the most native text there is for a blank panel. It hangs over the lane he's moving
  into, square to the lens.
- **Legibility (§20/§32 family):** a black panel against a black sky disappears. So the sky is low cloud lit
  orange-grey by the city, and the gantry and panel read as a dark silhouette against it.
- **Camera:** in the lane behind, at car-roof height, on an 85mm, which compresses the gantry to loom over the car
  (§14, long lenses). The car is seen from behind, so it's identified by the rear plate `BAD C0DE` and the roundel,
  per the wank-tank rule on the tailgate.
- **Light:** the one real source is the headlights of the vehicle behind (the camera's). They light the tailgate,
  the plate and the lane markings. The X8's red tail lights and the amber indicator are the most saturated things
  in frame, stated comparatively (§33).
- **Mid-lane-change:** the car straddles the dashed line, and the indicator is lit. That's a held state, not a
  motion (§38).
- **Scale and cost:** a lorry in the inside lane, which he cuts in front of.
- ⬜ **Check the lane lines** where they converge on the vanishing point (a known failure, tenth pass).

Nano Banana Pro · 16:9 · x2 · 2K. No Character (Tarquin is behind privacy glass).

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800 pushed one stop, a single handheld night exposure from a car on a British motorway just after rain. Heavy grain in the shadows, muted colour, unposed and imperfect.

Camera and framing: 85mm lens at f/2.8, held at car-roof height in the middle lane of a three-lane motorway, about twenty metres behind a blacked-out BMW X8. The long lens pulls an overhead steel gantry close, so it spans the upper half of the frame and looms over the car. A single rectangular electronic message panel hangs from the gantry above the outside lane, facing the lens squarely. The frame is not quite level.

Action: The X8 is halfway through moving from the middle lane into the outside lane, its body straddling the white dashed lane line, its right-hand amber indicator lit. On the left of the frame, in the inside lane, a large lorry rolls alongside, the black car cutting across ahead of it.

The car: a very large black BMW SUV seen from behind: a tall, flat tailgate with the round BMW roundel at its centre, slim red tail lights, a high beltline and dark privacy glass. Its rear number plate, lit by its small plate lamp, reads "BAD C0DE", spelled B, A, D, space, C, zero, D, E.

The panel: a large flat rectangle of dark matrix screen in a grey steel housing, switched off. Its face is plain matt black from edge to edge, held perfectly still, and it reads as a dark shape against the sky.

Environment: A wet three-lane motorway at night: white dashed lane lines, a hard shoulder with a crash barrier, the grey steel lattice of the gantry, and the road running on into the dark. The sky is low cloud lit a dull orange-grey by the city beyond, so the gantry and its panel show as dark silhouettes against it.

Light: The only light on the road is the white headlight beam from our own car behind the camera, lighting the tailgate, the number plate and the wet lane lines in front of us, and breaking into smeared reflections on the wet tarmac. The red of the tail lights and the amber of the indicator are the most saturated colours in the picture by a wide margin. Everything beyond the reach of the headlights falls into near-black that keeps a trace of detail.

Details: Spray lifting off the lorry's wheels, road grime on the car's lower tailgate, fine natural grain, ordinary and unstyled.

Constraints: The face of the message panel is plain matt black from edge to edge. The number plate reading "BAD C0DE" and the car's own badge are the only readable lettering; every other sign, the lorry and every other number plate carry no readable lettering.

Compose for a 16:9 frame.

Thanks.
```

### s19 — "WEALTH GAP?" / "WHAT A LOAD OF CRAP" · the wine label · still · written 2026-09-28, handed over 2026-09-28 (result not yet logged)

**Spec (shot-craft):**
- **Job:** the sneer. The line is printed on the most expensive object on the table, and it's presented to him by a
  man who can't afford it.
- **Presenting, not pouring:** a steward holds the bottle upright in both hands, label out, the real gesture of
  showing the label. A pouring bottle tilts, and the label must be square and still. The pour happens in the video
  after the text beat, or not at all.
- **One label, two lines,** swapped in post, as in s7 and s9.
- 🔴 **A label on a bottle is curved.** Corner Pin can't wrap a cylinder. Premiere's catalogue has no cylinder
  wrap (the Impact Warp and Wave effects are the nearest). ffmpeg's `remap` could do it with a generated map, but
  that's untested. So it's a **magnum** (a gentle curve) on an 85mm straight on, with a wide flat label. If
  the typed words look pasted on, the fallback is a cream card neck tag.
- **Visible cost:** the steward. He's sweating at the collar in the heat, tired around the eyes, and holding the
  bottle steady. He's sharp, and Tarquin is soft behind him, holding a glass up without looking (the recurring
  blind hand).
- **Anti-advert:** a yacht deck is a luxury-advert brief. So no golden hour: a flat white hazy sky, salt crust on
  the rail, a coiled line, and a crumpled napkin.
- **Depth:** the bottle and the steward's hands sharp in the foreground · the steward's face · Tarquin soft at the
  table · the sea.

Nano Banana Pro · 16:9 · x2 · 2K. Cast `@Tarquin-new`.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on the aft deck of a large private yacht at anchor, on a hot, hazy afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 85mm lens at f/4, held at chest height about two metres from a steward, facing him straight on. He stands a little left of centre and holds a magnum of red wine upright in front of his chest with both hands, its label turned toward the lens and square to it, sharp. Behind him, soft and out of focus, the man from the character reference sits at a low table. The frame is not quite level.

Action: The steward presents the bottle with the label outward, one hand around its neck and the other cupping its base, fingers clear of the label, the bottle held perfectly still. He is a man in his forties with a tired, lined face and cropped dark hair, in a white short-sleeved crew shirt with sweat darkening the collar, and he looks at the bottle, not at the guest. Behind him, the man from the character reference lounges at the table with his head turned toward the sea, holding an empty wine glass up beside him at shoulder height without looking at it.

The label: a wide, flat rectangle of thick cream paper covering the front of the bottle, its face plain cream from edge to edge: an even, matt, slightly textured surface. The bottle is a dark green glass magnum, wide enough that the label curves only gently.

Environment: The teak deck of the yacht, a low table with a white cloth, a crumpled napkin and an ice bucket, a steel rail crusted white with dried salt, a coil of rope, and beyond the rail the flat, pale sea and a faint line of hills in the haze.

Light: A hazy white sky, bright and flat, with no hard sun and no shadows to speak of. The sky is the brightest part of the frame and may burn out to white; the steward's face, the bottle and the label keep their detail.

Details: Real skin texture, beads of sweat at the steward's temple, dried salt on the rail, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the label is plain cream paper from edge to edge. No labels, logos, uniform badges or boat names anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

**Round 2 · 2026-09-28.** Jack: *"the bottle is comically large and the waiter does not look posh."*
- **Bottle:** the magnum is out, and an ordinary 75cl bottle is in, stated as in proportion to his hands. The
  camera goes back to 2.5 m so the bottle, his chest and his face all fit. 🔴 The label now curves more, so the post
  fallback (a flat neck tag or ffmpeg `remap`) is more likely to be needed.
- **Steward:** from crew-shirt worker to immaculate butler: a pressed white high-collared jacket, brass buttons,
  white gloves, combed hair, a composed face. The visible cost shrinks to one bead of sweat in the heat. Nothing else
  changed.

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on the aft deck of a large private yacht at anchor, on a hot, hazy afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 85mm lens at f/4, held at chest height about two and a half metres from a steward, facing him straight on. He stands a little left of centre and holds an ordinary 75cl bottle of red wine upright in front of his chest with both hands, its label turned toward the lens and square to it, sharp. Behind him, soft and out of focus, the man from the character reference sits at a low table. The frame is not quite level.

Action: The steward presents the bottle with the label outward, one hand around its neck and the other cupping its base, fingers clear of the label, the bottle held perfectly still. He is an immaculate butler-steward in his forties, clean-shaven, his hair neatly combed and parted, in a crisp, pressed white high-collared steward's jacket with a row of brass buttons, and white cotton gloves. He stands very straight, his chin level, his face composed and expressionless, and he looks at the bottle, not at the guest. In the heat, a single bead of sweat runs down from his temple. Behind him, the man from the character reference lounges at the table with his head turned toward the sea, holding an empty wine glass up beside him at shoulder height without looking at it.

The label: a wide, flat rectangle of thick cream paper covering the front of the bottle, its face plain cream from edge to edge: an even, matt, slightly textured surface. The bottle is a standard-size dark green glass wine bottle, in proportion to his gloved hands.

Environment: The teak deck of the yacht, a low table with a white cloth, a crumpled napkin and an ice bucket, a steel rail crusted white with dried salt, a coil of rope, and beyond the rail the flat, pale sea and a faint line of hills in the haze.

Light: A hazy white sky, bright and flat, with no hard sun and no shadows to speak of. The sky is the brightest part of the frame and may burn out to white; the steward's face, the bottle and the label keep their detail.

Details: Real skin texture, the one bead of sweat at the steward's temple, dried salt on the rail, fine natural grain, ordinary and unstyled.

Constraints: Only these two men are in the frame. The face of the label is plain cream paper from edge to edge. No labels, logos, uniform badges or boat names anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```

**Round 2 result, analysed 2026-09-28 (Jack's pick, no reference image for round 3):**
- ✅ **Working:**
  - the steward reads as posh (white jacket, brass buttons, gloves)
  - the bottle is normal size and the label is clean, blank cream
  - the hazy sea, the rope coil and the ice bucket
- 🔴 **Not working:**
  - **Tarquin isn't Tarquin.** A generic dark-haired man in a navy shirt, holding the glass at his chest and looking
    off camera. The blind held-out hand didn't land.
  - **Both faces are model-handsome** ("hyper-average", seventh pass). The steward reads as an actor, and the
    frame reads as a Riviera advert.
  - **The steward is turned three-quarters** with the bottle held off to the side. The label is square only by
    luck.
  - **"One bead of sweat" came back as a wet splash** across his cheek.
  - **No visible cost survives.** Two handsome men on a lovely boat.
- **Round 3, one direction: make it an argument, not an advert.**
  - Tarquin is written in prose from `characters/tarquin.md`: the face lock, plus a yacht version of the leisure
    register (linen, sockless tan loafers). His arm is stretched out toward the steward and his head is turned
    away.
  - The steward is older with a distinctive face, still immaculate, and he stands square to the lens.
  - The cost is carried by light, not sweat: Tarquin sits in the shade of an awning, and the steward stands in the
    white glare.
  - A deckhand on her knees wiping the rail adds the second working body.

Nano Banana Pro · 16:9 · x2 · 2K. **No Character, no reference** (Jack, round 3).

```prompt
SCENE:

Candid documentary photograph on Kodak Portra 800, a single handheld exposure on the aft deck of a large white motor yacht at anchor, on a hot, hazy afternoon. Fine grain, muted colour, unposed and imperfect.

Camera and framing: 85mm lens at f/4, held at chest height about two and a half metres from a steward, facing him straight on. He stands square to the camera, a little left of centre, out on the open deck, and holds a bottle of red wine upright in front of the middle of his chest with both hands, its label facing the lens squarely, sharp. Behind him on the right, soft and out of focus, a guest sits in the shade of a canvas awning. The frame is not quite level.

Action: The steward presents the bottle with the label outward, one gloved hand around its neck and the other cupping its base, fingers clear of the label, the bottle held perfectly still. He is a butler-steward in his late fifties, heavy-browed, with a long, slightly crooked nose, deep lines from nose to mouth and thinning grey hair combed straight back: an ordinary face, not a handsome one. He wears a crisp, pressed white high-collared steward's jacket with a row of brass buttons and white cotton gloves, stands very straight in the full glare of the open deck, and looks at the bottle, his face composed and expressionless. Behind him, the guest lounges in a cushioned deck chair under the awning, a white man in his late forties with dark hair greying at the temples and slicked straight back, a well-fed face with a faint jowl, a slight sheen and broken veins at the nose, and pale indoor skin. He wears an open-collared pale linen shirt, navy trousers and tan suede loafers with no socks, a heavy signet ring and an old steel watch. His right arm is stretched out toward the steward, holding up an empty wine glass by the stem, while his head is turned the other way toward the sea, his chin slightly raised.

The label: a flat rectangle of thick cream paper on the front of the bottle, its face plain cream from edge to edge: an even, matt, slightly textured surface. The bottle is a standard-size dark green glass wine bottle, in proportion to the steward's gloved hands.

Environment: The white fibreglass and teak aft deck of the yacht, a low table in the shade with a white cloth, a crumpled napkin and a steel ice bucket, a coil of rope by the rail, and at the far left of the frame, small and in the background, a deckhand in a navy polo shirt on her knees wiping the steel rail with a cloth. Beyond the rail, the flat, pale sea and a faint line of hills in the haze.

Light: A hazy white sun, high and bright. The steward stands out in the glare, his white jacket bright but keeping its folds; the guest sits in the cooler shade of the awning. The sky is the brightest part of the frame and may burn out to white; the faces, the bottle and the label keep their detail.

Details: Real skin texture, dried salt on the rail, a smear on the steel ice bucket, fine natural grain, ordinary and unstyled.

Constraints: Only these three people are in the frame. The face of the label is plain cream paper from edge to edge. No labels, logos, uniform badges or boat names anywhere in the frame carry readable lettering.

Compose for a 16:9 frame.

Thanks.
```
