# Suno voices — how we get a specific voice, on purpose

> **Merged 2026-08-05.** Both working threads (prompt-side design + the eight-round audio war) are
> recorded below, and the distilled playbook now lives in the **`suno-prompt` skill** ("Getting a
> specific voice") — the skill is the operating procedure; this file is the deep reference and the
> evidence behind it. Builds on `files/suno-controls-and-workflows.md` §4 (the consistency stack)
> and `files/producer-vocabulary.md` (vocals section).

## The four places a voice lives

A "voice" isn't one thing in Suno — it's specified in up to four layers, and a session should be
deliberate about which layers it's using:

1. **The canon character file** (`docs/stories/<story>/characters/<name>.md`) — the `voice:`
   frontmatter is the source of truth for *who this is* ("New York, brassy and entitled — the
   'speak-to-the-manager' register"). Every downstream description derives from it.
2. **The Style box** — gender + timbre + delivery + **arc**, in producer vocabulary. This is where
   most of the control actually is.
3. **Lyric bracket cues** — per-section delivery direction (`[spoken, drop to one chord]`,
   `[flustered, close, panicking]`). Modulates the Style-box voice; can't replace it.
4. **The platform features** — saved Voice, custom model, Lyricist. For *recurrence across tracks*,
   not for getting the voice right the first time. See the consistency stack.

---

## Thread 1 — the Karen song ("All Day to Complain", 2026-08-05)

Context: a skit-structured hip-hop track — one lead (Karen) against an escalating ladder of
background phone voices, ending on AI Sean. Prompt-side design; not yet iterated against audio.

### Describe the voice as an arc, not a state

The single biggest upgrade between our first and second drafts. A static descriptor ("dry
conversational female voice") gets a generic vocal; giving it somewhere to start and somewhere to end
gets a performance — and for a character, **the arc is characterization**:

- Karen A: `drifting from chatty and warm to flat and hollow` — six weeks in a phone box, audible.
- Karen B: `sweet syrupy-polite, hardening to flat and bored` — the politeness is the weapon.

### Character words vs emotion words

Karen's register came out best when described by **behavioural delivery words** rather than feelings:
`polite, patient and completely immovable` says exactly how she sounds *and* who she is.
"Determined" or "frustrated" (emotion words) would have pulled the vocal toward strain — she is
never strained, that's the joke. When the character has a defining trait, find the delivery word
that *is* the trait.

### The comedy words corrupt the voice too

The satire trap isn't only an arrangement problem. "Comedic deadpan" in the Style box pushes the
*vocal* toward mugging and funny-voice delivery. A comic character sung straight is funnier: strip
comedy words, keep the deadpan in the delivery description (`dry`, `flat`, `unbothered`) and put the
humour in the lyrics.

### A cast of voices, and how to place them

For a track with more than one voice, the design questions are *who leads* and *where everyone
stands*:

- **The lead is the only voice fully described.** One detailed voice spec in the Style box; the
  background cast gets a collective placement clause ("muffled telephone voices answer from behind
  the beat, each one further away than the last").
- **Background dialogue goes in parentheses** in the Lyrics box — `( )` is performed as
  backing/secondary vocal, which is what renders the other side of a conversation as half-audible
  mutterings rather than a duet partner.
- **Expect 2–3 differentiated background voices per generation, no more.** A ladder of nine
  functionaries won't survive one pass. Keep the nearest rungs in-generation; build the rest as
  Sounds-tab spoken one-shots and layer in the DAW.

### Filter and distance are voice traits

The production treatment on a voice is part of its identity, and it can carry plot:

- Karen: `close mic`, dry — she is *with us*, in the booth.
- The functionaries: `narrow band-passed phone tone`, progressively further away — the system,
  receding upward. Per-voice phone EQ (done in the DAW on the one-shots) is how the escalation is
  *sold* to the ear.
- AI Sean: `deep, gravelly, close and dry — no phone filter`. The reveal is entirely in the
  treatment: everyone human was on the line; the AI isn't on the line, because it *is* the line.

### Voice specs travel from canon, and back

Karen's Style-box spec was derived from `characters/karen.md`'s `voice:` frontmatter, translated
into producer vocabulary. Direction that emerges during song work that isn't in the character file
(AI Sean's Ray Winstone register was in `story.md`, not a character file yet) should flow back into
canon — the character file is where the *next* medium (comic, video, another track) will look.

---

## Thread 2 — the Karen voice war (same song, iterated against audio, 2026-07-30 → 2026-08-05)

Context: the same track, but this thread fought the *generated audio* through eight rounds. Six
rounds of prompt surgery failed to move the lead vocal off a smooth, silky, "Lauryn Hill" default;
the voice finally landed via a **saved-Voice transplant**, not a prompt. Lessons in order of weight:

### 1. The genre tag owns the lead vocalist

The genre is the strongest word in the prompt, and it doesn't just pick the instruments — it picks
the **vocalist pool**. "Female + Boom Bap + half-spoken" has a centroid, and every generation
converges on it no matter what adjectives you stack: the descriptors are weak words fighting the
prompt's strongest word. Diagnostic: convergence at **both low and high weirdness**. Weirdness
perturbs *within* the genre's vocal pool; it never jumps pools. If the voice you want isn't in the
genre's pool, no amount of prompting reaches it — that's a transplant problem (see §3), not a
prompting problem.

### 2. The prior binds to the lead slot — the parenthesis slot escapes it

The breakthrough observation: a generation nailed the character voice **on the parenthetical intro
lines** (an answering-machine bit, before the beat established) and snapped back to the smooth
default the moment Verse 1 started. The genre's vocal prior attaches to *the lead slot inside the
groove*; the backing/secondary slot performing character lines is largely free of it. Consequences:
- A character voice that "won't generate" may already be generating — in the wrong slot. Listen for it.
- The parenthesis slot is effectively a **second cast member** with a different default identity.
  One generation carries only one saved Voice, but lead-plus-parentheses gives you two voices.

### 3. The Voice transplant — the mechanism that actually worked

When 2 rounds of style-prompt surgery haven't moved the vocal, stop prompting. The ladder:

1. **Probe-farm the voice in its home genre.** Generate the character where their voice is the
   *default*, not a fight (for a whiny complaining woman: comedy patter song / musical theatre;
   sparse piano). Real lyrics, **no parentheses** (every second becomes Voice material), spoken-word
   cues, and the target genre in the *excludes*. This doubles as a cheap capability probe: if the
   voice won't generate even in its home genre, only audio-seeding is left.
2. **Remix → Voice on the best take, selecting the sub-region** where the voice is right — 15
   clean seconds beat 60 contaminated ones, though up to 2 minutes makes a stabler clone.
   **Delete the attached style prompt** so the Voice isn't welded to one genre.
3. **Apply the Voice to the real track**: audio influence 40–60, raise to 70+ if it drifts
   (artifacts expected), then two-pass — Cover the right-voiced take at ~25–40 to recover fidelity.
4. **The floor that cannot fail: audio-seed a human.** 15s–4min of someone doing the voice into a
   phone mic, one consistent register, Voice → Create voice, audio influence 70–100, two-pass down.
   Perform the ownership-verification phrase in character; flat reading fails it.

### 4. Articulation beats attitude; onomatopoeia beats anatomy

Mood words ("put-upon", "brittle", "immovable") average into nothing — describe the **mouth**, not
the feelings: nasal, pinched, through the nose, flat hard vowels, over-enunciated consonants, a
rising whine at the end of every line. Better still, words that *sound like* the voice: honk,
squawk, kvetch, bratty, cartoonish. Reliability folk-tiers (practitioner-sourced): texture words
`raspy / breathy / gritty / husky` are top-tier; `nasal` and `whiny` are unlisted; **age descriptors
are mid-tier (~50–80%)** — "elderly/grandmother" moved nothing here. Naming a *performance
tradition* the model knows (comedy character actress, musical-theatre patter, sitcom squawk) beats
naming demographics.

### 5. Negation in the Style box describes the thing you're banning

`spoken word, not singing, no melody, no flow, no swagger` reads — to a model with no negation — as
a description of **a male rapper**, and produced exactly that: a male-voice leak on half the
generations. Naming `melody`, `flow`, `swagger` puts them in the prompt regardless of the word in
front. Negations go in Exclude Styles (negation is that box's whole job); the Style box gets
positive speech-act words (*complaining, nagging, scolding*).

### 6. Character limits are ceilings — a maxed box outvotes its own vocal

A 990/1,000-char style prompt with the voice as a third of it lost to its own arrangement detail:
Suno dilutes across everything named, so every clause about rimshots is a vote against the vocal.
Cutting to ~670 chars and deleting everything the genre tag provides free (drum furniture, EQ
minutiae) gave the voice clauses their weight back.

### 7. Every section cue must carry the character — and re-paste every box, every round

Two compounding traps. (a) A bracket cue with no vocal direction lets Suno fall back to the genre
default *for that section* — the character must appear in (nearly) every section header, and
repeating it in different words is the sanctioned escalation. (b) **The stale-box trap: four rounds
of style-prompt surgery ran against a Lyrics box still holding round-0 cues** ("deadpan…
unhurried"), because "Reuse Prompt" silently carries old lyrics forward. A stale lyric box is
inaudible as such — it just sounds like the style prompt is being ignored. Re-paste Style, Exclude,
Lyrics *and* My Taste every round.

### 8. My Taste is an upstream vocal spec — and it cannot be turned off

The profile-level "My Taste" text is applied to **every** generation, and ours contained a full
competing vocal identity (male Scouse grime MC — the Camping voice), explaining a male-voice leak
and dead descriptors (`adenoidal`, `rising intonation` were in *both* specs, so carried no signal).
Facts learned the hard way: the box **cannot be saved empty** — a profile can only be *replaced*,
never disabled; the "My Styles" toggle governs only the magic-wand suggestion button, not
generation bias; and the written profile is only the explicit half — Suno also learns from what you
create/like/dislike, uncontrollably (mitigate: thumbs-down every reject; one workspace per arc).
Working procedure: swap in a **per-track taste profile** that pulls the same way as the song
(Vocals field first), restore the house profile after. A single global profile is the wrong shape
for a catalogue with more than one narrator.

### 9. Cast the default instead of fighting it

Endgame move: once the Voice pinned the lead, the smooth silky vocalist we'd fought for six rounds
was **recast as a character** — the institution itself, a polished choir singing the functionaries'
answers "pretty as hold music, never her", against Karen's spoken whine. The wrong voice is often a
right voice for somebody else in the story. Two mechanical corollaries: the sung hook moves into
parentheses so the choir carries the melody and the lead never sings; and **once a Voice pins the
lead, strip the anti-smooth words from the excludes** — armour against a lead defect strangles the
backing vocals you now want.

### 10. Model choice inverts for cue-heavy skit tracks

The house move (generate on 4.5+ for vocal variety, Cover into 5.5 for sonics) failed here: 4.5
went haywire with the lyric structure; **v5.5 followed the bracket cues exactly**. For a track whose
architecture lives in dense per-section cues, structure-obedience beats vocal variety — stay on
5.5 and spend direction in the brackets, which it demonstrably honours.
