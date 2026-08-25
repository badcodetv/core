---
story: karen
kind: record — prompts typed into Flow by hand, not a generation brief
flow_project: TODO — exact project name as it appears in Flow
updated: 2026-08-13
---

# Karen — Flow image prompt ledger

The exact image prompts used to make Karen's stills in **Google Flow**, kept
verbatim so any frame can be rebuilt or re-edited from the same words.

> ## 🖐 Record, not a licence to generate
>
> Karen's imagery is **Jack's, made by hand in Flow outside this repo**
> ([`README.md`](./README.md)). This file exists for the same reason the Flow
> Character ledgers in [`characters/`](./characters/) do — **so it is all
> together**, and so a lost asset can be reproduced from the exact prompt rather
> than reinvented. Do not generate new Karen imagery from these blocks, and do
> not "improve" the wording: they are a restore point.
>
> These are **image** prompts. Several of these stills are later turned into
> video; the video prompts are a separate step and are not recorded here yet.
>
> Nothing here goes through
> `.claude/skills/badcode-art-direction/SKILL.md`. Karen deliberately sits
> outside the global BadCode register — see §1.

---

## 1. The STYLE LOCK

Karen's look is a **capture emulation, not a period setting**: super-8 / Polaroid
texture over a world that is unambiguously present-day. That split is the whole
trick, and it is why every block below spends a paragraph insisting on it — the
model will happily give you 1974 if you let it.

This is the canonical block. It is pasted at the **top of every scene prompt**,
character-for-character identical, before any scene description:

```prompt
STYLE LOCK (keep identical every time):

Capture look only (NOT time period): cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day.

Present-day constraint: modern clothing, modern vehicles, modern architecture, contemporary street design and signage; no retro/period props or era-specific styling.

Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.

Color: punchy, vibrant palette with warm skin tones; mild film-like color cast; deep but soft blacks (not HDR).

Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).

Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.

Output: high detail, natural imperfections, candid snapshot energy.

Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look, no historical setting/era shift.
```

The same lock also appears in [`characters/karen.md`](./characters/karen.md) and
[`characters/aarron.md`](./characters/aarron.md) as the register their Character
reference images were shot in. **Susan's references are not in it** — that
divergence is flagged in [`characters/susan.md`](./characters/susan.md) and is
still owed a ruling.

### Standing rules visible across every prompt

- **No legible text, anywhere.** Not on signs, ads, subway maps, storefronts,
  billboards, plates, screens or clothing. Blank it or blur it past legibility.
  The one deliberate exception is the show title graphic in §2.4, which is
  scoped to the TV screen only.
- **No logos, no watermarks.**
- **Present-day or it's a reject.** An era shift is the failure mode this look
  invites; every prompt names it twice.
- **Characters are named "(fictional)"** inline — `Karen (fictional)`,
  `Ari (fictional)` — to keep the likeness request clear of a real-person read.
- Prompts are signed off with a *"Thanks."* — Jack's habit, preserved verbatim.

> **Naming drift:** the §2.2 prompt says **Ari**, which was the character's name
> when it was fired. He is **Aarron** in canon as of 2026-08-11
> ([`characters/aarron.md`](./characters/aarron.md)); *Ari at Home* survives as
> the real-life reference, not the character name. The prompt is left exactly as
> typed — if it is ever re-fired, use `@Aarron` / the current Flow Character tile.

---

## 1b. The ILLUSTRATED REGISTER — Karen's second style lock

**Added 2026-08-12** from six reference frames Kai supplied (video stills in which
the picture transitions *out of* the super-8 register in §1 and *into* this one).
This is a **second register, not a replacement**: §1 is the live-action-feel
capture emulation, this is the graphic register the films cut to. Both are Karen.

### What the reference frames establish

- **Two-family palette, no third.** Deep desaturated navy / slate-blue / near-black
  carries every unlit mass; amber, ochre and sodium-orange carry every lit surface.
  One saturated accent (a taxi yellow) is the only colour allowed to escape.
- **Flat geometric planes.** Buildings are plain extruded blocks; windows are
  punched rectangles of warm light. No surface detail below the level of a large
  flat shape.
- **Hard-edged light.** Light arrives as pools and shafts with crisp borders;
  shadows fall as clean geometric wedges, never soft gradients.
- **Matte painted texture.** Visible canvas tooth and fine grain — it reads as a
  photographed painted board, not clean vector.
- **Figures as near-silhouettes.** Hair is one flat mass, clothing is flat shapes,
  and **facial features are implied by shadow rather than drawn.** In the closest
  reference the face carries no features at all.
- **Depth by stacked value**, layers reading like separate cut-out cards.
- **Cinematic widescreen, strong central framing**, generous negative space, and
  hard scale contrast between a small figure and a large architectural mass.

Lineage: mid-century modern poster illustration / UPA-era animation, Saul Bass
title-card geometry, Hopper's light logic.

### The load-bearing split (same trick as §1)

**Mid-century graphic *style*, present-day *world*.** Exactly the trap §1 names:
the model will hand you 1958 if you let it. The register is a drawing convention,
not a period setting — modern clothing, modern vehicles, modern signage.

### Consequence for casting — this register overrides the casting rule

[`characters/karen.md`](./characters/karen.md) forbids describing a face in prose
because it competes with the Flow Character binding. **That rule is scoped to the
photoreal register and does not apply here.** In this style the face carries no
features, so likeness cannot live in it — it lives in **hair mass, silhouette,
wardrobe and posture**. Casting a photoreal Character into a flat graphic frame
pulls the render back toward photorealism, which is the failure mode.

So: in the illustrated register, **describe the likeness in prose and do not cast
`@Karen`.** Owed a ruling from Kai/Jack if they disagree.

### The block

```prompt
STYLE LOCK — ILLUSTRATED REGISTER (keep identical every time):

Style: flat graphic illustration in a mid-century modern poster register, painted in matte gouache on board, with visible canvas tooth and fine even grain as though the finished board were photographed.

Present-day constraint: the drawing convention is mid-century, the depicted world is contemporary — modern clothing, modern vehicles, modern architecture and signage. Style only, never period.

Palette: restrict to two families. Deep desaturated navy, slate-blue and near-black charcoal carry every unlit surface; warm amber, ochre and sodium-orange carry every lit surface. Permit one saturated accent colour and keep it rare.

Form: reduce everything to flat geometric planes — rectangles, trapezoids, wedges. Architecture becomes plain extruded blocks; windows become punched rectangles of warm light; keep surface detail at the scale of large flat shapes.

Light: one motivated source, emitted as hard-edged pools and shafts, with shadows falling as clean flat geometric wedges with crisp borders.

Figures: elegant, slightly elongated, reading close to silhouette. Hair is a single flat mass; clothing is flat shapes; imply facial features with shadow and leave them undrawn.

Depth: stack flat planes of stepped value so the layers read as separate cut-out cards.

Composition: cinematic widescreen, strong central framing, generous negative space, hard scale contrast between a small figure and a large architectural mass.

Surface: clean edges carrying a slight painterly imperfection; calm, graphic and still.

Keep the frame free of lettering, signage copy, logos and watermarks.
```


## 2. Scene prompts

Scene numbers map to the storyboard in
[`story.md`](./story.md#storyboard--scene-by-scene-video-canon).

### 2.1 The subway two-shot — §3.2 *The train*

The two riders playing the actual Karen tune in-world. Note the negative on
phones and earphones: the joke needs them *talking*, and a visible phone drags
the shot toward the Aarron cameo it must not resemble.

```prompt
STYLE LOCK (keep identical every time):

Capture look only (NOT time period): cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day.

Present-day constraint: modern clothing, modern vehicles, modern architecture, contemporary street design and signage; no retro/period props or era-specific styling.

Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.

Color: punchy, vibrant palette with warm skin tones; mild film-like color cast; deep but soft blacks (not HDR).

Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).

Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.

Output: high detail, natural imperfections, candid snapshot energy.

Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look, no historical setting/era shift.

CREATE A NEW IMAGE. Present-day New York City subway car interior.
Medium-wide two-subject shot, 35mm lens, eye-level, camera positioned directly facing a bench seat across the aisle. Frame both seated passengers centered in the composition with a little headroom, showing their upper bodies and knees, plus the surrounding subway details (bench seat, metal pole at far left edge, window to the right, a subway route map panel behind them). Background outside the window is motion-blurred like the train is moving.
Two people sit side-by-side on the bench, turned slightly toward each other, mid-conversation, smiling naturally. One wears casual streetwear (e.g., denim jacket over a graphic tee), the other wears smarter clothing (e.g., blazer or suit jacket), relaxed posture, friendly vibe.
Hard rules / negatives:

No phone, no earphones, no microphones, no filming gear, no text readable anywhere (ads/map text unreadable), no logos, no watermark, no posed stock-photo look. Thanks.
```

### 2.2 The phone box and the growing crowd — §3.3 *The crowd*

The street-canyon wide: Karen in the box, Ari/Aarron performing on the pavement
outside with his wearable rig, and the crowd forming around them. Ari and the
crowd are explicitly the **main action**, with Karen readable through the glass —
this is the frame where the story stops being hers alone.

Reference-anchored: *"use the reference images for the setting and characters
appearances"* — the box location is a fixed point across every Act 2/3
generation ([`story.md`](./story.md), Act 2 rules).

```prompt
Please use the reference images for the setting and characters appearances. STYLE LOCK (keep identical every time):

Capture look only (NOT time period): cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day.

Present-day constraint: modern clothing, modern vehicles, modern architecture, contemporary street design and signage; no retro/period props or era-specific styling.

Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.

Color: punchy, vibrant palette with warm skin tones; mild film-like color cast; deep but soft blacks (not HDR).

Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).

Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.

Output: high detail, natural imperfections, candid snapshot energy.

Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look, no historical setting/era shift.

Now generate: Wide street-level shot, 28mm lens, eye-level camera looking down a busy New York City "street canyon" toward an intersection. Wet pavement reflects the warm sky and traffic lights; cars and taxis pass in the roadway; pedestrians move along both sidewalks.
On the right side of frame near the curb is a grey aluminum-and-glass phone booth. Karen (fictional) is inside the booth, sitting on a small stool and talking into the handset mid-call, one free hand gesturing.
Just outside the booth, Ari (fictional) is set up with his wearable music rig and is actively making music: large over-ear headphones on, harness/backpack rig visible, compact keyboard mounted to the front at waist height, hands on the keys, and the rig-mounted microphone visible on his chest/shoulder. Ari faces slightly toward the street, performing.
A small crowd is forming around them on the sidewalk: a loose semicircle of onlookers at varying distances, some stopping mid-walk, some watching curiously, a couple holding phones up but no readable screens, and a few people passing behind the crowd. Keep Karen and the booth clearly readable through the glass, but make Ari and the growing crowd the main street-side action.
Hard constraints: no text anywhere (no readable street signs, storefront signs, posters, billboards, license plates, phone booth labels, screen UI, or lettering on clothing). If any text would normally appear, make it blank or blur beyond legibility. No logos. No watermarks. 16:9 landscape. Thanks.
```

### 2.3 The production office, edited — §4.1 *The TV studio*

**This one is an edit, not a generation.** It takes an existing production-office
still and changes exactly two things: the left man walks out of frame, the right
man takes a call. Everything else — angle, room, lighting, whiteboard, monitor,
road cases, background crew — is pinned. That is the pattern worth copying: an
edit prompt is a **short delta with a long do-not-change list**, not a re-write
of the scene.

```prompt
Please use the reference image for the setting and characters appearances. STYLE LOCK (keep identical every time):

Capture look only (NOT time period): cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day.

Present-day constraint: modern clothing, modern vehicles, modern architecture, contemporary street design and signage; no retro/period props or era-specific styling.

Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.

Color: punchy, vibrant palette with warm skin tones; mild film-like color cast; deep but soft blacks (not HDR).

Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).

Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.

Output: high detail, natural imperfections, candid snapshot energy.

Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look, no historical setting/era shift.

IMAGE EDIT — use the uploaded reference image as the base. This is NOT a new scene.

Keep the same camera angle, framing, perspective, room layout, lighting, color, and all background details (whiteboard, wall-mounted monitor, road cases, cables on floor, doorway/corridor, background crew).
CHANGE ONLY THESE THINGS:

The man on the left is now walking away from the conversation, moving toward the left edge of frame (mid-step, body turned away, slightly motion-blurred like he's leaving). Keep his clothing and identity the same.
The man on the right is now on a phone call: he holds a smartphone to his ear, focused expression, slightly tense/urgent. His other hand can be half-raised as if emphasizing a point. Keep his clothing and identity the same.
Adjust their poses naturally so it looks like the left man has just left and the right man has immediately taken a call.
DO NOT CHANGE:

Do not change either man's face/identity, age, hair, or clothing style.
Do not change the background people, doorway, monitor, equipment cases, cables, whiteboard, or any objects.
No new objects besides the phone in the right man's hand.
No text, no logos, no watermark. The monitor remains blurred/unreadable. Thanks.
```

### 2.4 The late-night set — §4.2 *The show*

Three references, each scoped to one job: **1** the set and camera language,
**2** the guest's face, **3** the host's face. Splitting references by role like
this is what stops a multi-reference generation from blending everyone into one
person.

The **fictional show title — "Late Night with Ted Connors" — is the single
sanctioned piece of legible text in the whole story**, and it is confined to the
rolling TV screen. Everything else stays text-free.

Note this block departs from the standard STYLE LOCK ordering: the scene is
specified first as straight photoreal broadcast realism, and the film emulation
is applied at the end as a *finish*. The lock is also compressed to one
paragraph rather than the full eight-line version.

```prompt
Create a photorealistic present-day late-night talk show publicity still in 16:9.

Reference mapping:
- Use reference image 1 for the full studio setting, composition, camera distance, desk placement, guest chair placement, arched skyline window, standing microphone, rolling TV placement, lighting direction, and overall premium late-night talk show atmosphere.
- Use reference image 2 for the older male guest's appearance only.
- Use reference image 3 for the younger male host's appearance only.

Scene:
A warm, polished late-night talk show set. The younger male host is seated behind his desk, turned slightly toward the guest, smiling and speaking mid-conversation. The older male guest is seated in the guest chair to the left of the desk, angled toward the host, listening and responding in a friendly, relaxed way. Both men should feel natural, engaged, and comfortable, as if the conversation is already underway. Their expressions should be open, warm, and conversational, not posed.

Host:
Use reference image 3 for the host's face, age range, hair, build, and overall appearance.
He is a handsome younger adult male with neat dark hair, clean-shaven face, tailored dark suit, white shirt, dark tie, polished late-night presenter grooming, friendly and confident on-camera presence.

Guest:
Use reference image 2 for the guest's face, age range, hair, build, and overall appearance.
He is an older adult male with short white hair, clean-shaven face, fair skin, light eyes, dark navy suit, white shirt, light blue tie, calm and distinguished presence.

Set details:
- warm wood-paneled walls
- arched curtain-framed city skyline window
- host desk
- guest chair
- overhead studio lighting rigs
- standing microphone
- large rolling TV screen visible on set
- upscale broadcast studio feel
- same 16:9 framing language as reference image 1

TV screen:
On the large TV screen only, display a tasteful fictional late-night show title graphic reading:
"Late Night with Ted Connors"
The title should look like a polished, premium, generic late-night talk show graphic. Clean, readable, elegant, and naturally integrated on the TV only.

Image requirements:
- photorealistic real-world photography
- present-day setting only
- one host and one guest only
- both identities consistent with their respective reference images
- realistic skin, hands, eyes, teeth, and body proportions
- crisp focus on both men
- no exaggerated expressions
- mid-conversation energy, friendly and believable

Lighting and finish:
Soft professional studio lighting, realistic broadcast exposure, warm wood tones, flattering skin tones, premium publicity-photo realism, high detail, natural imperfections.

STYLE LOCK:
Apply only a present-day film-emulation finish: cinestyle 800+, subtle grain, faint dust specks, gentle halation around highlights, mild vignette, slightly soft edges, vibrant but believable color, warm skin tones, deep but soft blacks, no HDR, no retro props, no era shift.

Hard negatives:
- no extra people
- no audience visible
- no duplicate host
- no duplicate guest
- no standing poses
- no waving
- no scene drift away from the late-night set
- no wardrobe changes
- no distorted faces
- no distorted hands
- no extra text outside the TV screen
- no watermark
- no logos other than the fictional TV title graphic. Thanks.
```

### 2.5 The pinned Manhattan map — Act 2, *the zoom-map escalation*

The **corkboard fallback** for the escalation formula. The storyboard's first
choice is photoreal aerial Manhattan; the pin-map "stays in the back pocket if it
doesn't land" ([`story.md`](./story.md), Act 2 formula, and *Open details*).
This prompt is that back pocket, now realised.

Two things carry it: the real map is a **supplied reference whose geography must
survive intact**, and every printed label is stripped so the roads and coastline
read as pure shape. The stripped-back framing is deliberate — *just* the map and
five pins, with the mug/lamp/desk investigative-office clutter explicitly banned.

```prompt
Use the uploaded Manhattan map as the actual reference image and keep its real geography, street layout, coastline, parks, and neighborhood structure exactly intact. Create a realistic photographic image of that exact map pinned to a wall or board in a landscape composition. The map itself is rotated and presented horizontally, filling almost the entire wide frame. Add five colored push pins in meaningful locations across Manhattan. Remove all printed text and labels from the map so there are no street names, no neighborhood names, no borough names, no park labels, no numbers, and no other text anywhere on the map. Keep the roads, blocks, coastlines, parks, and overall cartographic structure visible and realistic, but text-free. The image should feel like a real investigative office map: slightly worn paper, natural pin holes, flat pinned surface, warm practical indoor light, realistic texture, believable photographed angle. Keep it present-day and realistic. Only borrow the visual treatment from the earlier map image: pinned paper map, warm indoor lighting, candid photographic realism, subtle investigative-office mood. Do not add a desk, mug, phone, lamp, nameplate, papers, or any other objects. The image should be just the real Manhattan map with pins. STYLE LOCK: cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day. Visible film grain, slight gate-weave feel, occasional dust/specks, gentle halation around highlights, punchy vibrant palette, mild film-like color cast, deep but soft blacks, slightly soft edges, mild vignette, shallow-to-moderate depth of field, preserve detail, high detail, natural imperfections, candid snapshot energy. No added text, no logos, no watermark, no AI hyper-sharp HDR look, no era shift, no border. Thanks.
```

---

### 2.6 Karen at the jazz club bar — illustrated register `[fired · accepted]`

**Fired 2026-08-12 on Nano Banana 2 in Flow. Accepted first time, unmodified.**
The first prompt in the
[§1b illustrated register](#1b-the-illustrated-register--karens-second-style-lock),
and the frame every later shot in this register is style-referenced against.
Kai's verdict: *"it is what i wanted."*

Built on the six-slot structure Google's own prompt guide teaches — subject,
action, environment, style, lighting, details
([`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md)) — and
phrased positively throughout, because the guide is explicit that these models
handle "keep the frame clean" better than "no clutter".

**Likeness carries in the silhouette, not the face** — see §1b. Do **not** cast
`@Karen`; the photoreal Character binding fights the flat register.

**Flow settings:** landscape, 21:9 if the picker offers it, 4 candidates. Try it
on both Nano Banana 2 and Nano Banana Pro and compare the matte texture — NB2 is
reported to run sharper and more contrasted, which this register may not want.

```prompt
STYLE LOCK — ILLUSTRATED REGISTER (keep identical every time):

Style: flat graphic illustration in a mid-century modern poster register, painted in matte gouache on board, with visible canvas tooth and fine even grain as though the finished board were photographed.

Present-day constraint: the drawing convention is mid-century, the depicted world is contemporary — modern clothing, modern vehicles, modern architecture and signage. Style only, never period.

Palette: restrict to two families. Deep desaturated navy, slate-blue and near-black charcoal carry every unlit surface; warm amber, ochre and sodium-orange carry every lit surface. Permit one saturated accent colour and keep it rare.

Form: reduce everything to flat geometric planes — rectangles, trapezoids, wedges. Architecture becomes plain extruded blocks; windows become punched rectangles of warm light; keep surface detail at the scale of large flat shapes.

Light: one motivated source, emitted as hard-edged pools and shafts, with shadows falling as clean flat geometric wedges with crisp borders.

Figures: elegant, slightly elongated, reading close to silhouette. Hair is a single flat mass; clothing is flat shapes; imply facial features with shadow and leave them undrawn.

Depth: stack flat planes of stepped value so the layers read as separate cut-out cards.

Composition: cinematic widescreen, strong central framing, generous negative space, hard scale contrast between a small figure and a large architectural mass.

Surface: clean edges carrying a slight painterly imperfection; calm, graphic and still.

Keep the frame free of lettering, signage copy, logos and watermarks.

SCENE:

Subject: Karen (fictional), a woman in her early fifties, alone at the end of a long bar in a basement jazz club. Her likeness reads entirely through silhouette: shoulder-length auburn hair with volume and a side part, drawn as one flat chestnut mass catching a thin amber rim along the top; a camel cashmere cardigan draped over the shoulders of a cream blouse; tailored charcoal high-waisted trousers; a structured leather handbag set on the stool beside her. Leave her face in shadow with the features undrawn.

Action: she sits side-on to the camera on a low bar stool, one forearm resting along the bar top, the other hand holding a stemmed glass at chest height, chin slightly raised and turned a few degrees away from the room. Her posture is composed, self-possessed and faintly impatient — a woman entirely willing to wait, who fully expects someone to come and sort it out.

Environment: a small low-ceilinged basement jazz club at night. A long dark wood bar runs from the lower foreground into the middle distance; behind it the back-bar reduces to a flat grid of small amber rectangles standing in for bottles; three empty stools sit between her and the frame edge; a shallow stage in the deep background holds three flat black musician silhouettes — an upright bass, the raised lid of a piano, and a horn player — placed small against the far wall.

Art style: exactly the STYLE LOCK above.

Lighting: a single warm pendant lamp hanging low over the bar is the only source in the room. It pools amber light across the bar top and over Karen's shoulders and hair, and throws one hard-edged wedge of light across the floor toward the camera. Everything outside that pool settles into deep navy and near-black. A second much smaller cone of ochre picks out the stage at the back.

Details: a flat translucent band of smoke haze lies across the lamp light; the polished bar top carries one long warm reflection running toward the foreground; a lowball glass and a folded napkin rest near her hand; the floor is a large uninterrupted plane of dark slate; keep the whole frame calm, graphic and still.

Compose for a 21:9 cinematic widescreen frame. Thanks.
```

---

## 2a. The title-sequence plates — illustrated register

Four stills fired on **Nano Banana 2 in Flow, 2026-08-12, all accepted**. They are
the plates for a James Bond–style title sequence built out of Karen's story: the
cord, the grid, the booth and the walk.

> **A second wave of plates for this same sequence — ten more, unfired — is in
> [§2c](#2c-the-second-wave-of-title-sequence-plates--illustrated-register-not-yet-fired),
> along with the research that changed the recipe.**

> ### How to reconstruct any of these
>
> Each prompt as typed is **three parts in this order**:
>
> 1. the **§1b ILLUSTRATED REGISTER block**, pasted verbatim;
> 2. the **relationship instruction** below;
> 3. the **scene block** recorded under each heading.
>
> The lock is not repeated five times here — it lives in
> [§1b](#the-block) and is character-for-character identical in every one.
>
> **The §2.6 jazz club frame is attached as a style reference on every one of
> these generations.** That attachment is load-bearing: it is what holds the
> palette and flatness across a series. The relationship instruction that
> accompanies it, verbatim:
>
> ```prompt
> Use the attached image as the style reference: match its palette, flatness, hard-edged light and matte painted texture exactly. Not photorealistic.
> ```
>
> Both moves are vendor-documented — an attached image carries "artistic style,
> colour palette and visual treatment" onto new content, and the lock is repeated
> anyway because style drifts the moment you stop describing what stays. See
> [`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md).

### 2a.1 The cord spiral — title-sequence plate, morph start frame

Karen's signature motif. Bass emerged the *Vertigo* spiral from a pupil; hers
comes from a phone cord — the loop, the hold, the nine months. Composed dead
centre so it match-cuts to §2a.2.

```prompt
SCENE:
Subject: a coiled black telephone handset cord seen from directly overhead, filling the frame.
Action: static, wound into a tight flat spiral at the exact centre, the cord running out from the coil toward the lower frame edge.
Environment: lying on a flat, uninterrupted deep-navy surface.
Lighting: one warm amber source from upper left, throwing a hard-edged wedge across the surface; each coil catches a thin amber rim along its upper curve.
Details: place the spiral's centre precisely at the centre of frame, radially balanced, with a small faint amber mark on the surface at that centre point; keep generous empty navy around the coil.
Compose for a 16:9 frame.
```

### 2a.2 The aerial grid — title-sequence plate, morph end frame

The *North by Northwest* device: geometry that resolves into a city. The
crossroads lands on the same pixel as the spiral's eye, so the two cut together
as a morph without any interpolation.

```prompt
SCENE:
Subject: a dense city street grid seen from directly overhead.
Action: static, with a few small amber vehicle shapes spaced along the streets.
Environment: flat navy building blocks separated by wide amber streets running to every frame edge.
Lighting: a low sun from upper left, each block throwing a long hard-edged navy shadow across the amber street beside it.
Details: place one crossroads precisely at the centre of frame, slightly wider and brighter than the others, with the surrounding blocks radially balanced around it.
Compose for a 16:9 frame.
```

### 2a.3 The booth — title-sequence plate, gun-barrel iris

The Bond gun barrel, rebuilt as her phone box. **Generated as a plate, not as an
iris** — the circular reveal is a mask in the edit, which is free, exact and
repeatable. The prompt's only job is to leave enough empty navy for the circle to
open into.

```prompt
SCENE:
Subject: a glass phone booth glowing warm amber, standing alone on a night street, seen from across the road.
Action: a single seated-height silhouette stands inside with her back to camera, one flat chestnut mass of shoulder-length hair catching a thin amber rim, features undrawn.
Environment: flat navy building slabs receding on both sides, wet dark pavement in the foreground.
Lighting: the booth's interior light is the only source in the frame; it throws one hard-edged wedge of amber across the wet pavement toward camera.
Details: rain falls as thin pale diagonal streaks; keep the booth small and dead centre with large areas of empty navy on all sides.
Compose for a 16:9 frame.
```

### 2a.4 The ankle-height walk — title-sequence plate

The safest shot in the set and the best-looking: no face, no hands, and walking is
the one motion these video models handle reliably.

⚠️ **Palette drift — the odd one out.** This frame came back **warmer and more
saturated** than the other three, which are navy-dominant. It will show if the four
cut together. Either grade it back toward navy in post or re-fire with the palette
clause tightened. Unresolved.

```prompt
SCENE:
Subject: a woman's lower legs and shoes, seen from an extreme low angle at pavement level.
Action: mid-stride, crossing the frame from left to right.
Environment: flat amber pavement slabs below, navy building slabs rising steeply above and converging toward the top of frame, pale crosswalk bars running across the ground.
Lighting: a low warm source behind her throwing one long hard-edged shadow stretching toward camera along the pavement.
Details: charcoal trousers and dark low-heel shoes rendered as flat shapes; keep the framing below waist height so no hands or face enter the frame.
Compose for a 16:9 frame.
```

---

## 2b. Video prompts — Gemini Omni Flash `[not yet fired]`

**Written 2026-08-12. Briefs, not records** — replace each with what was actually
typed once they have been run. These animate the §2a plates.

**Model: Gemini Omni Flash, in Flow.** Kai's call, made after the trade-offs were
put on the table. Omni is already the default model in a fresh Flow project, so
nothing needs switching — but confirm it, because
[`docs/superpowers/flow-video.md`](../../superpowers/flow-video.md) drives the
*Veo* path and re-selects Veo 3.1 Quality every session.

Path: upload the still → hover the tile → `⋮ More` → **Animate** (attaches it as
the source frame) → paste the prompt → Create → approve the credit gate.
**30 credits per 10s clip**, back in 1–2 minutes, **720p native** with a 4K upscale
on download. Poll for completion — a queued clip looks like a failure, while a real
failure reads *"Oops, something went wrong!"* and re-posts the approve gate.

### Why these are shaped the way they are

Every clause is doing a job, and the shape is **not** the shape of a Veo prompt.
Full reasoning in
[`docs/google-flow/omni-flash.md`](../../google-flow/omni-flash.md); the short
version:

- **Open by locking the shot.** Duration, aspect and *oner* in the first sentence
  holds them more reliably than any setting. **Omni defaults to cutting** — left
  alone it builds a short narrative from several shots, which would wreck a slow
  push.
- **`Use the given image as the starting frame.`** This exact phrasing engages
  first-frame behaviour. Omni's default is to treat a still as a loose reference
  and redesign from it; the reports of "no true first-frame-to-video" appear to
  describe that default rather than a hard limit.
- **One main action per clip**, resolving inside 10s — there is no extension or
  interpolation to lean on.
- **`Keep … exactly the same`** is mandatory, not decorative. Without naming what
  to preserve, Omni re-styles the whole scene when asked to change one element.
- **Name the audio.** Omni generates sound regardless; unprompted it picks its own.
- **Short and plain.** Google's own guide says the model does not want overly
  prescriptive instructions. Veo-style constraint stacks cost quality here.
- **Nothing asks for faces, hands, on-screen text or instrument-playing** — all
  four are documented artefact sources.

### 2b.1 The cord spiral

`dolly zoom` is in Google's official camera vocabulary; on a spiral it is literally
the *Vertigo* effect. Swap it for `push in` if the plain move reads flat.

```prompt
Create a 10-second 16:9 noir title-sequence video as one continuous oner. Use the given image as the starting frame. Slow push in toward the centre of the coil while it rotates gently clockwise, the amber light wedge holding steady across it. Keep the flat illustrated style, the navy-and-amber palette and the hard-edged light exactly the same. Slow upright bass and brushed drums, no dialogue.
```

### 2b.2 The aerial grid

```prompt
Create a 10-second 16:9 noir title-sequence video as one continuous oner. Use the given image as the starting frame. The camera pulls slowly straight up, revealing more of the grid, while the small cars crawl steadily along the amber streets. Keep the flat illustrated style, the navy-and-amber palette, the hard-edged shadows and the overhead angle exactly the same. Slow smoky jazz, no dialogue.
```

### 2b.3 The booth

```prompt
Create a 10-second 16:9 noir title-sequence video as one continuous oner. Use the given image as the starting frame. Slow push in toward the phone booth as the rain keeps falling; the woman inside stays with her back to camera and shifts her weight slightly. Keep the flat illustrated style, the navy-and-amber palette, the amber light wedge on the wet ground and her undrawn face exactly the same. Rain and distant traffic under slow smoky jazz, no dialogue.
```

### 2b.4 The ankle-height walk — fire this one first

```prompt
Create a 10-second 16:9 noir title-sequence video as one continuous oner. Use the given image as the starting frame. Low tracking shot moving alongside her at ground level as she keeps walking steadily across the crossing, her hard-edged shadow sweeping with her. Keep the flat illustrated style, the warm amber ground, the navy slabs above and the framing below waist height exactly the same. Footsteps and slow smoky jazz, no dialogue.
```

### 2b.5 The spiral→grid morph — experiment only

**Do the morph in the edit, not in the model.** §2a.1 and §2a.2 share a centre
point, so a hard cut on a beat does it for free — and a cut with no easing is more
Bass than any dissolve. This block is a 30-credit experiment on the chance Omni's
transformation ability (its actual specialty) beats the cut.

```prompt
Create a 10-second 16:9 noir title-sequence video as one continuous oner. Use the given image as the starting frame. The coil rotates slowly and transforms into an overhead city grid of navy blocks and amber streets, the centre of the coil becoming a crossroads. Keep the flat illustrated style and the navy-and-amber palette exactly the same throughout. Slow smoky jazz, no dialogue.
```

### Refining

**One variable per turn** — `"Slower push in. Keep everything else the same."`
Over-detailed edit instructions trigger changes you did not ask for.

---

## 2c. The second wave of title-sequence plates — illustrated register `[8 of 10 fired · accepted]`

**Written and fired 2026-08-12.** Ten plates extending the
[§2a](#2a-the-title-sequence-plates--illustrated-register) Bond sequence — six
scenes and a four-shot match-cut chain.

> ### What came back
>
> **Eight fired on Nano Banana 2 in Flow, 2026-08-12, all accepted** — 2c.1, 2c.2
> (**two takes**), 2c.3, 2c.4, 2c.5, 2c.6, 2c.8, 2c.10. **2c.7 (the earpiece grill)
> and 2c.9 (the manhole) were not run** — status unknown, not known to have failed.
>
> Clip prompts for the eight accepted plates are in
> [§2d](#2d-clip-prompts-for-the-2c-plates--gemini-omni-flash-not-yet-fired).
>
> **Three things worth recording:**
>
> - **The series clause appears to have worked.** The palette held across eight
>   independent generations with no repeat of the §2a.4 drift. The two 2c.2 takes
>   differ markedly in warmth — one navy-dominant, one pushed to saturated
>   amber — but those are **two takes of one plate**, not drift across the set.
>   Both are keepers and they do different jobs; see §2d.4 and §2d.7.
> - **2c.1 came back as a three-by-three grid, not three-by-four.** The prompt asked
>   for twelve keys and got nine. Harmless — the meaning lives in the position, and
>   top-right still reads as the three — but it is a real divergence from the words.
> - **The single-accent spine emerged on its own.** Red turns up on the standing
>   statue's handset (2c.4), as one bubble among the grey in the river (2c.6), and as
>   the auburn hair mass seen from above (2c.10). Nobody prompted it. That is the
>   accent rule proposing itself, and it is worth adopting deliberately rather than
>   letting the next batch spend it elsewhere.

Each borrows a specific title-sequence device and rebuilds it out of Karen's own
material: Binder's dots and silhouette line-ups, Brownjohn's projections,
*GoldenEye*'s toppling statues, *Casino Royale*'s falling card suits, Bass's
refusal to let one shape leave the frame.

### What the research changed

Checked 2026-08-12 against Google's own guide and the current crop of NB2
playbooks; engine-level findings are filed in
[`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md). Six
things move the recipe from §2a:

1. **A style reference does not carry style.** The strongest finding, and it is
   counter-intuitive: a reference image anchors *identity and content*, and the
   model **will not assume the new image matches the reference's style unless the
   prompt says so**. The §2a instinct to paste the full lock *and* attach the jazz
   club frame was right — it is not belt-and-braces, it is the only thing holding
   the register. Do not drop the lock because a reference is attached.
2. **Name the use case.** Telling the model what the image is *for* measurably
   improves it — the guides put it as the model making "a thousand small
   decisions" off that context. Every block below now opens by declaring itself a
   title-sequence plate. New since §2a.
3. **Say where it sits in the series.** The recommended phrasing is explicit —
   *"this is panel 3 of a 6-panel sequence, maintain visual identity with panels 1
   and 2"*. Cheap, and aimed exactly at the §2a.4 drift problem.
4. **Negatives work here, but keep them short.** Google's house rule is positive
   framing only ("empty street", never "no cars") — but `Not photorealistic`
   appears in Google's own illustration examples, and NB2 is reported to follow
   targeted negations more reliably than its predecessors. The resolution we are
   adopting: **negate the style family, describe everything else positively**, and
   keep the negative tail to a clause, not a list. Long exclusion stacks dilute.
   This is why the eight-line exclusion block from the §1 super-8 lock is **not**
   imported into this register.
5. **Two regenerations, then rewrite.** If the same prompt misses twice, rewriting
   beats rolling again. Worth adopting as a standing rule for the whole ledger.
6. **Keyframes → video is the vendor's own recommended path** — generate the plate
   in Nano Banana, animate it in the video model. [§2b](#2b-video-prompts--gemini-omni-flash-not-yet-fired)
   is doing the endorsed thing.

**Two things to test, not adopt:**

- **Hex-pinned palette.** NB2 reportedly understands hex codes, though less
  reliably than Nano Banana Pro. Appending an explicit pin — e.g.
  `Unlit surfaces #1B2A41 · lit surfaces #E39A2C` — is the most direct candidate
  fix for the §2a.4 warmth drift. **Do not edit the canonical lock to add it**:
  the lock is character-for-character fixed. Run it as an appended clause on one
  plate and compare.
- **Lock-first ordering.** The playbooks say lead with the subject inside the
  first fifteen words, which the lock-first structure plainly violates. But §2.6
  was accepted first time as-is, so this is not being changed on paper. If a plate
  below comes back drifting toward photoreal, **moving the lock below the scene
  block is the first thing to try.**

> ### How to fire any of these
>
> Same three parts in the same order as §2a — (1) the **§1b ILLUSTRATED REGISTER
> block** verbatim, (2) the **relationship instruction**, (3) the **scene block**
> below. The lock is not repeated ten times; it lives in [§1b](#the-block).
>
> **Attach the §2.6 jazz club frame as the style reference on every one.** The
> relationship instruction gains a series clause and a use-case clause over the
> §2a version:
>
> ```prompt
> Use the attached image as the style reference: match its palette, flatness, hard-edged light and matte painted texture exactly. Not photorealistic.
>
> This image is one plate in a series of frames for a noir film title sequence. Maintain visual identity with the attached plate across the whole set.
> ```
>
> **Flow settings:** landscape, 16:9, 4 candidates, Nano Banana 2. Every block
> below closes by restating the ratio in prose, which the guides recommend doing
> even when the UI already sets it.
>
> **All ten are face-free, hand-free, text-free and single-action** — the four
> documented artefact sources. That is deliberate, not incidental.

### 2c.1 The keypad — Binder's dots, rebuilt

*Dr. No* opened on nothing but bouncing coloured dots. The song opens on
*"touch-tone beeps locked to the beat, the only percussion"* and a menu that ends
on **three**. The plate is the end state of that menu; the 1 → 2 → 3 light-up is
the video move.

The no-text rule does real work here: the keys are blank, so **position carries
the meaning**. Top-right of the top row is the three.

```prompt
SCENE:
Subject: a payphone keypad seen from directly overhead, filling the frame — twelve rounded square keys in a three-by-four grid, set into a flat navy steel faceplate.
Action: static, with the top-left and top-middle keys glowing a dim ochre and the top-right key burning a full bright amber, markedly brighter than anything else in the frame.
Environment: the faceplate fills the whole frame and runs out past every edge, each key sitting in a shallow inset that reads as one crisp flat shadow.
Art style: exactly the STYLE LOCK above.
Lighting: the keys are the only light source; the brightest key throws a hard-edged square of amber spill onto the faceplate immediately around it.
Details: keep every key face completely blank and unmarked; keep the faceplate a single uninterrupted flat navy plane carrying fine canvas tooth; keep the grid square to frame and evenly spaced.
Compose for a 16:9 frame.
```

### 2c.2 There is always a level above the level

The best line in the song had no picture. This is it: the light well of an office
tower from the very bottom, looking straight up, storeys repeating toward an
opening you never reach. The same escalation device as the canon zoom-map, turned
through ninety degrees.

**The ambitious one — give it the most candidates.** The endless-stack rhythm is
the thing that will or won't land.

```prompt
SCENE:
Subject: the interior light well of an office tower seen from the very bottom, looking straight up.
Action: static — on every storey a single small dark silhouette sits at a desk against the lit window of its own floor, one figure per level, repeating upward.
Environment: four flat navy wall planes rising and converging toward a small bright opening at the top of frame; each storey reads as a horizontal band of punched amber window rectangles.
Art style: exactly the STYLE LOCK above.
Lighting: warm amber light comes from inside every floor and from the small opening far above; the wall planes step from ochre near the top through slate-blue to near-black at the bottom of frame.
Details: place the vanishing point precisely at the centre of frame; let the storeys repeat at a steady rhythm and grow smaller and closer together toward the top so the stack reads as endless; keep every surface a flat unbroken plane and every window free of lettering.
Compose for a 16:9 frame.
```

### 2c.3 The hold-line chorus — Binder's silhouette line-up

Binder's dancers against flat colour, except these figures hold handsets. Five in
front, then the same arrangement receding until it disappears. This is *"a room of
voices sings the hook in unison"* given a body — the chorus plate.

```prompt
SCENE:
Subject: a long row of standing figures in near-silhouette, each holding a telephone handset to one ear, seen straight on from the front.
Action: static, each figure standing alone in its own circular pool of amber light, all facing camera, weight settled, the coiled cords hanging down from each handset.
Environment: an unbroken deep navy void with no walls, floor line or horizon — the pools of light are the only structure; five figures stand large across the foreground and the same arrangement repeats smaller and dimmer in receding rows behind them until it disappears into the dark.
Art style: exactly the STYLE LOCK above.
Lighting: one hard-edged circular pool of amber under each figure thrown from directly above, with crisp borders and flat unbroken navy between the pools.
Details: leave every face in shadow with the features undrawn; hair reads as one flat mass per figure and clothing as flat shapes, varied between figures so no two silhouettes match; keep the rows evenly spaced and the frame calm, graphic and symmetrical.
Compose for a 16:9 frame.
```

### 2c.4 The statues — *GoldenEye* inverted

Kleinman's sequence toppled the statues of dictators. Karen's story ends on a
bronze that is still on hold. So the frame carries the whole arc at once: two
figures going over on the left, one rising half-out of the ground in the centre,
one complete and upright on the right.

```prompt
SCENE:
Subject: a row of tall stone plinths on a wide public square at night, some bearing standing figures and some empty.
Action: on the left of frame two suited figures tilt backwards off their plinths mid-fall, already past the point of recovery; at the centre a third figure rises from a plinth still half-sunk into the ground; on the right a single figure stands upright and complete, one arm bent to hold a telephone handset to the ear.
Environment: a broad flat plaza of dark slate running to the lower frame edge, with plain navy building slabs standing along the far side of the square.
Art style: exactly the STYLE LOCK above.
Lighting: a low amber uplight at the base of each plinth throws every figure as a hard-edged silhouette and casts long clean wedges of shadow up the buildings behind.
Details: every figure is a flat near-silhouette with the features undrawn; the standing figure on the right is the tallest and most upright shape in the frame; keep the plinths blank and free of any plaque or lettering; keep a large area of empty navy sky above.
Compose for a 16:9 frame.
```

### 2c.5 The paper tower — *Casino Royale*'s falling suits

Kleinman built those titles out of card suits. Yours are forms. The lock already
asks for *"hard scale contrast between a small figure and a large architectural
mass"* — this just makes the mass out of bureaucracy, stacked until it is
geology.

```prompt
SCENE:
Subject: a colossal tower built entirely from stacked sheets of paper, standing alone on an empty plain.
Action: static, with a scatter of loose sheets falling slowly through the air around the tower's upper reaches, each catching a thin amber edge; one small figure stands at the base, tiny against it, a handset held to the ear.
Environment: a flat dark navy ground plane meeting a flat navy sky with no horizon detail; the tower rises from the centre of frame and runs out past the top edge.
Art style: exactly the STYLE LOCK above.
Lighting: a low warm source from the left rakes across the stacked edges so every layer catches a bright ochre line, while the shadowed side falls to near-black; the tower throws one long hard-edged wedge of shadow across the ground to the right.
Details: the stack reads as thousands of flat horizontal layers, slightly uneven, like a cliff face of sediment; keep every sheet blank and unprinted; the figure at the base is a flat near-silhouette with the features undrawn; keep generous empty navy around the tower.
Compose for a 16:9 frame.
```

### 2c.6 The phone in the river

Act 1 already throws it in, and modern Bond sinks things beautifully. Slow, still,
no faces, no hands — **the safest generation in the set after the §2a.4 walk, and
the one to fire first if you want an early read on whether the series clause is
holding the palette.**

```prompt
SCENE:
Subject: a telephone handset sinking through deep water, seen from below and slightly to one side.
Action: the handset falls slowly downward through the middle of frame, tilted, its coiled cord trailing upward above it in a loose curve.
Environment: a vast body of deep navy water, the surface far above reading as a flat plane of lighter slate-blue across the top of frame.
Art style: exactly the STYLE LOCK above.
Lighting: hard-edged amber shafts break through the surface and cut down through the water as clean straight-sided wedges, catching one edge of the handset as it passes through them.
Details: the water steps down through flat bands of stepped value from slate-blue at the surface to near-black at the bottom of frame; a few flat circular bubbles rise in a line toward the surface; keep the handset a simple flat shape with no detail below the level of a large plane; keep the lower third of the frame almost entirely empty near-black.
Compose for a 16:9 frame.
```

### 2c.7–2c.10 The circle chain — one shape that refuses to leave

Bass built whole sequences on a single shape passing through unrelated objects.
§2a.1 and §2a.2 already share a centre point; this makes it a **rule** rather than
a moment. Six circles, same pixel, cut hard on the beat:

> earpiece grill → rotary dial → **key 3** (§2c.1) → manhole → **the booth iris**
> (§2a.3) → the plinth from overhead

Four of the six need plates; the other two exist. All four are overhead, dead
centre, and share the same closing line — **the centring instruction is the whole
point, so do not trim it.**

**2c.7 — the earpiece grill**

```prompt
SCENE:
Subject: the earpiece end of a telephone handset seen from directly overhead, filling the centre of frame — a flat navy disc perforated with a ring of small round holes.
Action: static, held square to camera.
Environment: lying on a flat uninterrupted deep-navy surface that fills the rest of the frame.
Art style: exactly the STYLE LOCK above.
Lighting: one warm amber source from the upper left throwing a hard-edged wedge across the surface; each hole reads as a crisp dark circle carrying a thin amber rim along its upper edge.
Details: place the disc's centre precisely at the centre of frame and keep it radially balanced; keep generous empty navy on all sides.
Compose for a 16:9 frame.
```

**2c.8 — the rotary dial**

```prompt
SCENE:
Subject: a rotary telephone dial seen from directly overhead, filling the centre of frame — a flat disc with ten evenly spaced round finger holes around its edge.
Action: static, with one finger hole at the top of the dial glowing brighter amber than the rest.
Environment: the flat navy face of the telephone body fills the rest of the frame as one uninterrupted plane.
Art style: exactly the STYLE LOCK above.
Lighting: one warm amber source from the upper left, throwing a hard-edged wedge across the dial face and a clean crescent of shadow inside each finger hole.
Details: place the centre of the dial precisely at the centre of frame; keep the dial face completely blank with no digits, letters or markings of any kind; keep the ring of holes radially balanced.
Compose for a 16:9 frame.
```

**2c.9 — the manhole**

```prompt
SCENE:
Subject: an open round manhole in a road surface seen from directly overhead, warm amber light rising up out of it.
Action: static, the light spilling upward from below.
Environment: flat wet navy asphalt filling the whole frame as one plane, with pale crosswalk bars crossing one corner.
Art style: exactly the STYLE LOCK above.
Lighting: the light from the opening is the only source in the frame; it lays a hard-edged amber ring on the asphalt immediately around the hole and leaves everything beyond it deep navy.
Details: place the opening precisely at the centre of frame and keep it perfectly circular; keep the road surface a single flat plane free of markings or lettering apart from the pale crosswalk bars.
Compose for a 16:9 frame.
```

**2c.10 — the plinth from overhead**

The last circle in the chain, and the one that lands the sequence on the statue.

```prompt
SCENE:
Subject: a circular stone plinth seen from directly overhead, with a single figure standing on it in near-silhouette.
Action: static, the figure standing at the exact centre of the disc, one arm bent to hold a telephone handset to the ear, seen from straight above so only the shoulders, the flat mass of hair and the cast shadow read.
Environment: a flat dark slate plaza filling the frame around the circular plinth.
Art style: exactly the STYLE LOCK above.
Lighting: one warm amber source from the upper left; the figure throws one long hard-edged shadow across the plinth and out onto the plaza beyond it.
Details: place the centre of the plinth precisely at the centre of frame; leave the face undrawn; keep the plinth surface blank and free of any plaque or lettering; keep the surrounding plaza a single uninterrupted flat plane.
Compose for a 16:9 frame.
```

### Not on this list, deliberately

Four of the ideas from the same session are **edit-side moves and need no image
prompt at all** — recorded here so nobody generates a plate for them by mistake:

- **The light-wedge wipe** — every plate in this register already carries one
  hard-edged amber wedge; let it sweep and reveal the next plate behind it. The
  transition is made of what the style already does.
- **Cutting on the touch-tone beeps** — hard cuts, no easing, twelve plates before
  the drums arrive.
- **The hold-freeze** — picture freezes and drains to navy-only on each
  *"(I'm sorry, I can't help you)"*, snaps back on *"That's OK."*
- **The one saturated accent** — the lock permits a single rare accent colour.
  Spending it on one recurring object for the whole sequence (the red hold button,
  or Karen's handset) is a grade decision, not a prompt. It would also give
  everything else a reason to sit back down toward navy, which is the §2a.4 fix.

---

## 2d. Clip prompts for the §2c plates — Gemini Omni Flash `[not yet fired]`

**Written 2026-08-12. Briefs, not records.** Nine clips animating the eight
accepted [§2c](#2c-the-second-wave-of-title-sequence-plates--illustrated-register-8-of-10-fired--accepted)
plates — 2c.2 gets two, one per take. Numbered in the order the plates were
harvested, which is **not** §2c order.

**Model: Gemini Omni Flash, in Flow.** Path unchanged from §2b: upload the still →
hover the tile → `⋮ More` → **Animate** → paste the prompt → Create → approve the
credit gate. **30 credits per 10s clip**, so **the full set is ~270 credits** —
and note that **blocked generations still consume credits with no automatic
refund** ([`docs/google-flow/omni-flash.md`](../../google-flow/omni-flash.md)).
Poll for completion; a queued clip looks like a failure.

### What the research changed since §2b

Checked against Google's API reference and the DeepMind prompt guide; engine-level
detail is filed in [`omni-flash.md`](../../google-flow/omni-flash.md).

1. **There is a first-frame *tag*, and §2b did not know about it.** The API accepts
   `<FIRST_FRAME>` inline at the start of the prompt to bind an uploaded image to
   the starting-frame role, `<IMAGE_REF_0>` (zero-indexed, up to six) for
   references, and explicit declarations like
   `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]`. **This
   substantially undercuts the "no true first-frame-to-video" complaint** — there is
   a real binding mechanism, and the complaints most likely describe the *default*
   reference behaviour. It is **API syntax**, and in Flow the Frames input is
   supposed to do this job, so the prompts below use the plain-language sentence.
   **Worth one experiment:** type the tag into Flow's prompt box and see whether it
   binds harder than the sentence. If it does, it also reopens the `animate-slide`
   question in [`omni-flash.md`](../../google-flow/omni-flash.md#the-animate-slide-problem).
2. **The guiding instruction belongs at the very end.** Google's own wording is to
   "add instructions at the prompt's end". §2b put *"Use the given image as the
   starting frame"* second, in the opening breath. **All nine below move it to the
   last line** — the single most likely reason a §2b clip would have drifted.
3. **Timecodes parse.** `[0-3s] A person is walking`, or plainly *"after three
   seconds…"*. Not used below, because one-action-per-clip is the stronger rule —
   but the keypad's 1 → 2 → 3 light-up is the obvious candidate if anyone wants that
   whole beat as a single clip instead of a cut.
4. **Name the reference's job.** When an image is *not* a first frame, say whether
   it is a style, character, subject or background reference. Irrelevant to these
   nine; relevant to everything else in the pipeline.

**The ~50-word ceiling and why these bust it.** Omni is reported to lose quality
past roughly fifty words — and these run 55–65. That is a deliberate trade, not an
oversight: the **shot lock** is mandatory because Omni defaults to cutting, and the
**preserve clause** is mandatory because without a named keep-list Omni re-styles
the whole frame. Those two eat ~35 words before anything happens. The action and
the audio get what is left, which is why every action below is one terse sentence.
**If clips come back soft or drifting, shorten the preserve clause first** — down to
`Keep the flat illustrated style and palette exactly the same.` — and leave the
shot lock alone.

**Five of nine are locked off.** Deliberate. Over-specifying camera is a documented
Omni backfire, static is the most reliable instruction it takes, and camera moves
into geometry the plate never showed are a documented weak spot — which rules out
the pull-back that several of these frames invite.

### 2d.1 The paper tower — plate §2c.5

Push in rather than pull up: the tower runs out past the top of frame, and moving
into unseen geometry is where Omni distorts.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Slow push in toward the small figure at the tower's base as loose sheets keep drifting down around it. Keep the flat illustrated style, the navy-and-amber palette and the hard-edged shadow exactly the same. Paper rustle under slow upright bass, no dialogue. Use this image as the starting frame.
```

### 2d.2 The statues — plate §2c.4

The topple is the action, so the camera does nothing. Naming the standing figure as
*holding still* is what stops Omni animating all four.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Locked off. The two figures on the left tip slowly backwards off their plinths and out of the light; the standing figure on the right holds still. Keep the flat illustrated style, the amber uplight cones and the palette exactly the same. Low brass and timpani, no dialogue. Use this image as the starting frame.
```

### 2d.3 The hold-line chorus — plate §2c.3

**Note the audio clause is different.** This is the one clip that *wants* voices, so
it cannot say "no dialogue" — it asks for chatter and rules out intelligible speech
instead.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Slow push in toward the centre figure as every figure shifts weight slightly and the coiled cords sway. Keep the flat illustrated style, the amber pools of light and the palette exactly the same. Indistinct telephone chatter under slow strings, no intelligible speech. Use this image as the starting frame.
```

### 2d.4 The level above the level, cool take — plate §2c.2

The navy-dominant take gets the move: a continuous rise toward an opening it never
reaches. This is the shot the plate was designed for.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Slow continuous push in toward the small bright opening at the centre, storeys sliding steadily past the frame edges. Keep the flat illustrated style, the amber windows, the navy walls and the symmetry exactly the same. Distant office hum under slow smoky jazz, no dialogue. Use this image as the starting frame.
```

### 2d.5 The keypad — plate §2c.1

The plate is already the end state of the menu, so the clip carries it onward into
the iris-out. Motion graphics of exactly this kind are a documented Omni strength.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Locked off overhead. The lit key pulses once, then its amber glow spreads outward until it floods the whole frame. Keep the flat illustrated style, the navy faceplate and the key grid exactly the same. Three touch-tone beeps, then a dial tone, no dialogue. Use this image as the starting frame.
```

### 2d.6 The rotary dial — plate §2c.8

Object tracking through rotation is the thing Omni is reported to be *best* at, so
this is the highest-confidence clip in the set.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Locked off overhead. The dial turns slowly clockwise, carrying the lit hole round with it, then springs back to rest. Keep the flat illustrated style, the hard-edged wedge of light and the palette exactly the same. A mechanical dial whirr, then a dial tone, no dialogue. Use this image as the starting frame.
```

### 2d.7 The level above the level, warm take — plate §2c.2

**Same plate as 2d.4, different job.** The saturated take is held completely still
so the two cut together as a breath — the cool one moves, the warm one sits. That
turns the warmth difference between the takes from a defect into an edit.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Locked off, camera completely still. The tiny silhouettes at the desks shift and settle at their work; nothing else moves. Keep the flat illustrated style, the saturated amber windows, the ceiling grid and the symmetry exactly the same. Distant hold music and a low room hum, no dialogue. Use this image as the starting frame.
```

### 2d.8 The phone in the river — plate §2c.6

**The red bubble is named in the preserve list on purpose.** It is the single
saturated accent, and an unnamed one-pixel colour is exactly what a re-style eats.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. The handset keeps sinking slowly toward the dark, its coiled cord trailing above it, bubbles rising past. Keep the flat illustrated style, the amber shafts, the single red bubble and the stepped water bands exactly the same. Muffled underwater ambience under one low sustained bass note, no dialogue. Use this image as the starting frame.
```

### 2d.9 The plinth from overhead — plate §2c.10

The light moves, not the camera. **The variant worth one extra clip** is a slow
clockwise rotation about the plinth's centre — very Bass, and it lands the circle
chain — but overhead rotation is the riskier ask, so shoot the sweep first.

```prompt
Create a 10-second 16:9 title-sequence video, one continuous shot, no cuts. Locked off overhead. The amber band of light sweeps slowly across the plinth so the figure's long shadow swings round with it. Keep the flat illustrated style, the flat navy ground and the palette exactly the same. Slow smoky jazz and faint city air, no dialogue. Use this image as the starting frame.
```

### Fire order

**2d.6 (the dial) first** — rotation is Omni's strongest documented motion, so it is
the cleanest read on whether the moved guiding instruction and the preserve clause
are doing their jobs before ~270 credits go out the door. Then **2d.5** (motion
graphics, second-safest), then the rest. **2d.4 is the one most likely to fail**:
a sustained push into repeating geometry is precisely the "camera moves into areas
the source never showed" weakness.

---

## 2e. The New York walk plates — super-8 register `[not yet fired]`

**Written 2026-08-13. Briefs, not records** — replace each with what was actually
typed once they have been run.

Ten location stills of Karen crossing New York on foot, for the **music video** of
[`songs/all-day-to-complain.md`](./songs/all-day-to-complain.md). They are the
connective tissue the song already asks for and the ledger has never had: Verse 2
is a list of places and dates (*"Regional office, Thursday. Rain on the glass…
Borough office, Tuesday… State house, Friday"*), and Act 2's canon rule is that
**time passes in the wide shots — rain → snow → sun**
([`story.md`](./story.md), Act 2 formula, step 5).

So the set is **a nine-month clock**. One plate per month, September to May, plus
a tenth in hard June sun as the payoff. The weather is not decoration; it is the
only thing in the frame that says nine months went by.

> **These are the first §1 plates in this ledger that are ours rather than
> Jack's.** §2.1–2.5 are a record of hand-typed work. This section is a brief in
> the shape §2b/§2c/§2d established, and it is **owed the same treatment**:
> overwrite it with what was actually pasted once it is fired.

### The register, and why these are cast

**These are §1 super-8 photoreal, not §1b illustrated.** That decides the casting
question outright: `@Karen` **is** cast on every one of these, and **no prompt
below describes her face**, per the rule in
[`characters/karen.md`](./characters/karen.md). The §1b override — *describe the
likeness in prose, do not cast* — is scoped to the flat graphic register, where
the face carries no features. It does not apply here.

The illustrated title-sequence plates (§2a, §2c) and these are **two different
jobs in the same video**: the graphic register carries the titles and the hook,
this one carries the story between them.

### The engine: Nano Banana Pro, and a naming correction

**There is no model called "Nano Banana Pro 2".** Checked 2026-08-13. The family
is **Nano Banana 2** (Gemini 3.1 Flash Image) and **Nano Banana Pro** (Gemini 3
Pro Image), both generally available; Pro is the reasoning/quality lane, NB2 the
fast one ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available/)).

**Fire these on Nano Banana Pro**, and that is a reversal of the §2a/§2c default.
Three reasons, and the first is already an open question in
[`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md):

1. **NB2's default improvement direction fights this register.** A head-to-head
   report has NB2 coming back *"too sharp… too overly contrast… almost
   overexposed"* against Pro's *"a lot more natural"*. The §1 lock is soft edges,
   gentle halation, deep-but-soft blacks and `no AI "hyper-sharp HDR" look` —
   i.e. the exact axis NB2 pushes hardest on. **Consider this batch the
   calibration run that answers that open question.**
2. **Pro reads hex codes strongly**, NB2 only *"to a lesser extent"* — which is
   the lever for holding a grade across ten plates, and the proposed fix for the
   §2a.4 warmth drift.
3. **Pro is the structure-and-reasoning tier.** These are ten compositions with a
   named lens, a named crowd behaviour and a stated framing rule each. That is
   what the Pro lane is for.

**The cost, and it is real:** Pro exhausts Flow's rate limit far faster than NB2,
which is why practitioners default to NB2 in Flow at all. Ten plates × 4
candidates is where that will bite. **Fire the calibration plate first** (see
*Fire order*), confirm the register, then run the rest.

**Pro's context window is 65,536 tokens** — half NB2's. Irrelevant at this prompt
length, but worth knowing before anyone bolts a JSON style token onto the front.

**Live web search is wired into these models.** For §2c that was a drift risk; for
naming real New York locations in the present day it is a *feature*, and it is
part of why these prompts name actual places instead of describing generic ones.

### Avoiding the AI-slop look — what the research changed

Checked 2026-08-13. The consistent finding across the practitioner material is
that slop is **a process failure, not a model failure**: strip out creative
direction and the model falls back to the statistical average, which is centred,
symmetrical, oversaturated, posed, and set nowhere in particular. The named
signatures are all things a prompt can pre-empt
([imagine.art](https://www.imagine.art/blogs/ai-slop-in-images-and-videos),
[Miraflow](https://miraflow.ai/blog/how-to-make-ai-images-look-like-real-photos-prompt-tricks),
[Imagera](https://imagera.ai/blog/make-ai-images-look-real-2026)):

| Signature | What produces it | The counter used below |
|---|---|---|
| Centred, symmetrical framing | no stated composition | she is held a third off-centre, weight carried by the architecture |
| The frozen portrait | "smiling at camera" | mid-stride, weight on one foot, eyeline off-frame |
| Waxy, noiseless perfection | no grain or ISO named | the §1 lock already does this — do not weaken it |
| Oversaturated sheen | vivid colour words | restrained colour words in the scene; the vibrancy stays a *stock* property |
| Nowhere-in-particular settings | "urban background" | a named street, a named material, a named piece of wear |
| Over-rendered digital-art look | `hyperrealistic, 8K, masterpiece` | **not one of those words appears below** |
| Impossible/perfect light | "beautiful lighting" | one stated source, one stated weather, per plate |

**Two of these need saying out loud because they cut against instinct:**

- **"Cinematic" is a slop word on its own.** The advice is explicit — replace
  buzzwords like *cinematic* and *photorealistic* with a concrete reference
  (*"1970s European commercial photography"*). Every plate below names a lens, a
  camera position and a shutter behaviour instead. The word *cinematic* appears
  in this section's prose and in **none** of its prompts.
- **Do not answer slop with a long negative list.** NB2/Pro honour targeted
  negations, but **long exclusion stacks dilute** — the finding §2c already
  adopted. So the anti-slop material below is written **positively**, with a
  single short negative clause at the end.

### ⚠️ The one live tension: `vibrant` vs `restrained`

**The §1 lock says `punchy, vibrant palette` and `vibrant colours`. The
anti-slop research says vivid colour words are what produce the plastic
oversaturated sheen.** These pull against each other and it would be dishonest
not to flag it.

**The resolution adopted here: the vibrancy is a property of the *stock*, the
restraint is a property of the *scene*.** The lock keeps its words untouched —
it is a restore point and character-for-character fixed — and the candid clause
governs the subject matter, the weather and the light. A punchy film stock
photographing a grey wet street gives you a grey wet street with body in it. A
punchy film stock photographing a "vibrant bustling city" gives you slop.

**If plates come back candy-coloured anyway**, the fix is the untested lever from
§2c and this is the batch to try it on: **append a hex pin** rather than editing
the lock — Pro reads hex strongly. Do it on one plate and compare.

> ### How to fire any of these
>
> **Four parts, in this order.** The first three are identical every time; only
> part 4 changes.
>
> 1. the **cast + series instruction** below;
> 2. the **§1 STYLE LOCK** block, [verbatim](#1-the-style-lock);
> 3. the **CANDID CLAUSE** below, verbatim;
> 4. the **scene block** under each heading.
>
> **Part 1 — cast, use case, series and wardrobe:**
>
> ```prompt
> Cast: @Karen.
>
> Use the attached Karen Character reference for her identity and wardrobe only. Take the location, the framing, the light and the weather entirely from the description below.
>
> This image is one still in a set of ten present-day New York location plates for a music video, in which the same woman crosses the city on foot over nine months. Maintain visual identity across the whole set: the same woman, the same core wardrobe, the same film register.
>
> Wardrobe, constant in every plate: a cream blouse, a camel cashmere cardigan, tailored high-waisted charcoal trousers, low-heel leather flats, and a large structured leather handbag carried on one forearm. Only the outer layer changes, with the weather stated in the scene.
> ```
>
> Three vendor-documented moves are doing work there: **naming the use case**
> (the model makes "a thousand small decisions" off it), **stating series
> membership** in prose, and **naming what the reference contributes** — the
> relationship instruction is the load-bearing middle term of Google's own
> reference-image template. See
> [`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md).
>
> **The wardrobe clause is deliberately split.** The core outfit is fixed so the
> ten plates read as one woman on one errand; the **outer layer is the clock**.
> Cardigan alone in September, overcoat by December, cardigan again in May. That
> is the same device as the canon weather rule, worn instead of filmed.
>
> **Part 3 — the CANDID CLAUSE.** New in this section, and the whole anti-slop
> payload. Paste it verbatim, the same way the locks are pasted:
>
> ```prompt
> CANDID CLAUSE (keep identical every time):
>
> Framing: hold her about a third in from one edge of the frame and let the architecture carry the weight of the composition. Let one foreground element cross the lens, and let bystanders be cut by the frame edges.
>
> Moment: catch her mid-stride with her weight on one foot, her coat and hair still moving, and her eyeline off-camera on something outside the frame. She is walking somewhere, unaware of the lens.
>
> People: everyone else is indifferent and busy with their own errand. Nobody looks at her and nobody looks at the camera; faces are turned away, distant or in profile.
>
> Surfaces: the city is worn in — salt-stained kerbs, patched asphalt, gum-flecked stone, scaffolding pipe, weathered paint, blank taped-over hoardings.
>
> Optics: allow a trace of motion blur at her hands, faint colour fringing at high-contrast edges, and focus that sits on her and falls off honestly everywhere else.
>
> Restraint: keep the colour of the scene itself restrained and the light ordinary for the weather stated below. This is a frame pulled from a documentary.
>
> Not a posed portrait, not a stock photograph, not symmetrical.
> ```
>
> The last line is the entire negative budget for the prompt. **Do not extend
> it** — that is the diluting shape.
>
> **Flow settings:** landscape, **16:9**, 4 candidates, **Nano Banana Pro**. Every
> block restates the ratio in prose, which the guides recommend even when the UI
> already sets it. 21:9 is available and would match §2.6, but the music video
> cuts 16:9 — pick one and hold it across all ten.
>
> **No legible text in any plate.** Standing rule (§1), and it is doing heavy
> lifting here: Grand Central's boards, Wall Street's plaques and Midtown's
> avenue signage are all text minefields. Every block below blanks them.

### The shot list

Each plate is a month, a location, a lens and one composition rule. The
composition rule is the anti-slop content — it is what stops the model handing
back the postcard version of a famous place.

| # | Month | Where | The shot | The rule |
|---|---|---|---|---|
| 2e.1 | Sept | Grand Central concourse | 135mm from the west balcony, 1/15s | she is the one legible figure in a field of smear |
| 2e.2 | Oct | Wall Street canyon | 200mm compression, straight down the street | half-occluded by passing shoulders |
| 2e.3 | Nov | Civic colonnade, Foley Square | 35mm dolly alongside her | columns strobe the foreground as a natural wipe |
| 2e.4 | Dec | Staten Island Ferry, stern deck | 50mm handheld, from behind and low | the skyline is small, grey and leaving |
| 2e.5 | Jan | Roosevelt Island tram | 28mm from the back of the cabin | the window does the moving, not the camera |
| 2e.6 | Feb | Coney Island boardwalk | 85mm long lens down the boards | backlit, empty, off-season |
| 2e.7 | Mar | Brooklyn Bridge promenade | 24mm at plank level | she enters as legs and a coat hem; the tower is cropped |
| 2e.8 | Apr | Elevated 7 platform, Queens | 35mm low, down the platform | she is small; Manhattan is smaller |
| 2e.9 | May | Central Park, the Mall | 50mm static at path level, she exits frame | the dapple lands on the path, not on her |
| 2e.10 | June | Fifth Avenue crosswalk | 40mm handheld from inside a moving cab | shot through a door frame and a mirror |

**Reserve locations, no prompt written** — the obvious next ten if this set
lands: the High Line, Washington Square arch, Bethesda Terrace arcade, a subway
stair emerging into daylight, the Queensboro Bridge underside, the Whitehall
ferry terminal ramp, a Midtown steam stack, Times Square (**text minefield —
only with every fascia blown to unreadable glare**), the Oculus, a Harlem
brownstone stoop in rain.

---

### 2e.1 Grand Central — the long diagonal · September

The first rung, and the only plate where she is *inside* the machine rather than
walking between its buildings. The device is old and it still works: everybody
smears, one person doesn't.

The postcard version of this room is the sun shafts landing centre-frame on the
marble. **This prompt puts them behind her on purpose.**

```prompt
SCENE:

Subject: a woman crossing the main concourse of Grand Central Terminal at the morning rush, seen from the west balcony above.

Action: she walks one unbroken diagonal across the marble at a steady, purposeful pace, handbag on her forearm, chin level, her eyeline fixed on something out of frame ahead of her, while every other commuter around her changes direction and dissolves into streaks.

Environment: the concourse floor in early September, the painted ceiling cropped away by the top of the frame, the brass information clock sitting off to one side rather than centred, a cleaner's cart parked against a pillar, ticket windows dark.

Camera: 135mm long lens from the balcony, looking down at about thirty degrees, locked off on a tripod at one-fifteenth of a second so the crowd smears and she survives as the one legible figure, carrying her own trace of blur at the hands and feet.

Lighting: the high south windows throw thin dusty shafts that land on the floor well behind her; the concourse itself is lit flat and warm by its own chandeliers, and she walks through that flat light rather than through a beam.

Details: keep every departure board, sign and ticket window blank and unreadable; the marble is scuffed and gum-flecked; a wheeled suitcase and two turned backs cross the lower foreground; she wears the cardigan with no coat, because it is still warm.

Compose for a 16:9 frame.
```

### 2e.2 Wall Street — the canyon, compressed · October

The money rung. A 200mm from a long way down the street stacks the facades flat
and turns the crowd into a wall she has to come through — which is the song's
whole mechanism in one lens choice.

```prompt
SCENE:

Subject: a woman walking toward camera along a narrow Financial District street in Lower Manhattan, in the middle of the morning crowd.

Action: she walks straight at the lens at her own pace while the crowd flows around and past her, her handbag held against her body, one hand keeping her coat shut, a folded envelope in the other hand.

Environment: a tight stone street canyon in October rain, the facades stacked flat by the long lens, scaffolding pipe and plywood hoarding running down one side, wet black asphalt, a road stack venting steam that drifts across the frame between her and the camera.

Camera: 200mm telephoto from far down the street at chest height, hand-held, the compression flattening a whole block into layers behind her.

Lighting: flat grey overcast with no sun anywhere in the frame; the only warm points are a traffic signal and its long smeared reflection in the wet road.

Details: umbrellas at several heights, a steel police barrier at the kerb, blank taped-over hoardings, and passing shoulders crossing the foreground so she is briefly half-hidden; keep every sign, plaque and awning free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.3 The civic colonnade — Foley Square · November

**The bureaucracy rung, filmed literally.** A dolly alongside her past a civic
colonnade gives you a light-and-shadow wipe every time she passes a column — the
same device as the §2c light-wedge wipe, arrived at through architecture instead
of grading.

```prompt
SCENE:

Subject: a woman walking the full length of a civic colonnade outside a large government courthouse building in Lower Manhattan, seen from the side.

Action: she walks steadily in profile, handbag on her forearm, coat open, taking the steps at the end of the colonnade without breaking stride.

Environment: a deep stone colonnade of tall square columns in mid-November, the plaza and bare plane trees of the square visible between the columns, wet leaves flattened on the stone, a metal barrier stacked against a wall.

Camera: 35mm on a dolly running alongside her at exactly her walking pace, at chest height, so the near columns sweep through the foreground and briefly black out the frame between each one.

Lighting: low late-autumn sun raking straight down the length of the colonnade, laying hard bars of light and shadow across her one after another as she passes each column.

Details: she wears a charcoal wool overcoat over the cardigan now; two figures in suits stand talking at the far end with their backs turned; keep every plaque, notice board and door free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.4 The Staten Island Ferry — the skyline leaving · December

**Fire this one first.** One figure, no crowd, no text, one weather — it is the
cleanest possible read on whether the Pro register and the candid clause are
doing their jobs, before ten plates' worth of rate limit goes out the door.

The orange of the ferry is the single saturated accent, which is the rule §2c
watched propose itself. Let it be the only strong colour in the frame.

```prompt
SCENE:

Subject: a woman on the open stern deck of the Staten Island Ferry, seen from behind and slightly below.

Action: she walks the length of the empty deck away from camera toward the stern rail, coat and hair taking the wind sideways, one hand steadying the handbag on her forearm.

Environment: the open orange-painted steel stern deck in December, chipped paint and rust bloom along the welds, a chain slung across a gap in the rail, wooden benches bolted to the deck, Lower Manhattan pulling away behind her as a low grey band on pewter water, gulls holding station off the stern.

Camera: 50mm, hand-held at waist height a few metres behind her, slightly low, with a little natural sway in the frame.

Lighting: flat winter overcast with no sun and no horizon glow; the light is even, cold and directionless, and the orange steel is the only strong colour in the frame.

Details: she wears a charcoal wool overcoat buttoned over the cardigan; two other passengers sit at the far end of a bench with their backs turned and their hoods up; salt spray dries in pale streaks on the deck; keep every notice, sign and life-ring free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.5 The Roosevelt Island tram — January

The one plate where **the window moves and the camera doesn't** — a rest beat in
a set of walks, and a shot almost nobody uses.

```prompt
SCENE:

Subject: a woman inside the Roosevelt Island aerial tram cabin, seen from the back of the cabin at standing height.

Action: she moves down the length of the cabin toward the front glass, one hand travelling along the overhead pole to steady herself as the cabin sways, the other holding her handbag against her hip.

Environment: the tram cabin in January, condensation and snowmelt beaded on the windows, the Queensboro Bridge's steel sliding past outside, the East River flat grey a long way below, six or seven other riders standing and sitting in heavy coats.

Camera: 28mm from the rear of the cabin at standing eye height, hand-held, the cabin's own frame and pole running through the foreground.

Lighting: dull overcast daylight coming through fogged glass, topped up by the cabin's own cold strip light in the ceiling.

Details: she wears the charcoal overcoat with the collar up; one rider is asleep against the glass, another faces away out of the far window; wet footprints on the floor; keep every notice, map and panel in the cabin free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.6 Coney Island boardwalk — February

*"Sun, snow, sun again, and not one word."* The bridge line, given a picture. An
off-season boardwalk is the least AI-postcard version of New York available, which
is exactly why it belongs in the set.

```prompt
SCENE:

Subject: a woman walking toward camera along an empty Coney Island boardwalk in deep winter.

Action: she walks the boards straight at the lens with her coat held shut against the wind, her breath visible, handbag on her forearm, not hurrying.

Environment: the boardwalk in February, concessions shuttered behind blank roll-down steel, the Wonder Wheel's bare steel far out of focus behind her, scraped snow pushed into grey ridges along the rail, dry sand blown in fans across the planks, one gull on a post.

Camera: 85mm long lens from far down the boards at chest height, hand-held, so the shuttered fronts compress into a wall behind her.

Lighting: hard low winter sun coming from behind her, backlighting her breath and the blown sand and putting the boards themselves in shadow, with the front of her coat in soft bounce from the snow.

Details: she wears the charcoal overcoat over the cardigan, scarf, no hat; the planks are split and silvered with old nail heads standing proud; keep every shutter, kiosk and signboard free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.7 Brooklyn Bridge — from the planks · March

The most-photographed walkway in the world, so the whole job of this prompt is to
**refuse the centred symmetrical tower shot**. Camera on the deck, tower cropped,
her entering as a coat hem before she is a person.

```prompt
SCENE:

Subject: a woman walking the wooden promenade of the Brooklyn Bridge, seen from almost down at plank level.

Action: she enters the frame from the left and walks across it, so she reads first as low-heeled shoes, a coat hem and a handbag before the rest of her arrives in shot.

Environment: the promenade in wet March, worn dark timber planks running away underfoot, the suspension cables converging overhead and out of the top of the frame, one stone tower cropped hard by the right-hand frame edge, cyclists and a jogger cut by the edges of the frame.

Camera: 24mm wide angle set almost on the deck, tilted slightly up, locked off, with the near planks huge and soft in the foreground.

Lighting: flat grey daylight with the sky blown to plain white between the cables and no sun visible; the timber holds most of the tone in the frame.

Details: she wears the charcoal overcoat, hem wet at the back; puddles stand between the planks and hold the cable pattern; chewing gum and old tape marks on the boards; keep every plaque, banner and bike marking free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.8 The elevated platform, Queens — April

The rung where she is furthest from power and it shows: **she is small in the
frame and Manhattan is smaller still**, a serrated band on the horizon she has
been phoning for seven months.

```prompt
SCENE:

Subject: a woman walking the length of an outdoor elevated subway platform in Queens at dusk, seen from the far end of the platform.

Action: she walks away from the camera down the middle of the empty platform toward the far stairs, small in the frame, handbag on her forearm.

Environment: an elevated platform in April, a steel canopy on riveted stanchions with peeling green paint, the tracks running away on both sides, low brick and vinyl-sided blocks below, and the Manhattan skyline far behind as a small serrated band on the horizon.

Camera: 35mm at hip height from the opposite end of the platform, locked off, the canopy stanchions receding in a row down one side of the frame.

Lighting: the last of the blue dusk in the sky with the platform's own sodium fixtures just coming on warm, one of them flickering, so the platform is amber and everything beyond it is blue.

Details: she wears the cardigan with a light raincoat over it now; one other passenger sits far down a bench facing away; a discarded coffee cup by a stanchion; keep every sign, board and train front free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.9 Central Park — the Mall · May

Nine months in, and the first frame with anything green in it. **Dappled light is
the highest slop risk in the set** — every model in the world wants to bathe her
in it — so the prompt puts the dapple on the path and lets it clip her shoulder
only.

```prompt
SCENE:

Subject: a woman walking the elm tunnel of the Mall in Central Park, passing close to a camera set low at the edge of the path.

Action: she walks past the lens from left to right at her own pace and is already halfway out of the right-hand side of the frame, still in mid-stride, handbag swinging slightly.

Environment: the Mall in May, the double rows of old elms arching over the path in full leaf, cast-iron benches down both sides, a dog walker and two people on a bench well behind her, the path's hexagonal pavers worn smooth.

Camera: 50mm set low at knee height at the edge of the path, locked off, so she crosses close to the lens and the tunnel of elms runs away long behind her.

Lighting: high midday sun broken into hundreds of small moving patches by the canopy, landing almost entirely on the path and the benches, with only one patch clipping her shoulder as she passes.

Details: she wears the cardigan again with no coat, sleeves pushed up; last autumn's leaf litter still packed under the benches; keep every plaque, bin and lamp post free of readable lettering.

Compose for a 16:9 frame.
```

### 2e.10 Fifth Avenue, through a cab window — June

The payoff plate, and the only one shot from a vehicle. **Foreground depth is the
single most reliable anti-slop device** — a door frame and a wing mirror sitting
soft in front of the shot is something a generated image almost never volunteers.

```prompt
SCENE:

Subject: a woman crossing a wide Midtown avenue in a crowd of pedestrians, seen from inside a moving yellow taxi.

Action: she strides across the crosswalk in the middle of the crowd, half a pace ahead of everyone around her, coat over her forearm, handbag in the other hand.

Environment: a Fifth Avenue crossing in hard June sun, the crowd stepping off both kerbs at once, a cyclist cutting through the near lane, heat shimmer standing off the asphalt, tall facades running away up the avenue behind her.

Camera: 40mm hand-held from the rear seat of a moving taxi, shooting out through the open window, so the cab's door frame runs down one side of the shot and the wing mirror sits large and soft in the near foreground.

Lighting: high hard summer sun almost overhead, dropping short black shadows straight down under everyone, with one hot reflection sliding across the glass at the edge of the frame.

Details: she wears the cream blouse and the cardigan tied at her shoulders, sleeves pushed up; the crowd is dressed for heat and nobody is looking anywhere but forward; keep every street sign, awning, bus flank and shop front free of readable lettering.

Compose for a 16:9 frame.
```

### Fire order

1. **2e.4 (the ferry) first — it is the calibration run, not just a plate.** One
   figure, one weather, no crowd, no text. If Pro's register is right and the
   candid clause is landing, it will show here with nothing else to blame.
2. **2e.6 (Coney Island)** — the second-simplest, and it confirms that hard
   backlight survives the §1 lock's `preserve highlight detail` clause.
3. Then **2e.3, 2e.8, 2e.7, 2e.5, 2e.9** in any order.
4. **2e.2 and 2e.10 late** — dense crowds close to the lens are where hands and
   faces go wrong, and both are in text-heavy parts of the city.
5. **2e.1 (Grand Central) last, and expect to rewrite it.** It is the most famous
   interior in the set, the most text-dense, and the only one asking the model to
   hold one figure sharp inside a long-exposure smear. **Two regenerations, then
   rewrite** — the standing rule from §2c.

### What to watch, and what it would prove

- **Does Pro hold the soft register where NB2 over-sharpens?** This is the
  standing open question in
  [`nano-banana-2.md`](../../google-flow/nano-banana-2.md). Ten plates is a real
  answer to it.
- **Does the candid clause survive the style lock?** The lock says *vibrant*; the
  clause says *restrained*. If plates come back candy-coloured, the clause lost —
  and the hex pin is the next lever, appended, never written into the lock.
- **Does `@Karen` hold across ten locations, ten weathers and two outer layers?**
  If wardrobe drifts, the fix is the shorter-prompt finding from
  [`nano-banana-2.md`](../../google-flow/nano-banana-2.md), not a longer wardrobe
  paragraph.
- **Does the off-centre instruction actually take?** It is the one anti-slop
  clause with no fallback if the model ignores it — everything else can be
  graded, cropped or reshot.

### The clips these become

**No clip prompts are written yet.** When they are, they follow §2d's shape and
its one hard-won correction — **the guiding instruction goes on the last line** —
and the walking action is the safest possible ask of a video model (the §2a.4
finding). The obvious moves: 2e.3 and 2e.10 are already camera moves and want
the plate's own motion continued; 2e.1, 2e.4 and 2e.9 want to be locked off and
let her do the moving.

---

## 2f. Clip prompts for the §2e walk plates — Gemini Omni Flash `[not yet fired]`

**Written 2026-08-13. Briefs, not records** — replace each with what was actually
typed once they have been run.

**Ten plates came back and they are the ten clips below**, in the order they were
harvested. Two housekeeping facts before anything else:

- **§2e is still marked `[not yet fired]` above and that is now wrong.** Ten
  finished frames exist. The briefs in §2e are owed the same overwrite §2.6 got:
  paste what was actually typed.
- **2f.1 is a plate the §2e shot list never had** — a snow-and-slush street with a
  scaffolding pipe across the frame. It is a good frame and it slots straight into
  the winter run. Note also that she is in the **cardigan with no coat** in it,
  which puts it out of step with the wardrobe clock (§2e Part 1); the clip below
  does not try to fix that, because **a clip never fights its own plate**.
- The plate that did **not** come back is the civic colonnade (§2e.3). If it gets
  re-run, its clip is the easy one: the plate is already a dolly, so the clip is
  *continue the move at the same pace*.

**Model: Gemini Omni Flash, in Flow.** Same path as §2b/§2d. **30 credits per 10s
clip**, so **the full set is ~300 credits**, and blocked generations still consume
credits with no automatic refund
([`omni-flash.md`](../../google-flow/omni-flash.md)).

### Ingredients, not Frames — and how these get fired

Checked 2026-08-13. Google's own Flow help splits the input modes cleanly:
**Frames to Video** takes start/end images; **Ingredients to Video** exists so you
"consistently use the same images for your character and key objects from one clip
to the next", and you feed it by **dragging media into the prompt box or typing
`@` to reference an uploaded asset**
([Flow help](https://support.google.com/flow/answer/16353334)). Its two stated
rules matter here:

1. **Prepare clean ingredients.** The plates are clean — they are finished,
   graded, single-subject frames.
2. **Avoid conflicting guidance between text and visuals.** This is the load-bearing
   one, and it is why **no prompt below re-describes what the plate already shows.**
   The word budget goes on motion, timing and audio — the three things the still
   cannot carry. Re-describing the frame is how you talk the model into redrawing it.

> **How to fire any of these**
>
> 1. **Video tab → model picker → Gemini Omni Flash.** Confirm it; Flow's default
>    model has moved before.
> 2. **Drag the plate into the prompt box** (or `@` it if it is already uploaded).
>    That is the ingredient.
> 3. **Paste the block.** Nothing else — no style lock, no candid clause. Both of
>    those are *image* instruments and both are already baked into the plate. On
>    Omni they would be forty words of dilution.
> 4. **Cast `@Karen` only if identity drifts.** Not by default. The plate already
>    carries her, and adding a second visual source is exactly the "conflicting
>    guidance" the vendor doc warns about. If a clip comes back with her face
>    rebuilt, add the Character tile as a second ingredient and re-fire — that is
>    the documented purpose of the consistency layer, and it is the lever, not the
>    default.
> 5. **16:9, one clip at a time**, and poll for completion. A queued clip looks
>    like a failure; a real failure reads *"Oops, something went wrong!"*.
>
> **Never described in any block below: her face.** Standing rule
> ([`characters/karen.md`](./characters/karen.md)), and on this engine it is also
> just good practice — faces and fine hand articulation are the two documented
> artefact sources, and every one of these plates already frames around them.

### The shape, and the one thing that changed from §2d

Same six-part shape §2d settled on, with the guiding instruction **last** — the
correction §2d bought and has still not spent:

1. **shot lock** — duration, ratio, *one continuous shot, no cuts*, **and speed**;
2. **camera** — one of Omni's parsed camera words, or *locked off*;
3. **one action**, hers, resolving inside ten seconds;
4. **one ambient motion**, and where it helps, **one thing named as holding still**;
5. **preserve clause** — `Keep [X, Y, Z] exactly the same.`;
6. **audio**, named, ending `no dialogue`;
7. **`Use this image as the starting frame.`**

**What is new in this set is item 4 and the word `real speed` in item 1.** Both are
the live-action tax. §2b and §2d animate flat graphics, where nobody can tell how
heavy a thing is; these are photographs of a woman walking, and **weight is the
entire game**.

### Avoiding the AI-slop look in motion — what the research changed

Checked 2026-08-13, and the finding is the same one §2e landed on from the stills
side: slop is a process failure. The video tells are different tells, though, and
they are all things a prompt can pre-empt
([Green Frog Labs](https://greenfroglabs.com/blog/ai-video-quality-avoid-slop-appearance),
[Opus](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells),
[Magic Hour](https://magichour.ai/blog/realistic-ai-video-prompting)):

| Tell | What produces it | The counter used below |
|---|---|---|
| Weightless, gliding walk | gait never specified | `weight transferring foot to foot` — named in every walking clip |
| Everything drifts into slow motion | speed never specified | `at real speed`, in the opening sentence |
| The whole frame animates at once | every element implicitly in play | **one** action, **one** ambient motion, and often one thing named as *not* moving |
| Glassy robotic camera glide | camera unspecified | `locked off`, or handheld with the sway named — Omni's own vocabulary |
| Sterile silence, or a stock score | audio unprompted; Omni picks its own | a named ambient stack per clip, room tone first |
| Morphing faces and hands in crowds | crowd asked to perform | crowds are named as continuing, never as doing; no hand articulation is asked for anywhere |
| The frame quietly re-styled | no keep-list — **the Omni-specific one** | a per-clip preserve clause naming the grade and the wardrobe |
| It cuts to a different shot | **Omni defaults to cutting** | `one continuous shot, no cuts`, first line, every time |

**Two things worth saying plainly.**

- **There are no negative prompts on this engine** — the API does not accept them
  ([`omni-flash.md`](../../google-flow/omni-flash.md)). So every anti-slop item
  above is written **positively**. The only negations in the whole set are
  `no cuts` and `no dialogue`, both of which are instructions rather than
  exclusions.
- **The word `cinematic` appears nowhere below**, same rule as §2e. Nor do
  `hyperrealistic`, `8K` or `masterpiece`. The register is already in the plate;
  asking for it again in adjectives is how you lose it.

**The ~50-word ceiling, and these blow through it.** They run **80–98 words** —
worse than §2d's 55–65, and worth being honest about rather than quietly hoping.
Two things pushed them up and both are live-action costs: the preserve clause has
to name a *photographic* grade rather than "the flat illustrated style", and item
4 (the ambient motion) simply did not exist in the graphic sets. Everything that
could be cut has been: **no block below re-describes its own plate**, which is
where the first draft's extra fifteen words went.

**If clips come back soft or drifting, shorten in this order** and change nothing
else:

1. **the preserve clause**, down to `Keep the film grain, the light and her clothes
   exactly the same.` — §2d's rule, and it buys ~12 words;
2. **the ambient motion sentence** — the clip gets duller, but it survives;
3. **the audio line**, down to two named sounds.

**Never the shot lock.** `one continuous shot, no cuts` is what stands between us
and Omni's default, which is to cut.

---

### 2f.1 The snow street — the unlisted plate

Three blurred pedestrians already cross this frame, so the ambient motion is free:
they clear the lens and the street keeps going. Locked off, because the foreground
crossings only read as accidental if the camera is not chasing them.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off. She keeps walking in profile at the same steady pace, her weight transferring foot to foot. The blurred pedestrians cross the lens and clear it, and fine snow keeps falling. Keep the film grain, the flat grey winter light, her camel cardigan and the scaffolding pipe across the frame exactly the same. Slush underfoot, muffled traffic and cold wind, no dialogue. Use this image as the starting frame.
```

### 2f.2 Grand Central — the long diagonal

**Fire this one last and expect trouble.** The plate's whole conceit is a
*shutter* artefact: a one-fifteenth-of-a-second exposure that smears a crowd
around one sharp woman. Video has no such shutter. Asked to animate it, the
honest prediction is that Omni resolves the smear into ordinary sharp commuters
and the idea evaporates.

The prompt below asks for the smear explicitly, in the preserve clause, which is
the only lever available. **If it loses, do not spend three more generations on
it** — hold the plate as a still in the edit and put a slow digital push on it.
A long-exposure photograph is allowed to stay a photograph.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off from the balcony. She keeps walking her diagonal at the same steady pace while every other commuter stays a moving blur around her. The cleaner's cart does not move. Keep the long-exposure smear on the crowd, the warm chandelier light and her camel cardigan exactly the same. A vast echoing concourse, footsteps and rolling luggage, no intelligible speech. Use this image as the starting frame.
```

### 2f.3 Wall Street — the canyon

The steam is the gift here: it is the one element that can move a lot without
anyone being able to say it moved wrongly. Handheld, barely — a 200mm handheld
drifts, and that drift is worth more than any specified move.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Handheld on a long lens with a slight drift. She keeps walking toward the camera through the crowd, her weight transferring foot to foot. The steam keeps drifting across the street between her and the lens and the rain keeps falling. Keep the flat grey overcast, the red signal reflections in the wet road, her dark coat and the white envelope in her hand exactly the same. Rain on umbrellas, wet tyres and distant traffic, no dialogue. Use this image as the starting frame.
```

### 2f.4 The ferry — the skyline leaving

**The one clip with a real ending.** She reaches the rail and stops, which gives
the edit a natural out at ten seconds instead of a fade. The gulls hold station,
which is what gulls behind a ferry actually do — and it is a motion Omni can hardly
get wrong.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Handheld behind her with a little natural sway. She walks the last steps to the stern rail and stops there, her hair and cardigan taking the wind sideways. The gulls hold station off the stern and the skyline recedes very slowly. Keep the orange deck steel, the flat cold overcast, the pewter water and her camel cardigan exactly the same. Wind across the deck, engine drone, gull calls and water, no dialogue. Use this image as the starting frame.
```

### 2f.5 Coney Island — the boardwalk

**The Wonder Wheel is named as still on purpose.** It is off-season and it should
not be turning — and a big rotating structure in the background is exactly the
detail a video model volunteers unasked. Her breath is the anti-slop payload:
cold air is a physics tell that reads instantly.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off on a long lens far down the boards. She keeps walking toward the camera, her breath clouding in the cold and her weight transferring foot to foot. Blown sand drifts across the planks and the gull shifts on its post; the Wonder Wheel does not turn. Keep the hard low backlight, the shuttered steel fronts and her dark overcoat and scarf exactly the same. Wind, distant surf and creaking boards, no dialogue. Use this image as the starting frame.
```

### 2f.6 Brooklyn Bridge — from the planks

**Fire this one first.** No face in the frame at all, one motion, everything else
architecture. It is the cheapest possible read on whether Omni holds the plate's
grade and its plank-level geometry before 300 credits go out the door — and if it
comes back re-styled, we learn that with nothing else to blame.

She leaves the frame, which is the correct shape for a ten-second clip: an exit is
an edit point.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off almost on the deck. She walks across the frame and out of it, so she leaves as a coat hem and a handbag, and the cyclist rolls on past behind her. Keep the low plank-level angle, the wet dark timber, the converging cables and the flat white sky exactly the same. Footsteps and bicycle tyres on wet timber, wind through the cables, traffic below, no dialogue. Use this image as the starting frame.
```

### 2f.7 The elevated platform — Queens

She is tiny in this frame, so almost nothing about her can go wrong. The train is
**audio only, out of frame** — a passing train is complex motion into geometry the
plate never showed, which is the documented Omni weak spot, and the sound alone
sells it.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off down the platform. She keeps walking toward the camera, still small in the frame. The overhead strip light flickers once and settles. Keep the blue dusk sky, the amber platform lights, the peeling green stanchions and the small Manhattan skyline on the horizon exactly the same. Wind, a fluorescent hum and a train passing somewhere out of frame, no dialogue. Use this image as the starting frame.
```

### 2f.8 The tram — January

**The rest beat, and the only clip where she barely walks.** The window does the
moving. Naming the sleeping passenger as still is the same trick §2d.2 used on the
standing statue: it stops the model animating the whole cabin.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off at the back of the cabin. The cabin sways gently and she rides it with one hand on the overhead pole, shifting her weight as it moves, while the bridge steel slides past the windows. The sleeping passenger does not stir. Keep the cold cabin light, the condensation on the glass and her dark overcoat exactly the same. Cable hum, a rattling cabin and muffled wind, no dialogue. Use this image as the starting frame.
```

### 2f.9 Central Park — the Mall

**Fire this one second.** She passes closest to the lens of any plate in the set,
in profile, so it is the identity test the same way 2f.6 is the register test. If
`@Karen` is ever going to be needed as a second ingredient, this is the clip that
proves it.

She exits and the empty path holds — nine months of walking, and the last thing
you see is where she was.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Locked off low at the edge of the path. She walks past the lens from left to right, her weight transferring foot to foot, and out of the right-hand side of the frame; the empty path holds after her. The elms move so the dapple shifts across the pavers. Keep the knee-height angle, the elm tunnel and the dappled path exactly the same. Leaves, birdsong, footsteps on stone and a distant city hum, no dialogue. Use this image as the starting frame.
```

### 2f.10 Fifth Avenue — through the cab window

The payoff, and the riskiest crowd in the set: dense, close, sunlit, walking toward
camera. **Her reflection in the wing mirror is in the preserve clause, not in the
action** — asking a video model to track a reflection through a moving mirror is
asking for complex physics, which is a named failure mode. Let it sit there and
survive.

```prompt
Create a 10-second 16:9 video, one continuous shot, no cuts, at real speed. Handheld from the back seat as the taxi rolls slowly forward, so the wing mirror drifts across the near foreground. She strides across the crossing in the crowd, half a pace ahead of everyone around her, and the crowd keeps moving past her. Keep the hard overhead summer sun, the yellow door frame, her reflection in the wing mirror and her cream blouse and tied cardigan exactly the same. Traffic, a horn and summer street noise, no dialogue. Use this image as the starting frame.
```

### Fire order

1. **2f.6 (Brooklyn Bridge) — the register test.** No face, one motion, all
   architecture. If the grade or the geometry comes back rebuilt, we know before
   we have spent anything.
2. **2f.9 (Central Park) — the identity test.** Closest pass to the lens. If she
   holds here, she holds everywhere, and `@Karen` stays in the drawer.
3. **2f.4, 2f.7, 2f.5, 2f.8, 2f.1** in any order — one figure, simple weather,
   no crowd close to the lens.
4. **2f.3 and 2f.10 late.** Dense crowds near the lens are where faces and hands
   go wrong, and 2f.10 also carries the reflection.
5. **2f.2 (Grand Central) last, and expect to lose it.** See its note. **Two
   regenerations, then stop** — the standing rule from §2c — and put the plate in
   the edit as a still with a slow push instead.

### What to watch, and what it would prove

- **Does Omni hold a photoreal plate, or re-style it?** Every §2b/§2d clip animates
  a flat graphic, where a re-style is survivable. Here the plate *is* the art
  direction. This set is the first real test of that.
- **Does the plate survive as ingredient, or does it need the Frames input?** The
  last line asks for first-frame behaviour in plain language; the ingredient path
  asks for reference behaviour. **If frame one comes back visibly redrawn, that is
  the `<FIRST_FRAME>` experiment finally becoming urgent** — type the tag and
  compare ([`omni-flash.md`](../../google-flow/omni-flash.md#the-first_frame-tag--a-documented-binding-mechanism-vendor)).
- **Does `at real speed` beat the slow-motion drift?** It is one phrase against a
  documented default. If clips still drift slow, the next lever is a timecode
  (`[0-10s]`), which §2d established parses and has never been used.
- **Does the long-exposure smear survive at all (2f.2)?** A clean no is a useful
  answer: it tells us which plates in future sets must stay stills.
- **Do the crowds stay whole?** 2f.3 and 2f.10 are the ones to watch, and the
  failure will be faces and hands, not composition.

### The edit these are for

Ten ten-second clips is a hundred seconds of walking, which is more than the song
has room for. **They are cut-in material, not a sequence** — the wide shots that
carry Act 2's nine-month clock between the illustrated title plates (§2a, §2c) and
the narrative scenes (§2.1–2.5). Three of them have a built-in out — 2f.4 stops,
2f.6 and 2f.9 exit frame — and those are the three worth cutting *on*.

---

## 2g. The river drop — moved out

**Act 1 §1.6, the phone in the water.** Written 2026-08-14, then lifted into its own
file so an unfired brief could never be mistaken for this ledger's verbatim record,
and so revising it cannot disturb anything here:

> **[`prompts-river-drop.md`](./prompts-river-drop.md)** — the two-shot (2g.1/2g.2),
> the drop rebuilt for Omni after a failed attempt (2g.3/2g.4), and a fallback that
> never renders the water at all (2g.5).

The engine findings that came out of it are in
[`docs/google-flow/omni-flash.md`](../../google-flow/omni-flash.md), not there and not
here — **negative prompts are unsupported and `no`/`don't` phrasing actively
backfires**, which bears on every unfired clip prompt above.

---

## 3. Gaps

- **Three prompts are missing.** The batch this file was opened from included
  three more pasted blocks that never arrived as text (18, 24 and 33 lines).
  Paste them and they get slotted into §2 against their scenes.
- **No output images are recorded here.** The prompts have no rendered frame
  filed next to them the way the character references do in
  [`characters/img/`](./characters/img/). If the accepted stills should live in
  the repo, say so and they get a `img/` folder and a per-prompt filename column.
- **No Flow project name.** The frontmatter `flow_project` is `TODO`, same as the
  Character tiles in [`characters/`](./characters/).
- **Video prompts are partly here now.** [§2b](#2b-video-prompts--gemini-omni-flash-not-yet-fired)
  covers the illustrated-register title sequence. The **super-8 register stills in
  §2.1–2.5 still have no clip prompts recorded.**
- **§2b is unfired.** Five briefs written but not yet run; they need replacing with
  what was actually typed, the same way §2.6 was.
- **§2c is 8 of 10 fired and accepted.** Still owed: **2c.7 (the earpiece grill)
  and 2c.9 (the manhole)**, without which the circle chain is four links, not six.
  The accepted eight are also **not yet recorded as images** — see the bullet above.
  The use-case and series clauses that were untested when written are now **fired
  and apparently working**; the palette held across eight generations.
- **§2d is unfired.** Nine clip briefs against the eight accepted plates. They carry
  one untested recipe change — **the guiding instruction moved to the last line** —
  so 2d.6 is a calibration run as much as a clip. Full set is ~270 credits.
- **§2e is fired but its record is stale.** Ten finished plates exist (they are the
  ten [§2f](#2f-clip-prompts-for-the-2e-walk-plates--gemini-omni-flash-not-yet-fired)
  clips), yet §2e still says `[not yet fired]` and still holds briefs rather than
  the words that were typed. **Two specific corrections are owed:** the civic
  colonnade (**2e.3**) has no plate, and there is an **eleventh location that was
  never in the shot list** — a snow-and-slush street with a scaffolding pipe across
  the frame, in which she wears the **cardigan with no coat despite the snow**, out
  of step with the wardrobe clock. Whoever fired them: paste the prompts and mark
  the section.
- **The `vibrant` / `restrained` collision is unresolved.** The §1 lock asks for a
  punchy vibrant palette; the anti-slop research says vivid colour words are what
  produce the plastic sheen. §2e resolves it *on paper* — vibrancy is the stock,
  restraint is the scene — but nothing has been fired to test it. If it loses, the
  **hex pin** is the lever, appended to one plate, **never written into the lock.**
- ~~**No clip prompts for §2e.**~~ **Written 2026-08-13 as
  [§2f](#2f-clip-prompts-for-the-2e-walk-plates--gemini-omni-flash-not-yet-fired)** —
  ten briefs, ~300 credits, unfired. They carry **three untested things**: a
  **photoreal** plate through Omni for the first time (§2b/§2d are all flat
  graphics), the **ingredient** path rather than Frames, and the new live-action
  clauses (`at real speed`, named weight transfer, one named ambient motion). **2f.6
  fires first** as the register test, **2f.9 second** as the identity test.
- **The §2e plates are still not filed as images.** Ten frames now exist outside
  the repo with nothing next to their prompts. This is the same gap as §2a and §2c,
  now three sets deep, and §2f makes it worse: a clip brief that cannot be checked
  against its own plate is half a record. Say the word and they get an `img/`
  folder and a per-prompt filename column.
- **§2g is unfired, and lives in [`prompts-river-drop.md`](./prompts-river-drop.md).**
  The Act 1 river drop — a two-shot (2g.1/2g.2), the drop rebuilt for Omni after a
  failed attempt (2g.3/2g.4), and a no-physics fallback (2g.5). Three untested
  things: **`@Karen` and `@Susan` bound in the same frame**, which no plate has ever
  asked for; **Susan's clean e-commerce references under a super-8 night grade**, the
  sharpest available test of the divergence flagged in
  [`characters/susan.md`](./characters/susan.md); and **the falling-light idea**,
  which is the whole bet on 2g.4. Firing 2g.1 answers the Susan ruling on its own,
  and 2g.4 needs no Characters so it can go first.
- **⚠️ Every unfired clip prompt above is suspect on negations.** §2g's post-mortem
  established — now recorded in
  [`omni-flash.md`](../../google-flow/omni-flash.md#prompt-craft-what-a-failed-shot-taught-us) —
  that Omni supports **no negative prompts at all** *and* that `no`/`don't` phrasing
  is counter-recommended, because the tokens land as content. **§2b, §2d and §2f were
  written before we knew that** and lean on `no cuts`, `no dialogue`, `does not turn`.
  `no dialogue` is probably harmless (it is the vendor's own documented phrasing), but
  **`the Wonder Wheel does not turn` in 2f.5 is exactly the shape that backfires.**
  Nothing should be rewritten on theory — but whoever fires that set first should
  watch for the named-and-negated thing showing up anyway, and if it does, the fix is
  a positive restatement (*"the Wonder Wheel stands still"*).
- **The `<FIRST_FRAME>` tag is untested in Flow.** Documented API syntax that binds
  an image to the starting-frame role; whether it does anything typed into Flow's
  prompt box is unknown, and the answer matters well beyond Karen — see
  [`omni-flash.md`](../../google-flow/omni-flash.md#the-animate-slide-problem).
- **The hex-pinned palette is untested.** Proposed in §2c as the candidate fix for
  the §2a.4 drift, deliberately *not* written into the §1b lock. Somebody needs to
  run it on one plate and compare before it goes anywhere near the canonical block.
- **No images filed for §2a.** Four accepted stills with no frame next to the
  prompt — same gap as the bullet above, now with four more entries.
- **The §2a.4 palette drift is unresolved** — that plate came back warmer and more
  saturated than its three siblings and will show if they cut together.
- **The §1b casting override is owed a ruling.** The illustrated register
  contradicts the no-prose-faces rule in
  [`characters/karen.md`](./characters/karen.md), for a stated reason. Kai or Jack
  needs to confirm or reject it.
