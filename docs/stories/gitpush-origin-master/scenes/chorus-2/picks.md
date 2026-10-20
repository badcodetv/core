# Chorus 2 — picks and rulings

Append-only. Kai's words kept.

## 2026-10-19 — interview

- **Ask:** the second chorus, *"set in the environment of the first chorus"* (parade ground of robots, the mountain with *"the big Sauron eye"*), *"even more dramatic than the first chorus because we've built up the tension quite a lot"*, *"choose some slightly different shots and have some variation"*.
- **Length ruled:** *"I've doubled the number of clips… I've now altered the guides as well."* `gpom-s01` marker "chorus" **106.917 → 128.708s (21.79s, about 63 beats at 174 BPM)**; "war" now starts 128.708. Chorus 1 is 62.583 → 74.083 (11.5s).
- **Placeholder on V2 now:** white-flash 106.25–106.75, then chorus 1's set twice: WL2-b 106.75 · WL4-c 110.33 · EY1-b 112.29 · EY4-c 114.71 · WL2-b 117.71 · WL4-c 121.29 · EY1-b 123.25 · EY4-c 125.67 → 128.71. The second pass starts at 117.71 (the chant repeats).
- The lyric is chorus 1's four chant lines, headed `[Drop] [Chant | bigger]`.

## 2026-10-19 — the sentence and the two passes

- **Sentence agreed in outline:** the money bought an army; pass 1 = *"the same world closer and harder, lower among the ranks, the hooded robot's eyes. I love that."*
- **Pass 2:** *"the ships could come"*; *"the beam coming across an empty town is a really good shot. I love that"*; *"The eye turning to us."* Marching: *"I'm not sure… might be too ambitious, but let's see… the point of the new scene skill… is that we decide and cut."* → march stays on the board as a try.
- Draft brief.md + scene.json written (prefix `c2`).

## 2026-10-19 — brief approved

- **Night:** *"I think night time is correct, I like that, that's definitely a great shift."*
- **Ending = beam into the lens:** *"beam into the lens would be a brilliant end, well done."*
- **Brief approved:** *"yes, I totally approve."* → mood board round 1.
- Premiere released to another session (not needed until the bin import at the end of stage 3).

## 2026-10-20 — mood board round 1 published

- 56 stills across 8 beats (night), board https://claude.ai/artifact/E1AzBZ9ZC8ftaVVdHmdqg4 (Flow project 9415739d-6c98-4e7c-b68c-71bcb5cd1fb3). Made over three helper runs (two stopped by session exits); RK1–SH1 + MA1-a prompts in moodboard.json are reconstructed from the brief.
- 5 candidates rejected (Flow echoed the reference unchanged): TN1-a-a, TN1-b-a, TN1-c-a, TN1-d-a (sunset eye, no town), MA1-c-a (chorus 1's open-mouth face). In `moodboard/rejected/`, listed on the board as rows. No blocks, no md5 duplicates.
- Off-brief but kept: EC1-b-a came back at sunset, not night.

## 2026-10-19/20 — every still animated (Kai away)

- **Kai (goal, heading out):** *"animate each of these in a different way. So when I come back, we've kind of got lots of different options for videos. I really like the look and feel of what you've done here."* Still gate waived for this round: all 56 kept stills animated, no picks first.
- One motion per still in `r1-motions.json` (a different idea per still: eyes lighting row by row, heads turning to camera, the iris opening, lightning, ship descending, searchlight sweeps, marching, the beam over the town, the white-out). `make-jobs.py` turns them into `video-jobs.json` (keys mb01–mb56, stable). Camera locked, 6s, Omni 1.1 Flash, Frames, count 1.
