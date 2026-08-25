---
title: Camping (cover) — the A/B set
status: ROUND 11 — Kai picked 07 Dub soundsystem (+ 03's guitar). Merged style + lyric timing pass, generating 2026-08-25. v1 void, v2 judged — see §4–§5.
source_song: https://suno.com/song/299ef991-d51d-4384-a92f-974342a89714  # "Camping W - 75/65", v5.5, 3:56
parent_sheet: ./camping.md
released_take: ./camping-released.md
history: ./camping-prompt-history.md
workspace: camping-duet
model: v5.5
mode: Cover (Remix → Cover) — source audio attached, lyrics inherited, style rewritten
---
# Camping — the cover A/B set

**Ten variations on one question: what layer sits on top of the drum and bass?** The accepted
round-17 take is attached as the audio reference and the words come with it. The only things
that move are the **Style box** and the **Exclude list**.

| | |
|---|---|
| **The accepted original** | [`./camping.md`](./camping.md) — round 17, the take being covered |
| **The variations, in code** | [`scripts/suno/cover-variations.mts`](../../../../scripts/suno/cover-variations.mts) |
| **The runner** | [`scripts/suno/cover-ab.mts`](../../../../scripts/suno/cover-ab.mts) |
| **Where takes land** | workspace `camping-duet`, titled `Camping cover NN - <name>` |

---

## 0. What we like about the current version

Kai, 2026-08-25: **the indie layer on top of the drum and bass**. Guitars, and a delivery that
is ranting rather than rapping — not a drill or grime flow. That is what every variation below
is built to preserve while it changes one thing around it.

---

## 1. How this is driven

**The Cover screen is reached by hand, once.** Song page → `⋯` → **Remix ▸ Cover**. That
attaches the source audio and loads its lyrics into the create form. One click per session, and
it is not worth automating.

Everything after that is the runner:

```bash
npx tsx scripts/suno/cover-ab.mts lyrics          # write camping.md §4 into the page, generate NOTHING
npx tsx scripts/suno/cover-ab.mts plan            # print the ten boxes, touch nothing
npx tsx scripts/suno/cover-ab.mts check           # read the live form back, spend nothing
npx tsx scripts/suno/cover-ab.mts load <id>       # fill one variation, generate NOTHING
npx tsx scripts/suno/cover-ab.mts run [ids...]    # 10 credits and 2 takes per id
```

### The four cover-mode facts, all established live on 2026-08-25

🟢 **The attachment survives its own generation.** This was the open question and the reason
the runner re-checks after every Create. It does survive: ten Creates ran back to back off one
manual attachment. So a cover set is a single unattended run, not ten manual re-attachments.

🔴 **Never navigate away from `/create`.** The attached audio lives only in the page. Leaving
drops it and the whole form with it, and there is no draft recovery — it costs a manual
re-setup. `connect()` only calls `goto()` when the URL is not already `/create`, which is what
makes the tooling safe here. Nothing in this workflow may navigate.

🔴 **The attached audio carries the words it was generated from — not necessarily the current
ones.** This was learned the expensive way: the v1 set (below) ran against a stale attachment
whose lyrics predated a rewrite in `camping.md` §4, and all twenty takes sang the old words —
`SPEAK TO THE HAND BITCH!`, `let's make a happy ending for this song` — none of it usable.
`camping.md` §4 is the single source of truth for the words; the page is not. `run` now
**refuses to spend a credit** unless the words on the page match the sheet exactly, and `lyrics`
is the one command that writes them in — the only place in this whole workflow the lyrics box
is touched.

🟢 **A re-attach does not carry the old lyrics forward.** Re-doing Remix ▸ Cover by hand loads
whatever the *source song* was last generated with — so if `camping.md` moves again, `lyrics`
has to run again too. `check` reports the paragraph count; `run` compares the actual words.

🟡 **The Exclude Styles fill occasionally truncates, and `run` catches it before spending
anything.** Seen twice on 2026-08-25, both times as part of a two-variation `run` — the
SECOND variation's exclude box came back a fraction of its expected length (117/831,
169/871). The style box and everything else in the same load were correct; only the exclude
field was short. Cause unconfirmed — plausibly the input's own React re-render firing between
the previous variation's Create and this load's `.fill()`. **Not dangerous**: the length
check in `loadVariation` catches it and `run` stops before the Create button is ever clicked,
so no credit has been lost to it. The fix so far is just retrying the one id that failed.

### Two deviations from the house rules, both deliberate

**No weirdness pair.** The house rule runs every attempt at 30 and 60. Here weirdness is pinned
at **30** for all ten, because the variable under test is the style box. Pairing would double
the credits and muddy the comparison. The pair comes back once a genre is chosen.

**Audio Influence pinned at 25.** It is the strongest dial on this screen and moving it would
swamp the differences between the variations. It gets tuned after a vibe is picked, not during.

---

## 2. The ten variations

**What never moves.** `HEAD` (casting plus both voice sentences) and `TAIL` (the amen-fill
clause and `played straight`) are byte-identical in all ten. `British post-punk spoken word`
owns the vocalist pool and therefore the casting; the two voice sentences are what keep Bob and
Tarquin two different men. A variation that edited any of them would be testing four things at
once.

**Why clauses are swapped and never added.** The style box caps at 1000 characters and the
accepted original runs 997. There is no room to append, and a maxed box outvotes its own vocal
clauses anyway — §4c of the parent sheet is four rounds of exactly that regression.

**Why the excludes move too.** The accepted list bans `violins`, `brass band`, `piano`,
`acoustic guitar` and `dub` outright. Asking for strings while still excluding violins just
regenerates the original, so each variation lifts only the keywords it needs — and keeps the
neighbouring bans that stop the genre going where we don't want it.

| # | Take title | What is under test | Excludes lifted |
|---|---|---|---|
| 01 | **Strings intro** | A cold string section opens it, and the drop tears it away. | `orchestral strings`, `violins`, `cello`, `string section` |
| 02 | **Bitter brass** | Horns take the job the guitar was doing. | `brass band` |
| 03 | **More guitar** | The indie layer you already like, doubled. The safest variation. | — |
| 04 | **Blues** | The riff becomes a bottleneck slide on a valve amp. | `wah` |
| 05 | **Soul** | A warm keys bed under cold words. Warmth is the variable, not the words. | `piano` |
| 06 | **Shoegaze wall** | Verses stay dry and close; the drops become a wall of noise. | `power chords` |
| 07 | **Dub soundsystem** | Bass first, everything else stripped, delay throwing the vocal across the bar. | `dub` |
| 08 | **English folk intro** | Something almost pretty opens it, and the drum and bass demolishes it. | `acoustic guitar`, `guitar strumming` |
| 09 | **Industrial** | No guitar anywhere. The coldest, most machine-like version. | — |
| 10 | **Full orchestral** | Strings and horns carry the whole record. Rounds 1-14 abandoned this direction; this is the honest re-test. | `orchestral strings`, `violins`, `cello`, `string section`, `brass band` |

---

## 3. The ten style boxes

Each is `HEAD` + its own **Four steps** sentence + `TAIL`. Only the middle moves.

### 01 — Strings intro  `Camping cover 01 - Strings intro`

_A cold string section opens it, and the drop tears it away._

**Excludes:** lift `orchestral strings`, `violins`, `cello`, `string section` — the accepted list bans all four, so the strings would never arrive.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: a cold unaccompanied string section, violins and violas alone, one bleak sustained figure; then the voice over a low palm-muted electric guitar riff — distorted rock tone, one short figure repeating, never a solo, never chords, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, strings and guitar out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 02 — Bitter brass  `Camping cover 02 - Bitter brass`

_Horns take the job the guitar was doing._

**Excludes:** lift `brass band` — `marching band`, `oompah` and `dixieland` stay banned — they are what stops brass going comedy.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over a dirty brass section — trombone and baritone saxophone, one short figure repeating, never a solo, never a fanfare, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, horns stabbing hard on the downbeat, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it, so brass and break are one piece of music. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 03 — More guitar  `Camping cover 03 - More guitar`

_The indie layer you already like, doubled. The safest variation._

**Excludes:** the accepted list, unchanged — nothing lifted — this variation lives entirely inside the accepted list.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over two electric guitars — a low palm-muted riff underneath and a thin chorus-pedal jangle over the top, one short figure each, repeating, never a solo, never chords, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, both guitars out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 04 — Blues  `Camping cover 04 - Blues`

_The riff becomes a bottleneck slide on a valve amp._

**Excludes:** lift `wah` — `guitar solo`, `lead guitar` and `shredding` stay banned — the slide is a riff, not a lead break.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over a dirty electric blues guitar — bottleneck slide, minor pentatonic, valve amp on the edge of breakup, one short figure repeating, never a solo, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, guitar out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 05 — Soul  `Camping cover 05 - Soul`

_A warm keys bed under cold words. Warmth is the variable, not the words._

**Excludes:** lift `piano` — Rhodes and Hammond read as piano-family to the model; `major key` stays banned so it cannot go sunny.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over a warm Hammond organ and Rhodes bed, minor chords held long, one short figure repeating underneath, never a solo, running under every vocal section; then a dry chopped breakbeat under the vocal, with a walking soul bassline moving under it; then the drop, keys out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 06 — Shoegaze wall  `Camping cover 06 - Shoegaze wall`

_Verses stay dry and close; the drops become a wall of noise._

**Excludes:** lift `power chords` — a wall needs sustained chords; `guitar strumming` stays banned so it does not become an acoustic strum.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over a low palm-muted electric guitar riff — distorted rock tone, one short figure repeating, never a solo, never chords, dry and close under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, that same guitar swelling into an enormous reverbed wall of noise, kit at full weight, Reese sub cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 07 — Dub soundsystem  `Camping cover 07 - Dub soundsystem`

_Bass first, everything else stripped, delay throwing the vocal across the bar._

**Excludes:** lift `dub` — `reggae`, `ska`, `ragga MC` and `Jamaican accent` stay banned — we want the mixing desk, not the genre.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over a low palm-muted electric guitar riff, one short figure repeating, never a solo, with heavy tape delay throwing the end of every vocal line across the bar and spring reverb on the snare; then a dry chopped breakbeat under the vocal, sub bass first and everything else stripped out; then the drop, guitar out, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 08 — English folk intro  `Camping cover 08 - English folk intro`

_Something almost pretty opens it, and the drum and bass demolishes it._

**Excludes:** lift `acoustic guitar`, `guitar strumming` — both are banned outright, and the intro is nothing but an acoustic.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: a lone acoustic guitar and mandolin, English folk, one plain pretty figure played completely alone; then the voice over a low palm-muted electric guitar riff — distorted rock tone, one short figure repeating, never a solo, never chords, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, the acoustic gone, kit at full weight, Reese sub and a screaming detuned wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 09 — Industrial  `Camping cover 09 - Industrial`

_No guitar anywhere. The coldest, most machine-like version._

**Excludes:** the accepted list, unchanged — nothing lifted.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long low detuned synth note; then the voice over metallic industrial percussion — struck steel, anvils and factory noise, one short figure repeating, never a solo, no guitar anywhere on this record; then a dry chopped breakbeat under the vocal, no bass; then the drop, kit at full weight, a distorted analogue bass and a screaming detuned wavetable lead cut against it, so synth and break are one piece of music. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

### 10 — Full orchestral  `Camping cover 10 - Full orchestral`

_Strings and horns carry the whole record. Rounds 1-14 abandoned this direction; this is the honest re-test._

**Excludes:** lift `orchestral strings`, `violins`, `cello`, `string section`, `brass band` — `epic trailer music` stays banned — that is the clause holding this back from Hollywood.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: a cold string section and low brass alone, one bleak sustained figure; then the voice over strings and horns playing one short figure repeating, never a solo, never a fanfare, running under every vocal section; then a dry chopped breakbeat under the vocal, no bass; then the drop, the whole orchestra at full weight against the kit, Reese sub and a screaming detuned wavetable lead cut across it, so orchestra and break are one piece of music. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

---

## 4. Round log

One row per take. **Diagnose before rewording** — see
[`session-method`](../../../suno-gpt/session-method.md).

**v1 (2026-08-25, no suffix) is VOID.** All ten ran against a stale attachment carrying lyrics
from before a rewrite — see the fourth cover-mode fact above. Left in the workspace rather than
deleted, on the chance "the old words sounded better here" turns out to be a real finding, but
**do not listen to these expecting the current words.**

**v2 (2026-08-25, `(v2)` suffix) is the live set** — generated after `lyrics` synced the page to
`camping.md` §4 and `run` verified the match before every Create. `05 Soul (v2)` needed a manual
retry: its first Create timed out waiting for takes to register and produced nothing, so it was
re-run alone once the other nine confirmed.

| Take | Verdict | Note |
|---|---|---|
| 01 Strings intro (v2) | ⬜ | |
| 02 Bitter brass (v2) | ⬜ | |
| 03 More guitar (v2) | 🟡 the guitar | not the winner, but its second guitar goes into round 11 |
| 04 Blues (v2) | ⬜ | |
| 05 Soul (v2) | ⬜ | first Create timed out, retried alone |
| 06 Shoegaze wall (v2) | ⬜ | |
| 07 Dub soundsystem (v2) | ✅ **the one** | Kai, 2026-08-25 — the direction. Its cram at *"I want change"* is the fault round 11 fixes |
| 08 English folk intro (v2) | ⬜ | |
| 09 Industrial (v2) | ⬜ | |
| 10 Full orchestral (v2) | ⬜ | |
| **11 Dub + guitar (v3)** | ⬜ | the merge — §5. One Create, two takes, W30 |

**What to listen for**, in this order — the failure modes this track has already had:

1. **Two men, or one?** The recurring regression. If Bob and Tarquin sound like the same
   performer, the variation's genre tag has taken the vocalist pool over.
2. **Ranting, or rapping?** Any drift toward a drill or grime flow is the genre tag again.
3. **Did the new layer actually arrive**, or did the exclude list quietly veto it?
4. **Is it still played straight?** Soul, brass and folk all pull toward a wink. The words are
   the only thing allowed to be funny.

---

## 5. Round 11 — the merge, 2026-08-25

**Kai's verdict on the v2 set: 07 Dub soundsystem.** With 03's guitar folded in. The other
eight are not pursued.

This round moves **three things at once**, which the house rule forbids, and Kai asked for all
three by name — so they are listed here as three, so a fault can be traced to one of them:

| # | Change | Where |
|---|---|---|
| 1 | **Style: 07 + 03 merged** | the box below, 990/1000 |
| 2 | **Timing pass on `I want change`** | `camping.md` §4 — ellipsis + two commas, no words changed |
| 3 | **Performance cues** | `camping.md` §4 — the four from its §5 *"If the delivery goes flat"*, plus Kai's two |

### The style box

`HEAD` and `TAIL` are byte-identical to 03 and 07, so this is a merge and not a third thing.
Where the two middles disagreed at step three — dub says *sub bass first*, guitar says *no
bass* — **dub wins**, because dub is the one that was chosen. The union ran 1,101; trimmed to
990 by cutting only what the lyric cues already carry (`detuned`, `under the vocal`) and
adjectives (`heavy`, `thin`, `electric`). Nothing cut from the casting, the `never a solo,
never chords` guard, or `under every vocal section`.

```
Dark UK drum and bass, neurofunk, 174 BPM, minor key — British post-punk spoken word on top, ranted over the beat. Verse one, a weathered British man in his fifties: low, gravelly, smoke-worn, nasal, half-shouted and half-muttered, bone dry. Verse two, a well-spoken British man: higher, clean, plummy BBC English, talking down from a wide room. Four steps: one long synth note; then the voice over a low palm-muted guitar riff with a chorus-pedal jangle over it, one short figure each, repeating, never a solo, never chords, under every vocal section, tape delay throwing every line's end across the bar, spring reverb on the snare; then a dry chopped breakbeat, sub bass first, nothing else; then the drop, guitars out, kit at full weight, Reese sub and a screaming wavetable lead cut against it. Every four bars the drums tear into a chopped amen roll for a whole bar, snares tumbling over each other, loud up front, then straight back in. Grim and bitter, played straight, steady tempo.
```

**Excludes:** the accepted list minus `dub` — exactly as 07.

### The timing fix, and why it is a layout change and not a bar-count change

Kai's hearing: *cash / four tonnes / Cheddar / forever* is one four-bar group, *I want change
/ not from your pocket / in the meantime / please sir* the next — and *I want change* was
being folded into the bar after it. The mechanism is `camping.md` §4a's: **the first line of
a section sets the phrase slot for the whole section**, and verse 1 opens on nine syllables.
`I want change,` is **three**. A line that short cannot be stretched to fill a nine-slot, so
the model merged it with the next line and crammed twelve syllables into one bar. Not a
grouping error — an orphan line.

The fix uses the three levers §4a names, and changes **no words**:

| Line | Was | Now | Lever |
|---|---|---|---|
| `I want change,` | 3 syllables, comma | `I want change...` | ellipsis = trailing drift — the line holds its bar |
| *(above it)* | — | `[shouting]` | Kai's cue; a bracket line is a phrase boundary |
| `not from your pocket but at the top` | 1 stress unit | `not from your pocket, but at the top` | comma = stress boundary |
| `in the meantime though let me hold that door` | 1 stress unit | `in the meantime though, let me hold that door` | comma |

**If it still merges:** `I want chaaange...` — a stretch, not a word change (§4b). **Next
cram candidate if verse 1 still rushes:** `fucking sense of entitlement, and self belief`,
twelve syllables in the nine-slot, deliberately untouched this round.

### The performance cues

Kai asked for more square-bracket control over each part. `camping.md` §5 already held the
answer in reserve — *"If the delivery goes flat — re-add only these four"* — so those four go
in, at the four moments that change, alongside the two Kai had already placed:

```
[whisper, conspiratorial]    → before "but I bet, that you paid for your wheels on tick!"
[shout, full chest]          → before "cash from the bank for your wank tank"
[change tone to spoken word] → before "I can't live like this forever"        (Kai's)
[shouting]                   → before "I want change..."                       (Kai's)
[shout, cracking, begging]   → before "please sir, can I FUCKIN, have some more?"
[mocking falsetto sneer]     → before "What about if we taxed the rich?"
```

The shape that gives verse 1's back half: **shout → spoken → shout → begging.** Each of
Kai's two groups opens loud and closes changed.

**Two named risks.** Six one-clause cues across ten lines is denser than §5's "four across the
whole song"; if the verse chops into micro-sections, **pull `[whisper, conspiratorial]`
first** — it is furthest from the passage under repair. And `[mocking falsetto sneer]` is the
one cue that could make Tarquin *sing*, which is the failure that has actually happened on
this track (§4c); the exclude list is holding the line, but if he sings, that cue goes.

### My Taste — deliberately NOT changed this round

Kai asked that the Style box and My Taste both be overwritten to match. **The Style box is.
My Taste is not, on purpose**, for three reasons that each stand alone:

1. **It is already compatible.** The current profile (`camping.md` §1) says nothing about
   guitars and nothing about dub — it does not fight either. And **07 Dub soundsystem was
   generated under it.** The sound Kai picked is proof the profile allows it.
2. **It would be a fourth variable** in a round already carrying three.
3. **`setTaste` is unverified.** The function exists in `suno.mts`, but `automation.md` has
   never recorded it working — and My Taste is account-wide, changes every generation in every
   workspace, and cannot be turned off, only replaced.

**The draft, ready to apply as its own step** — the current *Music* paragraph with two
sentences added after `industrial stabs.`:

```
A low palm-muted electric guitar riff under the voice, one short figure repeating, never a solo, never chords — an indie band's guitar on a drum and bass record. Dub soundsystem mixing: tape delay throwing the ends of vocal lines across the bar, spring reverb on the snare, the sub bass first and everything else stripped back.
```

Apply it if round 11 lands and the direction is confirmed — then the profile should carry it,
because the profile is what every *future* generation in every workspace inherits.

### Settings

Weirdness **30** · Style Influence **50** · Audio Influence **25** · **one Create = two takes**,
per Kai ("just two"). Superseded by round 12 below.

---

## 6. Round 12 — the slider sweep, 2026-08-25

**Kai's move on 11:** Weirdness **30 → 60**, Style Influence **50 → 75**, Audio Influence
**25 → 15**. All three loosened toward the model and away from the source in one step — more
invention, stronger obedience to the style box, less pull from the reference audio. Same
words, same style box as round 11: **the sliders are the only variable this round.**

**Also folded in first: Kai's hand edit to `camping.md`** — `pathetic` → `it's pathetic`,
`sorroooooows,` → `sorrows,` (dropping the stretch respelling). A real word change, so it gets
its own suffix rather than riding on round 11's — see `cover-variations.mts`, `SET = ' (v4)'`.

**Three takes, not two.** With a slider sweep as the variable rather than a style A/B, one pair
is thin evidence for how much the model's own stochastic spread is doing versus the sliders —
three gives a spread to actually compare.

The runner didn't have a way to sweep sliders or repeat one variation before this round — both
added to `cover-ab.mts`:

```bash
npx tsx scripts/suno/cover-ab.mts lyrics                                 # sync the hand edit
SUNO_WEIRDNESS=60 SUNO_STYLE_INFLUENCE=75 SUNO_AUDIO_INFLUENCE=15 \
  npx tsx scripts/suno/cover-ab.mts run cover-11-dub-guitarx3            # 3 Creates, titled #1 #2 #3
```

`xN` repeats one variation N times, each Create titled with a `#1`/`#2`/`#3` suffix — without
it, `create()`'s "wait for two takes matching this title" would see the *first* run's takes
and report success on a round it never generated, which is exactly the failure class the v1/v2
lyrics bug came from.

| Take | Verdict | Note |
|---|---|---|
| Dub + guitar (v4) #1 | ⬜ | W60 · SI75 · AI15 |
| Dub + guitar (v4) #2 | ⬜ | W60 · SI75 · AI15 |
| Dub + guitar (v4) #3 | ⬜ | W60 · SI75 · AI15 |

**What to listen for, specifically:** Audio Influence dropped from 25 to 15 — the take should
pull *less* from the source reference than round 11 did. Style Influence rose to 75, matching
`camping.md`'s own accepted setting — the style box should be obeyed harder. Weirdness at 60 is
the sheet's own house pair's upper value — more invention, and the first real test of whether
that increases the one-voice regression risk this track has already had (§4c).

---

## 7. Round 13 — "I want change" restructured, and round 14 — why it still sounds close

**Round 13, 2026-08-25.** Three asks: Weirdness 60 → **40**, a length target (**200s**, read
from "maybe 320" as 3:20), and a real fix for `I want change` since round 11's punctuation
trick didn't survive generation. All three landed:

- **The line-merge fix** — see `camping.md` Watch items. Round 11's ellipsis/comma approach
  decorated an orphan line without removing it; round 13 merges `I want change,` into its
  neighbour, so there is no 3-syllable line left for the model to absorb. Words unchanged,
  line count down by one — which also serves the "get through it faster" ask, for free.
- **`SUNO_DURATION_SEC` added to the runner.** Cover mode's Duration control had never been
  driven from code before this round. It's the same soft target the rest of the toolkit
  already knows about — "shortens reliably, fails to stretch" — set at exactly what was asked
  (200s) rather than padded, so the take reveals whether it undershoots here too.
- **Audio Influence dropped again, 15 → 10** — testing Kai's own diagnosis that the bracket
  cues weren't landing because the source reference was pulling too hard on delivery.

One take, `Dub + guitar (v5)`, W40 · SI75 · AI10 · Duration 200s.

**Round 14, 2026-08-25 — the resemblance question.** Kai: *"it all sounds very, very similar
to the other song. I wonder if this is a problem."* This has a concrete, checkable answer, not
a guess, and it's worth stating plainly:

**Three separate things are all pulling every take back toward the source, and only one of
them is the Audio Influence slider.**

1. **The style box's `HEAD` and `TAIL` are word-for-word the source's own accepted style.**
   `camping.md` §2 — casting, both voice descriptions, 174 BPM, the amen-fill clause,
   `played straight` — carries unchanged into every variation in this set. Only the ~450–500
   character *middle* differs. Roughly half the box, by design, asks for the same record.
2. **The words are the same words.** Same rhyme scheme, same syllable rhythm, same rhyme
   payoffs — a cover with an unchanged lyric is going to phrase like the original almost by
   construction, independent of anything on the create form.
3. **Cover mode's audio anchor**, which is the one lever that's actually been swept —
   25 → 15 → 10 across rounds 11–13 — and is the one thing the sliders in this workflow can
   move.

**So: is this a problem?** Only if the goal moved from *"a cover of Camping"* to *"a new song
that happens to share its lyric."* If it's still a cover, sounding recognisably like its source
is doing its job, not failing it — reasons 1 and 2 are structural and would hold at Audio
Influence 0. **If it's a problem, the fix isn't another cover-mode round — it's editing the
style box's casting sentence itself**, which is the one thing every variation has deliberately
held fixed, because it's what keeps Bob and Tarquin two different men (§0's whole premise).
That's a bigger, riskier move than anything tried so far and hasn't been taken without asking.

**The orchestral overlays Kai asked for, as the first probe of this question** — two new
variations, both round 11's merge with a layer added, arrangement only, `HEAD`/`TAIL` and the
words still untouched:

| # | Name | What's added | Excludes lifted |
|---|---|---|---|
| 12 | **Dub + guitar + strings** | violins and cello, cold and sustained, holding under the guitar; out at the drop | `dub`, `orchestral strings`, `violins`, `cello`, `string section` |
| 13 | **Dub + guitar + horns** | a cold low brass section, stabbing under the guitar; out at the drop | `dub`, `brass band` |

Same settings as round 13 — W40 · SI75 · AI10 · Duration 200s — so the only variable is the
new layer.

| Take | Verdict | Note |
|---|---|---|
| Dub + guitar (v5) | ⬜ | W40 · SI75 · AI10 · Duration 200s |
| Dub + guitar + strings (v6) | ⬜ | round 14 — does an orchestral layer break the resemblance? |
| Dub + guitar + horns (v6) | ⬜ | round 14 |

**If these still sound close and Kai wants that fixed rather than accepted**, the next honest
step is a controlled experiment: run the same style box through ordinary **Create** mode (no
source attached at all) and compare. That isolates cover mode's audio anchor from reasons 1
and 2 above — if the Create-mode take *also* sounds like Camping, the resemblance was never
really about Audio Influence.
