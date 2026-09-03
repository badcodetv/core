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

### 2 · 439 words against a 250–320 budget

[`narration-brief.md`](../narration-brief.md) sets the ceiling at **~155 words/minute**, *"and an
authoritative voice sits under it"*, giving **≈250–320 words** — *"not 380, because three stretches
are wordless."*

The draft is **439**. That is ~37% over, and it is the same overrun the 2026-09-01 audit found in
the last draft (445). ⚠️ **Cutting is not a synthesis job** — but the lines most likely to go are
the ones doing a job the picture already does: *"Stepping out of the tent, he spots an old
newspaper"*, *"He heads off to Wales for this spiritual retreat"*, *"Time for bed."*

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

⚠️ **Ignore the widely-repeated advice to use SSML `<break/>` for pauses.** ElevenLabs' v3 doc is
explicit: **"Eleven v3 does not support SSML break tags."** That advice is written for v2 and will
either be read aloud or ignored.

⚠️ **And ignore "drop stability to 50–60%".** That is the v2 numeric slider. v3's stability is a
three-way choice, not a percentage.

## 🔑 Three rules that decide the read

**1 · Render one chunk at a time, in order.** ElevenLabs: *"very short prompts are more likely to
cause inconsistent outputs. Encourage prompts greater than 250 characters."* ✅ Every chunk below
clears 250. **Never split a chunk to fix one line** — you drop under the floor and the voice
destabilises. Generate the whole chunk and trim the audio.

**2 · Almost no tags, and only ones that flatten.** 🔑 **Over-tagging is the single most
recognisable tell of AI narration** — and ElevenLabs' own constraint is that **the voice must match
the tag** (*"don't expect a whispering voice to suddenly shout with a `[shout]` tag"*).

🔴 **`[sarcastic]` is banned here even though it exists.** [`docs/voice.md`](../../../voice.md) is
explicit that this narrator **never signals a joke**; a tag that performs sarcasm is the satire trap
wearing a TTS costume. The permitted set is the *anti*-performance tags only — `[understated]`,
`[deliberate]`, `[drawn out]`, `[sighs]` — which push toward flat, which is the register. **One per
chunk, maximum. Two are used in the whole script.**

**3 · Strip the house VO markup — it is not for the TTS.**
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

| | Credits | Running |
|---|---|---|
| Designing the voice | 1,212 | 1,212 |
| Chunks 1–6, once | 2,447 | 3,659 |
| ✅ **Left, against 4,739** | — | **1,080** |

🔴 **1,080 is thinner than the last draft's margin** — it buys chunk 6 (532) plus chunk 4 (493) and
nothing more. **Two full passes do not fit.** Render once, re-render only what fails.

🔑 **Settle the three content gaps first.** Rendering a 439-word script that is about to lose ~120
words spends roughly 700 credits on lines that will not survive the cut.

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

- [Prompting Eleven v3](https://elevenlabs.io/docs/best-practices/prompting/eleven-v3) — the tag list, the ellipsis/capitalisation rules, the three stability settings, "does not support SSML break tags", tag-voice matching
- [Text-to-speech best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) — the >250-character stability floor
- [Audio tags 101](https://elevenlabs.io/blog/v3-audiotags) — tag categories
- [Audio tags: precision delivery control](https://elevenlabs.io/blog/eleven-v3-audio-tags-precision-delivery-control-for-ai-speech) — the pacing/emphasis tags (`[deliberate]`, `[drawn out]`, `[understated]`)
