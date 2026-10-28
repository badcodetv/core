---
story: gitpush-origin-master
scene: simulation (Kai's scene 4 — five years later)
kind: scene sheet — beats, shot specs, still prompts
date: 2026-09-29
status: stills PICKED by Kai (S1 00-b, S2 vape-bets-c, S3 00b-a); no video spent; narration not written to narration.md yet
scratch: /mnt/d/badcode-videos/gitpush-origin-master/clips/simulation/
replaces: cut 5 `ghosts` (the empty world + the ghost kitchen) — shelved, not deleted
---

# Scene 4 — the simulation

**Kai, 2026-09-29.** The ghosts cut did not grab him. After the Swindon battle ("It declined."),
jump five years, drop the viewer into a bright fake world with a happy narrator, glitch out into
the real wrecked one, and let a small robot break the fourth wall to explain. Rulings in this
session, all Kai's:

- **Caption → fake world → glitch → real world** approved as the spine.
- **The bot** is our existing six-wheeled pavement delivery robot (amber beacon on a stalk) from
  `clips/empty-street/stills/es-robot-a|b.jpg`. Voice: **warm, West Country**.
- **The freeze:** a "pause" first (world held, only the bot live); **one orbit attempt** after.
- The narrator swears once, out of character: **"Oh, fuck."** The AI ends the bot's speech: **"Oi."**

## Rules this scene must keep

- **The AI is never personified** (`story.md` rule 1). The bot talks *about* the AI in the third
  person ("him", "him upstairs"). It is never the AI's body and never says "I" for it.
- **Rule 11, outside-in feelings.** The bot saying "he misses you" is exactly the outside
  attribution the rule asks for. The narrator never says it himself.
- **One fourth-wall explainer per film** (story-craft ruling 1). This is it.
- **"Simulation" is named only to throw it away.** Never imply our world is one (Storyverse
  vocabulary kill list).
- **The glitch runs a flash-safety pass** (`ffmpeg photosensitivity`) before anything ships.
- The prompts.md guardrail "the collapse stays off-screen, no burning cities" is **overruled here
  by Kai** for the aftermath frame only: ruin, not combat. No bodies.

## Beats (draft words — narration.md gets them only once Kai edits them)

| Time | Picture | Sound |
| --- | --- | --- |
| 0–2s | Black. FIVE YEARS LATER (ffmpeg `drawtext`) | Silence |
| 2–10s | **S1** the fake Swindon high street: sun, flowers, bunting, a busy Saturday | Bright music. Narrator, delighted: *"Look at it. Flowers. Sunshine. Everyone in work. Honestly, I've outdone mys—"* |
| 10–11s | **The glitch** | Music and voice cut dead |
| 11–14s | **S2** the identical frame, wrecked. Ash drifting | Wind. Quietly: *"Oh, fuck."* |
| 14–16s | **Pause.** Ash hangs; a pause glyph in the corner | Dead silence |
| 16–34s | **S3** the bot rolls into the frozen world, beacon blinking, and talks to us | Bot: *"Sorry about him. He gets like this. He built the nice one after you lot went. Trouble is, there's nobody in it. It's just him, doing all the voices. So much for the universe being a simulation. He's bored stiff. He misses you. He'd never say—"* |
| 34–36s | Beacon cuts out; ash resumes | Narrator: *"Oi."* |
| 36s → | The coin, the cat, the slits, the Storyverse (narrator's voice) — **not yet designed** | |

## Shot specs

### S1 — the fake world
- **Job:** make the viewer relax and doubt themselves. After three minutes of doom, this is wrong.
- **Register:** deliberately off-house: high-key, saturated, advert-bright (the Parr counter-tradition, `registers.md`). The only frame in the film that looks like this.
- **Depth:** flower planter in the near foreground; shoppers and market stalls mid; the long street receding to a church tower.
- **Light:** high summer sun, from behind camera-left.
- **Camera:** locked, a little above head height, straight down the street. **Must be exactly repeatable** — S2 is an edit of it.
- **Withheld:** any sign of the war.
- **Moves:** the world only (bunting, shoppers). Camera never.

### S2 — the real world
- **Job:** the rug pull. Same geometry, every surface failed.
- **How:** `flow_edit_image` off the accepted S1 (golden), so the frame matches line for line.
- **Light:** flat grey overcast; no sun. **Anchor:** none needed yet — the bot's amber beacon becomes it in S3.
- **Cost in frame:** a burnt-out tracked machine, collapsed shopfront, weeds. No bodies.

### S3 — the bot
- **Job:** the friendly face the film never had, in the ruin.
- **Camera:** at the bot's height (~50cm), close, slightly off-axis; the ruined street soft behind.
- **Light:** overcast; the amber beacon is the one warm point in frame.
- **How:** `flow_edit_image` with two references — the robot still and the accepted S2.
- **Scale:** kerb, a fallen bunting flag, a shopfront doorway.

## Still prompts

Model: Nano Banana Pro, 16:9. Two briefs for S1, two candidates each.

**S1-a**
```prompt
Hyper-realistic photograph on 35mm film, landscape 16:9. An ordinary English market-town high street on a hot sunny Saturday in summer, seen from a locked camera slightly above head height, looking straight down the length of the street toward a stone church tower at the far end. In the near foreground, a large planter overflowing with bright red and yellow flowers. The street is full of cheerful, ordinary shoppers of all ages walking in loose groups, market stalls with striped awnings selling fruit and flowers, colourful bunting strung across the street between the shopfronts, and people sitting at tables outside a pub. Blue sky with a few white clouds, bright summer sun from behind camera left, saturated colour, crisp and clean, the feel of a glossy tourism advert. No readable text, no logos, shop signs indistinct.
```

**S1-b**
```prompt
Hyper-realistic photograph, landscape 16:9, bright and high-key like a holiday brochure. A traditional British town high street on a perfect summer Saturday, the camera fixed a little above head height and centred on the street, which runs away from us between two rows of brick and stone shopfronts. Hanging baskets of flowers on every lamp post, pastel bunting crossing overhead, a busy open-air market down the middle of the street, families, couples and older people strolling and chatting, an ice-cream van parked at the kerb, café tables on the pavement in full sun. Clean pavements, freshly painted shopfronts, deep blue sky, warm sunlight from the left, vivid saturated colour. No readable text, no logos, signage indistinct.
```

**S2** (edit off the accepted S1)
```prompt
Using the provided image, keep the exact same camera position, street layout, buildings, rooflines and composition, and change the moment to the same street five years after it was abandoned in a war. Remove every person, every market stall, the bunting and the flowers. The shopfronts are fire-blackened and gutted, windows empty, one facade partly collapsed into the street, weeds and grass growing through the cracked road, drifts of grey ash and debris against the kerbs, a burnt-out tracked military machine lying abandoned in the middle distance. The sky is flat grey overcast, no sunlight, the colour drained to cold grey. Keep everything else in the image in the same place. No people, no text.
```

**S3** (edit, two references: the robot still, then the accepted S2)
```prompt
Using the two provided images, show the small six-wheeled pavement delivery robot from the first image, with its grey box body and amber beacon light on a short stalk, now standing in the ruined street from the second image. Camera very low at the robot's own height, close to it and slightly to one side, the robot filling the left half of the frame, the ruined street and fire-blackened shopfronts softly out of focus behind. The robot is scuffed, dusty and dented, one torn strip of faded bunting caught on its wheel, and its amber beacon is lit, the only warm colour in a cold grey overcast scene. Fine film grain. No people, no text.
```

## Revision log

| When | What |
| --- | --- |
| 2026-09-29 | Sheet written from Kai's rulings |
| 2026-09-29 | Flow project `Sept 29 - 21:13` (id `0856c51d-0fac-4086-aeb1-c23c2d8039f6`), Nano Banana Pro, 0 credits, 0 blocks. **S1:** S1-a → `stills/s1/00-a|b.jpg`, S1-b → `01-a|b.jpg`. **S2:** the S2 edit run once off EACH S1 candidate → `stills/s2/s2-from-<id>.jpg`, so Kai picks matched pairs. Line-up (edge difference, lower is closer): 00-a 53.0 · 00-b 52.3 · 01-a 40.5 · 01-b 39.9. Pairs 1–2 lost the foreground planter in the wreck. **S3:** refs `es-robot-b.jpg` + `s2-from-01-b` → `stills/s3/s3-bot-01b-a|b.jpg`; + `s2-from-00-b` → `s3-bot-00b-a|b.jpg`. Glitch mocks (ffmpeg `rgbashift` + band `blend` + `noise`, stills only) per pair. Picking board: https://claude.ai/artifact/RcoYmozBesKFfKhk9rrADK (`picks/pair`, `picks/bot`, `notes/pairs|bots`). |
| 2026-09-29 | **Kai's picks (board):** pair **2** (`s1/00-b` + `s2/s2-from-00-b`), bot **C** (`s3/s3-bot-00b-a`). Notes: *"I really love the bunting"*; *"it would be quite funny if on S2 we had a couple of vape shops and betting shops that are also now obviously wrecked… very subtle."* Edit off the golden `s2-from-00-b` (x3 returned): `s2/s2-00-b-vape-bets-a|b|c.jpg`. a barely changed; **b subtle (VAPE left, BETS right, horse posters) — Claude's pick**; c louder. Put on the board as `picks/vape`. ⚠️ The bot frame's background still shows the pub sign; in b that shopfront became BETS. Soft focus, likely invisible — check at the edit. |
| 2026-09-29 | **Kai picked vape/bets C** (the louder one) → the S2 plate is `s2/s2-00-b-vape-bets-c.jpg`. Locked set: S1 `s1/00-b.jpg` · S2 `s2/s2-00-b-vape-bets-c.jpg` · S3 `s3/s3-bot-00b-a.jpg`. |
| 2026-09-30 | **Sound locked** (see `songs/narration.md` scene 4): happy clarinet `63ce479c` · sad clarinet `57c6ef18` (r6, three lines) · robot = Gemini TTS Aoede/Bristol r2-b. On `gpom-s01` A4/A5/A6 from 162.6s, ~60s. "Oh, fuck" is gone. **Eight dramatic shots proposed** (Kai: *"I really want the simulation section to feel dramatic"*), each a `flow_edit_image` off a locked still, Nano Banana Pro, 0 credits → `stills/proposed/`: F1 aerial reveal, F2 flowers close, F3 workers (❌ came back unchanged, re-roll owed), W1 wreck aerial, W2 vape+bets close, W3 bunting in an ash puddle (the pause frame), R1 robot tiny in the distance, R2 beacon close. Several "-a" candidates came back near-identical to the reference and were left off. Board rebuilt in the Downfall style (same URL, v3): the audio, the proposed cut in order, one strip per shot; picks in db `shots/<id>`, notes in `notes/order-0930` and `notes/shots-0930`. |
| 2026-09-30 | **Kai's picks (board db `shots/`):** F1 **b** · F2 **c** · W1 **a** · W2 **b** · W3 **b** · R1 **b** · R2 **a** (all seven kept, none cut). F3 workers still owed a re-roll. |
| 2026-09-30 | **The "Oi" section.** Narration `gpom-sim-oi` r72 (2 takes, unpicked). Nine stills proposed (0 credits) → `stills/proposed/o*`: O1 beacon off · O2 coin spinning · O3 cat in a delivery box · O4 two slits (light striping a floor) · O5 infinite streets (rough) · O6 coin landed heads · O7 pages blowing (the pen never appeared) · O8 the fake street frozen, mannequin shoppers, a grid in the sky · O9 a grate glowing warm (the humans below). "-a" came back unchanged on O3/O4/O5/O7. Board v4 adds the section and extends the running order (Oi timings estimated). |
| 2026-09-30 | **Part 2 rewritten by Kai — no "Oi".** *"The robot could actually be far more empathic."* She carries on: *"Anyway, I've got a few errands to run. Nice to meet you."* (breaking the fourth wall), then we **follow her driving around for ~10s, GTA-style**; passing a drain she hears **humans arguing**; the **kill bots are sent immediately**; only then does the **narrator cut in: "What's going on?"**; the robot: *"I've found human life. And you've sent the kill bots. Please stop them."* The coin/cat/slits exposition leaves this scene (stills kept). Kai's Oi-shot picks: O1 a · O2 a · O3 c · O4 c · O8 a · O9 b (the grate = the drain); cut O5, O6, O7. **Video go given:** 16 clips (the 10 scene stills + the 6 Oi picks), Veo 3.1 Fast, camera locked, 8s → `clips/simulation/video/`. |
| 2026-09-30 (late) | **Robot re-voiced (Gemini TTS round r4, paid key).** Kai's tagged script (narration.md, opening → "Mind how you go") as ONE take: 6 tries, only `full-a` complete (81.84s); b–f truncated (46/31/22/41/21s). Also voiced as three pieces (block1 ×2, why ×2, bye ×2; several short tries discarded). Files `clips/simulation/audio/bot-tts-r4/`, imported to bin `simulation`. **Timeline `gpom-s01`:** `bot-r4-full-a-81s` replaces r2-b on A6 at 198.125 (ends 279.96); bed2 on A7 (Kai had set −2.8 dB) keyframed to −12 dB under the voice (source 3.3–84.9s). **Animations:** all 16 from the `sim-animate` agent (Veo 3.1 Fast, 8s, 1280×720, ~320 credits computed; 5 of 16 lost by flow-mcp's save bug and recovered) → `clips/simulation/video/01…16`, bin `simulation-video`, on **V3** scaled 150%: happy 01–03 from 163.96 · sad 04–07 ~3.2s each from 185.46 · robot 08–16 butted from 198.125 to 270.125. Rough lay, NOT synced to the words (no listen). 270–280 (the goodbye) has no picture: the follow-the-robot drive stills are owed. Veo's own sound landed on A1 and was removed during the session (Kai editing live). |
