---
title: Camping — the genre sweep (aggression and pace)
status: ROUND g1 — 2026-08-27, six genres over the drum and bass, each run BOTH as a cover of the h12 take and fresh from scratch. Verdict pending.
brief: Jack, 2026-08-27 — "I think we have lost the aggression and the pace, I think maybe experiment with different genres over the drum and bass."
source_take: "Camping HT AJ rap-rock W45 (h12)" (03:14) — attached by hand for the COVER half only
parent_sheet: ./camping-halftime.md
cover_sheet: ./camping-halftime-cover.md
words_canon: ./camping.md  # §4 — the words, unchanged by this experiment
workspace: camping-duet
model: v5.5
---
# Camping — the genre sweep

**This sheet is the whole prompt.** The runner parses the lane fences below verbatim. Edit the
markdown, not the script.

| | |
|---|---|
| **The runner** | [`scripts/suno/genre-sweep.mts`](../../../../scripts/suno/genre-sweep.mts) |
| **Where takes land** | workspace `camping-duet` |
| **Titles** | `Camping <genre> cover (g1)` and `Camping <genre> fresh (g1)` — named so Jack can pick by ear without a key |
| **The words** | [`camping.md`](./camping.md) §4 is canon; the cover half inherits them, the fresh half writes them from [`camping-halftime.md`](./camping-halftime.md) §4 |

---

## 🔴 Why the aggression went, and what this sweep changes about it

Jack is right, and like the c1 "cheesy" note the cause is **our own prompt vocabulary**, not Suno.
Every move of the anti-cheese pass (c2) was *subtractive*, and subtraction is what we got:

| What we wrote to kill the cheese | What it also killed |
|---|---|
| `flat deadpan spoken-word vocal` | **the aggression** — deadpan is the opposite of force |
| `dry, raw, no polish, no radio sheen` | the weight and the impact of the mix |
| `never anthemic`, `bleak, mechanical` | any sense of the track building |
| Lane C's `almost nothing on top`, `the space is the point` | the density that reads as energy |
| `double time` **in the exclude list** | literally the word for pace |
| the whole parent sheet is **half-time** | 174 BPM that *feels* like 87 |

**So pace and force are fixed in the shared HEAD/TAIL of every lane, and the genre is the only
variable.** Across all six lanes the vocal is now **barked, spat and rising in force** rather than
deadpan, the drums are **full tempo with no half-time and no pace-dropping breakdown**, and
`half-time`, `halftime` and `double time` have changed sides in the exclude list.

🔴 **This is a deliberate, reversible bet.** `deadpan` was doing real anti-cheese work — it is why
the men stopped drifting off the beat. If the sweep comes back energetic but cheesy again, the
answer is not to restore `deadpan` wholesale but to keep `barked` and re-add `never sung, no
melody in the voice`, which is the half of it that was actually load-bearing.

## The design

**Six genres × two modes = 12 creates, 24 takes.** One slider setting throughout — Style Influence
75, Weirdness 45, and Audio Influence 25 on the cover half — because **the variable under test is
genre**, not the sliders. Honing in on sliders is the round *after* Jack picks a direction.

Running each genre **both ways** answers a question the cover-only rounds could not: how much of
what we are hearing is the genre, and how much is the 3:14 rap-rock source dragging every cover
back toward itself. Same genre, same words, one built on the old take and one built from nothing.

🔴 **The two halves cannot run back to back unattended.** Cover mode needs the source audio
attached in the page and fresh mode needs it *gone*, and attaching or removing it is a hand
action (song page → ⋯ → Remix ▸ Cover, or the × on the attachment). The cover half runs first
because the attachment is already loaded.

## 🔴 Per-lane four-box atoms

Every lane below carries **its own Style, its own My Taste and its own Exclude** — three fences,
not one shared list. That is the four-box atom (Kai, 2026-08-27) taken to its conclusion, and it
exists because a shared exclude list *cannot* serve six genres: `power chords` has to be banned
for neurofunk and **allowed** for hardcore punk, `guitar` banned for jungle and required for
industrial. A shared list would silently fight half the sweep — which is exactly the bug that has
now cost us three rounds (h10 lead guitar, h11 dub piano, c4 operatic vocals).

The runner **throws offline** if any lane is missing any of its three fences.

---

## Lanes

### Lane `neurofunk` — Neurofunk

*style 829 · exclude 731 · taste 1109*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. A growling, morphing reese bass is the lead instrument — metallic, technical and machine-precise, edits snapping tight, ratcheting percussion, cold sci-fi menace, and no melody anywhere. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. The lead instrument is a growling, morphing reese bass — metallic, technical, machine-precise, with ratcheting percussion and cold sci-fi menace. No melody instrument at all.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, grime MC, UK drill, road rap, trap, young MC, American accent, ragga MC, Jamaican accent, choir, orchestral strings, violins, piano, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, guitar, acoustic guitar, power chords, guitar solo, live rock band
```

### Lane `jungle` — Jungle

*style 830 · exclude 742 · taste 1092*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. 1994 jungle: amen breaks chopped fine and ragged, timestretched hits flying across the bar, a huge round sub underneath, rowdy and raw off cheap tape, pirate-radio energy, no MC toasting. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. 1994 jungle: amen breaks chopped fine and ragged, timestretched hits, a huge round sub, rowdy and raw off cheap tape, pirate-radio energy and no MC toasting.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, grime MC, UK drill, road rap, trap, young MC, American accent, ragga MC, Jamaican accent, choir, orchestral strings, violins, piano, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, guitar, acoustic guitar, power chords, guitar solo, live rock band, neurofunk
```

### Lane `industrial` — Industrial metal

*style 832 · exclude 761 · taste 1116*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. Industrial metal on top: hammering sheet-metal percussion doubling the kick, a detuned guitar chugging in short violent bursts, clanging factory noise, everything overdriven and mechanical. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. Industrial metal on top: hammering sheet-metal percussion doubling the kick, a detuned guitar chugging in short bursts, clanging factory noise, everything overdriven and mechanical.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, grime MC, UK drill, road rap, trap, young MC, American accent, ragga MC, Jamaican accent, choir, orchestral strings, violins, piano, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, guitar solo, shred, hair metal, symphonic metal, gothic metal, power ballad, melodic lead guitar
```

### Lane `breakcore` — Digital hardcore

*style 830 · exclude 730 · taste 1101*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. Digital hardcore: breakbeats overdriven until they clip, distorted kicks, sirens and alarms cutting across, sudden stutter edits, riot noise underneath, the whole mix pushed into the red. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. Digital hardcore: breakbeats overdriven until they clip, distorted kicks, sirens and alarms, sudden stutter edits, riot noise underneath, the mix pushed into the red.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, grime MC, UK drill, road rap, trap, young MC, American accent, ragga MC, Jamaican accent, choir, orchestral strings, violins, piano, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, guitar solo, shred, melodic synths, hair metal, gabber, hardstyle
```

### Lane `hardpunk` — Hardcore punk

*style 810 · exclude 762 · taste 1107*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. Hardcore punk guitar on top: fast downstroke power chords buzzing at full tempo through a cheap trebly amp, in short violent bursts, no melody, no harmony and no solo. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. Hardcore punk guitar on top: fast downstroke power chords buzzing at full tempo through a cheap trebly amp, in short violent bursts, with no melody, no harmony and no solo.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, grime MC, UK drill, road rap, trap, young MC, American accent, ragga MC, Jamaican accent, choir, orchestral strings, violins, piano, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, guitar solo, shred, hair metal, harmonized twin lead, melodic lead guitar, chiming guitar, jangle
```

### Lane `bigbeat` — Big beat

*style 819 · exclude 736 · taste 1112*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. Big beat: fat distorted breaks squashed by heavy compression, rising filtered noise sweeps, a swaggering dirty bassline, all attack and swing, loud and grimy rather than bleak. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. Big beat: fat distorted breaks squashed by heavy compression, rising filtered noise sweeps, a swaggering dirty bassline, all attack and swing — loud and grimy rather than bleak.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, grime MC, UK drill, road rap, trap, young MC, American accent, ragga MC, Jamaican accent, choir, orchestral strings, violins, piano, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, guitar solo, shred, acid house, trance, hair metal, melodic lead guitar
```

### The g2 four — added 2026-08-27 on Jack and Kai's picks

`hiphop`, `grime`, `grunge` and `metal`. 🔴 **The MC and accent bans came out of the shared spine
and moved into the lanes**, because they were written for a sheet that had no hip-hop in it:
`grime MC`, `UK drill`, `road rap`, `young MC`, `ragga MC` and `Jamaican accent` are banned in the
eight lanes that do not want them and **allowed in `hiphop` and `grime`, which are made of them**.
`American accent` stays banned everywhere — the casting is British in every lane.

`metal` is the one lane where **`guitar solo` is allowed**: Jack asked for pure metal and a metal
lane without one is not the thing he asked for. It is fenced instead by banning the melodic
versions of it — `hair metal`, `glam metal`, `shred`, `sweep picking`, `harmonized twin lead`,
`power metal`, `symphonic metal` — so what is left is a short savage one. `grunge` keeps its solo
ban: the loud-quiet swing is the point, and `post-grunge` (the radio version) stays banned too.

### Lane `hiphop` — Boom-bap hip-hop

*style 888 · exclude 722 · taste 1149*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. A dusty boom-bap hip-hop layer on top — a filtered soul sample chopped hard on an MPC, vinyl crackle and tape hiss over everything, a fat swung snare landing across the breakbeat, scratched turntable cuts, all head-nod weight and no melody line. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. A dusty boom-bap hip-hop layer on top — a filtered soul sample chopped on an MPC, vinyl crackle and tape hiss, a fat swung snare across the breakbeat, scratched turntable cuts. Head-nod weight, never a melody line.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, American accent, choir, orchestral strings, violins, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, trap, trap hi-hats, mumble rap, drill, road rap, young MC, guitar, guitar solo, live rock band, jazz rap, conscious rap, smooth soul hook
```

### Lane `grime` — UK grime

*style 854 · exclude 714 · taste 1117*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. A UK grime layer on top — cold square-wave bass stabs, icy sparse synth hits landing in eights, eski clicks and metallic percussion, skeletal and menacing, pirate-radio energy, everything hard, dry and unlovely. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. A UK grime layer on top — cold square-wave bass stabs, icy sparse synth hits in eights, eski clicks and metallic percussion, skeletal and menacing, pirate-radio energy, hard and dry.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, American accent, choir, orchestral strings, violins, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, trap, drill, road rap, young MC, ragga MC, Jamaican accent, guitar, guitar solo, live rock band, afroswing, smooth R&B, sung hook
```

### Lane `grunge` — Grunge

*style 877 · exclude 764 · taste 1132*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. A grunge guitar layer on top — thick detuned fuzz chords dragging half a hair behind the beat, sludgy and downtuned through a blown speaker, sudden loud-quiet swings, feedback left ringing between them, no solo and no polish anywhere. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. A grunge guitar layer on top — thick detuned fuzz chords dragging behind the beat, sludgy and downtuned through a blown speaker, sudden loud-quiet swings, feedback left ringing. No solo, no polish.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, American accent, choir, orchestral strings, violins, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, grime MC, UK drill, road rap, trap, young MC, ragga MC, Jamaican accent, guitar solo, shred, hair metal, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, britpop
```

### Lane `metal` — Metal

*style 891 · exclude 801 · taste 1161*

```style
Dark drum and bass at 174 BPM, minor key, full tempo and relentless — no half-time anywhere, no breakdown that drops the pace. Chopped amen breakbeats rolling hard the whole way, sub bass underneath. British spoken-word vocal on top, barked and metrical, locked to the beat and rising in force as it goes — spat, not crooned, never sung, no chorus, no hook. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn. Verse two, a well-spoken British man: higher, clean, plummy BBC English, from a wide room. A pure metal layer on top — fast tremolo-picked riffs and palm-muted galloping chugs on a downtuned guitar, double-kick drumming doubling the breakbeat, pinch harmonics screaming out of it, and one short savage solo, aggressive rather than melodic. Dry, raw and close-mic'd — no polish, no radio sheen. Bleak, hostile and aggressive from the first bar to the last.
```

```taste
Vocals: British spoken-word — barked, metrical, locked to the beat at full 174 and rising in force, spat rather than crooned, never sung and never rapped over a melody. Two white British men in their late forties and fifties, and they must stay two different men. One is low, gravelly and smoke-worn, into a cheap close mic: a working-men's-club voice. The other is higher, clean and plummy BBC English, unhurried, from a wide room.

Music: dark drum and bass at 174 BPM, minor key, full tempo and relentless. No half-time, no breakdown that kills the pace. Chopped amen breakbeats rolling hard, sub bass first and loudest. No chorus anywhere on this record. A pure metal layer on top — fast tremolo-picked riffs and palm-muted galloping chugs on a downtuned guitar, double-kick doubling the breakbeat, pinch harmonics, and one short savage solo that is aggressive rather than melodic.

Register: bleak, dystopian, angry and completely serious. Dry, raw and close-mic'd — no polish, no radio sheen. Machine-cold, hostile and aggressive. Never anthemic, never jaunty, never feel-good.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung verses, sung chorus, vocal hooks, clean sung melody, crooning, autotune, harmonies, nu metal, rap rock, pop punk, post-grunge, emo, radio rock, arena rock, anthemic, big chorus, gang vocals, polished production, American accent, choir, orchestral strings, violins, marching band, oompah, dixieland, reggae, ska, 2 tone, offbeat guitar, skank rhythm, music hall, pantomime, liquid dnb, jump up, feel good, festival, happy hardcore, bright synths, euphoric, pop, jaunty, bouncy, comedic, parody, uplifting, major key, half-time, halftime, slow tempo, tempo change, vamp, outro jam, grime MC, UK drill, road rap, trap, young MC, ragga MC, Jamaican accent, hair metal, glam metal, shred, sweep picking, harmonized twin lead, symphonic metal, gothic metal, power metal, power ballad, clean sung chorus
```

---

## Round log

### g1 — 2026-08-27, the genre sweep. **Verdict pending.**

Jack on the c4 flair takes: **"we have lost the aggression and the pace."** Kai's instruction was
to widen rather than tune — *"a wide range of options to just see what they sound like, then we
can start to hone in on one once I get Jack's opinion."* So g1 deliberately spends its budget on
**spread, not depth**: one slider setting, six genres, two modes each.

The six were picked to cover genuinely different mechanisms of aggression rather than six shades
of one idea — two from inside drum and bass (**neurofunk**, aggression from bass design;
**jungle**, aggression from break editing and speed), two heavy (**industrial metal**, aggression
from hammering percussion and detuned chugs; **digital hardcore**, aggression from distortion and
riot noise), one guitar-led (**hardcore punk**, the one lane where `power chords` are *allowed* —
they are the sound, and pop-punk is fenced off by `no melody, no harmony, no solo`), and one
outlier (**big beat**, loud and grimy rather than bleak, included precisely because it is the only
one that is *fun*).

**Cover half: 6/6 clean, 12 takes.** Every lane passed the cover / lyric-paragraph / Voice /
style-length / exclude-length / Duration-is-Auto guards, and the freedom token was released *and
re-verified over a fresh connection*.

🔴 **The token guard fired for real, and it was right to.** The first attempt aborted before
spending anything: My Taste held **c4's lane-D flair profile**, despite the c4 run having reported
a successful release at the end. Setting the token and re-reading it directly held fine for 33
seconds under test, so the write works and **something re-installed the old profile in a gap we
cannot see. The cause is UNKNOWN — do not write it up as understood.** What changed is detection:
`genre-sweep.mts` now re-reads the box over a *new browser connection* after releasing it, which
is the only check that would have caught this one.

🟡 **One caveat on the c3c duration finding.** This round ran on Auto, and one Industrial metal
take still came back **4:00** while its own pair came back 3:15. So Auto can reach 4:00 by itself,
and the c3c evidence is weaker than "240 caused it" — what remains true is that **12/12 c3c takes
clustered at 3:59–4:00 while Auto rounds spread across 3:10–4:00**. Pinning is still the suspect;
it is no longer the proven cause.

**Fresh half: 10/10 clean, 20 takes.** Run after the create form was cleared by hand, which
removed the cover attachment and so *unblocked* the half that had been waiting on it. Lyrics were
written from `camping-halftime.md` §4 (71 paragraphs) and checked against `camping.md` §4 before
the first Create; no Voice; Duration on Auto; token claimed and released, and the release
re-verified over a fresh connection.

**Standing at the end of g1: 32 takes.** Six genres heard **both** ways (cover + fresh) and four —
`hiphop`, `grime`, `grunge`, `metal` — heard fresh only, because their covers need the source
re-attached by hand. That asymmetry is worth stating to whoever judges them: a fresh take and a
cover of the same genre are not the same test.

🟡 **A rendering trap worth knowing:** while a take is still generating, its card shows the title
*with the Style box text run on after it*, so a listing taken too early reads
`Camping Metal fresh (g1) Dark drum and bass at 1…`. Re-listing once rendering finishes shows the
clean title. **Do not "fix" a title on the strength of a listing taken during generation.**

🔴 **Named artists stay out**, as of the 2026-08-26 `Linkin Park` flag. Every one of these is a
genre term or a description, never an act.
