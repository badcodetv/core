# Post-production — the other half of every shot

**Flow is not the whole pipeline. It is the half that invents.** The other half is `ffmpeg`, and
it is where anything that must be *exact* belongs.

Established 2026-08-21, after the GPOM scene-0 shoot spent a day discovering it the expensive way.
Every command below has been run on real BadCode footage — nothing here is copied from a blog.

---

## 1. The decision, before you spend a credit

> **Does anything in the world actually move?**
> Cloth, water, smoke, a crowd, a machine turning, a face — or only the camera?

| Answer | Lane |
| --- | --- |
| Something in the world moves | **Veo.** That is what it is for, and it is very good at it |
| **Only the camera moves** | **Post.** It is a scale-and-crop on one image, and Veo can only make it worse |

**This is not a fallback, it is a first choice.** On a camera-only move, post beats Veo on every
axis at once:

| | Veo | `ffmpeg` |
| --- | --- | --- |
| Artefacts | hinging, join creep, morphing, invented components | **none possible** — it is one image |
| Rigidity | see [`video-prompting.md`](./video-prompting.md) §4 — not achievable with a pinned end frame | **perfect, by construction** |
| Length | 8s hard cap | **any** |
| Ease curve | whatever it feels like | **exact** |
| Cost | 10–100 credits per attempt | **free, seconds** |
| Iterations | one wait per try | instant |

The one thing Veo wins is **resolution headroom** — see §4, and it is a real constraint.

## 2. Ask the third question too: can Veo do the *inverse*?

The scene-0 breakthrough. If Veo refuses to do a move, check whether it will do the **opposite**
move — because `ffmpeg` can reverse it for free.

Veo could not hold a rigid subject through a pull-back when the destination was pinned as an end
frame ([`video-prompting.md`](./video-prompting.md) §4). It *could* hold one on a push-in from a
single start image. So: shoot the push-in, reverse the clip, and you have a rigid pull-back that
lands exactly on your art-directed plate.

**Generalise it.** Before concluding a shot is impossible, ask:

- Can it be shot **backwards** and reversed? (reveals, pull-backs, assembling/disassembling)
- Can it be shot **slower or faster** and retimed? (§3.7)
- Can it be shot **wider** and cropped in? (framing you could not get)
- Can it be shot **shorter** and looped? (§3.3)
- Can it be shot as **two clips** and joined? (§3.6)

⚠️ **A reversed clip only reads correctly if nothing physical moves.** Dust settling, sparks,
smoke, drifting debris and flickering all read as running backwards. Blinking lights are safe —
they are time-symmetric. Say the air is empty in the prompt.

## 3. The recipe book — all tested on BadCode footage

### 3.1 Strip audio — do this to everything

Veo's audio cannot be disabled and BadCode's track comes from Suno.

```bash
ffmpeg -i in.mp4 -c:v copy -an out.mp4
```

`-c:v copy` means no re-encode: instant, lossless.

### 3.2 Reverse a clip

```bash
ffmpeg -i in.mp4 -vf reverse -an out.mp4
```

### 3.3 Seamless loop by ping-pong

For a plate that must run under narration of unknown length. Forward then backward, so the join is
invisible and no frame-matching is needed. **Doubles the duration** (8s → 16s), and the result
loops cleanly end-to-end.

```bash
ffmpeg -i in.mp4 -filter_complex \
  "[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,setpts=PTS-STARTPTS[v]" \
  -map "[v]" -an -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
```

### 3.4 Eased camera move on a still — the workhorse

Cosine ease-in-out, so it accelerates and settles like a real dolly rather than sliding linearly.
**Pre-scaling to ~4× the output width before `zoompan` is what removes its integer-rounding
jitter** — without that line the move stutters.

```bash
# 12s eased PULL-BACK, 2.5x -> 1.0x, 25fps (300 frames; the 299 below is frames-1)
ffmpeg -loop 1 -i still.jpg -t 12 -r 25 -vf \
 "scale=5120:-2:flags=lanczos,\
zoompan=z='2.5-1.5*(1-cos(PI*on/299))/2':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1280x720:fps=25,\
format=yuv420p" \
 -c:v libx264 -crf 18 out.mp4
```

- **Push-in instead:** swap the `z` expression to `1+1.5*(1-cos(PI*on/299))/2`.
- **Linear instead of eased:** `z='2.5-1.5*on/299'`. Eased almost always looks better.
- **Off-centre target:** replace the `x`/`y` expressions; they currently centre the crop.
- **Different length:** frames = seconds × fps, and the `299` becomes frames − 1.

Renders a 12s 720p move in about 5 seconds.

### 3.4b Break the 8s cap: chained push-ins, reversed

**The move that beats Veo's hard cap and its inability to take a destination.** Proven on GPOM
scene 0, 2026-08-21: a 16s continuous rigid pull-out landing frame-exact on an art-directed plate.

Veo cannot be told where to *end* without Frames mode, and Frames mode interpolates (§ and
[`video-prompting.md`](./video-prompting.md) §4). Post cannot cover a big scale change either —
see §4. So invert it:

1. Shoot a push-in **from** the frame you want to arrive at. Start-image-only, no end frame.
2. Take that clip's last frame; shoot the next push-in from it. Repeat for as much magnification
   as you need — each stage starts from a real frame, so each one stays rigid.
3. Reverse each stage and concatenate **in reverse order**.

```bash
# stage 2 first, then stage 1 -- each reversed
ffmpeg -i push2.mp4 -vf "reverse,format=yuv420p" -an -c:v libx264 -crf 18 -y r2.mp4
ffmpeg -i push1.mp4 -vf "reverse,format=yuv420p" -an -c:v libx264 -crf 18 -y r1.mp4
ffmpeg -i r2.mp4 -i r1.mp4 -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 -pix_fmt yuv420p -crf 18 -y pullout.mp4
```

**Two bonuses.** N stages gives N×8 seconds of unbroken move. And the deepest stage's last frame
is a free, perfectly-matched anchor for a locked-off plate at that magnification — so the opening
hold joins the pull-out invisibly.

⚠️ Same reversal caveat as §2: forbid smoke, dust, sparks and drifting particles in the prompt, or
they read as running backwards. Blinking lights are safe.

### 3.5 Pull the last frame out of a clip

Chaining without opening the browser. (`flow_scene_save_frame position:"end"` does the same thing
inside Flow and lands the frame in the project — use that when the next generation needs it as an
asset; use this when you just need the file.)

```bash
ffmpeg -sseof -0.05 -i in.mp4 -update 1 -frames:v 1 -q:v 2 lastframe.jpg
```

### 3.6 Join clips

Re-encoding is the safe default — Flow's clips are uniform, but `concat` demuxer stream-copy
fails silently on any mismatch.

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
```

#### 🔴 Normalise fps and SAR BEFORE concat, or it runs away

**Veo returns 24fps. Every clip `ffmpeg` builds from a still defaults to 25fps.** Mix the two in
the `concat` *filter* and it does not error — it produces an ever-growing file that never
terminates. Measured on the GPOM scene-1 rough cut, 2026-08-21: a 23-second sequence reached
**628MB and 105 minutes of CPU** before it was killed, while every one of its five inputs was
correct and under 4MB.

Flow's own clips are uniform with each other, so this only bites once you start mixing generated
video with post-built plates — which is exactly what a finished scene is.

There is a second, quieter mismatch in the same family: `concat` also refuses inputs whose sample
aspect ratios differ (`SAR 0:1` vs `SAR 8778:8777`), and *that* one does error, immediately and
legibly. It is the good version of the same bug.

**Fix both at the source.** Put `fps=<N>,setsar=1` in every clip's filter chain as you build it,
pick the rate your generated footage already uses (24 for Veo, so the real footage is never
resampled), and then the concat **demuxer** with `-c copy` will join them in a second flat:

```bash
# build each piece with the SAME fps and SAR
ffmpeg -i veo.mp4 -vf "scale=1280:720,fps=24,setsar=1,format=yuv420p" -an -c:v libx264 -crf 20 -y q1.mp4
ffmpeg -loop 1 -i still.jpg -t 3 -vf "scale=1280:720,fps=24,setsar=1,format=yuv420p" -c:v libx264 -crf 20 -y q2.mp4

# then join with the DEMUXER, no re-encode
printf "file 'q1.mp4'\nfile 'q2.mp4'\n" > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy -y out.mp4
```

⚠️ **`-c copy` here is safe only because the pieces were built identically** — same codec, size,
fps, SAR and pixel format. That is the point of normalising at build time rather than at join
time. If you did not build them, re-encode.

### 3.7 Retime

Buys length out of the 8s cap when the move is too fast. `minterpolate` synthesises intermediate
frames rather than duplicating them.

```bash
# 8s -> 13.2s (60% speed)
ffmpeg -i in.mp4 -vf "setpts=PTS/0.6,minterpolate=fps=25:mi_mode=mci" -an -c:v libx264 -crf 18 out.mp4
```

⚠️ `minterpolate` is slow and can smear on fast or complex motion. Check a frame. On a slow rigid
move it is clean.

### 3.8 Crop off a stray burned-in subtitle

The escape hatch from [`failure-modes.md`](./failure-modes.md) — which is why dialogue clips should
be framed with dead space at the bottom.

```bash
ffmpeg -i in.mp4 -vf "crop=iw:ih*0.85:0:0,scale=1280:720" -an -c:v libx264 -crf 18 out.mp4
```

### 3.9 Contact sheet for review

**Look at frames. File size proves nothing.** This is how every verdict in the scene-0 shoot was
reached — six frames across the clip, tiled, in one image.

```bash
for t in 0 1.5 3 4.5 6 7.9; do
  ffmpeg -v error -ss $t -i in.mp4 -frames:v 1 -vf "scale=440:-1" -y /tmp/f-$t.png
done
ffmpeg -v error -i /tmp/f-0.png -i /tmp/f-1.5.png -i /tmp/f-3.png \
       -i /tmp/f-4.5.png -i /tmp/f-6.png -i /tmp/f-7.9.png \
  -filter_complex "[0][1][2][3][4][5]xstack=inputs=6:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0" \
  -y sheet.png
```

`scripts/video-contact-sheet.sh` wraps this with a `REGION` crop and an exposure lift for
near-black frames.


## 3.9 🔴 Hold a Veo clip's colour — and anchor on a PERCENTILE, never the mean

**Every Veo clip drifts.** Measured across six clips on GPOM cut 3, 2026-08-21: an exterior
flight brightened 177 → 200 over 8s, one station take *darkened* by 15, a row take brightened by
13. It is always smooth and monotonic, never a jump — which is why it is correctable, and why it
is easy to miss by eye until two clips are cut together and the join flashes.

**Tool: `docs/stories/gitpush-origin-master/scenes/hold_grade.py`** (clip in, 1080p clip out).

🔴 **The trap, and the first version fell straight into it.** Anchoring on the frame **mean**
measures *what is in shot*, not *how the shot is lit*. On a lateral move past rack ends, big dark
objects wipe through frame and the mean swung 64 → 48 → 68 with no exposure change at all.
Holding that mean applied a **1.4× gain** to the darkest frames and pushed clipped pixels from
0.22% to **1.85%** — the correction was destroying the shot it was meant to repair.

**Anchor on a high percentile (p90).** It tracks the light sources rather than the composition,
so a rack crossing frame does not move it. Same clip, corrected version: clipping back to ~0.5%
and flat, p90 held within 7/255 across 8s.

Three more things the tool does, each worth keeping:

| | Why |
| --- | --- |
| **Skip below a threshold** (p90 drift < 3/255) | A correction applied to noise is pure risk for no gain |
| **Clamp the gain** (0.88–1.14) | A shot the model cannot describe then degrades to roughly-right instead of to blown highlights |
| **Smooth the correction** over ~9 frames | A per-frame gain from a per-frame measurement flickers, and a fix you can see is worse than the drift |

⚠️ **Do the 1.5× upscale to 1080p here too**, in the same pass — not at concat time, where the
footage would be resampled twice.

## 4. 🔴 The resolution ceiling — the one real limit

**Flow returns 1376×768 stills and 1280×720 video, whatever model you pick.** Google documents 2K
and 4K for Nano Banana Pro; the Flow canvas does not give it to us. That governs every post move:

| Post zoom | Crop from a 1376px still | Upscale needed to fill 720p |
| --- | --- | --- |
| **1.07×** | 1280px | **1.00× — native, the ceiling** |
| 1.5× | 917px | 1.40× |
| 2× | 688px | 1.86× |
| 2.5× | 550px | 2.33× |
| 4× | 344px | 3.72× |

**About 1.07× is free. Everything beyond it trades sharpness.** In practice ~2× still reads on a
moody near-black shot where softness passes as atmosphere; past ~2.5× it looks like what it is.

**So a big reveal cannot be a single post move off one Flow still.** The routes that work:

1. **Let Veo carry the big scale change** (it has no resolution ceiling on invention) and use post
   for the exact, rigid, short moves.
2. **Art-direct two stills at two scales** and use each at native resolution for its half of the
   move — this is the "reframe the still, never the finished clip" rule in
   [`video-prompting.md`](./video-prompting.md) §3, applied to post.
3. **Shoot it in Veo and reverse it** (§2) — no resolution cost at all.

⚠️ **Open question:** whether Nano Banana Pro's 2K/4K output is reachable from Flow at all, or
only via the Gemini API. Worth one live check — it would raise this ceiling by 3× and change what
post can do.

## 5. Working rules

1. **Ask the §1 question before every generation.** "Only the camera moves" is more common than it
   feels, and it is free.
2. **Strip audio the moment a clip lands.** It is lossless and one command; a stray AAC stream in
   the edit is pure friction.
3. **Never crop the finished video to fix framing** — reframe the still and re-animate. Cropping
   throws away pixels Veo never had.
4. **Contact-sheet every take before judging it.** A clip that plays fine at speed can be deforming
   throughout.
5. **Keep the ffmpeg step in the plan, not as a rescue.** Write the shot down as *prompt → generate
   → transform*, so the transform is designed rather than improvised.

---

## Where this connects

- [`video-prompting.md`](./video-prompting.md) §4 — why Frames mode deforms rigid subjects, and the
  reverse trick this file generalises. §9 — the shot classes to route here.
- [`failure-modes.md`](./failure-modes.md) — the failures post can rescue and the ones it cannot.
- `.claude/skills/flow-automation/SKILL.md` — driving Flow; §8 is where new findings get written.
- `scripts/video-contact-sheet.sh` — the review tool.

**Provenance.** Every recipe run on GPOM scene-0 footage 2026-08-21, ffmpeg 4.4.2. The resolution
table is computed from measured Flow output, not from Google's published specs.
