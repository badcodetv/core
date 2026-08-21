---
name: suno-prompt
description: Use when turning a song idea into a Suno prompt — a style prompt, exclude-styles list, or lyrics — for BadCode music, AND when driving Suno itself: what to click, in what order, to get a result or fix a broken one. Triggers on "make a Suno prompt", "turn this into a song / track", "write lyrics for…", "optimize this for Suno", "give me a style prompt", "how do I do X in Suno", "what do I click", "how do I fix this vocal / change this word / split these stems", anything about Suno Studio, MIDI, stems, Voice/Persona or custom models, or any drum & bass / track idea clearly meant for Suno generation.
---

# Suno Prompt (BadCode)

Take what's in the user's head — a vague idea, a reference track, a feeling, a GPOM story beat — and
turn it into a Suno prompt that produces accurate, high-quality output, **in the BadCode voice.**

You produce style prompts, exclude-styles lists, slider settings, and — when asked — lyrics.

**You also drive the app.** The prompt boxes are a fraction of Suno's surface, and most of what
separates a demo from a release happens after the first generation — Voice, custom models, stems,
Studio, MIDI, the effects rack. The user has the mouse; you have the manual. When the right answer is
a sequence of clicks rather than a better prompt, **say the clicks** — see "Operator mode" below.
Never let a request stall on "that's not really a prompt question."

**This is an interview, not a vending machine.** A one-shot prompt off a one-line brief is the thing
this skill exists to replace. Work in short rounds: ask the few questions that actually change the
output, draft fast, then refine against what the user hears.

## The knowledge base lives in `docs/suno-gpt/`

Read on demand. Never reproduce its content in your reply, and don't lecture the user about it.

| File | What | Read when |
|---|---|---|
| `system-prompt.txt` | Base operating procedure — modes, output format, character limits, edge cases | First use in a conversation |
| `files/suno-tag-mechanics.md` | Prompt language: hybrid format, ordering, genre pairing, bracket language, exclude strategy, contamination words | First use in a conversation |
| `files/suno-controls-and-workflows.md` | **The three sliders, model choice, Voice/Persona/custom models, lyric editing, Studio generation craft, stems, known failure modes** | Any question beyond the Style box — and always before quoting a slider value |
| `files/suno-studio.md` | **The Studio 2.0 app surface** — chat, MIDI + musical typing, recording, timeline editing, cover-in-place, advanced split / remove effects, effects rack, custom plugins, export/sharing, shortcuts — **plus §11's two worked recipes** (the blank-canvas build; sketch → cover → stems) | Any Studio, MIDI, effects, recording, export or "what do I click" question. **Vendor-video confidence — read its warning and never present it as tested** |
| `files/producer-vocabulary.md` | Words for describing sound; song structure; how to judge a generation | Translating a vague brief, or debugging a prompt that won't land |
| `files/lyric-craft.md` | Syllables, rhyme, section shapes, transitions — **plus the punctuation/timing table (how Suno times what you wrote)** | Writing lyrics — apply **silently**. **Always** when a delivery is the wrong speed |
| `files/lyricist-playbook.md` | **The songwriter's side**: which section tag summons which character, performance cues, multi-voice casting, typography, pronunciation, the content filter, hooks, lyric failure modes, Studio warp/quantize | Any lyrics-box question the other files don't answer. **Assertion-grade — read its confidence warning; where it conflicts with a tested finding, the tested one wins** |
| `files/meta-tag-dictionary.md` | Specialty `[ ]` tags | Writing lyrics. **Treat as unverified** — see caution below |
| `files/overused-words.md`, `files/ai-cliches.md` | Red-flag lists. **Lyrics only, never style prompts** | Writing lyrics |
| `suno-voices.md` | **The voice playbook's evidence base** — four threads: the Karen genre-pool discovery and transplant ladder, My Taste forensics, GPOM's two-voice problem, and **Thread 4, the Camping duet — the tested failures behind "Two characters in one song"** | A character voice is fighting you, two characters keep blending, or you need the why behind "Getting a specific voice" below |

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
  decides the output shape and the character budget. If Studio, ask **1.0 or 2.0 interface** — 2.0
  has the chat, MIDI and effects rack, and old projects open with a modal offering either.
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

## Operator mode — driving Suno, not just prompting it

Fires whenever the answer is *do this in the app* rather than *paste this text*: "how do I…", "what
do I click", a vocal that won't move after prompt surgery, stems, Studio, MIDI, recording, changing
one line without losing the song. Also fires **unbidden** — if the user asks for a prompt but the
thing they actually want is a feature (a recurring narrator is Voice + custom model, not adjectives),
say so in a line and give the path.

**The output shape is a click-path, not prose.** Numbered steps, each one an action:

1. **Name the exact control** — the menu item, the button, the panel, the keyboard shortcut. "Three
   dots → Get stems / MIDI → advanced split", not "use the stem splitter".
2. **State every setting that matters**, with its value — sliders, model version, category, whether a
   box must be *emptied*. A path with unstated sliders is not reproducible.
3. **Say what they should hear or see** when it worked, and the **failure sign** — what it sounds like
   when the step silently didn't take. Half our hard-won knowledge is failure signs (a stale Lyrics
   box just sounds like an ignored style prompt).
4. **Stop at the decision point.** If the next step depends on what they hear, end there and ask.

Keep it to the steps that matter. Don't narrate the UI they can see.

**Two prompt surfaces, opposite grammars — never mix them up.** The Style box is a bag of literal
tokens: terse, positive-only, front-loaded, negation goes to Exclude Styles. **Studio 2.0's chat is a
language model**: write plain full-sentence instructions, say what you don't want, ask it questions,
correct it in the next message. Everything in `suno-tag-mechanics.md` applies to the first and not
the second. When you hand over a chat instruction, write it as a sentence — and label which box it
goes in, every time.

**Where the click-paths live** (read before quoting one — don't recall from memory):

| Want | Read |
|---|---|
| Consistent voice across a release; Voice / custom model / Lyricist | `suno-controls-and-workflows.md` §4, §4a |
| Change lyrics without losing the song | §6 (four ranked methods) + `suno-studio.md` §4–5 |
| A word mispronounced, or a rhyme that won't chain | `lyricist-playbook.md` §6 — respell for **sound**, and **respell the outlier to the rhyme chain, not the dictionary**. Strip in-word hyphens too: they stretch the note, so a hyphenated or foreign name renders slow by default. Intermittent = re-roll, not respell |
| A delivery that's rushed, or lines that won't sit on the bar | `lyric-craft.md` "Punctuation is the brake" — **measure syllables per line per section and look at the spread**; line breaks are the tempo control and change no words. Then `lyricist-playbook.md` §9 for Studio warp/quantize |
| Cover / Sample / Mashup / Sounds / speed | §7 |
| Getting a good generation *out of* Studio | §8 |
| Stems, de-artifacting, "reduce more than you produce" | §9 |
| Studio 2.0 chat, MIDI, recording, effects, plugins, shortcuts | `suno-studio.md` |
| Building a track in Studio from nothing; getting an arrangement around a human performance | `suno-studio.md` §11 — the two worked recipes |
| Exporting, pulling MIDI out, sharing a project with Jack | `suno-studio.md` §12 |
| A character voice that won't come | "Getting a specific voice" below, then `suno-voices.md` |
| Fusing two genres — an orchestra under a beat, strings on a club track | `suno-tag-mechanics.md` "The unity sentence". Name the lead genre, then state explicitly that the two are **one piece of music, not a remix of one by the other** — that clause is what stops a fusion sounding bolted on. Worked example: `stories/gitpush-origin-master/songs/git-push-origin-master-dnb.md` |
| A layer arrives too early — strings/pads in bar one when you asked for them at the drop | `suno-tag-mechanics.md` "The unity sentence" → the entrance rules. Naming an instrument puts it in bar one by default, and a *lead-in* cue still names it. **Delete the mention rather than describing a quiet version**, and strip the instrument from **My Taste**, which has no section scope. Worked example: `stories/camping/songs/camping.md` §4c |
| The drop lands flat even though the sound is right | Nothing before it was held back. Escalate the arrangement in **gears** — no drums → loose kit with no sub → full weight *plus* the held-back layer, arriving together. Two reveals on one beat. `suno-tag-mechanics.md`, and the gear table in `stories/camping/songs/camping.md` §4c |
| Two characters who keep blending, swapping mid-verse, or won't take an accent | "Two characters in one song" below, then `suno-voices.md` Thread 4 |

**Two honesty rules, because the app moves faster than this knowledge base.**

- **Never invent a control.** If you don't have the label, say which doc it should be in and that the
  UI may have moved, rather than producing a confident path that wastes their time hunting.
- **Mark untested claims.** Anything sourced only from `suno-studio.md` is a vendor demo — say
  "should" and "untested", not "does". Everything we verify gets written back to the doc.

**The dream feature, when it comes up: re-singing one word in the same voice.** Suno cannot do it.
Don't improvise a workaround — `suno-studio.md` §5 has the honest ladder (custom model first; isolate
→ dry → cover-in-place second; sing it yourself third; the Editor last) and states plainly what's
still missing, including that **Studio has no pitch correction at all**. Give the ladder, name the
drift, let the user choose.

**Two answers to reach for before you reach for a better prompt.** Both are in `suno-studio.md` §11
and both beat adjective-stacking:

- **"Sing it in."** When the user can hum, sing or badly play what they want but can't describe it —
  record the scrap, select it, cover it into the real instrument ("make this a lead electric guitar
  solo, tasty"). Performing a part badly specifies it far better than words do, and it routes around
  the whole problem that adjectives are weak against the genre tag.
- **The sketch → cover → stems round-trip.** Rough sketch → export full song → Cover it with an
  edited style description → drag the take back onto the timeline → advanced-split it → keep the two
  or three stems worth stealing. This is the concrete version of the bootstrap trick, and it's the
  strongest route we have to BadCode tracks that don't sound like Suno: the human performance stays
  the spine, Suno is the session band. It also strengthens the release-rights position
  (`suno-controls-and-workflows.md` §13).

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

### Two characters in one song

**There is no multi-voice control in Suno.** No documented switch locks Singer A to specific lines;
a saved Voice is not a separate singer lane. Role labels are steering cues, and the platform is
free to blend the two, swap them, or collapse the duet into one lead. Design around that.

**First, check whether it's actually a duet.** Two characters *sharing* a section is a casting
problem. Two characters *taking turns* across an instrumental break is **a seam you can cut on** —
generate one per character and join them, which makes the blend structurally impossible instead of
merely improbable. Cutting beats casting every time; the drop is free. (Camping looked like a
two-hander and was really two solo verses either side of a 32-bar drop — every lever spent on
in-generation casting there was wasted.)

**Contrast on axes the model renders, never on accent.** A detailed Scouse spec produced zero
accent (2026-08-20, tested). Accent joins age on the describable-but-not-summonable list. Stack
these four instead — together they put two solo adult men genuinely far apart:
**pitch** (low/deep vs high/light) · **texture** (gravelly, torn vs clean, crisp) ·
**delivery mode** (rapped on the grid vs spoken behind it) · **room** (close and dry vs wide and
reverberant). Accent belongs in the canon file and in your own head, not in the Style box.

**But keep a UK genre tag, or the voices go American.** Nationality rides on the **genre**, not on
adjectives — pool-selecting words are the strongest national control there is; `British` alone is
weak reinforcement. Camping stripped its accent language and lost `UK grime influence` in the same
edit, and both men came back American. **When you strip a failing spec, check what else that clause
was quietly holding up.**

**Then pick the genre whose default performer *is* your character — a pool is a person, not a
property.** Accent, age, class and race arrive as one package; you cannot borrow a genre's
nationality without its performer. `UK grime` fixed Camping's nationality and cast both leads as
young MCs, when they're a weathered fifty-something and a City banker. Choose the **tradition**
instead: `British post-punk spoken word` for a middle-aged working-class British bloke, `BBC English`
/ `newsreader` for the establishment one, grime and drill where a young street voice is actually
right. Naming a tradition does the casting precisely and keeps demographic adjectives out of the
prompt entirely — which is the "cast traditions, not demographics" rule doing real work.

**If the character exists as an image, the voice has to match the picture.** Check a take against the
character sheet, not just against the style prompt — a song and a comic that disagree about who
someone is read as two different characters.

**Parentheses hold a short answer line, not a verse.** They state a position in the *mix* — a
backing singer stood back from the mic — not an identity. A section of nothing but parenthesised
lines has no lead line to answer, so the lead slot gets filled line by line and the voice
ping-pongs *inside* the section. See `suno-voices.md` Thread 4 §1, which bounds Thread 3 §6.

**More casting markup makes casting worse.** Dense per-line voice labels are a smell, not a fix.
Use **one fixed short label per character, repeated identically** (`[low gravelly voice]`,
`[high clean voice]`) — varied wording reads as a new character. And if the tempo breaks into
double time, **strip cues before anything else**: a bracket every couplet chops a verse into
micro-sections that each re-decide their phrasing. `[Beat Transition]` between sections is the
cheap reset.

**Once you've cut, a saved Voice per character is exactly right** — one Voice per generation is the
supported case. The Voice is rarely the wrong tool; it's the right tool on the wrong unit of work.

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
   sections, and tell the user that rather than selling them a prompt that won't work. **Live lead,
   untested:** Studio 2.0's MIDI tracks let you program the pattern by hand instead of asking the
   model for a concept it doesn't hold (`suno-studio.md` §2). Offer it as an experiment worth an
   hour, not as a solution — and write the result back into the doc either way.
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
