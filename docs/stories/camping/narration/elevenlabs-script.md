---
title: Camping — the narration script, optimised for ElevenLabs
status: words are Jack's 2026-09-03 draft, optimised for synthesis — 3 content gaps open
model: Eleven v3
voice: ⚠️ not yet designed. Run voice.md → "THE RUN" steps 1–4 first
settings: Stability Natural · Similarity 75 · Style 0
---

# The script, paste-ready for ElevenLabs

> **What this is:** Jack's 2026-09-03 narration draft, normalised and chunked for **Eleven v3**.
> The words are his; what changed is spelling-for-the-ear, punctuation, chunk boundaries and one
> factual fix. The voice-design plan and the budget are in [`voice.md`](./voice.md) → "THE RUN".
> The job list is [`../narration-brief.md`](../narration-brief.md).

⚠️ **The voice does not exist yet** — no `voice_id` is recorded anywhere in the repo. Run
[`voice.md`](./voice.md) → "THE RUN" steps 1–4 (check the plan, six screening designs, confirm,
save) **before** any of this goes in the box.

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
| **Model** | **Eleven v3** | The only model that reads audio tags |
| **Stability** | 🔑 **Natural** | ElevenLabs' own words: *Creative* is *"more emotional and expressive, but prone to hallucinations"*; *Robust* is *"highly stable, but less responsive to directional prompts."* **Natural** is *"closest to the original voice recording"* — the only setting that is both stable and directable |
| **Similarity** | ~75 | |
| **Style** | **0** | Style pushes performance. This narrator must never perform |
| **Speed** | *not exposed on v3* | Pacing comes from punctuation and chunk structure |

### ⚠️ Three pieces of common advice that are wrong for v3

| Advice you will find | Why it is wrong here |
|---|---|
| *"Use SSML `<break/>` for exact pauses"* | ElevenLabs' v3 doc: **"Eleven v3 does not support SSML break tags."** It is v2 advice — the tag gets read aloud or ignored. Pauses come from the ellipsis and from the edit |
| *"Drop stability to 50–60%"* | That is v2's numeric slider. **v3's stability is a three-way choice**, not a percentage. Natural |
| *"Use request stitching to keep long narration continuous"* | 🔴 **"Request stitching is not available for the `eleven_v3` model."** This is exactly why the ruling above is Studio rather than six pastes |

## 🔑 RULED 2026-09-03 — build it in Studio, not the Speech Synthesis box

⚠️ **This reverses the earlier "paste one chunk at a time" instruction.** Four documented facts
decide it, and three of them were not checked before:

| Fact | Source | What it means here |
|---|---|---|
| **v3 takes 5,000 characters per generation** | [Models](https://elevenlabs.io/docs/overview/models) | The whole script is **2,447**. Chunking was never forced by a limit — earlier notes citing a 3,000 cap were wrong |
| 🔴 **"Request stitching is not available for the `eleven_v3` model"** | [Request stitching](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching) | Stitching (`previous_text`/`next_text`) is *the* mechanism that keeps prosody continuous across separate requests. **On v3 it does not exist.** So six separate pastes pay a drift cost with no fix available |
| 🥇 **Two free regenerations per paragraph**, if text, voice and settings are unchanged | [Two free regenerations](https://elevenlabs.io/blog/two-free-regenerations) | This is the repair budget the 730-credit margin does not have |
| 🥇 **Regenerate a paragraph — or just selected words** | [Studio](https://elevenlabs.io/docs/eleven-creative/products/studio) | One bad word costs nothing and does not touch the rest of the read |

🔑 **So manual chunk-by-chunk is the worst of the three options:** it takes the drift risk of
splitting *and* forfeits Studio's free re-rolls. **One Studio project. Six paragraphs. They are the
six chunks below, unchanged.**

⚠️ **The 250-character floor still applies — per paragraph.** ElevenLabs: *"very short prompts are
more likely to cause inconsistent outputs. Encourage prompts greater than 250 characters."* Studio
generates a paragraph at a time, so a paragraph is a generation. 🔴 **Do not let Studio's editor
split these into their natural sentence paragraphs** — *"Fuck me."* alone is nine characters. **The
blank lines inside each block below are line breaks within one paragraph, not paragraph breaks.**

### The click-path

1. **Studio → New project.** Project settings → **Model: Eleven v3**, voice = the saved camping
   narrator, **Stability Natural · Similarity 75 · Style 0**.
2. **Paste chunk 1 as one paragraph.** Confirm the editor shows **one** block, not four.
3. Repeat for chunks 2–6. Six paragraphs total.
4. **Generate paragraph 1. Listen. Judge it on the audition line rules below** before generating 2.
5. **Bad read → hit Regenerate, not Generate.** The button says *Regenerate* while a free re-roll
   is left and shows how many remain. If it says **Generate**, you are about to be charged — you
   changed the text or the voice.
6. **One bad word → select just that word and regenerate it.** Do not re-read the paragraph.
7. **Export per paragraph** into Premiere.

## Three rules that decide the read

**1 · Almost no tags, and only ones that flatten.** 🔑 **Over-tagging is the single most
recognisable tell of AI narration** — and ElevenLabs' own constraint is that **the voice must match
the tag** (*"don't expect a whispering voice to suddenly shout with a `[shout]` tag"*).

🔴 **`[sarcastic]` is banned here even though it exists.** [`docs/voice.md`](../../../voice.md) is
explicit that this narrator **never signals a joke**; a tag that performs sarcasm is the satire trap
wearing a TTS costume. The permitted set is the *anti*-performance tags only — `[understated]`,
`[deliberate]`, `[drawn out]`, `[sighs]` — which push toward flat, which is the register. **One per
chunk, maximum. Two are used in the whole script.**

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

## Chunk 1 — 2008 · 330 chars

```
Two thousand and eight. Meet Tarquin. Star trader on the NatWest floor, betting heavily on leveraged E.T.F.s. Pain infliction usually looks this banal. Uh. Nice tie, though.

Meet Bob. Standard middle-manager bloke. Getting away for a few days with his wife Jo, away from the financial stress of it all. Can you blame 'em, really.
```

## Chunk 2 — 2026 · 389 chars

```
Twenty twenty-six. Tarquin runs the country's biggest private equity firm, the one that buys up social housing. The bastard looks very pleased with himself. He ditched the tie, at least.

Driving home from work, he spots this lot, and thinks: interest rates up one percent next week. You chaps are going to have a few more mates soon. Cannot wait for my bonus.

It is a tad chilly, though.
```

## Chunk 3 — Bob's tent · 269 chars

```
Bob spends his days in this oh-so-luxury tent, taking any charitable beer donations he can get his hands on.

[understated] I don't know what's worse. That his cause is so rarely supported. Or that the ones who do support it judge him for being an I.P.A. man.

Fuck me.
```

## Chunk 4 — therapy · 493 chars

```
Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni.

The therapist tries to explain that empathy for the homeless does not warrant an emergency appointment. It does not sink in.

So he gives up, and says there is no helping him. He needs the strongest psychedelic known to man to fix his car crash of a personality. Forgive the pun.

Tarquin agrees that he needs to explore himself more. So he heads off to get supplies before his trip to Wales.
```

## Chunk 5 — the car park · 432 chars

```
Parks how he usually does. Bob is none too pleased.

I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.

Bob's mind is thrown into a tailspin every time he sees those wank tanks, as he calls them. Four by fours. Most common vehicle in this car park.

Tarquin locks on to a background figure. Not so much a wrestle with his conscience — just a small acknowledgement that it is in there... It being Bob.
```

## Chunk 6 — Wales, and the newspaper · 534 chars

```
He heads off to Wales for this spiritual retreat. Before they hand over the ayawaska, they insist on meditation. Tarquin has never sat on a floor before.

Safe to say it has kicked in...

He's had enough, bless him. Time for bed.

Awoken by the sound of thunder, with his heart in his throat. Stepping out of the tent, he spots an old newspaper.

Warming his hands on the fire, Bob tries to calm him down. Tells him to pay attention to the date.

Twenty thirty-one. Last one they ever printed.

He takes the news well. Excuse the pun.
```

## ⬜ Chunk 8 — the ending. NOT in the draft, NOT to be rendered yet

> 🔴 See **"Three things the draft drops"** above. These are the *previous* draft's closing lines,
> parked here so the gap is visible. They carry the two missing beats: **who owns the machines**,
> and **the last word the `12d` tilt is timed to.** Jack's call whether they come back, get
> rewritten, or get replaced.

```
It's not the drugs. The headline says the machines took the jobs. It doesn't say who owns the machines. Same man who owns the flats.

[sighs] Where the fuck have you been. You alright.

The paper goes on the fire. Nobody says sorry; the cans do it. I know how this ends... I've never been sure about this bit. Watch what goes up.
```

---

## The budget

**Chunks 1–6 are 2,447 characters = 2,447 credits.** Chunk 8 would add 329.

⚠️ **That is not the whole spend.** Voice Design is charged too — the plan in [`voice.md`](./voice.md)
is 6 screening designs at a 150-char preview (900) plus one confirmation at 312.

**Balance confirmed 2026-09-03: 4,389 credits.**

| | Credits | Running |
|---|---|---|
| Designing the voice | 1,212 | 1,212 |
| Chunks 1–6, once | 2,447 | 3,659 |
| ⚠️ **Left, against 4,389** | — | **730** |
| ⬜ *if chunk 8's ending comes back* | +329 | *leaves 401* |

### 🔴 To be clear about what is charged — the click-path does spend credits

**Only *re*-generations are free. Every first generation is charged.**

| Step | Charged? | Cost |
|---|---|---|
| Six screening voice designs @ 150-char preview | 🔴 **Yes** | 900 |
| One confirmation design @ 312-char preview | 🔴 **Yes** | 312 |
| **Generating each of the six paragraphs, first time** | 🔴 **Yes** | **2,447** |
| **Running total before a single repair** | | 🔴 **3,659 of 4,389** |
| Re-rolling a paragraph, text and voice unchanged | ✅ No | 0, twice |
| Re-rolling selected words, same conditions | ✅ No | 0, same allowance |
| Third re-roll of the same paragraph | 🔴 Yes | 269–534 |
| Any re-roll **after editing the text** | 🔴 Yes | full price — editing drops the converted status |

**So the plan spends ~3,659 and leaves 730.** The free allowance is a *repair* budget, not a way to
generate for nothing.

### 🔑 Where the spend can actually come down

**The 900 is the soft number, not the 2,447.** Voice Design charges the preview text **once per
attempt and returns three voices for it**, so:

| Screening attempts | Candidate voices | Cost | Leaves |
|---|---|---|---|
| 6 (the current plan) | 18 | 900 | 730 |
| **4** | **12** | 600 | **1,030** |
| 3 | 9 | 450 | 1,180 |

⚠️ **Do not economise by shortening the script instead** — that is the part you cannot repair for
free later, because editing text forfeits the re-rolls.

### ⚠️ One conflict in ElevenLabs' own documentation, unresolved

The [Studio help article](https://help.elevenlabs.io/hc/en-us/articles/30442535713937-Does-it-cost-credits-to-regenerate-in-Studio)
and the [Studio docs](https://elevenlabs.io/docs/eleven-creative/products/studio) both say the two
free regenerations apply **in Studio**. The older
[announcement blog](https://elevenlabs.io/blog/two-free-regenerations) says the opposite: *"Free
regenerations apply only to Speech Synthesis via the website, not in Projects or via API."*
"Projects" is Studio's former name, so the blog is most likely stale — but it is not proof.

🔑 **You do not have to resolve it before spending, because the UI tells you first.** The button
says **Regenerate** when the re-roll is free and shows how many remain on hover; it says
**Generate** when you are about to be charged. **Read the button every time. It is free to look.**

⚠️ **Three things forfeit a free re-roll**, per the announcement blog: changing the text, voice or
model; **refreshing the page**; and **more than two hours passing** since the original generation.
So judge and re-roll a paragraph in the same sitting, not the next day.

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
- [Models](https://elevenlabs.io/docs/overview/models) — **v3's 5,000-character limit**
- [Stitching multiple requests](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching) — 🔴 **"not available for the `eleven_v3` model"**
- [ElevenCreative Studio](https://elevenlabs.io/docs/eleven-creative/products/studio) — v3 support, paragraph blocks, per-word regeneration, project limits
- [Two free regenerations](https://elevenlabs.io/blog/two-free-regenerations) and [Does it cost credits to regenerate in Studio?](https://help.elevenlabs.io/hc/en-us/articles/30442535713937-Does-it-cost-credits-to-regenerate-in-Studio) — the free-re-roll allowance and what forfeits it
