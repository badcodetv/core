# Delivery and QC — getting the file right, and proving it

**The last step, and the one that silently ruins near-black films.** Premiere renders it;
this is what happens between that render and the upload.

> Run **[`scripts/delivery-qc.sh`](../../scripts/delivery-qc.sh)** on anything before it ships.
> ```bash
> scripts/delivery-qc.sh RENDER.mp4 shorts     # youtube · shorts · reels · tiktok
> ```
> It is read-only, needs nothing but ffmpeg, and it exits non-zero on a real fault.

---

## 🔴 The one that actually bit us

**`camping.mp4` — the finished film on the drive — ships with full-range content and no colour
tag at all.** Measured 2026-08-22: `YMIN=0 YMAX=255`, `color_range=unknown`,
`color_space=unknown`.

A player that finds no tag assumes **limited range** and expands 16–235 out to 0–255. Applied to
content that is *already* 0–255, everything below 16 flattens to black. **The shadows are where
BadCode's whole register lives**, so this is not a subtle grading difference — it is the picture.

It is invisible until you measure it. Nothing warns you, the file plays, and it looks
approximately right on the machine that made it.

### The fix, measured

```bash
ffmpeg -i in.mp4 \
  -vf "scale=in_range=full:out_range=limited" \
  -pix_fmt yuv420p -color_range tv \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:v libx264 -crf 18 -c:a copy out.mp4
```

Verified on a 5-second slice of `camping.mp4`: content lands at **18–231**, tagged `tv`, pixel
format `yuv420p`. Tag and content agree.

### 🔴 `out_range` alone is a silent no-op

The trap inside the trap. Drop `in_range=full` and ffmpeg assumes the input was already limited,
so the conversion does nothing — **but the `-color_range tv` tag is still written.** Measured:
content stayed at **4–249** while the file claimed to be limited range. You have manufactured
exactly the mismatch you were trying to fix, and now it clips the whites instead.

**Both halves of that scale filter are load-bearing.**

### Why limited range, and not full

Full range is the tempting answer for a film made of shadows — more code values in the blacks.
Two measured reasons not to:

- **libx264 will not produce `yuv420p` at full range.** Ask for full and you get **`yuvj420p`**,
  the deprecated J-variant, even with an explicit `-pix_fmt yuv420p`. Confirmed both ways.
- **Limited range tagged `tv` is what the entire delivery chain expects.** A platform that
  ignores your `pc` tag crushes the film; one that ignores a `tv` tag does nothing at all. The
  failure mode of being conventional is much cheaper.

Keep the extra shadow precision in the *master*. Convert on the way out.

---

## What the checker looks at

| Group | Checks |
| --- | --- |
| **Colour** | `pix_fmt` is 4:2:0 · `color_range` is tagged · BT.709 across space/primaries/transfer |
| **Levels** | Luma range against the tag — all four mismatch cases · blacks clipped at 0 · unintended black stretches · frozen frames |
| **Audio** | Integrated loudness against −14 LUFS · true peak under −1 dBFS · 48 kHz · a missing stream |
| **Platform** | Aspect, resolution cap, duration limit, bitrate ceiling, frame-rate window |

### Platform targets

| Platform | Wants | Source |
| --- | --- | --- |
| **YouTube** | H.264 High, 4:2:0, BT.709, 1080p ≥8 Mbps, AAC 48kHz | Primary (Google support) |
| **YouTube Shorts** | 9:16, ≤1080p, ≤3 minutes | Primary |
| **Instagram Reels** | H.264/HEVC, 4:2:0, 9:16, ≤25 Mbps VBR, 3s–15min, ≤300MB | Primary (Meta Graph API) |
| **TikTok** | 1080×1920, 9:16, 23–60fps | ⚠️ **Secondary** (Sprout Social). TikTok re-transcodes everything |
| **Loudness** | ≈−14 LUFS integrated, all three | ⚠️ Secondary consensus, not a quoted spec |

---

## What local QC cannot tell you

🔴 **Every platform re-encodes what you upload.** `ffprobe` and `signalstats` prove your file is
correct; they prove nothing about the transcode that actually reaches a viewer.

That re-encode hurts BadCode's material more than most: heavy compression bakes banding into
exactly the low-entropy near-black gradients the whole look is made of. The defence is to give
the encoder something to chew on — a light dither/grain pass before delivery:

```bash
ffmpeg -i in.mp4 -vf "noise=alls=3:allf=t" -c:a copy out.mp4
```

Not verified end-to-end against a real platform re-encode. It is a well-founded technique, not a
measured result here.

---

## Where the rest lives

- Full research: [`design/research/2026-08-21-video-fx-landscape/19-delivery-specs-and-qc-scopes.md`](../../design/research/2026-08-21-video-fx-landscape/19-delivery-specs-and-qc-scopes.md)
- Exporting from Premiere: [`../premiere/recipes.md`](../premiere/recipes.md) § *See it, then ship it*
- Everyday ffmpeg recipes: [`../flow/post-production.md`](../flow/post-production.md)
- Loudness *mixing* (as opposed to the delivery target): briefs 11 and 17

**No scope readback exists inside Premiere.** No UXP API exposes Lumetri Scopes values, so QC
happens on the rendered file, after export, or by eye in the Lumetri Scopes panel. That is a
job to hand to the human — see the `premiere-automation` skill §8.
