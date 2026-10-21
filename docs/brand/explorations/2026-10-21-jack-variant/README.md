# Jack's variant: red o + white triangle + outline (2026-10-21)

Jack picked this for social media (TikTok etc.): Kai's "Saved version 5" logo, with the name's o drawn as the bench
style **"Red o + white triangle + outline"** at its defaults (white triangle 36% of the o, 61% off centre; white
outline 20% of the o's radius). Not saved on the bench; built from those numbers. **Not yet the official logo**:
Kai ruled "Saved version 5", so swapping the o everywhere is his call too.

**Made in code, not Flow.** Flow redraws the letters and the triangle every time (tested 2026-10-21, see
`../2026-10-21-sketch-shadow/`), and upscaling an AI image adds blur. These are the exact vector shapes, so any
size is pixel-sharp.

| File | Use |
| --- | --- |
| `logo-and-name-on-black-4096.png` | banners, end cards, headers (matches the bench's big view: ring large, name beside it) |
| `logo-and-name-transparent-4096.png` | the same over video or a photo |
| `logo-only-on-black-4096.png` / `logo-only-transparent-4096.png` | the ring and triangle alone |
| `tiktok-profile-2048.png` | profile picture; the mark sits inside the circle TikTok crops to |
| `*.svg` | the vectors, any size |

The other files (favicons, wordmark, stacked) came from the same build and use the same o.

## Flow recreation (Jack asked, 2026-10-21)

Jack wants the same two pieces made in Flow so he can upscale there. Reference attached = identity kept (see
`docs/google-flow/nano-banana-2.md`, 2026-10-21), so each prompt attaches the exact render and asks for a faithful
redraw. Nano Banana 2, 2 takes each, fresh project each. Compare every take with the PNG above at 100% before use.

### f1 — logo and name (16:9) · Attach `logo-and-name-on-black-4096.png`
```
Image 1 is our finished logo. Recreate it exactly as it is in image 1: the same off-white ring with the same rounded red triangle in the same place, and beside it the same thin, round lowercase letters spelling "badcode", where the o is a red disc with an off-white rim and a small off-white triangle inside. Keep every size, gap, line thickness, position and colour the same, on the same plain near-black background. Clean, flat, crisp vector artwork with perfectly smooth edges and nothing added: no texture, no shadow, no gloss, no glow and no other text. Thanks.
```

### f2 — logo only (1:1) · Attach `logo-only-on-black-4096.png`
```
Image 1 is our finished logo mark. Recreate it exactly as it is in image 1: the same off-white ring and the same rounded red triangle in the same place inside it, with every size, line thickness, position and colour the same, on the same plain near-black background. Clean, flat, crisp vector artwork with perfectly smooth edges and nothing added: no texture, no shadow, no gloss, no glow and no text. Thanks.
```

### Results

| Take | Verdict |
| --- | --- |
| f1 a / b (`flow-f1-logo-and-name-*.jpg`, 1376×768, Flow project `c43cf89a`, "Oct 21 - 12:49") | ✅ Very close in both: letters, red o with off-white rim and small triangle all kept. Ring drawn a little thinner than the source; the lockup sits slightly smaller in the frame |
| f2 a / b (`flow-f2-logo-only-*.jpg`, 1024², project `abc9805d`, "Oct 21 - 12:50") | ✅ Near-identical to the source. ⚠️ The ring nearly touches the frame edge, so a circular profile crop (TikTok) cuts it; use `tiktok-profile-2048.png` for the avatar |

**Finding:** asked to *copy* (reference attached, "recreate it exactly"), NB2 was faithful; asked to *treat* it
(sketch shadow) or *redesign* it, it redrew the letters. Copy jobs work; anything more redraws.
