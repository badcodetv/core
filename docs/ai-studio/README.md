---
title: Google AI Studio — the voice toolkit
engine: gemini-3.1-flash-tts-preview
built: 2026-09-04
status: 🟡 strong free engine, but the camping narrator went to Hume Octave 2026-09-04
---

# Google AI Studio — voice generation

> **What this is:** everything we know about generating **spoken voice** in Google AI Studio,
> kept separate from the story sheets on purpose. The Suno toolkit's counterpart for speech.
> Craft *for a specific narrator* stays in that story's own sheet — e.g.
> [`../stories/camping/narration/voice.md`](../stories/camping/narration/voice.md). **Engine
> behaviour goes here.**
>
> Built 2026-09-04 from Google's own docs plus a live session on Jack's Ultra account.
> Where a claim was only *read*, it is marked ⬜ **unverified**.

## 🔑 THE HEADLINE (2026-09-04) — it is the first engine that does not sound like AI

**Jack, on the first take: *"The accent is wrong but it sounds like a normal person, not AI."***

🔑 **That is a first.** Read [`../stories/camping/narration/voice.md`](../stories/camping/narration/voice.md)
end to end and the recurring complaint is never "the accent is wrong" — it is **"every free AI voice
is awful."** Suno sang. ElevenLabs Voice Design averaged to the default. MiniMax went American.
Local cloners were rejected by ear as synthetic. **Gemini 3.1 Flash TTS cleared the slop bar on
attempt one, with the accent still unsolved.**

**So the ranking flips.** Accent is a *steering* problem and this file is about steering. Sounding
human is an *engine* property and no amount of prompting buys it. **We now have the hard half.**

🔴 **Open problem:** the accent. Two levers, in order — the **voice library's Accent filter**
(copy an accent) before **Voice Direction prose** (invent one). `voice.md`'s standing finding
still governs: *every route that works COPIES an accent; none invent one.*

## ✅ THE VOICE LANDED (2026-09-04) — Jack: *"that worked"*

**The winning configuration**, after five rewrites. Change one field at a time from here.

| Field | Value |
|---|---|
| **Model** | `gemini-3.1-flash-tts-preview`, Composer mode |
| **Voice** | **Algenib** (Gravelly, lower pitch) |
| **Temperature** | 1 |
| **Voice Direction** | The `# AUDIO PROFILE: Gaz M.` block below |
| **Scene** | Salford back room, voice-memo recording clause |
| **Sample Context** | Casting blurb **with the accent named in it** |
| **Transcript** | Chunk 1, elided |

🔑 **What actually fixed it, in order of contribution:**

1. **Google's headed structure** — `# AUDIO PROFILE` / `### DIRECTOR'S NOTES` with `Style / Accent /
   Pace` sub-headings, not flowing prose. This is the shape their own worked example uses.
2. **The box audit** — no field left accent-neutral. The town went into the Scene, the accent into
   the casting blurb.
3. **`deep` restated as pitch** rather than as an archetype, so it stopped cancelling `never boomy`.
4. **One name across every field.**

⚠️ **Not needed in the end:** the Accent filter, Voice Design, billing, or a cloned reference.
**Prose won on this engine** — the first time in the whole narration investigation that it has.

## 🔴 RULED 2026-09-04 — "too northern and weird… boring". Three causes, all mine.

**Jack, on the full pass: *"he is too northern and weird, make his voice better, clearer and less
boring."*** ✅ **All three trace to specific clauses, and two of them contradict the brief.**

| Complaint | Cause | Fix |
|---|---|---|
| 🔴 **"Too northern"** — twice now | The **phonetic articulation stack**: *swallowed consonants, dropped T's and dropped H's, hard flat vowels drawn out and drooping*. Spelling out phonemes produces an **impression of an accent**, not a man who has one | **Name the region, delete the phonetics.** The accent is background, not a feature |
| 🔴 **"Weird"** | *"He speaks through his nose, chin lifted, jaw pushed forward"* — a nasal/adenoidal placement instruction, imported from the Suno rounds where it was fighting a music model | **Delete the placement clause entirely** |
| 🔴 **"Not clear"** | *Swallowed consonants* and *dropped H's* are literally instructions to articulate badly, and they were sitting next to a request for grit | **Ask for clear articulation.** Accent and diction are separate axes |
| 🔴 **"Boring"** | 🔑 **A stack of flattening instructions:** `bored` · `unhurried` · `130 words per minute` · `he leaves gaps and does not rush to fill them` · `never getting louder and never getting quieter`. That is a recipe for monotone, and `suno-narration.md` §4b caught the same class of bug at round 5 | See below |

### 🔑 The brief was there all along, and I drifted from it

[`../stories/camping/narration-brief.md`](../stories/camping/narration-brief.md) specifies:

> **Baseline `{FLAT}`** — certain, dry, **administrative**. The narrator knows how this ends.
> **One `{WARM}` crack, spent once.** **~155 words/minute**, *"and an **authoritative** voice sits
> under it."*

| The brief says | I was directing |
|---|---|
| **~155 wpm** | **130 wpm** — 16% slower than canon |
| **Authoritative** | **Bored** |
| **One warm crack** | No warmth anywhere |

🔑 **`bored` is not the same word as `dry`, and the difference is the whole problem.** Deadpan works
through **timing and contrast**, not through absence of energy. [`../voice.md`](../voice.md) is
explicit: *"overtly sarcastic, dark humour, **total authority**… nurturing underneath the snark."*
**A narrator who cannot be bothered is not in the house voice.** He is enjoying this; he simply
will not admit it.

## Where this lane sits

| Lane | What it is | Verdict |
| --- | --- | --- |
| **A real human reading it** | Jack, Kai, or £40–60 on Fiverr | 🥇 Still the highest-fidelity answer. `voice.md` has recommended it four times |
| 🆕 **Google AI Studio (this file)** | Prompt-to-voice + a large voice library, free on the Ultra account | 🥈 **Best synthetic result we have had.** Human-sounding out of the box; accent unproven |
| ElevenLabs | Voice Design + Text to Speech | 🔴 **Abandoned 2026-09-03** — could not hold the accent, and the free tier grants no commercial rights |
| Suno | Music generator asked to talk | 🔴 Closed — **Suno cannot make silence.** Fourteen rounds bought a voice, not a narration engine |
| Local clone (Chatterbox / Qwen3-TTS) | Clone the approved Suno take on the 4070 | 🟡 Still viable, still needs a clean reference clip, still rejected by ear once |

## Access and money — nobody is being charged

| Question | Answer |
| --- | --- |
| Do we have access? | ✅ Yes. UK is a supported region; any Google account, 18+ |
| Which account | **The Ultra account** (`jacktttt330@…`) — the same one Flow runs on |
| Cost of the AI Studio UI | ✅ **"Google AI Studio usage is free of charge in all available regions"** |
| What Ultra adds | Raised AI Studio quota (Pro/Ultra benefit, April 2026) — **web UI only, not API keys** |
| Also included, likely unclaimed | 💰 **$100/month Google Cloud credits** for Ultra ($10 for Pro), folded in 27 Jan 2026 |
| 🔑 How to be certain nothing bills | `aistudio.google.com/apikey` → **Billing Tier** column. **"Free tier / Set up billing"** means no billing account is attached and nothing can be charged. ✅ Confirmed on our key 2026-09-04 |
| ⚠️ Tokens ≠ money | The token panel is a **quota/context** meter. On a free-tier key, exhausting it returns `429`, never an invoice |
| 🔴 The one way to start paying | Clicking **"Set up billing."** Don't |
| Data terms on the free tier | ⚠️ **"Human reviewers may read, annotate, and process your API input and output"**, and content is used to improve Google products. Only a **billing-enabled** project opts out. Our scripts publish anyway |

## The UI map — observed live 2026-09-04

**URL:** `aistudio.google.com/generate-speech` · **Model:** `gemini-3.1-flash-tts-preview`
(Run settings → the model card). Left sidebar → Playground.

⚠️ **Blog write-ups describe a different, older screen.** Trust this map, or a screenshot, over
anything found on the web — including Google's own docs, which describe the API, not the UI.

### Two modes, top right

| Mode | Use |
| --- | --- |
| **Text** | One box. Fine for a quick test |
| 🥇 **Composer** | The real workspace: Scene, Sample Context, and per-speaker speech blocks. **Use this** |

### 🔑 The handover convention — every block is labelled with its field

**Standing rule, set 2026-09-04:** any paste block handed over for this engine carries its
destination as a heading — `→ VOICE DIRECTION`, `→ SCENE`, `→ SAMPLE CONTEXT`, `→ TRANSCRIPT`.
Never a bare block.

| Heading | Where it goes | What belongs there |
|---|---|---|
| **→ VOICE DIRECTION** | Right panel → the voice chip → **Speaker settings** → the top box | **Who the speaker is.** Accent, timbre, attitude, pace. The load-bearing field |
| **→ SCENE** | Composer, top of the page | **Where he is and how it was recorded.** Room and microphone only |
| **→ SAMPLE CONTEXT** | Composer, under Scene | **A one-line casting blurb** — what this voice gets hired for. Not direction |
| **→ TRANSCRIPT** | The speech block labelled `Speaker 1 — <voice>` | **The words, plus inline tags.** The only text that is spoken aloud |
| **→ VOICE** | Speaker settings → **Voice** / Search 5,000+ voices | A voice name, or a filter path |
| **→ TEMPERATURE** | Run settings → **Model settings** | A number. Default 1 |

🔴 **There is no "Director's Notes" field, and there is no "Audio Profile" field.** Google's
four-part structure is a way to organise **one prompt document**, not four inputs — in the API it
is a single string. The Composer surfaces **Scene** and **Sample Context** as their own boxes and
folds **Audio Profile + Director's Notes into VOICE DIRECTION**. Google's own wording: *"cast
characters using unique Audio Profiles, then specify Director's Notes to **toggle** pace, tone and
accent"* — 🔑 **the Style / Pace / Accent dropdowns beside the box are the Director's Notes, exposed
as controls.**

🔁 **The alternative, worth one A/B:** switch to **Text** mode (top right) and paste Google's whole
markdown document — `# AUDIO PROFILE`, `## THE SCENE`, `### DIRECTOR'S NOTES`, `### SAMPLE CONTEXT`,
`#### TRANSCRIPT` — as a single prompt. ⬜ **Untested.** That is the exact shape of their worked
example, and the Composer may be splitting it in ways the model was not tuned for.

🔴 **Nothing else is ever spoken.** Wrapper lines (`SCRIPT TO READ:`), wrapping quotes and a
trailing `Thanks.` all get read aloud if they land in the transcript box. The *"end every prompt
with Thanks"* rule belongs to **Flow** and has no place here.

### Composer fields — and what actually belongs in each

| Field | Google's definition | What we put there |
| --- | --- | --- |
| **Scene** | *"the physical environment and emotional vibe"* | The room and the mood. Short. ⚠️ See the reverb trap below |
| **Sample Context** | *"a contextual starting point, so your virtual actor enters the scene naturally"* | A one-line **casting blurb** — what this voice is typically hired for. 🔴 **Not the direction.** Ours was in here at first and it was the wrong field |
| **Speech block** (`Speaker 1 — <voice>`) | The transcript | The words only, plus inline tags |
| **+ Add speech block** | — | Second speaker, or a deliberate hard break between passages |

### Speaker settings (right panel → the voice chip)

| Control | Notes |
| --- | --- |
| 🔑 **VOICE DIRECTION** | *"Describe the voice persona."* **The load-bearing field.** Persona + accent + style + pace go here |
| **Style / Pace / Accent** dropdowns | Presets sitting beside the box. ⬜ Unverified whether they beat writing the same thing in prose. Google's own rule says **specific beats generic**, so prose with a place name is the safer bet |
| 🔑 **Voice** — *"Search 5,000+ voices"* | Filters: **Language · Accent · Gender · Age · Style · Use case**. Groups seen: *Featured* (Charon, Kore, Puck), *Studio classics* (Achernar, Achird, Algenib…), *Narration* (Alnilam…) |
| 🥇 **+ New voice** | ✅ **Opened 2026-09-04 — it is Voice Design *and* cloning.** See "the copy route" below. This is the most important control on the screen |

🔴 **The 5,000-voice library is bigger than anything documented.** Every write-up and Google's own
API docs say **30 prebuilt voices** (Zephyr, Puck, Charon, Kore … Sulafat). The UI says 5,000+ with
an **Accent filter**. **The UI is the truth; the docs describe the API.** This is the single most
valuable thing on the screen and no article mentions it.

### Run settings

- **Model settings** contains **Temperature only** (default 1). 🔴 **No voice picker lives here** —
  the voice is on the speaker chip.
- **Get code** exports the session as an API call. ⚠️ That path is billed separately and gets **no**
  Ultra benefit.

## The prompt structure — Google's own four parts

Google's worked example ("Jaz R.", a Brixton radio DJ) maps 1:1 onto the Composer fields:

| Part | Definition, verbatim |
| --- | --- |
| **Audio Profile** | *"Briefly describe the persona of the character"* — name, role, archetype |
| **Scene** | *"location, mood, and environmental details that establish the tone and vibe"* |
| **Director's Notes** | *"specific performance guidance"* — **Style, Pacing, Accent** |
| **Sample Context** | *"helps the model enter the scene you set up naturally"* |
| **Transcript** | the spoken words, with inline tags |

### The three rules that matter

1. 🔑 **Be specific about accent, geographically.** Google: *"British English accent as heard in
   Croydon, England"* beats *"British accent."* **Name a town, never a nationality.**
2. ⚠️ **Do not overspecify.** *"You don't need to describe everything, the model will fill in the
   gaps."* Over-direction reduces naturalness — which is the exact quality we just won.
3. **Keep script and direction coherent.** A persona that contradicts the words fights the read.

## 🎭 The unnamed-reference technique — carried over, and it still applies

`voice.md`'s rule stands on this engine: **name a real person to yourself, never to the engine.**
*"Cloning-of-real-people filters trip on names, and descriptive traits steer better anyway."*
The camping brief is already built this way — the O2 voiceover for the throat, the gravel-baritone
comedic lead for the smirk, **neither ever named in a prompt**.

### The Mancunian direction — the reference, described, never named

> **The references (internal only), and the split:** the gravel-baritone comedic lead
> (Lego Batman / BoJack) gives the **timbre and the timing**; the Burnage frontman gives the
> **sneer**; the O2 voiceover (Sheffield, South Yorkshire) gives the **accent and the warmth**.
> **Never put any of those names in the box.** `voice.md`: *"cloning-of-real-people filters trip on
> names, and descriptive traits steer better anyway."*

🔑 **Three references, three jobs — keep them separate.** `voice.md`'s two-way rule (*"one gives
the throat, the other gives the smirk"*) extends: ask for all three at once as a blur of adjectives
and you get a bad impression of one of them.

🔴 **Accent is Sheffield, not Manchester.** A broad Mancunian articulation stack (nasal, adenoidal,
snarled through the nose) came back **too northern** on 2026-09-04 — it reads as an impression.
South Yorkshire flattened vowels carry the class without the caricature, and it is what
`voice.md`'s brief specified all along.

🔑 **Written in Google's own headed shape**, not flowing prose — the Jaz R. example is markdown
sections with `Style / Accent / Pace` sub-bullets and a **named persona**, and that structure is
the part of the documented method we had not used.

**→ VOICE DIRECTION**

```
# AUDIO PROFILE: Gaz M.
## "The man who already knows how it ends"

A working-class northern Englishman in his forties. Not a presenter and not a performer — a bloke telling you something across a table, who happens to have been right about all of it.

### DIRECTOR'S NOTES

Style:
* The permanent smirk: you should be able to hear the curled lip. Bored, cocky and completely unbothered, and he finds the man he is describing beneath contempt.
* The underplay: he throws every punchline away rather than landing it, and delivers sarcasm as if it were a weather report. He never signals that something is funny.
* The grain: a gravelly voice with real grit and a little smoke in it, worn and lived-in — but never boomy, never an announcer, never a movie trailer.
* Placement: he speaks through his nose, chin lifted, jaw pushed forward, like a man answering a question he resents.

Accent: Gaz is from Salford, Greater Manchester. Hard flat northern vowels, a short hard "a" in bath and last, drawn out and leaned on and drooping at the ends of words. Swallowed consonants, dropped T's and dropped H's. Never Received Pronunciation, never London, never American.

Pace: Slow and unhurried, around 130 words per minute. Ordinary conversational speech with uneven sentence lengths. He leaves gaps and does not rush to fill them, and every full stop is a real stop with a breath in it. His pitch swoops up inside a sentence and drops away at the end of it — never droning, never on one note.
```

**→ SCENE**

```
A small back room, late. One man and one microphone. Recorded like a voice memo: close and dry right on the mic, unproduced, no room and no echo on him at all. No music, no audience, nobody to play to.
```

**→ SAMPLE CONTEXT**

```
Gaz is the voice you hire for dry British satire — dark comedy, kitchen-sink documentary, deadpan political commentary. He reads out facts he finds contemptible without ever once raising his voice about them.
```

### 🔴 Two clauses the Suno rounds ruled OUT — do not reintroduce them

| Do not write | Why | Source |
|---|---|---|
| **"almost no pitch movement" / "flat" / "level"** | Produced an outright **monotone** at round 5. The target is the opposite: *"his pitch swoops up inside a sentence and drops away at the end"* | `suno-narration.md` §4b |
| **"mouth barely opening"** | Physically contradicts *"vowels drawn out and bent"*, and both are articulation clauses — the strongest lever we have. Two of them cancel | Round 19 |
| **"in his fifties"** | Round 19 settled on **forties** | Round 19 |

⚠️ **Try the Accent filter first anyway.** Filtering the 5,000-voice library to a real northern
English male narrator **copies** an accent; the prose above **invents** one. Every previous engine
in this investigation failed at inventing.

## 🔴 FOUND 2026-09-04 — Voice Direction has a ceiling, and it is the accent

**Jack, after four rewrites: *"it didn't change the voice much."*** ✅ **That is documented
behaviour, not a wording failure.**

| Finding | Source |
|---|---|
| 🔑 **Style instructions steer *delivery and tone*, not *timbre and accent*** | Google's own framing: *"describes speaking style, tone, and emotional delivery… beyond default narration"* |
| Accent requests in the style field can fail outright | Developer forum: *"In English with Indian accent"* returned **no audio at all** |
| The selected voice is not always the voice you get | Forum: *"the generated audio often comes out in a completely different voice than selected"* |
| Run-to-run drift | *"calling the model twice with the same voice ID, text and settings, the second clip can come back… different accent, pacing, or timbre"* — **judge on two takes, never one** |

🔑 **`voice.md`'s standing ruling, holding on a fourth engine:** *every route that works COPIES an
accent; none invent one.* **The difference here is that the copy route is free and built in.**

**The order of levers, corrected:**

1. 🥇 **Voice Design + an audio reference** (`+ New voice`) — the copy route. See below.
2. 🥈 **The voice library's Accent filter** — 5,000+ voices, filter to the accent.
3. 🥉 **The Accent dropdown** beside Voice Direction — a structured parameter beats prose.
4. 🔴 **Temperature does nothing.** Google: *"The API ignores the `temperature`, `top_k` and `top_p` generation config parameters in the request."* The slider is in the UI and is inert for TTS.
5. ✍️ **Prose** — last, not first.

### 🔑 The prompt lever nobody has pulled — the transcript fights the direction

Best practice for this model: **align style prompt, text content and inline tags** — *"a tense
prompt paired with neutral, meeting-style text will produce muddled results."*

🔴 **Our transcript is neutral, meeting-style text.** `suno-narration.md` round 19 measured it:
**420 words of formal standard English with zero northern coding** — `does not` ×2, `Cannot`,
`It is`, not one contraction, plus `pain infliction`, `banal`, `warrant`, `acknowledgement`.
Round 19 parked the fix as *"round 20 if round 19 misses."* **It missed. This transfers here
unchanged.** The fix is **elision, not rewriting** — and every substitution is Jack's call.

## 🥇 THE COPY ROUTE — "+ New voice" is Voice Design **and** cloning

**Screen: `Create voice · Voice Design`.** Three controls and an audition pane:

| Control | What it is |
|---|---|
| **Describe it** | A prose box, prompted with its own field order: *"Timbre and weight, age, gender, pitch, pacing, accent, tone, delivery quirks. The more specific, the better the result."* |
| 🥇 **Add audio reference** | **Upload a clip.** Cloning — free, inside the tool we are already in |
| **Enhance with Gemini** | Expands the description for you. ⚠️ Skip on the first pass: it generalises, and *generic* is what has killed every accent attempt so far |
| **Generate voice** | Returns **three takes to audition** |

🔑 **Write the description in the field's own stated order** — timbre and weight → age → gender →
pitch → pacing → accent → tone → delivery quirks. Same trick `voice.md` used on ElevenLabs
(*"structure follows ElevenLabs' documented order exactly"*), and it is free to obey.

🥇 **The audio reference is the answer, and we already own the asset.** **Round 13's Suno take is
the one Jack called "spot on" — right accent, right age, right class.**

**What the reference clip has to be** (round 19's clone rules, unchanged):

- **Fifteen clean seconds beat sixty contaminated ones.** One consistent register throughout — a
  clip that switches register clones unstable.
- 🔑 **Use the vocal stem, not the mix.** Suno always puts a bed under it, and the bed is exactly
  what must not be cloned.
- 🔴 **A human downloads it.** Suno caps downloads per month and that allowance is never spent by
  automation.
- 🔴 **Never upload a real person's voice.** References stay described, never cloned — consent-only,
  and `voice.md` rules it out for the same reason.

### → DESCRIBE IT

```
Timbre and weight: a gravelly voice with real grit and a little smoke in it, worn and lived-in, mid-weight — never boomy, never resonant like an announcer, never a movie trailer. Age: forties. Gender: male. Pitch: mid-range to lower-middle, never a deep bass or a plummy baritone. Pacing: slow and unhurried, around 130 words per minute, ordinary conversational speech with uneven sentence lengths; he leaves gaps and does not rush to fill them, and every full stop is a real stop with a breath in it. Accent: working-class northern English, from Salford in Greater Manchester — hard flat vowels, a short hard "a" in bath and last, drawn out and leaned on and drooping at the ends of words, swallowed consonants, dropped T's and dropped H's. Never Received Pronunciation, never London, never American. Tone: bored, cocky and thoroughly unimpressed, deadpan and certain, with a warmth underneath that he would deny. Delivery quirks: he speaks through his nose with his chin lifted and his jaw pushed forward, a curled lip on every line; his pitch swoops up inside a sentence and drops away at the end of it, never droning and never on one note; he throws every punchline away instead of landing it and never once signals that something is funny.
```

**Audition the three takes on one line only** — `voice.md`'s test, the driest thing in the script:

> *"I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit."*

Flat and amused is the narrator. Any lift, any grandeur, any sense that it knows it is funny is
wrong, however good the timbre.

### 🔴 CLOSED 2026-09-04 — Voice Design is allowlisted, and money does not open it

**Both attempts failed with `Failed to generate voice: Precondition check failed`** — the full
description *and* a two-word one. **Same error, so the feature is gated, not the prompt.**

| Finding | Source |
|---|---|
| 🔑 **Google's custom-voice products are allowlisted** — *"access… is restricted to allow-listed users, and to request access, you must contact a member of the sales team"* | Chirp 3: Instant Custom Voice docs |
| **Consent verification is part of the product**, not a formality — the voice actor must record a Google-chosen sentence (*"I agree that my voice will be used to create a synthetic custom Text-to-Speech voice"*) | Same |
| There is an **ethics review** against Google's AI Principles | Same |
| Instant Custom Voice is priced at **$60 per 1M characters** | Same |

🔴 **So enabling billing will not unlock this**, and the $100 Ultra credits are not the answer to
this particular door. **Do not attach billing on the strength of it.**

⚠️ **One door it does leave open, later:** the consent flow is designed for *a real person who
agrees* — which is exactly `voice.md`'s £0 route (Jack, Kai, or a paid northern reader). If we ever
want a permanent BadCode narrator voice, that is the legitimate path, and it starts with contacting
sales rather than clicking a button.

### 🔴 UNRESOLVED — can we publish audio made on the free tier?

⚠️ **One secondary source claims *"free-tier output isn't licensed for commercial use — production
audio for commercial purposes requires paid Cloud Billing."*** That **contradicts** the Gemini API
terms, which say Google *"won't claim ownership"* of generated content on either tier.

🔴 **Unverified in both directions, and it matters — BadCode publishes.** This is the same shape as
the ElevenLabs free-tier problem `voice.md` found late. **Settle it against Google's own terms
before any AI Studio narration ships**, not after.

### Which prebuilt voice, if you are not designing one

| Voice | Google's label | For this narrator |
|---|---|---|
| **Charon** | Informative, lower pitch | 🟡 The documentary default. Clear, neutral, safe — and *neutral* is what this brief is not |
| 🥇 **Algenib** | **Gravelly**, lower pitch | Closest to the gravel-baritone reference |
| **Alnilam** | Firm — filed under **Narration** in the UI | 🟡 Worth a pass |
| **Orus** | Firm | 🟡 Also recommended for narration |

⚠️ **The documented accent set is RP and Brixton. No northern English variant is named anywhere in
Google's docs** — which is exactly why Voice Design and the Accent filter matter more than the prose.

## 🔑 ALL FOUR FIELDS VOTE — run the box audit before every generation

`suno-narration.md` round 19's most transferable finding: **count the accent-coded tokens per box.**
There, the Exclude box was voting **9-to-2 against** the accent the Style box was asking for, and
nineteen rounds of rewording never found it because nobody counted.

**The same audit on this engine, 2026-09-04:**

| Field | Accent-coded | Neutral | Verdict |
|---|---|---|---|
| **Voice Direction** | `northern` ×2, `Salford`, `Manchester` | — | ✅ Strong |
| **Scene** | none | *"a small back room"* | 🔴 A free vote, unspent |
| **Sample Context** | `British` ×1 | *dark comedy, documentary, political commentary* | 🔴 Outvoted 3-to-1 in its own box |
| **Transcript** | `bloke` | 420 words of formal standard English | 🔴 The biggest box, voting neutral |

🔑 **Two rules out of it:**

1. **Never let a field sit neutral.** A neutral field is not silent — it votes for the model's
   default, which is General American. Put the town in the Scene. Put the accent in the casting
   blurb.
2. 🔴 **Never request and ban the same axis.** Round 19 caught `flat` being asked for and banned at
   once. **The live example on this engine is `deep`**: *"a deep gravelly voice"* alongside
   *"never boomy, never an announcer, never a movie trailer"* is the same self-cancelling pair, and
   `voice.md` names the reason — *both references sit low and the model will chase movie-trailer if
   you let it.* **State it as pitch, not as an archetype:** *"pitched low, at the bottom of his
   natural speaking range, not a performed bass."*
3. ⚠️ **One name, everywhere.** A profile called `Gaz` with a casting blurb about `Terry` is the
   documented top mistake — *"misaligning character identity with transcript content."*

## Chunk or whole script? — test in chunks, deliver in one pass

| | |
|---|---|
| **While auditioning a voice** | 🥇 **One short chunk.** Fast, and the whole script tells you nothing chunk 1 does not |
| **Once the voice is right** | 🥇 **The whole script, one generation.** 439 words ≈ 3 minutes, well inside the 16,384-token output ceiling |
| **Why one pass wins** | 🔑 **Run-to-run drift is documented** — the same voice, text and settings *"can come back… different accent, pacing, or timbre."* Six chunks means six chances to draw a different narrator, and there is no request-stitching to paper over the seams |
| **When to split anyway** | ⚠️ Google warns quality *"may drift"* past a few minutes. If it wanders, split at a **scene boundary**, never mid-beat |
| **Pauses** | `[long pause]` can execute `forms.md`'s `//` marks in the read — but the `12d` tilt is timed to the last word, so ⚠️ **keep timing pauses in the Premiere edit** and use tags only for comic beats |

## 🔑 THE PROMPTING RULES THAT ARE NOT IN GOOGLE'S DOCS (LiveKit, 2026)

Found 2026-09-04 in [LiveKit's practical prompting guide](https://livekit.com/blog/gemini-3.1-flash-tts-prompting-guide).
**Several of these contradict what we had been doing**, and one of them explains "boring" outright.

| Rule | Why it matters here |
|---|---|
| 🔴 **Never use flatness-inducing words** — *"quiet", "flat", "no rush", "whispered"* | ✅ **This is the "boring" diagnosis, independently confirmed.** `unhurried`, `leaves gaps`, `does not rush to fill them` are all this class. **Frame direction positively instead** — *"warm and sincere"*, *"patient"*, *"full of feeling"* |
| 🔴 **Do NOT use `DIRECTOR'S NOTES` as a section label** | We had been using it verbatim. Use **`### PERFORMANCE`** and **`### CONTEXT`** |
| 🔴 **Avoid apostrophes and multi-word section headers** | Which is *why* `DIRECTOR'S NOTES` fails — the apostrophe |
| 🔑 **A "do not speak the directions" preamble is load-bearing** | *"Synthesize speech for the performance defined below… Speak ONLY the lines under #### TRANSCRIPT."* Prevents direction bleeding into the read |
| 🔴 **Never quote literal transcript words inside a style note** | e.g. *"lean on the word banal"* — it gets spoken |
| 🔑 **Punctuation shapes the music** | **Commas** between tagged clauses; **periods only at real sentence endings**; **ellipses** (1–2 per utterance) for trailing pauses; **em-dashes** for micro-pauses. *"Period-separated fragments sound choppy"* — 🔴 **and our script is almost entirely period-separated fragments.** A second, separate cause of "boring" |
| 🔑 **Custom EMOTION tags are weak; custom non-emotional modifiers are strong** | *"Custom emotional adjectives receive insufficient training coverage"*, while *"custom non-emotional modifiers like `[whispers]` or `[like a cartoon dog]` work well."* 🔴 **So `[understated]` and `[matter-of-fact]` are the weak kind.** Prefer the proven set: `[warmly]`, `[thoughtfully]`, `[sighs]`, `[gently]`, `[soft laugh]`, `[cheerfully]`, plus Google's `[sarcastic]`, `[serious]`, `[slow]` |
| ⚠️ **Failure modes** | CONTEXT bleeding into TRANSCRIPT when section boundaries are vague; empty responses and 500s (retry with backoff); **phonetic collisions between the character name and the opening word** |
| **Length** | Examples run **200–400 words** for a full profile |

### ✅ And accent steering IS reliable — tested independently

Simon Willison, testing 3.1 on launch day, swapped the accent line from **Brixton** to **Newcastle**
to **Exeter, Devon** and got *"noticeably different vocal outputs, indicating reliable accent
directionality."* 🔑 **So naming a northern city does work.** Our failures were the phonetic stack
and the flatness words, not the accent request itself.

## 🎭 The storybook register — a Manchester version of the Ted opening

🔴 **Never name the actor.** Google enforces a **"prominent individuals"** filter across the
platform, and Gemini TTS *"ships preset voices only… as a compliance measure."* Naming him gets the
prompt blocked, exactly as `voice.md` predicted for every other engine.

**What the reference actually is, described:** a classically trained stage actor reading a
children's storybook aloud — grand, warm, avuncular, generous rise and fall, every word savoured —
delivering filth and cruelty with **total sincerity and no wink whatsoever.** The joke is entirely
in the gap between the register and the content.

🔑 **Why this fixes three problems at once:** storybook narration is **musical** (kills "boring"),
**precisely articulated** (kills "not clear"), and **warm** (kills "weird") — while the *content*
supplies all the contempt the brief wants, so the voice never has to sound bored to deliver it.

## 🔴 RULED 2026-09-04 — the prompt cannot change the voice. Only the voice name can.

**Jack, after ten prompt rewrites: *"it keeps making similar voices."*** ✅ **Structurally correct,
and now documented rather than inferred:**

> **`voice_name` determines the base voice and timbre. The prompt steers style, tone, accent, pace
> and emotion — the *delivery*.**

🔑 **We changed the direction ten times and the voice never once.** Every rewrite was pulling the
one lever that cannot move timbre. **The fix is one word in the Voice field.**

🔴 **And temperature is inert here.** Google: *"The API ignores the `temperature`, `top_k` and
`top_p` generation config parameters in the request."* The slider exists in Model settings and does
nothing for TTS — **do not spend a round on it.**

### The 16 male voices, for deliberate contrast

`Achird` · `Algenib` · `Algieba` · `Alnilam` · `Charon` · `Enceladus` · `Fenrir` · `Iapetus` ·
`Orus` · `Puck` · `Rasalgethi` · `Sadachbia` · `Sadaltager` · `Schedar` · `Umbriel` · `Zubenelgenubi`

⚠️ **Charon measures as an American male at ~160 wpm and ~152 Hz** — which is the family we spent
the day trying to drag to Manchester. **Algenib sits in the same low, grave family.** If two voices
have produced "similar", the answer is to jump family, not to rewrite the notes: **`Puck` (Upbeat)**,
**`Fenrir` (Excitable)**, **`Zubenelgenubi` (Casual)** and **`Iapetus` (Clear)** are the far end.

### 🎭 The register swing — the induction-video narrator

When the *grave* register has been tried five ways, **invert it.** A bright, brisk, relentlessly
pleasant corporate-onboarding voice describing asset stripping and homelessness is the opposite
comedic engine from a grizzled narrator, and it is arguably more BadCode: **it is the system
narrating itself.** [`../voice.md`](../voice.md) gets its sarcasm from register mismatch, and
`story-craft`'s rule holds — the irony is safe because **the picture supplies the undeniable
consequence** the words refuse to acknowledge.

## 🔑 RULED 2026-09-04 — the missing ingredient was ANGER, and it is the cure for "boring"

**Jack, on the induction-video swing: *"it is not very BadCode, it needs to be gritty, deadpan, with
a hint of sarcasm and anger."*** 🔴 **The register inversion is rejected — do not retry it.** A
cheerful corporate narrator is a legitimate comedic engine and it is not this house's.

🔑 **And the note names the thing every previous direction was missing.** Every block so far asked
for **bored, unbothered, cannot be bothered, beneath contempt** — all of which are *absence* of
feeling, and absence of feeling is exactly what came back as **"boring"**.

> **Deadpan is a lid on something, not an absence of it.** The flat delivery only reads as deadpan
> if there is visible pressure underneath it. Ask for the pressure, not the flatness.

**The house voice agrees, and always did.** [`../voice.md`](../voice.md): *"overtly sarcastic, dark
humour, **total authority**… nurturing underneath the snark. **The contempt is for the mistake, not
the people.**"* That is not boredom. **That is anger with manners.**

| Ask for | Not |
|---|---|
| Anger banked down and held still | Boredom |
| Sarcasm used as a weapon | Sarcasm as a joke |
| Tightening under pressure | Getting louder |
| Control | Flatness |

⚠️ **Say it as pressure, never as flatness** — LiveKit's rule bans *"quiet", "flat", "no rush"* as
flatness-inducing. **"Banked", "contained", "held", "compressed", "clipped" are all safe** because
they describe force being restrained rather than force being absent.

## 🔑 PACE — the wpm number is the weakest of the three levers

**Jack, on the Mac take: *"he talks way too slow."*** ✅ **And a number in the Pace section is the
least of what controls it.** Three levers, weakest first:

| Lever | Strength | Notes |
|---|---|---|
| **A words-per-minute figure** in the Pace section | 🟡 Weak | The model has its own native rate — Charon measures ~160 wpm — and a number nudges it rather than setting it |
| 🔑 **The transcript's punctuation** | 🥇 **Strongest** | LiveKit: *"period-separated fragments sound choppy"*, and every full stop is honoured as a stop. **Our script is almost entirely fragments.** Joining them with **commas and em-dashes** removes the brakes the model is obeying |
| 🥈 **The `[fast]` pacing tag** | Strong, documented | Google's pacing set is `[slow]`, `[fast]`, `[short pause]`, `[long pause]`. One `[fast]` at the head of the transcript is a direct instruction |
| ⚠️ **Any clause implying space** | Silent brake | *"every full stop is a real stop with a breath in it"*, *"he leaves gaps and does not rush to fill them"* — both were in earlier blocks and both are drag |

⚠️ **Note against canon:** [`../stories/camping/narration-brief.md`](../stories/camping/narration-brief.md)
sets *"~155 words/minute"* as a **ceiling**. Running faster than that is a deliberate departure —
**Jack's call, made by ear 2026-09-04** — and it shortens the film, so
[`../stories/camping/edit-plan.md`](../stories/camping/edit-plan.md) timings move with it.

## 🔴 RULED 2026-09-04 — northern is DROPPED. Ask for an accent the model already does.

**Jack: *"forget the northern thing, do any accent that works."*** ✅ **And this closes a question
`voice.md` opened on 2026-09-03 and never got a ruling on:** the northern accent **was never canon**
— not in [`../voice.md`](../voice.md), not in
[`../stories/camping/narration-brief.md`](../stories/camping/narration-brief.md). It arrived as a
preference during the Suno casting rounds and, in that page's own words, *"has now cost more than
every other decision on this film combined."* **It is now formally dropped.**

### Which accents actually work — the evidence, ranked

| Accent | Evidence | Verdict |
|---|---|---|
| 🥇 **Brixton / South-East London** | **Named in Google's own worked example** (*"Jaz is from Brixton, London"*) and in the documented accent set | **The safest British option**, and native to a film set around the NatWest floor, the Shard and a Waitrose car park |
| 🥈 **General American** | 🔑 **The model's native default** — Charon measures as an American male. And [`../stories/karen/narration/voice.md`](../stories/karen/narration/voice.md) already casts the BadCode narrator as *"General American with a faint Western ease"* | `voice.md`'s own post-mortem: *"Karen's target IS the model's default. Camping's is the opposite of it."* **Karen worked. That is the reason** |
| **RP · Estuary · Transatlantic** | In the documented set | Available; RP is wrong for the reader |
| **Newcastle · Exeter** | Simon Willison got *"noticeably different vocal outputs"* swapping these in | Steering works — but these are **undocumented**, i.e. what we spent a day failing at |

🔑 **Two house rules out of the whole day:**

1. **Ask for an accent the vendor advertises.** Every documented accent landed; every undocumented
   one produced either a caricature or the default.
2. **Name the place, never the phonemes.** Spelling out vowels and dropped consonants produced
   *"too northern"* twice and *"weird"* once. The city name alone is the whole instruction.

## 🔑 Three dials that are easy to confuse — placement, melody, and accent strength

Learned the hard way across 2026-09-04. **They are independent, and naming them separately is what
finally worked.**

| Dial | Say this | Never say |
|---|---|---|
| **Placement (how deep)** | *"The voice sits low, at the bottom of his natural range"* | `deep`, `bass`, `baritone`, `booming` — archetypes that summon a movie-trailer read and cancel against `never boomy` |
| **Melody (how animated)** | *"Wide, lively intonation — his pitch lifts and swoops up inside a sentence before dropping away at the end"* | `flat`, `level`, `monotone`, `never getting louder` — all flatness-inducing |
| **Accent strength** | *"a mild, everyday <city> accent, the kind nobody would remark on"* | Phoneme lists — dropped H's, swallowed consonants, flattened vowels. **Every "too over the top" note traces to these** |

🔑 **Low placement plus wide melody is a real combination and has to be asked for as two clauses.**
Ask for depth alone and you get a droning read; ask for melody alone and you get a light one.

🔑 **The pitch label in the voice list is the authority on depth, not the prompt.** The UI tags every
voice — *"Charon · Informative · Lower pitch"*, *"Achird · Friendly · Lower middle pitch"*. **If a
take is not deep enough, change the voice, not the words** — `voice_name` owns timbre.

## 🎭 The portentous-author register — researched properly 2026-09-04

🔴 **The name never goes in the box.** Google runs a **"prominent individuals"** filter, and
[`../stories/camping/narration/voice.md`](../stories/camping/narration/voice.md) already rules that
**living performers are described, never cloned**. What follows builds the *register* — the
delivery, the emphasis pattern, the texture — not the individual's identifiable voice.

### 🔑 The three facts that make this directable

| Fact | Why it is the whole engine |
|---|---|
| 🥇 **The low voice is an AFFECTATION.** The performer is *"channelling the look and **low voice of 80s horror novelists**"* | **He is doing an impression of what he thinks a serious author sounds like.** That is a directable idea, and it produces the stilted, pushed-down, over-solemn delivery that "just make it deeper" never will |
| 🥇 **The accent is ordinary and it is the joke.** The performer is from **Whitstable, Kent** — *"a neutral accent"* — and *"the accent comically undermines the pretentious, absurd and grandiose things the character says"*, carrying associations of *"an odd, imbecilic pub bore"* | 🔴 **So do NOT ask for a grand or posh voice.** Ask for an **ordinary south-east England / Estuary** accent saying enormous things. **Estuary is in Google's documented accent set**, which is why this register is likely to land where northern did not |
| **Wilful unawareness** — *"a conceited hack writer, blissfully (or wilfully) unaware of his lack of talent"* | Total conviction, no wink, no self-knowledge. The certainty is the comedy |



**What the register actually is, described:** a self-published horror author narrating his own
audiobook, who is entirely convinced he is a profound artist. **Total gravity, zero self-awareness.**
He delivers absurd and appalling material with the weight of scripture, leans hard on words that do
not deserve emphasis, and never once suspects he is funny.

🔑 **Why it fits the house better than anything tried today:** [`../voice.md`](../voice.md) asks for
**total authority** and *"story over sermon"*, and this register is authority taken past the point
of self-parody — which is a **joke the voice never has to tell**, because the certainty does it.
It also keeps the day's two hard-won ingredients: **grit** (it is a gravelly register by nature) and
**banked anger** (self-seriousness under pressure reads as fury, not boredom).

⚠️ **The one trade:** portentousness wants **emphasis**, and emphasis costs a little speed. Expect
to sit nearer **160 wpm** than 175, with the weight carried by hard stresses rather than by pauses —
**never by dead air**, which is the flatness trap again.

## 🔴 THE ACCENT DIAL OVER-FIRES — the pattern across every take on 2026-09-04

**Four accents asked for, four "too much" notes:** Salford *"too northern"*, Manchester *"too
northern and weird"*, Brixton *"too over the top"*, Estuary *"the accent is too much"*.

🔑 **The variable was never the accent. It was how much of the prompt was spent on it.** Every
block that came back over-cooked contained **three or more accent statements** — a city, a class
marker, a characterisation, and a `never` list — and the model summed them.

**The rule, ruled 2026-09-04:**

> **One short accent clause. No city if a region will do. No class marker. No colour. No `never`
> list.** The accent is a *setting*, not a *feature*, and every extra word turns it into an
> impression.

⚠️ **This overrides Google's "the more specific you are, the better" guidance for our use.** That
advice is written for someone who *wants* a strong regional performance. **We want an accent the
listener never notices** — the opposite target, and it needs the opposite dosage.

## 🔑 Two more traits of the portentous-author register (third research pass, 2026-09-04)

| Trait | Evidence | How to direct it |
|---|---|---|
| 🥇 **Breakneck exposition** | *"Garth delivers voiceovers at breakneck speed whilst the screen displays stills of inanimate objects"*, and the register *"varies between measured, pompous narration and rapid-fire exposition"* | **Speed is not the opposite of gravity here — it is part of it.** Ask for rapid-fire delivery with the weight carried by hard stresses. This resolves the pace fight we had all day |
| 🥇 **It sounds dubbed on afterwards** | The show's texture comes from ADR — *"voices constantly losing sync with mouths"*, creating an *"intentionally awkward, stilted feel"* | Ask for a read that sounds **recorded separately from the picture**: close, dry, flat-fronted, slightly detached from what it is describing. It is an uncanny quality and it is directable |
| **Grandiosity** | *"author, dreamweaver, visionary… plus actor"* | Self-aggrandising conviction, stated as fact |

🔴 **On "make it sound exactly like him":** not achievable in this tool and not our route.
Gemini TTS *"ships preset voices only… as a compliance measure"*, the platform runs a **prominent
individuals** filter, and [`../stories/camping/narration/voice.md`](../stories/camping/narration/voice.md)
already rules that **living performers with commercial voice careers are described, never cloned**.
**What is achievable is the register**, built from observed traits — and the traits above are
specific enough to get most of the way.

## 🔴 STOP RULE HIT 2026-09-04 — twelve prose rounds, and the last edit changed nothing

**Reverting to an earlier block produced no audible change.** That is the signal: **prose is
saturated.** Delivery nuance no longer moves the output because `voice_name` owns the timbre and we
have been editing the wrong lever for a dozen rounds.

🔑 **The house already has the rule, from the Suno toolkit:**

> *"If a vocal hasn't moved after ~2 rounds of style-prompt surgery, stop prompting — the voice you
> want probably isn't in the genre's vocalist pool, and no adjective stack jumps pools."*

**We are ten rounds past it.** Same failure, different engine.

### 🔴 The thing never tried in fifteen rounds: casting

**The voice library has 5,000+ voices with Language / Accent / Gender / Age / Style / Use case
filters, and it has not been opened once.** Every round has been spent rewriting notes for one of
six prebuilt voices.

| Untried male prebuilts | `Achird` · `Algieba` · `Alnilam` · `Fenrir` · `Iapetus` · `Rasalgethi` · `Sadachbia` · `Schedar` · `Umbriel` · `Zubenelgenubi` |
|---|---|
| **Untried entirely** | 🥇 **The 5,000-voice library.** Search `gravelly`, filter Style and Use case, audition |

**Ruling: casting beats directing on this engine.** Change the voice, keep the notes frozen.

## 🔴 BOTH LEVERS ARE WEAK ON THIS ENGINE (2026-09-04)

**Jack, after changing voices several times: *"it only makes a small difference."*** So neither
`voice_name` nor the prompt moves it far. **The engine has a house sound and everything lands near
it.** That is the finding, and it is worth more than another round.

### What is still genuinely untried, cheapest first

| Lever | Cost | Why it might matter |
|---|---|---|
| **The Style / Pace / Accent dropdowns** | 1 min | Structured parameters, never touched. They may bind harder than prose |
| 🥇 **Text mode instead of Composer** | 2 min | Paste Google's whole worked-example document as **one prompt**. LiveKit says the preamble and exact section delimiters are load-bearing — **Composer splits them into fields, and the model was never tuned on that split** |
| 🥇 **A different TTS model** | 5 min | `gemini-2.5-flash-preview-tts` and `gemini-2.5-pro-preview-tts` are **different models with different instruction-following**, and neither has been tried. ⚠️ Pro may be behind billing since May 2026 — it fails instantly if so |
| 🥈 **Post-process the best take** | 20 min | If the *performance* is close and the *voice* is not, [`../video-fx/ffmpeg-catalogue.md`](../video-fx/ffmpeg-catalogue.md) has pitch/formant shift, saturation for rasp, and EQ for chest. **Shape it in post instead of prompting for it** |
| 🥇 **Record the impression and clone it** | 30 min | 🔑 **An impression is a human performance.** Thirty seconds of a person *doing* it, cloned on Chatterbox (MIT) or Qwen3-TTS (Apache 2.0) on the 4070, delivers the accent, the pomposity and the timing at once — and settles the accent question permanently |

🔑 **The ruling this points at:** *"every route that works COPIES an accent; none invent one"*
([`../stories/camping/narration/voice.md`](../stories/camping/narration/voice.md)) extends to
**register**. A specific comic performance is not a describable set of traits — it is a
performance, and the only reliable way to get one is to record one.

## Audio tags — 200+, and ours are safe

- **Syntax:** `[tag] text [tag] text`. Square brackets, **separated by text or punctuation** —
  never two tags adjacent. Tags are **English-only** but work inside multilingual text.
- **Documented set includes:** `[sarcastic]`, `[serious]`, `[sighs]`, `[whispers]`, `[laughs]`,
  `[gasp]`, `[excited]`, `[curious]`, `[annoyance]`, `[amusement]`, `[tired]`, `[shouting]`,
  plus pacing tags `[slow]`, `[fast]`, `[short pause]`, `[long pause]`.
- ⚠️ **Custom tags are allowed but not equal.** Google says *"there are no limits to the tags you can use"* — but LiveKit's testing splits them: **custom EMOTION adjectives are weak** (insufficient training coverage), **custom non-emotional modifiers are strong**. 🔴 **`[understated]`, `[matter-of-fact]` are the weak kind.** Prefer documented tags.
- **Use them sparingly.** *"Tags work best for specific sections rather than entire transcripts."*
  Karen's rule — **one tag per paragraph, maximum** — transfers unchanged.
- 🔑 **Pacing tags are a real gain over ElevenLabs v3**, which has no break control at all.
  `[long pause]` can execute the `//` marks that [`../story-craft/forms.md`](../story-craft/forms.md)
  defers to the Premiere edit.

## Text normalisation — unchanged from the house rules

Spell it how it sounds, **before** synthesis, never after:
`ETFs` → `E.T.F.s` · `IPA` → `I.P.A.` · `1%` → `one percent` · `4x4s` → `Four by fours` ·
`Ayahuasca` → `ayawaska` · `2008:` → `Two thousand and eight.`

A digit-colon opening gets read as a label. A question mark lifts the pitch, which sounds eager —
**for a flat joke, use a full stop.**

## Limits and specs

| | |
| --- | --- |
| **Input limit** | **8,192 tokens** (3.1 Flash TTS). ⚠️ Smaller than 2.5's 32k |
| **Output limit** | **16,384 tokens** ≈ **10 minutes** of audio ⬜ *(token-per-second rate unverified)* |
| 🔑 **Our whole script fits in one pass** | 439 words ≈ 3 minutes. **No chunking, no stitching** — the thing ElevenLabs v3 flatly could not do |
| **Sample rate / format** | **24 kHz, 16-bit PCM.** ⚠️ Below the 48 kHz house delivery standard — resample on the way into Premiere and run [`../video-fx/delivery.md`](../video-fx/delivery.md) before anything ships |
| **Languages** | 70+, regional variants included |
| **Speakers** | Multi-speaker supported; **2 speakers** per the API docs ⬜ (the Composer's *Add speech block* may allow more — untested) |
| **Streaming** | ✅ Supported on 3.1; was not on 2.5 |
| **Watermark** | 🔴 **SynthID is embedded in the output.** Consistent with [`../using-ai.md`](../using-ai.md) — we disclose anyway — but know that the audio is detectably synthetic |
| **Not supported** | Caching, function calling, structured output, thinking, grounding, Live API |
| **Paid rate, if ever needed** | $20/M audio-output tokens (3.1) · $10/M (2.5 Flash TTS) — **pennies per pass** ⬜ *(estimate)* |

## Traps

| Trap | What happens | Fix |
| --- | --- | --- |
| 🔴 **Wrong surface** | Pasting a script at a chat/agent model returns **text**, or a description of a performance | Playground → the TTS model → **Composer** |
| 🔴 **Direction in the wrong field** | Persona text in *Sample Context* under-steers the read | Persona → **Voice Direction**. Casting blurb → Sample Context |
| ⚠️ **Describing the space** | `voice.md`: naming a room made a previous engine bake in **reverb** — *"bare room tone"* produced an echoing, processed voice | If a take sounds roomy, **empty the Scene field**. Say *close, dry, no room reverb* explicitly |
| ⚠️ **Wrapper text gets spoken** | `SCRIPT TO READ:`, wrapping quotes, and a trailing **`Thanks.`** are all read aloud | The transcript box holds **words only**. 🔑 The *"end every prompt with Thanks"* rule is a **Flow** rule and does not apply here |
| ⚠️ **Quality drift** | Google: quality *"may drift"* past a few minutes | Our script is 3 minutes; if it drifts, split at a scene boundary |
| ⬜ **Profanity** | Chunk 3 is *"Fuck me."* Untested on this engine | If it refuses: **swap the word, never asterisk it** |
| 🔴 **"Failed to generate voice: Precondition check failed."** (Voice Design, 2026-09-04) | `FAILED_PRECONDITION` means *"the request format may be fine, but you are not allowed to use that path from your current region or billing state."* 🔴 **Answered 2026-09-04: it is an ALLOWLIST, not billing.** A two-word description failed identically, so the feature is gated, not the text — and Google's custom-voice products are *"restricted to allow-listed users… contact a member of the sales team"*, with consent verification and an ethics review on top | 🔴 **Do not attach billing hoping to unlock it** — money is not the gate. Use the **Accent filter** instead: same copy route, free, no precondition |
| ⬜ **Text instead of audio** | Reported failure: the model occasionally returns text tokens and errors | Re-run |

## Verified vs read

| Claim | Status |
| --- | --- |
| AI Studio is free in the UK on this account; key shows **Free tier** | ✅ **Verified live 2026-09-04** (screenshot) |
| Composer field names and layout; Model settings holds Temperature only | ✅ **Verified live 2026-09-04** (screenshot) |
| The voice library says **5,000+ voices** with an Accent filter | ✅ **Verified live** — and 🔴 **contradicts every published source**, which says 30 |
| It sounds human rather than synthetic | ✅ **Verified by ear** (Jack, first take) |
| A named town steers the accent better than "British" | ⬜ **Read, not tested.** This is the next experiment |
| Custom audio tags perform rather than being spoken | ⬜ **Read, not tested** |
| Ultra raises the AI Studio quota for TTS specifically | ⬜ **Read.** No published per-model number; check `aistudio.google.com/rate-limit` |
| **+ New voice** is Voice Design + audio-reference cloning | ✅ **Verified live 2026-09-04** (screenshot) |
| Prose alone cannot move the accent | ✅ **Verified by ear** across four rewrites, and matches Google's own framing of the field |
| Ultra's $100/month Cloud credits are claimable | ⬜ **Read, not claimed** |

## Sources

- [Speech generation (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation) — the four-part
  prompt structure, the tag list, voices, the accent-specificity rule
- [How to prompt Gemini 3.1's new TTS model](https://dev.to/googleai/how-to-prompt-gemini-31s-new-text-to-speech-model-24bb) —
  🔑 the **full Jaz R. worked example** and the "don't overspecify" rule
- [gemini-3.1-flash-tts-preview model card](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview) — 8,192 in / 16,384 out
- [Gemini 3.1 Flash TTS on Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud) — 200+ tags, SynthID, 70+ languages
- [Pricing](https://ai.google.dev/gemini-api/docs/pricing) · [Billing](https://ai.google.dev/gemini-api/docs/billing) ·
  [Rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) · [Available regions](https://ai.google.dev/gemini-api/docs/available-regions)
- [Gemini API terms](https://ai.google.dev/gemini-api/terms) · [Data logging policy](https://ai.google.dev/gemini-api/docs/logs-policy) — the unpaid-services human-review clause
- [Google AI plans for developers](https://ai.google.dev/gemini-api/docs/google-ai-plans) — **UI only, not API keys**
- [GDP premium folded into AI Pro/Ultra](https://blog.google/innovation-and-ai/technology/developers-tools/gdp-premium-ai-pro-ultra/) — the $100/month credits
