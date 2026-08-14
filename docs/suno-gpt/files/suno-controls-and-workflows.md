# Suno Controls & Workflows

The part of Suno that isn't the Style box: the three influence sliders, the features that carry a
*voice* across a whole release, and the human procedures for building and fixing a track.

`suno-tag-mechanics.md` tells you what to *write*. This file tells you what to *do* — and which
knobs decide whether Suno obeys what you wrote.

> **Provenance.** Distilled from ~184 transcripts of the ChillPanic YouTube channel (a working
> producer who has used Suno since 2023), harvested 2026-07-29. See `docs/suno-gpt/README.md`.
> Everything here is one practitioner's tested experience, not Suno documentation — Suno publishes
> no meta-tag list and no slider guidance, so this whole domain is folk knowledge.
> **It dates fast.** Version notes are marked inline.

---

## 1. The three sliders are the real control surface

They only appear in Advanced mode (and Studio). Free-tier accounts reportedly don't get them.
Learn these before learning more tags — they govern whether your prompt is obeyed at all.

### Style influence — how literally Suno obeys your text

| Value | Behaviour | Use when |
|---|---|---|
| 0 | Suno's own musical judgement dominates; wanders off-brief | You want the reference audio to lead |
| 50 (default) | Balanced. Safe while your prompt vocabulary is still weak | Exploring |
| **75** | **The working default for a prompt you trust.** Strong adherence, still musical | Most BadCode work |
| 100 | Follows literally; can over-tighten and *degrade* adherence | Lyric-swap covers; a prompt you're certain of |

The single most-repeated numeric tip in the whole corpus is **75, not 100**. Push it up as your
prompts get more specific — high style influence rewards good vocabulary and punishes vague prose.

### Weirdness — injected randomness

| Value | Behaviour |
|---|---|
| 0 | Maximum obedience. Use whenever you need an exact reproduction (covers, lyric swaps, model upgrades) |
| 50 (default) | Effectively *no* randomness |
| **60–65** | **The creative sweet spot** — interesting without going off the rails |
| 80+ | UI turns this red as a warning |
| 90–100 | Glitch nonsense — but genuinely useful as free sample fodder (reversed beats, chopped vocals, IDM textures) |

Pairing rule: **weirdness 60–70 + style influence 75** sticks to the brief while still surprising
you. **Weirdness 0 + style influence 100** is maximum literal obedience.

### Audio influence — how hard your source audio drives the result

Only appears when there is source audio (cover, remix, upload, sample, Studio cover). This is a
**faithfulness-vs-fidelity** trade: high = follows your melody accurately but sounds worse
(artifacts, "underwater"); low = cleaner but takes liberties.

| Value | Use |
|---|---|
| 25 (default) | Suno takes liberties; best audio quality |
| **35–40** | **The workhorse.** Preserves melody with minimal quality loss |
| 50–60 | Clearly uses your melody, some quality cost. ~60 keeps a sample recognisable |
| 75–85 | Only when a specific vocal melody must survive verbatim (seeding from a hum; turning a soft chorus into a belted one). 85 for double-tracking |
| 100 | Audible degradation. Occasionally useful as an effect, or for lyric-swap covers |

**The two-pass melody capture** fixes "accurate but sounds like garbage": generate at audio
influence ~100 until the melody is right, then Cover *that result* at ~25. The melody is now baked
into the audio, so it survives at full quality.

Note the number means different things per context — 25–60 for voice cloning, ~30 for vocal
doubles, ~40 for harmonies, ~60 for samples, 100 for lyric-swap covers. Treat it as
context-dependent, never a global setting.

### Studio's standard recipe

**Weirdness 0 / style influence 75–80 / audio influence 25** is the reusable Studio combo for
covering your own recorded audio into an instrument.

---

## 2. Model choice — don't assume the highest number

- **v4.5 / 4.5+** — more musically *creative*. More varied instrumentation, more interesting tones,
  different vocalists between generations.
- **v5 / 5.5** — more *polished* and consistent, but blander, with harsher highs (excess energy
  around 3.4 kHz, audible sibilance and hiss).

**The hybrid move — generate in 4.5+ for the ideas, then Cover into 5.5 for the sonics.** Drag the
track into remix → Cover → newest model → **weirdness 0, style influence 0, audio influence 35–40**.
Result keeps the melody and arrangement, raises fidelity; instrument tones shift slightly. Below ~25
it starts rewriting the song. **Remaster** (three dots → Create → Remaster, *Subtle* or *Normal* —
never *High*) is the lighter-touch alternative for the same goal.

Suno Studio is the exception: **v5 outperformed v5.5 inside Studio** for voice→instrument work.

---

## 3. Setup hygiene (do this once per release, not per song)

1. **One workspace per release/arc.** Generations pile up fast; an undifferentiated workspace with
   thousands of songs becomes unusable.
2. **Neutralise "My Taste"** — it silently biases every generation toward what you've made before:
   contamination for a deliberately-designed release, and a suspected cause of v5.5 homogenisation.
   *(Corrected 2026-08-05, verified against the live UI: there is **no off switch**. The dialog has
   a 2,000-char free-text profile that **cannot be saved empty** — a profile can only be replaced,
   never disabled — plus a "My Styles" toggle that governs only the magic-wand style-suggestion
   button, not generation bias. Working procedure: swap in a per-track profile that pulls the same
   way as the song, restore the house profile after. The written profile is only the explicit half —
   Suno also learns from what you create, listen to, like and dislike, with no control surface;
   mitigate by thumbs-downing every reject and keeping one workspace per arc. Full forensics:
   [`../suno-voices.md`](../suno-voices.md) §8.)*
3. **Plan tier before you generate anything.** Free-plan output **never** gains commercial rights,
   even retroactively after upgrading. Anything you might release must be generated on a paid plan.
   Studio requires the top tier; the Editor and stems require at least Pro.
4. **Pick the coherence anchor now**, not at the end (§4).
5. **Triage as you go.** Thumbs-down every reject the moment you pick a keeper — disliked
   generations disappear from the workspace. Bookmark prompts that work; that library becomes the
   house style.

**Over-generate and cull hard.** A 13-track album took 17 finished candidates. The human
contribution to an AI release is taste, not prompting.

---

## 4. Coherence across a release — the consistency stack

This is the highest-value section for BadCode, which needs one recurring narrator across a whole
story arc.

### Voice (formerly "Persona") — the primary mechanism

Renamed **Persona → Voice** in v5.5. Two ways to build one:

- **From a generation you like:** song's three-dot menu → Remix → Voice. Suno isolates the vocal via
  stem separation. Name it, optionally select the sub-region you want, and **delete the attached
  style prompt** so the voice isn't welded to one genre — essential if the narrator must work across
  tracks. It survives a total genre change.
- **From your own audio (voice cloning):** top bar → Voice → Create voice → upload / library /
  record. You can upload a finished mixed track; Suno stem-separates under the hood.

Then: Advanced → **+ on Voice** → choose it.

**Verification trick:** Suno makes you read a phrase aloud to prove the voice is yours. Reading it
flat fails repeatedly; **singing** it, in the style of the reference clip, passes ~90% of the time.
The check is matching you against the reference.

**Expect a *consistent, unique* voice — not *your* voice.** Suno generalises toward a nearby
archetype. Even done well, cloning underdelivers on exact likeness.

### Custom model — the fidelity multiplier

Upload audio and Suno trains a model that generates in that idiom. **Minimum 6 files; docs suggest
24+.** The non-obvious trick: **upload the same file 6+ times** to build a model of one specific
song or voice.

**The "brainwashing" stack:** a Custom Model *and* a Voice trained on the same clip, used together.
Audio influence 25–60; above 60 gives artifacts. This is the recipe for a locked-in recurring
narrator.

**The maximum-information stack:** custom model + voice + the same song uploaded again as cover
audio, all at once. Export the full mix and the isolated acapella *separately from your DAW* — don't
rely on Suno's stem separation for the voice source, because separation artifacts degrade the model.

**Critical caveat:** the reference clip must be **one consistent delivery**. A clip that switches
registers produces an unstable clone. Record one uniform register.

### Inspo — album-level vibe

Point at a whole playlist rather than one track; new generations inherit the collective feel.
Explicitly the album-coherence tool.

### Lyricist — a saved *writing* voice (v5.5)

Full-screen lyrics editor → **Lyricist**. Give it a name, a prose description of who they are and
what they write about, and a sample block of their lyrics. Its lyric generation then writes in that
register.

*BadCode application:* this is the natural home for the narrator's register — described as
sarcastic, authoritative, nurturing underneath, seeded with our strongest existing verses. Pair with
a Voice + Custom Model so the same character both writes and sings consistently across the arc.

### Unique vocals: build the Voice in the *opposite* genre

Record the reference in a register deliberately opposed to the target song. The mismatch is what
breaks Suno out of its generic per-genre vocal default. Audio influence **40–60** gives the
strongest effect.

*BadCode application:* the narrator is a future superintelligence, not a D&B MC. Building its Voice
from spoken oratory, opera, a gospel preacher or a sardonic crooner is the cheapest route to a vocal
no other Suno D&B track has.

---

## 4a. Two voices in one song — the layered-cover method

> **Added 2026-08-08** from ChillPanic, *"Finally! Use TWO VOICES in ONE SUNO AI SONG"*, published
> **2026-08-04** — after the 2026-07-29 harvest, so it is not in the rest of this file. It is the
> author's own answer to the problem §4 could only work around.

**The premise: you do not get two voices out of one generation.** Every prompt-side trick (the
parenthesis slot, section cues, one saved Voice per generation) is a way of *biasing* a single
generation's vocal identity. This method stops fighting that and assembles the song instead — one
generation per voice, stems, layered over a shared instrumental. The author is explicit that it is
more work than prompting and argues that is the point: "this method requires a little bit more than
just straight-up prompting, but by learning it, you will not only be able to use as many voices as
you want."

**The critical consequence for us: there is no leak, because the voices never share a generation.**
Casting stops being probabilistic.

### The procedure

1. **Generate the instrumental first, alone.** Advanced tab (the author notes beats come out better
   in Advanced than Simple), style prompt in the Styles box, **More options → Instrumental**.
   Weirdness **0**, style influence **70**.
2. **Read its BPM and write it down.** Open in the Editor or Studio to see it. This is the song's
   "home base" — every later step is pinned to it.
3. **Cover that instrumental once per voice.** Drag the instrumental into **remix/cover**, and pick
   the saved Voice at the top if you have one.
   - **Delete the style prompt entirely.** Replace it with *only the BPM*, optionally plus a
     **vocal-delivery** description. `101 BPM, belted emotional chorus`.
   - **Do not mention the instrumental at all** — that is the load-bearing instruction. You are
     asking for a vocal performance, not a song.
   - Lyrics box: real lyrics, or a prose description of what the singer sings.
   - Sliders: **weirdness 0, style influence 100, audio influence 40** (40–60 whenever the result
     must stick to the source).
4. **Repeat for voice two against the *same instrumental*** — not against the take you just made
   with voice one. The author corrects himself on camera specifically to say this.
5. **Stem the lead vocal out of each cover.** Three dots → **Get stems / MIDI** → **advanced split**
   → *lead vocal* → extract → download as **WAV**, **fixed tempo**. The zip is named with its BPM.
6. **Open the original instrumental in Studio** (single track). Set BPM to **Manual** and type the
   instrumental's BPM. This is the master tempo.
7. **Drag each vocal stem onto its own track.**
8. **Set every vocal track's tempo mode to `on beat`, not `original`.** (Click the clip, `4` opens
   the sidebar.) **`on beat` time-stretches the vocal to the project BPM** — which is what
   reconciles a vocal that generated at 102 against an instrumental at 101. Miss this and the
   layers drift apart.
9. Place, duplicate and treat freely — the author duplicates a rap vocal and EQs the copy into a
   lo-fi radio effect for one section. Export as full song.

### What it costs, and what it buys

- **Expect the instrumental to change slightly on each cover, and expect extra vocals.** The author
  says this repeatedly and says it does not matter: those covers exist only to be stemmed. The
  instrumental you keep is the original from step 1.
- **Each voice gets its own full style box and its own sliders** — so two voices can be described
  in as much detail as one, instead of competing for one prompt's attention.
- **"As many voices as you want"**, not two — the method has no ceiling. The single-generation limit
  of 2–3 differentiated voices (§4, and `suno-voices.md` Thread 1) does not apply.
- **Requires Pro or above** for stems, and a DAW or Studio. Any DAW works; Studio is used in the
  video only because it is a Suno video.
- **A saved Voice per character makes it stronger but is not required** — step 3 can carry the
  voice in the style box as a delivery description instead.

### When to reach for it

Use prompting first: one generation that lands is cheaper than an assembly. Reach for this when the
casting is the thing that keeps failing — two voices that must not blend, a voice that must be
absent from one section, a chorus that keeps getting claimed by the lead. Those are exactly the
failures that prompting cannot *guarantee* away, and this method makes them structurally impossible
rather than improbable.

## 5. Building a track — the section-by-section loop

Do **not** try to prompt a whole finished song in one shot.

1. **Seed one strong section** (usually the chorus), ideally from uploaded audio — even a 10-second
   phone hum — at audio influence ~85 so your melody survives.
2. **Extend** from it. The extend UI splits into pink `keep` (verbatim) and grey `recreate`
   (regenerated bridge). **Do not drag the divider all the way right** — leave a slice of the ending
   inside `recreate` so Suno knows what it's continuing.
3. Prompt the extension for **what happens next only**, not the whole song.
4. **Get full song** concatenates original + extension.
5. Repeat: extend → get full song → extend. Intro → verse → chorus → verse 2 in four passes.
6. Vary audio influence per pass: **75–85** to inherit an existing melody, **~40** to let it invent.

Use `[instrumental]` to force an instrumental section, and an empty `[Verse 2]` tag to block out
structure before you have words.

**Rule of thumb: once you have half a song, you have the song** — verse 2 is a reinterpretation of
verse 1.

### Mumble mode — melody before words

Put `[mumble mode]` then a lowercase `a` in the Lyrics box. Suno sings wordless phonetic shapes with
real phrasing; you then write lyrics into that rhythm. Mirrors how pop songwriters actually work
(vowel shapes first, language after).

**Version-critical: works on v4.5+, broken on v5.5** (5.5 sings real words instead). So: mumble on
4.5+, then model-upgrade cover it to 5.5.

---

## 6. Changing lyrics without losing the song — four methods, ranked

Nothing gets you a byte-identical result. Expect small drift.

> Studio 2.0 adds a fifth surface — **cover in place** on a selected region, driven from the chat
> ("keep the lyrics the same but cover this into a new lead vocal performance"): same timing, same
> melody, new performance. It does **not** replace method 1 for voice preservation. See
> [`suno-studio.md`](./suno-studio.md) §4–5, which also lays out honestly how close 2.0 gets to
> re-singing a single word in the original voice (answer: not there, but the primitives now exist).

**1. Custom model of the song itself (~99.9%, best).** Download the song as **WAV** → Create custom
model → drag the same WAV in **6+ times** → name → create → wait. Select the model, drag the song
into remix on **Cover**, **delete the styles box entirely**, paste lyrics with your edits, set
**weirdness 0 / style influence 100 / audio influence 100**. Preserves voice and delivery exactly,
even when syllable counts change. Cost: one custom model per song.

**2. Studio multitrack cover (best without building a model).** Three dots → Edit → Open in Studio →
Multi-track. **Duplicate the vocal track** so the generation draws context from it. Click the vocal
clip — the right panel shows Suno's transcribed lyrics; copy the section you're changing. Select the
region → generate panel → **Cover** → category **Vocals** → paste the edited lyrics. **Leave the
style box blank** (a style prompt muddies the impersonation). **Weirdness 0, audio influence ~70**
(try 80–100 if the voice drifts). Set the model to the version the original was made in.
*Limitation:* regenerates the **lead vocal only** — backing vocals for that section are lost.

**3. Remix → Cover.** Drag into the remix slot on **Cover**, **delete the styles box**, edit the
lyrics, set **weirdness 0 / style influence 100 / audio influence 100**. No setup, but expect drift
in guitar tone and delivery — it re-covers the whole song rather than patching a section.

**4. The Editor (worst).** Three dots → Edit → Open in editor (Pro). Click a section, its lyrics
appear; **Replace lyrics** → type → algorithm (**Smart** default; **Fixed** for 1–2 words;
**Classic** for long sections) → **Replace**. Gives two alternates: preview, then **Commit** or
**Regenerate**. **Heal edits** undoes everything. Finish with **Save as new song**.
- **Select a whole line, not a single word** — single-word replacements fail and leave audible seams.
- **Keep the syllable count and, if you can, the rhyme.**
- It frequently rewrites the melody, and it can **silently flip the singer's gender** — pin the
  gender in the style prompt first.
- After Editor surgery, run a **Cover of the edited song** with the same style and lyrics to smooth
  the seams.

---

## 7. The other Create-tab tools

- **Cover** — reinterprets the melody in a new style.
- **Sample** — tries to place the *actual audio* inside a new arrangement, hip-hop style. **Include
  the literal word `sampled`** in the prompt; it measurably behaves better. Minimum 1 second; too
  long and Suno refunds your credits and returns garbage. Audio influence ~60 to keep the source
  recognisable, ~40 for tasteful flourishes.
- **Mashup** — combine two songs; choose whose lyrics survive (A / B / merge). Also the trick for
  putting your own recorded vocal onto a Suno instrumental *without* the Voice feature: upload the
  vocal, drag the instrumental in, switch to Mashup, take the lyrics from the vocal, **delete the
  style box**. Beta and chaotic.
- **Adjust speed** — multiplier plus a keep-pitch toggle. For chipmunk-soul flips leave keep-pitch
  **off**; 1.33× is the sweet spot, 1.5× is too much.
- **Sounds tab** — one-shots, loops and SFX at 2 credits. Prompt as *sound + timbre + [LENGTH IN
  CAPS]*. Set BPM and key to match your track for musical material; leave both on "any" for spoken
  word. **One-shot works better than loop.** Prefix a throwaway word plus a comma ("Yeah, …") for
  spoken word, because the first word regularly gets clipped.
- **Add vocals / add instrumental** on uploaded audio — one-directional completion tools most people
  miss.
- **Skip "Add stem"** (adding one instrument to a finished song). It fails repeatedly. Use Studio.

---

## 8. Suno Studio

> **The app surface moved on 2026-08-13 — see [`suno-studio.md`](./suno-studio.md) for Studio 2.0**
> (project-aware chat, MIDI tracks and musical typing, live-recording latency calibration, a real
> effects rack with sidechain, automation, and natural-language custom plugins). That release is
> **additive and backwards compatible**, so everything in this section still holds. Split of duties:
> that file is *what's in the app and how to drive it*; this section is *how to get a good generation
> out of it*.

A paid add-on and a genuinely different environment: a multitrack editor over an existing song's
stems, *and* a single-element generator.

**Studio is weakest building from nothing and strongest adding to an existing song.** Every element
already in the project becomes context for the next generation; a nearly-empty project generates
badly.

### The three verbs

- **Create** — invents new material fitting the surrounding context. For adding layers.
- **Replace** — regenerates over the selection, ignoring its melody, using the rest of the
  arrangement as context.
- **Cover** — regenerates *from* the selected audio, so it follows your melody. This is what makes
  voice→instrument work possible, and it's usually the one you want.

### Practical rules

- **Set BPM to Manual** and type the real BPM — auto-detect is unreliable and Suno drifts.
- **Highlight slightly more region than you want** — Studio truncates generations at random, and too
  short a selection produces a useless generation.
- **Always fill Exclude Styles** — Studio adds unrequested instruments constantly. Typical pairings:
  want drums → exclude `vocals, guitar, bass`; want a synth → exclude `drums, vocals`. **Clear it
  between generations** — a stale exclusion will silently ruin the next take.
- **Categories:** Song, Vocals, Backing vocals, Drums, Bass, Guitar, **Keyboard** (there is no
  "piano"), Synth, Woodwinds, Brass, Effects.
- **Take lanes** — every generation makes several takes. There's no "select this one" button; drag
  the take you want onto a new track. Two good takes panned opposite is instant width.
- **Corner handles** on a clip: bottom-right drag = fade out (the reliable outro — extend is
  unreliable for endings); bottom-left = fade in (kills the click Studio generations often start
  with); top corners = trim.
- **Ctrl+E** splits at the playhead, **Ctrl+D** duplicates.
- **EQ** (v1.2+) per clip or per track: high-pass, low shelf, peaking, notch, high shelf, low pass,
  with a resonance/Q knob and presets (Clarity, Bass boost, Lo-fi, Modern).
- **Export → Multitrack** (rename tracks first or the zip is unreadable) / **Full song** / **selected
  time range**.

### Studio prompt craft

Studio punishes elaborate prompts. Describe **one instrument in a few words**, front-load the most
important word, and add `only` to suppress extras. Working shapes:

```
house drums big 909 kick sharp transient thumpy four on the floor
synth bell, pluck, bells
bass, staccato, stabby 8s, west coast moog bass
guitar solo, slides, pinch harmonics, high amp gain, only guitar
```

Two reusable devices: **gear model numbers as tone shorthand** (`909 kick`, `MPC drums`) and
**restriction repeated in different words** (`vocals only, only rap vocals`; `just snare`).

> **Correction to the older doctrine:** the previous guidance said *never* use genre tags in Studio.
> In practice nearly every working Studio prompt **leads with a genre** (`house drums`,
> `boom bap hip hop drums`, `crunchy hard rock lead guitar solo`) because the genre is doing useful
> work as tone shorthand. The real constraint is **"don't describe a song"**, not "don't name a
> genre."

### The bootstrap trick

When Studio fights you on a from-scratch build: rough out the parts however janky → **Export → Full
song** → Create tab → **Cover** with a minimal style prompt (literally just the genre), **audio
influence 60, weirdness 0** → bring the covered song **back into Studio**. Now Suno has whole-song
context and everything afterwards locks in far better.

> **Studio 2.0 makes this concrete, and adds the step that matters** — advanced-split the covered
> take and **harvest two or three stems** rather than keeping the whole thing. The dragged-in cover
> auto-adjusts to the project tempo, and *insert all* arranges the stems to its timing. Full recipe,
> click by click: [`suno-studio.md`](./suno-studio.md) §11B.

---

## 9. Stems

**Why they sound bad, structurally:** Suno generates one master audio file end-to-end — it never had
separate instrument tracks. A stem splitter *guesses* which energy belonged to which instrument from
the finished mix. So a "bass" stem is mostly just the low band (containing kick and vocal
fundamentals, missing the bass's upper harmonics), every stem carries bleed, and no setting fixes it.

- **Vocals separate best. Drums are usually worst.**
- Artifacts concentrate in the **top end (~2–6 kHz)** as hiss/sizzle and the extreme lows as clicks.
- **Suno stems export mono.** Widen them.
- **Sidechain pumping cannot be undone** — Suno learned to *sound* pumped without a real sidechain.

**Use the advanced splitter, not autosplit.** Advanced **regenerates** each stem rather than
spectrally carving it — dramatically cleaner, especially vocals. Path: three dots → **Get stems /
MIDI** → advanced split → name the stems you want. Download **WAV**. Export MIDI at **fixed tempo**
so it grids in a DAW.

Stems are hidden in the workspace by default — Filters → uncheck **Hide stems**.

**Inside Studio 2.0** the same advanced split runs on a clip and **inserts the stem straight onto the
timeline** below the original; the Studio PM confirms he uses advanced split every time, for fidelity.
Studio also has **remove effects** (right-click a clip) to recover a dry signal — including from audio
you imported — which is the missing half of this section: a processed vocal is no longer processed
forever. See [`suno-studio.md`](./suno-studio.md) §6.

**Don't stem a song you only want to master.** Master the full stereo bounce; recombined stems
always sound worse. Take stems only when you intend to genuinely re-produce.

**De-artifact a stem by covering it in Studio:** solo it, highlight the region, set the instrument
category → **Cover**, style = a plain description plus the word `only`, exclude the other
instruments, **audio influence 30 / style influence ~60**. Low audio influence is what strips the
artifacts.

**"Reduce more than you produce."** The single highest-value thing to do with stems, and it costs no
generations: *remove* elements from early sections. Drop the synth out of verse 1, mute the drums
through the pre-chorus so they slam back at the chorus, cut everything for a beat before the final
chorus. This is where a flat AI arrangement gains dynamics.

---

## 10. Known failure modes — plan around these, don't fight them

1. **Half-time / double-time drums.** Across controlled tests a `breakdown` tag always slowed and
   thinned the arrangement but **never produced half-time drums**. The model appears not to
   understand the concept. **Directly relevant to D&B, where the half-time drop is a core device** —
   get it by editing in Studio or splicing sections, not by prompting. **Untested lead (2026-08-13):**
   Studio 2.0's MIDI tracks let you *program* the pattern by hand and render it to a drum part, which
   sidesteps the model's missing concept entirely. Best candidate in the update for BadCode — test it
   before recommending it.
2. **Isolating instruments by meta-tag.** "Vocals only", "a cappella", "no drums" are unreliable. If
   you need an element gone, **stem it out** — don't ask.
3. **Niche subgenres.** Broad genres work; specific subgenres don't. Riddim came back as generic
   dubstep with none of the characteristic sound design. Expect the same at neurofunk / liquid /
   jump-up level — **describe the sound design and rhythm instead of naming the subgenre.**
4. **Tempo drift** within a generation. State BPM in the prompt and pin manual BPM in Studio. Suno
   can still emit odd BPMs like 100.2357.
5. **Making songs longer.** The duration control reliably *shortens* but repeatedly fails to stretch.
   Lengthening is a job for Extend or duplicating a section.
6. **Ad-lib spam**, especially in rap — the compulsive "whoop!" after most bars. Put the ad-lib
   sounds themselves in Exclude Styles.
7. **The content filter blocks silently and mislabels.** Innocuous prompts get rejected as
   "copyrighted lyrics". **Rewrite, don't retry** — substitute a synonym or nonsense phrasing that
   keeps the rhythm.
8. **Studio stem extraction isn't guaranteed** — it sometimes refuses with no explanation.

---

## 11. Things that don't work (stop recommending them)

- **ALL CAPS for emphasis in the Lyrics box** — failed a direct A/B test by the person who
  popularised much of this vocabulary. Evidence is mixed (a separate test found caps + `!` reading as
  shouted, with partial success). **Treat as unreliable, not as a documented mechanic.** For shouted
  delivery use a bracket cue (`[angry voice]`, `[yelling]`) instead.
- **Pipes instead of commas inside meta-tags** — tested across eight generations per condition on
  three tag types. **No difference whatsoever.** Use commas. (The pipe is still fine as a readability
  convention; it just isn't a mechanic.)
- **The "Rhymes" tool** in the lyrics box — reportedly never works.
- **Chord progressions as text.** Suno was trained on adjectives describing vibe, not music theory;
  chord symbols are near-meaningless tokens. **Feed it audio instead** — play or render the
  progression, upload, and Cover it at audio influence ~40. **Or, since 2026-08-13, feed it notes:**
  Studio 2.0's MIDI tracks take the progression — voicing and all — by keyboard or musical typing,
  and chat renders it to any instrument. Same fix for intervals below. Untested by us.
- **Music-theory intervals** (`third`, `fifth`) in harmony prompts — little effect. Raise weirdness
  to ~60 instead to get a genuinely different harmony line, or write the line as MIDI.
- **"Max Mode."** The viral code block is almost certainly placebo: a control test with meaningless
  gibberish of the same shape produced a comparably different-and-decent result. **The real mechanism
  is token padding** — stapling many extra tags onto a prompt changes the output whether or not they
  mean anything. Different ≠ better. Ship it on request, don't recommend it unprompted.
- **Suno's built-in image/video generation** for cover art — poor and expensive.
- **Remove section / Crop** — no real use case.

---

## 12. Suno's own lyric tools

- **Magic wand on the Style box** — genuinely useful; rewrites your prompt "into Suno's language".
  Worth running once just to see how Suno wants to be spoken to.
- **Magic wand on the Lyrics box ("write full song")** — reject it. Suno's lyric model is a
  next-token predictor, so its default output is by construction the *most common* phrasing
  available. It compulsively writes about **wires, circuits, fractured things and broken glass**.
- **Reference** — highlight a span, then type a natural-language instruction; it rewrites in place.
- **Variations** — highlight, get ~5 alternative phrasings.
- **Library** — save and recall lyric blocks.
- **Lyrics models:** **Classic** follows the prompt more closely; **Remy** takes more creative risks.

**Division of labour that the whole corpus supports: AI writes the style prompt, humans write the
lyrics.**

---

## 13. Release notes (verify before relying — this moves fast)

- **Free-plan output can never be monetised**, even after you upgrade. Never draft anything you might
  release on a free account.
- **"Commercial use rights" ≠ ownership.** Suno's language shifted from "you own your songs" to "you
  are granted commercial use rights." Purely AI-generated work is not copyrightable absent human
  authorship — **the more human contribution, the more defensible the release.** That is a direct
  argument for the demo-seeded / custom-model / stems-in-a-DAW workflow over pure prompting.
- **Lyrics you wrote remain yours** on any plan.
- **Disclose AI use** when distributors ask. Spotify's stated position is that disclosure *protects*
  a release from takedown rather than down-ranking it. Not every distributor accepts Suno output.
- **Master before release** — raw Suno output is quiet and will be buried next to commercial tracks.
- **Cover art: 3000×3000 JPEG**, no logos, URLs, social handles or price tags, or the release gets
  rejected.
