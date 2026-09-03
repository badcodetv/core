---
title: Camping — the narration script, optimised for ElevenLabs
status: words are Jack's 2026-09-03 draft, optimised for synthesis — 3 content gaps open
model: Eleven v3
voice: ✅ "Camping Narrator" — built and saved, confirmed in the UI 2026-09-03
method: Text to Speech box, chunk by chunk (the Karen method)
settings: Stability Natural (the slider's midpoint) — v3 exposes no Similarity or Style
---

# The script, paste-ready for ElevenLabs

> **What this is:** Jack's 2026-09-03 narration draft, normalised and chunked for **Eleven v3**.
> The words are his; what changed is spelling-for-the-ear, punctuation, chunk boundaries and one
> factual fix. The voice-design plan and the budget are in [`voice.md`](./voice.md) → "THE RUN".
> The job list is [`../narration-brief.md`](../narration-brief.md).

✅ **The voice exists.** **"Camping Narrator"** is built and saved — confirmed in the ElevenLabs UI
on 2026-09-03. The repo never recorded it, which is why earlier versions of this sheet said it did
not exist. 🔑 **The design spend in [`voice.md`](./voice.md) → "THE RUN" is already paid** — that
whole 1,212-credit plan is history, not a cost still ahead of you.

---

## 🔴 Three things the draft drops — read before rendering

These are content calls, not synthesis calls. **None of them is fixed below**, because they are
Jack's to make. But rendering before settling them wastes credits on lines that will change.

### 1 · The newspaper said 2026. It has to be 2031.

✅ **Fixed in chunk 6, because this exact bug was already ruled on.** Commit `7da1604` fixed the
same line once: *"Chunk 5 told Tarquin to look at the date and then said 'twenty twenty-six' — the
same year the Shard already carries in scene 4, so the reveal revealed nothing."*

🔑 **The date's whole job is to prove five years passed.** A paper reading 2026 is the year he left
— it proves nothing. `shot-list.md:18` records Jack's own ruling: **the on-screen year is a
two-instance device and 2031 is spoken, not shown.** That line is the only place 2031 exists in the
film.

### 2 · 439 words — a pacing choice, not a hard limit

⚠️ **Corrected 2026-09-03.** The 250–320 figure is not a wall. It is derived from
`narration.mp3` being **150s**, and [`narration-brief.md`](../narration-brief.md) disclaims that
file in the same breath: *"`narration.mp3` predates the whole production run. Treat 150s as the
shape, not the target."*

🔑 **The brief's actual rule is "cut to the words, not the other way round."** So the script sets
the film's length; the length does not cap the script.

| | |
|---|---|
| Raw picture available | **272s** ([`edit-plan.md`](../edit-plan.md)) |
| The 2026-08-30 edit plan's target | ~157s, chosen to match the **old** 150s narration |
| **439 words at 155 wpm** (the ceiling) | **~170s** |
| **439 words at ~135 wpm** (unhurried, which the brief wants) | **~195s** |

**So the draft does not overrun the picture — it lengthens the film**, from a ~157s cut to roughly
**175–200s**, and there is 272s of raw picture to draw on. The edit plan simply trims less.

⚠️ **What it does cost is credits, and now that matters** — see the budget below.

**If you do want it tighter**, the lines paying least are the ones the picture already tells:
*"Stepping out of the tent, he spots an old newspaper"*, *"He heads off to Wales for this spiritual
retreat"*, *"Time for bed."* Roughly 25 words, no joke lost.

### 3 · 🔴 The two beats that carry the politics are missing

| Missing | Why it is load-bearing |
|---|---|
| **"It doesn't say who owns the machines. Same man who owns the flats."** | [`the-reader.md`](../../../marketing/the-reader.md) is a hard rule: **never raise automation fear without naming the beneficiary in the same piece** — unaimed, it demonstrably feeds nativism. The draft never mentions the machines *or* the owner, so scene 11's reach-back to scene 4 has nothing to reach with. This is the film's whole argument |
| **Scene 12 — the fire, and the last word** | The brief: *"write the last word first — the `12d` tilt is timed to it."* The draft ends on *"Excuse the pun."* The tilt has nothing to cut to |

Both are parked in **chunk 8 below, unrendered**, in the previous draft's words. They are there so
the gap is visible — not as a decision.

---

## Settings

| Control | Set to | Why |
|---|---|---|
| **Voice** | **Camping Narrator** | Already built and saved |
| **Model** | **Eleven v3** | The only model that reads audio tags |
| **Stability** | 🔑 **the slider's midpoint (Natural)** | ElevenLabs' own words: *Creative* is *"more emotional and expressive, but prone to hallucinations"*; *Robust* is *"highly stable, but less responsive to directional prompts."* **Natural** is *"closest to the original voice recording"* — the only setting both stable and directable |
| **Language Override** | **off** | |
| **Output Format** | MP3 44.1 kHz 128 kbps | Fine for a stem going into Premiere |
| ~~Similarity~~ · ~~Style~~ | ⚠️ **not present on v3** | Earlier versions of this sheet said "Similarity 75 · Style 0". Those are v2 controls — the v3 panel does not show them |
| **Speed** | *not exposed on v3* | Pacing comes from punctuation and chunk structure |

### ⚠️ Three pieces of common advice that are wrong for v3

| Advice you will find | Why it is wrong here |
|---|---|
| *"Use SSML `<break/>` for exact pauses"* | ⚠️ **Wrong for v3, RIGHT for v2 — and Jack is on v2.** *"Eleven v3 does not support SSML break tags"*, but v2 does, up to 3 seconds, and it is the **documented** pause control. An earlier version of this sheet told you to ignore this advice; that was correct only while we thought the model was v3. See the v2 chunks below |
| *"Drop stability to 50–60%"* | That is v2's numeric slider. **v3's stability is a three-way choice**, not a percentage. Natural |
| *"Use request stitching to keep long narration continuous"* | 🔴 **"Request stitching is not available for the `eleven_v3` model."** ⚠️ And it is **API-only** in any case — there is no stitching in either web screen, so it is not a reason to choose one over the other |

## 🔑 MODEL CHOICE — v2 vs v3, and v2 is the better bet for camping (2026-09-03)

**Jack was on Eleven Multilingual v2, not v3.** ⚠️ **That is not simply a mistake to undo.** The two
models expose completely different controls, and v2's are the ones camping's problem needs.

| | **Multilingual v2** | **Eleven v3** |
|---|---|---|
| 🔑 **Similarity** — *"how closely the AI should adhere to the original voice"* | ✅ **Yes** | 🔴 **No such control** |
| 🔑 **Speed** — 0.7–1.2, and the brief wants **unhurried** | ✅ **Yes** | 🔴 **Not available** |
| **Style Exaggeration** — 0 enforces "never perform" | ✅ Yes | 🔴 No |
| **Audio tags** (`[understated]` etc.) | 🔴 **No — they get read aloud** | ✅ Yes |
| **Request stitching** (prosody across chunks) | ✅ Yes | 🔴 *"not available for the `eleven_v3` model"* |
| Characters per generation | 10,000 | 5,000 |
| Professional Voice Clones | ✅ Yes | 🔴 *"does not currently support"* |

🔑 **The trade is tags against voice fidelity, speed and continuity.** The reported fault is *"it is
not doing the voice"* — and **Similarity is literally the control for that, and only v2 has it.**
This sheet's own research says over-tagging is the AI-slop tell and punctuation does most of the
work, so tags are the cheaper thing to give up.

🔴 **If v2 is the model, every audio tag must come out of the chunks.** v2 does not read them; it
speaks them. The tagged blocks below are the **v3** versions.

### Jack's settings, judged

From the 2026-09-03 screenshot, against ElevenLabs' *"most common setting is stability around 50,
similarity around 75, and keeping style at 0"*:

| Control | Set to | Verdict |
|---|---|---|
| **Similarity** | ~74 | ✅ Right |
| **Stability** | ~48 | ✅ Right. Too low is *"overly random… speak too quickly"*; too high is *"monotonous"* |
| **Style Exaggeration** | **0** | ✅ Right, and it is the register |
| 🔴 **Speed** | **right of centre — faster than 1.0** | 🔴 **Wrong direction.** The brief wants unhurried. Drop to **0.9–0.95** |

### ⚠️ But Similarity only bites on a clone

*"The similarity slider dictates how closely the AI should adhere to **the original voice**."*
🔑 **A Voice Design voice has no original recording** — it was generated from a prompt. So Similarity
has far less to hold on to, which is why 74 did not rescue the read.

🥇 **This is the third independent argument for the same conclusion:** clone round 13's Suno take as
an **Instant Voice Clone**, then run it on **v2** with Similarity ~75. Then the slider has a real
reference, the accent is one we already approved, and Speed and Style are there to shape it.

## 🔑 RULED 2026-09-03 — the Text to Speech box, chunk by chunk. The Karen method.

⚠️ **This replaces the Studio recommendation, which was wrong.** It rested on request stitching,
and **request stitching is an API feature** (`previous_text` / `next_text`). Hand-driving the
website, it was never available in *either* screen — so it was never a reason to prefer Studio.
Two corrections and one confirmation:

| What I said | What is actually true |
|---|---|
| *"Six pastes lose prosody continuity because stitching doesn't work on v3"* | 🔴 True but **irrelevant**. Stitching is API-only. Studio would not have given it either |
| *"Studio's free regenerations are the repair budget"* | ⚠️ The **Text to Speech box has them too** — and it is the one screen **both** sources agree on. The [announcement blog](https://elevenlabs.io/blog/two-free-regenerations) grants them to *"Speech Synthesis via the website"* and **denies them to Projects**; the [Studio docs](https://elevenlabs.io/docs/eleven-creative/products/studio) grant them to Studio. **This screen is the safe one** |
| *"v3 takes 5,000 characters"* | ✅ Still true. The whole script is 2,609, so it *could* go in one paste |

🔑 **And chunking beats one big paste, for a reason that is purely about repair.** The free
allowance is **two re-rolls per generation**, not per character:

| Approach | Charged | Free re-rolls | A bad line costs |
|---|---|---|---|
| One paste of 2,609 | 2,609 | 2, covering all 2,609 | re-roll the **whole script** |
| **Six chunks** | **2,609 — the same** | **12** | re-roll **one chunk (269–573)** |

**Same spend, six times the repair budget, and a bad line never costs you a good one.** This is
exactly what [`../../karen/narration/script.md`](../../karen/narration/script.md) already does with
nine chunks, and it is why that worked.

### The click-path

1. **Text to Speech.** Voice = **Camping Narrator**. Model = **Eleven v3**.
2. **Stability → the midpoint of the slider (Natural).** ⚠️ Not toward Robust: that is documented
   as *"less responsive to directional prompts."* Not toward Creative: *"prone to hallucinations."*
3. ⚠️ **There is no Similarity or Style control on v3** — the earlier "Similarity 75 · Style 0" in
   this sheet was v2's settings. v3 exposes Stability, Language Override and Output Format only.
   **Leave Language Override off.**
4. **Output Format: MP3 44.1 kHz 128 kbps** is fine for a narration stem going into Premiere.
5. **Paste chunk 1 alone. Generate. Listen.** Judge it on the rules below *before* chunk 2.
6. **Bad read → Regenerate.** Free twice, then charged. ⚠️ **Do not touch the text** — an edit
   forfeits both re-rolls for that chunk.
7. **Download each chunk as its own file** as you accept it, and name it `chunk-N`.
8. ⚠️ **Do not use "+ Add speaker."** That is v3's multi-speaker dialogue mode. This is one narrator.

⚠️ **Three things forfeit a free re-roll:** editing the text, voice or model; **refreshing the
page**; and **more than two hours** passing since the generation. So judge and re-roll a chunk in
one sitting, and download before you walk away.

⚠️ **The 250-character floor still binds.** ElevenLabs: *"very short prompts are more likely to
cause inconsistent outputs. Encourage prompts greater than 250 characters."* ✅ Every chunk below
clears it. 🔴 **Never paste a single line to fix a delivery** — *"Fuck me."* is nine characters.
Re-roll the whole chunk and trim the audio.

## Three rules that decide the read

**1 · Tags — the Karen set, one per paragraph.** ⚠️ **Corrected 2026-09-03.** An earlier version of
this sheet banned `[sarcastically]` and allowed only two tags in the whole script, arguing that
[`docs/voice.md`](../../../voice.md)'s *"never signals a joke"* rule forbade them. 🔴 **That was my
rule, not the house's.** [`../../karen/narration/script.md`](../../karen/narration/script.md) is the
worked precedent, it uses five tags freely, and it is the one that worked.

**The house set, copied from Karen's sheet:**

| Tag | Job |
|---|---|
| `[understated]` | The workhorse. Deadpan, thrown away. Most of the jokes |
| `[matter-of-fact]` | Stating a thing flatly that ought to be an outrage |
| `[sarcastically]` | Used sparingly and only where the line is *already* sarcastic on the page |
| `[deliberate]` | Slows a line that carries weight — a reveal, a fact |
| `[drawn out]` | Stretches a beat for comic delay |
| `[sighs]` | The one crack in the mask, chunk 8 only |

🔑 **Karen's own rule, kept: one tag per paragraph, maximum.** Over-tagging is the most recognisable
tell of AI narration, and ElevenLabs' constraint is that **the voice must match the tag** (*"don't
expect a whispering voice to suddenly shout with a `[shout]` tag"*). 🔴 **Never `[shouts]`,
`[excited]`, `[angry]`** — anything outside this narrator's range breaks him instantly.

🔑 **Karen's parallel is exact and worth copying:** her sheet renders *"Nice train shot, though."* as
its **own paragraph with `[matter-of-fact]`.** Camping's *"Nice tie, though."* now does the same.

⚠️ **If a tag gets read aloud instead of performed** — it happens — delete that tag and let the
punctuation carry the line.

**2 · Strip the house VO markup — it is not for the TTS.**
[`forms.md`](../../../story-craft/forms.md) marks pauses `/`, `//`, `///` and `[SIL n s]`. Those are
**executed in the edit**, by sliding the clip in Premiere. Only two marks survive into the box:
`[sighs]` (a real v3 tag) and the **ellipsis**, which v3 documents as *"pauses and emphasis."*

## What changed from the draft, and why

| Change | Why |
|---|---|
| `2008:` `2026:` → **`Two thousand and eight.` `Twenty twenty-six.`** | A digit-colon opening gets read as a label, not a sentence. Normalise **before** synthesis, never after |
| `ETFs` → **`E.T.F.s`** · `IPA` → **`I.P.A.`** · `1%` → **`one percent`** | Raw abbreviations are mispronounced. Standing rule from [`voice.md`](./voice.md) |
| `4 by 4's` → **`Four by fours`** | The digit-plus-apostrophe form risks *"four by four apostrophe s."* ⚠️ Diverges from the normalisation list in `voice.md`; this is the safer spelling for the ear |
| `Ayahuasca` → **`ayawaska`** | `voice.md`'s normalisation list. Spell it how it sounds |
| **Semicolons removed** | They produce muddy pacing. Replaced with full stops and em-dashes |
| `Can you blame em, really?` → **`Can you blame 'em, really.`** | 🔑 **A question mark lifts the pitch, which sounds eager. The full stop keeps it flat, which is the joke.** Also the missing apostrophe on `'em` |
| **Nested quotes removed** — `thinks, "…a few more "mates" soon"` | Quotes inside quotes confuse the parse. The line is the narrator ventriloquising, so it reads straight |
| `devils lettice` → **`devil's lettuce`** · `Star trader` → `star trader` | Typos. `lettice` would be read as written |
| `the fact that… or the fact that…` → **`That… Or that…`** | The repetition ate the joke's timing. Same words, tighter |
| **Ellipses kept where the draft had them** | `It is a tad chilly, though.` / `Safe to say it has kicked in...` / `It being Bob.` — v3 documents the ellipsis as a genuine pause-with-weight control |
| `Uh,` **kept** | It reads as dismissiveness, not a stumble, and a disfluency is anti-slop. Delete it if it reads as a glitch |
| **Chunks 6 and 7 merged** | The newspaper beat alone is 187 characters — under the stability floor |

---

## Chunk 1 — 2008 · 363 chars

```
Two thousand and eight. Meet Tarquin. Star trader on the NatWest floor, betting heavily on leveraged E.T.F.s. Pain infliction usually looks this banal.

[matter-of-fact] Uh. Nice tie, though.

Meet Bob. Standard middle-manager bloke. Getting away for a few days with his wife Jo, away from the financial stress of it all.

[understated] Can you blame 'em, really.
```

## Chunk 2 — 2026 · 420 chars

```
Twenty twenty-six. Tarquin runs the country's biggest private equity firm, the one that buys up social housing.

[sarcastically] The bastard looks very pleased with himself. He ditched the tie, at least.

Driving home from work, he spots this lot, and thinks: interest rates up one percent next week. You chaps are going to have a few more mates soon. Cannot wait for my bonus.

[understated] It is a tad chilly, though.
```

## Chunk 3 — Bob's tent · 269 chars

```
Bob spends his days in this oh-so-luxury tent, taking any charitable beer donations he can get his hands on.

[understated] I don't know what's worse. That his cause is so rarely supported. Or that the ones who do support it judge him for being an I.P.A. man.

Fuck me.
```

## Chunk 4 — therapy · 525 chars

```
Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni.

[matter-of-fact] The therapist tries to explain that empathy for the homeless does not warrant an emergency appointment. It does not sink in.

So he gives up, and says there is no helping him. He needs the strongest psychedelic known to man to fix his car crash of a personality.

[understated] Forgive the pun.

Tarquin agrees that he needs to explore himself more. So he heads off to get supplies before his trip to Wales.
```

## Chunk 5 — the car park · 459 chars

```
Parks how he usually does. Bob is none too pleased.

[understated] I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.

Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours. Most common vehicle in this car park.

[deliberate] Tarquin locks on to a background figure. Not so much a wrestle with his conscience — just a small acknowledgement that it is in there... It being Bob.
```

## Chunk 6 — Wales, and the newspaper · 573 chars

```
He heads off to Wales for this spiritual retreat. Before they hand over the ayawaska, they insist on meditation. Tarquin has never sat on a floor before.

[drawn out] Safe to say it has kicked in...

He's had enough, bless him. Time for bed.

Awoken by the sound of thunder, with his heart in his throat. Stepping out of the tent, he spots an old newspaper.

Warming his hands on the fire, Bob tries to calm him down. Tells him to pay attention to the date.

[deliberate] Twenty thirty-one. Last one they ever printed.

[understated] He takes the news well. Excuse the pun.
```

## ⬜ Chunk 8 — the ending. NOT in the draft, NOT to be rendered yet

> 🔴 See **"Three things the draft drops"** above. These are the *previous* draft's closing lines,
> parked here so the gap is visible. They carry the two missing beats: **who owns the machines**,
> and **the last word the `12d` tilt is timed to.** Jack's call whether they come back, get
> rewritten, or get replaced.

```
[deliberate] It's not the drugs. The headline says the machines took the jobs. It doesn't say who owns the machines. Same man who owns the flats.

[sighs] Where the fuck have you been. You alright.

The paper goes on the fire. Nobody says sorry; the cans do it.

[understated] I know how this ends... I've never been sure about this bit. Watch what goes up.
```

## 🔊 The v2 chunks — paste these on Multilingual v2

> **Use these on Multilingual v2.** ✅ **Tags kept — Jack's call, 2026-09-03**, on the strength of
> Karen having been generated on v2 with tags and working. That is direct evidence from the account
> that matters, and it beats the undocumented inference this sheet briefly carried. **The tag set and
> the one-per-paragraph density are Karen's.**
>
> 🥇 **Plus the thing Karen's sheet could not use:** **`<break time="x.xs" />`**, v2's *documented*
> pause control, good to 3 seconds. Karen's sheet assumed v3, where SSML breaks do not work, so it
> had to leave pauses to the edit. **On v2 the comic timing goes in the read.** ⚠️ *"Using too many
> break tags in a single generation can cause instability — the AI might speed up, or introduce
> additional noises or audio artifacts"*, so there are **at most two per chunk, at the biggest beats
> only.**
>
> 🔴 **Chunk 1 is the test, and it is free to judge.** If you hear the word *"matter-of-fact"* spoken,
> v2 does not take tags — delete every one and the punctuation carries it, exactly as before. If the
> read simply lands flat and amused, tags work and nothing needs changing.

### 🔴 OPEN — did Karen's tags work on v2, and what does v2 do with a bracket?

**Jack: *"we used tags for Karen and that was v2."*** ⚠️ **The repo cannot settle this.** Karen's
[`voice.md`](../../karen/narration/voice.md), [`README.md`](../../karen/narration/README.md) and
[`script.md`](../../karen/narration/script.md) all specify **Eleven v3** — but that is the *plan*.
**Nothing anywhere records which model was actually used**, which is the same gap that hid the
Camping Narrator's existence.

| | Status |
|---|---|
| Audio tags are a **v3** feature | ✅ Documented |
| `<break time="x.xs" />` works on **v2**, up to 3s | ✅ Documented |
| v2 does not support **phoneme** tags | ✅ Documented |
| 🔴 **What v2 does with `[understated]` — speaks it, or silently ignores it** | ❌ **Not documented anywhere I could find.** A search summary said *"would likely be read aloud"* — that is an inference, not a source |

🔑 **Jack's own result is the strongest evidence available, and it points the other way:** if v2
spoke the tags, Karen's takes would contain the audible word *"understated"*. They do not. **So on
this account, v2 most likely ignores them silently** — in which case Karen's read was carried by the
punctuation and paragraphing, and the tags were doing nothing.

### Two free ways to settle it — spend nothing

1. **History tab.** It records the **model** for every past generation. Open a Karen entry: it says
   v2 or v3. That alone answers the question.
2. **Listen to any Karen take** for an audible "understated" or "sarcastically."

✅ **You do not need the answer before generating.** The v2 chunks below use **break tags only**,
which are documented for v2 — so they are safe whichever way this falls. If History shows Karen ran
on **v3**, the tagged chunks further up are the ones to use instead.


### v2 · Chunk 1 — 2008 · 363 chars

```
Two thousand and eight. Meet Tarquin. Star trader on the NatWest floor, betting heavily on leveraged E.T.F.s. Pain infliction usually looks this banal.

[matter-of-fact] Uh. Nice tie, though.

Meet Bob. Standard middle-manager bloke. Getting away for a few days with his wife Jo, away from the financial stress of it all.

[understated] Can you blame 'em, really.
```

### v2 · Chunk 2 — 2026 · 442 chars

```
Twenty twenty-six. Tarquin runs the country's biggest private equity firm, the one that buys up social housing.

[sarcastically] The bastard looks very pleased with himself. <break time="0.5s" /> He ditched the tie, at least.

Driving home from work, he spots this lot, and thinks: interest rates up one percent next week. You chaps are going to have a few more mates soon. Cannot wait for my bonus.

[understated] It is a tad chilly, though.
```

### v2 · Chunk 3 — Bob's tent · 291 chars

```
Bob spends his days in this oh-so-luxury tent, taking any charitable beer donations he can get his hands on.

[understated] I don't know what's worse. That his cause is so rarely supported. Or that the ones who do support it judge him for being an I.P.A. man.

<break time="0.8s" /> Fuck me.
```

### v2 · Chunk 4 — therapy · 547 chars

```
Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni.

[matter-of-fact] The therapist tries to explain that empathy for the homeless does not warrant an emergency appointment. <break time="0.5s" /> It does not sink in.

So he gives up, and says there is no helping him. He needs the strongest psychedelic known to man to fix his car crash of a personality.

[understated] Forgive the pun.

Tarquin agrees that he needs to explore himself more. So he heads off to get supplies before his trip to Wales.
```

### v2 · Chunk 5 — the car park · 503 chars

```
Parks how he usually does. <break time="0.5s" /> Bob is none too pleased.

[understated] I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.

Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours. Most common vehicle in this car park.

[deliberate] Tarquin locks on to a background figure. Not so much a wrestle with his conscience — just a small acknowledgement that it is in there... <break time="0.6s" /> It being Bob.
```

### v2 · Chunk 6 — Wales, and the newspaper · 595 chars

```
He heads off to Wales for this spiritual retreat. Before they hand over the ayawaska, they insist on meditation. Tarquin has never sat on a floor before.

[drawn out] Safe to say it has kicked in...

He's had enough, bless him. Time for bed.

Awoken by the sound of thunder, with his heart in his throat. Stepping out of the tent, he spots an old newspaper.

Warming his hands on the fire, Bob tries to calm him down. Tells him to pay attention to the date. <break time="1.0s" />

[deliberate] Twenty thirty-one. Last one they ever printed.

[understated] He takes the news well. Excuse the pun.
```

**v2 total: 2741 characters.** Against 3,688 that leaves **947**, plus twelve free re-rolls.

## The budget

**The v2 chunks are 2,741 characters = 2,741 credits.** Chunk 8 would add ~357.

⚠️ **That is not the whole spend.** Voice Design is charged too — the plan in [`voice.md`](./voice.md)
is 6 screening designs at a 150-char preview (900) plus one confirmation at 312.

**Balance confirmed 2026-09-03: 3,688 credits.**

| | Credits | Running |
|---|---|---|
| ~~Designing the voice~~ | ✅ already paid | 0 |
| v2 chunks 1–6, once | 2,741 | 2,741 |
| ✅ **Left, against 3,688** | — | **947** |
| ⬜ *if chunk 8's ending comes back* | +329 | *leaves 401* |

### 🔴 To be clear about what is charged — the click-path does spend credits

**Only *re*-generations are free. Every first generation is charged.**

✅ **The voice is already built, so the 1,212 design spend is gone from this ledger.**

| Step | Charged? | Cost |
|---|---|---|
| ~~Voice design~~ | ✅ **Already done** | 0 |
| **Generating each of the six v2 chunks, first time** | 🔴 **Yes** | **2,741** |
| **Running total before a single repair** | | **2,741 of 3,688 — leaves 947** |
| Re-rolling a chunk, nothing changed | ✅ No | 0, twice per chunk |
| Third re-roll of the same chunk | 🔴 Yes | 291–595 |
| Any re-roll **after editing the text** | 🔴 Yes | full price |
| ⬜ *if the ending returns as chunk 8* | 🔴 Yes | +357, leaves 590 |

✅ **947 left, plus twelve free re-rolls.** That is one paid re-read of the longest chunk (595) and
the shortest (291) on top of the free ones. ⚠️ **Thinner than it was** — the tags and breaks cost
294 characters over the bare script. Judge each chunk before starting the next.

⚠️ **The tags cost 162 characters** across the six chunks (2,447 untagged → 2,609). Worth it, and
still budget it can afford.

🔑 **Read the button before every re-roll.** It says **Regenerate** while a free one remains, and
shows how many on hover; it says **Generate** when you are about to be charged. **Looking is free.**

🔴 **What 730 does not cover is changing your mind about the words.** Every text edit forfeits that
paragraph's free re-rolls and charges full price. **So settle the three content gaps before you
generate anything** — that is the main way to waste this balance.

⚠️ **The licence question is untouched by any of this.** [`voice.md`](./voice.md) rules it:
**Starter ($6/month) is the cheapest plan carrying the Commercial License, and BadCode publishes
this film.** A Free-tier balance grants no commercial rights to the output at all. 🔴 **Confirm the
plan before generating** — credits are not the constraint any more; the licence is.

⚠️ **Whether v3 audio tags are billed as characters is unverified.** The counts above include them;
it is 22 characters across the whole script.

## Judge each chunk before starting the next

The audition line is in chunk 5: *"I'd say it's a Mexican standoff, but there are no stakes and no
one gives a shit."* **Flat and amused wins.** Any lift, any grandeur, any sense it knows it is
funny is wrong, however good the timbre.

| What you hear | Fix |
|---|---|
| **He sells the jokes** | Style is above 0, or a tag crept in. Both must be zero |
| **A tag is read aloud** | It happens. Delete that tag — the punctuation is already doing most of the work |
| **He hesitates on an ellipsis** | Delete it; the pause moves to the edit |
| **A line lifts at the end** | A question mark or colon survived normalisation |
| **The voice drifts between chunks** | Stability is on Creative. Move to Natural |
| **It sounds recited** | Do **not** split into shorter chunks — that is the opposite fix. Re-roll |
| **`Uh.` reads as a glitch** | Delete it. It is the one disfluency in the script |

## Then

**One file per chunk**, into Premiere. The house VO marks (`/`, `//`, `///`, `[SIL]`) are executed
there by sliding clips, per [`forms.md`](../../../story-craft/forms.md) — every line is a cut point.

## Sources

Researched 2026-09-03. Every claim above that is marked with a quotation is from one of these.

- [Prompting Eleven v3](https://elevenlabs.io/docs/best-practices/prompting/eleven-v3) — the tag list, the ellipsis/capitalisation rules, the three stability settings, "does not support SSML break tags", tag-voice matching
- [Text-to-speech best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) — the >250-character stability floor
- [Audio tags 101](https://elevenlabs.io/blog/v3-audiotags) — tag categories
- [Audio tags: precision delivery control](https://elevenlabs.io/blog/eleven-v3-audio-tags-precision-delivery-control-for-ai-speech) — the pacing/emphasis tags (`[deliberate]`, `[drawn out]`, `[understated]`)
- 🔑 **In-repo precedent: [`../../karen/narration/script.md`](../../karen/narration/script.md)** — the house tag set and the one-per-paragraph rule, proven on a finished film
- [Best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) — 🔑 **`<break time="x.xs" />` up to 3s on v2**, the instability warning, and the v3 punctuation alternatives being *"less consistent"*
- [Do pauses and SSML phoneme tags work?](https://help.elevenlabs.io/hc/en-us/articles/24352686926609-Do-pauses-and-SSML-phoneme-tags-work-with-the-API) — 🔴 **Multilingual v2 does NOT support phoneme tags**, so pronunciation is bought by respelling (`E.T.F.s`, `ayawaska`) — which is what the normalisation rules already do
- [Voice settings](https://elevenlabs.io/docs/speech-synthesis/voice-settings) — stability ~50, similarity ~75, style 0; Speed 0.7–1.2
- [Models](https://elevenlabs.io/docs/overview/models) — **v3's 5,000-character limit**
- [Stitching multiple requests](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching) — 🔴 **"not available for the `eleven_v3` model"**
- [ElevenCreative Studio](https://elevenlabs.io/docs/eleven-creative/products/studio) — v3 support, paragraph blocks, per-word regeneration, project limits
- [Two free regenerations](https://elevenlabs.io/blog/two-free-regenerations) and [Does it cost credits to regenerate in Studio?](https://help.elevenlabs.io/hc/en-us/articles/30442535713937-Does-it-cost-credits-to-regenerate-in-Studio) — the free-re-roll allowance and what forfeits it
