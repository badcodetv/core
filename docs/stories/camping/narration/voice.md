# The narrator — camping

> **What this is:** the voice brief for the camping film's narration, 2026-08-31. The script's
> job list is [`../narration-brief.md`](../narration-brief.md); this is the *man reading it*.
> Karen's equivalent is [`../../karen/narration/voice.md`](../../karen/narration/voice.md) —
> **a different narrator**, deliberately (see the last section).

## 🔴 Higgsfield cannot design a voice from a prompt

Higgsfield Audio is **presets + cloning only**. It bundles four engines — **Eleven v3, MiniMax
Speech 2.8 HD, Seed Speech, VibeVoice** — with 40+ preset voices, per-line tone/speed/emotion
controls, and cloning from an uploaded or recorded sample. There is **no "describe a voice" box**.

So the prompt below is written to be used in one of three places:

| Route | Where the prompt goes | Trade |
| --- | --- | --- |
| **ElevenLabs Voice Design** | Verbatim, in the Voice Design prompt box | Proven — this is the Karen route. Costs ElevenLabs credits, and the voice lives in the ElevenLabs library, not Higgsfield |
| **MiniMax Voice Design** (platform.minimax.io or fal.ai) | Verbatim, as the `prompt`; preview text capped at **500 characters**; returns a reusable `voice_id` | Cheapest prompt-to-voice. Generate on MiniMax/fal, not inside Higgsfield |
| **Higgsfield preset library** | As **audition criteria**, not a prompt — search the library on the trait words and judge against the audition line below | Free, stays in one tool, but you take what's there |

⚠️ **Cloning the reference voices is not a route.** Higgsfield's terms are consent-only cloning,
and both references are living actors with commercial voice careers. Cloning a *consenting human
doing this read* — Jack, or anyone with the accent — is completely fine, and is the least
AI-sounding option on the table.

## The brief

A blend of two references. **Never name either to an engine** — cloning-of-real-people filters
trip on names, and descriptive traits steer better anyway.

| Reference | What we take from it |
| --- | --- |
| The O2 voiceover (Sheffield, South Yorkshire) | The **accent and the texture** — gravel, warmth, working-class Northern English, understated and trusted |
| The gravel-baritone comedic lead (Lego Batman / BoJack) | The **attitude and the timing** — deep, deadpan, a cocky glint, relishing a punchline by underplaying it |

The split is the whole trick: **one gives the throat, the other gives the smirk.** Ask for both
at once without splitting them and you get a bad impression of one of them.

**"Never boomy, never an announcer"** is a hard requirement and must be stated as a negative,
because both references sit low and the model will chase movie-trailer if you let it.

## The Voice Design prompt

```
British English. Northern English — a South Yorkshire, Sheffield accent, flattened vowels, working class. Not Received Pronunciation, not London. Male, late 50s to mid 60s. Perfect audio quality, studio quality.
Persona: a deadpan storyteller with a cocky glint, telling you exactly how it all turned out. Emotion: dry, amused, warm underneath the sarcasm.
A gravelly baritone with real grit and a little smoke in it — worn, lived-in and resonant, but never boomy and never an announcer. He speaks slowly and conversationally, unhurried, lands every sarcastic line completely flat, and underplays the punchlines rather than selling them. Fond of the listener, and thoroughly unimpressed by the man he is describing.
```

Structure follows ElevenLabs' documented order exactly: language and dialect first, then gender
and age, then quality, then persona and emotion, then timbre and delivery. MiniMax takes the same
text unchanged.

## Preview text

**Turn "Generate Preview Text" OFF** and paste this. Preview text must match the personality you
asked for, and longer text produces a more stable voice. 362 characters — inside MiniMax's 500 cap.

```
Meet Tarquin. In 2008 he was a star trader, betting heavily on leveraged E.T.F.s. Pain infliction usually looks this banal. Nice tie, though. Bob spends his days in an oh-so-luxury tent, taking any charitable beer donations he can get his hands on. I don't know what's worse. That his cause isn't supported much, or that his donors judge him for being an I.P.A. man.
```

Abbreviations are pre-normalised (`ETFs` → `E.T.F.s`, `IPA` → `I.P.A.`) because raw ones get
mispronounced. Do the same to the full script before synthesis: `2008` → `twenty oh eight`,
`4x4's` -> **`4 by 4's`** (ruled by Jack 2026-09-01 by ear; re-test per engine), `1%` -> `one percent`.

## Sliders

| Control | Set to | Why |
| --- | --- | --- |
| **Guidance Scale** (ElevenLabs) | **30%** | High guidance makes a voice sound artificial or robotic; ElevenLabs recommend *longer, detailed prompts at a lower guidance scale*, and this prompt is long and detailed. Band 20–40%. If it comes back generic go to 38% — never higher |
| **Loudness** | **centre (0)** | Neutral, ~−24 LUFS, audio unchanged. Loudness bakes into the **saved voice**; pushing it hot squashes dynamic range, which reads as synthetic. Level in Premiere instead |
| **Model, for the real reads** | **Eleven v3** | The one that responds to audio tags. Stability **Natural**, Similarity ~75, Style 0 |

## ⚠️ Never describe the space

**FX terminology — "reverb", "echo", "phone", "tape" — degrades the output.** This is what went
wrong on the Suno narration attempts, where asking for "bare room tone" produced an echoing,
processed voice. Say `studio quality` and you get dry and close for free.

## The audition line

Generate a shortlist, then judge every candidate on **one line only** — the driest thing in the
script:

> *"I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit."*

Whichever take lands that **flat and amused** is the narrator. Any lift, any grandeur, any sense
that it knows it's funny is wrong, however good the timbre. Second check, for the warmth the brief
spends exactly once: *"He takes the news well. Excuse the pun."*

### Searching the Higgsfield preset library instead

Audition on the same line. Search terms, in priority order:
`British` · `Northern English` · `gravelly` · `raspy` · `baritone` · `documentary narrator` ·
`deadpan` · `mature male` · `60s`. Accept a **generic Northern** if no Sheffield exists — reject
anything RP, anything Cockney, and anything that sounds like a trailer.

## 🇺🇸 → 🇬🇧 The MiniMax accent fix (2026-08-31)

**Symptom:** the prompt above, pasted into `minimax.io/audio/voice-design`, came back **American.**

### Why — five causes, in order of blame

1. **There is no accent lever to pull.** MiniMax's Voice Design API takes only `prompt`,
   `preview_text` and an optional `voice_id`. **No language or accent field exists.** And the
   `language_boost` parameter on the TTS side offers plain **`English`** with **no British
   variant** among its forty-odd values. Accent is 100% prompt-inferred — so there is no setting
   to fix, only words.
2. 🔑 **The prompt is ElevenLabs-shaped, and MiniMax is the opposite.** MiniMax's own documented
   example is **one short sentence** — *"Excited and enthusiastic male product reviewer (e.g.,
   tech vlogger), fast-paced, high energy, and persuasive."* Their guidance is explicit: *you
   rarely need ten vocal adjectives.* A three-paragraph layered prompt gets averaged out, and
   what the model falls back to is its default: **General American.**
3. **The accent wasn't first and wasn't repeated.** State the language and regional variant in
   the **opening words** to prevent drift, and restate it at the end of a short prompt.
4. **"South Yorkshire, Sheffield" is out of distribution.** The model knows *British* and
   probably *northern*. It does not know Handsworth. An unrecognised regional label is silently
   dropped, and dropping it lands you back on the default.
5. **The preview text read as American.** Preview text is what actually gets spoken, and accent
   is inferred partly from orthography and idiom. Ours was accent-neutral.

Also: **`thick` outperforms `slight` or `strong`** as the intensity word for an accent.

### The ladder — try these in order, stop when one lands

Each design returns **three variations**, and preview audio costs **$30 per 1M characters** —
about **one penny per attempt**. Iterate freely.

**Rung 1 — short, accent-first, MiniMax house style:**

```
A British man in his early 60s with a thick northern English accent, deep and gravelly, dry and deadpan, speaking slowly like a wry storyteller.
```

**Rung 2 — if it drifts, name the country and repeat the accent at both ends:**

```
Thick working-class northern English accent from Yorkshire, England. Male, early 60s, deep gravelly baritone, worn and smoky. Slow, unhurried, deadpan delivery, lands sarcasm completely flat. Strong British northern accent throughout.
```

**Rung 3 — if it still drifts, drop the region and buy the accent outright:**

```
A thick British English accent, working class, northern. Older man, gravelly and deep. Dry, deadpan, unhurried.
```

Rung 3 trades Sheffield for a guaranteed British read. **Take the trade** — a generic northern
gravel that is genuinely British beats a Sheffield that comes out of Ohio.

### British-loaded preview text

Swap the preview text for this. Every line is idiom the model can only have learned from British
speech, and it is the film's actual register. 312 characters.

```
Meet Bob. Standard middle-manager bloke, having a knees-up in a tent in a Waitrose car park. Meet Tarquin, who buys up council flats and leaves them empty, then drives off to Wales in a forty-grand motor to find himself. I'd say it's a Mexican standoff, but there are no stakes and nobody gives a toss. Bloody hell.
```

`toss` rather than the script's `shit` — MiniMax is a Chinese provider and profanity filtering is
unverified. Test the real profanity on a throwaway generation **before** committing the script.

### Generation settings, once a voice_id exists

| Field | Set to | Why |
| --- | --- | --- |
| `model` | **speech-2.8-hd** | HD, not turbo — this is narration, not latency-bound |
| `speed` | **0.85–0.9** | Range is [0.5, 2]. The brief wants unhurried |
| `pitch` | **−1 to −2** | Range is [−12, 12]. A touch of weight; go further and it turns into a cartoon |
| `emotion` | **calm** or **fluent** | The brief's baseline is `{FLAT}`. Never `happy`, never `surprised` |
| `english_normalization` | **true** | Handles `E.T.F.s`, `4x4`, `1%` — do it anyway in the script |
| `language_boost` | **English** | The only English value there is. It will not buy you British |

### 🔁 The fallback that skips Voice Design entirely

MiniMax's voice **library** has an **EN-British filter with 300+ British voices**, sortable by
gender, age band (Child / Young / Middle-aged / Elderly) and use case (Audiobooks, Podcasts).
A library voice has its accent **baked in rather than inferred**, so it cannot drift.

Filter **Male + Middle-aged or Elderly + Audiobooks**, and audition on the line below. The named
narrator presets skew polished and RP — *"Expressive Narrator — Crisp, Resonant, Modulated"*,
*"Nature Show Host — Smooth, Deep, Polished"* — which is the wrong register for this film, so dig
past the featured ones for something rougher. If nothing is rough enough, **that is the signal to
go and clone a consenting human** rather than keep spending prompts.

**Audition line, same as above:** *"I'd say it's a Mexican standoff, but there are no stakes and
no one gives a shit."*

## The full survey of routes — 2026-08-31

> Researched after MiniMax Voice Design returned an American accent. The finding that reorganises
> everything: **prompt-to-voice tools are systematically worst at regional accents.** RP ships as a
> dedicated voice almost everywhere; Yorkshire, Scouse, Geordie and Brummie *do not*, and get
> flattened into generic approximations. So the reliable routes all start from **a real regional
> mouth** — hired, or cloned with consent — and only the last tier starts from a description.

### Tier 1 — a real human. Not slop by definition

| Route | Cost | Turnaround | Notes |
| --- | --- | --- | --- |
| **Fiverr, native Yorkshire** | **$10–25** base (100–200 words); expect **$40–60** for our script | **24 hours** on several gigs | Multiple native South Yorkshire and northern English sellers. 🔑 **Cheaper than one month of any AI subscription** |
| Voquent / Voices.com / Voiceovers.co.uk / EasyTiger | **£100–£1000+**, scaled by reach and usage | Auditions in 2–3 working days | Agency rosters with native Sheffield and South Yorkshire talent. Buys direction and a re-record, not just a read |
| Record someone we know | £0 | Same day | A phone in a quiet room clears the bar. Also the only route with zero licensing questions |

### Tier 2 — clone a real regional voice. Accent is real, delivery is synthetic

| Route | Cost | Notes |
| --- | --- | --- |
| **Higgsfield cloning** | Already subscribed | Consent-only cloning; a short clean recording is enough. Keeps the whole job in one tool |
| **ElevenLabs Voice Library** | Credits | Has genuine **Yorkshire** voices and a **gravelly** category, cloned from real people, so the accent cannot drift. ⚠️ Community voices can carry a **creator-set credit multiplier** — check before committing a whole script |
| **Local on the RTX 4070** — Chatterbox Multilingual v3 (MIT), F5-TTS, XTTS-v2 | £0, unlimited | Zero-shot clone from **5–10 seconds**. Clones fool casual listeners **70–85%** on a 12GB card. Chatterbox took a blind A/B win over ElevenLabs; it is **watermarked** (inaudible, PerTh) |
| **Synthesia Express-Voice** | Enterprise-priced | A year of studio recordings of **real UK regional speakers**, Glaswegian to Scouse — explicitly built for the thing every other platform flattens. Best-in-class for UK regional, worst-in-class for our budget |

### Tier 3 — prompt-to-voice. Where we are, and the weakest tier for accent

| Tool | Cost | Verdict |
| --- | --- | --- |
| **Hume Octave** | Free 10k chars/mo · **$3/mo** 30k · **$14/mo Creator unlocks the commercial licence** · ~$7.60 per 1M chars | 🔑 **The upgrade from MiniMax.** Beat ElevenLabs Voice Design in a 180-rater blind study — **71.6%** audio quality, **51.7%** naturalness, **57.7%** description-match. Generates accent *and personality* from a description or a 5-second recording, and takes **natural-language acting instructions per line** — *"sound sarcastic"*, *"whisper"* — which is exactly the brief's `{FLAT}` baseline with one `{WARM}` crack. No SSML |
| ElevenLabs Voice Design | Credits, Creator tier and up | Proven — the Karen route. Long detailed prompts at low guidance |
| MiniMax Voice Design | ~1p per attempt | Cheapest to iterate, weakest at accent. See the ladder above before abandoning it |

⚠️ **Hume's commercial licence is the $14 Creator tier**, not the $3 one. BadCode publishes; budget for Creator or the output is not licensed for it.

### The ruling

**Spend the $20 on Fiverr.** The whole point of this narrator is that he must not sound like AI,
the script is ~440 words, a native Sheffield human turns it round in a day, and it costs less than
one month of any subscription on this page. **If the film's central claim is that people get
treated as costs to be optimised away, hiring one is on-message.**

If it has to stay synthetic — because the script will keep changing and re-records cost money —
then **Hume Octave at $14** is the one to move to, and the per-line acting instructions are worth
more to this script than the voice design is.

## 🔴 CLOSED 2026-09-03 — ElevenLabs is abandoned for this narrator

**Jack: *"it still did not fix the accent, I think we give up with ElevenLabs and move on."*** ✅
**Agreed, and the evidence below says it was never going to work.** Everything from here down is kept
as the post-mortem, not as a plan.

### What was tried, and what each attempt proved

| Tried | Result |
|---|---|
| Voice Design → "Camping Narrator" → **v3** | Accent wrong |
| Same voice → **Multilingual v2**, Similarity ~74, Style 0 | Accent still wrong |
| Karen's tag set, break tags, corrected speed | Delivery levers. **None of them touch accent** |

🔑 **Three independent findings all say the same thing, and they were available before any credits
were spent:**

1. **ElevenLabs' own troubleshooting** names the fix for accent drift as *"using an Instant Voice
   Clone or a Professional Voice Clone"* — **not a designed voice.**
2. **Similarity is defined as adherence to *"the original voice"*** — and a Voice Design voice has no
   original recording, so the one control that would have held the accent had nothing to hold.
3. **This page already ranked prompt-to-voice "Tier 3 — the weakest tier for accent"** on
   2026-08-31, and listed five causes of exactly this drift.

🔴 **And Karen was never evidence to the contrary.** Her brief asks for *"General American"*, which
is the model's own fallback — so every drift moved her toward her target. **Karen never tested
whether Voice Design holds an accent.**

### What was learned that is worth keeping

- **Voice Design cannot be trusted for a non-default accent.** Applies to any prompt-to-voice engine,
  not just this one — the MiniMax post-mortem above reached the same conclusion independently.
- **v2 and v3 are different tools.** v2 has Similarity, Speed, Style Exaggeration and `<break>`;
  v3 has audio tags and none of those. **For a narrator whose problem is fidelity, v2 is the better
  model** — worth remembering if we ever come back.
- **`<break time="x.xs" />` works on v2 up to 3 seconds.** [`forms.md`](../../../story-craft/forms.md)
  defers `//` and `///` to the Premiere edit because *"Suno cannot hit a timecode"* — that rationale
  is engine-specific, and any engine with a break control can execute them in the read.
- ⚠️ **Never settled:** whether v2 speaks or ignores `[understated]`. Not documented; Karen's takes
  suggest ignored.

### ➡️ Where this goes now — it is not back to square one

**The [2026-09-01 ruling below still stands](#-ruled-2026-09-01--go-local-and-clone-the-suno-take),
and it was made before ElevenLabs was tried.** Go local, clone round 13's Suno take — the one Jack
called *"spot on"* — on **Chatterbox** (MIT) or **Qwen3-TTS** (Apache 2.0), both of which run on the
4070.

🥇 **The blocker that ruling had is gone.** It needed a reference clip of the right voice, and we now
have one. **And cloning is exactly what ElevenLabs' own docs said the fix was** — we just do it
somewhere free, unlimited, offline, and without the commercial-licence question that a Free-tier
balance never resolved.

## 🔑 WHY KAREN WORKED AND CAMPING DID NOT (2026-09-03)

**Jack: *"why did the custom voice work for Karen and not for camping — did I miss a setting?"***
Two answers. The first is structural and is most of it. The second is three settings, and yes, they
are probably wrong.

### 1 · 🔑 Karen's target IS the model's default. Camping's is the opposite of it.

[`../../karen/narration/voice.md`](../../karen/narration/voice.md) asks for **"Native American
English. General American with a faint Western ease."** Camping asks for **thick working-class
northern English.**

**These models fall back to General American.** So every drift in Karen's design moved her *toward*
what she was supposed to be — the failure mode was invisible because her target and the default are
the same thing. **Every drift in camping's design moves it away from the target.** Karen was never a
test of whether Voice Design holds an accent, because Karen never asked it to.

🔴 **So "it worked for Karen" is not evidence the method works. It is evidence Karen was easy.**

### 2 · Three settings, and ElevenLabs' docs say all three matter

| Setting | What camping likely used | What the docs say | Verdict |
|---|---|---|---|
| **Guidance Scale** | Karen's **30%** is the number sitting in the more-familiar doc | 🔑 *"Higher values follow the prompt more rigidly… **High values: better for accent/tone accuracy when precision matters most.**"* | 🔴 **30% is the wrong end for an accent.** It cost Karen nothing because her accent was the default. It costs camping everything |
| 🔴 **`Perfect audio quality.`** — the first words of camping's rung 1 | Present, at the front | *"Including these types of phrases **can sometimes reduce the accuracy of the prompt in general if the voice is very specific or niche.**"* And their own descriptor list is *Ok / Good / Very good / Excellent / Studio / Broadcast* — **"Perfect" is not on it** | 🔴 **A thick working-class northern English accent is exactly "specific or niche."** This phrase is probably buying dry audio at the cost of the accent |
| **Preview text** | Unknown — if *"Generate Preview Text"* was left **on**, it is auto-written and accent-neutral | *"The preview text acts like a **performance script** — it sets the tone, pacing, and emotional delivery that the voice will attempt to match."* Longer is more stable | ⚠️ **Turn it OFF and paste the British-loaded 312-char text** below. An accent-neutral preview was already cause #5 in the MiniMax post-mortem |

✅ **`thick` over `strong`** — the repo already had this right, and the docs confirm it.
✅ **The word `accent`** is correct here, because we mean a regional dialect, which is the case
their warning exempts.

### 🔧 Corrected rung 1 — try this before cloning

**Quality phrase removed, accent first and repeated at both ends, long enough to carry high
guidance:**

```
A middle-aged man with a thick working-class northern English accent, from Manchester, England. Slow, unhurried and deadpan, landing every sarcastic line completely flat. Mid-range and nasal with a sandpaper rasp — never deep, never an announcer. Thick northern English accent throughout.
```

| Control | Set to | Why |
|---|---|---|
| **Guidance Scale** | 🔑 **45–50%**, not 30 | Accent accuracy is the entire problem, and the prompt above is long and detailed enough to carry it — *"longer, more detailed prompts handle higher guidance scales better."* Drop toward 40 only if it comes back robotic |
| **Generate Preview Text** | 🔴 **OFF** | Paste the 312-char British-loaded text in "Preview texts" below |
| **Loudness** | centre (0) | It bakes into the saved voice |

**Cost: ~312 credits per attempt, and each attempt returns three voices.** Two attempts is 624 of
4,057 — worth spending before falling back to a clone.

⚠️ **If two corrected attempts still drift, stop and clone.** The ruling below stands, and the docs
back it.

### ✅ Confirmed while checking this: PVC does not work on v3

Voice Design's own page: **"The v3 model does not currently support Professional Voice Clones."**
So if a clone is made, it must be an **Instant Voice Clone** — which is what the section below
already specifies.

## 🔴 RULED 2026-09-03 — the designed voice will not hold the accent. Clone the Suno take.

**Symptom:** "Camping Narrator" is selected in the UI, Eleven v3 is selected, and the generation
still does not come back as the narrator.

🔑 **The voice is not being ignored. The voice is wrong** — and ElevenLabs' own troubleshooting page
says so in as many words:

> **"Default/generated voices are primarily English and may carry an English accent."**
> Documented fix for accent drift: **"Using an Instant Voice Clone or a Professional Voice Clone
> trained on high-quality, consistent audio."**

⚠️ **A "generated voice" is a Voice Design voice — exactly what THE RUN below builds.** So the
platform's own guidance is that prompt-to-voice is the wrong tool for a specific regional accent,
which is what this page already concluded twice from the other direction:

- **§ Tier 3 — prompt-to-voice: "the weakest tier for accent."**
- **§ 🇺🇸 → 🇬🇧 the accent fix:** five causes of American drift, none of which is a setting.

### 🥇 The fix, and we already own the asset

**[`suno-narration.md`](./suno-narration.md) round 13 is the take Jack called *"spot on"* — right
accent, right age, right class, right attitude.** The 2026-09-01 ruling further down this page
already said to clone it; it aimed the clip at *local* open-weights cloners because that was the
cheap route. 🔑 **The same clip is an Instant Voice Clone in ElevenLabs, and IVC is the platform's
own documented answer to accent drift.**

```
Round 13's Suno vocal stem  →  ElevenLabs Instant Voice Clone  →  Eleven v3
=  the right accent, no music, no grid, no singing, and audio tags on top
```

### What the clip has to be

| Requirement | Value | Source |
|---|---|---|
| Length | 🔑 **1–2 minutes.** 30s can work; **never exceed 3 minutes** — *"can, in some cases, even be detrimental"* | IVC docs |
| Samples | Any number — *"the number of samples is irrelevant; what's important is the total run time"* | IVC docs |
| Format | **MP3 192 kbps or above** | IVC docs |
| Content | 🔴 *"no background noise, room reverb, or multiple speakers, at a consistent volume and tone"* | IVC docs |
| Level | −23 to −18 dB RMS, true peak −3 dB | IVC docs |

🔴 **Take it from the VOCAL STEM, never the mix** — three dots → Get stems → advanced split
([`suno-narration.md`](./suno-narration.md) §5). *"The AI will mimic everything heard, including
speed, inflections, accent, tonality, breathing pattern"* — which includes the drum loop if you
leave it in.

⚠️ **1–2 minutes is more than the 15 seconds the 2026-09-01 ruling called for.** That figure was
sized for local cloners, which clone from 5–10s. **ElevenLabs wants a minute or two**, so take the
longest clean continuous stretch of round 13, and stitch several clean stretches if one is short —
the docs say sample count does not matter, only total runtime.

✅ **No consent question.** The Suno voice is synthetic and generated on our own paid account.

⚠️ **Unverified:** whether creating an IVC costs credits or only a voice slot. The IVC docs do not
say. Budget as if it is free and check the balance after.

### If the clone is still not right

Then, and only then, go back to the Voice Design ladder in THE RUN below — rungs 1, 2, 3, in order,
and do not add adjectives to rung 1.

## 🔑 THE RUN — ElevenLabs, 4,057 credits (2026-09-03). ✅ The voice is already built.

✅ **The voice exists — "Camping Narrator", confirmed in the UI 2026-09-03.** The repo never
recorded it, so everything below about *designing* a voice is **history, already paid.** 🔑 **The
only spend still ahead is the script: 2,609 of 4,057.** Rungs and vocabulary are kept because they
are the fix if the saved voice turns out to have drifted American — the documented failure of this
tier.

🔑 **The paste-ready words live in [`elevenlabs-script.md`](./elevenlabs-script.md)** — the five
chunks normalised, tagged and character-counted. This section is the *plan and the budget*; that
file is what goes in the box.

### The budget, measured not guessed

| | Characters | Credits |
|---|---|---|
| **The whole script** (chunks 1–6 of `elevenlabs-script.md`, tagged) | **2,609** | **2,609** |
| chunk 1 · 2 · 3 · 4 · 5 · 6 | 363 · 420 · 269 · 525 · 459 · 573 | same |
| ⬜ chunk 8, if the ending comes back | +357 | 2,966 |

🔑 **1 credit = 1 character** on **Eleven v3** and **Multilingual v2** — the two models worth using
here. (Flash/Turbo are 0.5, but they are the latency models and this is narration.)

🔑 **Voice Design is charged on the PREVIEW TEXT only, once per attempt — and it returns three
voices for that one charge.** ElevenLabs' own words: *"the only charge for using voice design is the
number of credits to generate your preview text, which you are only charged once even though we are
generating three samples for you."* ⚠️ **Preview text must be 100–1,000 characters.**

### The plan that fits, with room to fix a bad chunk

| Step | Spend | Running total |
|---|---|---|
| **6 screening designs** @ a **150-char** preview | 900 | 900 |
| **1 confirmation design** @ the full **312-char** preview, on the winning prompt | 312 | 1,212 |
| ~~Voice design~~ | ✅ already paid | 0 |
| **Chunks 1–6, once** | 2,609 | 2,609 |
| ✅ **Left for re-reads, against 4,057** | — | 🥇 **1,448** |

⚠️ **730 buys one long chunk again and one short one** — chunk 6 (534) plus chunk 3 (269) is
already 803, so it does not even cover the two longest. 🔴 **And if the ending comes back as chunk 8
(+329), the margin falls to 401** — less than a single re-read of chunk 6. **That is not a safety
margin, it is one mistake.**

🔴 **What does NOT fit: two full script passes.** 2 × 2,609 = 5,218 — **more than the whole balance**, not even one
design attempt. **So the discipline is: design cheaply, render once, re-render only the chunks that
fail.** Never re-render the whole script to fix one line.

**Three rules that make the margin hold:**

1. 🔑 **Screen on a 150-char preview, confirm on 312.** Six attempts at 150 gives **eighteen candidate
   voices** for 900 credits. Longer preview text makes a *more stable* voice, so the finalist gets one
   full-length confirmation — but you do not pay 312 to reject something.
2. 🔑 **Make the preview text the audition line.** The design preview *is* the test, so auditioning
   costs nothing extra. Both preview texts below already contain the audition line.
3. **Render chunk by chunk, never the whole script in one go.** A bad chunk then costs 269–573 to
   redo instead of 2,609. ⚠️ **Whether v3 audio tags are billed as characters is unverified** — we
   could not find it documented. The 2,609 above budgets as if they are; the script carries twelve
   tags, 162 characters.

### 🔴 The prompt is rewritten for Voice Design v3 — the old one is the wrong shape

⚠️ **The three-paragraph prompt further down this page was written for the older Voice Design**,
which rewarded long detailed prompts at low guidance. **v3 wants the opposite**, and its guidance is
explicit: *"Describe age, accent, tone, pacing, and audio quality in a single sentence… The best
prompts read like everyday speech — short, specific, and jargon-free."*

🔑 **This is the exact trap that made MiniMax come back American** (see the five causes below): a
long layered prompt gets averaged, and the average is General American. **Do not paste the old one
into v3.**

Their own worked example is the template to copy: *"Perfect audio quality. Elderly male, thick
Scottish accent, slow and reflective, gravelly timbre."*

**Rung 1 — paste this** (matches their order: quality → age/gender → accent → pacing → timbre, and
carries the fourteen rounds of Suno casting: mid-range not deep, nasal, sneering):

```
Perfect audio quality. Middle-aged male, thick working-class northern English Manchester accent, slow and deadpan, mid-range nasal timbre with a sandpaper rasp.
```

**Rung 2 — if it drifts American or posh**, name the country and repeat the accent at both ends:

```
Perfect audio quality. Male in his forties, thick working-class northern English accent from Manchester, England. Slow, unhurried, deadpan, sarcastic. Mid-range nasal timbre, sandpaper rasp, never deep and never an announcer. Strong British northern accent throughout.
```

**Rung 3 — if it still drifts**, drop the city and buy the accent outright:

```
Perfect audio quality. Middle-aged male, thick British northern English accent, working class, slow and deadpan, mid-range and gravelly.
```

🔧 **Vocabulary rulings that carry over and are not up for re-litigation:**

| Rule | Why |
|---|---|
| **`thick`**, never `slight` or `strong` | Tested — the intensity word that lands |
| 🔴 **`mid-range`, never `deep`** | Fourteen Suno rounds. `deep` produced *too low* three times; what was wanted was **texture** (`rasp`, `grit`), not pitch. `suno-voices.md` §4b |
| **`never boomy, never an announcer`** | Hard requirement — the reference sits low and the model will chase movie-trailer |
| 🔴 **Never a room or FX word** — no `reverb`, `echo`, `room tone` | It degrades output and produced the echoing Suno takes. `Perfect audio quality` buys dry and close for free |
| ⚠️ ElevenLabs' own caution on the word `accent` | *"if you mean intonation or emphasis patterns rather than a regional dialect, use those terms instead."* We mean the dialect, so it is correct here |

### Preview texts

**Screening preview — 150 chars.** Cheap, and it is the driest line in the film, which is the whole
audition:

```
I'd say it's a Mexican standoff, but there are no stakes and nobody gives a toss. Bob calls them wank tanks. Most common vehicle in this car park, mind.
```

**Confirmation preview — 312 chars**, for the finalist only. Every line is idiom the model can only
have learned from British speech:

```
Meet Bob. Standard middle-manager bloke, having a knees-up in a tent in a Waitrose car park. Meet Tarquin, who buys up council flats and leaves them empty, then drives off to Wales in a forty-grand motor to find himself. I'd say it's a Mexican standoff, but there are no stakes and nobody gives a toss. Bloody hell.
```

⚠️ **`toss` rather than the script's `shit`** while designing — keep the filter out of the variable
set. Test the real profanity once on a short generation before committing the script.

### Settings

| Control | Set to | Why |
|---|---|---|
| **Guidance Scale** | 🔧 **~40%** for the short v3 prompt | The 30% ruling below was for the *long* prompt — ElevenLabs pair **low guidance with long detailed prompts**. A short prompt needs more adherence, not less. If it comes back artificial, drop toward 30 |
| **Loudness** | **centre (0)** | It bakes into the saved voice; level in Premiere instead |
| **Model, for the real reads** | **Eleven v3** | The one that takes audio tags — directly the brief's `{FLAT}` baseline and its one `{WARM}` crack. Stability **Natural**, Similarity ~75, Style 0 |
| **Voice slot** | one | Saving a design consumes a voice slot, not credits |

### 🔴 Before spending anything: check the plan, not the balance

**4,057 looks like a Free-tier remainder** (Free is 10,000 credits/month). If so, 🔴 **the output
carries no commercial licence and BadCode publishes this film.**

🔑 **The fix is $6 and it removes the whole budget question:** **Starter — $6/month, 30,000 credits,
and it is the cheapest plan that includes the Commercial License.** Thirty thousand credits is
**twelve full passes of this script**, which also ends the re-read rationing above. If the balance
shown is already a Starter balance, ignore this and run the plan above.

### The order

1. **Check the plan is Starter or above** (commercial licence). ⬅️ *before anything else*
2. **Six screening designs** on rung 1, 150-char preview. Judge every one of the eighteen on the audition line: **flat and amused wins.** Any lift, any grandeur, any sense it knows it is funny is wrong.
3. If all eighteen drift American or posh, go **rung 2**, then **rung 3**. Do not add adjectives to rung 1.
4. **One confirmation design** on the winner, 312-char preview. Save it.
5. **Render chunk by chunk**, in order, listening to each before starting the next.
6. **Re-read only the chunks that fail.** 730 credits of margin — one long chunk and a short one, and nothing after that.
7. 🔑 **Normalise before synthesis:** `E.T.F.s`, `I.P.A.`, `one percent`, `4 by 4's`, `Two thousand and eight`, `Twenty thirty-one`, `ayawaska`. Never after.

## 🔑 RULED 2026-09-01 — go local, and clone the Suno take

> ⚠️ **Superseded as the plan of record by the ElevenLabs run above (2026-09-01).** Kept because the
> engine ranking and the licence table are still the right answer if ElevenLabs is abandoned.

**Jack: *"it sounds good but there is still music. it sings it sometimes. should we just use a free
ai voice?"*** ✅ **Yes.** Three faults in a row — American accent, delivery on the grid, music and
occasional singing — and they all have the same root cause, which
[`suno-narration.md`](./suno-narration.md) states outright: **Suno cannot make silence.** It is a
music generator, so a bed is always there and a sung phrase is always one re-roll away. Fourteen
rounds bought a voice, not a narration engine.

### 🔑 What changed today, and it reorders this whole page

**Yesterday's blocker was the reference clip.** Every free local route needs a northern English
male sample to clone, and the best we had was a corpus stranger (OpenSLR 83) or an undertrained
Piper voice.

🥇 **We now have fifteen seconds of the exact narrator.** Round 13's Suno take is the one Jack
called *"spot on"* — right accent, right age, right class, right attitude. **That is the reference
clip**, and it makes every open-weights cloner on this page better than it was yesterday.

```
The approved Suno take (15s of clean voice)  →  a free MIT/Apache local cloner
=  the exact narrator, no music, no grid, no singing, unlimited retakes, offline, £0
```

⚠️ **Take the clip from the VOCAL STEM, not the mix** — [`suno-narration.md`](./suno-narration.md)
§5. A cloner will happily learn the drum loop as part of the timbre. Fifteen clean seconds beat
sixty contaminated ones, which is the same rule as the Suno Voice transplant.

✅ **No consent question here**, unlike the corpus route: the Suno voice is synthetic and generated
on our own paid account. Nobody's voice is being cloned. The 🔴 **licence question that does matter
is the model's weights** — see the table below.

### The ranking, rebuilt on an RTX 4070 (12 GB, confirmed)

| # | Model | Weights licence | Why |
|---|---|---|---|
| 🥇 **1** | **Chatterbox** (Resemble) | **MIT** — publishable | Clones from **5–10s**, ~2.3–3.5 GB VRAM, so it is comfortable on the 4070. **Beat ElevenLabs in a blind A/B — 63.8% of listeners preferred it**, and the Turbo variant ~65%. First open model with an **emotion-exaggeration dial**, which is directly the brief's `{FLAT}` baseline and its one `{WARM}` crack. ⚠️ Carries an inaudible **PerTh watermark** |
| 🥈 **2** | **Qwen3-TTS** | **Apache 2.0** — publishable, unrestricted | 🔑 **Newer than this page** (Jan 2026, so it post-dates the 2026-08-31 survey). Zero-shot clone from **3 seconds**, and its pitch is explicitly that it *"preserves the speaker's identity, **accent** and nuances"* — which is the one axis every other route keeps losing. **Run it head-to-head with Chatterbox on the same clip** |
| 3 | **Kokoro 82M** | Apache 2.0 | Highest Elo of the open models and the most-downloaded open TTS in the world — but **no cloning**, and all four British males are RP. **Wrong register, and it cannot learn ours.** Scratch track only |
| 4 | **Piper `en_GB-northern_english_male`** | CC-BY-SA 4.0 | Instant, right accent, **documented artifacts**. Still the fastest scratch track to cut picture against |
| 🔴 | **Higgs Audio v3** | non-commercial | Better features, wrong licence. **We publish** |
| 🔴 | **VibeVoice** | research use only | Same |
| 🔴 | **F5-TTS** | MIT code, **CC-BY-NC weights** | The code/weights trap. Same |
| 🔴 | **XTTS-v2** | CPML non-commercial, and Coqui is gone so no licence can be bought | Same |

### The order to do this in

1. **Get the vocal stem** of the approved round-13 take — three dots → Get stems → advanced split (`suno-narration.md` §5).
2. **Cut 15 clean seconds** of continuous speech, no bed bleed, one consistent register.
3. **Install Chatterbox**, clone from the clip, and read the **audition line**: *"I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit."* Flat and amused wins.
4. **Do the same on Qwen3-TTS** with the identical clip and line. One variable, two engines.
5. **Whichever wins, run the whole script** — it is free and unlimited, so re-record as the script changes rather than budgeting for it.
6. **Attribution:** none owed if the clip is our own Suno output. ⚠️ Owed under CC-BY-SA only if you fall back to an OpenSLR or Piper clip.

⚠️ **The tier-1 answer has not changed and is still worth saying: a native Sheffield human on
Fiverr is $40–60 and one day.** The ruling further up this page still stands on its merits — this
section is the answer to *"what if it stays synthetic and free."*

## Free routes only — 2026-08-31

> ⚠️ **Superseded in part by the 2026-09-01 ruling above** — the reference-clip problem this section
> works around is solved, so its Piper/OpenSLR ranking no longer applies. The licence table is still good.

> 🔴 **Every hosted free tier fails the commercial-rights test.** ElevenLabs Free grants no
> commercial licence and demands `elevenlabs.io` in the title; Hume's free and $3 tiers are
> non-commercial (the licence starts at **$14** Creator); MiniMax free credits are unclear. BadCode
> publishes. **So "free and publishable" means local open-weight models, or a real human.**

### ⚠️ Code licence is not model licence

The single trap in this whole tier. A repo can be MIT while its *weights* are non-commercial, and
the weights are what makes the audio.

| Model | Weights licence | Publishable? |
| --- | --- | --- |
| **Chatterbox** (Resemble) | **MIT** | ✅ Yes. Clones from **5–10s**, ~2.3–3.5GB VRAM, inaudible PerTh watermark |
| **Kokoro 82M** | **Apache 2.0** | ✅ Yes. No cloning — fixed voices only |
| **Higgs Audio v2** | **Apache 2.0** | ✅ Yes. Best naturalness of the open models; 5.8B is tight in 12GB |
| **Piper** | MIT engine, **per-voice licences vary** | 🟡 Check the individual voice's model card, every time |
| **VibeVoice** (Microsoft) | MIT, but the card says **research use only** | 🔴 Not without further diligence. The Realtime 0.5B variant is clean |
| **XTTS-v2** (Coqui) | **CPML — non-commercial**, and Coqui shut down in 2024 so no licence can be bought | 🔴 No |
| **F5-TTS** | MIT code, **CC-BY-NC-4.0 weights** | 🔴 No |

### 🔑 The free route that actually gets a northern accent

**Piper already ships `en_GB-northern_english_male`.** A real, local, free, northern English male
voice — the exact accent, no prompt, no drift.

| | |
| --- | --- |
| Voice | `en_GB-northern_english_male-medium`, 22.05kHz |
| Licence | **CC-BY-SA 4.0** — commercial use allowed **with attribution**, and share-alike |
| Trained on | **OpenSLR 83**, Google's UK & Ireland English Dialect corpus |
| ⚠️ Quality | Undertrained. Documented **artifacts — clicks, breathiness, dropped phonemes.** Fine for a test read, probably not for the final master |

**So use it as the fast test, and OpenSLR 83 as the real answer:**

🔑 **OpenSLR 83 is free Northern English male speech under CC-BY-SA 4.0** — 16,477 utterances
across Irish, Midlands, **Northern**, Scottish, Southern and Welsh English, as wavs with a TSV
index. Chatterbox needs **ten seconds** of it.

```
Chatterbox (MIT) + a 10s Northern English male clip from OpenSLR 83 (CC-BY-SA)
= free, local, unlimited retakes, publishable with attribution
```

That beats Piper's own voice because Chatterbox is a far stronger model and only borrows the
accent, rather than inheriting the undertrained corpus's artifacts.

### The other free reference-clip sources

| Source | Licence | Notes |
| --- | --- | --- |
| **OpenSLR 83** | CC-BY-SA 4.0 | 🥇 Accent-labelled by region. Purpose-built for this |
| **Mozilla Common Voice** | **CC0** — no attribution needed | Accent metadata is contributor-written free text, so "England English" is common but Yorkshire granularity is not guaranteed. Filter and see |
| **LibriVox** | Public domain | Long clean solo reads; you must audition for a northern reader |
| Internet Archive | 🟡 uploader-asserted | Per [`find-footage`](../../../video-fx/footage-sources.md), a `licenseurl` is not a licence. Per-item human check or skip |

⚠️ **A consent note worth ten seconds of thought.** CC0 and CC-BY-SA make corpus cloning legal.
Those volunteers recorded for dataset training, not to narrate political satire. They are
anonymised and not public figures, so this is not a rights problem — but
[`docs/using-ai.md`](../../../using-ai.md) is about being straight on method, and **recording a
consenting human is free too, and has none of this attached.**

### The genuinely free non-AI option

**Record it.** A phone in a quiet room clears the bar for this film. Zero cost, zero licence,
zero watermark, zero slop — and if nobody to hand has the accent, a northern narrator is a
preference, not a requirement. The brief's load-bearing traits are **deadpan, unhurried, flat** —
and those are free.

### Free ranking, for this film

1. **Record a consenting human.** £0, no licence, not AI.
2. **Chatterbox + OpenSLR 83 clip.** £0, MIT, unlimited, real northern accent, attribution owed.
3. **Piper `en_GB-northern_english_male`.** £0, instant, right accent, audible artifacts — a great
   scratch track to cut picture against.
4. **Kokoro `bm_*`.** £0, Apache 2.0, clean — but all four British males are **RP/standard**
   (George is graded classic RP, Lewis "modern British"), so the accent is wrong for this narrator.

## Prompt-to-voice only, no cloning — 2026-08-31

> The user's constraint: **describe the voice in a prompt; never clone.** Here is every tool that
> actually does that, ranked, plus the ones that look like they do and don't.

### 🔴 The headline finding

**There is no free, local, publishable, prompt-to-voice model with accent control.** The open
Apache-2.0 models that take a voice description **cannot control accent**, and every model that
*can* control accent is hosted and needs a paid tier for a commercial licence. Free tiers are for
**auditioning**, not for shipping.

### Tier A — genuinely takes an accent in the prompt

| Tool | What it costs | Verdict |
| --- | --- | --- |
| **Hume Octave** | Free **10k chars/mo** to audition · **$14/mo Creator** for the commercial licence (the $3 Starter is non-commercial) · ~$7.60 per 1M chars | 🥇 **The pick.** Accent sits in the prompt vocabulary alongside gender, age, vocal register and role. Beat ElevenLabs Voice Design in a **180-rater blind study** — 71.6% audio quality, 51.7% naturalness, **57.7% description-match**. Takes **natural-language acting instructions per line**, which is the brief's `{FLAT}` baseline and its one `{WARM}` crack, directly. Hume's own caveat: *less common accents are harder and subtle variations may not land* |
| **ElevenLabs Voice Design** | Credits, Creator tier and up | Proven — the Karen route. Long detailed prompt at **30% guidance**. Library also carries genuine Yorkshire voices if design fails |
| **Resemble AI** | Pay-per-use **$0.0005 per synthesis second** — this narration is **~9 cents** | Voice design from natural language, no subscription since they retired the consumer tiers. ⚠️ Designed voices may bill as the **$2–5/month voice add-on** — check before committing |
| **MiniMax Voice Design** | ~**1p** per attempt | Where we are. Cheapest to iterate, weakest at accent — run the ladder above before abandoning it |

### Tier B — looks right, is not. Do not install these for this job

| Tool | Why not |
| --- | --- |
| **Parler-TTS** (Apache 2.0, free, local) | 🔴 **Accent is not a controllable attribute.** The model card lists exactly: gender, background noise, speaking rate, pitch, reverberation — plus 34 named speakers. Several blogs claim accent control; the card does not support them. **This is the one that would have wasted a day** |
| **CosyVoice 2 / 3** (Apache 2.0, free, local) | 🔴 Natural-language instruction control is real, but the dialect coverage is **18+ Chinese dialects**. No Yorkshire, no British regional |
| **OpenAI `gpt-4o-mini-tts`** | 🔴 The `instructions` parameter nominally covers accent, but community reports are consistent that **accent instructions do not take** — it stays American. Excellent for steering tone, useless for this accent |
| **Typecast / Lovo / Cartesia** | 🟡 Expressive and emotional control over **preset libraries**, not voice design from a description |

### The Hume Octave prompt

Octave's documented pattern is *"The speaker is a…"*, combining accent with demographics, role and
disposition in one paragraph:

```
The speaker is a working-class northern English man in his early sixties with a thick Yorkshire accent, telling a story whose ending he already knows. His voice is a deep, gravelly baritone, worn and smoky. He speaks slowly and unhurried, lands every sarcastic line completely flat, and underplays the punchlines rather than selling them. Fond of the listener, and thoroughly unimpressed by the man he is describing.
```

Pair it with the **British-loaded preview text** above — the idiom does real work on accent in
every one of these engines.

Then use Octave's **per-line acting instructions** rather than tags: `deadpan` on the baseline,
and the single `{WARM}` crack in scene 11 gets its own instruction. **No SSML** — Octave does not
use it.

### The ruling for a no-cloning workflow

**Audition on Hume's free 10,000 characters.** That is roughly **three full passes** of this
script — enough to know whether the Yorkshire holds before spending anything. If it lands, **$14**
buys the commercial licence. If Hume flattens it too, the finding is no longer about tools: the
accent is not reliably promptable anywhere, and the choice becomes **an ElevenLabs library
Yorkshire voice** or **a human**.

## Divergence from the Karen narrator — deliberate

Karen's narrator is **General American, mid-range, explicitly "never deep."** This one is
**Northern English, deep and gravelly.** They are not the same man and are not meant to be. If
BadCode wants one house narrator across the whole run, that is a call to make now, before either
voice is saved and becomes a canon asset — see the standing rule at the top of Karen's
`narration/README.md`.

---

**Voice name once saved:** `# TODO`
**Engine and route used:** `# TODO`
