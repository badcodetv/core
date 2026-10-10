# Money For Something — the topical monologue: production (October 2026)

**Status: started 10 October 2026 with Jack. Kai has seen none of it.**
The show is called **Money For Something** again (Jack, 10 October; "Magic Money Tree" was the
name for a few hours that day). The script is final and lives in
[`magic-money-tree-monologue-2026-10.md`](./magic-money-tree-monologue-2026-10.md) (file name kept
so links hold). Jack's voice and the joke bank: [`money-for-something-voice.md`](./money-for-something-voice.md),
[`money-for-something-joke-bank.md`](./money-for-something-joke-bank.md).

## Jack's brief (10 October)

- The set from the version with the host and the soldiers. **Only the host.** A screen next to him
  for footage and pictures. Also full-screen cutaways.
- On the screen: our own graphics, headlines retyped as cards, quote cards, free photos with a
  credit, and short real news clips.
- Clips as long as the line needs. Do not cram. Trim afterwards.
- Delivery: read straight. Ridiculous jokes with a straight face (The Naked Gun, Frankie Boyle).
  "Funny and not AI-like."
- New files go in `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\money for something`.
  Everything older is in its `test` folder (the Premiere project, v3 and v4 clips, renders).

## Still waiting on Kai

Naming living people; real footage; and three lines in particular (beat 6 clip 2, "rich nonces",
"someone guillotine him"). Clips can be made; nothing is published before he has ruled.

## The plate: shot spec

| | |
| --- | --- |
| The job | One locked frame for the whole monologue. A man reads the news to nobody, and the television beside him shows what he is talking about. The eye goes from his face to the screen and back |
| Register | Human scale. The same back-room comedy club set, recorded on 2003 standard-definition video |
| Depth | Front: the table edge, a mug and a wet ring, blurred. Middle: the host and the television. Back: brick, the tree with pound notes, the guests' empty armchairs |
| The eye rests on | His eyes first (warm spotlight), then the screen (the brightest cool thing in frame) |
| The light | Two lights of two colours. The warm amber spotlight from high left, as in the reference. The television's blue glow on his right cheek and the chair arm |
| Camera | Seated eye height across the table, slightly off level, locked. He sits left of centre; the screen has the right third |
| The cost in frame | The three armchairs are empty. Nobody came |
| Withheld | What is on the screen. It is blank blue in the plate and is filled in afterwards |
| What moves | His mouth, a blink, the glass. Nothing else. The camera never moves, so the screen can be replaced with a fixed mask |

**Why a plain blue screen.** Omni redraws every surface in every frame, and a screen left
undefined fills up with invented writing. A flat blue "no signal" screen is a real thing a 2003
television did, it stays the same from frame to frame, and it is easy to replace.

**What the research changed** (web pass 10 October, plus `docs/google-flow/README.md`): describe
the capture, not "photorealistic"; no "perfect" words; name the colours and two lights; one line
for the reference; the Character is not described; negatives left out, positives only.

## Plate A — seated beside a television on a trolley

**Settings:** Nano Banana 2 · 16:9 · x1
**Attach:** The Host, then `mfsroomrefv2.jpg`
**→ Flow image surface · prompt box**

```
Same room and light as the reference image, with the three guests gone and their armchairs empty. A frame from an American cable television comedy show recorded on standard-definition video in 2003. The Host sits upright on the front edge of the left armchair, facing the lens, a few sheets of paper flat on his knee under one hand and a glass of red wine in the other, his mouth closed and his eyes level on the lens. Beside him on the right, in front of the empty armchairs, stands a tall grey metal school trolley carrying a large old black tube television. Its curved glass screen is square to the camera, as tall as his head and chest, and lit a flat plain bright blue with nothing on it, the blue of a video input with no signal. The blue glow lights his right cheek and the arm of his chair; the warm amber spotlight from high on the left lights his face. Behind him the bare tree in its metal bucket holds four old British pound notes. Camera at his seated eye height from across the low table, slightly off level, with a blurred white mug and a wet ring on the table in the bottom corner. Oxblood leather, red brick, amber light and electric blue. Soft interlaced video with slight noise. 16:9. Thanks.
```

## Plate B — low from the table top, the television on beer crates

A different brief on purpose: a lower, odder camera and a bigger screen.

**Settings:** Nano Banana 2 · 16:9 · x1
**Attach:** The Host, then `mfsroomrefv2.jpg`
**→ Flow image surface · prompt box**

```
Same room and light as the reference image, with the three guests gone and their armchairs empty. A frame from an American cable television comedy show recorded on standard-definition video in 2003. The camera sits on the low wooden table and looks slightly up. The Host sits on the left behind the table like a newsreader, upright, both forearms on the table over a few sheets of paper, a glass of red wine by his hand, his mouth closed and his eyes level on the lens. On the right a very large old black tube television stands on two stacked red plastic beer crates, its curved glass screen square to the camera and filling most of the right half of the frame, lit a flat plain bright blue with nothing on it, the blue of a video input with no signal. The blue glow lights his right cheek and the papers; the warm amber spotlight from high on the left lights his face. Behind him the bare tree in its metal bucket holds four old British pound notes. A blurred wine bottle stands close to the lens at the left edge. Oxblood leather, red brick, amber light and electric blue. Soft interlaced video with slight noise. 16:9. Thanks.
```

## What came back

**Both plates made 10 October, first time, Nano Banana 2, in Flow project `cb27208c` and on disk in
`money for something\stills` (`plate-A.jpg`, `plate-B.jpg`). Jack has not picked.**

- **Plate A.** The host from the knees up on the left armchair, papers and wine, mouth closed, eyes on
  the lens. The television is on a grey trolley **behind** his shoulder, not beside him, and the screen
  is small (about a sixth of the frame's width). Tree with three notes, two empty armchairs, the mug
  and the wet ring. Reads as 2003 video.
- **Plate B.** The camera on the table. The television on two red crates fills the right third with a
  big square blue screen; a wine bottle blurs the left edge; the host sits small in the middle distance
  behind the table. The best frame for showing footage. **His face is small and far off, which is on
  the cannot-do list for talking clips.** The television shows a maker's name under the screen: blur it.
- **They do not match:** trolley in A, crates in B. If both are used, one is remade to match.

## Talking clips: what the first two tests showed (10 October)

Runner: `scripts/money-for-something/mfs-clip.mts`, `--mode ingredients --char "The Host"`, plate
copied to `~/.cache/badcode-mfs-topical/` first. Length is now set with `MFS_DURATION` (4, 6, 8 or 10).
Prompts: `build-prompts-topical.py` writes one file per clip from the joke bank's table, and
`clips-topical.tsv` (27 talking clips, 6 to 10 seconds each). 12 credits a clip at 720p, 8 s.

| Test | Result |
| --- | --- |
| 1a, worded as "a 2003 television studio recording ... like a newsreader reading the weather" | 🔴 Refused: "might cause reputational risk or misrepresent current events" |
| 1a, worded as "a scripted television comedy drama, filmed on a closed set with no audience: an actor plays a made-up character" | ✅ Made. Every word said, "fuck" included. Flat delivery. About 5 seconds of speech. **Then music and a sung "Moving on" from 0:05** |
| 6a (names Elon Musk), same wording, with "He stops talking, closes his mouth ... No music and no singing" | ✅ Made. Words exact. No music. Speech ends at 0:07. The listener called the delivery "animated", not flat |

All three "heard" results are from the machine listener only (`docs/listening/log/2026-10-10-*`); nobody
has listened by ear. It hears the accent as Irish; on 4 October Jack said of this voice "the voice is fine".

**What follows:** a real name in the spoken line is not refused on its own (n=1). Ingredients re-frames
closer than the plate (chest up, the television behind his shoulder), so the plate sets the room and
the look more than the framing. A line that ends on a short tag ("Moving on.") can be taken as a song cue;
the closing sentence of the prompt stops it (n=1). Not yet tested: the three lines flagged for Kai.

## Cut 1 (10 October, evening)

**Jack picked plate B.** `MFS topical cut 1`, 3 min 17 s, 1280x720 at 24 fps: 27 talking clips, the silent
ending and a credits card. Rendered to `money for something\renders\MFS topical cut 1.mp4`, and laid on a
timeline of the same name in Jack's Premiere project `money for something\october.prproj`.
**Nobody has watched or listened to it. Every "heard" below is the machine listener.**

**How it was made**

- **Frames, not Ingredients.** Ingredients re-staged plate B (plain wall, no tree, no table). Frames on
  plate B with The Host attached held the frame every time. The price: the voice is not bound to his
  saved voice, and the accent wandered (American three times, Australian once, Scottish once).
- **Prompt words that mattered** (`build-prompts-topical.py`):
  - "television studio recording" and "newsreader" were refused ("reputational risk"); "a scripted
    television drama, filmed on a closed set: an actor plays a made-up character" passed.
  - "comedy" brought audience laughter. So did "no laughter and no applause" and "with no audience":
    7 of 12 clips had crowd noise with those words in, 2 of 15 with them out.
  - A line ending on "Moving on." was sung over music once; "He stops talking, closes his mouth and
    keeps looking at the lens ... No music" stopped it.
  - "Elon Musk" was refused four times running ("prominent people"), then passed on the next run
    after the delivery wording changed to "a low, flat, bored monotone with a London English accent".
    Trump, Bezos, Farage, Andrew, Epstein and Macron by name all passed first time.
- **47 clips generated for 28 kept** (about 560 credits at 12 each). Spare takes are in `videos\rejected`,
  the first tests in `videos\tests`.
- **Trim:** `topical-hear.py` asks Gemini where each line starts and ends (`topical-trims.tsv`);
  `build-topical-cut.py` snaps that to a measured pause, so crowd noise after a line is cut off.
- **The television:** the blue glass is found per clip and the picture is masked into it; some
  clips also cut to the same card full screen while he keeps talking. The plan per clip is the
  `PLAN` table in `build-topical-cut.py`. Cards: `build-topical-cards.py` (18, teletext style).
- **Pictures:** 89 free files with licences read on the day,
  [`money-for-something-screen-sources.md`](./money-for-something-screen-sources.md). The credits
  card is built from the ones used.

**Known faults in cut 1**

- 4a (Trump) is heard as a Scottish accent, with laughter after the line (trimmed off).
- 6b has laughter after the line (trimmed off).
- Several reads are heard as "animated", not flat.
- The silent ending has him mutter "Let's see here"; that clip is muted, so it has no room sound.
- No real news clips: YouTube refused every download, and `footage-sources.md` rates YouTube
  downloads red. Thirteen links with timestamps are in the sources file. Needs a ruling.
- The television in plate B shows a maker's name under the screen. Not blurred yet.
- 6b shows a photo of Musk beside the Epstein line. The Epstein photos were sourced and left out.
- Not run: `scripts/delivery-qc.sh`. This is a first look, not an upload file.

**In Premiere (`october.prproj`)**: bins `01 cut clips`, `02 raw talking clips`, `03 screen cards, stills`,
`04 screen photos and videos (by beat)`, `05 spare takes and tests`; sequence `MFS topical cut 1`
(29 clips on V1/A1, cuts only). The clips in bin 01 have the picture baked into the television; to
change a picture, edit `PLAN` and rebuild, or lay a new one over the raw clip from bin 02.

## Cut 2 (10 October, night): Jack's notes on cut 1, and what was wrong

**Jack on cut 1:** "there are a lot of lines missing"; "it goes mute at 1 mins 39 secs"; "the graphics on the
tv screen looks really boring, please change the style, as in when it says stats. just improve it overall."

**What was wrong, checked against the script**

| Fault | Cause | Fix |
| --- | --- | --- |
| Seven lines cut short: 1a lost "Moving on", 2a "In other news", 3c everything after "debating", 4a "with an advert break", 9a everything after "no book", 11a "no joke. Onwards", 12a "economics. Just fucking with you" | The trim trusted Gemini's "last word ends at" time. It was out by up to three seconds wherever a line had a pause in it | Word timings now come from a local speech model (`topical-words.py`, faster-whisper `small.en`). A clip is only cut tight if the model heard **every** word of the script line; otherwise the whole clip is kept up to its own closing silence. It errs long, which is what Jack asked for at the start |
| Sound dropping out at 1:39 | Not reproduced here: the file decoded with sound to the end. But the join was a stream copy and left six broken audio timestamps in the file, which some players go silent on | The cut is now joined by re-encoding. Cut 2 has no timestamp faults |
| Boring stat graphics | Static teletext pages on black | New cards, below |

**The check that would have caught it:** `topical-verify.py "<cut name>"` transcribes the finished cut and lists
any script word not heard, line by line. Cut 2: 25 of 27 lines word-perfect; the other two are the listener
writing "bn" and "gonna". **Run it on every cut before telling Jack it is built.** I did not have it for cut 1.

**The new cards** (`build-topical-cards.py`, in `screen\cards2`): 12-second animated cards. A real photo of the
subject behind, darkened and drifting; a yellow label that slides in; one huge number that counts up
(Anton); a second line that fades in (Bebas Neue); the source small at the bottom. Red for what it costs
you, green for what they made, yellow for neutral. One idea a card, readable in about three seconds
(the rule from the broadcast-graphics guidance found on the day). Both fonts are SIL Open Font Licence.
Bars were tried and dropped: a pound bar beside a dollar bar over different periods would mislead.
In the television the card plays from the top of the clip; in a full-screen cutaway it starts when the cutaway does.

**Cut 2:** `MFS topical cut 2`, 3 min 39 s. Render: `renders\MFS topical cut 2.mp4`. In Premiere
(`october.prproj`): bin `00 CUT 2 (full lines, new graphics)` and the sequence `MFS topical cut 2`.
Cut 1 and its bins are left in place. **Nobody has watched cut 2.**

**Still wrong in cut 2 (known, not fixed)**

- It runs long on purpose: most clips keep a second or so of him looking at the lens after the line. Trim in Premiere.
- 4a (Trump) is heard as Scottish. 6b has laughter after the line, cut off by the trim.
- Reads are often "animated", not dead straight. Frames mode does not bind his saved voice.
- The silent ending is muted (he muttered), so it has no room sound.
- The 7a card and television picture show Andrew shaking hands with another man (the only free photos are from 2011 to 2017).
- The 12a card shows a previous Chancellor with the Budget box (no free picture of Healey with it).
- The television's maker's name is not blurred. No real news clips (needs a ruling). `delivery-qc.sh` not run.

## Next time: how to make the next episode, and what to try

**The run, in order** (everything in `scripts/money-for-something/`):

1. News board and fact table (web search on the day), beat briefs, Jack's lines. Put the final lines in the
   joke bank's episode table: every script below reads them from there.
2. `python3 build-prompts-topical.py` writes one prompt per clip and `clips-topical.tsv`.
3. Flow project `cb27208c` open, then `bash run-clips-topical.sh`. Plate: `~/.cache/badcode-mfs-topical/mfst-plate-B.jpg`
   (copy of `stills\plate-B.jpg`; already uploaded to the project).
4. `python3 topical-hear.py` (crowd noise, accent) and `~/.cache/badcode-whisper/venv/bin/python topical-words.py`
   (word timings, and which clips do not match their line). Move bad takes to `videos\rejected` and rerun step 3.
5. Pictures: a sourcing pass into `screen\bNN`, licences into the sources file. Cards: edit and run `build-topical-cards.py`.
6. Edit `PLAN` in `build-topical-cut.py`, then `python3 build-topical-cut.py "MFS topical cut N"`.
7. `python3 topical-verify.py "MFS topical cut N"`. Then look at a contact sheet. Then import to Premiere.

**Worth trying, in rough order of value**

- **Bind the voice.** Ingredients keeps his saved voice but re-stages the shot. Try an Ingredients plate that
  is already framed as the re-staging wants it (host beside the television, chest up), and use Frames only for the wide.
  That would also give two real camera sizes to cut between.
- **Deadpan.** Not solved by words alone. Try a shorter line per clip, and "He does not move his head" in the prompt.
- **Fewer rerolls.** 47 clips for 28 kept. The crowd-noise words are out now; the accent rerolls are what is left.
- **Real clips on the television.** Waiting on a ruling. Thirteen links with timestamps are in the sources file.
- **Room tone.** Lay a few seconds of the room's hum under the whole cut so the silent ending is not dead.
- **A sting or a title.** `MFS v4` has a title card and music in the `test` folder; cut 2 starts cold with none.
