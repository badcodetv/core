---
slug: jungle
name: Jungle
kind: sound
family: UK street and bass music
checked: 2026-10-28, references and engine notes (see Web check)
---

# Jungle

> Frantic chopped breakbeats at about 160 to 170 BPM over slow, heavy sub-bass and ragga or soul samples, from London's mid-1990s rave scene.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Jungle emerged in London and Bristol around 1992 to 1994 from breakbeat hardcore, reggae sound-system culture and dancehall, sped up so that chopped Amen and other breaks run at roughly 160 to 170 BPM while the bass moves at half that speed. The result is a doubled sense of time: manic drums over slow, heavy sub-bass. Black British and Caribbean-descended producers made it, and its sampling of ragga MCs, soul and film dialogue gives it a documentary, street-level mood. It later split into drum and bass, but jungle proper remains rougher, more break-driven and more dub-influenced.

## Signature traits

- Tempo about 160 to 170 BPM with chopped, time-stretched Amen-style breakbeats and fast ghost-note snares
- Slow, dub-derived bass playing a half-time line, often deep sine or heavy reese
- Ragga/dancehall vocal samples and MC shouts ('big up', 'rewind') used as hooks
- Atmospheric pads and sampled soul or jazz chords for contrast, as well as film dialogue clips
- Dense, busy drum programming with swung or stuttered edits and abrupt breaks and rolls
- Dark, urban sci-fi mood in the darker strains; warmer and bright in the 'intelligent' strains
- Rewind/drop structure with long builds and sudden silence

## References

- *Original Nuttah* — Shy FX & UK Apache, 1994. A defining ragga jungle anthem: a ragga vocal over rolling breaks and a sub bass.
- *Inner City Life* — Goldie (as Metalheadz, album Timeless), 1995. The epic, atmospheric end: breaks, strings and a soul vocal, with real emotional weight. **(Corrected: Goldie (feat. Diane Charlemagne), single 1994 on Metalheadz; it is the opening track of the album Timeless (1995). Metalheadz is the label, not the artist. The search found nothing on this, so the fix comes from memory.)**
- *Brown Paper Bag* — Roni Size / Reprazent, 1997. Jazz-inflected, live double-bass drum and bass that won the Mercury Prize with New Forms.
- *Terminator* — Goldie, 1992. Early dark breakbeat hardcore that shows jungle's origin. **(Unconfirmed on the web.)**

## What it carries

Restless, urgent, tense, euphoric and dark in turns. It carries a sense of a city at night, anxiety, pursuit and defiance. It fights against anything relaxed, reflective or sentimental, and against a lyric that needs room to be heard.

## What it suits, and what it would undermine

Chase, heist, escape and uprising sequences, montage, or the sped-up collapse of a system (a market, an institution) where manic drums = panic. Instrumentals work well under footage. It would undermine a story that relies on a clear, spoken argument, because the busy drums fight with the voice, and a quiet or tender story.

## Asking Suno for it

Suno Style box: 'jungle, 165 BPM, chopped Amen breakbeat, fast ghost snares, deep half-time sub-bass, ragga MC vocal sample, dark atmospheric pads, 1994 rave'. Use 'instrumental' for beds. Exclude 'EDM drop, supersaw, pop vocals, trap, four-on-the-floor kick, liquid piano ballad, autotune'. Because the jungle/drum and bass boundary is blurred in training data, name 'ragga jungle' or 'Amen break' and 'not modern neurofunk'. Lyrics can be just one-line MC chants tagged [Hook].

## How generators get it wrong

Suno tends to produce modern polished drum and bass (clean 174 BPM two-step drums, melodic synth lead, festival drop) or a stiff loop of a single break rather than real edit-heavy chopping; breaks are often quantised and too regular. The ragga voice tends to become a generic rap or sing vocal. Fix by naming 'chopped, edited breakbeat, rolling snares, lo-fi 1994 sampler grit', and generate only short sections that you then edit together. Bass may come out at full speed rather than the half-time feel; add 'half-time bass line'.

## Measured in our own Suno runs (drum and bass, 2026-09)

Moved here on 2026-11-18 from the `suno-prompt` skill, where it sat as BadCode's own notes on drum and bass
(original: `archive/skill-pollution-2026-11-18/suno-prompt/SKILL.md`). Drum and bass is filed under jungle in
this library because the two are close in tool prompts. These are tested findings, not first guesses.

1. **Half-time drums are a blind spot.** Repeated controlled tests never produced half-time from a `breakdown`
   tag; it slows and thins the arrangement instead. Since the half-time drop is a defining drum and bass device,
   assume it cannot be prompted: edit it in Studio or splice sections, and say so. Untested lead: Studio 2.0's
   MIDI tracks to program the pattern by hand (`docs/suno-gpt/suno-studio.md` §2).
2. **Niche subgenres fail; broad ones work.** Riddim came back as generic dubstep with none of its sound design;
   expect the same at neurofunk, liquid and jump-up level. Describe the sound design and rhythm instead of the
   subgenre name. v6, 2026-09-09: a lazy `liquid DnB` prompt came back as two-step drums, while one naming the
   drum mechanics (`jungle breaks, rapid chop, hyperdetail percussion, dark synth bassline`) worked on both
   models. v6 Wild is the model to hunt niche drum and bass in, then Cover into v6 (`docs/suno-gpt/suno-v6.md` §9).
   `producer-vocabulary.md` has the toolkit: reese bass, sample-and-hold on the cutoff, amen break, sub layering,
   sparse drop.
3. **Suno's harshness sits where drum and bass lives:** brittle cymbals, sizzling hats, sibilance at 2–6 kHz.
   Budget for de-essing, or plan to replace the drum stem.
4. **Sidechain pumping is baked in** and cannot be undone.
5. **Sounds mode is the transitions kit** (risers, downlifters, sweeps, impacts, fills at the project's BPM and
   key); Suno won't build transitions into a generation.
6. **A fill over a bed that already is that fill never arrives** (an amen fill over `chopped amen breaks`):
   describe the event that changes against the bed, not a bar count.

## Production cost

Rhythms are consistent within a prompt, but long takes tend to loop. Cutting between sections is easy in an edit, so jungle is workable across a story as a recurring cue. Vocals are the weak point and are best kept as sparse chants.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

Sources:
- <https://en.wikipedia.org/wiki/Original_Nuttah>
- <https://en.wikipedia.org/wiki/New_Forms>
- <https://en.wikipedia.org/wiki/Original_Nuttah>
- <https://en.wikipedia.org/wiki/New_Forms>
