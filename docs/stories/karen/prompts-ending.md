---
story: karen
kind: brief — fired by hand in Flow; each block is the deliverable
engine: Nano Banana 2 (stills) → Omni Flash (clips)
updated: 2026-10-19
---

# Karen — the new ending (beat 10)

Jack, 2026-10-19: after AI Sean's card (4.3d), the sacked President rings Karen, then a cut to Tarquin in the
Shard, then *To be continued*. Both clips are **muted**; the lines are dubbed in AI Studio
([`narration/script-v2-brief.md`](./narration/script-v2-brief.md) beat 10, voices in
[`narration/profiles/`](./narration/profiles/)). Stills first, one at a time; then the clips.

| Shot | Line (dubbed) | Voice |
| --- | --- | --- |
| **10a** the President | *"Karen, let's get this A.I. mess sorted out. I'm going to put you in touch with my guy in England. He can pull a few strings."* | Alnilam, `president-alnilam.md` |
| **10b** Tarquin | *"Karen, is that you? I have an urgent message for you. For fuck's sake, listen. I have seen what happens if we do not take action... Christ, are you even there?!"* | Zubenelgenubi, `tarquin-urgent-zubenelgenubi.md` |
| **10c** card | *To be continued* | — (ffmpeg, Premiere cannot set text) |

## The two shots are a rhyme

**Both men are seen from behind, at a night window, phone to the ear.** Same grammar, two countries: the cut
says *these two are now on the same line* without a word, and it means no mouth is ever on screen, so a dub can't
be visibly out of sync (the failure in the Bank Robbery cuts). Canon already wants the President unseen: *"a
silhouette in a suit"* ([`prompts-act4-manager.md`](./prompts-act4-manager.md) ruling 2).

### 10a spec — the President

- **Job:** the man with no manager above him, now with no job, needing the woman in the phone box. The ladder
  turned upside down.
- **Register:** human-scale, the Act 4 world (warm, interior, expensive) emptied out.
- **Visible cost:** the redundancy box. A cardboard box of his desk things in the foreground, the same object
  every sacked office worker carries out. Karen's firing, his size.
- **Depth:** box (foreground, soft) · his back at the window (mid) · a city at night, out of focus (back).
- **Focal point:** his silhouette against the city lights, won by contrast.
- **Light:** one warm desk lamp behind him across his back; the cold city glow through the glass. The rest dark.
- **Camera:** waist height, low, behind and a little to one side, looking past him at the window.
- **Withheld:** his face. No flags, seals, office of state: he is *a man in a dark suit*.
- **Moves:** in the clip, only him: the free hand pressed on the glass, head bowing. Camera locked.

### 10b spec — Tarquin

- **Job:** the cut to London, a new world, and the first time Tarquin is frightened. The network widens.
- **Visible cost:** his own fear, in a room built to make him feel untouchable; papers spilled across the floor.
  (No condition description of him: `@Tarquin` is attached, so position, action and expression only.)
- **Depth:** the spilled papers and his chair (foreground) · Tarquin at the glass (mid) · London at night far
  below (back).
- **Focal point:** his reflection in the glass, worried, faint over the city.
- **Light:** the city below and one desk lamp; same two sources as 10a, so the rhyme holds.
- **Camera:** behind and to one side, a little higher than 10a (he is the one who has seen further).
- **Withheld:** his direct face; we read his expression in the reflection only.

## 10a — still

Commentary: if you have an accepted still of the man in the dark suit from Act 4, attach it as the reference and
delete the subject's age and suit from the prompt (a referenced character is never described).

**Settings:** Nano Banana 2 · landscape · x2
**Attach:** nothing (or the Act 4 man in the dark suit, see above)
**→ Flow image · prompt box**

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

SCENE:

Subject: a man in his sixties in a dark suit, seen only from behind, standing alone at a tall window at night with a phone held to his ear.

Composition: 16:9 on a 35mm lens at f/2.8, camera low at waist height, behind him and a little to the left, looking past his shoulder at the window. In the near foreground, out of focus, the corner of a desk with a cardboard box on it holding a few books, a mug and a framed photo lying face down. His back and shoulders fill the middle of the frame. Through the glass, a city at night, its lights soft and out of focus.

Action: he stands still, one hand pressed flat against the glass, the other holding the phone to his ear, his head bowed a little. His face is not visible.

Location: an ordinary modern office after hours, the desk cleared, the chair pushed back, nothing on the walls.

Light: a single desk lamp behind the camera throws warm light across his back and shoulders; the cold glow of the city comes through the window; the rest of the room falls away into shadow.

Style: a still from a 35mm independent film — a powerful man with nowhere left to go. Available light only, unretouched.

Constraints: a fictional man, do not resemble any real person; his face is never shown; no flags, seals, emblems or insignia; no readable lettering anywhere, including on the box and the books; no border or frame edge around the image.

Thanks.
```

## ✅ BUILT 2026-10-19

The 10a still prompt above was revised before firing (one key light; the city "too weak to light anything"; a dried coffee
ring; a lens vantage point; the connotation line removed), and 10b written the same way, casting `@Tarquin` (Camping project
`9b729074`). All Nano Banana 2, two candidates each; video on Omni Flash, one fresh Flow project per shot (`a99c9e72`, `09844f55`).
Files: `Karen VID NEW!\clips\ending\` (takes) and `…\final\` (on the timeline).

| Shot | Kept | Why | Motion prompt (summary) |
| --- | --- | --- | --- |
| 10a still | `10a-still-b` | box occludes the foreground, off-centre, phone clearly at the ear; `-a` centred, both hands at his head | — |
| 10a clip | `10a-president-b` (8 s) | phone stays at the ear; in `-a` it vanishes for a moment | drops the hand from his neck, weight shift, two nods; camera locked; office tone, a distant siren; no dialogue |
| 10b still | `10b-still-b` | matches `@Tarquin`'s sheet (green leather jacket, jeans, boots); worried face in the glass | — |
| 10b clip 1 | `10b-tarquin-1-b` (8 s) | ends with him lowering the phone to stare at it | presses the phone harder, hand slides down the glass, leans in; wind, office hum |
| 10b clip 2 | `10b-tarquin-2-a` (6 s, chained from 1-b's last frame) | jams the phone back and fists the glass | stares at the phone, back to the ear, one strike on the glass; the thud |

`final/10b-tarquin.mp4` = 1-b + 2-a (first frame of 2-a dropped), 13.97 s.

## ✅ REBUILT 2026-10-19 (evening), Jack's notes: the real President, Tarquin's face

| Shot | Kept | Prompt (summary) |
| --- | --- | --- |
| 10a2 still | `10a2-still-a` | `flow_edit_image`, NB2, reference = a frame of `37.mp4` (the President in the guest chair, from behind): same man, chair, angle and set, an hour after the show; studio dark but one work lamp; host's chair empty; monitor showing static; coffee cup and cable on the floor; a mobile at his ear; face away |
| 10a2 clip | `10a2-president-a` (8 s) + `10a2-president-2-a` (4 s, chained) | leans forward, elbow on knee, listening, one nod; then sits back and rubs his forehead; phone at the ear throughout; studio hum, static hiss |
| 10b2 still | `10b2-still-a` | `@Tarquin`, chest-up, face three-quarter to camera, 50 mm from just below eye line, lamp from the side, sweat sheen, Tower Bridge behind; "the phone is a plain dark smartphone held firmly against his ear" |
| 10b2 clip 1 | `10b2-tarquin-1-b` (8 s) | Frames, exact line: *He says: Karen, is that you? I have an urgent message for you. For fuck's sake, listen.* |
| 10b2 clip 2 | `10b2-tarquin-2-b` (8 s, chained) | exact line: *I have seen what happens if we do not take action. Christ, are you even there?* (harvested by hand with `scripts/flow/.tmp/grab-videos.mjs`, the tool's tile wait timed out twice) |

Both Tarquin clips say the exact words (checked by transcription) and keep the phone at his ear in every frame. They are muted
on the timeline; his line is dubbed from `t01-tarquin-a.wav`.
