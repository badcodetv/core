# The Bank Robbery — third pass of stills, for the script (7 October 2026)

**Asked for by Jack, 7 October 2026:** "make the stills for all of this, I liked the low angle /
David Lynch style from the old stills, they were great so do that again. Please avoid elements of
AI slop."

The script ([`script.md`](./script.md)) was gone through scene by scene with Jack the same day and
now has twelve scenes. Thirteen of yesterday's second-pass stills ([`stills.md`](./stills.md))
still fit it. This pass makes the shots the script added.

- **Flow project:** `63d22c4b` ("Oct 06 - 14:23"), where the twelve Characters live.
- **Settings:** Nano Banana 2 (Jack's standing rule; it costs no credits), 16:9, one candidate each.
- **Casting:** by hand through the "@" picker, up to four Characters a still.
- **Files:** `Desktop\Youtube Vids\animation\bank robbery\images\scenes-v3\<id>.jpg`. Not committed.
- **Prompts, word for word:** [`scripts/bank-robbery/br-stills-v3.json`](../../../scripts/bank-robbery/br-stills-v3.json).
  Each prompt is `pre` (only when a Character is attached) + the shot's `body` + `end` (or
  `endLens` for the scene 4 cards, where the person looks into the lens).
- **Runner:** `scripts/bank-robbery/br-stills-v3.mjs`, which calls
  `scripts/flow/.tmp/cast-many-v4.mjs` once per shot and skips files already on disk.

## What stays from the second pass (the look Jack liked)

The prompt shape is the same one, on purpose:

1. "A frame from a feature film, shot on 35mm with a [lens] lens [in a named physical place]."
2. Something large and out of focus against the lens.
3. The people: where each one is and what their face is doing. Nothing about how they look,
   because the Character carries that.
4. One sentence saying what is behind them "and nothing else".
5. "One light source only, no fill:" one named source, then where the shadow falls.
6. The colour lock, word for word: "Muted colour: stone grey, black and navy, with small touches
   of red and blue the only strong colour."

No director or person is named in any Flow field.

## What was added against the AI look

From the repo ([`nano-banana-2.md`](../../google-flow/nano-banana-2.md) anti-slop toolkit,
[`symptoms.md`](../../cinematography/symptoms.md)) and a web pass on 7 October 2026:

| The tell | What each prompt now does |
| --- | --- |
| Smooth, waxy skin | "Unretouched, natural skin texture" in the closing lock |
| A set that is too clean | One or two named bits of mess per shot: a ring of spilt tea, a dead fly, a dropped strawberry, an oil stain |
| Everything centred and level | "off-centre", "not quite level", and one person "nearer and larger" where two would mirror |
| Posed people | Everyone is caught in the middle of doing something |
| Light from nowhere | One named source with a position (unchanged from the second pass) |
| Praise words | None. No "cinematic", "masterpiece", "8k", "hyperrealistic" |
| Named haze, dust, reflections | Left out. The repo's own finding is that they arrive unasked and overdo it when named |

**What the web pass found** (a research agent's report; it read the pages through a summarising
fetch, so the quotes are as relayed, not checked word for word):

- Google's own guides for this model family give the order subject, action, location, composition,
  style; say to use photographic terms such as "low angle"; say to describe what you want and not
  what you do not want; and say to put any words that must appear in the picture in quotes and
  name the lettering.
  [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana),
  [Gemini API docs](https://ai.google.dev/gemini-api/docs/image-generation),
  [Google blog](https://blog.google/products/gemini/prompting-tips-nano-banana-pro/)
- Practitioners on the AI look name plastic skin, symmetry, impossible lighting, too-clean sets and
  perfect teeth, and report the same fixes the repo already had: pores and blemishes, one named
  light, mess, a film stock, closed mouths. These are vendor blogs, not measurements.
  [Magicshot](https://magicshot.ai/blog/why-your-ai-images-still-look-fake-12-tells-and-how-to-kill-them),
  [fal.ai](https://fal.ai/learn/tools/nano-banana-pro-prompting-guide)
- Google's own example prompts use "cinematic" and a teal grade. Leaving those words out is
  practitioner advice and the repo's finding, not Google's.
- **Not found anywhere:** a source for centred composition, fake blur or teal-and-orange being
  tells. Those stay as craft judgement.
- Flow's default image model is Nano Banana Pro, so Nano Banana 2 has to be chosen each time.
  [Flow Help](https://support.google.com/flow/answer/16729550?hl=en)

Nothing in the web pass disagreed with the repo.

## The shots

"Kept" means yesterday's second-pass still is used as it is.

| Scene | Still | Camera is | The one light | Characters |
| --- | --- | --- | --- | --- |
| 1 | `s01-breakfast` | Kept | | |
| 1 | `s01b-remote` | On the table top, behind the hand with the remote | The steamed window | The Proprietor, Mr Blue, Mr Red |
| 1 | `s01c-blue` | Plate height, close | The window | Mr Blue, Denise |
| 1 | `s01d-red` | Plate height, close | The window | Mr Red, Denise |
| 1 | `s01e-denise` | On the table top, looking steeply up | The window | Denise |
| 2 | `s02-spoiler` | Kept (Denise locks up, the van behind) | | |
| 2 | `s02b-shut-shops` | On the pavement, ankle height | One street lamp | Denise |
| 2 | `s02c-bank-door` | At the foot of the bank, looking up; the top two thirds left empty for the title | One lamp over the side door | Denise |
| 3 | `s03a-hearing` | On the committee table, behind a jug and a microphone | One lamp over his chair | The Ex |
| 3 | `s03-getting-out` | Kept; also The Ex's card in scene 4 | | |
| 4 | `s04b-fixer` | On the tablecloth | A table lamp, from below | The Fixer |
| 4 | `s04c-donor` | At the surface of the pool | Low evening sun | The Donor |
| 4 | `s04d-governor` | On his desk | The green desk lamp | The Governor |
| 4 | `s04e-proprietor` | On the print hall floor | A work lamp behind him | The Proprietor |
| 4 | `s04f-presenter` | Where the dressing-room mirror is | The mirror bulbs | The Presenter |
| 4 | `s04g-platform` | Chest height, at a laptop held up by an assistant | The laptop screen | The Platform |
| 4 | `s04h-accountant` | On the records-room floor | A failing strip light | The Accountant |
| 4 | `s04-recruiting` | Kept (the two screaming) | | |
| 4 | `s04i-drivers-freeze` | On the studio desk | One studio lamp | Mr Blue, Mr Red |
| 4 | `s04j-turquoise` | His own phone, at arm's length | Overcast daylight | Mr Turquoise |
| 5 | `s05-plan` | Kept | | |
| 5 | `s05b-blue-side` | Inside the model street | The blue glow of the model houses | The Proprietor |
| 5 | `s05c-red-side` | Inside the model street | The blue and red glow of the houses | The Platform, Mr Red |
| 5 | `s05d-twist` | At the table edge, close | The bare bulb | The Ex, The Donor, The Accountant |
| 6 | `s06a-list` | On the garage floor | The bare bulb | The Ex, Mr Turquoise, Mr Blue |
| 6 | `s06-colours` | Kept | | |
| 7 | `s07-night-before` | Kept | | |
| 7 | `s07b-off-record` | A camcorder, too close | Its own lamp | The Presenter, The Proprietor |
| 7 | `s07c-denise-hall` | High in the corner of the banking hall | One green desk lamp | Denise |
| 8 | `s08a-placards` | In the crowd, across the barrier | Overcast daylight | none |
| 8 | `s08b-remote-window` | In a dark upstairs room, behind the hand with the remote | The window | none |
| 8 | `s08c-megaphones` | On the tarmac of the empty strip | Overcast daylight | Mr Blue, Mr Red |
| 8 | `s08d-presenter` | Beside the news camera | The news camera's lamp | The Presenter |
| 8 | `s08-march` | Kept (the barrier going down) | | |
| 9 | `s09a-officer` | On the cobbles, boot height | A red flare | The Ex, The Fixer |
| 9 | `s09-walk` | Kept | | |
| 9 | `s09c-pallet` | On the tarmac, under the load | Overcast daylight | Mr Blue, Mr Red |
| 9 | `s09d-door` | On the bank's doormat, looking out | Daylight through the door | The Governor |
| 9 | `s09e-turquoise` | On the lobby floor | One green desk lamp | Mr Turquoise |
| 10 | `s10a-enter` | Behind the men's shoulders | The lit doorway behind her | Denise |
| 10 | `s10-hoover` | Kept | | |
| 10 | `s10c-that-much` | Very close, her hand in front | One green desk lamp | Denise |
| 10 | `s10d-counting` | Behind her shoulder, down the corridor | The open vault | Denise |
| 11 | `s11-vault` | Kept | | |
| 11 | `s11b-in` | On the vault floor, looking out | The vault's strip light | The Ex |
| 11 | `s11c-keys` | Inside a safe-deposit box | A strip light behind him | The Donor |
| 11 | `s11d-pricetags` | Inside the model street | The bare bulb | none |
| 12 | `s12a-standoff` | Kept | | |
| 12 | `s12d-lowering` | On the corridor floor | A strip light behind them | Mr Blue, Mr Red, The Governor |
| 12 | `s12b-count` | Kept | | |
| 12 | `s12e-sold` | In the dark staff room, through the window | One street lamp | none |
| 12 | `s12f-kebab` | On the wet pavement across the road | The neon sign | none |

**Thirty-nine new stills and thirteen kept.**

## Choices in this list that are mine

- **Pallets carry "shrink-wrapped blocks of paper",** not the word banknotes, in the new prompts.
  Money and weapons are both reported block triggers; this is a precaution, not a measured block.
- **`s09e-turquoise` has no gun in the prompt** (an arm straight up and plaster dust falling).
  Yesterday a still with three pistols was refused as a start frame for video.
- **`s12d-lowering` does name two small pistols,** because the beat is the guns coming down. It is
  the one most likely to be refused.
- **Words in the picture** are asked for only where the shot is the words: the two placards
  (`s08a`), the SOLD board (`s12e`) and the neon sign (`s12f`). The two headlines in scene 5 are
  not in any still and go on afterwards.
- **The scene 4 cards are in the film's look,** not an 80s look. The freeze, the chrome lettering
  and any video-tape treatment are added after.
- **The empty saucer** (scene 1) has no still. It set up the ending that was cut.

## What came back

**All thirty-nine were made, every one first time, with no refusals** (including the still with
two pistols). 1376×768, in `images\scenes-v3\`, with five contact sheets (`00-contact-sheet-1.jpg`
to `-5.jpg`). **My reading from contact sheets; Jack has not reviewed them.**

**The cast held again.** Each Character is recognisably the same person as in the second pass,
from below, from above and close up.

**The fix to the tool:** the hand-casting script chose the wrong browser tab (a second Flow tab was
open on the home page), so the first attempt timed out looking for the prompt box.
`cast-many-v4.mjs` picks the tab that is on a `/project/` page.

### Five were redone

First versions are in `scenes-v3\replaced\` as `<id>-r1.jpg`.

| Still | What was wrong | What changed in the prompt | Result |
| --- | --- | --- | --- |
| `s12f-kebab` | The sign read "badcoode": a dim extra ring beside the red o | "exactly seven round lowercase letters"; each letter listed; "There is only one o"; the "one letter dimmer as if flickering" line removed | Reads `badcode`, six white letters and a solid red o |
| `s01b-remote` | The hand with the remote looked like somebody else's | The Proprietor "has stretched his other arm out toward the lens... the arm clearly runs back to his own shoulder" | It is plainly his arm. Asked for by Jack ("fix them") |
| `s05c-red-side` | Price tags in dollars ("$250,000", "$300k"), and a small standing figure in the street | "handwritten in British pounds and... too small and soft to read"; "The cardboard street between them is empty" | Pound signs, empty street, stronger blue and red |
| `s08c-megaphones` | It came back on an empty road with flags and no crowd or town | A crowd named behind each barrier, shop fronts, the bank closing the far end | Two crowds, the empty strip, the bank at the end of it. More symmetrical than the rest |
| `s11c-keys` | The carrier bag had garbled shop lettering on it | "a heavy plain white carrier bag with nothing printed on it" | Plain bag |

**What the kebab sign taught:** asking for one letter to look as if it was flickering produced an
extra letter. The flicker belongs in the clip, not the still. Spelling a short word out letter by
letter, with the count, fixed it in one go (n=1).

### Rulings from Jack after the first look (7 October 2026)

- **`s04d-governor`:** the nameplate reading THE GOVERNOR stays. "This is funnier."
- **`s12f-kebab`, third version:** Jack sent a photograph of an old boxed neon takeaway sign that
  sticks out from the wall, and asked for the sign to be "outside of the shop, like a sign instead
  of on the storefront... hanging off of it". The photograph was not uploaded to Flow (it is a
  watermarked stock picture); it was described: a deep dark-blue metal box on a steel bracket, a
  row of bare bulbs along the top and bottom, looping hand-bent neon like handwriting, and OPEN in
  red down the side face. It came back as a box sign with bulbs, `badcode` in white script with a
  solid red o, and OPEN on the end. **It sits above the shop front more than it hangs out over the
  pavement.** The second version is `replaced\s12f-kebab-r2.jpg`.

### Still not right, left for Jack to judge

| Still | What |
| --- | --- |
| `s04c-donor` | Bright, centred and clean against a white wall. The least like the rest of the set |
| `s08a-placards` | Both signs read WE CAN'T AFFORD TO LIVE HERE in full, with nothing hidden below. The joke that the last line differs is not in the picture |
| `s09e-turquoise` | With no gun in the prompt, his raised arm reads as a wave |
| `s09c-pallet` | A plain sky and a tidy load. Reads a little like a stock photograph |
| `s12d-lowering` | Mr Red's free hand is large and reaching toward the lens for no reason |
| `s11d-pricetags` | The tag caught mid-flip does not read as flipping |
| `s05b-blue-side` | The price tags are legible and say "Price £1.50", which is wrong for houses |

### Not made

- No still for the two headlines in scene 5 (they are lettering, added afterwards).
- No still with all eleven at once. The most named faces in any still is four, as before.
