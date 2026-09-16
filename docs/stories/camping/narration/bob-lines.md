---
title: Camping — Bob's lines, render-ready
voice: Algenib · profile [`profiles/bob-algenib.md`](./profiles/bob-algenib.md)
source: Jack's script, 2026-09-09
status: ⬜ extracted and prepared, never rendered
---

# Bob's lines — all five

## ✅ B4 v2 — the scene-8 trigger line. WORKED 2026-09-16 (Jack: *"That worked"*)

**Replaces B4** (*"Fucking wank tanks, if only I could have..."*, A3 166.50 → 170.04). The brief:
Jo's death was too subtle, so Bob has to give it away without saying it outright. Seeing the X8
sets off his PTSD and he talks himself down.

**Where the line comes from:**
- **"We should've left early. I should've."** He starts with "we" and corrects it to "I", and
  it pays off B1's *"She wanted to leave early… I said there was no rush"*. The guilt lands
  without anyone explaining it.
- **The breathing count and "Different car. Different fella."** The then-versus-now self-talk
  taught in trauma-focused CBT (PTSD UK, Psychology Tools), and NHS breathing counts out to five.
- **"Two-man tent, this. Just the one man."** The tent is the one they bought for the Wales trip.

**What got it there, in order:**
1. **The first Sample Context was too emotional.** *"A bad fright"*, *"fighting to get his body
   back under control"* and *"every second of it costs him something"* all pushed the read toward
   drama, and it stopped sounding like Bob.
2. **The fix was Bob's original casting wording plus "a hundred times before".** It keeps the
   feeling but plays it as something he has practised. Only that one field changed.
3. **Changing the punctuation did not help.** Full stops turned into commas and a lower-case
   "fucking" were rejected. The line is kept exactly as written.
4. **"We bought this for the trip. I bought…" did not land.** When you only hear it, *this* points
   at nothing, and *"I bought…"* trails off like a lost thought rather than a correction.

⬜ **Timeline:** not placed yet. It runs about 10–12s against B4's 3.5s slot, so the scene-8
picture has to hold longer or the line has to start earlier. B3 (*"Why is he taking two spaces?"*)
can stay or go.

Settings: Composer · Temperature 1 · Voice `Algenib` · Voice Direction and Scene **unchanged**, as
below.

**→ Sample Context** (B4 v2 only)

```
Bob is talking himself down after a bad moment, the way he has done a hundred times before. He has had a long time to get used to it and is not asking for sympathy.
```

**→ Speech block** (no tags)

```
We should've left early. I should've. Fucking wank tanks. Breathe, you daft sod. In, two, three, four, five. Different car. Different fella. Two-man tent, this. Just the one man.
```

⬜ **Assumed, not confirmed:** that the take that worked is option 8 exactly as above, with the
tent-car-park Scene below rather than the voiceover-booth Scene in `profiles/bob-algenib.md`.

## 🔒 The box set is the 2026-09-08 build, unchanged — Jack ruled it 2026-09-09

**Jack: *"do what was saved before for Bob, I don't want the voice to change."*** ✅ **All four
fields are the original build, byte-for-byte.**

⬜ **A rewrite of the Scene and Sample Context was offered and rejected**, and the reasoning is kept
here because it may matter later, not because it should be applied now: both context fields were
written when this voice was a *narrator* candidate — *"a small voiceover booth… reading from a page
he half agrees with"*, *"Bob has narrated this kind of story many times before"* — and Bob in the
script is remembering his own life rather than reading a page.

🔑 **Jack's call is the right one on the evidence available: the build has been heard and the
rewrite has not.** [Changing a variable in a prompt that already works](../../../ai-studio/README.md#-confirmed-2026-09-09--kore-landed-the-camping-narrator-first-take)
is the mistake this session already paid for twice. **Render as built, listen, and only then decide
whether the framing costs anything.**

## One change to the words

`Could'nt` → `Couldn't`. **A misplaced apostrophe is a real pronunciation hazard.** Everything else
is Jack's, including `for christ sakes`, which is how it is said.

## ⬜ One risk to listen for

The Voice Direction stacks **three restraint clauses** — *restrained and inward*, *worn down*,
*delivery sits under the material rather than selling it*. That is close to
[the "boring" recipe](../../../ai-studio/README.md#-ruled-2026-09-04--the-missing-ingredient-was-anger-and-it-is-the-cure-for-boring):
absence of feeling rather than feeling held down. **Left as built, because it is an existing asset
and it has been heard.** ⬜ **If it comes back sleepy, swap one clause for pressure** — *"he has
decided not to be bitter about it, and it costs him something"* — rather than adding anything.

---

## The four Composer fields

**→ Voice Direction**

```
Bob, 47. Deep, gravelly, low chest tone, slightly rough from years of smoking. Restrained and inward. Intelligent, cynical, worn down. Delivery sits under the material rather than selling it. Natural conversational rhythm, short pauses, firm downward endings. Neutral southern English accent as heard in Reading or Guildford, faint London edge, no Cockney vowels or slang.
```

**→ Scene**

```
Sitting outside a tent in a supermarket car park, late, telling somebody about it years after it happened.
```

**→ Sample Context**

```
Bob is talking about his own life and has had a long time to get used to it. He is not asking for sympathy.
```

**→ Speech block**

```
We had four days booked in Wales, and the tent was already in the boot. She wanted to leave early to miss the traffic. I said there was no rush, a young fool I was.

I used to hear so many people debate what to do with us homeless back then, including work camps, euthanasia, and being sectioned. Couldn't give a fuck mate, I just wanted a sandwich for christ sakes. Uh, Armchair manifestos aside…

Why is he taking two spaces?

Fucking wank tanks, if only I could have...

He came out of that tent like a crackhead. I gave him the paper because he was never going to take my word for it.
```

## Where each line lands

| # | Scene | Line |
| --- | --- | --- |
| 1 | **2** · the car | *We had four days booked in Wales…* |
| 2 | **6** · outside Waitrose | *I used to hear so many people debate…* |
| 3 | **8** · the collision | *Why is he taking two spaces?* |
| 4 | **8** · the collision | *Fucking wank tanks, if only I could have...* |
| 5 | **11** · the newspaper | *He came out of that tent like a crackhead.* |

⬜ **Bob has no line in scene 12** — the fire, the ending. The
[three-voice script](./three-voice-script.md) gave him the last human words there; this draft does
not. **The film still has no closing line.**

## To render

```bash
python3 scripts/aistudio-tts.py chunk.txt out.wav --voice Algenib --profile docs/stories/camping/narration/profiles/bob-algenib.md
```

⚠️ **Rewrite the WAV to stereo** or Premiere shows it red.
