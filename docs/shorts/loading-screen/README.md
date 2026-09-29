# Loading Screen — illustrated cover → the real thing

> **Status 2026-09-14:** concept picked, pilot is **camping / Tarquin**. **V1 is built:** 8s, 16:9, the ink page (Omni) → a 3D page flip → the real `20.mp4`. Render: `Camping Comic/shorts/loading-screen/renders/v1-loading-screen.mp4`. Awaiting Jack's review.
> Asked for by Jack: *"a gta 4 like comic book video, where you flip through the characters and or
> pages, then it turns into the realistic style, like Tarquin in the waitrose car park and Karen in
> the phone booth… make shorts out of all of the videos."*

## The concept

A vertical short (9:16, 15–40s) that opens on **late-2000s game loading-screen illustration**:
ink, flat colour, overcast and desaturated, stern faces. **Two or three illustrated pages flip past:**
the character, the place, and the thing he owns. Then the last page **match-cuts into the real
footage in the same framing**, and the short runs as live action.

**Why this direction is fresh.** The trend on TikTok and CapCut goes *photo → game art*: upload
a selfie, get a loading screen. **We run it backwards: game art → real.** The joke lands on the cut:
*this isn't a game, and he isn't a character.*

**Why it survives Flow's weak consistency:** 🔑 **no page is invented from nothing.** Every
illustration is a **restyle of an accepted still we already own** (`images/N.jpeg` behind each
clip), attached as the single reference. The likeness, the set and the framing come from our own
photograph, so the model only has to change the *medium*. One image per page, one reference per
image, no Flow Character needed (Character casting is unmapped on the rebuilt Flow anyway).

## Research this rests on (2026-09-14)

Three web passes this session; the Nano Banana findings extend
[`docs/google-flow/nano-banana-2.md`](../../google-flow/nano-banana-2.md).

**The look.**
- The GTA IV cover and loading art is by Stephen Bliss with Anthony Macbain.
- Heavy black contour lines, flat colour with hard shadow edges, and a photo-real base.
- A **desaturated overcast palette** (grey and brown), nobody smiling, the figure mid-situation.
- The cover is a thin-gutter panel grid whose horizontal dividers tilt up to ~7°.
- ⚠️ **No source supports halftone dots for IV**, so they are left out of the prompts.
- ⚠️ Bliss's actual process is undocumented.

**The format.** Hook inside 2–3s, and the art frame should already be moving at 0s. The vendor
drop-off figures are indicative, not cited.

**Legal.** Style is not ownable (UK CDPA s30A pastiche; *Lohan v Take-Two*), but Take-Two does
enforce marks. 🔴 **Never on screen or in a prompt:**
- "GTA" or "Grand Theft Auto"
- the R\* logo
- the IV lockup
- Pricedown lettering
- the exact "Wasted" or "Mission Passed" graphics

Use another heavy condensed face for titles. Not legal advice.

**Anti-slop, for ink.**
- Name the physical process: brush and india ink, cheap matte print.
- Ask for **line weight that varies by depth**, heavier on the outer contour.
- Make shadows **solid black shapes**, not smooth grey gradients.
- Use a restricted palette with one muted accent.
- Keep out "cinematic", "masterpiece", "trending" and Google's own teal example.

## The pilot: camping, Tarquin

| Page | Restyled from | What it is |
| --- | --- | --- |
| **P1** | `images/20.jpeg` (clip `20.mp4`, `8c(ii)`) | Tarquin by the open car door in the rain. **Match-cuts into `20.mp4`** |
| P2 | `images/19.jpeg` (clip `19.mp4`, `8c(i)`) | Bob in the tent mouth *(not yet written)* |
| P3 | `images/17.jpeg` (clip `17.mp4`, `8b`) | The car and the tent across two bays *(not yet written)* |

Order in the cut is decided in the edit, not here.

**🔴 Needs a human, known now:**
- Title text, whether "TARQUIN" or a mission-style card, is a hand job. The Premiere API cannot
  write text, and ffmpeg is not installed in WSL.
- The page flip is a Premiere transition, picked by eye.

### P1 — shot spec (shot-craft, Design mode)

- **Job:** the hook. Present him as a game character, the illustrated twin of a real frame, so the
  cut to live action is the reveal.
- **Register:** illustrated loading-screen poster, overcast and desaturated. It deliberately breaks
  the house photographic register, and only for the first seconds.
- **Depth:**
  - midground: him, standing by the open driver's door
  - background: the black car body, with flat pale sky above it
  - foreground: none, because the 9:16 crop loses Bob's shoulder. The cost is carried by P2 (Bob),
    not this page.
- **Focal point:** his face, winning on contrast against the pale sky and on height in the frame.
- **Light:** flat overcast daylight from the sky, rain falling. The car is the one big solid-black
  mass, and the face is the brightest skin in frame.
- **Camera:** as in the photograph, low eye level (a seated man's height), looking slightly up, on
  a moderate telephoto. Recomposed as a tall vertical, head to knee.
- **Withheld:** Bob. We see only what Tarquin is looking down at later.
- **Moves:** nothing in the image. A slow push in post, then the cut.

### P1 — prompt, round 1 · Nano Banana 2 · 9:16 · ref `20.jpeg` · x2

**Box: Flow → prompt box (reference `20.jpeg` attached as the only ingredient)**

```
Redraw the attached photograph as a hand-inked video-game loading-screen illustration from the late 2000s, recomposed as a tall 9:16 vertical poster.

Reference: the attached photograph is the only source for the man, his clothes, his pose, his expression, the open car door and the rainy car park. Keep all of those exactly as they are in the photograph. Change only the medium and the framing.

Framing: a tall vertical crop centred on the man, from just above his head to just below his knees, with the open driver's door and the dark flank of the car filling the space behind him and a strip of pale overcast sky above. The camera stays where the photograph's camera is, low and looking slightly up at him.

Medium: drawn from the photograph with a brush and india ink on board. Confident black contour lines, heaviest on the outer edge of his figure and the car, thinner on the folds of the quilted gilet and the creases of the jeans, with small dry-brush breaks where the line thins. Shadows are solid black shapes with hard edges. Colour is laid flat in two or three tones per surface over the ink, printed on matte paper with a faint paper tooth.

Palette: desaturated and overcast: slate grey sky, blue-grey wet tarmac, near-black car, olive-brown gilet, faded denim. The one accent is the dull red of the car's tail light.

Light: flat grey daylight from the overcast sky, fine rain falling as thin pale ink strokes, the car's body the largest solid black mass, his face the brightest skin in the picture.

Constraints: the illustration runs full-bleed to all four edges. The car's badge is a plain dark shape. His expression stays exactly as small as it is in the photograph.

Thanks.
```


### 🔁 Jack, 2026-09-14: *"do it all in 16:9, do b, and make 1 video out of it with Omni Flash, with a comic book page turn transition."*

So the format changes from vertical Short to **16:9**, the look is candidate **`b`** (slate sky,
paper texture, dry-brush line), and the deliverable is **one video**. At 16:9 the photograph's full
framing survives, **so Bob's blurred shoulder comes back into the foreground**. That restores the
depth layer and the visible cost that the vertical crop had lost.

### P1 — prompt, round 2 · Nano Banana 2 · 16:9 · ref `20.jpeg` · x2

Round 1's prompt, with three changes: the framing is now the photograph's own, `b`'s qualities
(slate sky, paper tooth) are stated rather than hoped for, and the foreground shoulder is named.

**Box: Flow → prompt box (reference `20.jpeg` attached as the only ingredient)**

```
Redraw the attached photograph as a hand-inked video-game loading-screen illustration from the late 2000s, in the same 16:9 landscape framing as the photograph.

Reference: the attached photograph is the only source for both men, their clothes, the standing man's pose and expression, the open car door and the rainy car park. Keep all of those exactly as they are in the photograph, in exactly the same positions in the frame. Change only the medium.

Framing: identical to the photograph. The seated figure's out-of-focus shoulder and back fill the left foreground as one large soft dark shape, the standing man is right of centre by the open driver's door, and the long dark flank of the car runs behind him under a wide band of overcast sky.

Medium: drawn from the photograph with a brush and india ink on board. Confident black contour lines, heaviest on the outer edge of the standing man and the car, thinner on the folds of the quilted gilet and the creases of the jeans, with small dry-brush breaks where the line thins. Shadows are solid black shapes with hard edges. Colour is laid flat in two or three tones per surface over the ink, printed on matte paper whose tooth shows through the flat colour, most visibly in the sky.

Palette: desaturated and overcast: a slate grey sky, blue-grey wet tarmac, a near-black car, an olive-brown gilet, faded denim, and a dull brown coat on the foreground figure. The one accent is the dull red of the car's tail light.

Light: flat grey daylight from the overcast sky, fine rain falling as thin pale ink strokes, the car's body the largest solid black mass, the standing man's face the brightest skin in the picture.

Constraints: the illustration runs full-bleed to all four edges. The car's badge is a plain dark shape. His expression stays exactly as small as it is in the photograph.

Thanks.
```

### The video — how it is built, and why not all in one Omni generation

**Research, 2026-09-14:** nobody has documented a convincing AI-generated paper page turn in any
model (Veo, Omni, Kling, Runway). Omni 1.1 Flash *does* take start and end frames now; the old
"rejects a last frame" rule dates from 1.0. But an ink start frame and a photo end frame are as
different as two frames get, and the documented failure is **a soft morph or crossfade, not
paper physics.** Our own standing rule already says pinned end frames morph. So the one video is
built in the house hybrid layers:

| Layer | Tool | What |
| --- | --- | --- |
| 1 | **Omni 1.1 Flash**, Frames, start = `p1-169-r2-b` | **The ink page comes alive**: rain falls in ink strokes, he breathes and blinks, the lines stay drawn. 6s, locked camera |
| 2 | **Real footage we already own** | `new clips/20.mp4`, the same shot live. It is the reveal |
| 3 | **Premiere** | **Page Turn** transition from 1 into 2 (exact paper geometry, eased), a slow push on the ink page before it, and a paper-turn sound |
| *(optional)* | Omni, start = ink, **end = `20.jpeg`** | One test of Omni doing the turn itself. Needs a Flow-tool guard change and one reconnect. Expect a morph |

### V1 — shot spec (shot-craft)

- **Job:** make the drawing breathe just enough that the viewer accepts it as a *world*, so the turn
  to the real one lands as a reveal, not a slideshow.
- **What moves in the world:** rain, one breath, one blink, a small hand flex, and the coat of the
  foreground figure as he breathes. **Nothing else.** A still that truly holds reads as a scan, and
  too much motion stops it reading as a drawing.
- **Camera:** does not move. The push is added in post (hybrid method).
- **Sound:** rain on the car roof and wet tarmac. The page-turn sound belongs to the edit, not to
  this clip.

### V1 — motion prompt · Omni 1.1 Flash · Frames (start only) · 16:9 · 6s · x1

**Box: Flow → prompt box, with `p1-169-r2-b.jpeg` in the Start frame slot**

```
The attached image is the first frame of this shot, and the picture stays a hand-inked drawing for the whole shot, every line crisp black ink and every colour flat. The camera does not move. At real speed, fine rain keeps falling as thin pale ink strokes and splashes on the dark car roof, the standing man breathes and blinks once, and the fingers of his right hand flex slightly at his side. The foreground figure's coat rises and falls with his breathing.
Audio: steady rain drumming on the car roof and the wet tarmac, and distant traffic. No music and no voices.
Thanks.
```

## Revision log

| Page | Round | Model | Result | Verdict |
| --- | --- | --- | --- | --- |
| P1 | 1 | Nano Banana 2 · 9:16 · x2 · Flow project `42ec9ea3…` (`Sep 14 - 18:30`) | `Camping Comic/shorts/loading-screen/stills/p1-r1-a.jpeg`, `-b.jpeg` (768×1376, "Original size") | **Both hold the likeness, the pose and the door exactly.** `a` is clean flat colour with a pale blue sky (reads more webcomic). `b` is grittier: a slate sky, paper texture and dry-brush breaks (closer to the overcast IV register). Line weight is still fairly even in both, and neither puts solid black on the face. **Jack picked `b`**, then asked for everything in 16:9 |
| P1 · 16:9 | 2 | Nano Banana 2 · 16:9 · x2 · same project | `p1-169-r2-a.jpeg`, `-b.jpeg` (1376×768) | Both match the photo's framing, and Bob's shoulder is back. `a` grew a painted horizon band across the sky. **`b` taken as the plate:** clean slate sky, red tail-light accent, paper tooth. ⚠️ A faint "X8"-like badge is still legible on the wing |
| V1 clip | 1 | **Omni 1.1 Flash** · Frames (start = `p1-169-r2-b`) · 16:9 · 6s · 720p · x1 · Flow project `073c8423…` (`Sep 14 - 19:01`) | `clips/v1-ink-page.mp4` (1280×720, 24fps, with audio) | ✅ **Stays a drawing for all 6s.** Face stable, rain falls, one breath and blink. ⚠️ Omni smoothed away most of the plate's paper tooth. ⚠️ A pale vertical streak runs near his left hand late in the clip |
| V1 edit | 1 | ffmpeg, `build-v1.sh` (not Premiere: the bridge panel was closed) | `renders/v1-loading-screen.mp4` (1920×1080, 24fps, 8.00s, bt709 tagged) | Looked at on 10fps and 8fps contact sheets of the turn. The page swings off its left edge toward camera, shades, catches light, shows a paper edge and casts a shadow, revealing the real frame. The reveal lands at 4.5s |

### V1 — the edit as built (`build-v1.sh`)

| Time | Picture | Sound |
| --- | --- | --- |
| 0–3.5s | `v1-ink-page.mp4`, upscaled 1280→1920 (lanczos) | Omni's rain |
| 3.5–4.5s | **Page flip**, eased: hinged on the left edge, 0→90°, with perspective (F=2.2 page widths). Shading `−38%` as it lifts, a light sheen, a paper-edge line and a cast shadow on the real frame | Rain crossfades into `20.mp4`'s own audio. **Paper swish** synthesized from pink noise (1.4–7.5 kHz, 100ms attack) at 3.55s |
| 4.5–8s | `new clips/20.mp4` from its first frame (the plate `20.jpeg` is that frame, which is why the two line up) | `20.mp4` audio |
| 0–8s | **One slow push, 100→105%**, on the finished composite so both worlds share one camera | |

**Rebuild:** `SP=<scratch> FF=<ffmpeg> INK=<v1-ink-page.mp4> REAL=<new clips/20.mp4> docs/shorts/loading-screen/build-v1.sh <out.mp4>` (~50s on this machine).

**Needs a human / not done**
- ⬜ **Watch it at speed**, especially the turn at 3.5–4.5s and the swish.
- ⬜ **The swish is a placeholder** built from noise. A real recorded page-turn sound will be better.
- ⬜ **The real side is ungraded** `20.mp4` (bright white sky), so the reveal is a hard jump from slate to bright. That may be the point, or the camping grade could be applied.
- ⬜ **Alternative turn:** Premiere's built-in **Page Turn** (a true corner curl) once the BadCode Bridge panel is reopened.
- ⬜ **Untested option:** Omni doing the turn itself (start = ink, end = `20.jpeg`). It needs the Flow tool's stale "Omni rejects a last frame" guard removed (Omni 1.1 has end frames) and one `/mcp` reconnect, after killing the old server first (law 22). Research expects a morph.
- ⬜ **`scripts/delivery-qc.sh` not run.** There is no ffprobe here, only a scratch ffmpeg.
