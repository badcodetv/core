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

## Cut 4 (18 October 2026)

**Jack, on cut 3:** "the painting that changes works, need to trim down the ww2 footage, it is too long and has too much dead
air, the painting changes into the old one and the setting does not remain consistant with barry and denise so we need to
change that ... barry pulls out a twix not a freddo ... the clip at 52 seconds needs to change the drop in the puddle looks
like ai slop alonside the random camera appearing on the bank ... printing money part looks unrealisitc, please find real
footage of that happeing and use it as a refenece image ... the door closing at 1 mins 40 secs looks unrealistic and ai slop
... 1 min 44 secs looks unrealistic please fix it. we need to show them putting the printed money in the bank. 2 mins 3
secs, please make this look better. please watch and listen to it and suggest improvements or make obvoius fixes."

- **Render to watch:** `renders\bank robbery short - cut 4-20261018.mp4` (2:18.6, 138.6 s). Premiere: `bank robbery short - cut 4`
  (bin `short cut 4`; V1/A1 33 pieces, A2 10 narrator lines at +2 dB, A3 14 dubs at +4 dB (the last two +6, the crowd tail 0),
  A4/A5 five music cues; every start checked against `edl-short4.json` from the state file, no gaps). Saved.
- **Rebuild:** `python3 scripts/bank-robbery/build-short4.py --preview` (pieces in `clips\short4\`, plan `edl-short4.json` / `.txt`).
  Prompts: [`brs4-stills.json`](../../../scripts/bank-robbery/brs4-stills.json), [`brs4-clips.json`](../../../scripts/bank-robbery/brs4-clips.json),
  [`brs4-print-stills.json`](../../../scripts/bank-robbery/brs4-print-stills.json), [`brs4-print-clips.json`](../../../scripts/bank-robbery/brs4-print-clips.json);
  runners `brs4-clips.mjs`, `brs4-print-clips.mjs`; the slot window `slot4.py`. 12 stills (Nano Banana 2; the picker reads "2.1"),
  19 clips (Omni 1.1 Flash), project `63d22c4b`. Room references uploaded as `brs4-cafe-room` (the cut 3 café wide),
  `brs4-vault-room` (`s11g-full`), `brs4-press-ref` (a frame of the ECB film) and the three old press stills.

| Jack's note | Done |
| --- | --- |
| WW2 archive too long, dead air | Four shots cut to their action, 12.2 s → 5.9 s; the archive was silent, so the old Flow Dunkirk clip's battle sound (gunfire, a dive bomber) now runs under it and into the painting. Narrator line moved up to 0.6 s. Reveal 8.2 s → 6.6 s |
| The painting changes into the old one; the setting doesn't stay with Barry and Denise | Barry (`c02n-barry`) and Denise (`c03n-denise`) re-shot with the café wide as the room reference: the same tiles, window and the desert-soldier painting behind them in every café shot. All seven talking clips re-made from them |
| A Twix, not a Freddo | `c04n-freddo10` / `f02n-freddo20`: a jar of real Cadbury Freddos (the frog on the purple wrapper, thumb-sized), the card spelled FREDDO'S (cut 3's said FREDOS). The 20p card crosses out the old price |
| 0:52, the puddle drop and the camera | `b01n-bank`: the bank across the road seen from inside the café through the steamed window, Barry eating in the window seat with his back to it ("Neither of them is looking at the bank"). Rain on the glass, nothing else moves |
| Printing looks unrealistic: use real footage | Two real inserts from the ECB's own film of the EUR20 being printed (purple ink into the press duct, the magenta roller; no currency in frame), credited on screen: **"Footage: ECB euro, CC BY 3.0"**. Then the brick room re-made around a real modern sheet-fed press, the ECB frame as its reference: the wide (`p05`), The Ex (`p06`), Mr Red and Mr Blue (`p07`); sheets of purple £20s on the delivery pallet. The deposit reveal pushes in on the stack |
| 1:40, the door closing | `s01n-side-door`: a plain grey fire door a hand's width ajar down a service alley, warm light in the gap, a parked pallet truck, rain. Only the clip's second half is used: in its first 3 s the door opens wider with a figure in it |
| 1:44 (the key in the green door) and "show them putting the money in" | The key and the pallet shots are out. In: `v1-deposit-wide` (Mr Blue slides a brick of new £20s onto the last gap on the vault shelf, Mr Red ticks his clipboard) and `v2-deposit-close` (hands with a signet ring press a brick of £50s home), then the full vault as before |
| 2:03, the slot machine | A new plate (`e01n-estate`: three cards behind wet glass at a sharp angle, street lamps in the reflections). Each price is a fruit-machine reel warped onto its card in perspective (OpenCV): it spins with motion blur, eases to a stop on double, one after another, a flash as the last lands. Same clicks, dings and bell |

**Obvious fixes, mine (from watching and the listening model, `docs/listening/log/2026-10-18-131640-cut3.md`):**
the crowd's roar now dies away under Denise instead of stopping dead; the side door's rain fades out instead of cutting to
the vault; the dubbed voices are 2 dB up and the last two (heard thin) 4 dB up; the mix is normalised to −14 LUFS (it was
−12.5 with peaks at −0.1 before the fix); the file carries BT.709 tags and is squeezed to limited range.

**Learned:** Ingredients mode treats the still as a suggestion, not a frame. Two of nine café clips came back in a different
room (one built a TV because the prompt mentioned one). Since every talking clip is now muted and dubbed, they can go through
**Frames mode**, which holds the composition; the accent drift that kept speech out of Frames no longer matters.

**Checked.** Every clip read at 2 frames a second; the whole render transcribed against the script (every line present, in
order; the TTS "At least something's still cheap" transcribes as "Are these samplings still cheap", the same take as cut 3);
the listening model on the final mix (battle sound under the first line, no dead air, dubs level with the narrator).
Delivery check: −14.7 LUFS, true peak −1.4 (ok); 1 fail, the same stray-pixel fail as cuts 1 to 3 (the 10th-percentile black
sits near 35; 300 of 3,328 frames carry single pixels under 16, grain and encoder ringing, not crushed picture).

### 🔴 For Jack

1. **2:18.** Down 8 s. Still over the two-minute aim; the cheapest cuts left are the café wide under the last narrator line
   (9 s) and the Donor's keys (8.7 s).
2. **The ECB credit** is burned into the two inserts (bottom left). The ECB has its own rules on reproducing euro banknotes;
   none is in frame, but the rules were not read.
3. **Barry's "Another boat last night" clip** was made in Frames mode with no line in the prompt, so his mouth moves to
   unrelated words under the dub. Check it reads.
4. **Mr Red's glasses** come and go between his shots, as before.
5. **No human has heard any voice.**

## Cut 5 (18 October 2026, later)

**Jack:** "some of the audio cuts off early, please listen and fix it, also put trasitions that fit and make it look
cinematic, so it is not only hard cuts." Plus the composite test: "Barry on a real street, or Denise outside a real café ...
put them at the end of the film so they are easily deletable."

- **Render to watch:** `renders\bank robbery short - cut 5 + composite test-20261018.mp4` (2:31: the film 2:19, 1 s black,
  then the two tests). The film alone: `renders\bank robbery short - cut 5-20261018.mp4`. Premiere: `bank robbery short - cut 5`
  (V1 45 pieces incl. 12 transition segments; the tests at 139.125 s, bin `short cut 5 - composite test`; cut 4 untouched). Saved.
- **Rebuild:** `python3 scripts/bank-robbery/build-short5.py --preview`; the test: `scripts/bank-robbery/composite.py`.

**What was cutting off, as measured** (listening model `docs/listening/log/2026-10-18-142552-cut4.md` and `-143046-cut5.md`, then by level):

| Where | Cause | Fix |
| --- | --- | --- |
| Start of "Nine hundred quid", "Another boat" | The TTS slices were cut on the transcriber's word times, which put Barry's first word 0.6 s late | Slices now follow the take's own sound (silencedetect). Every dub also lost up to 0.5 s of leading silence, so the voices sit on the mouths 0.3–0.5 s earlier than in cut 4 |
| Ends of nine lines in Premiere | Dubs placed at the stretched length, 0.1–0.25 s shorter than the file | Placed at the whole file length |
| 0:07.8, the battle stops dead | The Dunkirk sound file is 8 s long and ran out under the painting | The tail is the file's last 4 s, fading over 2.2 s into the café sound, which comes in earlier |
| 1:26.8, the crowd stops mid-shout | The shouted lines ended with no decay | An outdoor echo rings off each shout and fades over 1.8 s; the roar under Denise is louder and dies over 3.3 s |
| Music hand-overs | 0.8 s fades | 1.5 s crossfades between cues |

Re-listened: no speech cut-offs left; the quietest point at 0:08 is −30 dB (was −45). Transcribed: every line present.
−15.0 LUFS, true peak −1.3. The same stray-pixel delivery fail as before.

**Transitions (12).** Dissolves where the film changes place or time; dips to black going inside or to the end; hard cuts
kept inside the café conversation, the protest and the vault, and on the slot → 20p Freddo joke. Each one is centred on
the cut and made from the clips' own frames past the cut, so no line moves: Freddo → bank window (0.5 s), café → printing
(dip, 0.75), real press → made room (0.5), reveal → front pages (dip, 0.5), front pages → crowd (0.42), crowd → Denise
(0.67), Denise → side door (0.67), side door → vault (dip, 0.5), vault → the Donor (0.75), keys → window (0.42), café →
sink (0.83), sink → kebab shop (dip, 0.83). The film fades out at the end (render only; the Premiere sequence ends on a cut).

### The composite test (real plate, AI person)

Method: a frame of the real footage as the reference image in Nano Banana 2 with the Character added ("keep the reference
photograph exactly as it is ... add Barry"), animated in Frames mode with the camera locked, then the person cut out of
every frame (rembg `u2net_human_seg`, local, free, venv `~/.cache/badcode-matte/venv`), the edge steadied over time, the
colour pulled a third of the way to the plate, grain added, and laid over the real footage. Every background pixel is real.

- `k01`: Barry on a real Ealing street at dusk (6 s); the traffic, the lamps and the restaurant behind him are real.
- `k02`: Denise in front of a real shop front (5 s); the customers in the doorway are real.
- 🔴 **Both plates are Pexels and must not ship.** Pexels' terms (read 2026-10-18) bar use "in connection with any political
  party or viewpoint". No free (PD/CC0/CC-BY) British street plate with a locked camera was found on Commons. For real use:
  film our own plate (a tripod and 15 s on any high street), which we would own outright. Details in
  `docs/video-fx/footage-sources.md`, 2026-10-18.
- Nano Banana kept the plate's background almost pixel for pixel and lit the person for it; the cut-out edge held with no
  boiling. Not tested: a person touching the scene, a moving camera, a full figure with a shadow.

### The real-café test (2026-10-18, after the composite test)

Jack on the composite test: the shots "looked completely out of place in the new cut". He asked for a real greasy-spoon
café found online, used as a **reference image in Flow** (not composited), made to look real, and placed right after
the old tests.

**Why the old tests failed.** They kept the plate's flat phone-video look and an eye-level, centred camera, and the
characters stood looking at the lens like a cut-out. None of that matches the film's 35mm look, its low angles or
its single light source.

**The real places.** Both are 🟢 CC0 on Wikimedia Commons, by User:Onthewings, and both are Brighton cafés:

- **Kitchen Cafe:** `File:Interior of Kitchen Cafe 2025-01-29.jpg`, sha256 `42a93275…`.
- **Café Belchers:** `File:Interior of Café Belchers 2023-07-24.jpg`, sha256 `7e1e2b9a…`.

The originals are in `clips/short4/real-cafe/`, cropped to 16:9 as the Flow refs `brs4-real-kitchen` and
`brs4-real-belchers`.

No free greasy-spoon *video* was found:

- Commons video is talks and short films.
- Pexels and Pixabay bar political use.
- Coverr's café clips are modern coffee shops.

A frame is all Flow needs anyway.

**The method.**

1. Stills from `brs4-real-stills.json` (Nano Banana 2), each the real photo first plus the Character.
2. The prompt says "same café as the reference photograph, from the same camera position", gives one mid-action pose
   and names one light source, and ends with the film's own line: "Unretouched 35mm film still, rich saturated colour,
   fine grain, a little underexposed."
3. Clips from `brs4-real-clips.json` / `brs4-real-clips.mjs` (Omni Flash, Frames mode, locked camera, sound effects
   only, no dialogue).
4. Pieces cut to 6.5 s with grain, a slight vignette and fades; room tone lifted to about −26 LUFS.

**The shots.**

- `k03-barry-caff`: Barry at a table at Kitchen Cafe, eating and turning a page. The room held almost pixel for pixel.
  🟡 The plate of breakfast fades into the newspaper by about 4 s.
- `k04-denise-caff`: Denise behind Belchers' counter, a tea towel on her shoulder, a sigh and a blink. The room held.
  She is small in the frame (a wide shot).

**Where to watch.**

- Render: `renders\bank robbery short - cut 5 + cafe test-20261018.mp4` (2:44). The new test starts at 2:31.6, after
  0.5 s of black.
- Premiere: `bank robbery short - cut 5`, V1/A1 at 151.125–164.625 s, bin `short cut 5 - cafe test`.

### The real-plate test (2026-10-18): real café footage, only the person is AI

Jack: "please try the real footage approach and try and make it look realistic". This is the composite method again,
on real greasy-spoon footage, with a better compositor.

**The footage.** *The Night Shift: A Look at the People at Beth's Cafe*, a short documentary by Shannon Snider and
Stefanie Malone about Beth's Cafe, a 24-hour greasy spoon on Aurora Avenue, Seattle.

- YouTube `C9daETgW6xI`, 1080p, uploaded by Stefanie Malone (the filmmaker's own channel) on 2013-08-02.
- Licence: 🟡 **CC BY 3.0**, YouTube's "reuse allowed". The file is
  `clips/short4/real-plate/beths-cafe-night-shift-ccby.mp4`, sha256 `64db5cde…`, with the `.info.json` receipt beside it.
- Credit to use: *Footage: "The Night Shift" by Shannon Snider and Stefanie Malone, CC BY 3.0, modified*. It is
  **not on screen yet**.

The search behind it (a subagent plus me): no locked-off, publishable greasy-spoon plate exists.

- Pexels and Pixabay bar political use.
- Mixkit's diner clips are all "Restricted License".
- Coverr's diner clips are AI-generated (`isAiGenerated: true`).
- Commons and Flickr have only SD or vertical phone clips.

Beth's is the only real greasy spoon with a usable licence. yt-dlp 2026.08.19 (fresh venv at `~/.cache/badcode-ytdlp`)
downloads it; an older install got HTTP 403 on every client.

**The method** (`composite2.py`, which adds integration steps to `composite.py`):

1. Nano Banana 2 still from a plate frame ("Keep the reference photograph exactly as it is … Add Denise …").
2. Omni Flash clip in Frames mode.
3. The person cut out with rembg, limited to a box so the AI's redrawn copy of the real cook is ignored.
4. Aligned onto the plate with a homography, then tracked to the plate's handheld drift.
5. The contact shadow taken from the AI frame (AI ÷ plate, darkening only).
6. Black and white points pulled toward the plate, the person's focus matched to the plate's, and a light wrap.
7. One grade over the whole frame: saturation 1.12, contrast 1.04, grain 7, vignette.

Sound is the Flow clip's own effects, because the plate's audio is interview and music.

**The shots.**

- `k05-denise-grill` (plate 43.0–49.5 s): Denise behind the counter, watching the real cook work the grill.
  - The real yellow jug stays in front of her.
  - The cook steps toward the camera and the plate drifts about 130 px; she stays pinned to the counter.
  - Reads as real footage.
- `k06-barry-sign` (plate 2.6–5.6 s, only 3 s): Barry under the real lit sign ("CHICKENS WANTED MUST LAY 12 EGGS PER
  DAY / BETH'S CAFE") at night, looking up.
  - The first clip prompt was refused as "prominent people"; the reworded one passed.

**Risks and gaps.**

- 🔴 **Real, identifiable people.** Beth's staff and customers are in the plates, inside a political satire. That is
  the risk a licence cannot close (footage-sources.md). Fine for a test; to ship, use only frames where nobody real
  is identifiable, or film our own plate.
- 🟡 **Overlap.** Where the real cook passes in front of Denise, she is drawn over him; there is no depth matte.
  Nothing overlaps in this take.

**Where to watch.**

- Render: `renders\bank robbery short - cut 5 + real plate test-20261018.mp4` (2:55). It holds every test in order:
  street 2:20, café 2:31, real plate 2:45.
- Premiere: `bank robbery short - cut 5`, V1/A1 164.625–174.625 s, bin `short cut 5 - real plate test`.
- When this was placed, the street and café tests (140.1–164.6 s) had been removed from the timeline, apparently by
  hand. Their media is still in the bins.

### Real-plate test 2 (2026-10-18): fixing "crazy" and "random sizes"

Jack's verdict: Barry under the sign was "somewhat realistic", Denise at the grill "looks crazy". He wanted characters
that "dont look out of place/random sizes/weird", placed at the end where the tests have been.

**Diagnosis.**

- **k05 (Denise at the grill) fails four ways:**
  - *Size:* the real camera pushes in, so the cook grows from mid-shot to close-up while Denise stays fixed. She was
    tracked to the whole frame, which follows the busiest plane, not her own.
  - *Subject:* the shot is the real cook's shot, so she is an extra standing in it.
  - *Overlap:* she sits close behind a moving person.
  - *Depth:* nothing at her depth gave a size reference.
- **k06 (Barry under the sign) worked because:**
  - the shot is nearly locked off (0.46 px/frame at 480 wide, the steadiest in the film);
  - nothing crosses him;
  - the light on him has a source we can see.
  
  Its remaining tell: he was sharp when the lens is focused on a far sign.

**Fixes** (research: match the horizon and eye line for scale, and match depth of field):

- **Scale by a reference at the same depth.** `k08-denise-pass` uses the counter shot (plate 105.3–108.8 s), where a
  real waitress stands at the same distance. The prompt says "her head is the same size as the waitress's head and
  level with it".
  - The first still reframed the plate. The prompt was re-run with "Do not zoom, crop, reframe or move anything: the
    output must line up pixel for pixel", and it held.
- **Track the person's own depth plane.** `composite2.py` now takes a tracking box, and tracks shift, scale and turn
  only (`estimateAffinePartial2D`). It also takes `BLUR=` for focus.
- **Keep invented props out.** The keep-box is clipped above the counter, because Nano Banana invented a white tub
  that leaked into the cut-out.
- **Barry: over-the-shoulder, out of focus.** `k07-barry-sign2` has him close to the lens and turned away, with a rim
  of sign light, a faint red neon tint and softer than the sign (BLUR=0.6). Turning him away also keeps the face, the
  most AI-looking area, out of the shot.

**Result.**

- k08 Denise matches the waitress's scale, and the real waitress happens to turn and smile toward her.
- k07 reads as a real over-the-shoulder shot.
- The ledger for the prompts is `brs4-beths2-stills.json`, `brs4-beths2b-stills.json` and `brs4-beths2-clips.json`.

**Where to watch.**

- Render: `renders\bank robbery short - cut 5 + real plate test 2-20261018.mp4` (2:27). The film, 1 s of black,
  then k08 at 2:20.1 and k07 at 2:23.6.
- Premiere: `bank robbery short - cut 5`, V1/A1 140.125–147.2 s, straight after the film. Jack had already cleared
  the earlier tests from the timeline.
- 🔴 The real-people risk and the missing on-screen credit still stand (see the previous section).

## Cut 6 (2026-10-18): the printing scene without an AI machine, and the money typed in

Jack: "forget all of this real footage with ai stuff ... with the money printing scenes, what work arounds can we find
that will fix it looking like ai, flow clearly cant do this". Of the options offered, he chose 1+2+3 and 5:

1. the real ECB machine;
2. faces lit by the press;
3. a still montage with heavy press sound;
5. the money typed rather than printed.

**Diagnosis of cut 5's printing** (symptoms.md, "It looks like AI"):

- The AI press was a spotless pastel product render that never visibly ran.
- The notes were lilac blocks.
- Five suits were posed round a centred table, evenly lit, all in focus.
- Only the two real ECB inserts read as real.

**The rule now: Flow never draws the machine.**

- **The machine is only the ECB's real film** (CC BY 3.0, credit burned in): ink into the duct (89.0 s), the
  numbering heads (376.0), sheets flying into the delivery (176.8, blurred, no readable euro). The magenta roller is
  out.
- **The planners are never beside the machine.** They are lit by it: one hard caged work lamp, off frame, which
  the press's arms cut once a beat. The dip in exposure is done in ffmpeg (`flicker()`), in phase with the sound.
- **Two Nano Banana 2 stills for the montage**, each a slow push with the flicker:
  - `m1-glass-press`: whisky on the feed board, ink.
  - `m2-band-brick`: a paper band round a brick of twenties.
- **New talk clips**, Frames mode, muted and dubbed as before:
  - `m3-ex-lamp`: The Ex, low at table height, half his face lit.
  - `m4-red-blue-toast`: Mr Red and Mr Blue from high above the table.
- **The press bed is the ECB film's own machine sound** (67 s on, clean of music and voice by listening), with a low
  thump under each beat.
  - Its beat is 0.49 s, by autocorrelation; the light dips on each thump.
  - The first, all-synthetic bed was heard as "a tight, unvarying loop ... artificial".
  - The bed sits on its own track, A6.
- **Option 5, the key:** `m5-enter-key` (a finger with the signet ring, ink on the tip) presses a key.
  - The press **stops dead on the click**, with a moment of room ring.
  - The music goes silent with it.
  - The narrator's R1 starts in the silence.
  - Then the bank screen (`screen6.py`, code-made, green phosphor) rolls up through the orders of magnitude to
    **£200,000,000,000** and lands **PAID IN** on "This lot are paying it in".
  - No narrator line was added: the picture tells the joke. The fact under it is the Bank of England's 2009 QE
    pamphlet: "no new money will actually be printed".
- **Prompts:** `brs6-print-stills.json`, `brs6-print-clips.json`, runner `brs6-print-clips.mjs`.
  - Built for slop-avoidance: one hard named light, a strange angle, texture and dirt, "a little underexposed", no
    "cinematic"/"8K", referenced Characters never described.

**Checks.**

- Listened: the press reads as a real machine, every line is clear, and the press stops on the click.
- Transcribed: every line of the section is present.
- `delivery-qc.sh`: loudness −14.9 LUFS, true peak −1.2 dB. The same single "limited range" fail as cut 5 (stray
  grain pixels; known).

**Where to watch.**

- Render: `renders\bank robbery short - cut 6-20261018.mp4` (2:19.5). The scene runs 0:48–1:09.
- Premiere: `bank robbery short - cut 6`, bin `short cut 6`, 47 V1 pieces.
  - A2 narrator +2 dB; A3 voices +4 dB (v24/v25 +6, crowd-tail 0); A4/A5 music; A6 the press bed at −2 dB.
- Rebuild: `python3 scripts/bank-robbery/build-short6.py --preview`.

**Open.**

- 🟡 **Story logic:** the money is typed in at R1, yet later the vault scene shows them carrying notes in. It works
  as satire (they do both), but Jack may want the vault beat reframed.
- 🟡 **A draft narrator tag** for the key, if wanted: Jack writes the jokes. Beat brief: *the press was the
  costume; the real thing is one key*.

### Cut 6b (2026-10-18): "this lot print the money then pay it in", and more money

Jack on cut 6: "the narrator should say 'this lot print the money then pay it in' also there is not enough of the money
being printed, there should be more of it".

- **R1 is a new line**, placed whole: *"Most people rob a bank to get money out. This lot print the money... then pay it in."*
  - `nr6-print-pay` (brs-narration6.json): the same voice and director's note (Sadaltager, Walthamstow, deadpan).
  - Three takes; take c chosen for a clean "lot" and a 0.69 s pause after "money". Levelled +2.3 dB under a limiter
    (−12.5 LUFS, peak −0.9).
  - It replaces `nr1-paying-in`.
- **The key's click lands in that pause** (5.15 s into the line). The press stops dead between "print the money" and
  "then pay it in", and the screen lands PAID IN on "pay".
- **More money:** a second montage, 4.8 s, under "Most people rob a bank … print the money":
  - ECB 128.5 s, sheets streaming, hue-shifted to the twenty's purple (only this shot, which is all paper);
  - ECB 142.0 s, a pallet of printed sheets pushed off;
  - Nano Banana still `m7-table-bricks`, a table buried in banded bricks, with the flicker;
  - ECB 330.0 s, a trolley tower of stacks;
  - ECB 515.0 s, bundles shrink-wrapped.
  - A pallet still (`m6`) was rejected twice: first it copied the AI press room, then the stack came out knee-high.
- **Checks:** listened; the wording is exact, the click lands in the pause, and nothing is clipped.
- **Where to watch:**
  - Render: `renders\bank robbery short - cut 6b-20261018.mp4` (2:20). The scene runs 0:48–1:10.
  - Premiere: `bank robbery short - cut 6`, cleared and re-laid from bin `short cut 6b`. The pieces were copied to
    `clips/short6b`, so Premiere reads fresh files.

## Cut 7 (2026-10-19): Jack's four notes on cut 6b

Jack: "at 9 seconds, the camera goes all over the place still, instead of simply zooming out of it revealing the cafe.
20 secs she stops talking but the narrater keeps talking. 26 seconds his phone morphs into a mug, please change it. the two
clips at 1 min 20 secs and 1 mins 24 secs of the people protesting, i want to keep the vibe of it and the camera angles,
however there are a lot of duplicate faces, please diversify both crowds ... please watch and listen to fix a lot of the
problems, but only once you have added the new clips".

| Jack's note | Cause | Done |
| --- | --- | --- |
| 0:09, the camera all over the place | Not the café clip (it is steady). The zoom was centred on the painting, which touches the top of the frame, so the crop was clamped and slid sideways while it shrank | One zoom out about a fixed point (`anchorzoom`): the painting shrinks in place and the room opens round it. Edit only, no new footage |
| 0:20, Denise stops, the voice keeps going | Her mouth says two phrases with a 2 s pause; the dub was one continuous take laid over both | `dubtalk` now cuts the take at its own pauses and lays each phrase on its run of mouth movement. The same fault at 0:28 (`c03b`) and in The Ex's line got the same fix |
| 0:26, the phone morphs into a mug | The start frame had the phone in his hand and the prompt asked him to drink | New still `c02p-barry`: phone already on the table, both hands already round the mug. New clip `c02p-barry7` (Frames, the line in the prompt, no drink). Read at 4 fps: no morph |
| 1:20 / 1:24, duplicate faces | Both stills cast one face over and over | New stills `pr-a7-chant`, `pr-b7c-reply`: each front-row person written as a different individual (clothes, what they carry, one face feature); everyone further back hooded or under umbrellas; **no reference to the old still**. Same camera and light text. The reply took three rounds: take 1 went eye-level and symmetrical, take 2 (camera clause moved first) got the angle but went flat afternoon light, take 3 (after dark, one floodlight) is used |

**Found on the watch-and-listen pass, and fixed:**
- Denise's 0:28 take has a sentence her mouth never says ("Put mine up twice this year"). That sentence now plays over a
  cutaway of Barry listening: the last second of his own new clip at half speed, mouth shut, mug still in his hands.
- The dub takes ranged from −11.7 to −19.7 LUFS, so some lines sank under the music. Every take is now levelled to −16 LUFS
  before it is cut up; the +6 dB special case on the last two lines is gone.
- Barry's new line split in four phrases (one per sentence) after a two-way split crammed 5 s of voice into 2.5 s of mouth.
- Two transition pieces were one video frame short (11 frames of picture, 12 of sound) and left one-frame gaps in Premiere.
  Patched with padded copies (`x-010-fade-p`, `x-027-fade-p`); the builder now renders every transition with a spare frame.

**Checked:** contact sheets of the whole cut at 2 fps; every new clip at 4 fps; a faster-whisper transcript (every line
present, in order); two passes of the listening model (`docs/listening/log/2026-10-19-092736-*`, `-093459-*`; the second
found nothing). Listener claims that measurement disproved: a gap at 0:12–0:16 (none) and a clipped onset at 0:41 (it rises
cleanly). Delivery check: −14.7 LUFS, true peak −1.4; the one fail (full-range content in a limited tag, grain pixels) is
identical on cut 6b.

- **Render:** `renders\bank robbery short - cut 7-20261019.mp4` (2:20.4).
- **Premiere:** `bank robbery short - cut 7` (cut 6 untouched), bin `short cut 7`: V1/A1 54 pieces with no gaps; A2 narrator
  +2 dB; A3 voices +4 dB (crowd tail 0); A4/A5 music; A6 press bed −2 dB; A7 the reply crowd (it overlaps the chant). Saved.
- **Rebuild:** `python3 scripts/bank-robbery/build-short7.py --preview`. Prompts: `brs7-stills.json`, `brs7-clips.json`
  (runner `brs7-clips.mjs`). Stills `images\short7\`, clips `vids\short7\`. Flow project `63d22c4b`, Nano Banana 2, Omni 1.1 Flash.

### 🔴 For Jack

1. **Unwatched by a human.** Only machines have looked and listened.
2. **0:41, "At least something's still cheap"** still sounds a little smeared: the take is slowed to 0.8× to fill the Freddo
   clip's long mouth movement. Playing it at normal speed would leave his mouth moving after the voice stops, which is the
   0:20 fault, so it was left.
3. **The reply crowd:** the security guard's jacket lettering garbles mid-clip, and the lad in the overalls reads young.
4. **The chant and reply crowds are now ethnically and age mixed on both sides.** The cut 6b crowds were all white on both sides.

## Cut 7b (2026-10-19, later): lips, and megaphones

Jack on cut 7: "at 20 secs she speaks but her lips dont move ... the cafe scene is not lip synced correctly, they speak
when their mouths are closed ... the protesters shouting at each other must change it sounds terrible, maybe they use
megaphones and only hear the rest of the crowds background noise, so either side has one megaphone".

**Cause of the lip sync:** every dub since cut 2 was timed to the faster-whisper word times of the Omni clip's **own
audio**, and Omni's speech track does not follow its own picture. Denise's 0:16 clip "says" its second phrase at 5.5 s
while her mouth is shut (checked by eye on a close-up sheet). So the lips are now measured from the picture.

| Jack's note | Done |
| --- | --- |
| 0:20, she speaks and her lips don't move; the café speaks with mouths shut | New `lips.py`: MediaPipe Face Landmarker on a 2x crop round the face (the faces are too small for it at 720p), the inner-lip gap per frame, runs where it keeps changing. New `lipsync()` in the builder: each line opens on its speaker as the lips start; the face stays up while they move; whatever the voice still has to say carries over a cutaway of the listener with a shut mouth (spans read off the same data, each used once), and comes back to the face only if a later lip run can carry a whole sentence. Voices at natural speed (at most 1.15x), so the 0:40 smear is gone |
| The protest sounds terrible | New stills and clips with ONE megaphone a side, held over the mouth from the first frame (`pr-a7m2-chant`, `pr-b7m-reply`; same faces brief, same cameras and light; Barry's sign passed to the woman in pink beside him). One TTS voice a side through the megaphone filter, levelled to −14 LUFS; under it the wide's wordless roar run on backwards, at −5 dB. Omni sang its own chants into both new clips ("We will not be moved!"), so their sound is muted. The chant shot starts at 3.0 s: the police officer in the foreground punches the air at 1.5–2.6 s |

**Measured:** share of voiced time on a face where the lips are moving, cut 7 → cut 7b: Denise 0:16 53% → 80%, 0:28 59% →
79% and 70%, 0:37 66% → 90%; Barry's 10p Freddo 51% → 88%; the rest 69–88%. Mr Red's toast reads 32% in both: it is a high
shot from above with small faces and the tracker is not reliable there.

**Checked:** contact sheets of the café and the protest; a transcript (every line, in order; "At least something's still
cheap" now transcribes correctly); no two voices overlap (sound spans, not file lengths); the listening model on the
protest (`docs/listening/log/2026-10-19-102835-*`: both megaphones intelligible, "skint" clear, crowd wordless). Its first
pass caught the megaphones at −34 LUFS, unheard; fixed. Delivery check: −14.8 LUFS, true peak −1.3; the same one range fail
as cut 6b.

- **Render:** `renders\bank robbery short - cut 7b-20261019.mp4` (2:18.6).
- **Premiere:** `bank robbery short - cut 7b` (cut 7 untouched), bin `short cut 7b`, 65 V1 pieces, no gaps; A2 narrator +2 dB,
  A3 voices and megaphones +4, A6 press −2, A7 crowd −5. Saved.
- **Rebuild:** `python3 scripts/bank-robbery/build-short7.py --preview` (pieces in `clips\short7j`); lip data cached in
  `scripts/bank-robbery/lips-short.json` (`lips.py` needs `~/.cache/badcode-lips/venv` with mediapipe 1.1.1 and
  `face_landmarker.task`).
- **Spare folders:** `clips\short7b` to `short7i` hold abandoned test builds, never imported into Premiere. Safe to delete.

### 🔴 For Jack

1. **More cuts in the café.** Lines now cut to the listener when the speaker's lips stop, so the café has about 16 shots where
   it had 10. If it feels busy, the alternative is new talking clips, which Omni can't promise to lip-sync either.
2. **Barry's side of the protest:** his mouth shows past the megaphone at that angle while he shouts; it is continuous
   shouting, so it reads.
3. **Unwatched by a human.**

## Cut 7c (2026-10-19, evening): why some lines synced and others didn't, and the fix

Jack on cut 7b: "the two clips of barry at 18 and 19 seconds have his lips moving but denise is talking, maybe in shots
where it is easy to lip sync, just show panning shots of the cafe as they are talking. lip syncing is off at 27 secs. for
some clips you have matched the lip syncing perfectly and some are completly messed around, please research ... why ...
56 secs, please remove the flashing black screen thing ... 1 min 14 secs the whole crowd are white people ... when they
put the money in, it looks unrealistic ... make quick cuts".

### Why (measured, n = 11 clips + 7 remakes)

Every cut 4 talking clip was prompted with exactly its dub line, so wording was not the difference. What was: **does the
clip's OWN generated speech say the dub's words, and does it sit on the moving lips?** Scored by MediaPipe lip motion
against faster-whisper on the clip's own audio:

| Group | Clips | Own speech on moving lips |
| --- | --- | --- |
| Synced | `c02p-barry7` (**Frames**), `c02c-barry4`, `m3-ex-lamp`, `m4-red-blue-toast` | 86–100% |
| Not synced | all Denise clips, `c02a`, both Freddo clips (Ingredients) | 45–77%; several said other words ("How much?") |

Re-made in **Frames mode with the exact line**, all seven say the right words; five then pass. When a clip passes, its own
speech is the timing map. Research (`docs/video-fx/2026-10-19-lip-sync-for-dubbed-ai-clips.md`) agrees: match the words,
then align; late audio is far less visible than early (about 125 ms against 45 ms).

### The fix (`build-short7.py`, `dtwsync.py`, `lips.py`)

- **`ownsync()`**: the take is time-warped onto the clip's own speech (MFCC dynamic time warping, cut at the take's quiet
  points, each piece stretched by ffmpeg's rubberband 0.75–1.33x), or shifted and evenly stretched if that matches the
  clip's speech envelope better; the measured audio-to-lips lag on top; a breath of room reverb. Sync score per face shot
  (voice against lip motion): **0.57–0.90**, every one at its best shift ±0.12 s. The clips' own voices score 0.54–0.80.
- **`cafepans()`** for the lines with no passing clip (Denise 0:27, "Bloody landlord"): the line at its own speed over slow
  pans across four new café details with no people (`cd1`–`cd4`: painting, tea urn, empty table, rainy window). The window
  shows the bank, so it comes after the narrator's reveal. No listener cutaways any more, so no moving lips under the
  wrong voice (Jack's 0:18).
- **0:56 flicker**: removed (the press-lamp dip).
- **1:14 wide**: re-made with a mixed crowd (`pr-w7-wide`); Flow refused the first motion prompt ("reputational risk or
  misrepresent current events"), the softer one (no "surge", no "police line braces") went through. The old wide's
  wordless roar plays under it.
- **The vault**: five stills, no faces, 0.8–1.6 s each with a small exact push: the trolley through the vault door, from
  above, gloved hands on the shelf, the packed aisle, the door shutting. Under them the old vault clips' room sound.
- The Ex and Mr Red keep cut 7b's timing (both own-speech searches hit their limits there; Jack didn't flag them).

**Checked:** contact sheets of the café, printing, wide and vault; transcript in order; the listening model
(`docs/listening/log/2026-10-19-113846-*`): no warble, clipping or overlaps in the café, the megaphones clear, no repeats.
Delivery check: −15.2 LUFS, true peak −1.1; the old range fail only.

- **Render:** `renders\bank robbery short - cut 7c-20261019.mp4` (2:22). **Premiere:** `bank robbery short - cut 7c`, bin
  `short cut 7c`, 58 V1 pieces, no gaps. Saved. **Rebuild:** `build-short7.py --preview` (pieces in `clips\short7t`).
- **Spare folders** `clips\short7b`–`short7s`: abandoned test builds, never imported. Safe to delete.

### 🔴 For Jack

1. **Denise's long line (0:27) and "Bloody landlord" are now voice over the café.** Neither of her clips for them passed,
   even re-made. One more Frames re-roll each could put her face back.
2. **Unwatched by a human.**
