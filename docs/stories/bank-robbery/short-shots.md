# The Bank Robbery short — shots, clips and voices (15 October 2026)

**Asked for by Jack, 15 October 2026:** "do all of it … go ahead and do everything on the list that needs doing to
make this film. save everything." Script: [`short.md`](./short.md) (agreed). Every pick below is mine; Jack has
seen none of it.

- **Flow project:** `63d22c4b` (the Bank Robbery production project).
- **Stills:** Nano Banana 2 (the picker shows "Nano Banana 2.1"), 16:9, one take each. Prompts:
  [`scripts/bank-robbery/brs-stills.json`](../../../scripts/bank-robbery/brs-stills.json), runner `brs-stills.mjs`.
  Files: `images\short\`.
- **Clips:** Omni 1.1 Flash, 720p, 8 s, one take; talking clips in Ingredients with the speaker's Character, silent
  ones in Frames. Prompts: [`brs-clips.json`](../../../scripts/bank-robbery/brs-clips.json), runner `brs-clips.mjs`.
  Files: `vids\short\`.
- **Narrator:** the cut 9 voice (AI Studio, Sadaltager, the Walthamstow deadpan note), two takes a line; take 2 of
  every line was word-perfect on a faster-whisper check and is used. Lines:
  [`brs-narration.json`](../../../scripts/bank-robbery/brs-narration.json). Files: `narrator\short\`.
- **Web pass:** [`docs/google-flow/2026-10-15-bank-robbery-short-sweep.md`](../../google-flow/2026-10-15-bank-robbery-short-sweep.md)
  (thin: nothing changed in Flow since 9 October; most per-shot rules there are inferences). Used from it and from the
  earlier passes: describe the war look rather than name the film; the painting as a restyle of the accepted battle
  still with that still as the only reference; exact short text in quotes, large; the camera locked in every clip
  and the moves done afterwards; "sharp in every frame, no motion blur, normal speed"; price changes as ffmpeg text.
- **Cinematography** (`shot-craft`, `docs/cinematography/`, Jack's standing notes for this film): a camera position
  named as a place for every shot, something out of focus in the foreground, two lights of different colours named,
  saturated colours named, no eye-level-from-across-the-room shots, the hard part of any action already done in the
  first frame (hand already in the jar, cloth already on the counter).

## New cast: Barry

A Flow Character with a Portrait, a Body and a custom Voice, made 15 October 2026 in project `63d22c4b`:
`491aad1f-3e8f-4b07-b03c-b4b552edfda3`. Jack's brief: "typical hi vis working class bald bloke".

- **Portrait:** candidate b of two (`images\characters\13-barry-b.jpg`; picked copy `picked\barry-portrait.jpg`),
  the cast-portrait template from [`characters/cast-portraits.md`](./characters/cast-portraits.md).
- **Body:** made from the portrait with the cast's body template (`picked\barry-body.jpg`).
- **Voice:** preset Alnilam, saved as **`Barry BRS voice`**: "A working man of about fifty from a town in the
  south-east of England, a builder in a hi-vis jacket. Blunt, gruff and fed up, in short flat sentences, with a dry
  laugh at his own bad luck. A plain working-class English accent. Speaking to people in the room, not performing."
- 🔴 **Found on the first café still:** with only the Character cast, Barry came out in a dark jacket twice. The
  Character binds the face, not the hi-vis. **Fix that worked:** also attach his uploaded portrait
  (`brs-barry-portrait`) as a reference and say "Barry is dressed exactly as in his portrait reference", which
  names no garment. The Character's info note would be the cleaner place, but the MCP cannot set it on the rebuilt
  Flow (`FLOW_REBUILD_UNMAPPED`).

## The shots

| Still | Beat | Job | Camera and light |
| --- | --- | --- | --- |
| `d01-dunkirk` | 1 | The war, loud and real, so the painting lands | At the waterline, spray on the lens; overcast white sky against an orange fire glow |
| `d02-painting` | 2 | The same frame as a car-boot oil painting, for the match cut | Flat on, the canvas filling the frame |
| `c01-cafe-wide` | 3, 26 | The reveal: it's on a café wall, and these two live under it | Low on the next table, a sauce bottle in front; blue window light against a yellow strip light |
| `c02-barry` | 4, 6, 8 | Barry's three lines | Across the table at table height, a mug rim in front |
| `c03-denise` | 5, 7, 9, 25 | Denise's four lines | Low at counter height, the tea urn in front |
| `c04-fredo10` | 10 | The Fredo at 10p (the plant) | At counter height beside the jar; hand already in it |
| `c05-window-bank` | 11 | Out of the window to the third culprit; barriers going up for tomorrow | From inside through the steamed glass |
| `p01-press` | 12 | The planners, no masks, printing money | Low on the floor in a corner, the press wheel in front; one bulb and a green exit sign |
| `p02-ex`, `p03-red`, `p04-donor` | 13 to 16 | One speaker a still | Table height, a glass or bottle in front |
| `r01-barry-sign`, `r01b-woman-sign` | 17 | Both sides holding the same sign | Low in the gap, tilted opposite ways; the riot look (`br5-riot-look`) |
| `r02-red-megaphone` | 17 | Mr Red's chant, aimed at Barry | Low in the crowd, a hi-vis shoulder in front |
| `r04-denise-window` | 19 | Denise watching from the café | From the street through the glass, the protest reflected on it |
| `e01-estate` | 23 | The window whose prices double | Straight on; six blank strips, prices put on in ffmpeg |
| `e02-donor-keys` | 23 | Who gains | Low on the kerb; shop light against a street lamp |
| `f02-fredo20` | 24 | The Fredo at 20p (the payoff) | The same set-up as `c04` |
| `s01-sink` | 27 | The one straight beat | Low by the draining board; one bulb against blue street light |

**Reused from cut 10:** the two megaphones ("whose fault it is"), the pallet walk, the vault ("You're putting it in?
/ Count it in the morning") and the `badcode` kebab neon.

## What came back

**Stills (19, plus three retakes), read by eye at full size. No refusals.**

- **First take kept:** `d01-dunkirk` (drained, spray on the lens, the rust sail, a dive bomber; the water is knee
  deep, not waist deep), `d02-painting` (the same composition exactly, cracked varnish: the match cut works),
  `c02`, `c03`, `c04-fredo10` ("FREDOS 10p" readable), `c05`, all four back-room stills (Mr Red on the left as
  asked), both sign stills (WE CAN'T AFFORD TO LIVE HERE readable on both), `r02`, `r04`, `e02`, `f02-fredo20`
  ("FREDO'S 20p", with an apostrophe the 10p card does not have).
- **`c01-cafe-wide`, third take.** Takes 1 and 2 lost Barry's hi-vis (see Barry, above). Take 3, with his portrait
  attached, has it. The painting hangs big above them.
- **`e01-estate`:** no blank price strips came back, but each card has a white margin under its photo, which takes
  the ffmpeg prices.
- **`s01-sink`, second take.** Take 1's letter was too small to read; take 2 is over her shoulder with the letter
  filling the right half: NOTICE OF RENT INCREASE, £2,400 a month circled in red. Its small print is gibberish and
  too small to matter.
- Earlier takes are kept beside the picks as `-take1`, `-take2`.

**Clips (24), Omni 1.1 Flash, about a minute each.** 23 first time; Denise's landlord line timed out once and came
back on a plain retry. Every talking clip says its scripted words (faster-whisper, checked one by one). One extra:
"Bloody landlord" came back with "She still lives with you" after it, cut out in the edit. Frames read at about
two a second on the Dunkirk and café clips, and at one every 1.5 s across the whole cut: no morphing seen. 🔴 **No
human has heard any of the voices.** Accents are unjudged; a machine has only checked the words.

## Cut 1 (15 October 2026)

**Premiere sequence `bank robbery short - cut 1`**, 1:53 (113.0 s), in `bank robbery.prproj` (cut 10 untouched).
Bin `short cut 1`. **Tracks:** V1 and A1, 31 pieces with their own sound; A2, 8 narrator lines; A3 and A4, five
lofi cues pre-ducked under every line. Saved.

- **Render to watch:** `renders\bank robbery short - cut 1-20261015.mp4` (the delivery file: limited range,
  BT.709 tags, −14.8 LUFS, true peak −1.2 dBFS). The ffmpeg preview is `clips\short\preview-short.mp4`.
- **Rebuild:** `python3 scripts/bank-robbery/build-short.py --preview` (pieces, music stems, `edl-short.json`,
  `edl-short.txt`; word times cached in `words-short.json`). Premiere placement: one overwrite action per piece
  from `edl-short.json`, in batches of twelve (`docs/premiere/recipes.md`, "lay down a whole cut from a plan").
- **The reveal** (0 to 10.4 s) is one made piece: the Dunkirk clip, drained, grain and a hand-held jolt in
  ffmpeg, pushing in on the soldier's face; a dissolve into the painting at the same zoom; the painting pulls back;
  a dissolve into the café clip cropped to the painting on the wall, which pulls back to the whole room.
  Narrator over the push-in and the pull-out.
- **The prices** are ffmpeg text in the white margins of the six cards, doubling on a one-frame flash.
- **Inside-line pauses longer than 0.55 s are closed** to a jump cut on the locked camera, except "Your daughter's
  right. / She still lives with you.", where the pause is the joke.
- **Verified against the script:** the whole render transcribed; every line present, in order, word for word.

**Delivery check** (`scripts/delivery-qc.sh`): 7 ok, 1 warn, 1 fail. 🟡 The fail is the absolute-minimum luma
test: 123 of 2,712 frames carry single pixels outside 16–235, which is the encoder ringing on the grain (mostly
the Dunkirk shot), not the picture; every frame's 10th and 90th percentiles are inside. The warn is one held
stretch (the café wide under the last narrator line).

### 🔴 For Jack

1. **Length: 1:53, not the ~75 s the script estimated.** The spoken lines take that long at natural pace; nothing
   is padded. To get to ~75 s something has to go. Candidates, biggest first: the café wide under "no law for
   that one, mate" (9 s, could ride over the sink shot instead); the reveal (10.4 s, could lose 2); Denise's long
   landlord line (7 s); the back-room wide under "This lot don't wear masks" (4.6 s).
2. **Voices and accents:** only a machine has listened. Barry's voice is new (`Barry BRS voice`).
3. **Music:** cut 10's lofi cues, one per scene (HoliznaCC0, CC0). The battle has none.
4. **Owed:** the music credit on screen if HoliznaCC0 is credited (CC0 does not require it); Kai has not seen the
   Dunkirk opening or the chant in context.
