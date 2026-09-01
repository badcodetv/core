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
`4x4's` → `four-by-fours`, `1%` → `one percent`.

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

## Free routes only — 2026-08-31

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
