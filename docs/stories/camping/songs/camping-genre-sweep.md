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

## 🔴 g2 — the lanes were 78% identical, and that was the real bug

Kai, 2026-08-27, looking at the take list: *"it looks like every single style prompt is exactly the
same."* He was right, and the measurement is worse than the screen implied. Between any two g1
lanes:

| Box | Identical | Unique |
|---|---|---|
| Style | 644 of 829 chars | **22%** |
| My Taste | 936 of 1109 chars | **16%** |
| Exclude | 731 of 731 chars | **0%** |
| Lyrics | all of it | 0% (correct — it is the same song) |

**And the unique 22% sat at character 528**, behind a shared HEAD, so Suno's take list — which
shows the opening of the Style box — displayed the *same first 200 characters* for all ten.

🔴 **This was a design error, not a display artefact.** g1 held a common HEAD and TAIL constant on
purpose, to isolate genre as the single variable. That is good experimental method and it is the
wrong instrument for this job: Kai asked to **lean all the way into each style**, and Jack's
complaint that everything sounds samey is the predictable consequence of ten prompts that agree on
78% of their words — including every production instruction (`mixed like a dub soundsystem`,
`dry, raw and close-mic'd`, `chopped amen breakbeats`), which is precisely the vocabulary that
decides what a record *sounds* like.

**What g2 changes.** Each lane is now written **from scratch in its own idiom**. Only three things
are shared, because only three things are actually the song:

1. **The casting** — two British men, spoken, barked, never sung.
2. **174 BPM drum and bass as the foundation** — Jack's brief was genres *over* the drum and bass.
3. **The words.**

Everything else is the genre's own language. Neurofunk is `surgical, on the grid, wide precise
stereo`; jungle is `cut raw to cheap tape — hiss, saturation, clipping`; boom-bap is `mixed almost
mono, sampler-crushed`; metal is `quad-tracked, mids scooped`. **The genre clause now comes first**,
so the take list shows what each one is.

The exclude spine shrank from sixty terms to **eleven** — only what is true in every genre — and
the rest is per-lane. A shared ban list is itself a flattening force: `guitar` banned across the
board is a decision about *sound*, and it was being applied to lanes built on guitars.

## Lanes

### Lane `neurofunk` — Neurofunk

*style 618 · exclude 281 · taste 673*

```style
Neurofunk at 174 BPM, minor key. A growling reese bass morphs bar to bar and is the only melodic thing in the record. Drums surgical and snapping: tight cracking snare, clipped hats, every edit exactly on the grid. Cold metallic sound design, sci-fi menace, filtered risers into each drop, deep clean sub, wide precise stereo. Loud, controlled and machine-perfect. Bleak and clinical. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: neurofunk at 174 BPM. A morphing growling reese bass is the lead and the only melody. Surgical snapping drums, clipped hats, everything exactly on the grid. Cold metallic sound design, sci-fi menace, deep clean sub, wide precise stereo.

Register: clinical, bleak, machine-perfect and menacing.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar, live rock band, acoustic instruments, jungle breaks, lo-fi, tape hiss, warm analogue, jazzy chords, liquid dnb, jump up, euphoric, festival
```

### Lane `jungle` — Jungle

*style 585 · exclude 292 · taste 668*

```style
1994 jungle at 174 BPM. Amen breaks chopped fine and ragged, timestretched hits flung across the bar, ride cymbal chattering, fills that fall over themselves. A huge round sub bass under everything. Cut raw to cheap tape — hiss, saturation, clipping, no polish anywhere. Rowdy pirate-radio energy, dub sirens and air-horn stabs. Dark, alive and rough. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: 1994 jungle at 174 BPM. Amen breaks chopped fine and ragged, timestretched hits, chattering ride, a huge round sub. Cut raw to cheap tape — hiss, saturation, clipping. Dub sirens and air-horn stabs, pirate-radio energy.

Register: rowdy, dark, rough and alive. Never clean, never polished.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar, live rock band, neurofunk, clean modern production, polished mix, ragga MC, Jamaican accent, liquid dnb, jump up, euphoric, happy hardcore, piano riff
```

### Lane `industrial` — Industrial metal

*style 559 · exclude 288 · taste 667*

```style
Industrial metal over a 174 BPM breakbeat. Hammering sheet-metal percussion doubling the kick, a detuned guitar chugging in short violent bursts, clanging factory noise, a distorted machine drone holding underneath. Everything overdriven and squashed to the edge of the meter, cold, rusted and mechanical. Brutal and inhuman. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: industrial metal over a 174 BPM breakbeat. Hammering sheet-metal percussion doubles the kick, a detuned guitar chugs in short violent bursts, factory noise clangs, a distorted machine drone sits underneath. Overdriven and squashed to the edge.

Register: brutal, rusted, cold and inhuman.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, symphonic metal, gothic metal, power ballad, melodic lead guitar, clean guitar, acoustic guitar, orchestral strings, choir
```

### Lane `breakcore` — Digital hardcore

*style 573 · exclude 273 · taste 664*

```style
Digital hardcore at 174 BPM and feeling faster. Breakbeats overdriven until they clip and tear, kicks blown out, gunshot snares, sudden stutter edits and hard gates. Sirens and alarms cutting across, riot noise and crowd chaos underneath. The mix shoved into the red on purpose — distortion IS the production. Violent, chaotic and hostile. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: digital hardcore at 174 BPM. Breakbeats overdriven until they clip and tear, blown-out kicks, gunshot snares, stutter edits, sirens and alarms, riot noise underneath. The mix is deliberately in the red — distortion is the production.

Register: violent, chaotic, hostile and political.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar solo, shred, melodic synths, clean production, polished mix, gabber, hardstyle, happy hardcore, euphoric, trance, orchestral strings
```

### Lane `hardpunk` — Hardcore punk

*style 559 · exclude 299 · taste 654*

```style
Hardcore punk over a 174 BPM breakbeat. Fast downstroke power chords buzzing through a cheap trebly amp, distorted bass guitar shadowing them, drums played like a live kit — ride bell, crash on every turnaround, cymbals bleeding into everything. Cut in a room in one take, mid-heavy and shouty. Furious, shambolic and urgent. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: hardcore punk over a 174 BPM breakbeat. Fast downstroke power chords through a cheap trebly amp, distorted bass shadowing, drums played like a live kit with cymbals bleeding into everything. Cut in a room in one take.

Register: furious, shambolic, urgent and cheap-sounding.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, pop punk, skate punk, polished production, gang vocals, big chorus
```

### Lane `bigbeat` — Big beat

*style 557 · exclude 266 · taste 652*

```style
Big beat at 174 BPM. Fat compressed breaks squashed flat by heavy limiting, huge live-sounding drums, filtered noise sweeps rising into every drop, a swaggering dirty bassline and acid squelch underneath. Loud, grimy and cocksure — a party record with the lights off and something wrong in the room. Mean rather than bleak. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: big beat at 174 BPM. Fat compressed breaks squashed by heavy limiting, huge live-sounding drums, filtered noise sweeps into every drop, a swaggering dirty bassline, acid squelch.

Register: loud, grimy, swaggering and mean — a party record with something wrong in the room.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, trance, happy hardcore, feel good, festival anthem, sung chorus, orchestral strings, acoustic guitar
```

### Lane `hiphop` — Boom-bap hip-hop

*style 569 · exclude 280 · taste 650*

```style
Boom-bap hip-hop over a 174 BPM breakbeat. A filtered soul sample chopped hard on an MPC, vinyl crackle and tape hiss over everything, a fat swung snare cracking across the break, upright bass walking underneath, scratched turntable cuts on the turnarounds. Warm, dusty and narrow — mixed almost mono, sampler-crushed. Grimy and heavy. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: boom-bap hip-hop over a 174 BPM breakbeat. A filtered soul sample chopped on an MPC, vinyl crackle and tape hiss, a fat swung snare across the break, upright bass, scratched turntable cuts.

Register: warm, dusty, narrow and sampler-crushed. Grimy and heavy, never slick.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, trap, trap hi-hats, mumble rap, drill, road rap, guitar, live rock band, jazz rap, conscious rap, smooth soul hook, R&B vocal, modern polished mix
```

### Lane `grime` — UK grime

*style 576 · exclude 286 · taste 627*

```style
UK grime over 174 BPM drum and bass. Cold square-wave bass stabs, icy sparse synth hits landing in eights, eski clicks and metallic percussion, an arrangement with holes punched through it. Cheap FM synths, everything dry, hard and unlovely, nothing sweetened. Pirate-radio menace, skeletal and minimal, built to sound wrong on good speakers. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: UK grime over 174 BPM drum and bass. Cold square-wave bass stabs, icy sparse synth hits in eights, eski clicks, metallic percussion, cheap FM synths, an arrangement full of holes.

Register: cold, hard, skeletal, menacing and deliberately unlovely.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, trap, drill, road rap, ragga MC, Jamaican accent, guitar, live rock band, afroswing, smooth R&B, sung hook, warm analogue, lush pads, orchestral strings
```

### Lane `grunge` — Grunge

*style 579 · exclude 298 · taste 634*

```style
Grunge over a 174 BPM breakbeat. Thick detuned fuzz chords dragging half a hair behind the beat, downtuned through a blown speaker, sudden loud-quiet swings that fall away to almost nothing and slam back, feedback left ringing in the gaps. Bass guitar fat and woolly. Recorded flat and mid-heavy, no click, no gloss. Sludgy, bitter and dragging. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: grunge over a 174 BPM breakbeat. Thick detuned fuzz chords dragging behind the beat through a blown speaker, loud-quiet swings, feedback ringing in the gaps, fat woolly bass. Recorded flat and mid-heavy.

Register: sludgy, bitter, dragging and unpolished.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, britpop, post-grunge, radio rock, polished production, big chorus
```

### Lane `metal` — Metal

*style 546 · exclude 313 · taste 645*

```style
Pure metal over a 174 BPM breakbeat. Fast tremolo-picked riffs and palm-muted galloping chugs on a downtuned guitar, double-kick drumming doubling the break, pinch harmonics screaming out of the riff, and one short savage solo — aggressive, not melodic. Guitars quad-tracked, mids scooped, tight, loud and total. Two British men trade the verses, spoken and locked hard to the beat — one weathered, gravelly and smoke-worn in his fifties, the other higher, clean and plummy BBC English. Barked and rising in force, never sung, no chorus, no hook.
```

```taste
Vocals: two white British men in their late forties and fifties, and they must stay two different men — one low, gravelly and smoke-worn into a cheap close mic, the other higher, clean and plummy BBC English. Spoken and barked, locked to the beat, rising in force. Never sung, never a chorus.

Music: pure metal over a 174 BPM breakbeat. Fast tremolo-picked riffs and palm-muted galloping chugs on a downtuned guitar, double-kick doubling the break, pinch harmonics, one short savage solo. Quad-tracked guitars, scooped mids.

Register: savage, tight, loud and total.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, vocal hooks, clean sung melody, autotune, American accent, half-time, slow tempo, comedic, parody, uplifting, major key, hair metal, glam metal, shred, sweep picking, harmonized twin lead, symphonic metal, gothic metal, power metal, power ballad, clean sung chorus, orchestral strings, acoustic intro
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
