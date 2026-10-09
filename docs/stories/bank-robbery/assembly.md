# The Bank Robbery — first assembly (7 October 2026)

**Asked for by Jack, 7 October 2026:** "do the narration, then put it all together in premiere."

**This is a first assembly, not a finished cut.** Everything is in script order with the narrator
laid over it. Nobody has watched it at playing speed: it was checked by measurement and by ten
frames from the render.

## The narration

- **32 lines, 3 min 25 s in all,** one WAV per line, in `Desktop\Youtube Vids\animation\bank robbery\narrator\`.
- **Voice:** the Money For Something narrator, as Jack ruled: `gemini-3.1-flash-tts-preview`, voice
  **Zubenelgenubi**, Accent **British (Brixton)**, nothing else. The prompt is word for word the one
  the AI Studio page sent when Jack chose the voice.
- **Words:** [`scripts/bank-robbery/br-narration.json`](../../../scripts/bank-robbery/br-narration.json),
  taken from [`script.md`](./script.md). Runner: `scripts/bank-robbery/br-narration.py` (plain HTTPS;
  the Google SDK is not installed on Jack's machine).
- **One take each, first time.** 🔴 **Nobody has listened.** One take in ten of this voice is reported
  to drift, so each line wants comparing with the reference take
  (`money for something\narrator\NARRATOR-VOICE-reference-zubenelgenubi-brixton.wav`).
- **Two small changes to the words as read:** line 16 ends with a full stop where the script has
  three dots, and line 18 has a full stop where the script has a semicolon.
- **Not written, so not recorded:** scene 2's optional line.
- `narrator\original-full-level\` holds a copy of each file. It was made during a levelling attempt
  that was undone; the files in `narrator\` are identical to those copies.

## Premiere

**Project:** `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/bank robbery.prproj`
**Sequence:** `bank robbery - cut 1` — 1280×720 @ 24, 510.7 s (8 min 30 s)
**Built:** 2026-10-07 by session (bridge). `bank robbery - scenes in order` (yesterday's) is untouched.

| Track | What |
| --- | --- |
| V1 | 86 clips, butted, no gaps |
| A1 | Each picture clip's own sound, same times |
| A2 | The 32 narrator lines |

**Bins:** `01-scenes` (yesterday's silent clips) · `02-clips-v3` (41 of today's clips) ·
`03-cut1-pieces` (38 rendered pieces) · `04-narrator` (32 WAVs).

**The plan the timeline was built from:** `scripts/bank-robbery/edl-cut1.json`, with a readable list
in `scripts/bank-robbery/edl-cut1.txt` (start, length, clip, kind). Rebuild both, and the rendered
pieces, with `python3 scripts/bank-robbery/build-cut1.py`. Each entry was placed by setting the
source in and out on the project item, overwriting onto V1 and A1, and clearing the in and out;
narrator lines went onto A2 whole. Twelve placements an eval, nine evals.

**How the cut was decided (all of it mine, none of it ruled):**

- **A talking clip is trimmed to its speech,** found from the sound level, with 0.8 s before and
  1.1 s after. Where the sound is loud throughout (megaphones, the bell, the hoover) nearly the
  whole clip is used.
- **A narrator line never plays over a talking clip.** It sits over a silent clip, starting 0.4 s
  in, with 0.6 s after it.
- **Where there was no silent clip for a line, a still is held with a slow push** (17 of these,
  `hold-*.mp4`). Where the line runs longer than the 8-second clip, the clip's last frame is frozen
  for the rest (7 of these, `ext-*.mp4`).
- **Scene 4's name cards** are 1.3 s of the clip and then a 1.3 s freeze with the name and job in
  white Impact (`card-*.mp4`). The jobs are the plain ones; Jack's funny tags are not written yet.
  Mr Blue and Mr Red get the old clip of them stopping at the buzzer, then the freeze with an arm
  round each other.
- **Lettering** was added with ffmpeg, since the bridge cannot write text: the title over the bank
  door, THREE WEEKS EARLIER, BANK HOLIDAY MONDAY, and the two headlines in scene 5.

**Applied in Premiere:** one thing. The narrator's 32 clips on A2 have Volume set to −9 dB
(Level 0.0631), because the narrator files measure −13 LUFS and the talking clips about −27.

**Outputs**

- Render: `renders\bank robbery - cut 1-20261007-1659.mp4` (473 MB). The earlier
  `…-1657.mp4` is the same picture with the narrator at full level; it can be deleted.
- Measured on the 1659 render: no black frames except the first third of a second of the two
  title cards; integrated loudness −22.5 LUFS; true peak 0.0 dBFS.
- Ten frames read by eye: the title, both title cards, three name cards, both headlines, the remote
  at the window and the kebab shop. All as intended.

**Needs a human**

- **Watch it.** Nobody has.
- **The voices** in the talking clips (see [`clips-v3.md`](./clips-v3.md), "The voices").
- **The narrator's 32 takes,** by ear.
- **Sound:** A1 jumps from one room to the next at every cut, and holds and frozen frames have no
  sound under the narrator. There is no music, including under the scene 4 montage, which was meant
  to have 80s music. Audio crossfades cannot be added through the bridge.
- **Seven shots freeze on their last frame** and seventeen are held stills. They are the first
  things to replace if they read as cheap.
- **The delivery check fails** (`scripts/delivery-qc.sh`): the render is untagged full range, the
  peak is at 0 dBFS and the loudness is off target. That is expected for an assembly and has to be
  fixed before anything is uploaded.
- **Length:** 8 min 30 s against the seven minutes guessed from the script.

---

# Cut 2 — the tightening pass (8 October 2026)

**Asked for by Jack, 8 October 2026,** after watching cut 1: "it is not that funny… way too long, a lot of dead
air in the clips… the volume clips are too loud when there is narration, there are a lot of video errors and ai
slop elements." The review that led to this cut is [`review-cut1.md`](./review-cut1.md).

**Cut 1 is untouched.** Cut 2 is a new sequence beside it. Every choice below is mine and none is ruled.

## Premiere

**Sequence:** `bank robbery - cut 2` — 1280×720 @ 24, 351.0 s (**5 min 51 s**, was 8 min 30 s)
**Built:** 2026-10-08 by session (bridge): 88 picture clips and 26 narrator lines, nine evals, no failures.

| Track | What |
| --- | --- |
| V1 | 88 clips, butted |
| A1 | The 30 talking pieces only, already levelled |
| A2 | 26 narrator lines, Volume −3 dB |
| A3 | The bed: the sound of every clip that plays under the narrator or with no words, each with its own Volume |

**Bins added:** `05-cut2-pieces` (44 files from `clips\cut2\`). `s08b-remote-window.mp4` and `s11c-keys.mp4`
were added to `02-clips-v3`.

**Rebuild:** `python3 scripts/bank-robbery/build-cut2.py` writes `edl-cut2.json` (entries, narrator, levels) and
the readable `edl-cut2.txt`; `REDO=1` re-renders the talking pieces. Placement was the cut 1 eval, eleven
entries at a time, then one eval for the 26 narrator lines and one transaction for 68 Volume values.

## What changed, and why

- **Pauses inside talking clips are cut out.** Each clip was generated slow (the "long holds" brief), so a
  three-second line sat in eight seconds. Each kept phrase has 0.3 s before it and 0.3 s after (0.6 s after the
  last, so a punchline has room). Alternate phrases are punched in 10 % so the jump reads as a change of shot.
  Rendered to `clips\cut2\c2-t-*.mp4`; the untouched 8 s clips are still in `02-clips-v3`.
- **The narrator runs over moving footage.** Cut 1 had 17 held stills and 7 frozen last frames. Cut 2 has
  10 held stills, none longer than 6.3 s, and no frozen frames. The cover is the unused part of the 8 s clips
  and four old silent clips that cut 1 did not use (`s10-hoover` under "there isn't a crime number for that").
- **The narrator is tighter:** 0.15 s after the cut, 0.35 s between lines, 0.4 s clear at the end.
- **Levels.** Narrator −3 dB. Talking pieces levelled to one loudness in the render (they ranged over 15 dB).
  Bed clips under the narrator sit about 30 dB under him; cut 1 had three that were as loud as he was
  (`s07-night-before`, `s09-walk`, `s12a-standoff`). Bed clips with no words over them are lifted a little.
- **Six narrator lines are out:** n06 (consultancy), n07 (what you came in with), n11 (with the snacks),
  n13 (chocolate fountain), n20 (third side), n23 (nobody films it). The WAVs are still in `04-narrator`.
  n06, n07, n13 and n23 went because the only cover was a long still; n20 repeats n19's joke; n11 went with:
- **Scene 6 is cut to its first joke** ("Why am I Mr Turquoise?" / "Blue was taken."), then straight to
  "Thirteen years! Fourteen!". The establishment / van / reluctantly exchange is out.
- **Scene 2 is 8 s** (was 17.5 s), **the name cards are 1.7 s each** (were 2.6 s), **the ending is 14 s** (was 23 s).
- **Restored:** the panel's "what would you do?" and Denise's "What's all that, then?", both cut off in cut 1.

## Outputs

- Render: `renders\bank robbery - cut 2-20261008-1246.mp4` (325 MB). `…-1245.mp4` is the same cut with four
  single black frames; it can be deleted.
- Measured on the 1246 render: integrated −17.2 LUFS, true peak −1.4 dBFS; no black except the first tenth of
  a second of the two title cards.
- Checked by listening model (Gemini, both halves and then the whole): every cast line present and complete.
  It reports the first "whose fault it is" clipped at its last word where the two megaphones overlap.
- Checked by eye: contact sheets of the preview and two of the Premiere render. **Not watched at speed by anyone.**

## Needs a human

- **Watch it.**
- **Music. There is none,** and it is the largest thing missing: the name-card montage is 19 s of near
  silence and the ending is 14 s of room tone. A bed would also cover the room-tone jump at every cut on A3.
- **Audio crossfades** on A3 (no API). Twelve frames, Constant Power, at each cut.
- **The six cut lines and scene 6** are Jack's call; each is one overwrite to put back.
- **The megaphone overlap** at 3:21 to 3:27.
- **The delivery check still fails** on colour range (untagged full range) and reports 13 frozen stretches
  (the ten stills and the name-card freezes). Loudness is 3 LU under target. Fix at export, not now.
- **Shots worth re-making** are listed in `review-cut1.md`.

---

# Cut 2, second pass — lettering and the megaphone line (8 October 2026, afternoon)

**Asked for by Jack, 8 October 2026:** "make the changes you were going to make to bank robbery." Done in the
same sequence, `bank robbery - cut 2`; length and every cut point are unchanged (351.0 s, 88 + 30 + 26 + 58 clips).

## Premiere

- **16 pieces replaced in place** on V1 (15 with sound on A3, the megaphones on A1), each at the old piece's
  start, in and length. New files are `clips\cut2\c2b-*.mp4`, in bin `05-cut2-pieces`. One eval: set in and
  out, `createOverwriteItemAction`, clear, sixteen times, then the 15 A3 Volume values set again by start time
  (an overwrite resets Volume to 0 dB). Checked from the state file: no gaps on V1, no old piece left, all 15
  levels as planned.
- **Lettering (review finding 10).** Impact is gone. Names and the title are Franklin Gothic Demi Cond in
  white; the job line and the two black cards are Gill Sans Bold in cream with a short rule; THEY'RE LETTING
  THEM IN is Franklin Gothic Heavy on a newspaper strip; the platform's headline is a white post in Segoe UI
  Bold, in sentence case. The words are the same. The name-card jobs are still the plain ones: Jack's tags are
  not written.
- **The megaphone line.** `c2b-t-s08c-megaphones.mp4` gives the first "whose fault it is" 0.45 s of tail
  (was 0.3) and the second 0.15 s of lead (was 0.3), so the length is the same. The level trace shows the old
  cut landed 34 dB down the tail, so the "clipped word" was the listening model's report and may never have
  been audible. Not heard by anyone since.
- **Rebuild:** `python3 scripts/bank-robbery/build-cut2.py` now makes the `c2b-*` pieces and writes them into
  `edl-cut2.json`.

## Outputs

- Render: `renders\bank robbery - cut 2-20261008-1432.mp4` (325 MB). It replaces `…-1246.mp4` as the one to watch.
- Measured: no black frames at all; integrated −17.2 LUFS, true peak −1.4 dBFS (unchanged).
- Checked by eye: nine frames from the render (title, both black cards, three name cards, both headlines,
  the megaphones). **Not watched at speed by anyone.**

## Started, waiting on Jack

- **Music:** two cues generated in Suno, eight takes, unheard. Sheet and links:
  [`songs/score.md`](./songs/score.md). Jack picks and downloads; then they go on A4.
- **Re-made shots:** eight new stills, no video yet. Record and picks needed:
  [`stills-v4.md`](./stills-v4.md).

## Still needs a human

- Watch the 1432 render; rule on the six cut lines and scene 6.
- Jack's name-card tags.
- Audio crossfades on A3 by hand; the delivery check (colour range tag, loudness) at export.

---

# Cut 3 — the re-made shots and music (8 October 2026, late afternoon)

**Asked for by Jack, 8 October 2026:** "use the new stuff, but i liked the old kebab badcode ending, dont replace
that that was cool. use royalty free music, for the mood of each scene for now, we'll do suno stuff later. use
anything that fits and would improve it."

**Cut 2 is untouched.** Cut 3 is a clone of it (`createCloneAction`, renamed). No cut point moved and the length
is the same. Which shot, which tune and how loud are my choices; none is ruled.

## Premiere

**Project:** `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/bank robbery.prproj`
**Sequence:** `bank robbery - cut 3` — 1280×720 @ 24, 351.0 s (5 min 51 s)
**Built:** 2026-10-08 by session (bridge): one clone, 5 swaps, 10 music clips placed twice, 5 Volume values.

| Track | What |
| --- | --- |
| V1 | 88 clips, butted, no gaps (as cut 2, five replaced) |
| A1 | The 30 talking pieces (unchanged) |
| A2 | 26 narrator lines, Volume −3 dB (unchanged) |
| A3 | The bed (as cut 2, five replaced) |
| A4, A5 | **Music:** ten stems, alternating tracks so neighbours overlap for a crossfade. Volume 0 dB; the fades and the ducking are in the files |

**Bins added:** `06-cut3-pieces` (5 files), `07-music` (20 files: the ten `m??b-*.wav` on the timeline and the
ten first-pass `m??-*.wav`, which are no longer used and can be deleted from the bin).

**Rebuild:** `python3 scripts/bank-robbery/build-cut3.py` copies the clips, makes the name card and the stems
into `clips\cut3\`, and writes `edl-cut3.json` (swaps, music, the credit line).

## The five re-made shots (stills in [`stills-v4.md`](./stills-v4.md))

Clips: Omni 1.1 Flash, start frame, 720p, 8 s, `scripts/bank-robbery/br-clips-v4.mjs` → `vids\v4\`. Four came
back first time. `s12e-sold` was the clip submitted before the browser closed earlier in the day; it was
finished in Flow and was downloaded, not made again.

| At | Old | New (in `clips\cut3\`) | In | Length | A3 level |
| --- | --- | --- | --- | --- | --- |
| 1:27.2 | `c2b-card-09-drivers` | `c3-card-09-drivers` (still 4i **b**; 0.6 s of clip, then the freeze and lettering) | 0.0 | 1.92 | −6 dB |
| 2:38.9 | `s07-night-before` | `c3-s07-night-before` (still **b**) | 0.0 | 7.96 | −26.2 dB |
| 3:55.0 | `s09c-pallet` | `c3-s09c-pallet` | 0.0 | 7.17 | −14.3 dB |
| 5:37.0 | `s12b-count` | `c3-s12b-count` | 2.29 | 4.5 | +4 dB |
| 5:41.5 | `s12e-sold` | `c3-s12e-sold` (still **b**) | 1.0 | 4.0 | +4 dB |

- **The kebab shop is the old one** (`s12f-kebab.mp4`, the neon sign). The blank-sign still and the logo
  composite are not used.
- `c3-s12b-count` starts at 2.3 s so that she counts for about two seconds and then looks up at the window on
  the cut to the board. `c3-s12e-sold` uses 1.0 to 5.0 s: after 6 s the street lamp jumps to a new place.
- The stills were my pick of each pair, on the reads in `stills-v4.md`. Jack did not pick.
- 🟡 Mr Red wears glasses on the name card and on the pallet walk and has none at the party.

## Music

All Kevin MacLeod, incompetech.com, **CC BY 4.0**. Sources are in `music\` (ten files; `I Knew a Guy`,
`Hidden Agenda` and `Sad Trio` were fetched and not used). Each tune was described by the listening model
first (logs in `docs/listening/log/`, 2026-10-08 15:10 to 15:13); nobody has heard them by ear.

| Stem | From | To | Tune (from) | For | Open level |
| --- | --- | --- | --- | --- | --- |
| m01b | 0:00.0 | 0:47.8 | Covert Affair (0:00) | Breakfast, the spoiler, the title: walking bass, muted horn | −20 LUFS |
| m02b | 0:46.9 | 1:10.8 | Cool Vibes (0:00) | The hearing and getting out: plucked strings | −22 |
| m03b | 1:10.6 | 1:30.8 | Neon Laser Horizon (0:12.8) | The name cards: the 80s montage. **Cut dead** on the meeting room | −17 |
| m04b | 1:30.8 | 2:39.3 | Marty Gots a Plan (0:00) | The plan and the colours: sneaky woodwinds | −22 |
| — | 2:38.9 | 2:46.9 | none | The party makes its own noise | |
| m05b | 2:46.5 | 3:05.0 | Covert Affair (1:00) | Off the record; Denise in the hall | −22 |
| m06b | 3:04.2 | 3:43.0 | Volatile Reaction (0:00) | The march: drums | −24 |
| m07b | 3:42.3 | 4:18.6 | Hitman (0:00) | The walk: its beat comes in at 3:55, on the pallet | −24 |
| m08b | 4:17.8 | 5:37.4 | Covert Affair (1:30) | Inside the bank, the vault, the standoff | −22 |
| m09b | 5:36.8 | 5:45.6 | Heartbreaking (0:00) | Denise counts; the SOLD board: one guitar | −21 |
| m10b | 5:45.5 | 5:51.0 | Neon Laser Horizon (0:30) | The kebab shop: the montage tune's last bars and final chord | −18 |

- **Ducking is in the files.** Each stem sits at −33 LUFS while anyone speaks (cast or narrator, from
  `edl-cut2.json`, each span widened 0.3 s, gaps under 1.2 s closed) and rises to its open level where nobody
  does, over 0.8 s. The narrator plays at about −16.
- **First pass was −36 under speech** (`m??-*.wav`, render `…-1616.mp4`). The listening model then listed music
  only where nobody spoke, and the last chord ran into the end of the file. Second pass: −33, the open levels
  above, 0.5 s fade on the last chord.
- The Suno takes in [`songs/score.md`](./songs/score.md) are parked, as Jack said.

**Credit owed in the film (not yet on screen):**
> Music: "Covert Affair", "Cool Vibes", "Neon Laser Horizon", "Marty Gots a Plan", "Volatile Reaction", "Hitman"
> and "Heartbreaking" by Kevin MacLeod (incompetech.com). Licensed under Creative Commons: By Attribution 4.0.

## Outputs

- Render: `renders\bank robbery - cut 3-20261008-1619.mp4` (325 MB). `…-1616.mp4` is the first music pass and
  can be deleted.
- Measured on 1619: 351.0 s; integrated −17.4 LUFS, true peak −1.4 dBFS; black only on the two black cards
  (0:45.8 and 3:04.4, 1.5 s each, intended).
- Checked by eye: twelve frames from the 1616 render (same picture): the new name card, the party, the pallet,
  Denise counting and looking up, the SOLD board, the neon kebab sign.
- Checked by the listening model (Gemini 3.5 Flash, whole soundtrack, `docs/listening/log/2026-10-08-152201-cut3b.md`):
  music "comfortable" under the narrator in the three stretches asked about, no line masked, no pumping, the
  1:31 cut reads as deliberate, the last chord fades. The questions named what to listen for, so this is weak
  evidence. **Not heard or watched at speed by anyone.**

## Needs a human

- **Watch and listen.** Above all: is each tune right for its scene, and is the music level right under the voices.
- **The dead cut at 1:30.8** and **the synth tune over the kebab shop** are jokes I chose; either is one clip to change.
- **A credit for the music** has to be on screen before upload. There is no credits card in the cut.
- **The delivery check still fails** on untagged full-range colour (`scripts/delivery-qc.sh`: 4 ok, 7 warn,
  1 fail); loudness is 3.4 LU under −14. Export-stage fixes, as before.
- Still open from cut 2: the six cut narrator lines and scene 6, Jack's name-card tags, crossfades on A3.

---

# Cut 4 — Jack's notes on cut 3 (8 October 2026, evening)

**Asked for by Jack, 8 October 2026,** after watching cut 3. His words are quoted in full at the top of
[`stills-v5.md`](./stills-v5.md), with the design of every new shot. **Cut 3 is untouched.** Which characters stay
in the montage, the paper names, every shot design and every trim are my choices; none is ruled.

## Premiere

**Sequence:** `bank robbery - cut 4` — 1280×720 @ 24, 351.0 s (5 min 51 s; the same length as cut 3 by accident:
the montage lost 9 s, the party and the ending gained it back)
**Built:** 2026-10-08 by session (bridge): new sequence from one clip, emptied; 85 picture clips in three evals of
29, 29 and 27; 26 narrator lines and 10 music stems in the third; 37 bed levels and 26 narrator levels in one
transaction; then four name cards replaced in place.

| Track | What |
| --- | --- |
| V1 | 85 clips, butted, no gaps |
| A1 | 30 talking pieces |
| A2 | 26 narrator lines, −3 dB |
| A3 | 55 bed clips, each with its own level |
| A4, A5 | 10 music stems (`m??d-*.wav`), 0 dB, ducked in the file |

**Bin added:** `08-cut4-pieces` (36 files from `clips\cut4\`; the four `c4-card-*` are superseded by `c4b-card-*`).
**Rebuild:** `python3 scripts/bank-robbery/build-cut4.py` → `edl-cut4.json`, `edl-cut4.txt`. It takes cut 3 as a
list, applies the rules below, and works out every start time again. Narrator lines keep their offset from the
picture they sat on; music cues move with the picture.

## What changed, note by note

| Jack's note | What was done | At |
| --- | --- | --- |
| Montage too long; names not on long enough | **Four cards, not ten:** The Ex, The Donor, The Proprietor, Mr Blue and Mr Red. Each is 2.7 s (0.6 s of the shot, then the name for 2.1 s; it was 1.1 s). A dark band sits behind the lettering, because THE DONOR was white on a white wall. The montage is 12.5 s, was 19 s. Out: the Fixer, Governor, Presenter, Platform, Accountant, Mr Turquoise | 1:11.8 |
| Stop-the-boats: spinning newspaper headlines for both | Two front pages made in Flow, spun in ffmpeg (`c4-paper-blue` 5.0 s, `c4-paper-red` 4.2 s). The model-town headline shots are gone | 1:36.7 |
| "the model house arent working" | "Which one's true?" and "I need them to reply" are re-shot at the garage table between two newspapers (`s05e-papers`, two dialogue clips). 🟡 **The planning table itself (`s05-plan`, six pieces) still has the model town on it**; I read the note as being about the headlines and the café, and left it | 1:45.9 |
| The night before: funnier, a compilation | Five shots in 12 s: laughing, pints, darts, pool, and the Fixer being sick in a champagne bucket beside the Proprietor, who does not react. The narrator's line covers the first four; the bucket plays in the clear and cuts to the Proprietor in the same chair for "off the record". No music under it | 2:33.5 |
| The man at the window: David Lynch | `s08b-remote-window`: a locked-off wide from the back of a dark room, the man small and off-centre against a window of pink and blue smoke, red curtains, one dim lamp, a dial telephone | 3:11.5 |
| Riot in the look of the barrier shot | New: placards (3:04.5), megaphones (3:19.4, new dialogue clip), the bank with BANK carved on it under "It's got BANK written on it" (3:23.4, was a held still), the walk (3:44.5). Kept: the barrier shot itself, the Presenter, the officer, the pallet | 3:04 to 3:52 |
| Real café, not the model, where they talk about buying it | One shot of the café with a FOR SALE board and a hand holding tagged keys, under "On houses… Including one above a café". It replaces the model insert and the price-tag shot. Slowed to 81 % to cover 9.7 s | 5:09.0 |
| The guns look like AI slop | New plate: three full figures a corridor away, red rim light, dark faces. 🔴 **Flow refused to animate it** (below), so the plate is moved in ffmpeg and carries the old clips' sound | 5:18.7 |
| Café sold: the cleaner outside in the rain, she looks up, the camera pans up | `s12h-denise-rain` 4.5 s (her back, the SOLD board across the road), then `s12i-denise-face` 7.5 s: she tips her head back, shuts her eyes, and the camera tilts up into rain through lamp light. Savings book and window shots are out. The ending is 17.5 s, was 14 s | 5:33.5 |
| Keep the kebab shop | Kept, untouched (`s12f-kebab.mp4`) | 5:45.5 |

## Clips (Omni 1.1 Flash, start frame, 720p, 8 s; `vids\v5\`)

Fourteen of sixteen made. `scripts/bank-robbery/br-clips-v5.mjs`, prompts in `br-clips-v5.json`.

- **First time or on the runner's own retry:** window, megaphones, bank, walk, pints, darts, pool, bucket, both
  papers clips, Denise's face, the café. Seven tries failed with `UPLOAD_REFUSED` on the start frame and passed
  on the next try with nothing changed.
- **"Unusual activity" once each, passed when run again:** placards, Denise in the rain.
- 🔴 **Refused four times, never made:** both standoff clips. Twice with "pistols" and "aim" in the text, twice
  without. The start frame shows pistols pointed at people; the repo had already seen this once
  (`docs/google-flow/omni-flash.md`). **So the standoff is not a Flow clip:** `c4-t-s12g-standoff.mp4` and
  `c4-s12g-standoff-balance.mp4` are the still with a slow push, a little drift, a pulsing light and grain
  (ffmpeg `zoompan`, `eq`, `noise`), with the sound of the old clips: the three shouted lines and the bell.
  Nobody's lips can be read at that size. Nothing moves in it except the camera and the light.

## Music

Cut 3's ten cues and levels, moved with the picture (`m??d-*.wav`). The montage tune now runs 13.75 s and still
cuts dead on the meeting room; "Marty Gots a Plan" stops as the party starts; "Heartbreaking" runs 12 s under
Denise. Credit still owed on screen (line in the Cut 3 section).

## Outputs

- Render: `renders\bank robbery - cut 4-20261008-1732.mp4` (327 MB). `…-1730.mp4` has the old name cards and can
  be deleted.
- Measured on 1732: 351.0 s; black only on the two black cards and the first frame of each newspaper spin
  (the page is a speck). On 1730 (same sound): integrated −17.5 LUFS, true peak −1.4 dBFS.
- Checked by eye: 32 frames from the 1730 render, one or more from every changed shot, and the new Donor card.
- Checked by the listening model (`docs/listening/log/2026-10-08-163355-cut4.md`): all four re-made dialogue
  moments heard complete ("Hang on. Which one's true?", "Doesn't matter…", the megaphone line, the three
  standoff lines), the narrator clear over the party. It hears the retching as "a loud double-cough" and says the
  last note is cut off at 5:51; the file has a half-second fade there, the same as cut 3, where it said the
  opposite. **Not watched or heard at speed by anyone.**

## Needs a human

- **Watch it.** Each shot was judged from eight frames a clip, so anything that warps between frames is unseen.
- **Which four in the montage,** and the paper names (THE DAILY TRUMPET, THE PEOPLE'S VOICE): Jack's call.
- **The standoff does not move.** If that reads as a still, the route is a new plate with the pistols lowered or
  out of frame, which Flow will animate.
- **`s05e-papers`:** the two newspapers hang in the foreground with no hands on them.
- **The planning table still shows the model town.**
- **Mr Red's glasses** come and go between shots.
- Still open: the music credit on screen, the delivery check (untagged full-range colour, loudness), the six cut
  narrator lines and scene 6, the name-card tags, crossfades on A3.

---

# Cut 5 — Jack's notes on cut 4 (8 October 2026, late)

**Asked for by Jack, 8 October 2026,** after cut 4. His words are quoted in [`script.md`](./script.md),
"Jack's notes on cut 4"; the design of every new shot is in [`stills-v6.md`](./stills-v6.md). **Cut 4 is
untouched.** He ruled three things: the paper names are fine, the still with the guns stays, the kebab shop
stays. Everything else below is my choice.

## Premiere

**Sequence:** `bank robbery - cut 5` — 1280×720 @ 24, 382.3 s (**6 min 22 s**; cut 4 was 5:51. The new opening is
19 s and the restored narrator line with its two shots is 10 s)
**Built:** 2026-10-08 by session (bridge): new sequence from one clip, emptied; 102 picture clips in three evals
of 34; 28 narrator lines, 10 music stems and 80 levels in the third.

| Track | What |
| --- | --- |
| V1 | 102 clips, butted |
| A1 | 30 talking pieces |
| A2 | 28 narrator lines, −3 dB |
| A3 | 72 bed clips, each with its own level (the five archive shots are silent) |
| A4, A5 | 10 music stems (`m??e-*.wav`), 0 dB, ducked in the file |

**Bin added:** `09-cut5-pieces` (41 files from `clips\cut5\`, plus `n00-s00-proud.wav`).
**Rebuild:** `python3 scripts/bank-robbery/build-cut5.py` → `edl-cut5.json`, `edl-cut5.txt`.

## What changed, note by note

| Jack's note | What was done | At |
| --- | --- | --- |
| A panning shot of the café open at the beginning | `c5-s00a-cafe-pan`, 5.5 s: the same corner as the SOLD shot, on a wet morning, lit and busy, a builder leaving with a bacon roll. The clip is locked; the pan is an eased crop across it in ffmpeg (hybrid method) | 0:00 |
| Full English, English pride, WW2, pints, football; quick, eye-grabbing; the narrator proud to be British | Twelve shots at 1.1 s each under a new narrator line: full English, fry-up, tea, pint, park football, Spitfires, pilots scrambling, bunting and a St George's flag, the Home Guard, VE Day crowd, St Paul's floodlit, fish and chips. 🔴 **The line is my placeholder** (`n00-s00-proud`, 13 s; words in `script.md`) | 0:05.5 |
| Montage: only the exciting ones, not just men with lettering | Five names, each **over the moving shot** for 2.1 s (no freeze): the Ex, the Donor, the Proprietor, Mr Turquoise (the selfie with the van), Mr Blue and Mr Red. Two shots with no lettering between them: the crew round the fountain from below (unused until now) and the two faces nose to nose. 12.5 s | 1:30.8 |
| Remove every model-town scene | The plan's first three lines are re-shot at a bare table (`s05h-table`, two dialogue clips). **Cut:** "And her?" / "She keeps every penny", and the Ex pushing the model crowds together. "Nothing. We put it in.", the accountant and "You bastard" are the same clips **cropped 1.28× with the bottom of the frame shaded**, which takes the cardboard roof out. The two garage wides in scene 6 are cropped 1.59× to lose the table with the model on it | 1:43 to 2:46 |
| The eating clip back | `s09-walk.mp4` (second pass) is back under "this is the bit with the lasers" | 4:01.0 |
| More on left and right; the politicians laughing | **Laughing:** Mr Blue and Mr Red in the dark upstairs room, megaphones dumped on the table, 4 s, no narrator, straight after "It's got BANK written on it" (3:42.2). **Left and right:** the narrator's "Nobody films it. Every phone in the street is pointed at a neighbour", cut since cut 2, is back over the riot-look walk and then two protesters with the same face filming each other while the pallet goes by between them (4:08.0). **No new conversation was written:** briefs for four are in `script.md`, with a ruling owed first | 3:42, 4:08 |
| Denise: barely acknowledges them, asks someone to move, bleach and a rag | New clip after "Lift your feet": the Fixer sits on the counter eating; she says "Shift."; he shuffles along; she sprays where he sat and wipes it. Seen along the counter past a green desk lamp. "Shift." is my word | 4:48.1 |
| The guns still works; keep the kebab shop; paper names fine | Unchanged | |

## Clips (Omni 1.1 Flash, start frame, 720p, 8 s; `vids\v6\`)

Ten of eleven made, nine first time. `scripts/bank-robbery/br-clips-v6.mjs`.

- 🟡 **`s08g-laugh` cuts itself:** at 3 s the clip jumps to a closer framing of the two men, with the street and
  the crowd visible below the window. The prompt asked for one continuous shot. The close half is what is in the
  cut (3.4 s to 7.4 s); it is the better shot.
- 🔴 **`s08f-argue` was refused three times, three different reasons:** "this video failed to generate", "Audio
  generation failed", and then **"Unable to generate videos that might cause reputational risk or misrepresent…"**
  with the shouting taken out of the sound line. The frame is two realistic men in a street confrontation. It is
  in the cut as the still with a slow push through the gap toward the pallet, flare flicker and grain (ffmpeg),
  over the placards clip's sound and under the narrator.

## Archive footage

Five shots, from three US government films on archive.org, picture only: ledger, timecodes, hashes and what was
and was not verified in [`footage-ww2.md`](./footage-ww2.md). `ww2-04` (soft) and `ww2-07` (spare) are not used.
No credit is owed; the courtesy credit strings are in that file. 🟡 Its author's own doubts stand: the British
shots inside the two Capra films are not traced to their original maker, and the newsreel's producer was not
re-checked.

## Music

Cut 4's cues, moved with the picture (`m??e-*.wav`). "Covert Affair" now starts under the café and runs through
the proud montage. No music was added for the montage; it wants something of its own (see below).

## Outputs

- Render: `renders\bank robbery - cut 5-20261008-1845.mp4` (355 MB), 382.3 s; integrated −17.4 LUFS, true peak
  −1.1 dBFS.
- Checked by eye: 38 frames from the render, at least one from every new or changed shot.
- Checked by the listening model (`docs/listening/log/2026-10-08-174719-cut5.md`): the new narrator line, the
  two re-shot plan clips, "Shift." and the restored line all heard complete and as written. It hears the
  laughing as one man "panting and chuckling", and lists four places where a clip's own sound stops dead at a
  cut (0:05, 1:18, 2:53, 3:45). **Not watched or heard at speed by anyone.**

## Needs a human

- **Watch it.**
- 🔴 **The opening line** is mine. Jack writes the jokes.
- 🔴 **How far the piss-take goes into the crowd** (Jack and Kai): see the note in `script.md`. Then the four
  conversations can be written and shot.
- **"She keeps every penny" is gone,** and with the savings book also gone nobody says Denise kept her money.
- **The proud montage has the film's jazz under it.** A brass band or a terrace chant would do more; nothing was
  fetched.
- **Sound stops dead at cuts** on A3 (no crossfade API): twelve frames, Constant Power, by hand, most of all at
  0:05.5 and 3:46.2.
- **Length:** 6:22.
- Still open: music credit on screen (and the archive courtesy credit if wanted), the delivery check, Mr Red's
  glasses, the six cut narrator lines and scene 6.

**Pieces made with plain ffmpeg, not by the build script** (all in `clips\cut5\`):

- `c5-card-*.mp4`: 2.4 s of the shot from its in-point, a black band at 55 % opacity over the lower middle from
  0.35 s, the name in Franklin Gothic Demi Cond 128 pt and the job in Gill Sans Bold 38 pt cream.
- `c5-t-s05d-twist-1`, `c5-s05d-twist-1`, `c5-hold-s05-accountant`, `c5-t-s05d-twist-2`:
  `crop=iw*0.78:ih*0.78:iw*0.11:0`, scaled to 1280×720, a black gradient over the bottom from 66 % to 82 % of
  the height, `noise=alls=5`.
- `c5-t-s06-colours-talk`, `c5-s06-colours-talk`, `c5-s06-colours`: `crop=iw*0.63:ih*0.63:iw*0.37:ih*0.2`,
  scaled, `noise=alls=5`.
- `c5-s08f-argue`: the still, `zoompan` from 1.0 to 1.38 on the centre over 7 s with a small drift, a flicker
  (`eq` brightness), `noise=alls=8`, the sound of `vids\v5\s08a-placards.mp4`.

---

# Cut 6 (9 October 2026): the morphing shots, from Jack's notes on cut 5

**His words:** "i like the last cut… sometimes objects morph and change, sometimes they randomley have an
american accent, sometimes they say the same thing at the same time, there are elements of ai slop… i like the
intro that was great. Please fix."

Review, fault list and what was and was not fixed: [`review-cut5.md`](./review-cut5.md).

- **Render:** `renders\bank robbery - cut 6-20261009-patch.mp4`, 382.3 s, the same length as cut 5.
- **What changed:** seven picture faults (an egg, a pint, a mug, a remote, a black band, a man walking through
  another man, a keyring), each swapped for a clean stretch of the same clip or a re-crop. **Sound is cut 5's,
  untouched.**
- ✅ **Premiere sequence `bank robbery - cut 6`** (built 9 October, about 10:30, after Jack connected the panel): a
  clone of cut 5 (`createCloneAction`, renamed) with six silent picture pieces on **V2**, over the old shots:
  `c6-fry` 6.625, `c6-pint` 8.875, `c6-g1` 32.083 (breakfast, Denise, remote), `c6-g2` 133.792 (the four twist
  shots), `c6-g3` 240.958 (both walks and the argument), `c6-keys` 340.292. Files in `clips\cut6\v2\`, bin
  `cut6`. **V1 and every audio track are exactly cut 5's;** to undo a fix, delete its V2 piece. Cut 5 is untouched.
- **Premiere render:** `renders\bank robbery - cut 6-20261009-1036.mp4` (355 MB). The earlier
  `…-20261009-patch.mp4` is the same picture made in ffmpeg before the panel was up and can go.
- 🟡 The V1 shots under the pieces were not re-trimmed, so `edl-cut6-changes.txt` is still the list to follow if
  cut 7 is built from the edit list and not from this sequence.
- **Not fixed here:** the voices (one voice for two men; accent). See the review for the cause and the test.
- **Not watched or heard at speed by anyone.**

**After Jack played cut 6 in Premiere (9 October, about 10:45):** "the audio is weird and it was strangley sped
up", all the way through, on timeline playback. Measured: the cut 6 render's sound matches cut 5's render in
every five-second window, and both files have the same length, frame count and sample rate. So the edit was not
the cause. A few minutes later he reported "it is fixed now for some reason". **Cause not found.** If it comes
back, look at Premiere's own playback first (audio hardware sample rate, dropped frames), not at the sequence.

**Made, not placed:** `clips\cut6\v2\c6-keys-b.mp4`, the keys shot at normal speed (6.2 s forward, then 3.5 s of
the same frames backward) as an alternative to the slowed `c6-keys.mp4` now on V2 at 340.292. Swap it in if the
slowed one looks odd.

---

# Cut 7 (9 October 2026): the vault and the riot re-made, every flagged line in the speaker's own voice

**Asked for by Jack, 9 October 2026,** after cut 6. His words, the review and the diagnosis:
[`review-cut6.md`](./review-cut6.md). Shots and results: [`stills-v7.md`](./stills-v7.md). **Cut 6 is untouched.**

## Premiere

**Sequence:** `bank robbery - cut 7`, 1280×720 @ 24, 382.3 s (**6 min 22 s, the same as cut 6**).
**Built:** a clone of `bank robbery - cut 6` (`createCloneAction`), then thirty pieces overwritten **in place**:
new picture on **V2**, its sound on **A1**, and a silent WAV on **A3** under every replaced stretch so the old clip
sound there is gone. Every piece is rendered to the exact length of the slot it fills, so **the narrator (A2) and
the music (A4, A5) did not move.** V1 is still cut 5's; to undo a change, delete its V2 piece and its A1 clip and
the A3 silence over it.
**Bin:** `cut7`. **Pieces:** `clips\cut7\c7-*.mp4`. **Rebuild:** `python3 scripts/bank-robbery/build-cut7.py` →
`edl-cut7.json`, `edl-cut7.txt` (speech marks in `speech-cut7.json`, several set by hand).

## What changed

| Where | Was | Now |
| --- | --- | --- |
| 0:44 to 0:53 | Mr Blue and Mr Red's two lines (heard as American) | Re-made with their own Characters' voices, same framing |
| 1:43 to 1:55 | The plan table, two clips | Three clips, one speaker each: the Ex, the Governor, the Ex |
| 2:04 to 2:18 | "Which one's true?", **The Platform**, "How much do we take?" / "Nothing. We put it in." | All re-made. **The Platform is English** (his Character's saved voice was replaced too). The Donor's question is now a wide of the three men |
| 2:22 | "You bastard." | Re-made, the same wide |
| 2:58 | The Presenter, "off the record" | Re-made, same framing |
| 3:17 to 3:32 | Placards (two in one hand), then the man at the window | **New order:** the street from a first-floor window (the geography, once), the man at the window, then two placards made by two people, landing under "They agree on the first line" |
| 3:46 | The Presenter in grey daylight | **New:** at dusk in the riot's light, from the cobbles |
| 4:11 to 4:18 | Two protesters, a frozen still with a push | **New, moving:** from a window above, each leaning over his barrier with a phone on the other, the pallet wheeled between the two phones |
| 4:25 to 4:34 | The bank door in white daylight, three shots | **New, one shot:** from the lobby floor, four silhouettes pull their masks on against the flare smoke and walk in; the doorman's "Morning, Governor" moved ahead of the narrator |
| 5:06 to 5:32 | The vault: three different-looking rooms, the hoover shot and the men's backs played a second time | **New, one room, one lamp:** drilling → "Why am I drilling?" → "It looks better." → still drilling → the key → he stands there with the drill → "You're putting it in?" → "Count it in the morning." → the vault filling, from the ceiling → the pallets still going in |
| 5:50 to 5:55 | "Who talked? / He talked. / Your lot always talk." in one wide (heard as a New York caricature) | Three close-ups in the alarm light, one speaker each. The wide with the pistols (Jack's "the guns still works") follows as before |

**Kept on Jack's word:** the opening, the old eating walk, the guns still, the kebab shop.

## Outputs

- **Render to watch:** `renders\bank robbery - cut 7-20261009-1501.mp4` (356 MB), 382.3 s, integrated −17.3 LUFS.
  `…-1457.mp4` is the same cut before two sound fixes and can go.
- **Checked by eye:** every changed stretch of the render at one frame every two thirds of a second. No black
  frame was added (`blackdetect=d=0.03` finds only the two title cards and the two newspaper spins, as in cut 5).
- **Checked by the listening model:** 1:40 to 2:30, 3:15 to 4:35 and 5:00 to 6:00 of the first render. Every
  re-made line heard complete and British. It flagged the doorman's line landing on the narrator and an alarm bell
  far louder than the voices; both were fixed in the second render, which was **not** listened to again.
- **Not watched or heard at speed by anyone.**

## Needs a human

- **Watch and listen.** 🔴 Above all: do the re-made lines sound English to Jack, and does each man now sound
  like himself from shot to shot? The machine says yes; the machine has been wrong.
- 🔴 **Scene 6 ("Mr Blue. Mr Red. Mr Turquoise. Why am I Mr Turquoise?") was heard as American in this pass.** It
  was not on the list this morning and was **not re-made**. Also not re-made: the megaphone line, the officer,
  Denise's lines, the hearing, "So nobody's coming? / It's policy."
- 🟡 **Two shots next to the new vault still show the old one:** Denise looking down the corridor (5:02) and the
  Donor taking keys through a hatch (5:32). They are the old fluorescent look.
- 🟡 **`s11e-in`** ("You're putting it in?") has a bright corridor behind the guard.
- 🟡 **The doorman's mouth moves late in the door shot** with no words on it, because his line was moved to the top.
- 🟡 Most new talking clips have their own room tone (rain, a buzz, a tick) that stops at the cut. Crossfades are
  still a job by hand.
- **Unchanged from cut 5:** Jack's opening line and the four left/right conversations, the ruling with Kai on
  how far the piss-take goes, music credit on screen, the delivery check, Mr Red's glasses.

---

# Cut 8 (9 October 2026): Jack's fourteen notes on cut 7

**Asked for by Jack, 9 October 2026.** His notes frame by frame, the diagnosis and the new prompt rules:
[`review-cut7.md`](./review-cut7.md). Shots and results: [`stills-v8.md`](./stills-v8.md). **Cut 7 is untouched.**

## Premiere

**Sequence:** `bank robbery - cut 8`, 1280×720 @ 24, 353.4 s (**5 min 53 s**; cut 7 was 6:22).
**Built:** a clone of `bank robbery - cut 7` (`createCloneAction`), then, in this order:

1. The ten music clips lifted off A4 and A5.
2. **Three stretches removed and closed up** (cut 7 times): 177.875 to 190.375 (the whisper at the party, its
   narrator line 15, and Denise counting in the hall), 258.25 to 265.417 (two men and one pallet, with narrator
   line 24), 292.708 to 301.958 ("It's about that much" and "What's all that, then?"). Each was one
   `createRemoveItemsAction(selection, true, MediaType.ANY, false)` with every clip inside the stretch, on every
   track, in the selection. Checked against cut 7's state: all 276 remaining clips moved by exactly the same
   amount.
3. **Twenty-nine new pieces overwritten in place** (V2 picture, A1 sound, silence on A3), as in cut 7. Pieces:
   `clips\cut8\c8-*.mp4`. Bin `cut8`.
4. Narrator line 29 replaced by `n29c-s11-crime-number.wav` (Jack's wording), level set to match the others (−3 dB).
5. Music laid again. Three stems cross a removed stretch and were re-rendered with it cut out and a 0.3 s
   crossfade: `m05f`, `m07f`, `m08f` in `clips\cut8\`.
6. **Colour:** Lumetri Color, **param 16 Saturation 128**, on the 105 older clips. Not on the new `c8-` pieces
   (already saturated), the archive film, the newspaper spins or the black cards. Six evals of eighteen clips.

**Rebuild:** `python3 scripts/bank-robbery/build-cut8.py` → `edl-cut8.json`, `edl-cut8.txt` (times in the .txt are
cut 8's). Speech marks: `speech-cut8.json`, several set by hand.
**To undo the colour:** remove the `Lumetri Color` component from the clips, or set its param 16 back to 100.

## What changed (cut 8 times)

| Where | Now |
| --- | --- |
| 1:10 to 1:20, the hearing | Her question is `narrator\v8-panel-q.wav` (AI Studio speech, voice Gacrux, an RP note) over the old picture. His answer is a new Ingredients clip in The Ex's own voice |
| 2:24 to 2:36, the garage | Five one-speaker Ingredients clips: the Ex, Mr Turquoise, the Ex, Mr Blue, Mr Red |
| 2:58, the party | The whisper is gone; the night-before compilation now cuts straight to Denise |
| 2:58 to 3:03, the hall | Denise hoovering (a new clip from the old still), under "the only person so far with real jobs" |
| 3:59 to 4:06 | "Nobody films it": from inside the crowd, three phones pointed across the street, the pallet going by behind them |
| 4:06 to 4:15, the door | Four men already in rubber masks, standing in the doorway in the smoke. The doorman's "Morning, Governor" is cut 7's sound, mixed in at the top |
| 4:15 to 4:22 | Mr Turquoise with the pistol in his raised hand, plaster falling |
| 4:22 to 4:33 | Denise comes in (from behind her); the hoover goes round three pairs of planted shoes; "Shift." with the cloth already under her glove and the bleach bottle untouched |
| 4:33 to 4:37 | Denise looking at the money, in the hall (was the old vault corridor) |
| 4:37 to 5:03, the strongroom | New place: cream brick basement, green iron door. Drilling → "Why am I drilling?" → "It looks better." → drilling → the key → he looks at the drill → the guard's question (`v8-guard-q.wav`, his back to us) → "Count it in the morning." → bricks onto shelves → the full strongroom, the door closing |
| 5:21 to 5:26, the standoff | "This is your mess! / We inherited it! / Thirteen years! / Fourteen!" (lines mine) |

**Cut on Jack's word:** narrator lines 15 and 24; Denise's "Lift your feet", "It's about that much" and "What's
all that, then?". The last one was not named by Jack; it sat between two removed shots in the old look.

## Outputs

- **Render to watch:** `renders\bank robbery - cut 8-20261009-1837.mp4` (329 MB), 353.4 s, integrated −17.0 LUFS.
- **Checked by eye:** 1:04 to 3:10 at one frame every 1.5 s and 3:56 to 5:31 at one frame a second. Every new
  piece is where the plan says, with no black frame between them.
- **New clips checked** at two frames a second before they went in. None shows a prop changing or a face breaking.
- **Checked by the listening model** (the twelve new talking clips and the two spoken lines, before assembly):
  every line complete, one voice each, none heard as American. It called all twelve "Northern English", which is
  not what was asked for and shows how coarse it is. Log: `docs/listening/log/2026-10-09-172911-talk-v8.md`.
- 🔴 **Nobody has heard cut 8 with human ears, and the render's sound was not listened to by anything.**

## Needs a human

- 🔴 **Watch and listen.** Above all the accents (the hearing, the garage, the strongroom, the standoff) and
  whether the levels of the two spoken-in lines sit right.
- 🟡 **Old-look shots still next to new ones:** the Donor's keys through the hatch (5:03) and both standoff wides
  (5:26 to 5:36) are the grey look. The garage wide after "Fourteen!" (2:36) is the first-pass picture.
- 🟡 **The hearing answer is a wider frame than the shots round it** (Ingredients re-staged it). It cuts as a
  wide, but the Ex is small in it.
- 🟡 **`s06-names` and `s06-thirteen` were re-rolled once** because the first takes moved to a different room;
  first takes are in `vids\v8\replaced\`.
- 🟡 **Saturation 128 was not judged on a frame in Premiere** (`premiere_export_frame` failed); it was judged on
  the render's contact sheets.
- **Jack's to rule:** the standoff lines; whether "What's all that, then?" comes back.
- **Unchanged from before:** his opening line and the four left/right conversations, the ruling with Kai on the
  piss-take of the crowd, a music credit on screen, the delivery check, crossfades by hand on A3.
