---
title: Camping (cover) — the A/B set
status: RUNNING — ten style variations through Suno Cover mode, 2026-08-25. Weirdness pinned at 30.
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
npx tsx scripts/suno/cover-ab.mts plan            # print the ten boxes, touch nothing
npx tsx scripts/suno/cover-ab.mts check           # read the live form back, spend nothing
npx tsx scripts/suno/cover-ab.mts load <id>       # fill one variation, generate NOTHING
npx tsx scripts/suno/cover-ab.mts run [ids...]    # 10 credits and 2 takes per id
```

### The three cover-mode facts, all established live on 2026-08-25

🟢 **The attachment survives its own generation.** This was the open question and the reason
the runner re-checks after every Create. It does survive: ten Creates ran back to back off one
manual attachment. So a cover set is a single unattended run, not ten manual re-attachments.

🔴 **Never navigate away from `/create`.** The attached audio lives only in the page. Leaving
drops it and the whole form with it, and there is no draft recovery — it costs a manual
re-setup. `connect()` only calls `goto()` when the URL is not already `/create`, which is what
makes the tooling safe here. Nothing in this workflow may navigate.

🔴 **The lyrics come with the source and are never written.** As of 2026-08-25 the words in the
page are **ahead of `camping.md` §4** — twelve blocks differ, including `SPEAK TO THE HAND
BITCH!`, `let's make a happy ending for this song` and `and it might go wrong`. Writing the
sheet's lyrics in would silently downgrade the track to an older cut. The runner asserts the
paragraph count is unchanged before every Create and aborts if it moved. **The sheet still owes
a sync.**

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

| Take | Verdict | Note |
|---|---|---|
| 01 Strings intro | ⬜ | |
| 02 Bitter brass | ⬜ | |
| 03 More guitar | ⬜ | |
| 04 Blues | ⬜ | |
| 05 Soul | ⬜ | |
| 06 Shoegaze wall | ⬜ | |
| 07 Dub soundsystem | ⬜ | |
| 08 English folk intro | ⬜ | |
| 09 Industrial | ⬜ | |
| 10 Full orchestral | ⬜ | |

**What to listen for**, in this order — the failure modes this track has already had:

1. **Two men, or one?** The recurring regression. If Bob and Tarquin sound like the same
   performer, the variation's genre tag has taken the vocalist pool over.
2. **Ranting, or rapping?** Any drift toward a drill or grime flow is the genre tag again.
3. **Did the new layer actually arrive**, or did the exclude list quietly veto it?
4. **Is it still played straight?** Soul, brass and folk all pull toward a wink. The words are
   the only thing allowed to be funny.
