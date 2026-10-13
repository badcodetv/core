# Money For Something 2026 (the year in news): production

**Status: in production, started 14 October 2026. Jack has not watched anything yet. Kai has seen none of it.**
The script is [`money-for-something-2026-script.md`](./money-for-something-2026-script.md) ("THE SHOOTING SCRIPT" at the
bottom). The method is October's ([`money-for-something-topical-production.md`](./money-for-something-topical-production.md));
this file only records what is different.

**Jack's brief (14 October):** make the clips in Flow, put the cut in his open Premiere project, save new files in
`C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\money for something\2026`; avoid "AI slop"; use the
cinematography files and skills.

## Where things are

| What | Where |
| --- | --- |
| Folder | `...\animation\money for something\2026` (`stills`, `videos`, `screen\cards`, `clips`, `renders`) |
| Premiere project | `2026\2026.prproj` |
| Flow project | `cb27208c-4b16-426d-9144-c394f2735c15` ("mmt jack") |
| Kit | `scripts/money-for-something/y2026/` and `mfs-still.mts`, `mfs-clip.mts` one level up |

## The two plates (shot spec)

| | |
| --- | --- |
| The job | October's locked frame again, with a pint in it, so the heat line and the ending pay off |
| Register | Human scale; a back-room set on 2003 standard-definition video |
| Depth | Front: an empty pint glass with dried foam, blurred. Middle: the host and the television. Back: brick, the tree, an empty armchair |
| The eye rests on | His face (warm spotlight), then the screen (the brightest cool thing) |
| The light | Two colours: amber spotlight from high left, the television's blue on his cheek and the papers |
| Camera | On the table, looking slightly up, locked. He is chest-up, closer than October's plate B, because a small far face that then moves is on the cannot-do list |
| The cost in frame | The empty glass in front of the lens, the empty armchair |
| Withheld | What is on the screen (plain blue, filled in afterwards) |
| What moves | His mouth and a blink. The pint is only touched in the two silent clips |

- **Plate P1** (pint on the table): `stills\plate-P1-a.jpg`. Prompt: `y2026/prompts/plate-P1.txt`. Nano Banana 2, 16:9, two
  candidates, October's plate B and The Host attached. Candidate a was used: his face is larger. Picked by me, not by Jack.
- **Plate P2** (pint already at his lips): `stills\plate-P2-a.jpg`. Prompt: `y2026/prompts/plate-P2.txt`, P1 and The Host
  attached. It exists because Omni lifts props badly: the silent clips start with the glass already raised.
- Both show a real maker's name under the television glass. The cut builder blurs it.

## The run

1. `python3 y2026/build-prompts-2026.py` : 31 talking clips and 2 silent ones (`clips-2026.tsv`). Numbers are written as spoken.
   Two lines were too long for ten seconds and are split in two (17, 21).
2. `bash y2026/run-clips-2026.sh` : Frames, Omni 1.1 Flash, one clip at a time, The Host attached.
3. `~/.cache/badcode-whisper/venv/bin/python y2026/words-2026.py` : every word's time, and which clips do not match their line.
4. `~/.cache/badcode-whisper/venv/bin/python y2026/build-cards-2026.py` : 18 cards in October's third style.
5. `python3 y2026/build-cut-2026.py "MFS 2026 cut 1"` then `python3 y2026/verify-2026.py "MFS 2026 cut 1"`.
6. Import to Premiere, export, `silencedetect` for mute clips.

## What was learned (14 October)

- The Flow client's own Character picker no longer closes (the `@` picker stays open and blocks the prompt box).
  `mfs-still.mts` attaches a plate and a Character by name the way `mfs-clip.mts` does, and that works.
- A new prompt with the old plate attached as a reference kept the room, the light and the television and moved the
  camera closer, first time, both candidates usable (n=2).
- First two talking clips: every script word heard by the local speech model, frame held.

## Cut 1 (14 October)

`MFS 2026 cut 1`: 3 min 35 s, 1280x720 at 24 fps, 33 clips and a credits card. Render: `2026\renders\MFS 2026 cut 1.mp4`.
In Premiere (`2026.prproj`): bin `00 CUT 1`, sequence `MFS 2026 cut 1`, 34 clips on V1/A1, cuts only. Project saved.
**Nobody has watched or listened to it.**

- **Clips:** 33 kept from 37 made (about 440 credits at 12 each). Four were remade, spare takes in `videos\rejected`:
  y-11 said "three, three thousand"; y-23 dropped the "two" of "a hundred and two billion"; y-25 said "six point six six";
  y-18 was unclear after "People are angry". The numbers in those prompts were reworded and the second takes were right.
- **Refusals:** y-22 (the Epstein bailout line) was refused twice ("might violate our policies") and passed on the third try,
  same prompt. One timeout on y-21b and one on y-11, each fine on the retry.
- **The speech model invents words when it is given the script as a hint** and the clip has a quiet tail: it wrote
  "Thanks for watching" on four clips where nothing of the kind is said. For those, `NOPROMPT=1 VAD=1` gave the true words.
- **The screen finder** had to be limited to the right half of the frame: the windows, the front glass and the table all
  carry the television's blue in this plate, and the cards were landing across half the picture.
- **Checked:** `verify-2026.py`: every script word that is not a number was heard in the render; the listener writes numbers
  as digits, so it flags every number line. No timestamp faults. Contact sheet looked at: every card sits in the television.
  Premiere export: no mute clip (the only silence is the credits card). The maker's name under the screen is blurred.
- **Not passed:** `scripts/delivery-qc.sh` fails the render: it is tagged limited range and the picture is full range.
  This is a first look, not an upload file. Fix in the builder before anything ships.
- **Known:** in the first pint clip (y-28) he leaves a little in the glass. Each card restarts its animation at the top
  of every clip it is in. No room tone under the credits.

## Cut 2 (14 October): October's lessons applied, and a watch and listen pass

Jack: "remember the changes we made to the final cut of october, please apply what we learnt to this one. also watch and
listen to it, and fix any mistakes, make it better overall."

`MFS 2026 cut 2`: 3 min 32 s. Render: `2026\renders\MFS 2026 cut 2.mp4`. In Premiere: bin `00 CUT 2 (word-timed cards,
levelled, room tone)`, sequence `MFS 2026 cut 2` (34 clips on V1/A1, the room-tone bed on A2). Cut 1 is left in place.
**Watched and listened to by machine only (Gemini and a local speech model, contact sheets by me). No person has.**

**What the pass found in cut 1, and what was done**

| Found | How | Fix in cut 2 |
| --- | --- | --- |
| A laugh after "Who would have thought" (y-03) | Gemini | Clip remade; the new take is clean |
| Dead air before HS2; six clips opened on up to 0.7 s of low noise | Gemini, then measured | Heads are cut at the voice's measured start, not only at detected silence |
| The Farage clip quieter than its neighbours | Gemini | Every clip's gain is set from its measured loudness (one-pass `loudnorm` misjudged short clips). Cut 2 is -15.1 LUFS |
| Abrupt starts on three clips | Gemini | A little more air at heads and tails (0.10 s and 0.16 s) |
| Six seconds of dead silence on the credits | Measured | Credits 4.5 s; a faint room tone (about -54 dB) under the whole cut |
| A pub murmur under the last drink (y-30, first five seconds) | Gemini, twice | Those five seconds are turned down; the glass and the footsteps are kept |
| Cards landed before their word, or sat over the punchline | October's lesson from the shorts | A full-screen card arrives on its word and leaves before the punchline (`PLAN`: card, word in, word out) |
| Second lines of cards tiny in the television | October's review | Each type-only card is cropped to its own type so it fills the glass |
| Delivery check failed (range) | `delivery-qc.sh` | Flow's clips are converted from the BT.601 matrix and the picture is held inside 20 to 231 |
| "Anyway." (y-18) is mumbled and the tighter trim cut it | `verify-2026.py` | That clip keeps its head whole (`SOFT`) |

**Checked on cut 2:** every script word that is not a number heard in the render; no timestamp faults; contact sheet: every
card fits the television; accent heard as London on every clip; no laughter, music or second voice heard; Premiere export
has no mute clip.

**Still wrong or unjudged**

- `delivery-qc.sh` still prints FAIL on range. It tests the single darkest and brightest pixel, and the encoder's ringing puts
  a few pixels outside. Measured: 0.002% of pixels are outside legal range in cut 2 (0.12% in cut 1).
- The ending line (y-29) is heard as more acted than the rest. Left alone: it is the one line thrown at the audience.
- "Blah, blah, blah" (y-14) is heard as rushed. The petrol line (y-03, new take) is heard as slightly rushed.
- In y-28 he leaves a little in the glass.
- A counting card shows wrong numbers for its first half second (it counts up).
- The room tone is synthetic (filtered noise), not recorded from the set.

## Cut 3 (14 October): real pictures on the television

Jack: "Please add real footage/photos on the tv. also look through the repo for money for something october, apply what
you learnt from there."

`MFS 2026 cut 3`: 3 min 32 s. Render: `2026\renders\MFS 2026 cut 3.mp4`. In Premiere: bin `00 CUT 3 (real pictures on
the television)`, sequence `MFS 2026 cut 3` (34 clips on V1/A1, room tone on A2). Cuts 1 and 2 are left in place.
Same clips, trims, levels and pauses as cut 2; only the television, the card backdrops and the credits changed.

- **The television now shows a real picture or clip on 19 of 33 clips.** 13 new pictures from Wikimedia Commons (licence
  read per file on the day) and 7 of October's cleared files, one of them video (a destroyer firing a missile, under the
  "Trump bombed Iran" line). Record: [`money-for-something-2026-screen-sources.md`](./money-for-something-2026-screen-sources.md).
- **Seven cards have a photo behind them**, October's third style.
- **Credits card:** five credits owed (CC BY), shown whole. Cut 2's card cut one credit short at 92 characters and carried
  an Open Government Licence line though nothing in it was OGL; both fixed.
- **Not pictured on purpose:** the unnamed "British minister" (the television shows euro notes) and the unnamed "baroness"
  (the ident). A picture would name them.
- **Downloaded and not used:** the Maduro picture. It carries an "Obtained by NBC News" caption, so it is rated amber.
- **Nothing free found:** Count Binface, a Channel dinghy, PPE, Piddington. Those clips keep a type card.

**From October's files, checked or applied in this pass**

| October lesson | Where it was | In 2026 |
| --- | --- | --- |
| Real photos in the television, the card full screen on its word | cut 1 to cut 3, the shorts | Cut 3 |
| A photo behind each card | `build-topical-cards3.py` | Seven cards |
| Read every licence on the day; skip ShareAlike; record the credit string and the hash | the screen-sources file | New sources file, same table |
| Credits in the video, never cut short | Kai's ruling in `footage-sources.md` | Fixed in cut 3 |
| Never trim on an LLM's timings; verify the render against the script | cut 1's fault | Local speech model for timings; `verify-2026.py` on every cut |
| Do not use a joke twice | the joke bank | Checked: no repeats. Episode 2 is now in the joke bank |
| Check names, numbers and dates every time | the voice file | The cards use the script's fact tables of 13 and 14 October; **not re-searched today** |
| After a Premiere import, export and look for mute clips | cut 3's two mute clips | Done for cuts 1, 2 and 3: none |
| Words that summon crowd noise stay out of prompts | cut 1 | Kept out; one laugh still arrived and was remade |

**Checked on cut 3:** every script word that is not a number heard; no timestamp faults; contact sheet and a credits frame
looked at; Premiere export has no mute clip. **Not re-listened:** the sound is cut 2's, clip for clip.

## Not done, and open

- Jack has not approved the plates. Kai's rulings are all still open (living people, real photos, the Mone line, the Epstein lines).
- The fact checks listed in the script ("Checks owed") have not been re-run for the cards.
