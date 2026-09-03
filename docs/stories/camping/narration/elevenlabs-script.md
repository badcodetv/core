---
title: Camping — the narration script, formatted for ElevenLabs
status: words final — blocked on the voice being designed
model: Eleven v3
voice: ⚠️ not yet designed. Run voice.md → "THE RUN" steps 1–4 first
settings: Stability Natural · Similarity 75 · Style 0
---

# The script, paste-ready for ElevenLabs

> **What this is:** the five chunks of the camping narration, normalised for synthesis and
> formatted for **Eleven v3**. ⚠️ **The voice does not exist yet** — no `voice_id` is recorded
> anywhere in the repo, so [`voice.md`](./voice.md) → "THE RUN" steps 1–4 (check the plan, six
> screening designs, confirm, save) run **before** any of this goes in the box. The script's job list is
> [`../narration-brief.md`](../narration-brief.md). The words are the 2026-09-01 rebuild and are
> unchanged — only the markup is new.

## Settings

| Control | Set to | Why |
|---|---|---|
| **Model** | **Eleven v3** | The only model that reads audio tags |
| **Stability** | 🔑 **Natural** | Documented: *Creative* is "prone to hallucinations", *Robust* is "less responsive to directional prompts". Natural is the only setting that is both stable and tag-responsive |
| **Similarity** | ~75 | |
| **Style** | **0** | Style pushes performance, and this narrator must never perform |
| **Speed** | slightly slow, if exposed | The brief wants unhurried |

## 🔑 Three rules that decide the read

**1 · Render one chunk at a time, in order.** Every chunk is **over 250 characters**, which is
ElevenLabs' own stability floor — *"very short prompts are more likely to cause inconsistent
outputs."* ✅ All five clear it (334 / 549 / 317 / 322 / 734). **Never split a chunk into single
lines** to fix a delivery: you drop under the floor and the voice destabilises.

**2 · 🔴 Almost no audio tags, and that is deliberate.** The brief's baseline is `{FLAT}` and
[`docs/voice.md`](../../../voice.md) is explicit that the narrator **never signals a joke**. A
`[sarcastic]` tag makes him *perform* sarcasm, which is the satire trap wearing a TTS costume — and
ElevenLabs' own rule is that **the voice must match the tag**. The voice is already cast deadpan by
the design prompt. **So chunks 1–4 carry no tags at all**, and chunk 5 carries exactly one.

**3 · 🔴 Strip the house VO markup — it is not for the TTS.**
[`docs/story-craft/forms.md`](../../../story-craft/forms.md) marks pauses `/`, `//`, `///` and
`[SIL n s]`. Those are **executed in the edit**, by sliding the clip in Premiere — paste one into
ElevenLabs and it gets read or it confuses the model. **Only two marks survive into the box:**
`[sighs]` (a real v3 tag) and the **ellipsis**, which v3 documents as a genuine pause-and-emphasis
control.

⚠️ **Whether audio tags are billed as characters is unverified** — we could not find it documented.
Budget as if they are; it is 9 characters here.

## The one tag, and why it is `[sighs]`

The brief spends exactly one `{WARM}` crack, in chunk 5, and says it is *worth more than every joke
in the script.* There is no documented `[warmly]` or `[softly]` tag, and ElevenLabs warns that
experimental tags "may be less consistent."

🔑 **`[sighs]` is documented, and it is the better direction anyway:** the crack is not the narrator
turning kind, it is **the mask dropping for one line.** A sigh into *"Where the fuck have you been.
You alright."* is that, exactly — and it costs nothing in register, because a sigh is not a signal.

## Bob's word — ✅ ruled 2026-09-03

**The real word, uncensored.** Canon is *"Where the fuck have you been, then?"*; the script had
`hell`, softened for **Suno's** filter, which no longer applies. 🔑 **Jack's call, made: restore it.**
Chunk 4 already carries `gives a shit`, so the register was already set. The trailing `then` stays
out — the narrator is reporting Bob, not doing him.

⚠️ **If ElevenLabs does filter it** (undocumented either way), the fallback is `hell`, not an
asterisked spelling — **never write a censored swear anywhere in this repo.**

## ⚠️ One open call before you render

| | |
|---|---|
| **Ellipsis in chunk 5** | One is added — `I know how this ends... I've never been sure about this bit.` It earns the admitted uncertainty a beat. Delete it if the pause reads as hesitation rather than weight |

## Normalisation — already applied, do not undo it

`Two thousand and eight` · `Twenty thirty-one` · `E.T.F.s` · `one percent` · `4 by 4's` (not in this
script, but the standing rule). **Normalise before synthesis, never after.** A question mark lifts
the pitch and a colon does the same — both are why several lines end in a full stop that looks wrong
on the page and is right in the ear.

---

## Chunk 1 — 2008 · 334 chars

```
Two thousand and eight. Tarquin, star trader on the NatWest floor, betting other people's houses on leveraged E.T.F.s. He is the reason it happens. Pain infliction usually looks this banal. Nice tie, though.

Meet Bob. Middle manager. Normal. Off for a few days with his wife Jo, away from the stress of it. Can you blame him, really.
```

## Chunk 2 — 2026 · 549 chars

```
Eighteen years on. Tarquin runs the biggest private equity firm in the country. It buys social housing. It does not rent them out. Empty pays better than full — the price climbs either way.

What a brilliant businessman. He ditched the tie, at least. Driving home he spots this lot. Rates up one percent next week. You chaps'll have a few more mates soon.

His car heater broke last week. Worst four days of his life. Three ways past a man in a tent. Ignore him. Politely say no — ignoring him with manners. Or stop. Have a guess which one's rarest.
```

## Chunk 3 — therapy · 317 chars

```
Tarquin sought professional help. He'd felt a feeling, first time since the devil's lettuce at uni. The therapist explains that empathy for the homeless is not an emergency. It doesn't sink in.

So he gives up, and prescribes the strongest psychedelic known to man for his car crash of a personality. Forgive the pun.
```

## Chunk 4 — the car park · 322 chars

```
Parks how he usually does. Bob is none too pleased. I'd say it's a Mexican standoff, but there are no stakes and no one gives a shit.

Bob calls them wank tanks. Most common vehicle in this car park. Tarquin clocks him. Not a wrestle with his conscience — just a small acknowledgement that it's in there. Then he shuts it.
```

## Chunk 5 — Wales, and the newspaper · 734 chars

```
Wales. Tarquin has never sat on a floor before. And somewhere in all that he works out that the distance between him and the man outside the supermarket is about four bad months and a bit of luck.

Thunder. He's out of the tent with his heart in his throat. Christ, that's strong stuff. Give it an hour.

Bob's at the fire, telling him to look at the date. Twenty thirty-one. Last one they ever printed.

It's not the drugs. The headline says the machines took the jobs. It doesn't say who owns the machines. Same man who owns the flats.

[sighs] Where the fuck have you been. You alright.

The paper goes on the fire. Nobody says sorry; the cans do it. I know how this ends... I've never been sure about this bit. Watch what goes up.
```

---

## The budget

**2,256 characters = 2,256 credits**, the one tag included.

⚠️ **That is not the whole spend.** Voice Design is charged too — the plan is 6 screening designs at
a 150-char preview (900) plus one confirmation at 312, so **1,212 before a word of script is read.**

| | Credits | Running |
|---|---|---|
| Designing the voice | 1,212 | 1,212 |
| The whole script, once | 2,256 | 3,468 |
| ✅ **Left for re-reads** | — | 🥇 **1,271** |

**1,271 buys chunk 5 (734) plus one short chunk**, or all three short ones. It does **not** cover
chunks 5 and 2 together. 🔴 **Two full passes do not fit** — render once, re-render only what fails.
Full ledger and the design prompts: [`voice.md`](./voice.md) → "THE RUN".

## Judge each chunk before starting the next

The audition line is in chunk 4: *"I'd say it's a Mexican standoff, but there are no stakes and no
one gives a shit."* **Flat and amused wins.** Any lift, any grandeur, any sense it knows it is funny
is wrong, however good the timbre.

| What you hear | Fix |
|---|---|
| **He sells the jokes** | Style is above 0, or a tag crept in. Both must be zero |
| **He hesitates on the ellipsis** | Delete it — the pause moves to the edit |
| **A line lifts at the end** | Check for a question mark or colon that survived normalisation |
| **The voice drifts between chunks** | Stability is on Creative. Move to Natural |
| **It sounds recited** | Do **not** split into shorter chunks — that is the opposite fix. Re-roll |

## Then

**Out as one file per chunk**, into Premiere. The house VO marks (`/`, `//`, `///`, `[SIL]`) are
executed there by sliding clips, per [`forms.md`](../../../story-craft/forms.md) — every line is a
cut point.
