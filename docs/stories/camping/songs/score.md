---
title: Camping — the background score (story video)
status: generated 2026-09-17, 36 takes, unheard
model: v6
settings: SI 75 · weirdness 30 and 60 (the pair) · Variety Normal · Max Mode off · Vocal Gender unset · Personalize off · no Voice · instrumental (no lyrics) · durationSec per cue · workspace camping-Jack
---

# Camping — the background score

**Jack, 2026-09-17:** *"add suno background cinematic music throughout, please analyse the video as a whole and choose
what music where."* This is the story video, `camping jack` › `0 synced`, 290.1s. It isn't the Camping song, which has
its own sheet and project.

**How it was chosen:** all 66 clips exported as frames and read as contact sheets, with the narration (A3) laid against
them. **Nine cues**, one per movement of the story, each built for its own scene rather than as one track re-costumed.
Every cue is an instrumental bed under narration: sparse in the middle frequencies where the voice sits, with no lead
melody fighting the words.

🔑 **Two rulings inside the plan:**
- **The crash stays silent.** Cue 2 cuts dead at 65.1 on the cut to black, and nothing plays until 2026. Canon:
  *impact, then silence* (`story.md`, `assembly.md`).
- **The film is bookended by one motif.** Cue 1's ticking ostinato (2008, the machine that made him) comes back
  slowed and broken under the burning newspaper and the `BAD C0DE` plate. ⬜ Best made as a **Cover** of the chosen
  Cue 1 take, so the melody actually matches. The Cue 9 prompt below is the fallback if the Cover doesn't work.

## The cue map

| Cue | Timeline | What's on screen | Music job | durationSec |
| --- | --- | --- | --- | --- |
| **1 · The machine** | 0.0–37.7 | 2008 skyline, trading floor, Tarquin's grind montage | arrogant, relentless ticking pulse | 45 |
| **2 · The last good day** | 37.7–65.1 | Bob and Jo, the lane, the café, the car laughing | warm, fragile, hopeful. **Hard cut at 65.1** | 35 |
| 🔇 **silence** | 65.1–69.9 | the crash, the wrecked lane | nothing | none |
| **3 · The top floor** | 69.9–100.9 | 2026, the Shard, the X8, homeless through the glass, the smile, and the smile fading | cold, glossy, detached. Thins to one note at 97.9 | 40 |
| **4 · The tent** | 100.9–119.2 | Waitrose in the rain, the tent, Bob's POV | bleak, lonely, grey | 25 |
| **5 · The couch** | 119.2–139.2 | therapy | dry, deadpan, awkward, played straight | 25 |
| **6 · Two bays** | 139.2–192.5 | the drive, the X8 arrives, the standoff, the aerials | slow-burn showdown tension | 60 |
| **7 · The trip** | 192.5–256.1 | forest, yurt, the eye, the mug, the kaleidoscope, the bad trip | serene, then an overwhelming nightmare | 70 |
| **8 · Five years later** | 256.1–275.4 | into the dome, the bed, wakes in the tent, fear, the camp wide | dread, one hit on the reveal | 25 |
| **9 · BAD C0DE** | 275.4–290.1 | the newspaper burns, the plate | the motif returns, a final hit, ring-out | 25 |

**Mix (human, in Premiere):** beds sit well under the voice, roughly −20 to −24 dB against the narration, and duck
further under each A3 line. Crossfade each cue into the next one by hand. ⬜ The bridge has no audio-level or audio-
transition API that's been proven (`assembly.md`).

---

🔎 **Research pass, 2026-09-17 (web, community):**
- Put *Instrumental* first in Style and keep vocals in Exclude. The community's third layer, an `[Instrumental]` lyric tag, isn't used: v6's lyrics box says *"leave this empty for instrumental"*, so empty is the native switch ([hookgenius](https://hookgenius.app/learn/suno-instrumental-prompts/), [freesongwritingtools](https://freesongwritingtools.com/blog/how-to-make-suno-instrumental/)).
- 60–75 BPM and *steady, minimal variation* for beds under dialogue ([suno.bi](https://suno.bi/en/blog/instrumental-music-from-text-prompts-7-tips-sunomv-2026)).
- Suspense cues work from drones, pulses and low strings, not melody ([hookgenius film score](https://hookgenius.app/learn/suno-film-score-prompts/)).
- Keep Exclude lists short and related ([Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide)).

Every cue's Lyrics box is **empty**, which `suno.mts` clears for an instrumental atom.

#### cue-1-machine

Style:

```
Instrumental hybrid film score at 120 BPM: a relentless ticking synth ostinato, pulsing low staccato strings and cheap synth strings driving like a trading floor, deep braams underneath, arrogant, cold and unstoppable. Sparse in the midrange, a steady bed under narration.
```

Exclude styles:

```
vocals, singing, choir, humming, vocal chops, piano ballad, acoustic guitar, happy, comedic
```

#### cue-2-last-good-day

Style:

```
Instrumental British indie film underscore at 72 BPM: one fingerpicked acoustic guitar and a soft felt piano, warm, fragile, hopeful and intimate, a family road trip on a grey morning. Steady, minimal variation, close and quiet, no drums.
```

Exclude styles:

```
vocals, singing, humming, whistling, drums, synth, orchestral swell, braams, country
```

#### cue-3-top-floor

Style:

```
Instrumental cold minimal electronic score at 90 BPM: an icy analogue synth arpeggio and glassy high pads over a slow sub pulse, sleek, expensive and emotionally detached, a city at night from the top floor. Spacious and sparse, a steady bed under narration.
```

Exclude styles:

```
vocals, singing, choir, humming, acoustic guitar, piano, orchestral, lo-fi, hip hop, happy
```

#### cue-4-tent

Style:

```
Instrumental bleak British social-realist underscore at 60 BPM: one low solo cello and a distant, slightly detuned upright piano, long pauses between phrases, rain-soaked, grey and lonely. Steady, minimal variation, very sparse, no drums.
```

Exclude styles:

```
vocals, singing, choir, humming, drums, synth, orchestral swell, braams, uplifting, sentimental
```

#### cue-5-couch

Style:

```
Instrumental dry deadpan chamber underscore at 70 BPM: a hesitant plucked pizzicato motif, a soft ticking clock pulse and a single low clarinet, awkward, patient and quietly absurd, played completely straight. Steady, minimal variation, lots of air.
```

Exclude styles:

```
vocals, singing, humming, comedic, cartoon, whimsical, quirky, kazoo, ukulele, whistling, drums
```

#### cue-6-two-bays

Style:

```
Instrumental slow-burning standoff score at 70 BPM, hybrid orchestral: a low heartbeat kick, a tremolo string drone climbing slowly, cheap synth strings and distant brass braams, grey and cold like a western showdown in the rain, tension building and never released.
```

Exclude styles:

```
vocals, singing, choir, humming, whistling, western guitar, harmonica, piano, drop, triumphant, heroic
```

#### cue-7-trip

Style:

```
Instrumental dark cinematic trip score that starts serene and turns into a nightmare: a warm drone and soft reversed textures bloom into swirling detuned synths, backwards cymbals, a huge distorted orchestral swell and pounding war drums, overwhelming and disorienting.
```

Exclude styles:

```
vocals, singing, choir, chanting, humming, psychedelic rock, electric guitar, sitar, trance, EDM drop
```

#### cue-8-five-years

Style:

```
Instrumental dread-soaked dark ambient score: a low sub drone, storm rumble and a slow heavy heartbeat, one sharp orchestral hit, then a vast bleak swell of cheap synth strings over a ruined world. Sparse, no melody.
```

Exclude styles:

```
vocals, singing, choir, humming, piano, acoustic guitar, groove, beat, hopeful, heroic
```

#### cue-9-bad-code

⬜ **First choice: a Cover of the chosen Cue 1 take** with this Style box. **Fallback:** this plain instrumental, which is what's generated now.

Style:

```
Instrumental elegiac hybrid film-score finale at 70 BPM: a ticking synth ostinato returns slowed down and broken, warm cheap synth strings rise under a crackling fire, one huge final braam and impact, then a long ring-out into silence. Bittersweet and defiant.
```

Exclude styles:

```
vocals, singing, choir, humming, piano ballad, acoustic guitar, happy ending, triumphant, beat drop
```

## ✅ Generated 2026-09-17 · workspace `camping background music`

All 9 cues as pairs: 18 Creates, 36 takes. Credits went 3,310 → 3,090 (220). Most Creates cost 10. A few read 20, probably the balance being read mid-update (unconfirmed). Every load passed its checks.
🔑 **Duration control works on v6:** every take landed within about 10s of its target, most within 1s. ⬇️ **Downloading is a human step** (Suno's monthly cap).

| Cue | w30 | w60 |
| --- | --- | --- |
| 1-machine | [afc47947](https://suno.com/song/afc47947-c25f-4ac8-8b79-6b2db38bf76c) 45s · [94f3e606](https://suno.com/song/94f3e606-4b6f-4982-917b-b2bb8d891204) 45s | [63c42c00](https://suno.com/song/63c42c00-0f39-402f-aca9-8e460ee201b4) 46s · [47c3b4b5](https://suno.com/song/47c3b4b5-bf07-4f10-85c0-d24ff948a37f) 46s |
| 2-last-good-day | [284b6b99](https://suno.com/song/284b6b99-a87c-463b-99bf-afa7abed012d) 38s · [670b092b](https://suno.com/song/670b092b-5f07-4519-a41a-def6546a401a) 44s | [ac36f362](https://suno.com/song/ac36f362-5915-4614-b952-8ba459044812) 35s · [b326f6b0](https://suno.com/song/b326f6b0-4dd5-4cbd-9ab4-ae5ccc86c348) 37s |
| 3-top-floor | [5b570801](https://suno.com/song/5b570801-d2d6-41d4-b4ff-04defcb03b30) 49s · [2398d386](https://suno.com/song/2398d386-6d92-4dc2-8494-fd4662dcd4ae) 48s | [192bdabe](https://suno.com/song/192bdabe-92dc-4318-bfc9-9df38382ae25) 44s · [004200ce](https://suno.com/song/004200ce-89e4-4f6d-b162-52124561b447) 40s |
| 4-tent | [7a7069f2](https://suno.com/song/7a7069f2-6fce-402f-9136-a7a5aa796104) 25s · [5c9a169b](https://suno.com/song/5c9a169b-2c86-4fff-9391-4c3cf74814c4) 27s | [d2a5cda1](https://suno.com/song/d2a5cda1-e9f7-4edb-96f7-525b0167be9f) 25s · [4c0e5ba2](https://suno.com/song/4c0e5ba2-2482-418d-bf19-4e89f2663035) 25s |
| 5-couch | [98afdd7d](https://suno.com/song/98afdd7d-cbb5-466c-8dc3-bf29db24b461) 26s · [79ff9fe8](https://suno.com/song/79ff9fe8-77a2-43cc-88f0-457e732da6fd) 25s | [cff6495b](https://suno.com/song/cff6495b-6bc6-4671-b81f-107dcbdad7af) 26s · [e205e524](https://suno.com/song/e205e524-3e30-4013-8e98-3c4d860caffa) 25s |
| 6-two-bays | [94f3e2f5](https://suno.com/song/94f3e2f5-39fb-468e-9da7-b41880545c25) 63s · [0dfc7451](https://suno.com/song/0dfc7451-f3af-432d-ae9b-d31f71542bce) 60s | [30d6950a](https://suno.com/song/30d6950a-9f9a-4c6d-a4b7-e8c4f1722353) 61s · [0d2c97ad](https://suno.com/song/0d2c97ad-e6ac-4f2c-a517-37a64a9ea7b1) 59s |
| 7-trip | [5fae6377](https://suno.com/song/5fae6377-7666-45a5-84fd-a5c6891fca1b) 70s · [7f4d9711](https://suno.com/song/7f4d9711-7c7f-4c62-93d9-688365e3020e) 70s | [37308370](https://suno.com/song/37308370-9d2c-442a-95f3-0219f5f11bc2) 70s · [8feec1c2](https://suno.com/song/8feec1c2-fb99-41e9-8c9f-c292673c0fc9) 70s |
| 8-five-years | [037394d2](https://suno.com/song/037394d2-10cf-4112-acb6-015535773a54) 25s · [d77689f1](https://suno.com/song/d77689f1-aeea-4784-9693-65a42fff6826) 25s | [1db59eb0](https://suno.com/song/1db59eb0-8565-4611-a3f7-764a5a17f01f) 28s · [58eca931](https://suno.com/song/58eca931-c97f-40a7-a6e4-737b822a0b22) 26s |
| 9-bad-code | [e44d37f8](https://suno.com/song/e44d37f8-6084-4a58-b12a-5214456d539e) 28s · [f7bae8c3](https://suno.com/song/f7bae8c3-21c4-4d5c-89c1-a7a0406b43ad) 26s | [3d08b4df](https://suno.com/song/3d08b4df-ae4f-46ad-8f2e-e01cdb1148a1) 37s · [ac3b6f74](https://suno.com/song/ac3b6f74-b22c-4ddf-8280-6f21fbd48726) 26s |

⬜ Nobody has listened yet.
