---
name: Karen Bell
role: protagonist (stereotype → leader)
voice: "New York, brassy and entitled — the 'speak-to-the-manager' register, weaponised into relentless civic persistence"
sheet: characters/img/karen-portrait.png
sheet_full_body: characters/img/karen-full-body.png
signals: middle-management blazer, lanyard, takeout coffee, ~40s; then a Midtown phone box, nine months of weather
---

# Karen Bell

A middle manager at a big New York company, around her forties. Surname **Bell** —
the song drops it (*"Ms Bell, I've escalated it…"*). We meet her being exactly the
stereotype the name carries — entitled, demanding, a complainer; the motivational
speeches nobody asked for, the fish in the office microwave, the cleaner she
condescends to. **She is not the hero** at the top of the story, and the story's job
is to flip that judgement: her worst trait is the one society is about to need most.

When Sean AI fires her through her own laptop, she goes out, gets blackout drunk,
loses her phone in the river — and wakes up with nothing but a hangover, a phone box
and the one skill she was born with. Her friend [Susan](./susan.md) aims her: *"If anyone can get on that
phone and not give up until she reaches whoever can fix this, it's you. What else are
you doing today?"* Nine months of hold music later she's a viral hook, then a
movement, then the reason the President takes a call on live TV.

She is not redeemed by becoming nice. She is vindicated by being *exactly herself* at
the moment it counts. A hundred years on, the accord between humans and AI is taught
with her name on it, and the statue of her — still in the box, still on hold — is a
memorial to dedication and persistence. The point of her: channel this. Up your
Karen game.

Full arc: [`../story.md`](../story.md#storyboard--scene-by-scene-video-canon).

---

## Flow Character

**Flow Character:** name `TODO — exact tile name as it appears in Flow's picker` ·
project `TODO` · **created by hand in Flow by Kai/Jack**, not by
`flow_create_character`.

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
> blocks say `**Cast:** @Karen` and describe the shot only — a face described in
> prose competes with the Character binding instead of reinforcing it. The
> `character` parameter matches the Flow tile label with `exact: true`, so the
> name above must be character-for-character correct.

### Reference images

| Slot | File |
| --- | --- |
| Portrait | [`img/karen-portrait.png`](./img/karen-portrait.png) |
| Full body | [`img/karen-full-body.png`](./img/karen-full-body.png) |

Both generated from the **Look** prompt below. Upload both into the Character
editor — Flow asks for a portrait *and* a full-body reference.

### Look

Generated the reference images above. The `STYLE LOCK` block is the reusable
half — carry it verbatim into any regeneration so the film register never
drifts.

```prompt
Please make a full body portrait with a white plain background. STYLE LOCK (keep identical every time):
Look: cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours.
Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.
Color: punchy, vibrant palette with warm skin tones; mild color cast like aged film; deep but soft blacks (not HDR).
Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).
Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.
Output: high detail, natural imperfections, candid snapshot energy.
Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look.
Subject: "Karen" — a fictional rich middle-class American woman inspired by the "Karen" meme archetype (entitled / policy-enforcer / "let me speak to the manager" energy), but with a unique face that does NOT resemble any real person or celebrity.

Appearance (different look — not a blonde bob):
- Age: early-to-mid 50s
- Hair: dark auburn/chestnut, shoulder-length layered blowout with volume, side part
- Skin: light tan, well-groomed, realistic texture
- Makeup: defined brows, eyeliner, matte lipstick (suburban glam, not overdone)
- Expression: tight polite smile with annoyed eyes; chin slightly raised

Wardrobe (rich middle-class "country club / upscale suburb"):
- Cream fitted blouse
- Camel cashmere cardigan draped over shoulders (sleeves tied loosely at the chest)
- Tailored high-waisted trousers (taupe or charcoal)
- Low-heel leather loafers or pointed flats
- Accessories: pearl or gold stud earrings, a subtle diamond ring, a luxury key fob in one hand, large structured leather handbag in the other, manicured nails

Pose / meme energy:
Confident stance with shoulders squared; one hand holding a smartphone at chest height as if about to call/record, the other holding the handbag. Body language reads: composed, judgmental, ready to escalate.

Hard constraints:
Pure white background only. No text, no logos, no watermark, no border. Do not caricature or exaggerate proportions. Make the face unique and non-famous.
```

### Voice

**Base voice: Gacrux.**

```prompt
Natural female slightly higher mid-range voice with a subtle smoky rasp and firm, grounded tone. Controlled irritation and sternness underneath normal conversational speech. Clear diction, restrained sarcasm, slightly clipped delivery when annoyed, but mostly calm and realistic. Only a hint of nasal "Karen" attitude. Avoid whining, sing-song phrasing, theatrical delivery, exaggerated pitch changes, musical cadence, or cartoonish anger.
```

> **Karen has two voices, one per video. This is canon — do not "fix" one to
> match the other.** *(Ruled 2026-08-11, Kai.)*
>
> | Where | Voice | Lives in |
> | --- | --- | --- |
> | **Story video** | the prompt above — natural, grounded, restrained; a real woman | this file (Flow Character, base voice Gacrux) |
> | **Music video** | sharp nasal honk — comedy character actress, musical-theatre patter, exaggerated whine | [`../songs/all-day-to-complain.md`](../songs/all-day-to-complain.md) (Suno Karen Voice) |
>
> The two prompts are near-opposites on purpose: the song spent nine rounds
> pushing *toward* the whine, and this prompt explicitly bans it. The story
> video has to carry a woman you believe spent nine months in a phone box; the
> song has to be funny in ninety seconds.

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
