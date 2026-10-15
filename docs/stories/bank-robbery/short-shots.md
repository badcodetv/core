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

## Cut 2 (15 October 2026, evening)

**Asked for by Jack, after the meeting:** "Each character in their own voice, as a voice-over. dont change the
videos, just mute the videos and use the https://aistudio.google.com/generate-speech text to speech for each
character as they are talking, with a similar script, use the changes from the transcript, whilst keeping our main
narrator." The plan it follows: [`short.md`](./short.md), "Cut 2".

- **Render to watch:** `renders\bank robbery short - cut 2-20261015.mp4` (2:16, 136.1 s), from ffmpeg.
- **Premiere sequence `bank robbery short - cut 2`** (built later that evening; cut 1 and every other sequence untouched).
  1280×720 @ 24, made from `s-archive.mov`, 136.083 s. Bin `short cut 2` (58 items). **Tracks:** V1/A1 29 pieces with
  their own sound, end to end, no gaps; A2 11 narrator lines; A3 13 dubs; A4 music cues 1, 3, 5 and A5 cues 2, 4.
  Narrator and dub clips at **+2 dB** clip Volume (Level 0.22387), to match the preview; music at 0 dB. Audio is
  placed as whole files, as the preview mixes them (dub files run 0.03 to 0.21 s past the plan's `length`).
  Premiere floors each audio clip to the frame, so a tail of up to 1 frame is lost (ms-01: 42.458 → 42.417 s).
  Placement: pieces by set in/out + overwrite, audio by overwrite, from `edl-short2.json`; every start matches the
  plan to the frame (checked by script over the state file). Frame at 112.5 s checked by eye: the estate agent's
  window with prices. Saved.
- **Rebuild:** `python3 scripts/bank-robbery/build-short2.py --preview` (pieces in `clips\short2\`, the plan in
  `edl-short2.json` / `.txt`, with a dub track beside the narrator and music). Cut 1 and its files are untouched.

**The voices.** Every talking clip is cut 1's picture with its sound **muted**. Each character's line is new
text-to-speech, laid where the mouth moves and stretched toward the clip's own speech (0.8 to 1.25 times).
- Engine: `gemini-3.1-flash-tts-preview`, the model behind AI Studio's generate-speech page, called through the
  API with the same director's-note format (`brs-voices.py`, lines and notes in `brs-voices.json`). Not typed into
  the AI Studio page itself.
- Voices: the same preset as each Flow Character. Barry Alnilam, Denise Gacrux, the Ex Umbriel, Mr Red Achird (and a
  shouting note for the chant), Mr Blue Orus (shouting). The two megaphone lines are filtered to sound like
  megaphones.
- Two takes a line, files in `voices\short2\take1`, `take2`; checked word by word with faster-whisper
  (`words-short2-tts.json`). The pick per line is in `PICK` in the builder: word-perfect first, then the closest
  length. "Least something's still cheap" came back as "**At** least" in both takes; that matches what Barry's
  mouth says in the clip, so it stays.
- **The narrator is unchanged** (Sadaltager, cut 9 note). Four new lines, same voice, `narrator\short2\`:
  A1 "Your grandparents fought the Nazis for this country." (take 2), R1 "Most people rob a bank to get money out.
  This lot are paying it in." (take 2), P1 "Then give both sides something to shout about." (take 1), S1
  "Everyone's watching the front door. Nobody's watching the side one." (take 1). Take 1 of R1 said "there's a lot
  of paying it in"; take 2 of P1 said "share about".

**The meeting's changes, as made.** No new pictures were generated (Jack: "dont change the videos").

| Change | How |
| --- | --- |
| Real WW2 footage first | 10 s: the Dunkirk deck, the pilots' scramble, the Home Guard, St Paul's (`clips\cut5\ww2-0*`, cleared in [`footage-ww2.md`](./footage-ww2.md)), light grain, a low film hiss, line A1 |
| No camera jitter | The reveal rebuilt with the hand-held jolt taken out; the push-in and pull-out are unchanged |
| Sausage roll / the walk into the bank | Gone (the cut 10 pallet walk), with "Left end. Right end. Same pallet." |
| Deposit dialogue | Gone: the Donor's and the Ex's "how much do we take / we put it in", and the vault's "you're putting it in / count it in the morning" |
| The deposit reveal, lingering | R1 over a slow push-in on the press still, held 1.8 s after the line, before the protest |
| Newspaper drops | The two cut 9 front pages ("THEY'RE LETTING THEM IN", "WE DESTROYED THEIR HOMES") under P1 |
| Side door | S1 over the bank across the road (the `c05` window shot, later in the clip). No shot of anyone going in |
| Slot machine | The estate agent's window: old prices, then every card rolls like a reel (a new price every 1/12 s), stopping one by one on exactly double, with ticks, a ding per reel and a jackpot bell; then a hard cut to the 20p Fredo. The Donor and his keys now come first, under "He's just early" |

**Checked.**
- **Transcript of the render against the script:** every line present, in order. Faster-whisper hears Mr Blue's
  megaphone line as "who's bolt it is" (the filter; the raw take was word-perfect) and "bought" as "bolt" once.
- **By eye**, a sheet of 16 frames over the new pieces: the archive, the smooth reveal, the press, both front pages,
  the reels mid-roll and landed (£360,000 … £450,000, each double), the 20p jar.
- **Delivery check:** 6 ok, 3 warn, 1 fail. The fail is the same as cut 1's: 404 of 3,266 frames have single pixels
  below 16 (the grain); no frame's 10th or 90th percentile is outside 16–235. Loudness −15.0 LUFS, true peak −1.2.

### 🔴 For Jack

1. **Length 2:16**, longer than cut 1's 1:53. The additions (archive 10 s, the held reveal 7.3 s, the papers 5.7 s,
   the side door 5 s, the slot machine 3.8 s) outweigh what went. Talk pieces are also continuous now (cut 1 closed
   pauses with jump cuts; a dub cannot follow a jump cut).
2. **Lip sync is approximate.** Each line starts where the mouth starts and is stretched toward its length; four
   lines hit the 1.25x limit (Barry's boat line, the Ex, "Twenty p", "Bloody landlord"), so they may sound quick.
3. **No human has heard any of the new voices.**
4. **The four narrator lines are my drafts.**
5. **Premiere:** done, `bank robbery short - cut 2` (see above). Audio crossfades, if wanted, are by hand.

## Cut 3 (15 October 2026, night)

Jack's notes on cut 2 and the plan: [`short.md`](./short.md), "Cut 3".

- **Render to watch:** `renders\bank robbery short - cut 3-20261015.mp4` (2:26, 146.4 s). Premiere: `bank robbery short - cut 3`.
- **Rebuild:** `python3 scripts/bank-robbery/build-short3.py --preview` (pieces in `clips\short3\`, plan `edl-short3.json` / `.txt`).
- **New pictures:** 10 stills (Nano Banana 2, project `63d22c4b`, `images\short3\`) and 9 clips (Omni 1.1 Flash, `vids\short3\`), prompts in
  [`brs3-stills.json`](../../../scripts/bank-robbery/brs3-stills.json) and [`brs3-clips.json`](../../../scripts/bank-robbery/brs3-clips.json), runner `brs3-clips.mjs`.
  No refusals. `b01-bank` hit "Frames on Omni 1.1 Flash unavailable" once and came back on the retry; so did `c01b-cafe-wide`.
- **Archive:** seven new action cuts ([`footage-ww2-action.md`](./footage-ww2-action.md)); six used: the Stuka over the Dunkirk beach, the
  Alamein advance through wire, the tank through a shell burst, the tank charge, the bayonet charge, and the soldier striding through smoke.
  `wa-06` (a shell bursts between two men and they drop) is left out: it can read as men being hit.

**What changed, as made.**

| Jack's note | Done |
| --- | --- |
| Action archive | 12.2 s of combat, then the ending shot |
| The painting from the end of the footage | The last frame of `wa-end` uploaded (`brs3-archive-end`) and repainted (`a01-painting`). Take 1 gave him a helmet that read German; take 2 asks for the flat British "tin hat" and has it (take 1 kept as `-take1`). The real shot holds its last frame and dissolves into the painting at the same framing |
| Zoom out in the café, no shake | A new café wide with that painting on the wall (`c01b-cafe-wide`, painting reference + Barry and Denise); the zoom starts on the canvas and eases back over 2.6 s. No jolt anywhere |
| The bus at 0:55 | `b01-bank`: the bank at dawn from the wet kerb, barriers in the foreground. Used for its first 4.5 s only: the CCTV camera appears out of nowhere after that |
| Real notes | `p01b-press`, `p02b-ex`, `p03b-red`: same brick room and men (each made from the old still as the only reference), now purple £20 and red £50 polymer notes in slanted stacks |
| The protest | `pr-w-wide` (from the bank's columns: two crowds, a police line, nobody looking up), `pr-a-chant` (four TTS voices together: "Get off our streets, you fucking Nazi bastards!"), `pr-b-reply` (Barry's side, Barry's voice leading three: "We're not Nazis, we're skint, you posh little wankers!", my draft). No politicians, no flags, no coloured smoke. Mr Red's and Mr Blue's megaphones are gone |
| Denise at 1:35 | Kept (`r04-denise-window`, under "only the blame was bought and paid for") |
| The bus at 1:40 | `s01d-side-door`: the side door down the alley, pallet-truck tracks leading in, swinging shut under the side-door line |
| The vault | Back after the side door, muted: the key in the green door (`v8/s11b-key2`), the pallet beside the vault (`v7/s11e-in`), the full vault and the door shut (`v8/s11g-full`) |

**Also changed:** "Three hundred thousand men got off that beach" is **out**. The painting is now a desert soldier, not
Dunkirk, so the beach line no longer matches the picture. The opening reads "Your grandparents fought the Nazis for this
country." … "Their grandkids can't get a one-bed." Jack's call whether to bring it back.

**A bug fixed:** when a shot was asked for more seconds than its clip had, the piece came out short and everything after it
drifted against the voices (cut 2 has this at the Donor's keys, about 1 s, and on the last café wide). The builder now holds
the last frame instead. Every piece of cut 3 was measured against the plan.

**Checked.** Transcribed (all lines present; the shouted crowd lines are only partly readable to the machine, as you'd expect),
word timings spot-checked across the protest, 16 frames read by eye across the new pieces. Delivery check: 6 ok, 3 warn,
1 fail, the same stray-grain-pixel fail as cuts 1 and 2 (now mostly the archive). −14.5 LUFS, true peak −1.5.

### 🔴 For Jack

1. **2:26.** Longer again (the archive is 12 s plus 8 s of painting reveal; the vault adds 8.6 s).
2. **The reply line is my draft.** No human has heard any voice.
3. **The press notes** follow the Bank of England's rules for showing notes by construction (stacks at a slant, portraits small),
   but the portraits are Flow's; check none reads as a distorted King or Queen.
