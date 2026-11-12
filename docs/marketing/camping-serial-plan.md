# Camping serial: the plan, with a stranger test per part

> 🔴 **Superseded the same day by trailers.** Jack, 12 Nov 2026, after watching the seven slices: "all of them
> don't feel like shorts, i feel like if we are clipping up this story, they should be more like fast trailers."
> Round 1 is three rough trailers (lines pulled from across the film, picture cut faster than the words, an end
> card pointing at the full film): **t1 Good business** (Tarquin's rise and fall, 38 s), **t2 Two men, one car
> park** (Bob against Tarquin, ends on the AI headline, 31 s), **t3 Rapid fire** (eight punchlines, 18 s). Cut
> lists: `design/camping-serial/build_trailers.py`; same page, same `picks` collection (docs `t1`–`t3`, `general`).
> Rough ffmpeg sketches for rhythm only: no music bed, 16:9. The pick is built properly in Premiere.
> The slice table below is kept as the record of what was tried.

**Status: plan, 12 November 2026, for Jack. Nothing cut in Premiere. Nothing ruled.**
Page (play each part, Keep / Change / Drop, a note each): https://claude.ai/artifact/SUr7Uzc2BqpGyYibafGus9,
built from `design/camping-serial/plan.html`; picks in its db collection `picks` (one doc per part, `p1`–`p7`, plus `general`).

Why this exists: batch 1 (September) was rejected as "random" ([`shorts-karen-camping.md`](./shorts-karen-camping.md) §1).
Jack, 12 November: last time the shorts "made no sense, how do we get around that". The answer agreed: a plan
first, one line per part saying what a stranger who has never heard of BadCode takes away, Jack's yes, then
one test short before the rest.

## What changed from the September slate (§6 of shorts-karen-camping.md)

The September in and out points were written **without hearing the film**; that file says Camping was
"probably score-only". It is not. The master (`Camping Comic/Camping Video NEW!/camping jack/Camping story video.mp4`,
290 s, 17 Sept) carries a full voiced drama: a female narrator, Tarquin, Bob and the man in the tent.
Its cut points land mid-sentence (part 2 opened inside the narrator's line, part 3 ended inside the tent
monologue), its hooks ("THREE THINGS PEOPLE DO") don't match what is said, and its part 7 leaned on a line
("IT DOESN'T SAY WHO OWNS THE MACHINES") that is **not in the film**. So every part below is redrawn on
sentence boundaries from a transcript.

Transcript: Gemini via the listen tool, `docs/listening/log/2026-11-12-141352-camping-story-video.md`.
Each preview clip was checked again for clipped words (logs `2026-11-12-1415*`–`1417*`); part 5 clipped
"I" and was re-cut 0.6 s earlier. **Timestamps are an LLM's, checked only by a second LLM pass: confirm by
ear before the Premiere cut** ([[verify-a-cut-against-the-script]]).

## The parts

| # | Name | In → out (s) | Len | A stranger gets… | Test | Hook bar (0 s), the film's own words |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Good business | 0.0 → 37.8 | 38 s | A posh trader in 2008 bets on ordinary people losing their homes and calls it good business. | ✅ | `SOME TWAT IS GOING TO LOSE A HOUSE OVER THIS TRADE` |
| 2 | Leave early | 37.8 → 70.0 | 32 s | A kind man's holiday ends in a crash he blames himself for. Nothing ties it to money or the trader. | ⚠ sad, no point alone | `SHE WANTED TO LEAVE EARLY` |
| 3 | Empty flats | 70.0 → 100.5 | 30 s | The same banker, 2026, buys social housing and leaves it empty, and jokes about the homeless from his car. | ✅ | `WE BUY MOULDY OLD EMPTY SOCIAL HOUSING` |
| 4 | A sandwich | 100.5 → 119.8 | 19 s | Everyone argued about what to do with homeless people; he just wanted a sandwich. | ✅ most sendable | `THEY DEBATED WORK CAMPS. I WANTED A SANDWICH.` |
| 5 | Empathy is not an emergency | 119.2 → 147.8 | 29 s | A rich man feels empathy for the first time; his therapist says no therapy can help him, he needs psychedelics. | ✅ comedy | `EMPATHY IS NOT AN EMERGENCY` |
| 6 | Wank tanks | 147.8 → 192.8 | 45 s | A rich man in a 4x4 screams at a man in a tent; the man's quiet reply hints a 4x4 wrecked his life. | ✅ the clash · ⚠ "two Macans, just the one man" is cryptic alone | `GET A JOB, YOU FUCKWIT` (burnt in only, never in a title or thumbnail: no adverts) |
| 7 | That's the economy | 233.5 → 290.1 | 57 s | The banker, tripping, screams "I only wanted to make money, that's the economy", then wakes homeless in a tent city under a headline: Britain's last worker replaced by AI. | ✅ rant · ⚠ last 30 s are silent | `I ONLY WANTED TO MAKE MONEY` |

Left out: 192.8 → 233.5 (meditation, "what am I, a dog?", the trip kicking in). Adding it to 7 makes 97 s.

## Flags

- 🔴 **Part 7 and the reader gate.** It carries the AI headline. The beneficiary is implied (the man who "only
  wanted to make money" is the one we've watched profit), not named. Kai relaxed the rule on 23 Oct to allow an
  implied beneficiary where the story carries it ([`the-reader.md`](./the-reader.md)); Jack's call.
- 🔴 **Part 7 and the new ending.** The 15 Oct call changed Tarquin's ending ([`../stories/camping/story.md`](../stories/camping/story.md)).
  This master predates it. If the film is re-cut, part 7 changes with it.
- ⚠ **Part 2** only works after part 1, or as the back half of a longer short. Recommendation: drop it as a
  standalone, or fold its last 10 s (black, glass) into part 6 as the reason behind "two Macans".
- **Titles** never carry a swear word (YouTube removes or limits adverts; [`profit.md`](./profit.md)).

## Recommended order and the test

Post order: 1 → 3 → 4 → 6 → 5 → 7 (2 held). **Test short: part 1.** It is the cleanest standalone, it opens
the story, and it carries no AI and no swearing in the hook. (Earlier today I suggested part 7; having heard
the film, 7 carries two open flags, so it should not be the first test.)

## Next, on Jack's picks

1. Read the page's notes (`ArtifactData` list `picks`) into `docs/stories/camping/feedback/` before acting.
2. Cut the test part in Premiere as its own vertical sequence from the master, hook bar burnt in, delivery QC.
3. Jack watches it on the timeline; then the rest.

## Trailer 2 into Premiere (12 Nov 2026)

Jack kept **t2 Two men, one car park** (page round 1; `docs/stories/camping/feedback/2026-11-12-trailers-r1.json`;
t1, t3 no vote). Jack's calls: **film's own audio + hits** (no new music), **letterbox + text** (whole 16:9 picture
in the middle of 9:16), and **the project goes in the shorts folder**.

**Folder:** `Desktop\Youtube Vids\animation\shorts\camping-trailer-two-men\` · pieces in `cut\` (built by
`design/camping-serial/premiere_pieces.py <master> t2 <cut dir> "trailer two men r1"`), 31.6 s:

| Track | What |
| --- | --- |
| V1 | 16 picture pieces, 1080×1920, picture 1080×608 centred on black, no audio (`cut\video\`), ending on the end card (CAMPING / the full film is on our channel) |
| V2 | `CAMPING` title in the top band, 0 → end card (`cut\text\title.mov`, ProRes 4444 alpha) |
| V3 | 9 captions, the film's own words, bottom band, one per line (`cut\text\NN-caption.mov`) |
| A1 | 15 line and flash clips cut from the master on word timings (`cut\audio\`) |
| A2 | `hit.wav` (synthesised sub drop, ffmpeg) at the glass, the newspaper, the BAD CODE plate and the end card |

**✅ BUILT 12 Nov 2026** in `camping trailer two men.prproj`, sequence **`trailer two men r1`** (1080×1920, 24 fps,
guid 73d3b2ac-be8a-4b3d-aff4-f3eeca819d85), media bin `trailer two men r1` (40 files). place.js: 43 placed, `fail: []`,
video tracks [16, 1, 9], audio [13, 4]. Frames checked at 7 s (title + shot + caption) and 29.5 s (end card); saved.
Next: Jack watches it on the timeline and notes it.

Rebuild from scratch (any session that owns Premiere):
1. `premiere_open_project({ path: "…\\shorts\\camping-trailer-two-men\\camping trailer two men.prproj" })`
2. `premiere_import` every file in `cut\video`, `cut\text\*.mov`, `cut\audio`, **bin `trailer two men r1`**
3. `premiere_create_sequence({ name: "trailer two men r1", fromItems: ["01a-shot-60.mp4"] })`
4. `premiere_eval` with the body of `cut\place.js` pasted in; expect `fail: []`
5. Export a frame at ~7 s and ~29 s and look; save.

Needs a human afterwards: audio crossfades if any line join clicks (no API for audio transitions).
