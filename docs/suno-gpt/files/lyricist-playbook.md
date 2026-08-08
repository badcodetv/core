# The Lyricist's Playbook

The songwriter-side companion to the rest of this knowledge base. What you type in the **Lyrics
box**, how it gets performed, and how to fix it when it isn't.

> **Why this file exists.** The rest of `docs/suno-gpt/` was distilled from a working *producer*
> (see [`../README.md`](../README.md)) and is strong on sliders, models, Studio, stems and mixing.
> It is thin on everything a lyricist controls. That gap was found the hard way on 2026-08-08: the
> single most useful discovery of a day's work on the GPOM chorus — that delivery speed is syllable
> density per line, and that commas insert beats of silence — appears nowhere in 184 transcripts.
> This file is the result of an 11-agent web sweep scoped deliberately to the lyricist's side.

## Read this before trusting anything below

**Of 81 findings gathered, exactly zero were gradeable as *tested*.** Every one was an assertion:
stated as fact, with no A/B, no methodology, no sample size. That is not a sampling accident — the
songwriter-facing Suno web is overwhelmingly SEO content marketing for prompt-generator products,
and it copies from itself.

Consequences, and they are load-bearing:

- **This file is weaker evidence than the producer corpus**, where the source demonstrably tested
  claims on camera. Where the two disagree, the producer corpus wins.
- **Where something here contradicts a *tested* finding, the tested finding stands.** Two sources
  here assert ALL CAPS reliably increases intensity. It failed a direct A/B test elsewhere. It stays
  on the known-unreliable list.
- **Treat everything as a hypothesis with a cheap test attached.** Most of these cost one generation
  to check.
- Ranges quoted as precise (`6–12 syllables`, `90% / 70% / 50% bracket compliance`) are folk
  numbers. Use them as directional, never as thresholds.

---

## 1. Delivery speed and timing

The core mechanism and the punctuation table live in
[`lyric-craft.md`](./lyric-craft.md) → *"Punctuation is the brake"*. This section is the
refinements the sweep added.

**The first line of a section sets the bar length for the whole section.** Suno derives its
rhythmic template from the syllable pattern of the opening line(s), then force-fits every later
line into that same slot. A section going 8 syllables → 14 syllables doesn't smoothly speed up; it
*crams*, and cramming sounds glitchy and robotic rather than fast. So **match syllable counts across
parallel lines**, especially in a repeated chorus, and put the line whose rhythm you want as the
template first.

**The safe band is ~6–12 syllables per line; past ~15 the model compresses, smears consonants and
mumbles.** For drum & bass and anything at 170+ BPM the ceiling is *lower*, because there is less
time per bar — sources warn that long lines at those tempos get rushed, mumbled, or cut off
entirely. Dense rap bars deliberately run 12–16.

> **The unresolved tension.** Density is the only reliable accelerator, but the safe band is slow
> and exceeding it risks mumbling. There is no source that resolves this. In practice: strip
> punctuation first (free speed, no risk), then push density, and treat anything past ~15 syllables
> at 170+ BPM as a deliberate gamble with mumbling as the fail state.

**Two different "faster" levers appear across sources and nobody reconciles them:** per-line
syllable density (a smooth, proportional speed-up) versus *overloading the whole section* with more
bars than fit, which one source says triggers a global "double-time machine-gun" fallback. Unclear
whether these are one mechanism at two scales.

**Short lines are not fast.** This cuts against intuition and is worth stating plainly: sources
consistently recommend short lines (4–6 words, one breath) for *slower, clearer* delivery, and warn
that too-short lines produce awkward pauses rather than a tight read.

**Write the stressed syllable onto the strong beat.** Suno places vocal stress on the downbeat; when
natural word stress fights that, the model rushes, mumbles or shifts syllables to force alignment.
Mismatched stress reads as "rushed" even at a safe syllable count.

**Internal rhyme is a rhythmic device, not just a poetic one.** For patter/rapid delivery, short
punchy words with internal rhyme and alliteration act as a "vocal drum kit" that snaps syllables to
the grid, letting Suno articulate one-syllable-per-note cleanly instead of slurring. Prefer this to
simply raising the syllable count.

**Avoid stacked consonant-cluster onsets** (`str-`, `scr-`, `spl-`, `thr-`) back to back at high
density — the articulation model blurs them. Space them with vowel-heavy words.

## 2. Section tags

**The reliable backbone** — these have the most precedent in tagged-lyric training data:

```
[Intro] [Verse] [Pre-Chorus] [Chorus] [Post-Chorus] [Hook] [Bridge]
[Instrumental Break] [Guitar Solo] [Outro]
```

**Invented tags are not reliably obeyed.** The model pattern-matches bracket text against training
data; an unfamiliar label has no prior and it falls back to inferring the section's role from the
lyric content. One source puts the reliable vocabulary at roughly 200 tags.

**The label changes the musical character, not just the structure** — the single most useful claim
in this section:

| Tag | What it summons |
|---|---|
| `[Chorus]` | A **sung, melodic**, repeating hook section |
| `[Drop]` | A **rhythmic/bass energy-release** moment — electronic convention |
| `[Chant]` | A **rhythmic, monotonic, group-delivered, near-spoken** vocal with percussive timing |
| `[Post-Chorus]` | Extends a hook into a **chanted / response / motif** section |
| `[Call and Response]` | Leader/crowd back-and-forth |
| `[Rapped Verse]` | Pushes a section toward spoken-rap cadence |

The existence of `[Post-Chorus]` and `[Chant]` as separate conventions is itself the evidence that
**plain `[Chorus]` defaults to sung melody.** If you want a chant, stop labelling it a chorus.

*Caveat:* one source argues the opposite — that a chorus reads as a chorus because it's *written*
with chorus-like prosody and repetition, not because of the bracket. Both are asserted. The safe
reading is that tag and content should agree, and neither alone is decisive.

**Bar counts work as duration control:**

```
[Intro - 8 bars]      [Outro: 8 bars]      [Drop - 16 bars]
```

**Form is authored by tag placement.** Each occurrence of `[Chorus]` is a fresh instruction to play
that section; repeat the tag wherever you want it. Vary the final one (`[Double Chorus]`,
`[Final Chorus: full stack]`) to lift energy.

**Always close with an explicit `[Outro]`** carrying a bar count or a closing line. One source
attributes "90% of abrupt cutoffs" to a missing or misplaced ending tag. (A second blames lyric
density exceeding the time budget; neither acknowledges the other.)

**Suno gives disproportionate melodic weight to the first line under a section tag.** Put the
strongest line there, never buried at line three.

**Stacking tags on one line** — `[Verse 1] [Female Vocal] [Soft]` — is reported to improve
compliance over one-per-line. Soft pattern, not guaranteed syntax.

## 3. Directing the performance

**Square brackets on their own line, never sharing a line with lyrics.** A bracket that shares a
line with words risks being *sung out loud*. The rule of thumb across sources: **if it is a
direction, square brackets; if it should be heard, parentheses.**

**Cues are line-scoped, not section-scoped.** They apply to the nearest following text rather than
persisting. Put the cue immediately before the line you want changed; only a cue alone before a
whole block extends across it.

**Quotation marks scope a spoken/whispered quality to one phrase** without the section-wide shift a
`[Spoken Word]` tag causes.

**Don't stack more than 3–4 cues in close proximity.** Dense tagging is reported to confuse the
model and produce inconsistent results; a tag on every line is counterproductive.

> ⚠️ **This contradicts BadCode house practice.** Our tracks use very long multi-clause bracket cues
> (six to eight directions in one header). Those cues have produced takes we liked, so this is not a
> reason to rewrite them — but if a heavily-cued section keeps ignoring its own directions,
> *cue overload is now a named suspect*, and the test is to cut the header to its three most
> important clauses and re-roll.

**When a cue is ignored, simplify rather than escalate.** Sources here recommend a shorter, plainer,
more conventional tag plus a re-roll — not a longer or more emphatic one. *Note this sits in tension
with our own escalation ladder (`[spoken word]` → `[spoken word speech]` → `[spoken word speech
talking]`), which came from the producer corpus. Both are asserted; try simplifying first since it's
cheaper.*

**Getting speech instead of singing is unreliable and probabilistic.** No guaranteed narration
grammar exists. Rhyming lines, chorus/refrain labels, melodic style words and busy arrangement all
pull back toward singing even with a spoken tag present. To maximise the odds: `[Spoken narration]`
/ `[Monologue]`, a *minimal* style box, short non-rhyming conversational sentences.

## 4. Casting more than one voice

**Label every line, not just the section.** `[Female]` / `[Male]` / `[Both]` at the start of each
line. (Tag format is disputed — some sources use bare `[Female]`, others `[Female Vocal]`. Nobody
tested which parses better.)

**Duets are described by one source as "more of an exploit, definitely not a feature."** Voices swap
which line they take, or render too similar to tell apart, especially over longer sections. Other
sources present duets as straightforward — that confidence gap is unresolved, and the pessimistic
source is the more specific one.

**Call-and-response works best asymmetric and short:** the lead sings full lines, the responder
answers in 3–6 words, and the two overlap only once, on a shared hook line.

**Short parenthesised ad-libs (1–3 words) are the reliable way to add extra voices as texture** —
more reliable than writing full parallel lines for a second voice.

**To keep a lead vocal alone in a section**, three layers at once: name a single lead in the Style
box; write the restriction *inside the section tag* in the lyrics box; and list the unwanted vocal
types in Exclude. The reason all three are needed is that **Suno infers group vocals from context
words** — `anthemic`, `festival`, `arena`, `singalong`, `gospel` — even when no choir was requested.
The source is explicit that this only *improves the odds* and guarantees nothing.

## 5. The typographic vocabulary

| Symbol | Reported effect |
|---|---|
| `word~` | Sustains the note **with vibrato** |
| `word............` | Sustains **longer than a tilde** — more dots, longer hold |
| `fa-a-a-alling` | Melisma — stretches a vowel across notes. Cap at 3–5 |
| `I-I-I can't` | Stutter on the word |
| `G-A-L-A-X-Y` | Spells the word out **letter by letter** |
| `"phrase"` | Spoken/whispered quality, scoped to the phrase |
| `Line!` / `NO!!!` | More emphasis; repeated marks push toward a barked shout |
| `Ha ha ha` | Laughing-while-singing (written in the lyric, not as a tag) |
| `I... I miss you` | Hesitation/stutter/near-sob, not just a pause |
| `Co... lle... ct... ions` | Staccato, percussive, hard-landing delivery on one word |
| `{braces}` | Emphasis/repetition — **least reliable bracket type** |

**Reported bracket compliance: square ~90%, parentheses ~70%, curly ~50%.** Folk numbers, but the
ordering is consistent across sources.

**Avoid `&`, `@`, `#` and emoji** — reported to break parsing.

**Asterisk sound effects (`*sniff*`, `*gunshots*`) are disputed** — two sources give working
examples, another says they're undocumented and inconsistent. Treat as experimental.

## 6. Pronunciation, numbers and the content filter

**Respell phonetically for the sound you want, not the correct spelling.** Suno sounds words out
from spelling patterns; it has no dictionary and no IPA.

```
through→thru   knight→nite   colonel→kernel   enough→enuff   because→becuz
read (past)→red    live (performance)→laiv    lead (metal)→led
AI→A-I    DJ→dee-jay    USA→U-S-A
Saoirse→SEER-sha    Siobhan→Shi-vawn
```

**Keep the respelling identical everywhere the word recurs** — inconsistent spelling reintroduces
the error. And don't preemptively respell words that haven't actually failed.

**Spell numerals out as words:** `24/7` → *twenty four seven*, `2024` → *twenty twenty-four*,
`100` → *a hundred*.

> **One sharp exception.** Suno's tag filter **strips spaces and hyphens before matching**, so
> `ninety-three` collapses to `ninetythree` and can collide with a producer-tag alias, injecting an
> unwanted artifact. For years and decades specifically, digits (`'93`) may be safer than words.
> The two pieces of advice point opposite ways; the collision risk is only for number-words that
> resemble known producer aliases.

**The content filter is a black box and non-deterministic.** The same lyric sometimes passes on a
retry, so **retry once before rewriting**. To localise a block, **bisect** the lyric (delete half,
test, repeat). Because the filter strips spaces and hyphens before matching, **re-punctuating a
blocked phrase does not help** — `low light`, `low-light` and `lowlight` all trigger identically.
Only a genuinely different word choice works.

**Profanity** may be filtered or mangled. Reported workarounds: near-homophone respelling
(`fuck`→`fuhk`/`phuck`, `shit`→`sh*t`), and dropping direct second-person address
(`I hope you choke` → `Hope you choke`), which is guessed to reduce flagging. All speculative — if
your profanity is already rendering intact, leave it alone.

## 7. Hooks and choruses

**Duplicate the hook line literally; `(x2)` notation is not parsed.** Suno sings what is present.

**Keep the hook to 2–4 short lines.** One source claims the four-line ceiling is repeatedly tested
("anything over four lines loses melodic focus"), though shows no data. Long choruses repeat badly
across instances and come back robotic.

**Escalate repeats through the tag, not the words.** Keep the lyric identical and change the
bracket's production descriptors each time:

```
[Chorus: light, single voice]
[Chorus: added harmonies, fuller]
[Final Chorus: full vocal stack, soaring]
```

**For a terrace/anthem chant, cap the chantable line at four words or fewer** — the
"three-second learnability" heuristic for whether a crowd could shout it back. Build the rest of the
song around that short repeatable core in a leader-line / crowd-answer shape.

**Name group vocals explicitly on the chorus if you want a stadium lift** — Suno keeps verses
vocally lean by default and will not add stacking unless the section implies group energy.

## 8. Failure modes and fixes

| Symptom | First fix |
|---|---|
| Lines rushed, consonants smeared | Cap syllables per line; split overloaded lines |
| Lines dragging | Remove punctuation; raise density |
| Tag sung out loud as a lyric | Move the bracket onto its own line |
| Words mispronounced | Phonetic respelling, consistent across every recurrence |
| Extension garbles / hallucinates words | Prime the extend prompt with the next expected words, or repeat the last sung line as a lead-in — the model "lost its place" |
| Song ends before the lyrics do | Explicit `[Outro]` + closing lines; and check lyric density against the time budget |
| A section repeats unbidden | Replace Section with an explicit "do not repeat the previous chorus" |
| Innocuous lyric blocked | Retry once; then bisect to find the line; then change the *word*, not the punctuation |

**Test density before writing a full sheet.** Generate one verse + chorus (~60 words) alone. A clean
50–60s clip means full-song pacing is fine; ~30s means the lyrics are too dense and the song will
truncate. Generous instrumental tags (`[guitar solo: 16 bars]`) eat the same budget.

## 9. Fixing timing after generation — Studio 1.2

The escape hatch when prompting can't get the delivery on the grid. **Confirmed as of Studio 1.2:**

- **Warp Markers** — click a clip's waveform to drop a marker (or auto-place at every transient),
  then drag to move that point in time. Time-stretches without changing pitch. Suno's own wording is
  "with surgical precision."
- **Quantize** — after placing warp markers, snap the marked points to the tempo grid. This is the
  direct answer to a loose, off-grid vocal take.
- Both apply to **any audio clip**, not vocals specifically.
- **Clip Settings → `On Beat` vs `Original Tempo`** is the coarser, non-destructive alternative:
  locks a whole clip's tempo to the project grid. (Same control the layered-cover method depends
  on — [`suno-controls-and-workflows.md`](./suno-controls-and-workflows.md) §4a.)
- **Manual region fix:** split at the drift point, nudge the piece, then **Heal Edits** to smooth
  the seam. Heal Edits blends the timbral transition; it does not regenerate.

**Replace Section** regenerates one region's lyrics without touching the rest: highlight the region
→ Edit Lyrics → Replace Lyrics → *Replace Section*. Voice and melody character reportedly survive.
**Do not surgically edit one or two words** — that forces new phonemes into a fixed slot and glitches.
Regenerate the whole line, keeping the syllable count close to the original.

*Documentation conflict:* Suno's own "Editing in Studio" article lists none of Warp/Quantize/Split,
while the Studio 1.2 announcement and third-party guides describe them as core. Most likely the
older article simply predates 1.2 — but "split" and "nudge" as literal button names appear only in
third-party paraphrase, never in a primary source.

## 10. Open contradictions

Recorded so they aren't silently resolved by whoever reads this next:

1. **Brackets vs parentheses for inline cues** — one source says short square-bracket tags are fine
   inline; another warns Suno may sing bracket text and recommends parentheses near lyric lines.
2. **Tag choice vs lyric content** as the driver of section character — sources disagree on which
   dominates.
3. **Escalate or simplify an ignored cue** — this file's sources say simplify; the producer corpus
   says escalate with redundant synonyms.
4. **Numbers as words vs digits** — general advice says spell out; the producer-tag collision case
   says digits, for years/decades.
5. **Cause of premature song endings** — missing outro tag vs lyric density over time budget.
6. **Duet reliability** — "an exploit, not a feature" vs presented as routine.
7. **Two "faster delivery" mechanisms** — per-line density vs whole-section overload triggering a
   double-time fallback.

## Provenance

11-agent web sweep, 2026-08-08, scoped to the lyricist's side (territories: punctuation timing,
syllable density, typography, section tags, vocal direction, multi-voice casting, pronunciation,
hooks, failure modes, genre lyric craft, post-generation fixes). 81 findings, **none gradeable as
tested**. Principal sources: songsmith.studio, hookgenius.app, acetaggen.com, jackrighteous.com,
tagasong.com, howtopromptsuno.com, usesuno.com, sunoarchitect.com, suno.wiki, kordra.io, plus
Suno's own help articles for the Studio section.
