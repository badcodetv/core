# Suno toolkit

The knowledge base behind the **`suno-prompt`** skill (`.claude/skills/suno-prompt/`). The skill is
the entry point — this is what it reads.

## Files

| File | What |
|---|---|
| [`system-prompt.txt`](./system-prompt.txt) | Base operating procedure — mode detection, output format, character limits, famous-artist translation, edge cases |
| [`files/suno-tag-mechanics.md`](./files/suno-tag-mechanics.md) | The prompt language: hybrid format, information ordering, genre pairing, bracket language, exclude strategy, contamination words |
| [`files/suno-controls-and-workflows.md`](./files/suno-controls-and-workflows.md) | **The control surface and the platform.** Sliders, model choice, the consistency stack (Voice / custom model / Lyricist), lyric editing, Studio, stems, known failure modes |
| [`files/producer-vocabulary.md`](./files/producer-vocabulary.md) | Words for describing sound, by domain; song structure; how to judge a generation |
| [`files/lyric-craft.md`](./files/lyric-craft.md) | Syllable counts, rhyme schemes, section shapes, engineered transitions |
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
- **Pipes vs commas in meta-tags** — no measurable difference across controlled testing. Keep the
  pipe as a readability convention only.
- **"Max Mode"** — almost certainly placebo; a gibberish control block performed comparably. The real
  effect is token padding, which changes output without improving it.
- **Chord progressions as text** — ignored. Feed audio instead.
- **Music-theory intervals** (`third`, `fifth`) in harmony prompts — little effect.
- **The exotic meta-tag dictionary entries** — uncorroborated by any practitioner source.
- **The contamination-word compound ban** (`live drum kit`, `acoustic pop`) — probably over-broad;
  the trigger looks like venue/audience words rather than instrument modifiers.

## Volatile areas

Re-verify before relying on these; they move fast and some are version-pinned:

- Model behaviour (v4.5 creative vs v5.5 polished; mumble mode broken on 5.5; Studio better on v5)
- Feature names and locations (Persona was renamed **Voice** in v5.5)
- Plan tiers, pricing, credit costs, and which features each tier gates
- Rights, ownership, AI-disclosure requirements, and distributor policy
