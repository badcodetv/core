# Suno toolkit

The knowledge base behind the **`suno-prompt`** skill (`.claude/skills/suno-prompt/`). The skill is
the entry point — this is what it reads.

## Files

| File | What |
|---|---|
| [`system-prompt.txt`](./system-prompt.txt) | Base operating procedure — mode detection, output format, character limits, famous-artist translation, edge cases |
| [`files/suno-tag-mechanics.md`](./files/suno-tag-mechanics.md) | The prompt language: hybrid format, information ordering, genre pairing, bracket language, exclude strategy, contamination words |
| [`files/suno-controls-and-workflows.md`](./files/suno-controls-and-workflows.md) | **The control surface and the platform.** Sliders, model choice, the consistency stack (Voice / custom model / Lyricist), lyric editing, Studio generation craft, stems, known failure modes |
| [`files/suno-studio.md`](./files/suno-studio.md) | **The Studio 2.0 app surface** — project-aware chat, MIDI + musical typing, live recording, cover-in-place, advanced split / remove effects, the effects rack + sidechain + automation, natural-language custom plugins, shortcuts. **Vendor-demo confidence — read its warning** |
| [`files/producer-vocabulary.md`](./files/producer-vocabulary.md) | Words for describing sound, by domain; song structure; how to judge a generation |
| [`files/lyric-craft.md`](./files/lyric-craft.md) | Syllable counts, rhyme schemes, section shapes, engineered transitions — **and the punctuation/timing table: how Suno times what you wrote** |
| [`files/lyricist-playbook.md`](./files/lyricist-playbook.md) | **The songwriter's side**: section-tag character ([Chorus] vs [Drop] vs [Chant]), performance cues, multi-voice casting, typography, pronunciation, the content filter, hooks, lyric failure modes, Studio 1.2 warp/quantize. **Weaker evidence than the rest of this base — read its confidence warning first** |
| [`suno-voices.md`](./suno-voices.md) | **Getting a specific character's voice, on purpose** — the evidence base behind the skill's "Getting a specific voice" and "Two characters in one song". Four threads: the genre-pool discovery + Voice-transplant ladder (Karen), My Taste forensics, the two-voice problem (GPOM), and the Camping duet. **Contains most of what we have actually tested ourselves** |
| [`files/meta-tag-dictionary.md`](./files/meta-tag-dictionary.md) | Specialty `[ ]` tags. **Largely unverified — see caveat below** |
| [`files/overused-words.md`](./files/overused-words.md), [`files/ai-cliches.md`](./files/ai-cliches.md) | Red-flag lists for lyrics only, never style prompts |

## Provenance

The original `system-prompt.txt` + the first five `files/` came from a Suno-prompting GPT.

`suno-controls-and-workflows.md`, `producer-vocabulary.md`, and the corrections marked **Field note**
in `suno-tag-mechanics.md` were added on **2026-07-29** from a research pass over the
[ChillPanic](https://www.youtube.com/channel/UCj83I0PrbdTDmoUXBosTyXg) YouTube channel — a working
producer who has used Suno since 2023 and tests claims on camera. 443 videos were enumerated, 186
filtered as Suno/AI-music instructional, and **184 transcripts** harvested and distilled by seven
parallel research agents.

Reproduce the harvest with:

```bash
scripts/fetch-youtube-transcripts.sh \
  -c https://www.youtube.com/channel/UCj83I0PrbdTDmoUXBosTyXg/videos \
  -o /tmp/suno-research \
  -f 'suno|udio|ai music|ai song|prompt|stems|lyria' \
  -x 'official (lyric|music|visualizer|audio)|\(Official'
```

Raw transcripts are research input and are deliberately **not committed** — the distilled guidance
here is the artifact.

**Post-harvest additions** (the channel keeps publishing; the harvest is a snapshot):

| Added | Source | Landed in |
|---|---|---|
| 2026-08-08 | ChillPanic, *"Finally! Use TWO VOICES in ONE SUNO AI SONG"* (published 2026-08-04) | `files/suno-controls-and-workflows.md` §4a — the layered-cover method |
| 2026-08-08 | 11-agent web sweep, songwriter-side sources (non-ChillPanic) | `files/lyricist-playbook.md` (new) + `files/lyric-craft.md` timing table |
| 2026-08-14 | Suno Music official, *"Introducing Suno Studio 2.0"* (published 2026-08-13) | `files/suno-studio.md` (new) + cross-refs in `suno-controls-and-workflows.md` §6, §8, §9, §10, §11 |
| 2026-08-14 | Suno Music official, *"Getting Started in Suno Studio 2.0"* (published 2026-08-14, 37 min) | `files/suno-studio.md` §10–13 — a full blank-canvas build with the mistakes left in; the source for the timeline-editing, workflow, export and sharing material |
| 2026-08-20 | **Our own generation** (Camping duet re-cut, round 1) + a web sweep on multi-voice casting | `suno-voices.md` Thread 4 + skill "Two characters in one song"; bounds Thread 3 §6; corroborates `lyricist-playbook.md` §3 and resolves its §4 duet disagreement |
| 2026-08-20 | **Our own generations** (Camping duet re-cut, rounds 5–6 — the orchestral layer arriving in bar one, twice) | `files/suno-tag-mechanics.md` entrance rules (delete the mention, don't describe the absence; My Taste has no section scope; escalate in gears) + `suno-voices.md` Thread 4 §6a + two skill routing rows |
| 2026-08-20 | **Our own generation** (Camping duet re-cut, round 6 — a mid-verse arrangement change that never happened) | `files/suno-tag-mechanics.md` — an inline cue is a modifier and the genre tag is the noun, so mid-section arrangement changes need a real section tag (`[Build]`); plus the easy-direction/hard-direction rule for instrument entrances |
| 2026-08-21 | **Our own generation** (Camping duet re-cut, round 14 — adding a guitar to a prompt that banned guitars) | `files/suno-tag-mechanics.md` — grep Exclude and My Taste for an instrument *and its category* before adding it; a stale ban is invisible and reads as the Style box being ignored. Plus how to word a low rhythmic guitar bed without getting a solo |
| 2026-08-21 | **Our own generation** (Camping duet re-cut, round 12 — a glockenspiel made two ranting men start singing) | `files/suno-tag-mechanics.md` — a melodic accompaniment invites a melodic vocal and will undo casting; when five wordings each fail *differently* the category is wrong, not the wording; plugin brand names don't travel, the synthesis technique does |
| 2026-08-21 | **Our own generation** (Camping duet re-cut — Suno rejected the word `skank`) | `files/suno-tag-mechanics.md` — `skank` is filter-blocked by artist-alias collision; a rejected innocuous musical word is usually a *name*, so describe the mechanic instead of naming it |
| 2026-08-21 | **Web sweep** (reggae/dub prompting guides) + **our own generation** (Camping duet re-cut, round 10) | `files/suno-tag-mechanics.md` — how to word a dub `skank` and a dub horn section; and the larger rule: reach for a **named technique** that is already sparse rather than spending rounds asking an instrument to play less |
| 2026-08-21 | **Our own generations** (Camping duet re-cut, round 9 — a sparse piano that stayed busy, and a `[Build]` gap that survived three denials) | `files/suno-tag-mechanics.md` — adjectives are comparative so give a **rate**; deny the part exists; swap to an instrument that physically cannot do the banned thing; and replace a fighting keyword rather than arguing with it (`[Verse 1 continues]` over `[Build]`) |
| 2026-08-21 | **Our own generation** (Camping duet re-cut, round 8 — a solo piano turned the whole track pantomime) | `files/suno-tag-mechanics.md` — naming a *form* imports its *texture* (`Chopin nocturne` = busy, not sad); one instrument's texture can flip the register; don't name the genre you're satirising in a mood line; negatives belong in Exclude, positives in Style |
| 2026-08-20 | **Our own generation** (Camping duet re-cut, round 7 — `[Build]` worked and emptied the section of vocals) | `files/suno-tag-mechanics.md` — a section tag brings its whole genre convention: never put a bar count on a tag you want sung over, and state the exception three ways |
| 2026-08-20 | **Our own generation** (Camping duet re-cut — the invented word `BLOUGH`) | `files/lyricist-playbook.md` §6 — the monosyllable respelling ladder, the `-ough` warning, and caps-on-invented-words; sharpens the ALL CAPS entry below |

Re-run the harvest script with a date filter to catch up on anything newer.

### Two things to know when weighing any of it

**The original GPT and the video channel are the same author.** That makes the corrections unusually
significant: they are places where the practitioner's own on-camera testing diverges from the
doctrine baked into his GPT — usually because a video is newer, or because he tested a rule and it
failed.

**Suno publishes no meta-tag list and no slider guidance.** This entire domain is folk knowledge
discovered by trial. Treat confident claims — including ours — as testable, not settled. Where the
corpus reports a controlled A/B test, that is noted inline.

**The corpus has a shape, and it is a producer's.** ChillPanic is a working music producer, so the
distillation is strong on sliders, model choice, Studio, stems, mixing and workflow — and thin on
everything a *lyricist* controls. This was found the hard way on 2026-08-08: the single most useful
discovery of a day's work on the GPOM chorus (that delivery speed is syllable density per line, and
that commas insert beats of silence) appears nowhere in 184 transcripts, and came from
songwriter-facing sources instead. When a lyric-side question comes up, assume this knowledge base
may simply not cover it and search outward.

## Known-unreliable claims

Recorded so nobody re-derives them:

- **ALL CAPS for emphasis** — failed a direct A/B test; evidence elsewhere is mixed. Not a mechanic.
  **On an invented word it is actively harmful**: an unfamiliar all-caps token reads as an
  initialism and gets spelled out or mumbled (`BLOUGH` → *bleh*, 2026-08-20). Capitalised real
  words are safe. Risk scales with how unfamiliar the token is.
- **Pipes vs commas in meta-tags** — no measurable difference across controlled testing. Keep the
  pipe as a readability convention only.
- **"Max Mode"** — almost certainly placebo; a gibberish control block performed comparably. The real
  effect is token padding, which changes output without improving it.
- **Regional accents** — a detailed Scouse spec produced no accent at all (tested 2026-08-20). Accent
  sits with age words: describable, not summonable. Contrast voices on pitch, texture, delivery mode
  and room instead. **But nationality is real and rides on the *genre* tag** — dropping `UK grime`
  turned the same voices American. Keep a UK genre; `British` alone is weak reinforcement.
- **Borrowing one attribute from a genre** — a vocalist pool is a *person*, not a property: accent,
  age, class and race come as one package. `UK grime` bought Britishness and cast two middle-aged
  white characters as young MCs. Pick the genre whose default performer *is* your character.
- **Per-line voice labels to fix a duet** — tested worse than one repeated short label per character.
  More casting markup makes casting worse.
- **A "quiet lead-in" cue to make a layer arrive late** — failed twice on the same track
  (2026-08-20). A cue describing a soft early version of an instrument still *names* it,
  and naming defaults to bar one. Delete the mention instead; state the entrance once in
  the Style box and once in the cue for the section it arrives in.
- **Inline cues asking for a weaker version of the genre's default sound** — e.g.
  `[drums enter — stripped back, no sub yet]` inside a neurofunk track. Produced no
  audible change at all (2026-08-20). Use a section tag (`[Build]`) so the model
  re-decides the arrangement; an adjective cannot outvote the genre tag.
- **A composer or repertoire name as a *mood* instruction** — `a Chopin nocturne,
  mournful` returned a busy, upbeat piano (2026-08-21). Form names carry texture and beat
  the adjective beside them. Describe the texture, and describe the silence.
- **Adjectives for sparseness** (`utterly sparse`, `more silence than notes`, `no melody,
  no runs`) — still returned a busy piano (2026-08-21). They are graded against the
  instrument's normal idiom. Give a rate: `one note every two seconds`.
- **Denying a section tag's connotation** — `[Build … no instrumental gap, no break in the
  words, carrying straight on]` still produced an instrumental gap, twice. Replace the
  keyword instead.
- **Plugin / brand names** (`Serum 2`, etc.) — no reliable effect, plus alias-collision
  risk. Name the synthesis technique (`wavetable`) and the behaviour instead.
- **Chord progressions as text** — ignored. Feed audio instead.
- **Music-theory intervals** (`third`, `fifth`) in harmony prompts — little effect.
- **The exotic meta-tag dictionary entries** — uncorroborated by any practitioner source.
- **The contamination-word compound ban** (`live drum kit`, `acoustic pop`) — probably over-broad;
  the trigger looks like venue/audience words rather than instrument modifiers.

## Volatile areas

Re-verify before relying on these; they move fast and some are version-pinned:

- Model behaviour (v4.5 creative vs v5.5 polished; mumble mode broken on 5.5; Studio better on v5)
- Feature names and locations (Persona was renamed **Voice** in v5.5)
- **Everything in `files/suno-studio.md`** — two vendor videos, nothing tested by us or by an
  independent practitioner. Suno is shipping Studio fast; assume it has moved again.
- Plan tiers, pricing, credit costs, and which features each tier gates
- Rights, ownership, AI-disclosure requirements, and distributor policy
