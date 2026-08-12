---
story: karen
kind: record — prompts typed into Flow by hand, not a generation brief
flow_project: TODO — exact project name as it appears in Flow
updated: 2026-08-11
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

### 2.6 Karen at the jazz club bar — illustrated register `[not yet fired]`

**Written 2026-08-12, not yet generated.** The first prompt in the
[§1b illustrated register](#1b-the-illustrated-register--karens-second-style-lock),
and the only block in this file that is a **brief rather than a record** — it is
here so it can be fired, judged and then rewritten as what was actually typed.

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
- **Video prompts are not here.** Several of these stills become clips; that step
  has no ledger yet.
