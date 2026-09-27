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
  ("McRefugees": 334 a night in 2018, 57% of them working). ⬜ **Whether begging with a sign is legal in Hong Kong
  is unverified.** Check before the sign shot, or give the Asia sign to the fast-food window.
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
| 10 | Hook 1 | **"I CAN'T LIVE LIKE THIS FOREVER"** | Kingston, King Street, day: an upright man in his fifties in a clean shirt holds the hook; shoppers pass, one schoolboy stops to read it | The hook goes global, with dignity |
| 11 | Hook 1 | "I DO WANT CHANGE" (on the vendor's hand-painted cooler board) | Negril beach: a vendor walks the sand with a coconut cooler; behind him a hotel's fence and a guard | Working, not begging; the fence |
| 12 | Hook 1 | "I CAN'T LIVE LIKE THIS FOREVER" ⬜ *legality unverified* | Sham Shui Po, rain, night: a man on a divided bench under a flyover; fluorescent lightboxes, one surviving neon; office workers under umbrellas step past | Asia, without the cliché |
| 13 | Hook 1 | "I CAN'T LIVE LIKE THIS FOREVER" · 🃏 *"1 in 153 people in England are homeless tonight. — Shelter, Dec 2025"* | Back to Bob: the same hook, both hands | The rhyme closes the hook |
| 14 | V2 | "YOU ARE INTENT ON LIVING IN A TENT" (white enamel sign bolted to railings) | Tarquin's building: studs on the ledge, the enamel sign above them, Tarquin passing in | The refusal family introduced |
| 15 | V2 | "PROSPECTS EXIST" (engraved brass plaque) | Close: his hand touches the brass plaque by the door as he enters; the doorman holds it | His words on money's surfaces |
| 16 | V2 | "I WORK HARD" (the golf club's green-and-gold board) | The caddie shot (mv2-3): the old man carrying the bag in the foreground, the club board by the tee | The cost in frame |
| 17 | V2 | "MY POCKETS ARE EMPTY" (the hotel beach gate) | Jamaica resort: Tarquin on a lounger inside the fence; outside, the vendor from shot 11 passes a coconut through the bars | The beneficiary, paired |
| 18 | V2 | "THE ONLY THING I'M CHANGING IS THE LANE" (motorway gantry sign) | Night motorway, the X8 under an overhead gantry | The pun paid |
| 19 | V2 | "WEALTH GAP?" / "WHAT A LOAD OF CRAP" (the wine label) | Yacht deck, a bottle poured, the label turned to the lens | The sneer |
| 20 | Hook 2 | — | Tokyo, dawn: blue tarp shelters along the Sumida river wall; a bench with steel dividers, a rolled bedroll beneath | The refusal is global |
| 21 | Hook 2 | "I CAN'T LIVE LIKE THIS FOREVER" | Hong Kong: the bench from shot 12 now empty, his sign wedged between the dividers | Moved on |
| 22 | Hook 2 | — | Hellshire: a woman frying fish in a cookshop with the sea at its door; fishermen haul a boat; kids flip off the bow | Joy, and the sea taking it |
| 23 | Hook 2 | "I MIGHT BE INSANE" | Bob again, looking straight into the lens | Home |
| 24 | Bridge | "HERE WE BOTH ARE" + "LIVING IN A CAR PARK" | The ruined car park, five years on: both men side by side facing the lens, one sign each | The jump, with no narration |
| 25 | Bridge | "THE AI DOES THE FAST PART" | Tarquin tries to sit on his own building's ledge; the studs stop him | Locked out by his own spikes |
| 26 | Bridge | "WE WERE ON THE SAME SIDE ALL ALONG" | Their two signs turned to face each other, over the drum fire | The turn |
| 27 | Final hook | "I CAN'T LIVE LIKE THIS FOREVER" ×5 · 🃏 *"Billionaire wealth rose $2.5tn in 2025 — about the wealth of the poorest 4.1 billion people. — Oxfam, Jan 2026"* | Beat-cut: Kingston man, Negril vendor, Hong Kong sign, Bob, Tarquin, each holding the hook | Everyone, same words |
| 28 | Outro | — | Every sign on the fire; the embers become bad code | The film's own ending |

Next session: one still at a time, then that shot's video. **First up: shot 3** (the device and look test, and the first blank-card test).

### s3 — "ONCE AGAIN" · still · written 2026-09-27, unrun

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
