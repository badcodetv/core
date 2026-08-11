---
name: Aarron
role: catalyst (five-second cameo)
voice: "Easy, warm street-producer — collaborative, unbothered, lets the city write the hook"
sheet: characters/img/aarron-portrait.png
sheet_full_body: characters/img/aarron-full-body.png
signals: homemade portable DJ desk, headphones, roams NYC, makes tracks with strangers
---

# Aarron

A street-roaming YouTuber/producer who wanders New York making music with whoever he
bumps into. (Touchstone: **Ari at Home** and the wider real-world genre of roaming
"make-a-beat-with-a-stranger" music creators. *Ari at Home* is the reference we
cast against, **not** our character's name — he is Aarron.)

**In the story video he gets roughly five seconds** ([`../story.md`](../story.md#storyboard--scene-by-scene-video-canon),
§3.1), and that limit is deliberate — the believable version is the accidental one.
He happens to pass the phone box, hears Karen's *"I've got all day to complain,"*
stops, records a few seconds on his phone, and walks off. He cuts the tune that
night at home, releases it, it does 20 million views, and **we never see him
again**. He's off doing his next thing. He doesn't lead anything; he just makes
the thing catch.

Structurally he is BadCode's thesis embodied: the idea travels because it became a
*song*, not a speech.

**His big outing is the music video**, not the story video — direction decided
2026-07-22: the whole music video is the freestyle-YouTuber format, Aarron roaming
with Karen, freestyling into the mic.

---

## Flow Character

**Flow Character:** name `TODO — exact tile name as it appears in Flow's picker` ·
project `TODO` · **created by hand in Flow by Kai/Jack**, not by
`flow_create_character`.

> **Naming — settled 2026-08-11 (Kai).** The character is **Aarron**. *Ari at
> Home* is the **real-life reference** we cast against, not his name and not a
> channel in our fiction. This file, its assets (`aarron-*`) and the Flow
> Character all use *Aarron*; the story canon was renamed to match on the same
> date. Earlier transcripts and design docs still say "Ari" — those are records
> of what was said and are left as they are.

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
> blocks say `**Cast:** @Aarron` and describe the shot only — a face described in
> prose competes with the Character binding instead of reinforcing it. The
> `character` parameter matches the Flow tile label with `exact: true`, so the
> name above must be character-for-character correct.

### Reference images

| Slot | File |
| --- | --- |
| Portrait | [`img/aarron-portrait.png`](./img/aarron-portrait.png) |
| Full body | [`img/aarron-full-body.png`](./img/aarron-full-body.png) |

Both generated from the **Look** prompt below. Upload both into the Character
editor — Flow asks for a portrait *and* a full-body reference.

### Look

The `STYLE LOCK` block is shared verbatim with
[`karen.md`](./karen.md#look) — it is the register for this story's cast, and
must stay identical across both characters or they will not read as being in
the same film.

The **wearable rig is the character**: it is what makes him legible as a
roaming street producer in a single frame, so the harness, keyboard, mic and
cables are load-bearing, not costume detail.

```prompt
Please STYLE LOCK (keep identical every time):
Look: cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours.
Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.
Color: punchy, vibrant palette with warm skin tones; mild color cast like aged film; deep but soft blacks (not HDR).
Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).
Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.
Output: high detail, natural imperfections, candid snapshot energy.
Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look.
 Full-body portrait on a pure white seamless background (no environment). Vertical 4:5, full head-to-toe, centered. A young man (early–mid 20s), light skin, short curly light-brown hair, clean-shaven, average height and build. He stands relaxed, facing slightly toward camera, looking down in concentration while playing a wearable keyboard/synth.
Wearable rig (must be clear and functional):

Large over-ear headphones. Black backpack-style harness with chest straps and a secure waist belt. A compact keyboard mounted to the front of the harness at waist height; both hands on the keys. A small microphone with a foam windscreen mounted on/near the upper chest/shoulder area. Include realistic straps, buckles, brackets, and cables connecting components (no floating parts).
Clothing: patterned crewneck sweater, casual trousers, everyday shoes.
```

### Voice

**Base voice: Zubenelgenubi.**

```prompt
Young American male in his 20s with a relaxed mid-low voice. Confident, casual and naturally cool, with slightly dry humour and the easy rhythm of a musician. Clear but conversational diction, understated energy and a little swagger. Friendly without sounding eager or goofy. Avoid announcer voice, exaggerated enthusiasm, deep gravel, theatrical delivery or surfer caricature.
```

> Consistent with the written voice in this file's frontmatter — *"easy, warm
> street-producer — collaborative, unbothered."* Unlike Karen, he has **one
> voice across both videos**: he is barely in the story video (five seconds,
> probably no line at all), and the music video is his format. Nothing to split.

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
