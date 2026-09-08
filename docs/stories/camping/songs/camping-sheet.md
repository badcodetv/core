---
title: Camping — the live sheet (style lanes, lyrics, sliders, rounds)
status: ROUND g3 — bold rewrite: ten independent extreme prompts, 10% shared text (was 78%). ROUND g1 — 2026-08-27, six genres over the drum and bass, each run BOTH as a cover of the h12 take and fresh from scratch. Verdict pending.
brief: Jack, 2026-08-27 — "I think we have lost the aggression and the pace, I think maybe experiment with different genres over the drum and bass."
source_take: "Camping HT AJ rap-rock W45 (h12)" (03:14) — attached by hand for the COVER half only
words_canon: ./camping.md  # §4 — the words, unchanged by this experiment
workspace: camping-duet
model: v5.5
---
# Camping — the genre sweep

**This sheet is the whole prompt.** The runner parses the lane fences below verbatim. Edit the
markdown, not the script.

| | |
|---|---|
| **The runner** | [`scripts/suno/camping.mts`](../../../../scripts/suno/camping.mts) |
| **Where takes land** | workspace `camping-duet` |
| **Titles** | `Camping <genre> cover (g1)` and `Camping <genre> fresh (g1)` — named so Jack can pick by ear without a key |
| **The words** | [`camping.md`](./camping.md) §4 is canon; the cover half inherits them, the fresh half writes them from [`camping-sheet.md` § Lyrics |

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

## 🔴 g3 — BOLD, NOT MEEK. Ten independent prompts, not one prompt with a swappable clause

Kai's ruling, 2026-08-27: *"the idea of changing a single sentence inside the style to represent a
new style, I would call a meek effort. So let's do a bold effort."*

g1 and g2 were both meek by that standard. g1 shared 78% of its Style text between any two lanes;
g2 cut that but still built every lane off one skeleton. **g3 has no skeleton.** Each lane is
written from nothing, in its own idiom, and the measurement is the point:

| | g1 | g3 |
|---|---|---|
| Longest identical run between any two Style boxes | **644 chars (78%)** | **69 chars (10%)** |
| What those shared characters are | the entire production spec | the casting phrase, and nothing else |

**Three things are shared, and only these three, because only these three are the song:**

1. **The two men** — one gravelly and smoke-worn in his fifties, one clean and plummy.
2. **The words** — `camping.md` §4, untouched and guarded.
3. **A drum-and-bass foundation at 174** — Jack's brief was genres *over* the drum and bass.

🔑 **Everything else now varies, including how the men deliver the line.** That was the biggest
single flattener: all ten g1 lanes said *"barked and metrical, locked to the beat"*, so ten
genres arrived with one voice. In g3 the delivery belongs to the genre — neurofunk **speaks flat
and processed**, jungle **chants hyped**, hip-hop **raps properly**, grime **spits fast and
clipped**, grunge **half-yells strained and slurring**, metal **roars throat-first**, digital
hardcore **screams, distorted and peaking**, punk **shouts hoarse**, big beat **shouts cocky
through a megaphone**. `never sung` survives in all ten — that is the one delivery rule that is
the song rather than the genre.

**And the mix language varies, which is what actually decides how a record sounds.** Neurofunk is
`wide, surgical, mastered loud and airless`; jungle is `mid-heavy, narrow, tape hiss and clipping
left in on purpose`; boom-bap is `crushed to twelve bits, almost mono, no highs`; metal is
`quad-tracked, hard-panned, mids scooped`; grunge is `flat, mid-heavy, no click, one guitar out of
tune with itself`. In g1 every one of these said the same sentence.

**Each lane is written EXTREME rather than tasteful** — the brief is to hear where the edges are,
because only an ear can decide which one suits the story. Digital hardcore is *"deliberately
unlistenable at the edges"*; punk is *"played fast and badly on purpose"*; big beat is *"huge,
stupid and mean"*. A tasteful sweep would tell us nothing we do not already know.

The shared exclude spine is down to **eight terms** — the ones true of the record in any genre —
and each lane then bans **the other lanes' sounds**, which is what stops ten prompts converging in
the model's head even when the text differs.

## 🔴 f1 — the prompts had been growing every round, and that is the mud

Kai, 2026-08-27: *"everything's sounding a bit samey now and a bit bland… we might have just
overwhelmed the style concept here with too many things… over-fit on the punk thing and we lack
funk and soul."*

**The measurement backs it.** Every round this session answered a note by *adding* a clause, and no
round ever removed one:

| Lane | Style box | Sentences |
|---|---|---|
| `grime` (g3) | 603 | 8 |
| `punkmetal` | 709 | 7 |
| `sabbath` (d1) | 808 | 8 |
| `annoyed` (a1) | 880 | **11** |
| `doomlow` (d2) | 917 | 9 |

🔑 **A prompt with eleven instructions averages them; a prompt with three commits to them.** That is
the whole mechanism behind "muddy" and "samey": eleven competing demands in one box produce a
weighted blend of everything, and a blend of many strong flavours is beige. **The f1 lanes are
~230–290 characters — a third of the size — and each one names exactly three things: a groove, one
instrument doing one specific thing, and the cast.** The excludes shrank the same way, because a
long ban list is also a pile of simultaneous demands.

**And the punk lock came off.** Kai's read is that what works is *the funky guitar riff that comes
out of punk* — a rhythmic, intermittent, single-note guitar — while what fails is punk's *wall*:
fast incessant drumming, muddy bass, jangly strummed chords all fighting the breakbeat. So punk
stays as a **guitar attitude and an anger**, not as a genre lock, and every lane below pairs it
with a groove tradition that is built on **space and repetition** rather than density.

**Six lanes, all angry, none of them a wall:** `punkfunk` (chicken-scratch and gaps),
`nowave` (atonal figure over a stiff funk bass), `heavyfunk` (wah riff in the pocket),
`darktone` (bleak minor-key two-tone — the closed-down-town record), `soulpunk` (a fuzz riff playing
the horn line), `afrovamp` (two guitars circling one chord that never changes).

🔑 **The common thread is that anger is carried by RESTRAINT and REPETITION, not by volume.** Every
one of these traditions is angry music that leaves holes — which is also, not by accident, what
drum and bass needs above it, since the breakbeat is already doing the density.

### Lane `punkfunk` — Punk-funk

*style 336 · exclude 199 · taste 296*

```style
Angry punk-funk over drum and bass at 174. One scratchy single-note guitar figure, chicken-scratch and trebly, played tight and dry with big gaps between the phrases. An elastic funk bass under the sub. Almost nothing else in the record. Two low English men trade the verses, spoken, hard and unhurried. Taut, cold and furious, held in.
```

```taste
Music: angry punk-funk over drum and bass at 174. One scratchy chicken-scratch guitar figure, trebly, tight and dry, with big gaps. Elastic funk bass under the sub. Almost nothing else.

Vocals: two low English men, spoken, hard, unhurried. Never sung.

Register: taut, cold, furious and held in.
```

```exclude
jangly guitar, wall of sound, strummed chords, power chords, hardcore punk, screaming, gang vocals, muddy bass, busy drumming, American accent, whiny vocal, falsetto, big chorus, feel good, major key
```

### Lane `nowave` — No-wave funk

*style 317 · exclude 196 · taste 329*

```style
No-wave funk over drum and bass at 174. One atonal scraped guitar figure locked to a stiff, repetitive funk bassline. Dissonant, mechanical and dry, nothing ever resolving. Long stretches with only bass and drums. Two low English men trade the verses, spoken, hard and unhurried. Cold, hostile, and somehow danceable.
```

```taste
Music: no-wave funk over drum and bass at 174. One atonal scraped guitar figure locked to a stiff repetitive funk bassline. Dissonant, mechanical, dry, never resolving. Long stretches of bass and drums alone.

Vocals: two low English men, spoken, hard, unhurried. Never sung.

Register: cold, hostile, mechanical — and danceable.
```

```exclude
jangly guitar, wall of sound, melodic guitar, guitar solo, warm chords, hardcore punk, screaming, gang vocals, muddy bass, American accent, whiny vocal, big chorus, feel good, major key, uplifting
```

### Lane `heavyfunk` — Heavy funk

*style 327 · exclude 203 · taste 305*

```style
Heavy funk over drum and bass at 174. A syncopated one-bar guitar riff through a wah pedal, clavinet stabs answering it, a fat elastic bassline. The drums sit in the pocket rather than filling every bar. Space between every hit. Two low English men trade the verses, spoken, hard and unhurried. Dirty, angry, and in the groove.
```

```taste
Music: heavy funk over drum and bass at 174. A syncopated one-bar wah guitar riff, clavinet stabs answering it, fat elastic bass. Drums in the pocket, not filling every bar. Space between every hit.

Vocals: two low English men, spoken, hard, unhurried. Never sung.

Register: dirty, angry, in the groove.
```

```exclude
jangly guitar, wall of sound, hardcore punk, punk guitar, screaming, gang vocals, busy drumming, blast beats, American accent, whiny vocal, smooth soul, disco, feel good, major key, uplifting, big chorus
```

### Lane `darktone` — Dark two-tone

*style 298 · exclude 193 · taste 295*

```style
Bleak minor-key two-tone over drum and bass at 174. A hollow organ line, one clipped offbeat guitar chop, a walking bass underneath. Empty and haunted rather than jaunty — the sound of a closed-down town. Two low English men trade the verses, spoken, hard and unhurried. Cold, sardonic and English.
```

```taste
Music: bleak minor-key two-tone over drum and bass at 174. A hollow organ line, one clipped offbeat guitar chop, walking bass. Empty and haunted, the sound of a closed-down town.

Vocals: two low English men, spoken, hard, unhurried. Never sung.

Register: cold, sardonic, English, never jaunty.
```

```exclude
jaunty, bouncy, happy, feel good, major key, party, brass band, comedic, wall of sound, jangly guitar, hardcore punk, screaming, gang vocals, American accent, whiny vocal, big chorus, uplifting
```

### Lane `soulpunk` — Soul-punk

*style 326 · exclude 205 · taste 331*

```style
Soul-punk over drum and bass at 174. A fuzzed-out riff playing the line the horns would play, a driving tambourine, deep round bass. Cut live and hot, raw rather than tidy, with the guitar dropping out for whole bars. Two low English men trade the verses, spoken, hard and unhurried. Angry, and with real soul force behind it.
```

```taste
Music: soul-punk over drum and bass at 174. A fuzzed-out riff playing the line horns would play, driving tambourine, deep round bass. Cut live and hot, raw not tidy, guitar dropping out for whole bars.

Vocals: two low English men, spoken, hard, unhurried. Never sung.

Register: angry, with real soul force behind it. Never sweet.
```

```exclude
smooth soul, sweet soul, R&B vocal, sung chorus, gospel choir, jangly guitar, wall of sound, hardcore punk, screaming, gang vocals, American accent, whiny vocal, big chorus, feel good, major key, uplifting
```

### Lane `afrovamp` — Afro-funk vamp

*style 289 · exclude 203 · taste 305*

```style
Afro-funk vamp over drum and bass at 174. Two interlocking guitars circling one chord that never changes, a repeating bass figure, shakers and rim clicks. Hypnotic, unresolved and disciplined. Two low English men trade the verses, spoken, hard and unhurried. Furious, but patient about it.
```

```taste
Music: afro-funk vamp over drum and bass at 174. Two interlocking guitars circling one chord that never changes, a repeating bass figure, shakers and rim clicks. Hypnotic, unresolved, disciplined.

Vocals: two low English men, spoken, hard, unhurried. Never sung.

Register: furious, but patient about it.
```

```exclude
chord change, key change, jangly guitar, wall of sound, hardcore punk, screaming, gang vocals, horns, brass section, American accent, whiny vocal, big chorus, feel good, major key, uplifting, world music
```

## 🔴 vv1 — six voices, one band

Kai, 2026-08-27: *"vary the voice a lot… style variations, but only on the voice, because I think
we've got the punk guitar undertones."*

🔑 **The band half is frozen byte-for-byte across all six** — the same 199 characters lifted
from `dynamics`, which is the arrangement Kai approved. Only the voice sentence changes. This is the
v1 construction used for exactly what it is good for: **anything you hear differing between these
six is the singer, and nothing else can be.**

**Run as COVERS of the approved take**, now that `attachCover` makes that a single command. That
anchors the arrangement in the source audio as well as in the prompt, so the whole of the model's
attention goes on the voice. Audio Influence sits at 25 — enough to hold the band, low enough that
the vocal is not simply copied from the source.

**The six are chosen to be genuinely different KINDS of anger**, not six volumes of one:

| Lane | The idea |
|---|---|
| `v-deadpan` | never raises at all; the threat is entirely in the calm |
| `v-seethe` | forced through clenched teeth — a man deciding not to hit someone |
| `v-preacher` | hectoring in rhythm, each phrase starting higher than the last |
| `v-weary` | said it all before and expects nothing; flashes of bile, then flat |
| `v-pub` | squaring up — slurring at the edges, clipping the mic, slightly out of control |
| `v-posh` | clipped RP, rage entirely controlled — being dismissed politely |

`v-posh` also **inverts who leads**, which no round has tested: the plummy man takes the front and
the gravelly one answers.

**Kept in every lane** (all proven, all costly to relearn): two British men who must stay two
different men, low and English, `never sung`, and the American/whiny/falsetto bans that fixed d1.

### Lane `v-deadpan` — Deadpan menace

*style 528 · exclude 562 · taste 571*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS FLAT, QUIET AND MENACING. It never raises at all. A low English baritone speaking just above a murmur, close on the mic, absolutely level — no emphasis, no build, no anger on the surface. The threat is entirely in the calm. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: flat, quiet and menacing. A low English baritone just above a murmur, close on the mic, absolutely level — no emphasis, no build, no surface anger. The threat is entirely in the calm. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, parody, uplifting, major key, wall of guitar, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, polished production, shouting, screaming, ranting, raised voice, aggressive vocal, gang shout
```

### Lane `v-seethe` — Seething growl

*style 542 · exclude 560 · taste 597*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS A SEETHING GROWL. A low English baritone forced out through clenched teeth, tight and pressurised, the anger held down hard and leaking out at the consonants. Never loud, never released — it sounds like a man deciding not to hit someone. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: a seething growl. A low English baritone forced through clenched teeth, tight and pressurised, anger held down and leaking out at the consonants. Never loud, never released — a man deciding not to hit someone. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, parody, uplifting, major key, wall of guitar, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, polished production, screaming, shrieking, gang shout, hysterical, unhinged, cracking voice
```

### Lane `v-preacher` — Ranting preacher

*style 513 · exclude 568 · taste 596*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS A STREET PREACHER'S RANT. A low English baritone hectoring in rhythm, hammering the stresses, building phrase by phrase and starting each one higher than the last — a man on a box who will not be interrupted. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: a street preacher's rant. A low English baritone hectoring in rhythm, hammering the stresses, building phrase by phrase and starting each one higher than the last — a man on a box who will not be interrupted. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, parody, uplifting, major key, wall of guitar, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, polished production, screaming, gang shout, gospel choir, singing, melodic vocal, American preacher
```

### Lane `v-weary` — Weary contempt

*style 526 · exclude 561 · taste 598*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS TIRED AND CONTEMPTUOUS. A low, worn English baritone, gravelly and short of breath, delivering the lines like a man who has said all this before and expects nothing. Occasional flashes of bile, then straight back to flat. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: tired and contemptuous. A low worn English baritone, gravelly and short of breath, delivering like a man who has said all this before and expects nothing. Occasional flashes of bile, then straight back to flat. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, parody, uplifting, major key, wall of guitar, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, polished production, screaming, shouting, energetic vocal, gang shout, uplifting, triumphant
```

### Lane `v-pub` — Pub aggression

*style 533 · exclude 568 · taste 610*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS A MAN SQUARING UP IN A PUB. A loud, thick English baritone, consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a bark without warning — real, unpolished and slightly out of control. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: a man squaring up in a pub. Loud, thick English baritone, consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a bark without warning. Real, unpolished, slightly out of control. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, parody, uplifting, major key, wall of guitar, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, polished production, screaming, gang shout, comedic, novelty, drunk singing, singing, melodic vocal
```

### Lane `v-posh` — Cold posh fury

*style 499 · exclude 571 · taste 569*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS ICY AND WELL-SPOKEN. Clipped RP English, precise and unhurried, every word placed exactly, the rage completely controlled and all the colder for it — the sound of someone being dismissed politely. The plummy man leads and the gravelly one answers. Two British men, both low. Never sung.
```

```taste
Vocals: icy and well-spoken. Clipped RP English, precise and unhurried, every word placed exactly, rage entirely controlled and colder for it — the sound of being dismissed politely. The plummy man leads, the gravelly one answers. Two different British men, both low. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, parody, uplifting, major key, wall of guitar, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, polished production, screaming, shouting, gang shout, rough accent, cockney, mockney, comedic, singing
```

## 🔑 pv1 — the pub voice gets a band

**Kai picked `v-pub` out of the vv1 six:** *"the pub aggression is a great voice, I like that a lot.
Could we please use the pub aggression voice over the punk instrumental layer."*

**The voice clause is frozen** — the same words that produced the take he chose. **Two band halves
are tested against it**, because "the punk instrumental layer" has meant two different things in
this sheet and guessing which would waste the round:

| Lane | Band |
|---|---|
| `pub-stabs` | the sparse arrangement Kai approved earlier — choppy stabs off the beat, whole bars empty |
| `pub-fullpunk` | an actual hardcore punk band — fast downstrokes, live kit, cymbals over everything |

**And both run twice, fresh and as a cover**, which answers a second question in the same breath:
`v-pub` was heard as a *cover*, so its band came largely from the source audio rather than from the
prompt. **Fresh mode is the first time the pub voice is asked to arrive with a band built from the
words alone.** If fresh sounds thinner, the arrangement Kai likes is living in the source audio, and
covers are the lane from here on.

### Lane `pub-stabs` — Pub voice, punk stabs

*style 533 · exclude 533 · taste 674*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS A MAN SQUARING UP IN A PUB. A loud, thick English baritone, consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a bark without warning — real, unpolished and slightly out of control. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: a man squaring up in a pub. Loud, thick English baritone, consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a bark without warning. Real, unpolished, slightly out of control. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Register: real, unpolished, angry and slightly out of control.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, novelty, drunk singing, singing, melodic vocal, screaming, gang shout, gang vocals, uplifting, major key, jangly guitar, muddy bass, half-time, slow tempo, polished production
```

### Lane `pub-fullpunk` — Pub voice, full punk band

*style 652 · exclude 533 · taste 724*

```style
THE BAND IS HARDCORE PUNK OVER DRUM AND BASS AT 174. Fast downstroke power chords buzzing flat out through a cheap trebly amp, distorted bass clinging on, drums thrashed like a live kit over the chopped breakbeat, crash on every turnaround, cymbals washing over the whole record. Cut fast in a room and never polished. THE VOICE IS A MAN SQUARING UP IN A PUB. A loud, thick English baritone, consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a bark without warning — real, unpolished and slightly out of control. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy. Never sung.
```

```taste
Vocals: a man squaring up in a pub. Loud, thick English baritone, consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a bark without warning. Real, unpolished, slightly out of control. Two different British men: one gravelly and smoke-worn, one clean and plummy. Never sung.

Music: hardcore punk over drum and bass at 174. Fast downstroke power chords through a cheap trebly amp, distorted bass clinging on, drums thrashed like a live kit over the chopped breakbeat, cymbals washing over everything. Cut fast in a room, never polished.

Register: real, unpolished, angry and slightly out of control.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, autotune, harmonies, sung chorus, big chorus, vocal hooks, catchy hook, pop melody, rapping, comedic, novelty, drunk singing, singing, melodic vocal, screaming, gang shout, gang vocals, uplifting, major key, jangly guitar, muddy bass, half-time, slow tempo, polished production
```

## Lanes

### Lane `neurofunk` — Neurofunk

*style 708 · exclude 296 · taste 661*

```style
Neurofunk, 174 BPM, minor key, clinical to the point of cruelty. The bass is the song: a reese growling and morphing every bar, resampled and re-distorted, sweeping under a razor-tight two-step. Snares crack like a nailgun, hats clipped to nothing, every hit quantised dead. Sound design instead of musicality — metallic scrapes, filtered risers, sci-fi machinery, no chords and no tune anywhere. Sub deep and clean, stereo wide and surgical, mastered loud and airless. Two British men speak the verses over it, processed cold and close: one gravelly and smoke-worn in his fifties, one clean and plummy. Flat, hard and exact, absolutely never sung. It should sound like a machine that has stopped pretending.
```

```taste
Music: neurofunk at 174 BPM. A morphing, resampled reese bass is the whole song. Razor-tight two-step, nailgun snare, hats clipped to nothing, every hit quantised dead. Sound design over musicality — metallic scrapes, filtered risers, sci-fi machinery. No chords, no tune. Deep clean sub, wide surgical stereo, mastered loud and airless.

Vocals: two British men speak the verses, processed cold and close — one gravelly and smoke-worn in his fifties, one clean and plummy. Flat, hard, exact. Never sung.

Register: clinical, inhuman, menacing. A machine that has stopped pretending.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, guitar, live drums, acoustic instruments, tape hiss, lo-fi, warm analogue, jazzy chords, soul sample, jungle breaks, liquid dnb, jump up, euphoric, festival, sung vocal, rapping, shouting, screaming
```

### Lane `jungle` — Jungle

*style 684 · exclude 294 · taste 721*

```style
Raw 1994 jungle at 174 BPM — a dubplate cut in a bedroom. Amen and Think breaks chopped to ribbons and reassembled wrong, timestretched snares smeared across the bar, ride chattering, fills tumbling over the one. A vast round sub, bowel-deep, doubled by a dark reese. Dub sirens, air-horn stabs, reverb throws, tape hiss and saturation and clipping all left in on purpose. No modern polish anywhere: mid-heavy, narrow, the drums and the bass fighting for the same room. Two British men chant the verses over it, hyped and rowdy, close on a cheap mic chain: one gravelly and smoke-worn, one clean and plummy. Spoken and riding the break, never sung. Pirate radio at two in the morning.
```

```taste
Music: raw 1994 jungle at 174 BPM, like a dubplate cut in a bedroom. Amen and Think breaks chopped to ribbons and reassembled wrong, timestretched snares smeared across the bar, fills tumbling over the one. A vast round sub doubled by a dark reese. Dub sirens, air-horn stabs, reverb throws. Tape hiss, saturation and clipping left in. Mid-heavy and narrow, drums and bass fighting for room.

Vocals: two British men chant the verses, hyped and rowdy, close on a cheap mic chain — one gravelly and smoke-worn, one clean and plummy. Spoken, riding the break, never sung.

Register: rowdy, dark, rough, alive. Pirate radio at two in the morning.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, guitar, live rock band, neurofunk, clean modern production, polished mix, mastered loud, ragga MC, Jamaican accent, liquid dnb, jump up, happy hardcore, euphoric, piano riff, sung vocal, screaming
```

### Lane `industrial` — Industrial metal

*style 646 · exclude 330 · taste 664*

```style
Industrial metal, brutal and mechanical, hammering over a 174 BPM breakbeat. Sheet-metal and anvil percussion doubling the kick until it distorts, a detuned seven-string chugging in short violent bursts, a rusted machine drone holding underneath, pneumatic hiss and factory noise filling every gap. Everything overdriven, gated hard and squashed flat — the mix should sound damaged. No melody, no relief, no air, nothing pretty. Two British men shout the verses over it through a tight, bullhorn-hard compressor: one gravelly and smoke-worn in his fifties, one clean and plummy. Barked, never sung. It should feel like a press that will not stop.
```

```taste
Music: industrial metal hammering over a 174 BPM breakbeat. Sheet-metal and anvil percussion doubling the kick until it distorts, a detuned seven-string chugging in short violent bursts, a rusted machine drone, pneumatic hiss and factory noise in every gap. Overdriven, hard-gated, squashed flat — the mix should sound damaged. No melody, no relief, no air.

Vocals: two British men shout the verses through a bullhorn-hard compressor — one gravelly and smoke-worn in his fifties, one clean and plummy. Barked, never sung.

Register: brutal, rusted, inhuman. A press that will not stop.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, symphonic metal, gothic metal, power ballad, melodic lead guitar, clean guitar, acoustic guitar, orchestral strings, choir, warm analogue, lo-fi, soul sample, turntable scratching, sung vocal, rapping
```

### Lane `breakcore` — Digital hardcore

*style 672 · exclude 300 · taste 685*

```style
Digital hardcore at 174 BPM, deliberately unlistenable at the edges. Breakbeats overdriven until they tear, kicks blown into square waves, gunshot snares, hard gates slamming shut, stutter edits shredding whole bars. Sirens, alarms, riot noise and crowd roar buried underneath. Bass distorted past recognition. The whole mix shoved into the red and clipping — distortion is not an effect here, it is the production. No tune, no groove offered for comfort, only forward violence. Two British men scream and bark the verses over it, distorted and peaking, both losing control: one gravelly and smoke-worn, one clean and plummy. Never sung. A riot recorded on a broken phone.
```

```taste
Music: digital hardcore at 174 BPM, unlistenable at the edges on purpose. Breakbeats overdriven until they tear, kicks blown into square waves, gunshot snares, hard gates, stutter edits shredding whole bars. Sirens, alarms, riot noise and crowd roar underneath. Bass distorted past recognition. The mix is in the red and clipping — distortion is the production, not an effect.

Vocals: two British men scream and bark the verses, distorted and peaking, losing control — one gravelly and smoke-worn, one clean and plummy. Never sung.

Register: violent, chaotic, political. A riot recorded on a broken phone.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, melodic synths, clean production, polished mix, guitar solo, shred, gabber, hardstyle, happy hardcore, euphoric, trance, orchestral strings, warm analogue, soul sample, jazzy chords, sung vocal, rapping
```

### Lane `hardpunk` — Hardcore punk

*style 649 · exclude 326 · taste 656*

```style
Hardcore punk played fast and badly on purpose, over a 174 BPM breakbeat. Downstroke power chords buzzing flat out through a cheap trebly amp with the gain long past useful, bass guitar distorted and just hanging on, drums thrashed like a live kit — ride bell, crash on every turnaround, cymbals washing over the whole record. Cut in one take in a room that is one microphone short: mid-heavy, no real bottom end, cymbals clipping. No overdubs, no solo, no polish, nothing in tune for long. Two British men shout the verses hoarse over it: one gravelly and smoke-worn, one clean and plummy going ragged. Never sung. The third band on at a squat gig.
```

```taste
Music: hardcore punk played fast and badly on purpose over a 174 BPM breakbeat. Downstroke power chords through a cheap trebly amp with the gain past useful, distorted bass hanging on, drums thrashed like a live kit, cymbals washing over everything. One take in a room one microphone short — mid-heavy, no bottom end, cymbals clipping. No overdubs, no solo, no polish.

Vocals: two British men shout the verses hoarse — one gravelly and smoke-worn, one clean and plummy going ragged. Never sung.

Register: furious, shambolic, urgent and cheap. The third band on at a squat gig.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, pop punk, skate punk, emo, polished production, mastered loud, gang vocals, big chorus, sung vocal, rapping, turntable scratching
```

### Lane `bigbeat` — Big beat

*style 623 · exclude 273 · taste 660*

```style
Big beat at 174 BPM — huge, stupid and mean. Fat breaks compressed until they breathe, kick and snare the size of a building, filtered noise sweeps climbing into every drop, a dirty swaggering bassline, acid squelch crawling underneath, brass stabs and vinyl stops. Everything limited flat and loud and drenched in room, deliberately overblown: a party record playing in a car park at four in the morning with something wrong in it. Two British men shout the verses over it through a megaphone filter, cocky and grinning: one gravelly and smoke-worn, one clean and plummy. Spoken, never sung. Swagger rather than bleakness.
```

```taste
Music: big beat at 174 BPM, huge and stupid and mean. Fat breaks compressed until they breathe, kick and snare the size of a building, filtered noise sweeps into every drop, a dirty swaggering bassline, acid squelch, brass stabs, vinyl stops. Limited flat and loud, drenched in room, deliberately overblown.

Vocals: two British men shout the verses through a megaphone filter, cocky and grinning — one gravelly and smoke-worn, one clean and plummy. Spoken, never sung.

Register: swaggering and mean — a party record in a car park at four in the morning with something wrong in it.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, trance, happy hardcore, feel good, festival anthem, orchestral strings, acoustic guitar, bleak, ambient, minimal, sparse, sung vocal, screaming
```

### Lane `hiphop` — Boom-bap hip-hop

*style 636 · exclude 295 · taste 667*

```style
Filthy boom-bap hip-hop, the break running double-time at 174 so the pocket sits at 87. A dusty soul loop chopped hard on an MPC and left slightly out of tune, vinyl crackle and tape hiss over everything, a fat swung snare cracking a fraction behind the beat, upright bass walking, turntable cuts scratching every turnaround. Sampler-crushed to twelve bits, mixed narrow and almost mono, no highs, no width, no gloss at all. Two British men rap the verses properly over it — on the beat, hard consonants, no melody in the voice: one gravelly and smoke-worn in his fifties, one clean and plummy. Never sung. Lifted off a warped cassette.
```

```taste
Music: filthy boom-bap hip-hop, the break at double-time 174 so the pocket sits at 87. A dusty soul loop chopped on an MPC and left slightly out of tune, vinyl crackle and tape hiss, a fat swung snare cracking behind the beat, upright bass, turntable cuts on the turnarounds. Crushed to twelve bits, narrow and almost mono, no highs, no gloss.

Vocals: two British men rap the verses properly — on the beat, hard consonants, no melody in the voice — one gravelly and smoke-worn in his fifties, one clean and plummy. Never sung.

Register: dusty, grimy, heavy. Lifted off a warped cassette.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, trap, trap hi-hats, mumble rap, drill, road rap, guitar, live rock band, jazz rap, conscious rap, smooth soul hook, R&B vocal, modern polished mix, mastered loud, wide stereo, screaming, sung vocal
```

### Lane `grime` — UK grime

*style 603 · exclude 302 · taste 637*

```style
UK grime over 174 BPM drum and bass, skeletal and hostile. Cold square-wave bass stabs, icy FM synth hits landing in eights, eski clicks, metallic percussion, and holes punched through the arrangement where a normal record would put music. Cheap presets, dry as bone, nothing sweetened and nothing warm. Sub heavy and blunt. It should sound wrong on good speakers and right through a phone. Two British men spit the verses over it, fast, clipped and aggressive, right on the mic with no reverb at all: one gravelly and smoke-worn, one clean and plummy. Never sung. Pirate-radio menace, minimal and cold.
```

```taste
Music: UK grime over 174 BPM drum and bass, skeletal and hostile. Cold square-wave bass stabs, icy FM synth hits in eights, eski clicks, metallic percussion, holes punched through the arrangement. Cheap presets, dry as bone, nothing warm. Sub heavy and blunt. It should sound wrong on good speakers and right through a phone.

Vocals: two British men spit the verses fast, clipped and aggressive, right on the mic with no reverb — one gravelly and smoke-worn, one clean and plummy. Never sung.

Register: cold, hard, skeletal, menacing, deliberately unlovely.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, trap, drill, road rap, ragga MC, Jamaican accent, guitar, live rock band, afroswing, smooth R&B, sung hook, warm analogue, lush pads, orchestral strings, tape hiss, soul sample, screaming, big room reverb
```

### Lane `grunge` — Grunge

*style 626 · exclude 308 · taste 645*

```style
Grunge over a 174 BPM breakbeat, sludgy and dragging. Thick detuned fuzz chords lurching a hair behind the beat through a blown speaker cone, a woolly fat bass guitar, and violent loud-quiet swings — whole bars falling away to almost nothing then slamming back with the feedback still ringing. Recorded flat, mid-heavy and unglamorous: no click track, no gloss, tape saturating, one guitar out of tune with itself. Two British men half-yell the verses over it, strained and slurring at the edges: one gravelly and smoke-worn, one clean and plummy going hoarse. Shouted and spoken, never properly sung. Bitter, tired and heavy.
```

```taste
Music: grunge over a 174 BPM breakbeat, sludgy and dragging. Thick detuned fuzz chords lurching behind the beat through a blown speaker cone, woolly fat bass, violent loud-quiet swings — bars falling to almost nothing then slamming back with feedback ringing. Recorded flat, mid-heavy and unglamorous, no click, no gloss, one guitar out of tune with itself.

Vocals: two British men half-yell the verses, strained and slurring — one gravelly and smoke-worn, one clean and plummy going hoarse. Shouted, never properly sung.

Register: bitter, tired, heavy, unpolished.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, guitar solo, shred, hair metal, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, britpop, post-grunge, radio rock, polished production, mastered loud, big chorus, turntable scratching, rapping
```

### Lane `metal` — Metal

*style 665 · exclude 328 · taste 677*

```style
Pure metal over a 174 BPM breakbeat, and total. Fast tremolo-picked riffs and palm-muted galloping chugs on a downtuned eight-string, double-kick drumming doubling the break the whole way through, pinch harmonics screaming out of the riff, and one short savage solo that is violence rather than melody. Guitars quad-tracked and hard-panned, mids scooped out, everything tight, dry and enormous. No clean passage, no let-up, no breathing space anywhere. Two British men roar the verses over it, throat-first and dead on the grid: one gravelly and smoke-worn in his fifties, one clean and plummy turning vicious. Never sung. It should sound like it wants to hurt you.
```

```taste
Music: pure metal over a 174 BPM breakbeat, and total. Fast tremolo-picked riffs and palm-muted galloping chugs on a downtuned eight-string, double-kick doubling the break throughout, pinch harmonics screaming out of the riff, one short savage solo that is violence rather than melody. Quad-tracked hard-panned guitars, scooped mids, tight, dry and enormous. No clean passage, no let-up.

Vocals: two British men roar the verses, throat-first and dead on the grid — one gravelly and smoke-worn in his fifties, one clean and plummy turning vicious. Never sung.

Register: savage, total, overwhelming.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, hair metal, glam metal, shred, sweep picking, harmonized twin lead, symphonic metal, gothic metal, power metal, power ballad, clean sung chorus, orchestral strings, acoustic intro, turntable scratching, soul sample, lo-fi, rapping
```

### Lane `punkmetal` — Punk-metal

🎯 **Kai's pick, 2026-08-27:** *"the punk version, the hardcore punk definitely works, and the
voice from the metal works… so it's of punk metal."* Punk's instrumentation and recording (fast
downstrokes, cheap amp, cymbals clipping, cut fast) with metal's **vocal** (roared, throat-first)
and metal's guitar discipline (palm-muted gallops, double-tracked, scooped mids).

*style 709 · exclude 382 · taste 730*

```style
Hardcore punk and metal welded together over a 174 BPM breakbeat. Fast downstroke power chords and palm-muted galloping chugs on a downtuned guitar, flat out through a cheap trebly amp, distorted bass clinging on, double-kick doubling the break, crash on every turnaround, cymbals washing over everything. Guitars double-tracked, mids scooped, tight and loud but still raw — cut fast, never polished, cymbals clipping. No clean passage, no let-up, no breathing space. Two British men roar the verses over it, throat-first and dead on the grid: one gravelly and smoke-worn in his fifties, one clean and plummy turning vicious. Never sung. It should sound like a hardcore band that got heavier than it meant to.
```

```taste
Vocals: two British men roar the verses, throat-first and dead on the grid — one gravelly and smoke-worn in his fifties, one clean and plummy turning vicious. Shouted from the chest, never sung, never a chorus.

Music: hardcore punk and metal welded together over a 174 BPM breakbeat. Fast downstroke power chords and palm-muted galloping chugs on a downtuned guitar through a cheap trebly amp, distorted bass, double-kick doubling the break, cymbals washing over everything. Double-tracked guitars, scooped mids, tight and loud but raw — cut fast, never polished.

Register: savage, urgent and total. A hardcore band that got heavier than it meant to.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, hair metal, glam metal, shred, sweep picking, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, pop punk, skate punk, emo, post-grunge, radio rock, symphonic metal, power ballad, big chorus, gang vocals, polished production, turntable scratching, soul sample, rapping
```

## Lyrics — the one cue sheet

🔴 **This is the only place lyrics live for generation.** Before 2026-08-27 the runners read them
from this sheet's § Lyrics while the words canon sat in `camping.md` §4 and the two disagreed on
the first-verse cues — which is exactly why the stutter looked unprompted. `camping.md` §4 remains
the **words** canon and the guard: the runner compares the page's words against it and refuses to
spend a credit if they have drifted. **The cues are this file's business; the words are never.**

Currently loaded: **variant B** (three cues in the disputed run). Variant A is preserved in
§ *Timing test* below; switching is a one-line edit of which fence this section holds.

```lyrics
[Intro — 2 bars, high-register 80s rock guitar lick, straight to the beat]
[Verse 1 | gravelly rapped voice, tight to the beat | no drums for the first half, then the breakbeat]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
[whispered]
but I bet, that you paid for your wheels on tick!
[hard and slow]
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[spoken word, quiet, drums out]
I can't live like this forever
[back on the beat, raised, and straight through to the end of the verse]
I might be insane but I do want change, 
let's see what we can arrange!
now, I insist that I hold that door
[shout, cracking, begging]
please sir, can I FUCKIN, have some more?
[Verse 2 | posh voice, a completely different man]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
[mocking falsetto]
What about if we taxed the rich?
[angry]
what the fuck you think this is, BITCH!
[posh voice]
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Bridge | the two men trade, close and dry | drums stripped back]
[gravelly voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[pause | posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly voice]
yet I don't begrudge you,
it's us and them now
[pause | posh voice]
well we don't have long
[Outro — both voices]
and by the time it hits, we'll be gone
[end]
```

---

### Lane `punkbody` — Punk body, metal throat

🎯 **Kai, 2026-08-27:** *"we're liking the punk instrumental layer, but the voice doesn't work very
well as a punk voice… lean in more to the guitar layer of the punk genre and less into the voice of
the punk genre."*

**The prompt is written as two labelled halves, in caps, with an explicit denial.** `punkmetal`
described one blended thing and let Suno decide which half won; this one states the seam —
`THE BAND IS HARDCORE PUNK` / `THE VOICE IS NOT PUNK — IT IS METAL` — and then bans the punk vocal
by name in its excludes (`snotty vocal`, `hoarse yelping`, `gang shout`, `yelped vocal`) while
leaving every punk *instrument* word untouched. An exclude has no section scope, but a term that is
**about the voice** is scoped by its own meaning, which is the only scoping excludes offer.

*style 683 · exclude 480 · taste 756*

```style
THE BAND IS HARDCORE PUNK. Fast downstroke power chords buzzing flat out through a cheap trebly amp, distorted bass clinging on, drums thrashed like a live kit over a 174 BPM breakbeat, crash on every turnaround, cymbals washing over the whole record. Cut fast in a room and never polished, mid-heavy, cymbals clipping. THE VOICE IS NOT PUNK — IT IS METAL. Two British men roar the verses from the throat, guttural, chest-deep and controlled, dead on the grid: one gravelly and smoke-worn in his fifties, one clean and plummy turning vicious. No snotty sneer, no hoarse yelping, no gang shout, no crowd. Never sung, no chorus, no hook. A punk band with a metal singer in front of it.
```

```taste
Vocals: METAL, not punk. Two British men roar the verses from the throat — guttural, chest-deep, controlled and dead on the grid. One is gravelly and smoke-worn in his fifties, the other clean and plummy turning vicious. They must stay two different men. No snotty sneer, no hoarse yelping, no gang shout. Never sung.

Music: HARDCORE PUNK, played over a 174 BPM breakbeat. Fast downstroke power chords through a cheap trebly amp, distorted bass clinging on, drums thrashed like a live kit, cymbals washing over everything. Cut fast in a room, mid-heavy, never polished.

Register: a punk band with a metal singer in front of it. Savage, urgent, and heavier than it means to be.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
sung chorus, clean sung melody, autotune, American accent, comedic, parody, uplifting, major key, punk vocals, snotty vocal, sneering vocal, hoarse yelping, yelped vocal, gang shout, gang vocals, crowd vocals, oi vocals, shouted chorus, rapped vocal, rapping, spoken word verse, hair metal, glam metal, shred, sweep picking, harmonized twin lead, melodic lead guitar, chiming guitar, jangle, pop punk, skate punk, emo, post-grunge, radio rock, polished production, 80s rock guitar
```

### Lane `dynamics` — Annoyed band, angry voice, controlled dynamics

🎯 **Kai, 2026-08-27, on the take he chose to cover:** *"the voices feel slightly bipolar — when it
gets angry and shouty it gets REALLY angry and shouty… make it not be so random and not so extreme
when it gets angry, and equally when it's in a quiet period it should be softer and more quiet than
it is now."*

🔑 **This is not "less angry" — it is a wider range, controlled at both ends.** The loud end comes
*down* (`a hard contained growl through the teeth — furious but held in, never a scream, never
cracking`) and the quiet end goes *further down* (`a close low murmur, almost under the breath, and
quieter than the band`). Then the thing that actually fixes "bipolar": **`every move between the two
is gradual and deliberate, never sudden and never random`** — the complaint is about the *transitions*
as much as the extremes.

**Ran as a COVER**, so the arrangement Kai already approved is anchored by the source audio and the
prompt's whole budget goes on the voice. That is the configuration this sheet has been circling all
day and has never actually run: every previous cover round was trying to change the *music*.

🔴 **In cover mode we do not write the lyrics** — they arrive with the attachment. So the bipolar
cue `[shout, cracking, begging]` is still in the source's own sheet and **cannot be edited from
here**. `cracking voice`, `voice breaking`, `shrieking` and `sudden dynamic jumps` are therefore
banned in the excludes instead: the excludes are the only lever left pointing at that cue. **If the
takes still lurch at that line, the cue is the cause and a fresh-mode round is the way to test it.**

*style 790 · exclude 757 · taste 1061*

```style
THE BAND STAYS AS IT IS: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Space around everything. THE VOICE IS LOW, ENGLISH AND ANGRY, AND ITS DYNAMICS ARE CONTROLLED. It never lurches. At its loudest it is a hard contained growl through the teeth — furious but held in, never a scream, never cracking, never shrieking. At its quietest it drops right down to a close low murmur, almost under the breath, quieter than the band. Every move between the two is gradual and deliberate, never sudden and never random. Plain working-class English vowels, Midlands and northern. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy, both pitched low. No chorus, no hook.
```

```taste
Vocals: low, English and angry, with CONTROLLED dynamics. The voice never lurches. At its loudest it is a hard contained growl through the teeth — furious but held in, never screamed, never cracking, never shrieking. At its quietest it drops right down to a close low murmur, almost under the breath and quieter than the band. Every move between the two is gradual and deliberate, never sudden and never random. Plain working-class English vowels, Midlands and northern, no American vowels. Never nasal, never whiny, no falsetto. Two British men, and they must stay two different men: one gravelly and smoke-worn in his fifties, one clean and plummy. Both low. Never sung.

Music: a punk guitar tone playing short choppy stabs off the beat with whole bars left empty, over drum and bass at 174 that carries all the pace by itself. Never a wall of downstrokes. Space around everything.

Register: anger under control. A man who is furious and knows that shouting louder will not help.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
screaming, screamed vocal, shrieking, cracking voice, voice breaking, yelping, erratic vocal, sudden dynamic jumps, wild dynamics, unhinged, hysterical, death growl, gang shout, gang vocals, shouted chorus, wailing, keening, American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, operatic vocals, rapping, big chorus, vocal hooks, catchy hook, pop melody, autotune, harmonies, anthemic, uplifting, feel good, major key, comedic, parody, wall of guitar, constant downstrokes, jangly guitar, muddy bass, busy drumming, half-time, slow tempo, tempo change, polished production
```

### Lane `funkpunk` — Funk band, punk mouth

🎯 **Kai, 2026-08-27:** *"funk is an interesting layer, but the singing voice on the funk backing is
always a bit lame… could we create a funk-punk genre where the funk controls the instrumental with
always drum and bass underneath as the core anchor, and then we get a punk angry voice on top."*

🔑 **The two-halves construction again, with the genres swapped between the halves.** `punkbody` put
a metal throat on a punk band; this puts a **punk mouth on a funk band**. The construction is the
reusable thing — v1 proved the Style box holds band and voice as independent halves, and every
useful round since has been an assignment of one genre to each.

**Why the f1 funk lanes came back lame on the voice, and it was in the prompt.** All six of them
cast the singer in one short neutral clause — *"two low English men trade the verses, spoken, hard
and unhurried"* — because the round was testing **grooves**, and the vocal was deliberately held
constant so it would not confound the comparison. That was right for f1 and it is exactly why the
voice was flat: `spoken` and `unhurried` is not a performance, it is a placeholder. **This lane
gives the funk groove a real singer for the first time.**

**The vocal resolves a real tension rather than ducking it.** Kai rejected the punk voice once
already (`punkbody`, too snotty) and has consistently chosen **low and English** since. So this is a
punk *delivery* — shouted, sneering, ranted at the front of the beat — in a **low gravelly English**
voice, not the high snotty one. Plus the escalation device that fixed a1's flatness:
`getting louder every verse`.

**Short by design.** 562 characters against `angryvoice`'s 980 and `doomlow`'s 917 — the f1
finding held: three things named (groove, guitar, voice), not eleven.

*style 562 · exclude 516 · taste 866*

```style
FUNK RUNS THE BAND, OVER DRUM AND BASS AT 174. A chicken-scratch wah guitar riff one bar long, repeating with gaps; clavinet stabs answering it; a fat elastic bassline riding the sub. The chopped breakbeat anchors it and nothing fills the space between. THE VOICE IS PUNK AND FURIOUS. A low, gravelly English shout — snarled and sneering, ranted hard at the front of the beat, hard consonants bitten off, getting louder every verse. Close and hot on a cheap mic. Two British men: verse one smoke-worn, verse two plummy, both low, both raging. No chorus, no hook.
```

```taste
Music: funk runs the band, over drum and bass at 174. A one-bar chicken-scratch wah guitar riff repeating with gaps, clavinet stabs answering it, a fat elastic bassline riding the sub. The chopped breakbeat anchors everything and nothing fills the space between.

Vocals: punk and furious, but LOW and ENGLISH. A gravelly shout, snarled and sneering, ranted hard at the front of the beat, hard consonants bitten off, getting louder every verse, close and hot on a cheap mic. Never nasal, never whiny, no falsetto, no American vowels. Two British men, and they must stay two different men: one smoke-worn in his fifties, one clean and plummy. Both low, both raging. Never sung.

Register: a funk band with a rioter at the microphone. Tight and groove-led underneath, out of control on top.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
jangly guitar, wall of sound, strummed chords, power chords, hardcore punk, thrash, busy drumming, muddy bass, screaming, screamed vocal, death growl, gang vocals, gang shout, American accent, American vowels, US rock vocal, whiny vocal, nasal vocal, high-pitched vocal, falsetto, head voice, smooth soul, sweet soul, disco, funk horns, brass section, sung chorus, big chorus, vocal hooks, autotune, harmonies, feel good, uplifting, major key, party, comedic, polished production, half-time, slow tempo, tempo change
```

### Lane `angryvoice` — Annoyed band, angry voice

🎯 **Kai on the a1 takes, 2026-08-27:** *"all of the actual musical styles sounded really good —
guitar riffs at the beginning, breakbeat drum and bass setups. It's just the voice is very middle of
the road and meh… there's a chance that it's just the voice that's wrong as opposed to the underlying
instrumental."*

🔑 **The instrumental half is copied from `annoyed` VERBATIM — byte for byte, 429 characters
— and only the vocal half is rewritten.** That is the whole design, and it is only possible because
v1 proved the Style box holds band and voice as separable halves. It also makes this the cleanest
round in the sheet: anything that changes between a1 and this take is the voice.

🔴 **And it walks back `annoyed`'s vocal instruction on purpose.** a1 asked for
`contemptuous rather than furious — spat and half-muttered, rising only when a line earns it`.
**`half-muttered` and `rising only when a line earns it` are a recipe for "middle of the road and
meh"** — they ask the performance to stay flat and withhold, and that is what arrived. The restraint
experiment succeeded on the band and failed on the singer, which is a genuinely useful split:
**space in the arrangement reads as contempt; space in the vocal just reads as boring.**

**What replaces it:** `snarled through the teeth and seething`, `loud, chesty and out of patience`,
`hard consonants bitten off`, and — the part `annoyed` had no equivalent of — **a direction of
travel**: `the voice tightening and getting louder as every verse goes on`. A flat delivery has
nowhere to go, and "meh" is often just an absence of escalation. Plus `close and hot on a cheap mic,
distorting a little at the peaks`, because a clean centred vocal is itself middle-of-the-road.

**Everything proven is kept:** low, chest-deep, English, Midlands/northern vowels, two distinct men,
never nasal or whiny (the d1 → d2 fix), and `screaming`, `gang shout` and `death growl` stay banned —
furious is not the same as the hardcore shout Kai already rejected.

*style 980 · exclude 718 · taste 1137*

```style
THE GUITAR IS PUNK BUT IT DOES NOT PLAY LIKE PUNK. The same cheap trebly overdriven amp, but short choppy stabs and one wiry angular figure repeating, landing off the beat with whole bars left empty — never a wall of downstrokes, never constant, never strummed through. THE BAND IS DRUM AND BASS AT 174 BPM and it carries all of the pace by itself: chopped breakbeat, deep dry sub, rolling and unhurried. Space around everything. THE VOICE IS LOW, ENGLISH AND FURIOUS. A dark chest-deep baritone, gravelly and thick, snarled through the teeth and seething — loud, chesty and out of patience, hard consonants bitten off, the voice tightening and getting louder as every verse goes on. Close and hot on a cheap mic, distorting a little at the peaks. Never nasal, never whiny, no falsetto. Plain working-class English vowels, Midlands and northern. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy, both pitched low and both furious. No chorus, no hook.
```

```taste
Vocals: LOW, ENGLISH AND FURIOUS. A dark chest-deep baritone, gravelly and thick, snarled through the teeth and seething — loud, chesty, out of patience, hard consonants bitten off, tightening and getting louder as each verse goes on. Close and hot on a cheap mic, distorting a little at the peaks. Never nasal, never whiny, no falsetto, no head voice. Plain working-class English vowels, Midlands and northern, no American vowels. Two British men, and they must stay two different men: one gravelly and smoke-worn in his fifties, one clean and plummy. Both low, both furious. Never sung.

Music: drum and bass at 174 BPM carries all the pace on its own — chopped breakbeat, deep dry sub, rolling. On top of it a punk guitar tone that does NOT play like punk: short choppy stabs and one wiry angular figure repeating, landing off the beat, whole bars left empty. Never a wall of downstrokes. Space around everything.

Register: rage held at the edge of control — a man shouting because he has run out of any other way to say it. Never screamed, never chaotic.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
screaming, screamed vocal, death growl, growled vocal, gang shout, gang vocals, shouted chorus, chaotic, blast beats, wall of guitar, constant downstrokes, strummed chords, jangly guitar, muddy bass, busy drumming, hardcore punk, thrash, rapping, American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, keening, wailing, operatic vocals, big chorus, vocal hooks, catchy hook, pop melody, autotune, harmonies, anthemic, uplifting, feel good, major key, comedic, parody, half-time, halftime, slow tempo, tempo change, polished production
```

### Lane `annoyed` — Annoyed, not angry

🎯 **Kai, 2026-08-27:** *"it's feeling a bit fast and aggressive… it's the guitar side of the punk
that we're really liking… annoyed, pissed off, sarcastic rather than angry… I wonder if we're
leaning too heavily into the punk thing to try and get the anger, and that's actually overwhelming
everything else."*

🔑 **The principle this lane is built on: aggression came from the guitar's DENSITY, not its TONE.**
Hardcore punk is constant downstrokes — a wall with no gaps — and a wall reads as *shouting in your
face*. The tone (cheap trebly amp, overdriven, buzzing) is the part Kai likes and it is kept
untouched. What changes is the **behaviour**: short choppy stabs, one wiry angular figure repeating,
landing off the beat, **whole bars left empty**. Same guitar, a quarter as much of it.

**Restraint is what reads as contempt.** Loud-and-constant is anger; sparse-and-precise is
*sardonic*. That is the whole move, and it is why the fix is subtraction on one axis only rather
than a new genre — `annoyed`, `pissed off`, `sarcastic`, `sardonic`, `eye-rolling`, `contemptuous`,
`anger held in rather than shouted out`, with `furious`, `chaotic`, `screaming` and `blast beats`
banned outright.

**The drum and bass now carries all of the pace by itself**, which it was always capable of — the
punk kit was doubling a job the breakbeat was already doing, and that duplication is a second source
of the "too fast, too aggressive" feeling.

**The voice keeps the d2 fix and lowers its energy to match:** the same dark chest-deep English
baritone, but `spat and half-muttered, rising only when a line earns it` rather than roared. A
contemptuous record cannot have a singer who is shouting throughout — the restraint has to be in
both halves or it is in neither.

**Not a new direction — a dial turned down.** Three things have now held across every round and are
not in question: the punk **guitar tone**, the **low English voice**, and the **drum and bass
underneath**. This lane changes only how hard they hit.

*style 880 · exclude 718 · taste 1131*

```style
THE GUITAR IS PUNK BUT IT DOES NOT PLAY LIKE PUNK. The same cheap trebly overdriven amp, but short choppy stabs and one wiry angular figure repeating, landing off the beat with whole bars left empty — never a wall of downstrokes, never constant, never strummed through. THE BAND IS DRUM AND BASS AT 174 BPM and it carries all of the pace by itself: chopped breakbeat, deep dry sub, rolling and unhurried. Space around everything. THE VOICE IS LOW AND ENGLISH. A dark chest-deep baritone, gravelly and thick, dry and close on the mic, contemptuous rather than furious — spat and half-muttered, rising only when a line earns it. Plain working-class English vowels, Midlands and northern, hard consonants. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy, both pitched low. Annoyed, pissed off and sarcastic. Sardonic, not screaming. No chorus, no hook.
```

```taste
Vocals: a low English voice, contemptuous rather than furious. A dark chest-deep baritone — gravelly, thick, dry and close on the mic, spat and half-muttered, rising only when a line earns it. Never nasal, never whiny, never rising into head voice; no falsetto and no high notes. Plain working-class English vowels, Midlands and northern, hard consonants, no American vowels at all. Two British men, and they must stay two different men: one gravelly and smoke-worn in his fifties, one clean and plummy. Both pitched low. No chorus, no hook.

Music: drum and bass at 174 BPM carries all the pace on its own — chopped breakbeat, deep dry sub, rolling. On top of it a punk guitar tone that does NOT play like punk: short choppy stabs and one wiry angular figure repeating, landing off the beat, whole bars left empty. Never a wall of downstrokes. Space around everything.

Register: annoyed, pissed off and sarcastic. Sardonic and eye-rolling, contemptuous, restrained. Anger held in rather than shouted out. Never furious, never chaotic, never screaming.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
hardcore punk, thrash, blast beats, wall of guitar, constant downstrokes, strummed chords, power chord wall, screaming, screamed vocal, furious, chaotic, gang shout, gang vocals, shouted chorus, death growl, rapping, American accent, American vowels, transatlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, high-pitched vocal, tenor, head voice, falsetto, keening, wailing, soaring vocal, operatic vocals, big chorus, vocal hooks, catchy hook, pop melody, autotune, harmonies, anthemic, uplifting, feel good, major key, comedic, parody, half-time, halftime, slow tempo, tempo change, polished production, mastered loud
```

### Lane `doomlow` — Low English doom

🔴 **`sabbath` failed on timbre, and the prompt is why.** Kai on the d1 takes: *"too whiny,
high-pitched and American cheesy… we need a much lower tone… focus on an English voice."* The
`sabbath` style box literally asked for **`nasal, adenoidal, high-set`**, **`keening`**,
**`plaintive`** and **`wailing long vowels`**. Every one of those produces a high, thin, whining
vocal. The take was not a model failure; it was an accurate rendering of the words we gave it.

**So this lane inverts the timbre words and keeps the arrangement ones.** Kept from `sabbath`,
because none of them concern pitch: the take **doubled with itself**, **plate reverb**, **following
the guitar in unison**, **untrained**, **doom-laden**, and the tempo fence. Replaced outright:
`nasal` → **`chest-deep baritone`**; `high-set` → **`sung low, almost droning, heavy in the bottom
of the throat`**; `keening/plaintive/wailing` → **`gravelly, thick and resonant`**. Then the failure
is banned by name — `whiny vocal`, `nasal vocal`, `adenoidal`, `high-pitched vocal`, `tenor`,
`head voice`, `falsetto`, `keening`, `wailing`, `soaring vocal`.

🔴 **"American cheesy" gets its own fence.** `American accent` alone was already in the d1 excludes
and was not enough, because the *genre* default for this register is American. So the ban is widened
to the vowels and the styles: `American vowels`, `transatlantic accent`, `mid-Atlantic accent`,
`US rock vocal`, `radio rock vocal`, `post-grunge vocal`, `nu metal vocal`, `arena vocal`,
`emo vocal`, `pop punk vocal` — and the style box states the accent positively as **`plain
working-class English vowels, Midlands and northern`** rather than only saying what to avoid.

⚠️ **This has moved off the original reference, and that is Kai's call.** Low-and-English is not
the voice he named — that one is high and nasal by nature. What survives of it is the *arrangement*
(doubled take, unison with the riff, dread) rather than the timbre.

🟡 **One suspect left untested:** the lyric sheet still carries **`[mocking falsetto]`** in verse 2.
v1 ruled that section headers do not cast the voice, but that is a mid-verse *delivery* cue, which
is not the same thing. If a take still goes high in verse two, that line is the next place to look.

*style 917 · exclude 682 · taste 1212*

```style
THE BAND IS HARDCORE PUNK OVER DRUM AND BASS, AND IT DOES NOT SLOW DOWN. 174 BPM throughout, fast downstroke power chords through a cheap trebly amp, distorted bass, drums thrashed like a live kit over a chopped breakbeat, cymbals washing over everything. THE VOICE IS A LOW ENGLISH DOOM VOCAL. A dark, chest-deep baritone — gravelly, thick and resonant, sung low and almost droning, heavy in the bottom of the throat. Never nasal, never whiny, never rising into head voice: no falsetto and no high notes anywhere. Plain working-class English vowels, Midlands and northern, flat and unhurried, the consonants hard. Untrained and doom-laden, following the guitar in unison rather than singing a tune of its own, the take doubled with itself and drenched in plate reverb, sitting back behind the band. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy, both pitched low. No chorus, no hook.
```

```taste
Vocals: a LOW English doom vocal. A dark, chest-deep baritone — gravelly, thick and resonant, sung low and almost droning, heavy in the bottom of the throat. NEVER nasal, never whiny, never rising into head voice; no falsetto and no high notes anywhere. Plain working-class English vowels, Midlands and northern, flat and unhurried, hard consonants, no American vowels at all. Untrained and doom-laden, following the guitar in unison rather than singing a tune of its own. The take is doubled with itself and drenched in plate reverb, sitting back behind the band. Two British men, and they must stay two different men: one gravelly and smoke-worn in his fifties, one clean and plummy. Both pitched low. No chorus, no hook.

Music: hardcore punk over drum and bass at 174 BPM, and it never slows down. Fast downstroke power chords through a cheap trebly amp, distorted bass, drums thrashed like a live kit over a chopped breakbeat, cymbals washing over everything. Cut fast, mid-heavy, never polished.

Register: heavy, dark and English. Dread sung from the chest by a man too tired to shout, over a band playing far too fast for him.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, American vowels, transatlantic accent, mid-Atlantic accent, US rock vocal, radio rock vocal, post-grunge vocal, nu metal vocal, arena vocal, emo vocal, pop punk vocal, whiny vocal, nasal vocal, adenoidal, high-pitched vocal, tenor, head voice, falsetto, keening, wailing, soaring vocal, vibrato, operatic vocals, power metal, symphonic metal, gothic metal, comedic, parody, uplifting, major key, big chorus, vocal hooks, catchy hook, pop melody, autotune, harmonies, death growl, screaming, gang shout, gang vocals, rapping, doom tempo, sludge tempo, slow tempo, half-time, halftime, tempo change, blues rock, hair metal, shred, acoustic guitar, polished production
```

### Lane `sabbath` — Doom wail over punk

🎯 **Kai, 2026-08-27:** the Black Sabbath / Ozzy register — *"obviously we can't put Ozzy Osbourne
into Suno because it will block us"* — with the punk drum-and-bass instrumental kept underneath.

🔴 **Named artists are off the table** (Suno flagged `Linkin Park` live on 2026-08-26), so the
register goes in as **description**: nasal, adenoidal, high-set; a Black Country Birmingham accent;
keening and untrained; long wailed vowels bending flat at line ends; **following the guitar in
unison rather than singing its own tune** (the defining trick of that band's vocal arrangement);
**the take doubled with itself slightly out of time**, plate reverb and tape flange, sitting back
behind the band. Every one of those is a *sound*, not a name, and together they are more specific
than the name would have been.

🔴 **This lane lifts `never sung`, and that is the only lane that does.** The register is a wail —
a sung line — so the rule that has protected every other Camping round is suspended here on
purpose. The cheese it was guarding against is held off by other means instead: `big chorus`,
`vocal hooks`, `catchy hook` and `pop melody` are all banned, so the voice may sing but the record
still cannot grow a hook.

🔴 **And it fights its own genre's tempo.** That register implies *slow*, and Kai's instruction is
that the punk drum and bass stays. So the style box opens with `AND IT DOES NOT SLOW DOWN`, repeats
174 BPM, and the excludes ban `doom tempo`, `sludge tempo`, `slow tempo`, `half-time` and
`tempo change`. **If a take drags, that is the failure mode to watch for** — not the voice.

**Lyrics are deliberately untouched.** v1 proved the section headers do not move the casting
(A and B came back the same), so leaving them alone keeps this a clean one-variable round.

*style 808 · exclude 464 · taste 1044*

```style
THE BAND IS HARDCORE PUNK OVER DRUM AND BASS, AND IT DOES NOT SLOW DOWN. 174 BPM the whole way, fast downstroke power chords through a cheap trebly amp, distorted bass, drums thrashed like a live kit over a chopped breakbeat, cymbals washing over everything. THE VOICE IS EARLY-SEVENTIES BRITISH DOOM METAL. A nasal, adenoidal, high-set male voice with a Black Country Birmingham accent — keening, plaintive and untrained, wailing long vowels, bending flat at the ends of lines, following the guitar in unison rather than singing its own tune. The take is doubled with itself, slightly out of time, drenched in plate reverb and tape flange, sitting back behind the band. Two British men: verse one gravelly and smoke-worn, verse two clean and plummy, both wailing. Ominous and doom-laden. No chorus, no hook.
```

```taste
Vocals: an early-seventies British doom-metal wail. Nasal, adenoidal and high-set, with a Black Country Birmingham accent — keening, plaintive, untrained, holding long vowels and bending flat at the ends of lines, following the guitar line in unison rather than singing a tune of its own. The take is doubled with itself slightly out of time, drenched in plate reverb and tape flange, sitting back behind the band. Two British men, and they must stay two different men: one gravelly and smoke-worn in his fifties, one clean and plummy. Both wail. No chorus and no hook anywhere.

Music: hardcore punk over drum and bass at 174 BPM, and it never slows down. Fast downstroke power chords through a cheap trebly amp, distorted bass, drums thrashed like a live kit over a chopped breakbeat, cymbals washing over everything. Cut fast, mid-heavy, never polished.

Register: doom-laden and ominous, sung by a man who is frightened, over a band playing far too fast for him.

Subject: British class, money, work, and the people the economy left behind.
```

```exclude
American accent, comedic, parody, uplifting, major key, big chorus, vocal hooks, catchy hook, pop melody, autotune, harmonies, death growl, growled vocal, screaming, gang shout, gang vocals, snotty punk vocal, sneering vocal, rapped vocal, rapping, operatic vocals, power metal, symphonic metal, gothic metal, modern metal, polished production, doom tempo, sludge tempo, slow tempo, half-time, halftime, tempo change, blues rock, hair metal, shred, acoustic guitar
```

## The instrument/voice split test

Can a prompt hold **punk instruments and a metal voice** at once? Two levers exist and they are
tested separately, because knowing *which one works* is worth more than one good take.

| | What moves | Question it answers |
|---|---|---|
| **A** | the `punkbody` prompt only — lyrics unchanged | Is stating the seam in the Style box, plus banning the punk vocal by name, enough on its own? |
| **B** | `punkbody` **and** recast section headers (variant C) | Do the lyric section headers out-vote the Style box on casting? |

🔴 **Why B exists at all.** The live cue sheet was still casting the voice from two abandoned
rounds: `[Verse 1 | gravelly **rapped** voice…]` (the h12 rap-rock pivot) and
`[Intro — 2 bars, high-register **80s rock guitar lick**…]` (the h10 Steve Vai round). Nothing in it
ever said *roar*. **Section headers are the only genuinely section-scoped casting control we have**,
so a header saying `rapped` while the Style box says `roar` is a fight the Style box may well lose.

Variant C changes **only bracket text** — no cue line added, none removed — so the first-verse
timing fix stays exactly as it is. Per `suno-voices.md` §3, each character gets **one fixed short
label repeated identically** (`[gravelly roared voice]`, `[posh roared voice]`); freshly-worded
descriptions read as a new character each time.

```lyricsC
[Intro — 2 bars, one downtuned guitar burst, straight to the beat]
[Verse 1 | gravelly roared voice, throat-first, tight to the beat | no drums for the first half, then the breakbeat]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
[whispered]
but I bet, that you paid for your wheels on tick!
[hard and slow]
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[spoken word, quiet, drums out]
I can't live like this forever
[back on the beat, roared, and straight through to the end of the verse]
I might be insane but I do want change, 
let's see what we can arrange!
now, I insist that I hold that door
[shout, cracking, begging]
please sir, can I FUCKIN, have some more?
[Verse 2 | posh roared voice, a completely different man]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
[mocking falsetto]
What about if we taxed the rich?
[angry]
what the fuck you think this is, BITCH!
[posh roared voice]
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Bridge | the two men trade, close and dry | drums stripped back]
[gravelly roared voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[posh roared voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[pause | posh roared voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly roared voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[posh roared voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly roared voice]
yet I don't begrudge you,
it's us and them now
[pause | posh roared voice]
well we don't have long
[Outro — both voices]
and by the time it hits, we'll be gone
[end]
```

## Timing test — the first-verse stutter

🔴 **Two lyric files, two different cue sets.** Kai reads `camping.md`; the runner generates from
this sheet's § Lyrics. In that one run they disagree — `camping.md` has **no cue** before
*"let's see what we can arrange!"*, and the generated sheet has **`[sarcastic, high pitched]`**.
That is why the stutter looked unprompted. **Whatever this test settles must be written back into
BOTH files, or the next session inherits the same confusion.**

**Two hypotheses, one test, same words in both.** Only the bracket cues differ.

| | Hypothesis | Cues in the run |
|---|---|---|
| **A** — Kai | A standalone cue is a *directive*, and the delivery reverts unless it is restated. So restate it before every line. | **5** |
| **B** — the toolkit | A standalone cue is a *section boundary*: Suno re-enters at each one, and the re-entry IS the stutter. Our own GPOM notes call dense cues "micro-sections that each re-decide their own phrasing" and say a timing fault is a reason to **strip cues before anything else**. | **3** |

Both keep the dip at *"I can't live like this forever"* (which works) and the
`[shout, cracking, begging]` before *"please sir"* (which Kai wants kept). They differ only in what
happens across the three lines between.

```lyricsA
[Intro — 2 bars, high-register 80s rock guitar lick, straight to the beat]
[Verse 1 | gravelly rapped voice, tight to the beat | no drums for the first half, then the breakbeat]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
[whispered]
but I bet, that you paid for your wheels on tick!
[hard and slow]
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[spoken word, quiet, drums out]
I can't live like this forever
[still spoken word, back on the beat, raised]
I might be insane but I do want change, 
[still spoken word, sarcastic]
let's see what we can arrange!
[still spoken word, level, straight on with no pause]
now, I insist that I hold that door
[shout, cracking, begging]
please sir, can I FUCKIN, have some more?
[Verse 2 | posh voice, a completely different man]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
[mocking falsetto]
What about if we taxed the rich?
[angry]
what the fuck you think this is, BITCH!
[posh voice]
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Bridge | the two men trade, close and dry | drums stripped back]
[gravelly voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[pause | posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly voice]
yet I don't begrudge you,
it's us and them now
[pause | posh voice]
well we don't have long
[Outro — both voices]
and by the time it hits, we'll be gone
[end]
```

```lyricsB
[Intro — 2 bars, high-register 80s rock guitar lick, straight to the beat]
[Verse 1 | gravelly rapped voice, tight to the beat | no drums for the first half, then the breakbeat]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
[whispered]
but I bet, that you paid for your wheels on tick!
[hard and slow]
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
[spoken word, quiet, drums out]
I can't live like this forever
[back on the beat, raised, and straight through to the end of the verse]
I might be insane but I do want change, 
let's see what we can arrange!
now, I insist that I hold that door
[shout, cracking, begging]
please sir, can I FUCKIN, have some more?
[Verse 2 | posh voice, a completely different man]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
[mocking falsetto]
What about if we taxed the rich?
[angry]
what the fuck you think this is, BITCH!
[posh voice]
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Bridge | the two men trade, close and dry | drums stripped back]
[gravelly voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[pause | posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly voice]
yet I don't begrudge you,
it's us and them now
[pause | posh voice]
well we don't have long
[Outro — both voices]
and by the time it hits, we'll be gone
[end]
```

---

## 🥇 mr1 — the mod R&B holler, and the take Kai liked most

**Ruled by ear, 2026-09-08: *"this is the song I liked the most."*** The boxes came out of a voice
sweep on **2026-09-05** and were never written down at the time — they lived in a session
transcript until Kai pasted three of them back and asked for the matching My Taste. They are
recorded here verbatim.

⚠️ **This lane predates the consolidation conventions.** It ran on the four-box set below with
**its own lyrics** (`lyricsD`), not this sheet's § Lyrics. Running it through
[`camping.mts`](../../../../scripts/suno/camping.mts) will therefore load the lane's three fences
against the **live** cue sheet, which is a different performance. To reproduce the liked take,
§ Lyrics must first be switched to `lyricsD` — the same one-line edit the § *Timing test* variants
use.

**The complaint going in was "every take is the same man, and the delivery is cheesy."** Three
causes were found, and each is answered by one part of this lane.

| What was wrong | Mechanism | Answered by |
|---|---|---|
| Every variant came back the same man | `British post-punk spoken word` sat in the **leading slot of the Style box and opened My Taste** — one pool voting in two boxes, and nothing downstream outvotes that | a pool-neutral `taste` fence with no genre words in the Vocals line, plus an entirely different lead tradition in `style` |
| Cheesy, barked emphasis | caps are a **volume instruction**, exclamation marks push toward a shout, and `[shout…]` / `[mocking falsetto sneer]` are literal theatre directions | `lyricsD` — every one of them removed |
| Homogenised vocalist | v5.5 is *"more polished and consistent, but blander"*; **v4.5+ gives different vocalists between generations** | 🔴 **the model, not a box** — this lane ran on **v4.5+**, not the sheet's v5.5 |

**Sliders:** Style Influence **75** · Weirdness **30** · Audio Influence n/a (fresh, nothing
attached) · **no saved Voice**.

🔴 **Weirdness 30 is below this repo's own neutral of 50 and was never tested against it.** Whether
the liked take is good *because of* 30 or *despite* it is open — the pair at 30/50 with every box
frozen is the round that settles it, and it has not been run.

🔴 **The exclude fence is 935 characters** and [`camping.mts`](../../../../scripts/suno/camping.mts)
prints its budget as 933. Whether 933 is a real cap or a stale constant is **unverified** — if it is
real, `slow tempo` loses its last two characters. It is left verbatim because this is the box the
liked take actually ran with.

### Lane `modrb` — 1960s mod R&B holler

*style 899 · exclude 935 · taste 1761*

Picked out of a four-way sweep of vocal traditions — **F** 1977 punk snarl · **G** mod R&B holler ·
**H** British trip hop, half-spoken · **I** pub rock talking blues. This is G. The other three are
not recorded: they were never generated once G landed.

📎 **A small bloke with an enormous torn voice.** The lane works because it changes the *larynx*,
not the adjective — hoarse and throaty where every previous round had been nasal and thin. Note
that it does **not** ban depth or weight: `deep`, `chest voice` and `baritone` are banned in the
narration sheet, where a voice kept coming back too deep, and importing that ban here on 2026-09-05
took the size out of "an enormous raspy voice" and flattened the whole take. It was reverted the
same evening.

```style
Dark UK drum and bass, neurofunk, 174 BPM, minor key. 1960s British mod R&B holler on top, hollered over the beat, never sung. Verse one: a weathered English man in his fifties - a small bloke with an enormous raspy voice, torn and hoarse at the top of every line, hard English consonants, throaty and unpolished, no vibrato, bone dry. Verse two: a well-spoken British man, higher, clean, plummy BBC English, wide room. Under every vocal a low palm-muted guitar riff, one short figure repeating, never a solo, never chords. At the drops it opens into a wall of chiming Britpop guitars strumming slow and wide at half speed over the kit at full weight, Reese sub, screaming wavetable lead, tambourine on every beat, so guitars, synth and break are one piece of music, not a remix of one by the other. Chopped amen rolls tearing across every fourth bar. Grim and bitter, played straight, steady tempo.
```

```taste
Vocals: two English men in their late forties and fifties, talking over the beat rather than singing — there is no melody in either of them. One is low, gravelly, smoke-worn and nasal, close and bone dry on a cheap mic. The other is higher, clean and plummy BBC English, precise and unhurried, talking down at you from a wide room. Talking over singing, every time. Flat and unbothered over theatrical. Raw over polished.

Music: dark UK drum and bass and neurofunk at 174 BPM, minor key. Rolling Reese bass, deep sub, dry chopped breakbeats, industrial stabs. Drum fills that tear across a whole bar every few bars: chopped amen rolls, snares tumbling over each other, loud at the front of the mix, then straight back into the groove. Arrangements that climb in steps: a track that opens on one unaccompanied instrument and does not show its full weight until the drop. Big aggressive wavetable synthesizers where an orchestra would be: screaming detuned leads, hard-synced and formant-morphing, growling gnarly mid-range. In the drops and outro only, a wall of chiming Britpop guitars, layered and doubled, strumming slow and wide at half the speed of the break, tambourine on every beat, so the guitars, the synths and the break are one piece of music, not a remix of one by the other. Under the vocals the guitar is only a low palm-muted figure, never chords, never a tune. No orchestral instruments and no piano anywhere. Cold, grimy, relentless, rock steady in tempo start to finish. A British record, made in Britain, about Britain.

Register: bleak, bitter, angry, played completely straight. Whatever is funny lives in the words alone — the music never winks and never plays along.

Subject: British class, money, work, and who the economy left behind.
```

```exclude
singing, sung verses, sung chorus, melodic vocal, vocal melody, vocal hooks, crooning, clean sung melody, autotune, harmonies, grime MC, UK drill, road rap, trap, hip hop, young MC, American accent, American vocal, US rap, transatlantic, southern drawl, ragga MC, toasting, Jamaican accent, dancehall vocal, soprano, operatic vocals, vibrato, angelic voices, sustained vocal notes, female vocal, children's choir, choral harmony, orchestral strings, violins, cello, string section, piano, glockenspiel, brass band, marching band, oompah, dixieland, guitar solo, lead guitar, shredding, acoustic guitar, wah, mashup, bootleg, remix, rock remix, nu metal, rap rock, rapcore, grunge, punk, epic trailer music, reggae, dub, ska, music hall, vaudeville, pantomime, ragtime, honky-tonk, liquid dnb, jump up, pop, lo-fi, jaunty, playful, whimsical, bouncy, comedic, novelty, parody, uplifting, major key, double time, tempo change, slow tempo
```

### `lyricsD` — de-dramatised, what `modrb` ran with

Every shout, falsetto and whisper cue deleted, caps lowercased, emphasis exclamation marks removed.
The **words** are unchanged and still pass the `camping.md` §4 guard. What replaces the performance
cues is per-section **arrangement** description — what plays and what does not.

⚠️ **The known cost, and the sheet already warned of it:** stripping every performance cue may take
the peaks with it. If it comes back monotone, re-add **one** cue only — `[quieter, close]` before
*"but I bet, that you paid for your wheels on tick"*.

```lyricsD
[Intro — 8 bars | one long low detuned synth note, completely alone, held and slowly filtering open | a texture, not a tune, no melody | distant city hum far underneath | no drums, no bass, no guitar]
[Verse 1 | gravelly ranting voice, flat and unbothered, never selling a line | the low synth note holds underneath | no drums and no bass for the first half of this verse, then a dry chopped breakbeat comes in under the vocal and runs to the drop | amen rolls tearing across every fourth bar | the words never stop, no instrumental passage in this verse]
Once again, and you catching my eye,
and you looking to the side in shame, but why
now, let me explain, how I'm just poor
you keep on walking, through that Wait trose door
presenting yourself, with your shiny teeth
fucking sense of entitlement, and self belief
I get, that you think your deals are slick
but I bet, that you paid for your wheels on tick
cash from the bank for your wank tank
four tonnes of steel, just to get a meal deal
you got cheese but I want Cheddar
I can't live like this forever
I might be insane but I do want change, 
let's see what we can arrange
now, I insist that I hold that door
please sir, can I fuckin, have some more?
[Drop — instrumental, 8 bars, no vocals | the kit hits full weight and the sub bass drops for the first time | amen rolls tearing across every fourth bar | the palm-muted riff opens out into a wall of chiming Britpop guitars, strumming slow and wide at half the speed of the kit, tambourine on every beat | the wavetable lead tears in over the top]
[Beat Transition]
[Verse 2 | well-spoken posh voice, a completely different man, dry and unbothered, never selling a line | full-weight drum and bass carries straight on, drums flip, colder synths, sharper hats | amen rolls tearing across every fourth bar | the guitar wall is gone, only the same palm-muted riff returns underneath, unchanged | nothing else playing at all]
you are intent on living in a tent
it's a lack of work ethic, it's pathetic, 
getting parra lettic, it seems that you are just a bum
drowning your sorrow until tomorrow comes
prospects exist and now I insist
that you just stop the grift 
What about if we taxed the rich?
what the fuck you think this is, bitch
I work hard to pay for my yard
Payin my tax with a platinum card
you want change but my pockets are empty
the only thing I'm changing, is the lane in my M3
if you worked hard, then you could have plenty, fenty,
all you now seem to do, is resent me.
wealth gap? fuckin what a load of crap
now please let me drink my shatoe nerf doo pap
[Drop — instrumental, 8 bars, no vocals | everything heavier and more distorted than the first drop — neuro bass growling underneath, the amen rolls harder and longer, the lead screaming higher, the guitar wall thicker and wider than before]
[Beat Transition]
[Bridge | the turn | drums strip right back, intimate | the two men trade, both close and dry in the same cold room now | the guitar riff sparser and quieter here, still one repeating figure, never a tune]
[gravelly ranting voice]
Oh shit, here we both are, living in a car
park, rained on in the fucking dark
[well-spoken posh voice]
went down the wrong track, then I got the sack,
then I drank, broke my back, now I'm in the last part
[both men together, doubled]
the AI does the fast part, now, the real question is
will it allow, because it's in charge now...
[well-spoken posh voice]
you see as it turns out, there is very little clout,
in having the manager or any of the c-suite about
[gravelly ranting voice]
the speed the robots replaced us was quicker
and sicker than when the government debased us
[well-spoken posh voice]
back to that time when we very first met,
I do regret that I judged you, I was wrong,
[gravelly ranting voice]
yet I don't begrudge you,
it's us and them now
[well-spoken posh voice]
well we don't have long
[Outro — 8 bars | both men together, and behind them a football terrace of hoarse untrained British men roaring the line with them in unison, massed and low, close and dry | the guitar wall comes back wide and slow underneath | then diminuendo, voices, guitars and bass dissolve into static]
and by the time it hits, we'll be gone
[end]
```

### 🔴 Three near-misses from the same evening — none of them is this lane

| Variant | What changed | Verdict |
|---|---|---|
| **taste 1,786** (19:25) | `low` → `mid-range` + `sandpaper grit`; `growling` deleted from the synth line; ten growl bans added to exclude | 🔴 **Rejected — "the song is too flat."** Taking the *size* out of the voice is what did it |
| **taste 1,851** (19:56) | the above reverted, except `Flat and unbothered over theatrical` → `Bored on the surface and furious underneath`; four narrow growl bans kept (`guttural, death growl, harsh vocals, screamed vocal`); four performance cues restored to the lyrics | 🟡 **Untested against the liked take.** It differs from the `taste` fence above by one sentence — a legitimate single-variable round if flatness returns |
| **the jungle recut** (20:08) | `Dark UK drum and bass, neurofunk` → `1994 UK jungle`; guitars moved from drops-only to global; `reggae` and `dub` taken out of exclude | 🔴 **"None of those are like this one."** A different track |

🔑 **The escalation nobody has run.** If two more traditions return the same man, that is
convergence on the pool centroid and **no adjective jumps a pool**. The next lever is a **Voice
transplant**: best 15 seconds of any take → ⋯ → Remix → Voice, **delete the attached style
prompt**, then apply it to the take with the best delivery at audio influence 40–60. Unrun, and
unverified.

---

## Round log

### mr1 — 2026-09-05, the vocal-tradition sweep. 🥇 **`modrb` RULED IN by ear, 2026-09-08.**

Run outside this sheet, before the boxes had anywhere to live — the whole round survived only in a
session transcript until Kai pasted the Style, Exclude and Lyrics back on 2026-09-08 and asked for
the My Taste that went with them. Now filed as lane `modrb` above, with its own `lyricsD`.

**The finding that unblocked it:** every previous variant had kept `British post-punk spoken word`
in the **leading slot of the Style box** *and* at the head of `My Taste`. One pool, voting twice,
from two boxes — which is why nine rounds of adjectives all returned the same man. The fix was not
a better adjective, it was **removing the genre words from `My Taste` entirely** so the Style box
could cast alone.

📎 **Two levers were pulled that this sheet does not otherwise use:** the model dropped to **v4.5+**
(different vocalists between generations, where v5.5 homogenises), and every performance cue came
out of the lyrics — caps, exclamation marks and `[shout…]` directions are all volume instructions,
and they were the cheese.

🔴 **Two things are still unaudited.** No take from this round is filed in a workspace or linked
anywhere — the audio exists only in Kai's Suno library. And the lane has never been run *from this
sheet*, so its fences are recorded but not exercised.


### pv1 / vv1 — 2026-08-27, the voice search. ✅ **`v-pub` RULED IN.**

**vv1: six voices over one frozen band** (the {} band half, byte-identical in all six, run as covers
of the approved take so the arrangement was anchored twice). Kai: ***"the pub aggression is a great
voice, I like that a lot."*** `v-pub` — *a man squaring up in a pub: loud, thick English baritone,
consonants slurring at the edges, too close to the mic and clipping, veering between a mutter and a
bark without warning* — is the voice this song has been looking for since h1.

📎 **Why it took twenty rounds to find.** Every earlier vocal instruction described an *attitude*
(`contemptuous`, `furious`, `annoyed`, `barked`) and the model returned a competent generic
delivery. `v-pub` describes a **situation and a microphone**: who the man is, where he is standing,
what the signal chain is doing. **Describe the performance, not the emotion** — the emotion is what
the words already carry.

**pv1: that voice against two bands, each run fresh AND as a cover** — four creates, eight takes.
`pub-stabs` (the sparse arrangement Kai approved) against `pub-fullpunk` (an actual hardcore punk
band), because "the punk instrumental layer" had meant both things in this sheet and guessing would
have wasted the round. The fresh/cover pairing answers the second question in the same breath:
**`v-pub` had only ever been heard as a cover**, so its band came largely from the source audio. If
fresh sounds thinner, the arrangement lives in the audio and covers are the lane from here on.

🔑 **And this was the first round with cover mode fully automated in both directions** — the log
reads `detach:ok` → fresh → release → claim → `attach:ok … 02:58 (2 matched, took #1)` → cover →
release → re-verified, with no human touching the browser.

### fp1 / a3 / f1 — 2026-08-27, the two-halves era. **Verdicts pending.**

Three rounds run back to back, all resting on the **v1 construction**: the Style box holds a *band
half* and a *voice half* and they can be assigned to different genres independently. Every useful
round since v1 has been an assignment.

| Round | Band half | Voice half | Why |
|---|---|---|---|
| **f1** (12 takes) | six funk/soul/punk grooves | *held constant, deliberately neutral* | testing grooves; the vocal was a control |
| **a3** (4 takes) | `annoyed`, **copied verbatim** | rewritten furious | Kai: the band is right, the voice is meh |
| **fp1** (4 takes) | funk (chicken-scratch wah, clav, elastic bass) | punk, low and English | Kai: *"funk controls the instrumental… a punk angry voice on top"* |

🔴 **A control looks like a failure if you forget it is a control.** All six f1 lanes cast the
singer as *"two low English men, spoken, hard and unhurried"* — one neutral clause, held identical
so the groove comparison would not be confounded. Kai heard the result as *"the singing voice on the
funk backing is always a bit lame"*, and he was right about the sound: **`spoken` and `unhurried` is
not a performance, it is a placeholder.** The f1 takes are evidence about **grooves only**, and
should be judged with the vocal discounted. fp1 exists because a groove deserves a real singer
before anyone rules on it.

🔑 **The a1 → a3 split is the session's most transferable finding: space in the ARRANGEMENT reads as
contempt; space in the VOCAL reads as boring.** The same restraint instruction that made the band
work (`whole bars left empty`, `never constant`) made the singer flat (`half-muttered`, `rising only
when a line earns it`). Restraint is a property of arrangements, not of performances — and "meh" is
very often just an absence of escalation, which is why both new lanes carry
`getting louder every verse`.

🟡 **fp1 resolves a standing contradiction rather than ducking it.** Kai rejected the punk voice
once (`punkbody`: too snotty) and has chosen **low and English** every time since. So fp1 asks for a
punk *delivery* — shouted, sneering, ranted at the front of the beat — in a **low gravelly English**
voice. If it comes back snotty, the delivery and the timbre are not separable and that is worth
knowing.

### a2 — 2026-08-27, the Style Influence line. 3/3 clean, 6 takes. **Verdict pending.**

Kai: *"how confident are we about our style influence of a hundred? Is that not making everything
too much?"* **Correct challenge — SI 100 was a judgement call, never a measurement.** It was raised
to 100 for `sabbath` because that lane was almost entirely a vocal description, and then carried
into `doomlow` and `annoyed` without ever being retested.

🔑 **There is a specific reason it may be actively wrong on this lane.** `annoyed` is a prompt about
**restraint and empty space**. Style Influence is how hard the model is made to deliver every clause
it can see. **Maximum obedience to a prompt about holding back is close to self-defeating** — the
model tries to render all of it, which is the opposite of leaving bars empty.

A pure SLIDER round on the `annoyed` lane: **SI 40 / 60 / 80 at W 30**, prompt frozen (style 880,
exclude 718, taste, 70 lyric paragraphs, re-measured per cell). With `(a1)`'s `SI100 W30` cell
already rendered, that is **four points on one line** — a direction to read, not four guesses.

🎧 **A second, independent vote is already sitting unjudged:** `(s1)`'s `Camping punk-metal SI50 W30`
against `SI100 W30`, the same question asked of a different prompt. If looser wins in both, the
finding generalises beyond this lane.

### a1 — 2026-08-27, annoyed not angry. 2/2 clean, 4 takes. **Verdict pending.**

Kai: *"a bit fast and aggressive… it's the guitar side of the punk that we're really liking…
annoyed, pissed off, sarcastic rather than angry."*

🔑 **The finding this round is built on: the aggression was the guitar's DENSITY, not its TONE.**
Hardcore punk is constant downstrokes — a wall with no gaps, and a wall reads as shouting in your
face. The tone Kai likes is untouched; only the **behaviour** changed: choppy stabs, one wiry
figure repeating off the beat, whole bars left empty. Same guitar, a quarter as much of it.
**Loud-and-constant is anger; sparse-and-precise is contempt** — restraint is what reads as
sarcasm, and that is a general principle, not a Camping one.

Two consequences followed. **The breakbeat now carries all the pace alone** — the punk kit had been
doubling a job the drum and bass already did, which was a second, independent source of "too fast".
And **the voice came down to match** (`spat and half-muttered, rising only when a line earns it`),
because a contemptuous record cannot have a singer shouting throughout.

### d2 — 2026-08-27, the low English doom. 2/2 clean, 4 takes. **Verdict pending.**

The timbre inversion after d1's rejection: `nasal` → `chest-deep baritone`, `high-set` → `sung low,
almost droning`, `keening/plaintive/wailing` → `gravelly, thick and resonant`, with the failure
banned by name and **"American" fenced at the level of vowels and styles** rather than just
`American accent`, which had already been in the d1 excludes and was not enough — the genre's own
default is American, so a single ban does not hold it.

🔑 **Stating the accent positively beat banning its opposite:** `plain working-class English vowels,
Midlands and northern, hard consonants` is in the style box, not just a list of what to avoid.

🟡 **Still untested:** the lyric sheet's `[mocking falsetto]` in verse 2. v1 ruled that section
*headers* do not cast the voice, but that is a mid-verse *delivery* cue and the ruling does not
cover it. If a take climbs in verse two, look there next.

### d1 — 2026-08-27, the doom wail. 2/2 clean, 4 takes. 🔴 **REJECTED on timbre.**

**Kai: *"too whiny, high-pitched and American cheesy… we need a much lower tone… focus on an
English voice."*** The prompt asked for `nasal, adenoidal, high-set`, `keening`, `plaintive` and
`wailing long vowels`. **That is a recipe for a thin, high, whining voice, and the take rendered it
accurately.** Not a model failure — a prompt failure, and the third time this session a "genre
didn't work" verdict has traced back to our own words (h10's lead guitar, c1's cheese, this).

📎 **The lesson worth keeping: describing a real singer's timbre honestly can import the half you
did not want.** That voice genuinely *is* nasal and high-set; those words are accurate. Accuracy is
not the goal — **the sound you want is.** Take the arrangement traits (doubling, unison with the
riff, dread) and write the timbre from scratch.

Kai asked for the Black Sabbath register — *"Ozzy Osbourne style voice… obviously we can't put Ozzy
Osbourne into Suno because it will block us"* — with the punk drum-and-bass instrumental kept
underneath. Ran straight after v1 proved the Style box is what casts the voice, so this is a clean
one-variable round: the vocal half of the prompt, and nothing else.

**How the register went in without the name.** Nasal, adenoidal, high-set; a Black Country
Birmingham accent; keening and untrained; long wailed vowels bending flat at line ends; **following
the guitar in unison rather than singing its own tune**; **the take doubled with itself slightly out
of time**, plate reverb and tape flange, sitting back behind the band. Each is a *sound*, and
together they are more specific than the name would have been — the unison-with-the-riff trick in
particular is what most people hear as "that sound" without being able to name it.

🔴 **Two rules were deliberately broken, and both are fenced.** `never sung` is lifted — the only
lane in this sheet where it is — because the register *is* a sung wail; the cheese it guarded
against is held off by banning `big chorus`, `vocal hooks`, `catchy hook` and `pop melody` instead,
so the voice may sing but the record still cannot grow a hook. And the register **implies a tempo
the brief forbids**: the style box therefore opens `AND IT DOES NOT SLOW DOWN`, states 174 twice,
and the excludes ban `doom tempo`, `sludge tempo`, `slow tempo`, `half-time` and `tempo change`.
**A dragging take is this lane's expected failure mode, and it is not a failure of the voice.**

Two cells, SI 75 and SI 100 at W 45 — because this lane's entire content is a vocal description, so
Style Influence is the dial that decides how literally it is followed.

### v1 — 2026-08-27, the instrument/voice split. 2/2 clean, 4 takes. ✅ **RULED.**

**Kai's verdict: both takes roar, and A and B sound the same.** Two findings, and the second one
retires a hypothesis:

1. ✅ **The instrument/voice split WORKS.** A punk band with a metal throat over it is a thing the
   Style box can be asked for directly. The two-halves-in-caps construction plus banning the punk
   vocal *by name* is the pattern; keep it.
2. 🔴 **Lyric section headers do NOT move the vocal casting.** B recast every header to
   `[gravelly roared voice]` / `[posh roared voice]` and came back indistinguishable from A, whose
   headers still said `gravelly rapped voice`. **The Style box out-votes the headers on casting.**
   This is worth more than the takes: it means a stale header is *not* the thing to chase when a
   voice comes out wrong, and it retires the lever before we spent a round on it again.

⚠️ **Scope of the ruling: casting only.** This says nothing about whether headers control *timing*
or *arrangement* — the first-verse stutter fix was a header/cue change and it worked. Cues still
shape structure; they just do not choose the singer.

Kai: *"we're liking the punk instrumental layer, but the voice doesn't work very well as a punk
voice… somehow split these two genres by instrumental and voice, would that be possible?"*

🔴 **It was possible all along, and the lyric sheet was voting against it.** The live cue sheet
still carried `[Verse 1 | gravelly **rapped** voice…]` from the h12 rap-rock pivot and
`[Intro — 2 bars, high-register **80s rock guitar lick**…]` from the h10 Steve Vai round. **Nothing
in it ever said roar.** Every punk-metal round so far has had its Style box asking for one thing
while its section headers asked for another — and section headers are the only genuinely
**section-scoped** casting control the platform offers, so that is not a fight the Style box can be
assumed to win.

`Camping punk-body A (v1)` — the new two-halves prompt, lyrics untouched.
`Camping punk-body B (v1)` — the same prompt with the headers recast.

**What each outcome means.** B better → the headers are the casting control, and they get fixed
once for every future round. A ≈ B → the Style box was already winning and the voice needs
different *words*, not a different place to put them. Neither → punk instrumentation may simply drag
the vocal with it, and the cover route (map Audio Influence against the take Kai likes) is next.

**The lane's design, worth keeping whatever the verdict.** `punkmetal` described one blended thing
and let the model decide which half won. `punkbody` **states the seam in caps with an explicit
denial** — `THE BAND IS HARDCORE PUNK` / `THE VOICE IS NOT PUNK — IT IS METAL` — and bans the punk
vocal *by name* (`snotty vocal`, `hoarse yelping`, `yelped vocal`, `gang shout`) while leaving every
punk instrument word untouched. An exclude has no section scope, but a term that is **about the
voice** is scoped by its own meaning, and that is the only scoping excludes offer.

**Variant C changed bracket TEXT only — no cue line added or removed** — so the first-verse timing
fix survives intact, and each character carries **one fixed short label repeated identically**
(`[gravelly roared voice]`, `[posh roared voice]`) per `suno-voices.md` §3: freshly-worded
descriptions read as a new character every time, which is how a duet comes apart.

### s1 — 2026-08-27, the first true SLIDER round. 6/6 clean, 12 takes. **Verdict pending.**

Kai: *"an experiment that does not change any of the prompt settings for the moment… just to see
if we are just needing to iterate on the same prompt, almost rolling the dice."* The punk-metal
lane held completely still — style 709, exclude 382, taste 730, 70 lyric paragraphs, re-written and
**re-measured before every one of the six Creates** — and only the two dials moved.

| | Weirdness 30 | Weirdness 60 |
|---|---|---|
| **Style Influence 50** | `SI50 W30` | `SI50 W60` |
| **Style Influence 75** | `SI75 W30` | *(p1 sits at W45)* · `SI75 W60` |
| **Style Influence 100** | `SI100 W30` | `SI100 W60` |

A 3×2 factorial around the already-rendered p1 cell, deliberately at the corners rather than
scattered, so a result reads as a **direction** (*"obeying the prompt harder helps"*) rather than as
one lucky take. `sliders` enforces the round type in code: it asserts the Style and Exclude lengths
per cell and **voids any cell where a prompt box moved**, because a round with two variables proves
nothing.

**What this round is for, and it is binary.** If a cell is acceptable → keep rolling, and we now
know which corner to roll in. If none is, but a corner is clearly better → the prompt is close and
should move *toward* that corner. If all twelve are equally not-it → **the prompt is the ceiling**,
and no amount of dice will fix it. That third outcome is the valuable one: it is what stops another
day being spent rolling.

### p1 — 2026-08-27, punk-metal on the consolidated sheet. **Verdict pending.**

The first render after the consolidation, and the first generation in this song's history to read
its cues from **one** file. `Camping Punk-metal fresh (p1)`, 2 takes, `camping-duet`. Lyrics went
in at **70 paragraphs** — variant B, three cues in the disputed run — and the words still matched
`camping.md` §4, which is the point of keeping the two jobs separate.

**What p1 is for:** Kai's taste call (*"the punk version definitely works, and the voice from the
metal works… it's of punk metal"*) rendered against the cue set that should stop the first-verse
stutter. Two questions, and they are separable: **does the verse flow**, and **is punk-metal the
direction**.

🟡 **Variant B was chosen without the A/B being judged.** The `(t1)` pair — `timing A` (5 cues,
delivery restated before every line) and `timing B` (3 cues) — was generated and is still unheard.
B is loaded because the documented evidence points that way (dense cues chop a verse into
micro-sections), **not because it won a listening test.** If A flows better, this section swaps to
the ```lyricsA fence and everything downstream follows.

### g3 — 2026-08-27, the bold rewrite. 10/10 clean, 20 takes. **Verdict pending.**

Ten independent prompts, generated fresh into `camping-duet`, titled `Camping <genre> fresh (g3)`.
Every lane passed the fresh-mode guards: no cover attached, 71 lyric paragraphs matching
`camping.md` §4, no Voice, Duration on Auto, style and exclude lengths asserted per lane. Token
claimed, released, and re-verified over a fresh connection.

**This round tests one thing, and it is not "which genre wins".** g1 and g2 both came back samey
from prompts that shared 78% and then ~55% of their text. g3 shares **10%**, and those characters
are the casting phrase. So the question the ear has to answer first is: **are these finally
different from each other?**

- If yes → the prompt was the bottleneck all along, the method is `bold, not meek`, and the sweep
  can be judged on taste.
- If no → **the prompt was never the bottleneck**, and rewriting it again is the wrong move. The
  next suspects, in order: Style Influence at 75 (too low to override the model's own read of the
  lyrics), Weirdness pinned at 45, and the possibility that a 71-paragraph cue sheet full of
  bracket lines is imposing its own arrangement on every genre regardless of the Style box.

🟡 **The lyric stutter is still in these takes.** The standalone bracket cues at lines 20 and 23 of
this sheet's § Lyrics were left untouched, so all twenty carry the three-in-a-row re-entry Kai
identified. Judging *arrangement* here is fair; judging *flow* is not.

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
written from this sheet's § Lyrics (71 paragraphs) and checked against `camping.md` §4 before
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
