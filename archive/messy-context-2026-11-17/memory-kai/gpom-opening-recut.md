---
name: gpom-opening-recut
description: 2026-10-17 Kai — recut the GPOM music-video opening (gpom-s01 0:00–1:14): replace weak bulletin shots, ownership text after the push, robot choir + colossus at the drop; board SmYozTsKzUzB6Ask9rQs5H
metadata:
  type: project
---

Kai's notes on gpom-s01 (gpom-story.prproj), 17 Oct 2026. Clip refs as of that day:
- REPLACE: e02-far (near-miss car, 15.1s), 02-23-f2-b (champagne, 23.7s), 04-21-f1-b (two men at graph, 26.5s), 33-15-f1-b (shop, woman + four old men, 29.5s), 03-exchange-alive (old stock exchange, 34.0s).
- KEEP: e03-pass (workers in rain + server cabinets), 04-trading-floor (laughing traders), 2-glide-v2-b (zoom into tower).
- After `git push origin master` (HK-b4-terminal), over S2-shaft-tilt (servers, 57s) and EARTH-b2-pullout1 (LED, 59.7s), while the chant sings the developers line: text "ACQUIRING RESOURCE LOCK" then "NEW OWNERSHIP TRANSFERRED" — humanity pushed its ownership to a new master. Two lines only.
- THE DROP at 1:02:13 (v0:17 onward, building site) must be far more exciting. Data-centre-building story isn't working. Chorus line 1 = futuristic robot CHOIR at clone-army scale, red eyes, crimson hooded cloaks ("Traitors"-ish), singing; line 2 = the colossus AI machine with blinding festival-strength lights. Lean into Jeff Wayne's War of the Worlds: story + operatic.

Board: https://claude.ai/artifact/SmYozTsKzUzB6Ask9rQs5H (db `votes` {iid,by,v}, `notes`); builder scripts/gpom/build-opening-moodboard.py + opening-moodboard-template.html; prompts docs/stories/gitpush-origin-master/scenes/opening-recut-moodboard.json; stills D:\badcode-videos\gitpush-origin-master\clips\opening-recut\moodboard\.

**How to apply:** read the board's votes before shot design; don't touch Kai's timeline without asking. Related: [[gpom-music-video-fusion]], [[gpom-second-half-2026-10-16]].

**Round 2 (17 Oct, from Kai's votes + notes):** colossus = CO6 ring eye ("futuristic Sauron") ONLY, far bigger, on a mountain top in dust, ranges around, sun setting, no "Oracle Project" text. Animation: the red rim dots light in sequence so a dot seems to travel round the ring as the words are sung (the lights don't move). Choir = CH5 well joined to CH6 ship and army: start inside the well, rise out, the ship's floodlight is the light; CH7 face belongs inside the well, not a church. Street: ST1 scrapped (same as KEEP-rain); ST2 less rigid; one-desk-one-box must be obvious and use KEEP-rain's cabinets. Toast: TO2's look, real unglamorous owners, no headcount graph, not glitzy (TO3 no). Market: modern, not glitzy, not 70s. Bread BR1 yes; MK3 (banknote hall) yes. Round 2 stills: EY1-3, WL1-3, DB1, ST4, BD1-2, MK4-6 (-a/-b/-c). flow_edit_image harvests the reference image as one "candidate" when it returns 3 — delete that one.

**Picks locked (17 Oct, late):** docs/stories/gitpush-origin-master/scenes/opening-recut-picks.md is the shot list — ST4-c, DB1-b, TO1T-a (TO1 + table, keeps the HEADCOUNT screen), TO2, BR1, MK5-b, MK3, WL1-b→WL2-b, EY1-b, EY2-c. Open: text style (TX1–4), WL3.

**Animation storyboard (17 Oct):** https://claude.ai/artifact/7HjuaiKdhp2EYYMxaepsTi — 15 frames, 2-3 animation options each (db `picks` kind still|anim, `notes`), same template as the second-half storyboard. Data: scenes/opening-recut-storyboard.json + opening-recut-animation-options.json; builder scripts/gpom/build-opening-storyboard.py + opening-storyboard-template.html.

**17 Oct evening:** picks all anim option a; stills #5 TO1T-a, #6 MK3P-c (£50 re-make — Kai: anchored in the UK, never dollars), #12 WL3-b, #15 EY4-c (re-made from EY1-b: same eye/mountain/sunset, no town — humans gone). #5 fallback to front-two clink approved. Frame 10 text = typed on the CRT by `scripts/gpom/build-terminal-ownership.py` (patched copy of clips/s01/build_terminal.py, Mx437 font); Kai RULED version B (fits slot, "perfect timing"): HK-b4-terminal-own-B.mp4 replaces HK-b4-terminal on gpom-s01 at the same in/out — not yet placed. V2 clip 17-27-f2-a sits over the terminal 54.2–58.9 on gpom-s01: check before placing. Premiere bridge was held by another session — not taken.
**Clips (17 Oct night):** `scripts/gpom/opening-video/` (copy of second-half runner; the flow MCP's generate_video fails "Frames on Omni 1.1 Flash" — use run.mts with FLOW_CDP_PORT=9223). 10/12 in clips/opening-recut/video/ (reel opening-reel-v1.mp4 sent to Kai). #12 WL3-b silently blocked x4 (likely policy); #7 BR1 upload REFUSED (mother + toddler). #14 redraws the scene after ~2.3s (sunset → daylight) — only the first ~2s usable, which contains a big flare. Kai asked about timestamped Flow prompts for the eye flash/dot chase at 174 BPM (beat 0.345s, bar 1.38s); proposed a dark-eye still + timestamped take, awaiting his go + which word.
