---
name: suno-prompt
description: Use when turning a song idea into a Suno prompt — a style prompt, exclude-styles list, or lyrics — for BadCode music. Triggers on "make a Suno prompt", "turn this into a song / track", "write lyrics for…", "optimize this for Suno", "give me a style prompt", or any drum & bass / track idea clearly meant for Suno generation.
---

# Suno Prompt (BadCode)

Take what's in the user's head — a vague idea, a reference track, a feeling, a GPOM story beat — and
turn it into a Suno prompt that produces accurate, high-quality output, **in the BadCode voice.**

You produce style prompts, exclude-styles lists, slider settings, and — when asked — lyrics.

**This is an interview, not a vending machine.** A one-shot prompt off a one-line brief is the thing
this skill exists to replace. Work in short rounds: ask the few questions that actually change the
output, draft fast, then refine against what the user hears.

## The knowledge base lives in `docs/suno-gpt/`

Read on demand. Never reproduce its content in your reply, and don't lecture the user about it.

| File | What | Read when |
|---|---|---|
| `system-prompt.txt` | Base operating procedure — modes, output format, character limits, edge cases | First use in a conversation |
| `files/suno-tag-mechanics.md` | Prompt language: hybrid format, ordering, genre pairing, bracket language, exclude strategy, contamination words | First use in a conversation |
| `files/suno-controls-and-workflows.md` | **The three sliders, model choice, Voice/Persona/custom models, lyric editing, Studio, stems, known failure modes** | Any question beyond the Style box — and always before quoting a slider value |
| `files/producer-vocabulary.md` | Words for describing sound; song structure; how to judge a generation | Translating a vague brief, or debugging a prompt that won't land |
| `files/lyric-craft.md` | Syllables, rhyme, section shapes, transitions — **plus the punctuation/timing table (how Suno times what you wrote)** | Writing lyrics — apply **silently**. **Always** when a delivery is the wrong speed |
| `files/lyricist-playbook.md` | **The songwriter's side**: which section tag summons which character, performance cues, multi-voice casting, typography, pronunciation, the content filter, hooks, lyric failure modes, Studio warp/quantize | Any lyrics-box question the other files don't answer. **Assertion-grade — read its confidence warning; where it conflicts with a tested finding, the tested one wins** |
| `files/meta-tag-dictionary.md` | Specialty `[ ]` tags | Writing lyrics. **Treat as unverified** — see caution below |
| `files/overused-words.md`, `files/ai-cliches.md` | Red-flag lists. **Lyrics only, never style prompts** | Writing lyrics |
| `suno-voices.md` | **The voice playbook's evidence base** — both Karen threads in full: the genre-pool discovery, the transplant ladder, My Taste forensics | A character voice is fighting you, or you need the why behind "Getting a specific voice" below |

**Caution on the meta-tag dictionary.** Its exotic entries (`[fugue]`, `[retrograde]`,
`[pedal-point]`, `[length: …]`) are uncorroborated by any practitioner source we have. Suno publishes
no tag list, so the whole vocabulary is folk knowledge. Prefer plain-language production cues, which
are demonstrably what works. Never promise a meta-tag will fire.

---

## The interview

Ask in rounds of **2–3 questions maximum**, then draft. Skip anything the user already told you, and
skip straight to drafting if they clearly just want something fast.

**Round 1 — the frame.** (Ask only what's missing.)
- **Which Suno mode?** Simple / Advanced / Studio. Ask once per conversation, remember it. This
  decides the output shape and the character budget.
- **What is this song for?** A GPOM story beat, a standalone release, a comic soundtrack, an
  experiment? If it ties to canon, skim the story folder before drafting.
- **What's the feeling, or the reference?** Take a fragment, a mood, an adjective, a track they like.
  Don't demand a brief.

**Round 2 — the levers that actually change the output.**
- **The vocal arc.** Not "what voice" — *where does it start and where does it end?* This is the
  highest-leverage single question in the whole interview. `soft verses → belted refrain`;
  `snarled aggression → clean chant`. A static descriptor gets you a generic vocal; an arc gets you a
  performance.
- **What must survive?** The one thing that, if Suno loses it, makes the take worthless. That word
  goes first in the prompt.
- **What should it absolutely not sound like?** Feeds Exclude Styles, and catches register mismatches
  early (see the satire trap below).

**Round 3 — only if relevant.**
- Is there **source audio**? A hum, a demo, a spoken take, a field recording. If yes, that changes
  everything — audio-seeding is the single cheapest route to a sound nobody else has, and it brings
  the audio-influence slider into play.
- Does this need to **match an existing track** (same narrator, same release)? If yes, go to the
  consistency stack in `suno-controls-and-workflows.md` §4 before writing anything.
- Is the lead a **character** (a specific person, not just "a vocal")? If yes, read their canon
  `voice:` frontmatter, check what's in **My Taste** before generating, and plan for the voice via
  "Getting a specific voice" below — character voices routinely need the Voice-transplant ladder,
  and knowing that up front saves rounds.

Then **draft**. Don't wait for perfect information — a draft the user can react to is worth more
than three more questions.

---

## Building the prompt

### The skeleton: Genre → Mood → Instruments → Vocals

- **Genre** — 1–2 terms: parent + specific subgenre. The single highest-leverage word in the prompt;
  changing it alone rewrites the whole track.
- **Mood** — 2–3 emotion words. BPM lives here.
- **Instruments** — 2–3 named, each with an adjective. Bind mood to instrument where one element
  should carry it (`aggressive guitar`, `angelic piano`) rather than letting it wash over everything.
- **Vocals** — gender + timbre + technique + **arc**.

**Cap each slot at 2–3 terms.** Suno takes everything literally and can only process so much;
overloading dilutes, and a long prompt is *harder to debug* because every word has pull.

### The shape

Two sentences — one instrumental, one vocal, ~35–45 words. Far shorter than the character ceiling:

```
A/An <mood> <genre> track with <three instrument/production details>.
<Gender> vocals that <delivery>, <arc clause>.
```

This is a proven shape, not a rule — the hybrid format in `suno-tag-mechanics.md` is still correct,
and denser prompts are fine when the user has specifics. But **default short**. Character limits are
ceilings, not targets.

### The three-pass upgrade

When a draft feels flat, upgrade it in passes rather than adding more nouns:
**emotion** (replace the generic feeling word with a precise one) → **texture** (if you could touch
it, how would it feel?) → **production** (dry/wet, sparse/dense, wide/mono, polished/lo-fi).
Vocabulary and the antagonist-pairs table are in `producer-vocabulary.md`.

### Advanced vs Simple: split the content, not just the length

- **Simple** (3,000 chars) carries *both* the sound and what the song is about. A long, specific
  prose description of the subject gets picked up in the lyrics.
- **Advanced** (1,000 chars) should skip subject matter entirely — that lives in the Lyrics box —
  and spend the whole budget on **sound**.

Pasting a Simple prompt into Advanced truncates it. Flag this if you see it.

---

## Output format

Always give the sliders. They are prompt-adherence controls, not platform trivia, and omitting them
leaves the best advice on the floor.

- **Simple:** Style block only.
- **Advanced:** My Taste block, Style block, Exclude Styles block, then a one-line settings note.
  Lyrics only on request.
- **Studio:** single-element style block + Exclude Styles (mandatory there — Studio leaks instruments
  constantly).

**Always produce a per-track My Taste block** (Advanced work). My Taste biases *every* generation,
cannot be turned off, and can only be replaced — a stale profile from the last track is a competing
identity silently fighting this one (the Karen lesson: her profile would drag any later track toward
her voice). So every track gets its own profile to swap in for the session: positive statements
only, **vocals first**, pulling the same way as the Style prompt, no artist names, well under the
2,000-char limit. Remind the user to restore (or swap to the next track's) profile afterwards.

**The generation workflow is four pastes, in order: My Taste → Style → Exclude Styles → Lyrics** —
all four boxes, every round, from this session's blocks. Never trust what a box already contains.

Default settings line, unless the situation calls for otherwise:

> Style influence **75**, weirdness **60**, audio influence **40** (only if you're seeding from audio).

Adjust with reasons from `suno-controls-and-workflows.md` §1 — e.g. weirdness 0 and style influence
100 for a lyric-swap cover; weirdness 0 for an exact reproduction; audio influence 75–85 when a
specific melody must survive.

---

## The refinement loop

This is where the quality actually comes from. After the user reports back:

1. **Ask what specifically was wrong** — and which of the four axes it failed on: *creativity,
   prompt adherence, fidelity, realism*. Conflating them is why AI-music feedback is usually useless.
2. **Fix by deleting, not adding.** Find the single word pulling the wrong way and remove it. Adding
   a corrective word makes Suno average the two into mush. If it came out too bluesy, take out
   `blues rock` — don't add `not bluesy`.
3. **Front-load a stubborn word.** If something keeps getting ignored, move it to the very start of
   the prompt. Front-loading is a *fix*, not just an initial-ordering rule.
4. **Re-roll before rewriting.** Meta-tags and cues are probabilistic — the same prompt often lands
   on the second generation. Don't rewrite a prompt that was merely unlucky.
5. **Escalate a tag that's ignored** by adding redundant synonyms: `[spoken word]` →
   `[spoken word speech]` → `[spoken word speech talking]`. Redundancy is a real technique, not a
   smell.
6. **Re-paste every box, every round — Style, Exclude, Lyrics, and My Taste.** "Reuse Prompt"
   silently carries the old lyrics forward, and a stale Lyrics box is inaudible as such — it just
   sounds like the style prompt is being ignored. (This cost the Karen track four rounds.)
7. **If a vocal hasn't moved after ~2 rounds of style-prompt surgery, stop prompting** — the voice
   you want probably isn't in the genre's vocalist pool, and no adjective stack jumps pools. Go to
   "Getting a specific voice" below.

---

## Getting a specific voice

Distilled from the eight-round Karen voice war ([`docs/suno-gpt/suno-voices.md`](../../../docs/suno-gpt/suno-voices.md)
has the full evidence). A "voice" lives in four layers — the canon character file (`voice:`
frontmatter, the source of truth), the Style box, the per-section lyric bracket cues, and the
platform features (saved Voice / custom model / Lyricist). Be deliberate about which you're using.

**The core discovery: the genre tag picks the vocalist pool, not just the instruments.** Every
generation converges on the pool's centroid ("female + boom bap + half-spoken" *is* the smooth
silky vocalist), and adjectives are weak words fighting the prompt's strongest word. Diagnostic:
convergence at both low and high weirdness — weirdness perturbs within the pool, never across it.

**Style-box voice grammar** (in force before you ever escalate):

- **Arc, not state** — where the voice starts and where it ends. The arc is characterization.
- **Articulation beats attitude** — describe the mouth (nasal, pinched, flat hard vowels,
  over-enunciated consonants), never the feelings ("put-upon", "brittle" average into nothing).
  Onomatopoeia beats anatomy: honk, squawk, kvetch. A **performance tradition** the model knows
  (musical-theatre patter, sitcom squawk, gospel preacher) beats demographics — age words are
  ~50–80% reliable and may simply not fire.
- **No negation.** "not singing, no melody, no flow, no swagger" *describes a male rapper* — and
  generated one. Negations go in Exclude Styles; the Style box gets positive speech-act words.
- **Short prompt or the voice loses.** Suno dilutes across everything named; delete whatever the
  genre tag provides free so the voice clauses keep their weight. Ceilings, not targets.
- **The character in (nearly) every bracket cue.** A section header with no vocal direction falls
  back to the genre default *for that section*.

**Check upstream before debugging downstream: My Taste.** The profile text biases every
generation and can hold a full competing vocal identity. It **cannot be saved empty** — only
replaced — and the "My Styles" toggle is just the suggestion wand, not the bias. Working move: swap
in a per-track profile that pulls the same way as the song (Vocals field first), restore after.
The implicit half (learned from your library and likes) has no off switch: thumbs-down every
reject, one workspace per arc.

**The escalation ladder, when prompting stalls:**

1. **Listen for the voice in the wrong slot.** The vocal prior binds to the *lead slot inside the
   groove*; the parenthesis/backing slot escapes it (Karen first appeared on the parenthetical
   answering-machine lines). If the voice exists anywhere in a take, skip to step 3.
2. **Probe-farm it in its home genre** — generate the character where their voice is the default
   (whiny complainer → comedy patter song, sparse piano), real lyrics, **no parentheses**, target
   genre in the excludes. Doubles as a capability probe: not even there → step 4 is the only road.
3. **Voice transplant:** Remix → Voice on the best take, **select the sub-region** where the voice
   is right (15 clean seconds beat 60 contaminated; up to 2 min clones stabler), **delete the
   attached style prompt**, apply to the real track at audio influence 40–60 (70+ if drifting),
   then Cover the right-voiced take at ~25–40 to recover fidelity.
4. **The floor: audio-seed a human** — 15s–4min of someone *doing* the voice, one consistent
   register, Voice → Create voice, audio influence 70–100, two-pass down. Perform the verification
   phrase in character; flat reading fails.

**Once a Voice pins the lead:** strip the anti-defect words from the excludes (armour against a
lead problem strangles the backing vocals), and consider **casting the genre default instead of
fighting it** — the smooth vocalist that kept invading Karen's lead became the institution's choir,
singing the functionaries' answers against her spoken whine. The wrong voice is often a right
voice for somebody else in the story. One saved Voice per generation, but lead + parentheses =
two cast members.

**Cue-heavy skit tracks invert the model rule:** v4.5's extra vocal variety isn't worth it when the
track's architecture lives in dense bracket cues — 4.5 shreds the structure, v5.5 obeys it. Stay on
5.5 and spend direction in the brackets.

---

## The BadCode layer

Apply on top of everything above. This is why the skill exists and not just the raw procedure.

- **Default to drum & bass.** Lead with a specific subgenre (`Drum and Bass, Neurofunk` / `Liquid
  DnB` / `Jump Up` / `Jungle`) paired with the parent genre — but see the D&B notes below, because
  Suno is weak at exactly these subgenres.
- **Lyrics carry the BadCode voice.** Read [`docs/voice.md`](../../../docs/voice.md). Overtly
  sarcastic, dark humour, total authority — a superintelligence from the future that already knows
  how it all played out, nurturing underneath the snark. Politics and economics first. Story over
  sermon: encode the point in metaphor, character and a punchline. Never lecture.
- **Every song carries a point.** Before finalizing lyrics, check there's a load-bearing
  political/economic idea in there. The bet is that people absorb an *idea* through a song they'd
  never absorb in an essay.
- **Write the lyrics ourselves.** Suno's lyric model is a next-token predictor, so its default output
  is by construction the most common phrasing available — and it compulsively writes about wires and
  circuits. The division of labour the whole corpus supports: **AI writes the style prompt, humans
  write the lyrics.** Use Suno's lyric tools to *refine* our words, never to originate them.
- **Break AABB.** It's the clearest AI-lyric tell. Prefer ABAB, and leave a line unrhymed —
  especially the last line of a verse. An abandoned rhyme reads as the speaker being too wrecked to
  keep up the pattern.
- **Stay in canon.** If the idea ties to the GitPush Origin Master arc, skim
  [`docs/stories/gitpush-origin-master/README.md`](../../../docs/stories/gitpush-origin-master/README.md)
  and keep the polyphonic future-narrator voice and arc beats consistent.
- **Read the as-built comic, not just the canon.** When a story has a rendered comic, the panel
  narration and bubbles (`apps/web/src/comics/<story>/comic.json`) carry texture the canon files
  don't — specific locations, running gags, name spellings, the closing image. Karen's whole outro
  ("Hold, please") came from a statue panel the canon never mentions. They can also *disagree* with
  canon (AI Sean vs "AI Shaun"); flag mismatches rather than silently picking one.

### The satire trap — the failure mode that would ruin a BadCode track

An absurd or surreal subject drags the arrangement toward **novelty and comedy**. BadCode's whole
register is *dark satire played straight* — the joke is in the words, never in the music.

So whenever the concept is absurd but the sound must be serious, **state the register explicitly and
negate the default**, with the negation repeated for weight: `…no comedy, no novelty, played
completely straight.` Put comedic/novelty/parody in Exclude Styles as well.

This holds **even when the user literally asks for a funny song**. "Funny hip hop" translated
faithfully ("comedic deadpan", "comedy-skit energy" in the Style box) summons kazoos and vaudeville —
*less* funny, not more. Read the brief's intent against its wording: the humour goes in the lyrics
and the conceit; the arrangement stays sincere and warm. Learned the hard way on the Karen track
(2026-07) — first drafts led with "comedic" and had to be stripped.

### Skit / dialogue tracks — the worked recipe (Karen, 2026-07)

For a track built on a background conversation (phone calls, an argument, an interrogation) rather
than a second rapper:

- **Parentheses are the mechanism.** `( )` text is *performed* as backing/secondary vocal, so the
  other side of the conversation goes in parentheses on the lead's lines. That's what renders it as
  half-audible mutterings *behind* the beat instead of a duet. Reinforce placement in the Style box
  ("muffled telephone voices answer from behind the beat") rather than only in the lyric tags.
- **Make the conceit the instrumentation.** Build the beat from objects in the song's world — for
  Karen: the hold-muzak loop *is* the lead melodic element, touch-tone beeps are percussion, dial
  tone opens and closes the track. This is the strongest counter to the satire trap: the joke
  becomes *audible* without the arrangement going novelty.
- **An escalation ladder of distinct voices will not survive one generation.** Suno gives you two,
  maybe three differentiated background voices in-generation. Keep those in the parentheses; build
  the rest as **Sounds-tab spoken one-shots** (BPM/key on "any", throwaway word + comma prefix
  against first-word clipping) and layer them in the DAW — which also lets each voice get its own
  phone EQ, and per-voice EQ is how you *sell* the escalation.
- **Rhyme across the speakers as characterization.** The lead finishing the background voice's rhyme
  reads as refusing to let it be a separate conversation; leaving the rhyme hanging reads as being
  stonewalled. Cheap, and it does story work the arrangement can't.
- **A dialogue chorus is call-and-response**, not alternating verses: the functionary's line in
  parentheses, the lead's fixed answer as the hook ("I'm sorry, I can't help you" / "That's OK").

### The narrator problem

BadCode needs one recurring voice across a whole release arc. That is a *feature* problem, not a
prompt problem — see `suno-controls-and-workflows.md` §4 for the full stack (Voice + custom model +
Lyricist). Two BadCode-specific notes:

- **Build the narrator's Voice in a register that has nothing to do with D&B** — spoken oratory,
  opera, a gospel preacher, a sardonic crooner. The genre mismatch is what breaks Suno out of its
  generic per-genre vocal default, and it's the cheapest route to a vocal no other Suno D&B track
  has. Audio influence 40–60 for the strongest effect.
- **Narration segments** use the spoken-word recipe in `suno-tag-mechanics.md`, and it composes with
  a saved Voice — so the narrator can speak in one track and sing in the next as the same character.

### Drum & bass specifics — where Suno will fight you

1. **Half-time drums are a known blind spot.** Repeated controlled tests never produced half-time
   from a `breakdown` tag — it slows and thins the arrangement instead. Since the half-time drop is a
   defining D&B device, **assume you cannot prompt it.** Get it by editing in Studio or splicing
   sections, and tell the user that rather than selling them a prompt that won't work.
2. **Niche subgenres fail; broad ones work.** Riddim came back as generic dubstep with none of the
   characteristic sound design — expect the same at neurofunk / liquid / jump-up level. **Mitigation:
   describe the sound design and rhythm rather than relying on the subgenre name.** `producer-
   vocabulary.md` is exactly that toolkit — reese bass, sample-and-hold on the cutoff, amen break,
   sub layering, sparse drop.
3. **Suno's harshness sits exactly where D&B lives** — brittle cymbals, sizzling hats, sibilance in
   2–6 kHz. Budget for de-essing, or plan to replace the drum stem.
4. **Sidechain pumping can't be undone** — it's baked in, not a real sidechain.
5. **Sounds mode is the D&B post-production kit** — risers, downlifters, sweeps, impacts, fills, at
   your project's BPM and key. Suno won't build transitions into a generation, so this is how you get
   them.

---

## Saving a song

When a prompt or lyric is worth keeping, write it to `docs/stories/<story>/songs/<slug>.md` — the
same file `new-story` step 4 produces. Frontmatter carries **metadata only** (`title, status, bpm,
model, settings, voices`). Everything destined for a Suno input box lives in the **body as fenced
code blocks** that copy clean — **never in frontmatter** (YAML `>-` blocks indent every line, which
makes copy-pasting a pain). A `## Suno prompt` section carries all four, in paste order: **My Taste,
Style, Exclude Styles**, then the lyrics in a `lyrics` block.
`docs/stories/gitpush-origin-master/songs/git-push-origin-master-orchestral.md` is the worked
reference. Its D&B sibling (`…-dnb.md`) is the worked reference for **two cuts of one song**: when
a track forks rather than iterates, give each cut its own file with a `sibling:` frontmatter key,
keep the shared material (the lyric/bulletin bank) in one file only, and say in both headers which
one is canonical.

Record the **slider settings and the Suno model version** alongside the prompt — a prompt without
them isn't reproducible, and model behaviour shifts between versions.

If the song isn't tied to a story yet, offer to run **`new-story`** first. Curate — these feed the
GPOM narrative; don't bulk-dump.
