# The Bank Robbery — eighth-pass shots (9 October 2026)

**Asked for by Jack, 9 October 2026,** after cut 7. His notes and the diagnosis are in
[`review-cut7.md`](./review-cut7.md). In short: every shot he called slop asked the video model for a move it
cannot do, and the prompts themselves ordered grey. This pass designs round the moves and names the colour.

- **Settings, stills:** Flow project `63d22c4b`, Nano Banana 2, 16:9, one candidate each.
- **Settings, clips:** Omni 1.1 Flash, 720p, 8 s, one take. Talking clips in Ingredients with the speaker's
  Character (and every other visible Character); silent clips in Frames.
- **Prompts:** [`scripts/bank-robbery/br-stills-v8.json`](../../../scripts/bank-robbery/br-stills-v8.json) and
  [`br-clips-v8.json`](../../../scripts/bank-robbery/br-clips-v8.json). Stills average 115 words (cut 7: 244);
  clips average 59 (cut 7: 120).
- **Files:** `images\scenes-v8\`, `vids\v8\`.
- **References:** two new masters, uploaded to the project as **`br8-hall`** and **`br8-strongroom`**; the riot
  still uses `br5-riot-look` as before.
- **Spoken outside Flow:** `scripts/bank-robbery/br-tts-v8.py` (the panel's question, the guard's question, and
  narrator line 29 in Jack's wording).

## The two places

| Master | What it is | Colour and light |
| --- | --- | --- |
| `s10-00-hall` | The banking hall at night, low and wide | Black and cream chequered floor, mahogany, oxblood columns, brass. **Green banker's lamps against pink flare smoke from the doors** |
| `s11-00-strongroom` | A brick basement with a green iron strongroom door (replaces the steel vault) | Cream gloss brick, oxblood floor, a red fire bucket. **One tungsten lamp against a green glow from the stairs** |

## The design of each shot

| Shot | Job | Camera | How it avoids the thing that broke last time |
| --- | --- | --- | --- |
| `s09d-door3` | The crew arrive, masked | On the floor inside the doors, tilted | The masks are already on; they stand, the smoke moves |
| `s09e-turquoise2` | He fires at the ceiling and checks his phone | On the floor, steeply up | The pistol is in his raised hand in the first frame; only dust and a thumb move |
| `s10a-enter2` | Denise walks in on a robbery | Behind her, at hip height | Her face is not in the shot; the men are masked |
| `s10-hoover2` | She hoovers round them | Lens on the floor | Shoes planted, cut off at the knee; one object moves |
| `s10e-bleach2` | "Shift." | On the counter, bleach bottle in the foreground | The cloth is already under her glove; nobody touches the bottle |
| `s10d-looking2` | The only one looking at the money | Close, below her eye line | Chest-up, lips closed, in the hall and not the old vault corridor |
| `s08j-phones` | Every phone is on a neighbour | In the crowd, behind raised arms | No faces; the pallet is out of focus behind |
| `s06-nose` | "Thirteen years! / Fourteen!" | Chest height, nose to nose | A two-shot big enough for Ingredients to keep both faces |
| `s11a-drill2` | He is working very hard at a door | Pressed to the door, along its paint | The bit is already on the door; his face fills half the frame |
| `s11c-why2` | "Why am I drilling?" | Low, knees up | Drill hanging, goggles up |
| `s11d-better2` | "It looks better." | Waist height, up | The key is already in his hand, held still |
| `s11b-key2` | It opens with a key | Macro on the brass plate | The key is already in the lock |
| `s11h-open` | He looks at the drill | From inside the dark strongroom | One small move |
| `s11e-in2` | "You're putting it in?" | Behind the guard's shoulder | He is not a Character, so his back is to us and the line is spoken in |
| `s11f-count2` | "Count it in the morning." | On a shelf, between two stacks | Chest-up, one pat |
| `s11g-full` | The strongroom full, under "there isn't a crime number for that" | On the floor inside | One rigid thing moves: the door |

**The gate (`shot-craft`, gate 2).** The hall shots show the crew small, daft and in the cleaner's way; the
strongroom is a shabby basement with a mop in it. Nothing is built to make the bank or the crew look good.

## Results

**Stills:** eighteen, all first time, no refusal. 🟡 The strongroom stills came back with a rounded film-frame
border (the master has one); it is cropped off in the cut (`CROP` in `build-cut8.py`). A future master should be
re-made without it.

**Clips:** twenty-four asked for, twenty-four came back; two re-rolled.

| What | Result |
| --- | --- |
| Twelve talking clips in Ingredients | All came back with the line complete and one voice. Framing kept in eight. **Re-staged in four:** `s03a-ex` (wider, the Ex small), `s11c-why2` (wider), `s06-names` and `s06-thirteen` (a different room; both re-rolled once and then stayed in the garage) |
| 🟢 `s09e-turquoise2`, a pistol pointed at the ceiling | **Not refused**, first time, as a still and as a Frames clip |
| Twelve silent clips in Frames | Read at two frames a second: no prop changes shape, no face breaks, the masks stay on, the shoes stay planted, the bottle stays a bottle |
| 🟡 `s08j-phones` | In the last two seconds the pallet comes right up to the lens. The cut uses the first 5.6 s, slowed |
| 🟡 `s11g-full` | The clip moved to a wider view than its still; the door closes cleanly |

What became of each in the cut is in [`assembly.md`](./assembly.md), "Cut 8".
