---
name: Susan
role: the friend (the hinge — delivers the pep talk that starts everything)
voice: "New York, dry and lived-in — the one person who talks to Karen straight and gets away with it"
sheet: characters/img/susan-portrait.png
sheet_full_body: characters/img/susan-full-body.png
signals: bar seat next to Karen, olive suede bomber, phone to her ear in bed, unimpressed patience
---

# Susan

Karen's friend. Named **Susan** on 2026-08-11 (Kai) — before that the canon only
ever called her *"the friend."*

She is the drinking buddy in Act 1 and, the morning after, **the hinge of the whole
story**. Karen wakes with no phone, no memory and no job, gets to the phone box, and
rings Susan. Susan is the one who tells her what actually happened — *"Karen.
Yesterday you got sacked. By an AI. And you dropped your phone in the river."* — and
then, when Karen asks what she's supposed to do now, aims her at the rest of the
film: *"You complain. You're Karen — if there's one person alive who can get on that
phone and not give up… what else are you doing today?"*

That line is the story's ignition. Nothing after it happens without her.

Her value is that she is **not** impressed by Karen. Everyone else in Act 1 either
endures Karen or is fired by her; Susan is the one person who can flatten her in a
sentence and still be on her side. The affection has to read through the bluntness —
if she plays as contemptuous, the pep talk becomes mockery and the hinge snaps.

Scenes: the bar and the Polaroid compilation ([`../story.md`](../story.md#15-the-bar-in-polaroids--redo-compress-hard),
§1.5), and the morning-after call (§1.7) — including the waking-in-bed shot that
deliberately mirrors Karen's.

**Open:** her exact pep-talk wording is still unlocked ([`../story.md`](../story.md),
§1.7 — structure locked, words open).

---

## Flow Character

**Flow Character:** name `Susan` ·
id `05d2f68b-a762-476d-b53a-069609fc73f8` ·
project `da8feea7-0574-437b-8ff9-97da233a0a4f` (*"Aug 10, 12:51 PM"*) ·
**created by hand in Flow by Kai/Jack**, not by `flow_create_character`.
**Confirmed live 2026-08-14.**

> **Why these prompts live here.** Flow's Character editor takes a **look**, a
> **voice** and a **personality**, and takes **portrait + full-body** reference
> images. Our automation cannot set any of the text fields —
> `createCharacter` only uploads references and fills *Character Name*
> (`packages/flow-mcp/src/flow-client.ts:464-484`). So everything below is
> **hand-entered into Flow**, and this file is the only record of it. Treat the
> blocks as a **restore point**, not documentation: keep them verbatim, so the
> Character can be rebuilt identically if it is ever lost or re-made.
>
> **Casting rule:** these prompts are never pasted into a scene prompt. Scene
> blocks say `**Cast:** @Susan` and describe the shot only — a face described in
> prose competes with the Character binding instead of reinforcing it. The
> `character` parameter matches the Flow tile label with `exact: true`, so the
> name above must be character-for-character correct.

### Reference images

| Slot | File |
| --- | --- |
| Portrait | [`img/susan-portrait.png`](./img/susan-portrait.png) |
| Full body | [`img/susan-full-body.png`](./img/susan-full-body.png) |

Both generated from the **Look** prompt below. Upload both into the Character
editor — Flow asks for a portrait *and* a full-body reference.

### Look

> **Note — Susan's references are in a different register to Karen's and
> Aarron's, and someone should rule on it.** Karen and Aarron share a `STYLE
> LOCK` block verbatim (cinestyle 800+, grainy super-8, halation, candid
> snapshot energy). Susan's prompt is the opposite: *clean commercial fashion
> e-commerce photography*, even softbox lighting, sharp at f/5.6, greige
> cyclorama. As a **Character reference** that is arguably the better input —
> a neutral, evenly-lit, unambiguous plate is exactly what a face binding
> wants, and the film register gets applied per shot anyway. But it is a
> divergence from the other two, so it is recorded here rather than quietly
> normalised. **If the references should be re-shot in the shared `STYLE LOCK`,
> say so** — the prompt below is preserved verbatim either way.

```prompt
A woman in her late 30s with fair skin and long dark brown wavy hair
parted in the centre, falling just past her shoulders. She wears an
unzipped olive-taupe suede bomber jacket with a stand collar, silver
zip, and ribbed cuffs and hem; a plain cream crew-neck cotton t-shirt
tucked in underneath; mid-blue straight-leg denim jeans with subtle
fading at the thighs; and brown leather low-top sneakers with cream
rubber soles.

She stands squarely facing the camera, feet shoulder-width apart, arms
relaxed at her sides, with a calm, neutral expression and direct eye
contact.

Seamless greige studio cyclorama, with a soft contact shadow pooling
at her feet.

Full-body shot, eye-level, subject centred with generous negative
space on both sides. Ultra-wide 21:9 frame.

Clean commercial fashion e-commerce photography. Even, soft three-point
softbox lighting with minimal shadow. Shot on an 85mm lens at f/5.6,
sharp throughout. Muted warm-neutral colour grading, natural skin
texture, fine fabric detail.
```

### Voice

**Base voice: Kore.**

```prompt
American woman in her late 30s to early 40s with a natural New York accent, confident mid-range voice and a slightly sharp, lived-in edge. Quick conversational rhythm, dry humour, strong opinions and subtle impatience, but still grounded and believable. A touch of nasal "Karen" energy without whining or caricature. Clear diction, expressive emphasis, occasional restrained sarcasm and a faint rasp when annoyed. Avoid cartoonish delivery, bland neutrality, sing-song phrasing, theatrical acting or exaggerated accent.
```

> **She is deliberately adjacent to Karen, not a copy.** Both prompts ask for a
> New York woman with restrained sarcasm and a rasp when annoyed, and both ban
> whining and caricature — they should sound like they drink together. The
> separation is age and temperature: Karen is *controlled irritation*
> (Gacrux, higher mid-range, smoky), Susan is *quick and impatient* (Kore,
> confident mid-range, faster rhythm). If a take makes them hard to tell apart
> on audio alone, push Susan faster and drier rather than lowering her pitch.
>
> One voice, one video: she is only in the story video. Nothing to split, unlike
> [`karen.md`](./karen.md#voice).

### Personality — deliberately left empty

**Ruled 2026-08-11 (Kai): we do not fill Flow's personality field, for any
character.** A standing personality colours every shot the Character appears in,
which fights per-scene direction and makes video prompts harder to write — and
keeping those as easy as possible is the priority. It is the same logic as the
casting rule above: anything baked into the Character competes with the scene
instead of serving it.

So the **scene prompt is the only place** that says what the character is doing
or feeling. If a shot needs an attitude, put it in that shot. This is not a
backlog item — do not fill it in.
