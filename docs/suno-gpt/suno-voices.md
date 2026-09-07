# Suno voices — how we get a specific voice, on purpose

> **Merged 2026-08-05.** Both working threads (prompt-side design + the eight-round audio war) are
> recorded below, and the distilled playbook now lives in the **`suno-prompt` skill** ("Getting a
> specific voice") — the skill is the operating procedure; this file is the deep reference and the
> evidence behind it. Builds on `files/suno-controls-and-workflows.md` §4 (the consistency stack)
> and `files/producer-vocabulary.md` (vocals section).
>
> 🔑 **Start at [Thread 5](#thread-5---the-talking-finding-camping-narration-2026-09-01--tested) if
> you want a man TALKING** — it is the one thread here whose headline finding is fully tested, and
> its headline is: **never ask for `spoken word`.** It also carries the third confirmation of the
> nationality trap in §2a, and the new "voice goes quiet as if waiting for a drop" failure sign.

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

---

## Thread 3 — the two-voice problem (GPOM drum & bass cut, 2026-08-08)

Context: the GPOM song forked into two cuts. The orchestral master's narrator is the best voice
we have and is about to become the saved Voice `BC-NEWSREADER`; the D&B sibling needs the *chorus*
to be somebody else. The question — can one generation carry a saved Voice on the verses and a
different voice on the chorus? — turns out to have a clean answer.

### 1. A saved Voice has no section scope. There is no such control.

Suno's Voices documentation says only that songs made with the feature "will use your voice instead
of a default Suno singer." It does not expose lead-vs-backing scope, per-section attachment, or more
than one Voice per generation, and it answers none of the three anywhere else. Practitioner guidance
is blunter: a Persona/Voice carries "vocal character and general delivery" across the track, and
stacking identity layers (Voice + custom model + My Taste + uploaded audio) "can create more
conflict, not more control" — the standing advice being to use *the smallest identity tool that
solves the problem*.

**So: attaching a Voice and then asking for a second, different voice in the same take is not a
supported operation.** Expect a blend. Plan around it rather than prompting at it.

### 2. The lead/parenthesis boundary is the only in-generation casting seam we have

This is Thread 2 §2 promoted from an observation to a working mechanism. The vocal prior — and, by
extension, an attached Voice — binds to the **lead slot inside the groove**. The
**parenthesis/backing slot escapes it**. That gives every generation exactly **two castable slots**:

| Slot | How you write it | What it's for |
|---|---|---|
| Lead | unparenthesised lines in the groove | the saved Voice / the character you're pinning |
| Backing | `( )` lines | the *other* voice — and the only place it can safely live |

Corollary for song design: **whichever voice you are cloning goes in the lead; the other one goes
in parentheses, whatever its narrative importance.** On Karen, that meant the sung hook moved to
the parentheses so the institution's choir carried it and the lead never sang. On GPOM D&B it
means the *chorus* — the title hook of the song — lives in parentheses, sung by schoolchildren,
while the narrator holds the lead and never touches it.

### 3. Cast across *categories*, not across adjectives

The strongest predictor of whether two voices stay separate is how far apart they are in kind. Two
descriptions of one solo adult male ("gravelly" vs "robotic", "calm" vs "furious") sit close enough
in the space that the model will average them — which is exactly what happened when GPOM's chorus
was a vocoded robot against a gravelly narrator, twice, both times retired.

A **room of children** against **one close-mic'd adult man** cannot average — they are different
vocal categories, not different adjectives on the same one. Reach for a category jump (solo → crowd,
adult → child, human → instrument) before reaching for a stronger adjective.

Related: robotic/vocoder vocals are a *bad* target for this, and there's a mechanistic reason.
Practitioner guidance reports that robotic-sounding vocals are typically what Suno produces **from
conflicting vocal tags** — it's the failure texture. Asking for it deliberately means asking for the
thing the model emits when confused.

### 4. Treatment and distance are casting, not mixing

Cheap and reliable, and it works before any timbre argument lands: give each slot its own space.
Close-mic'd and dry against roomy and distant reads as *two different people in two different
rooms* even when the timbres are neighbours. (Karen used the same lever for plot — the phone-filter
ladder, with AI Sean's reveal carried entirely by the absence of a filter.)

### 5. Splitting a register out of a character makes their clone better

Non-obvious payoff. The one-register rule says a Voice must be cloned from a single consistent
delivery. A character asked to do two registers in one song (GPOM's narrator: spoken bulletins *and*
a booming chant) is therefore a worse clone source than one who does a single register throughout.
**Recasting the second register onto somebody else doesn't just fix the casting — it purifies the
clone's source material.** Worth checking whenever a lead is being asked to do two things.

### 6. The lead/backing seam is per *line* — and parentheses are a bias, not a bind

Added 2026-08-08 from GPOM's D&B cut; **corrected the same day** after an adversarial review caught
the first version overstating it.

> **Bounded 2026-08-20 by Thread 4 §1 — read that before applying this at scale.** Everything below
> was observed on a **four-line** chorus. Camping tried the same lever across a **sixteen-line
> verse** and it failed: parentheses state a position in the *mix*, not an identity, so a section
> with no lead line to answer gets the lead filled in line by line. **Short answer lines against a
> present lead — not a whole verse.**

The observed facts, across many takes: with **all four** chorus lines parenthesised and a section
cue explicitly silencing the lead, the crowd took the three short slogan lines reliably — and the
fourth line, the only long syntactically-complete clause, went to the *lead* voice anyway, every
take. Two findings follow, one of which corrects this entry's original claim:

- **The seam is per line.** Casting is decided line by line, not per section, so genuine
  call-and-response is available inside one section, in one generation, with no second Voice:

  ```
  (slogan line — crowd)
  (slogan line — crowd)
  (slogan line — crowd)
  answer line — lead
  ```

- **But punctuation biases; it does not bind.** The original entry called this deterministic
  ("just punctuation"). The observed leak went *through* a parenthesis. Parens are the strongest
  per-section casting lever the platform has — short chant-shaped lines hold near-perfectly — but
  a long complete clause reads as a lead line and gets claimed by one. **Line shape is itself
  casting**: if a line must belong to the crowd, make it slogan-shaped; if it stays a sentence,
  expect to re-roll for it, or drop an inline cue (`[all voices together]`) directly above it.

A third observation worth as much as either: **the backing slot does not mean background.** GPOM's
parenthesised choruses rendered as full-weight drops. The slot decides *who owns the line*; the
section cue and arrangement decide how big it is. Don't strip parens to make a chorus "the
protagonist" — that trades the casting mechanism for nothing the cue wasn't already providing.
(GPOM tried exactly this in round two and reversed it on review before generating.)

Two practical corollaries:

- **Give the lead the line that suits its register.** GPOM's lead line is the driest, most clinical
  one in the hook, which is why the handoff reads as authorial rather than arbitrary.
- **It's also a swearing valve.** Profanity assigned to the parenthesised crowd keeps a narrator's
  composure intact while the song still swears — the fix for "that voice shouldn't be saying that"
  is usually reassignment, not rewriting.

### 7. An ironic vocal choice is the satire trap wearing a different hat

GPOM's chorus was first cast as schoolchildren — kids deadpanning the news, the *Another Brick in
the Wall* move. It read beautifully in the design doc and generated wrong: Suno has one dominant
register for a children's choir and it is **school assembly** — sweet, thin, twee, well-behaved. It
fought the dread instead of deepening it.

The general lesson, and it's the vocal-casting twin of the satire trap in the skill: **a concept
being funny or chilling *in description* is not evidence the model can render it that way.** Where a
vocal category has one strong wholesome prior, irony is not reachable by stacking adjectives on it —
the prior wins, exactly as the genre's vocalist pool wins over voice adjectives (§1).

Two rules that fall out:

- **Cast performance traditions, not demographics or concepts.** "Gospel choir", "cathedral choir",
  "football-terrace chant" are traditions the model has heard performed and can play straight. "A
  room of ordinary people", "a crowd of workers" have no prior to land on and average into nothing.
  (This is §4's "name a performance tradition" rule, applied to groups rather than soloists.)
- **When a cast choice fails on *tone* rather than identity, replace the category, don't adjust it.**
  The children generated reliably — the casting was simply wrong. Adding `dark, flat, deadpan` to a
  wholesome prior buys very little; moving to a category whose default is already grave buys
  everything.

### 8. The Exclude box is global — it cannot protect one section from another's voice

The corollary to §6, and the thing that makes the parenthesis seam so valuable. Excludes have **no
section scope**. On a track whose verses are a solo male narrator and whose chorus must be a crowd,
you cannot ban `solo male vocal` to defend the chorus — it strips the verses too. The Exclude box
can only ban things that appear *nowhere* in the track.

So when two voices compete for one slot, the levers are, in order: re-roll; escalate the wanted
voice in the section cue; push the two apart with **treatment and distance** (close/dry vs
far/reverberant), which is per-section because it lives in the cue; and finally the parentheses,
which are the only genuinely *mechanical* per-section vocal control the platform offers. Reaching
for the excludes here is a category error that quietly damages the part of the song that was working.

### 9. Weirdness follows the same rule as model choice: cue-heavy tracks want obedience

The house default is weirdness 60–65, the "creative sweet spot". GPOM's D&B cut tested materially
better at **30**. That isn't a contradiction of §10's model finding — it's the same finding:

> When a track's architecture lives in dense per-section bracket cues, every control should be set
> toward **obedience**, not variety. That's why v5.5 beats 4.5 on these tracks, and it's why low
> weirdness beats the creative sweet spot.

Weirdness perturbs *within* the pools the prompt selects (§1), so on a track where the prompt is
doing precise structural work — this voice here, that voice there, this section drops cold — the
perturbation has nothing to add and plenty to disturb. Reserve 60–65 for tracks where you're
shopping for a feel rather than executing an arrangement.

### 10. Delivery speed is syllable density per *line* — *moved*

**This finding now lives in [`files/lyric-craft.md`](./files/lyric-craft.md)** → "Punctuation is
the brake — the timing table", which is where a lyricist will look for it. It is not a voice-identity
finding; it is lyric delivery.

One line of it belongs here, because it bears on casting: **merging short lines into long ones
reduces lead-slot leakage.** A short standalone line containing a complete clause reads as a lead
answer and gets claimed by the lead voice; the same clause absorbed into the tail of a long rushed
line does not. See §6.

### 11. Two performance traditions in one clause do not average — the dominant one wins

GPOM asked for a crowd "somewhere between a gospel choir and a football terrace." What came back was
a gospel choir: high, sung, operatic. §7 established that naming a *performance tradition* beats
naming a demographic; the refinement is that **you get to name exactly one.** Where two are named,
the more musically dominant — the trained ensemble over the untrained noise, the pitched over the
shouted — takes the generation.

If a hybrid is genuinely wanted, make one the noun and the other its adjectives (`a gospel choir of
hundreds of untrained ragged voices, massed like a football terrace`) rather than asking for a
midpoint. And count the nouns: a single choral noun (`choir`, `congregation`, `cathedral`, `hall`,
or the verb `singing`) will out-vote several rough adjectives, especially when an orchestra elsewhere
in the prompt is pulling the same way.

---

## Thread 4 — the Camping duet (2026-08-20)

Context: "Camping" is a two-hander — Bob (weathered Scouse) and Tarquin (posh London) — released
with a saved Voice attached, which made both men the same performer. This thread is the re-cut that
tried to separate them. **Round 1 generated and failed on three counts, which makes most of what
follows *tested* rather than asserted** — rare in this corpus, and it is why these entries outrank
the blog-sourced material in `files/lyricist-playbook.md` §4 where they disagree.

### 1. Parentheses are a mix-position mechanism, not a name tag — and they don't scale to a verse

**This bounds Thread 3 §6.** That entry established the lead/paren seam as per-line and called
parens "the strongest per-section casting lever the platform has." It was derived from a **four-line**
GPOM chorus. Camping tested the same lever across a **sixteen-line verse** and it broke down: the
voice ping-ponged *within* the verse instead of holding Tarquin for it.

The mechanism explains why. Parentheses mean **"backing singer standing slightly back from the
mic"** — Suno drops the level, adds spatial reverb, shifts the pitch. It is a statement about
*position in the mix*, not about *identity*. So a section of nothing but parenthesised lines is a
section of nothing but backing lines, and the lead slot — which does not go away — gets filled by
whatever is nearest, in and out, line by line.

**The working rule:** the paren slot holds a **short answer line against a present lead**. It cannot
carry a whole verse that has no lead to answer. If a character needs a section to themselves,
parentheses are the wrong tool, and reaching for them harder makes it worse (§3).

### 2. Regional accent does not render. Contrast on pitch and texture instead

A detailed Scouse spec — adenoidal Merseyside drawl, softened hard consonants, rising sing-song
line ends — produced **no accent whatever**. This is Thread 2 §1 again (the genre tag owns the
vocalist pool) with accent added to the list of weak words alongside age: *describable, not
summonable.*

The replacement, and it is the practical takeaway of the whole thread — **cast on axes the model
renders readily**:

| Axis | Why it works |
|---|---|
| **Pitch** — low/deep vs higher/light | The most mechanical contrast available; renders near-always |
| **Texture** — gravelly, torn, smoke-worn vs clean, crisp, smooth | Ordinary timbre vocabulary, well represented in training data |
| **Delivery mode** — rapped on the grid vs spoken behind the beat | A category difference, not an adjective difference (Thread 3 §3) |
| **Room** — close and dry vs wide and reverberant | Treatment and distance are casting, not mixing (Thread 3 §4) |

Four axes stacked put two solo adult men genuinely far apart without ever naming a region. Accent
is a thing you write in the **canon file** and hear in your own head; it is not a thing you order
from Suno.

### 2a. But nationality rides on the *genre tag* — and stripping accents can strip it by accident

**The trap that follows directly from §2, and we walked into it.** Round 2 removed every accent word
and both men came back **American**.

The released take had carried `dark neurofunk with **UK grime influence**` in the genre stack.
Round 2's rewrite dropped it while cleaning out the accent language. The Britishness had never been
coming from "adenoidal Merseyside" or "clipped RP" at all — it was coming from the **genre**, which
owns the vocalist pool (Thread 2 §1). Take out the UK genre and the pool reverts to its default,
which is American.

Three rules:

- **Nationality is a genre lever, not an adjective lever.** `UK grime`, `UK garage`, `grime`,
  `UK hip hop` are the strongest British-vocal controls available, because they are pool-selecting
  words. `British` is a weak adjective by comparison — useful as reinforcement, useless alone.
- **Front-load the UK genre**, and let `British` repeat several times after it. Redundant
  reinforcement is a real technique for a term being ignored.
- **When you strip a failing spec, check what else it was quietly holding up.** The accent language
  was dead weight *and* load-bearing at the same time: dead for the region, load-bearing for the
  nation, because the genre tag was sat in the same clause.

🔴 **Confirmed a third time, 2026-09-01 — see Thread 5 §4.** Camping's narration replaced
`Northern English post-punk spoken word` with `Trip hop skit` to kill the poetry noun, and came back
**American** — with four American bans sitting in the Exclude box the whole time. Two things that
adds to the rules above: **Exclude-box bans do not control nationality at all**, and **`trip hop` is
too weak a British lever to survive `skit`'s US hip-hop gravity.** The lever that is worth trying
next is a British **place or scene name in genre position** (`Madchester`), which is externally
reported to move accent where a bare adjective does not.

### 2b. A genre tag carries a whole *performer*, not one attribute — pick the tradition, not the nationality

**The trap on the other side of §2a, walked into one round later.** `UK grime` fixed the
nationality and immediately miscast both men: Camping came back sung by young Black British MCs,
when Bob is a weathered fifty-something white homeless Merseyside man and Tarquin a late-forties
white City banker — both of whom **we have comic panels of**.

The rule: **a vocalist pool is a person, not a property.** Accent, age, class and race arrive
together as one package, and choosing a genre for one of them means accepting its defaults for all
the rest. There is no such thing as borrowing a genre's nationality without its performer.

**So choose the genre whose default performer *is* your character.** For a middle-aged white
British man ranting over a beat, `British post-punk spoken word` is the pool — every bit as British
as grime, and the right bloke. It also keeps our own **cast performance traditions, not
demographics** rule (Thread 3 §7) intact: naming a tradition the model has heard performed does the
casting precisely, and no demographic adjective ever has to go in the prompt.

**A starter map for BadCode's British registers:**

| Character | Pool that casts them | Not |
|---|---|---|
| Weathered working-class British bloke, 40s–60s | British post-punk spoken word; Britpop snarl; British performance poet | grime, drill, road rap — young MC by default |
| Posh / establishment British | BBC English, newsreader, after-dinner speaker | "posh" alone, `clipped RP` — register words without a tradition |
| Young British street voice | grime, UK drill, road rap | — this is where grime is *correct* |

**Cross-medium corollary, new and load-bearing for us:** when a character already exists as an
**image** — a comic panel, a character sheet — the voice has to match the picture, and "sounds
British" is not the bar. Check a generated voice against the character sheet, not just against the
style prompt. A song and a comic that disagree about who someone is will read as two different
characters.

**Class register survives where regional accent doesn't** — name it as a *performance tradition* the
model has heard: `BBC English`, `newsreader`, `after-dinner speaker` land where `clipped RP` and
`Scouse` don't. This is Thread 2 §4's "name a performance tradition" rule, applied to class instead
of to genre.

### 3. More casting markup makes casting worse

Round 1 answered a casting problem by adding casting markup to every line. That is the exact
failure the external guidance names — *"adding more labels can sometimes make a duet worse"* — and
it is now corroborated by a take we generated. **Treat dense per-line voice markup as a smell, not
a fix.** One fixed short label per character, repeated **identically** (`[low gravelly voice]`,
`[high clean voice]`), beats a freshly-worded description each time: varied wording reads as a new
character.

### 4. Cue density has a tempo cost — the playbook's warning gets its first observation

Round 1 carried a bracket cue roughly every two lines and **broke into double time** for a stretch.
Two suspects, not separated: syllable cramming (the documented machine-gun rush, `lyric-craft.md`),
and cue density chopping a verse into micro-sections that each re-decide their own phrasing.

This matters because `files/lyricist-playbook.md` §3 warns against dense multi-clause cues and is
flagged there as *contradicting BadCode house practice*. **It now has a supporting observation.**
The house style isn't overturned — GPOM's dense cues produced a track we like — but "cue overload"
graduates from a named suspect to a suspect with a case, and **a tempo fault is now a reason to
strip cues before anything else.** `[Beat Transition]` between sections is the cheap reset.

### 4a. A tempo fault is usually a *consistency* fault, and the fix is line breaks

Round 2/3 came back rushed, with lines "not starting at the start of the bar". Measuring the sheet
turned a vague complaint into a number: **only 5 of 48 lines were over the density ceiling.** The
problem was the **spread**, not the speed.

The rule doing the damage is in [`files/lyric-craft.md`](./files/lyric-craft.md): the first line of
a section sets the bar length, and every later line is force-fit into that slot. Camping's bridge ran
**9 → 15 syllables** against a 12-syllable opening line, so the long ones crammed. Cram is what
"rushed and off the bar" sounds like.

**Measure before prescribing.** Count syllables per line, per section, and look at the *range*. A
section with a spread of 6+ has a timing problem waiting whatever its mean. This takes one throwaway
script and it converts an unactionable note ("feels rushed") into a list of specific lines.

**Line breaks are the tempo control, and they change no words** — which makes them the right lever
whenever a lyric is locked (a released track, someone else's words, a re-cut). Splitting a
15-syllable line into 7 + 8 halves the density *and* buys a second phrase. Reach for this before
commas and long before the Style box.

**The asymmetry that decides which way to err:** a short line gets **stretched**, which sounds
deliberate; a long line gets **crammed**, which sounds broken. Break shorter when unsure.

**Also a stress problem, not only a density one.** Lines opening on a run of unstressed function
words (*"and you looking to…"*, *"in having the manager…"*) are pickups: the model starts them early
or crams them to force the stress onto the downbeat. This is why lines inside the safe band still
land off the bar.

**Multiple spaces are not a pause mechanism** — worth knowing because it is an intuitive thing to
try. The vocabulary that works is comma / full stop / line break / ellipsis / in-word hyphen.

**The ceiling is honest: the sheet gets phrasing close, Studio gets it exact.** Warp markers +
Quantize (and `Clip Settings → On Beat`) are the post-generation answer to a line that will not sit
on the grid. Re-roll first — phrasing varies between takes on an identical sheet.

### 5. Ask whether it is actually a duet before reaching for duet machinery

The most useful realisation of the thread, and it is structural rather than technical. Camping
*looks* like a two-hander but is really **two solo verses separated by a 32-bar instrumental drop**,
plus one traded bridge. The verses never overlap — so there was never a two-voices-in-one-section
problem to solve there, and every lever spent on it was wasted.

**Check the song's shape first.** Where two characters share a section, you have a casting problem.
Where they merely take turns across an instrumental, you have **a seam you can cut on** — and
cutting is strictly better than casting, because the voices never share a generation and there is
nothing to average.

Corollary: a genuinely traded section (Camping's bridge) is *short alternating complete lines*,
which is the one duet shape the external guidance calls easiest to stabilise. So the hard-looking
part is the tractable part, and the easy-looking part is where you cut.

### 6. A saved Voice is right for one-voice-per-generation, and wrong for anything else

The released take's root fault. A Voice binds the lead slot for the whole track and has **no
section scope** (Thread 3 §1) — external sources put it plainly: *"a Persona is not a separate
singer lane."* Attaching one to a two-hander guarantees one performer.

But the inverse is the good news: once the song is **cut into one generation per character**, a
saved Voice per character is exactly the supported case and the strongest version of the plan.
**The Voice wasn't the wrong tool; it was the right tool on the wrong unit of work.**

### 6a. Arrangement is casting's neighbour — hold the band back the way you hold a voice back

Not a voice finding, but it surfaced in the same thread and the mechanism is the one
this file keeps rediscovering: **naming a thing puts it in the track, and describing a
quiet version of it still names it.**

Camping's orchestra was asked to arrive at the drop. It arrived at bar one — twice —
because (a) a strings paragraph sat in **My Taste**, which has no section scope, and
(b) the lyric sheet carried a lead-in cue, `[one low cello note holds underneath,
building into the drop]`. The lead-in reads as *these instruments exist*, and existence
defaults to bar one.

**The fix that worked was subtraction:** strings removed from My Taste entirely, the
lead-in cue **deleted** rather than moved, and the entrance stated once in the Style box
and once in the drop cue. **Delete the mention; don't describe the absence.**

The second half of it is that a reveal needs something to reveal. Camping's verse-one
header asked for `amen break + deep sub`, so the verse and the drop were the same
weight and the drop had nowhere to go. The arrangement now climbs in **gears** — no
drums → loose kit with no sub → full weight *and* the strings together — so one moment
carries two reveals.

Full detail, with the transferable recipe, is in
[`files/suno-tag-mechanics.md`](./files/suno-tag-mechanics.md) under the unity sentence.

### 7. What we still don't know

Round 2 (texture contrast, zero parentheses, one cue per section) is **drafted and ungenerated** —
see [`../stories/camping/songs/camping.md`](../stories/camping/songs/camping.md). Open
questions it should settle: whether stripping cues fixes the tempo; whether the four-axis contrast
separates two solo verses without any slot mechanism at all; and what stripping the cues costs in
delivery. Update this thread with the answers.

### Sources

External guidance quoted above, harvested 2026-08-20:
[multiple Personas in one song](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/can-suno-use-multiple-personas-duets-bands-ai-casts) ·
[duet & harmony guide](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/duet-harmony-theme-meta-tags-suno) ·
[brackets, vocal tags & lyric formatting](https://paddystudio.com/blog/suno-song-structure-and-vocal-tags/).
All assertion-grade; the round-1 failures they agree with are ours and are tested.

---

## Thread 5 — 🔑 The talking finding (Camping narration, 2026-09-01) — **TESTED**

**This is the most transferable thing in the file, and it took ten rounds to see.** If you want a
man **talking** over music, everything above about pools applies — but the pool word almost everyone
reaches for first is the wrong one, and it fails the same way every time.

### 1. 🔴 Never ask for `spoken word`. Ask for a man talking over a beat.

**`spoken word` is not a delivery mode. It is a performance-poetry genre** — slam, dub poetry,
performance poetry — and its canonical delivery is metrical, end-stopped and declamatory. Ask for it
and you get a poem, read like a poem, every single time.

| Rounds | What was in the boxes | Result |
|---|---|---|
| **1–9** | `spoken word` in the Style box, in My Taste, and in all 29 bracket cues — **33 mentions** | 🔴 **A poem.** Nine rounds of adjective surgery around the noun; the noun was never touched |
| **10** | **No `spoken word` anywhere.** `Trip hop skit, a man talking over a beat`, prose lyrics under `[Monologue]`, the whole poetry pool in the Exclude box | ✅ **He talked.** Jack: *"ten times better"* |

🔑 **The reframe that fixed it: Suno cannot make silence, so stop fighting for a cappella and ask
for a form that actually exists.**

| What you ask for | What is in the training data | What you get |
|---|---|---|
| A man talking over **nothing** | Poetry recordings, almost exclusively | **A poem** |
| A man talking over **a low loop** | Skits, album interludes, spoken intros, radio drama, documentary VO — enormous | **A bloke talking** |

**So the beat is not a cost, it is the casting mechanism** — and it is usually free, because
narration comes out as a **vocal stem** anyway (`files/suno-controls-and-workflows.md` §9). Nine
rounds were spent paying casting damage to avoid an instrument we throw away.

**The rule that replaces the a-cappella fight: MELODY makes him sing; RHYTHM does not.** Tested on
this same story — the round-4 singing came from a glockenspiel and a French horn, not from a drum.
**Keep every pitched instrument banned; take drums off the ban list.**

### 2. The recipe, in four boxes

| Box | What goes in |
|---|---|
| **Style** | A **skit / interlude** pool word, `a man talking over a beat`, a BPM, one unpitched bed, `voice-forward mix, no singing, no melody`. **No genre word containing "spoken" or "word."** |
| **Exclude** | 🔑 **The whole poetry pool, explicitly**: `spoken word, performance poetry, poetry slam, dub poetry, beat poetry, recital, recitation, declamatory, oratory, verse, stanza, rhyming, metrical, incantation, dramatic reading, elocution` |
| **Lyrics** | **One label, `[Monologue]`, repeated identically** — a talking word with no genre attached. Then **continuous prose paragraphs**, natural punctuation, no rhyme, no parentheses |
| **My Taste** | The same speech act stated first: *he is TALKING — not singing, not rapping, not reciting* |

### 3. 🔴 The layout votes as hard as the wording, and nobody looks at it

**Suno reads a line break as a phrase reset and a section break as a musical event.** So a script
laid out one line per bracketed section, blank line either side, gets *landed, paused and restarted*
line by line — **which is the slam cadence, drawn as a page.** Camping had 29 of them. No wording
fixes that.

**Continuous prose paragraphs under one label** is the fix, and it is corroborated: the Jack
Righteous 2026 narration workflow prescribes *short sentences with natural punctuation · minimise
rhyme · paragraph breaks between ideas · no verse structure · write conversationally rather than as
song lyrics.*

⚠️ **This retires the escalation ladder** `[spoken word]` → `[spoken word speech]` →
`[spoken word speech talking]` **for narration** — it escalates the poison noun. The lateral ladder
that replaces it: **`[Monologue]` → `[Spoken Word Narration]` → `[Interlude]` → no label at all.**
`files/suno-tag-mechanics.md`'s all-parentheses spoken-word recipe is superseded for narration too;
parentheses triple-voted for declamation.

### 4. 🔴 What the skit pool does NOT fix: nationality — §2a, for the third time

**Round 10 came back American**, with `American accent, American vocal, transatlantic, southern
drawl` all sitting in the Exclude box and `Northern English working-class man` in the Style box.

**Both of those are the weak levers.** This is §2a again, and the trap is identical: round 10
replaced `Northern English post-punk spoken word` — a **pool-selecting** phrase that was doing
*all* the accent work — with `Trip hop skit`, and only the *poetry* half was supposed to go. The
Britishness went with it.

Three things this settles:

- 🔴 **Exclude-box bans do not control nationality.** Four American bans were in place and it came
  out American anyway. Nationality is a **genre lever**, full stop.
- 🔴 **`Trip hop` is not a strong enough British lever**, despite being Bristol by origin —
  and **`skit` carries US hip-hop gravity** that appears to beat it. A weak British word in front of
  a strong American one loses.
- ✅ **Front-load a British *place or scene* name in genre position.** Corroborated externally:
  *"adding a geographical location can dramatically influence the accent and delivery."* This is why
  `Madchester` behaves differently from `northern English` — one is a pool, the other is an adjective.

**The northern-bloke pools, updated, with the poetry ones now disqualified for narration:**

| Want | Pool | Why not the obvious one |
|---|---|---|
| Weathered northern working-class bloke, **talking** | **`Madchester skit`** — a place-name scene whose default performer is a northern working-class man half-talking over a loop | `British post-punk spoken word` is the right bloke but carries the poison noun |
| The same man, if Madchester grows a guitar band | `UK hip hop skit`, `British rap skit` | ⚠️ §2b applies — these cast a **young MC** by default |
| Posh / establishment British | `BBC English`, `newsreader`, `after-dinner speaker` | unchanged |

### 4a. 🔴 The Exclude box votes on nationality too — and it can outvote the Style box

**Round 11 changed the front word to `Madchester skit` and came back American anyway.** The Style box
was not being ignored. **It was being outvoted, by the box nobody re-reads.**

| | |
|---|---|
| British-coded words in the **Style** box | **3** — `Madchester`, `British`, `northern English` |
| British-coded words in the **Exclude** box | 🔴 **37** |

The ban list had grown across eleven rounds into a dense, specific statement of *not British*:
`music hall, vaudeville, pantomime, panto, cabaret, variety show, oompah` (British comedy),
`RP, received pronunciation, BBC newsreader, after-dinner speaker, posh, plummy` (British class),
`grime MC, UK drill, road rap` (**three of the four strongest British-vocal pools we have**),
and `indie rock, guitar band, post-punk band, band, rock band, live band, guitar, jangly guitars` —
plus, self-cancelling and added in the very same round as the Style-box fix, **`Madchester baggy`**.

🔑 **We banned the pool's entire sonic signature and then asked for the pool.** Suno resolved the
contradiction the only way it can: it dropped the pool, and the vocalist reverted to the default,
which is American.

**Three rules out of it:**

- **A ban is a category vote, not a subtraction.** The stale-ban rule in `files/suno-tag-mechanics.md`
  already said to grep the Exclude box for *the thing and its category*. This extends it: **grep for
  the thing's whole cultural family.** Nationality has a family; so does era, and so does class.
- 🔑 **Count both boxes before blaming the Style box.** If the Exclude box holds more words from a
  family than the Style box does, the Style box loses. It is a one-minute check and it would have
  saved two rounds here.
- **Never ban a genre adjacent to the pool you are casting.** Banning `indie rock` to keep guitars
  out of a `Madchester` prompt is banning Madchester. **Take the instrument risk instead** — when
  narration ships as a vocal stem, an unwanted band is an inconvenience; a wrong accent is a dead
  take.

### 4c. 🔑 The accent audit — count what NAMES the wrong nationality, in **all four** boxes

**Round 12 fixed the Exclude box and round 13 found the Style box had been carrying an American word
in genre position the whole time.** §4 above convicted `skit` — *"`skit` carries US hip-hop gravity"* —
and then the sheet kept `Madchester skit` for three more rounds. **A British place name welded to an
American form-word is the conflict, not the fix for it.**

**The audit, run on every box at once. Do this before touching a single word.**

| What to grep for | Camping's American hits |
|---|---|
| **Scene / place names** | — |
| 🔴 **Form words** — the words for *a kind of track* | `skit` (Style, genre position) |
| 🔴 **The form's own phrasing** | `a man talking over a beat` — *over a beat* is hip hop's own phrase |
| 🔴 **Production slang** | `dusty` drum loop — US boom-bap / crate-digging vocabulary |
| **The literal country adjective**, incl. in Exclude | `American accent, American vocal, transatlantic, southern drawl` |
| **Adjacent-genre bans that name the family** | `US rap, young MC, rapping, bars, flow, trap` |

**Then weight the count — position decides, not frequency.**

| Strong | Weak |
|---|---|
| Genre position (the first two or three words) · the form word · production vocabulary | **Nationality adjectives anywhere** — `British`, `northern`, `Manchester` as a description. §2a and §4 both record these as buying nothing |

🔑 **Camping round 12 scored 3 strong American to 2 strong British**, with `Madchester` in the box and
five British-coded words on the page. It read as *British with an American accent problem*; it was
**an American prompt with British adjectives on it.**

**Three rules out of it:**

- 🔴 **Never weld a foreign form-word to a native pool word.** `Madchester skit`, `UK hip hop skit`,
  `British rap skit` — the pool word and the form word are in the same slot and the model does not
  average them, it picks (Thread 3 §11: *two performance traditions in one clause do not average*).
  Find a form word from the same culture, or a nationality-neutral one.
- ✅ **`monologue` is the neutral talking form-word.** No nationality, no poetry pool, and it matches
  the `[Monologue]` lyric label — so the Style and Lyrics boxes reinforce each other for free. ⚠️
  Untested as a *replacement* for `skit`; `skit` is the tested word that got a man talking, so
  deleting it risks the poem coming back. Revert target, not a free swap.
- 🔴 **A ban that has failed three times is not free — delete it.** `American accent, American vocal,
  transatlantic, southern drawl` sat through rounds 10, 11 and 12 and he was American in all three.
  Either §4 is right and they cannot reach nationality, or §5 is right and they are *naming America
  four times*. Both readings say cut.
- 🔴 **Never spend a ban from one axis on a word from another.** `mumbling, muttering, trailing off`
  were banned to fix a **loudness** fault (§5) and were quietly banning the **articulation** —
  slurred, swallowed, drooping *is* the Manchester delivery being asked for. Ban the axis that broke.

### 4b. `deep` is a trap in both directions

Rounds 1 and 4 came back **too low**, so the depth words were banned. Round 10 lifted the ban because
Jack asked for "an interesting northern English deep voice". **Round 11 came back too deep again.**

**The resolution: `deep` is not the word for what was wanted.** What was wanted was *weight and
grain* — which are **texture** words (`rasp`, `grit`, `sandpaper`), not **pitch** words. `deep` is
back in the Exclude box permanently, along with `chest voice` and `growl`, and the pitch clause now
says **`mid-range`** explicitly.

⚠️ **And watch the word `level`.** Round 11 fixed the ducking with `exactly the same level start to
finish`, meaning *loudness* — but `level` is a pitch word too, and `flat`/`level` are exactly what
caused the round-5 monotone. **State loudness as loudness**: `never gets louder, never gets quieter`.

### 5. New failure sign — **"the voice goes quiet, as if waiting for a beat to drop"**

Round 10's second fault, and it is an **arrangement** fault, not a vocal one.

**Cause: the pool word names a *section*, and a section leads somewhere.** `skit` and `interlude`
both literally mean *a short thing between the songs* — so the model builds toward whatever it thinks
comes next, ducking the voice for tension on the way. Trip hop's own dynamic-swell grammar compounds
it.

⚠️ **It is not the default behaviour** — external guidance is that Suno gives *"flat verse at
constant volume"* unless a build is tagged. So the build was **asked for**, by a style word, which
means the fix is in the Style box and not in a new tag.

**The fix, in three parts:**

1. **Style box, positive form:** `one dusty drum loop, unchanging, exactly the same level start to
   finish` + `voice loud and in front the whole way`.
2. **Exclude box:** `build, buildup, riser, drop, beat drop, breakdown, crescendo, decrescendo,
   swell, fade in, fade out, quiet passage, sparse breakdown, half time, dynamic build, tension
   build, pre-drop, vocal ducking, distant vocal, buried vocal, mumbling`.
3. **Only if 1 and 2 fail — the untested lever:** `[Energy: High]` on the section start is reported
   to lock the vocal level. Assertion-grade, one source. ALL-CAPS as a volume control is reported by
   the same source as *"less reliable than ellipsis"* — do not reach for it, and note our Exclude box
   bans `shouting`.

### 6. 🔑 Rhythm makes him RAP — the melody-not-rhythm rule, corrected

**Round 14, Camping. The voice was finally right and the delivery was still wrong:** *"it still
sounds like he is saying it to a beat, instead of just talking."*

🔴 **§1's rule was half true.** It read *"MELODY makes him sing; RHYTHM does not"*, and it was written
to justify lifting the drum bans so the skit pool could cast a talker. It worked — and it hid the
other half:

> **Melody makes him sing. Rhythm makes him rap. Narration wants neither.**

A man performing to a bar is the same fault as a man reciting a poem: **a performance, not speech.**
The skit recipe traded the poem for the bar and called it done.

**Three things declare a grid, in descending strength:**

| | |
|---|---|
| 🔴 **A stated BPM** | A number in the Style box **is** a grid. The community field guide's own phrasing is *"**lock** BPM and key in the style field, and reuse the same values for every generation"* — it is the anchor you set when you want sections to splice on the beat. For narration it is a metronome you asked for |
| 🔴 **A drum loop of any kind** | A metronome with a tone |
| 🟡 **Music-scene pool words** | Their native vocal sits on the bar. **Never trade these** — they are the accent (§4c) |

#### ✅ The fix is a third option: not silence, not a beat — a **bed**

⚠️ **Deleting the bed is the wrong move** and it walks straight back into the poem (§1): *a man
talking over nothing* barely exists in the training data. **Every practitioner narration template we
can find uses an UNDERSCORE instead** — a low, non-metrical ambient bed — and **not one of them puts
a drum under it.**

| Style box | Exclude box |
|---|---|
| 🥇 **`free pacing`** — the corpus's one direct anti-grid phrase, from a worked narration template · `pausing where the meaning breaks and never on a bar` · `one low ambient underscore, no pulse and no rhythm` · **no BPM number at all** | the whole grid family: `drums, drum kit, drum loop, percussion, breakbeat, beat, kick, snare, hi-hats, groove, four to the floor, pulse, metronome, quantized, on the beat, in time with the beat, rhythmic delivery, cadence, syncopation, bars, rap flow`. 🔴 **Leave `underscore, ambient bed, drone, room tone` UNBANNED** — that distinction is the whole fix |

🔴 **And grep the Exclude box for every noun in the new Style box, before pasting.** Round 14 asked
for `one low ambient underscore` while **`underscore` was banned** — added ten rounds earlier inside
`film score, underscore, orchestral score`, meaning a film cue. The take would have come back with no
bed at all, which is the poem. **Third stale ban in four rounds.** The existing rule says grep for
*the thing and its category*; this adds: **grep the ban list for the new prompt's own words, every
round, both directions.**

**The ladder if it persists**, cheapest first: re-roll twice → swap the form word to
**`documentary voiceover, radio drama`** (Thread 5's *ask for a form that exists*, applied to rhythm:
the forms where a man talks with no beat) → widen the **sentence-length spread** in the lyrics, since
even lengths let a bar pattern emerge → place **ellipses** deliberately (*"Hyphens = speed.
Punctuation = breath. Line breaks = phrases."*).

🔑 **And the discipline that made round 14 cheap: once an axis is confirmed right, freeze it.** The
A6 voice clauses are byte-identical to the approved take, so anything odd about the voice is a
re-roll, not a rewrite — and the round stays attributable to the one axis that moved.

### Sources

External guidance quoted above, harvested 2026-09-01. All assertion-grade; the tested findings are
ours:
[spoken narration workflow](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-narration-workflow) ·
[spoken word guide](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-spoken-word-when-the-world-was-a-whisper) ·
[Suno prompt guide 2026](https://hookgenius.app/learn/suno-prompt-guide-2026/) ·
[the formula that actually works](https://roo.beehiiv.com/p/suno-ai-prompt-guide-2026-copy-paste-templates-the-formula-that-actually-works) ·
[dynamic control guide](https://acetaggen.com/blog/silent-architect-pause-space-hard-cut-dynamic-control-suno) ·
[achieving specific vocal styles](https://www.anywiki.net/sunoai/achieving-specific-vocal-styles-in-suno-ai).
