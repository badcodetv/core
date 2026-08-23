# Delivery specs and QC scopes

## What this covers

What YouTube (incl. Shorts), TikTok and Instagram (Reels/feed) want from a finished file in
2026 — resolution, aspect ratio, frame rate, codec/container, bitrate, colour tagging, max
duration, loudness — and how to hit each target and then **check** it before shipping, from
ffmpeg and Premiere's H.264 export. This is the brief [`12-ffmpeg-filter-map.md`](12-ffmpeg-filter-map.md)
promised ("aspect-ratio delivery, QC scopes... get full treatment in briefs 13–18") that none of
13–18 delivered — see the sweep [README's Gaps](README.md#gaps). Loudness *mixing* stays with
files [11](11-audio-ducking-denoise-narration-mix.md) and [17](17-ffmpeg-audio-filters.md); this
is only the delivery target and how to verify a file hits it.

## What's possible

| Need | Tool/route | How | Cost tier |
| --- | --- | --- | --- |
| Interrogate container/codec/colour tags | `ffprobe` | `-show_entries stream=codec_name,pix_fmt,color_range,color_space,color_primaries,color_transfer` | free |
| Interrogate duration/bitrate/container | `ffprobe` | `-show_entries format=duration,bit_rate,format_name` | free |
| Flag illegal (out-of-broadcast-range) pixels | `signalstats stat=brng` | flags pixels outside 16–235 | free |
| See levels as waveform/vectorscope/histogram | ffmpeg `waveform`/`vectorscope`/`histogram` | render a frame or the whole clip as a scope | free |
| Same, GUI, live while grading | Premiere Lumetri Scopes panel | Window → Lumetri Scopes | included |
| Confirm delivery loudness | `ebur128` / two-pass `loudnorm` | measure then apply — recipe in files 11/17 | free |
| Catch a dead-black head/tail | `blackdetect` | flags near-black intervals past a duration | free |
| Catch a frozen/stuck frame | `freezedetect` | flags near-identical consecutive frames | free |
| Hit YouTube's spec | H.264 High Profile, 4:2:0, BT.709, ladder below | encode + tag on export | free |
| Hit YouTube Shorts | ≤1080p, vertical, ≤3 min | scale to 9:16, encode as above | free |
| Hit Instagram Reels | H.264/HEVC, 4:2:0, ≤25 Mbps VBR, 9:16 | encode + tag on export | free |
| Hit TikTok | 1080×1920, 9:16, 23–60fps | encode + tag on export | free |
| Export from Premiere at spec | H.264 "Match Source — High bitrate" preset | File → Export → pick the `.epr` | included |
| Cut banding risk in a near-black gradient | dither/grain pre-pass (files 12/13) + "Render at Maximum Depth" | apply before final encode | free/included |

**Platform numbers, sourced:**

- **YouTube** (primary): MP4, moov atom fast-started; H.264 High Profile, 4:2:0; AAC-LC/Opus
  48kHz; **BT.709 for SDR**; bitrate (SDR, 24–30fps) 1080p **8 Mbps**, 720p **5 Mbps**, 4K
  **35–45 Mbps**; audio 384 kbps stereo. Encode at the frame rate it was rendered at.
- **YouTube Shorts** (primary): vertical, **max 1080p**, **up to 3 minutes**.
- **Instagram Reels** (primary, Meta's Graph API spec — the same one the app enforces): MOV/MP4,
  fast-started; **HEVC or H.264**, 4:2:0; max **1920px** horizontal, **9:16** recommended;
  **23–60fps**; **VBR ≤25 Mbps**; AAC 48kHz **128kbps**; 3s–15min; ≤300MB.
- **TikTok** (secondary — no plain platform spec page found; its developer API docs list only
  container types): **1080×1920, 9:16, 23–60fps** per Sprout Social's 2026 roundup. TikTok
  re-transcodes everything server-side regardless of what's uploaded.
- **Loudness** (secondary, reused from file 11): **≈-14 LUFS integrated** is the 2026 consensus
  for YouTube; TikTok/Instagram cluster -14 to -15 LUFS, no published number. Master to -14 LUFS.

## Named tools

### ffmpeg's QC filter bank (`signalstats`, `blackdetect`, `freezedetect`, `ebur128`, `waveform`, `vectorscope`, `histogram`)
Already in the 4.4.2 build this repo runs — same finding as file 12. Free, ffmpeg core. Confirmed
via `ffmpeg -h filter=<name>` and exercised live this session.

### `ffprobe`
Ships with ffmpeg — read-only interrogation of codec, pixel format, colour tags, duration,
bitrate. Free, CLI, already installed.

### Premiere Lumetri Scopes panel
GUI waveform/vectorscope/histogram/parade, live while grading — the same checks as the ffmpeg
filters, done by eye pre-export. Included with any CC seat. **Not live-verified against 26.3.2
this session** — standard, long-documented Premiere UI, not a fresh finding.

### Premiere H.264 "Match Source — High bitrate" export preset
The `.epr` this repo's bridge points at:
`C:\Program Files\Adobe\Adobe Premiere Pro 2026\MediaIO\systempresets\4E49434B_48323634\01 - Match Source - High bitrate.epr`
(per the plan's Host facts table). Matches source resolution/frame rate at a high bitrate — a
safe starting point for any of the three platforms, still worth an `ffprobe` check after.

### "Render at Maximum Depth" (Premiere export option)
Export Settings checkbox that renders internally at higher bit depth even into an 8-bit codec,
cutting banding risk on a smooth gradient. Included. **Not live-verified this session** —
long-standing option; confirm the label before citing it in `docs/video-fx/`.

## Automation hook

**Premiere side.** No UXP API exposes scope *readings* — a scan of the plan's Interfaces section
confirms `Exporter`/`EncoderManager` cover export, nothing covers scope readback. **QC happens
post-export**, on the rendered file, via `ffprobe`/the filters below — not live inside Premiere.

**ffmpeg side** — run against a synthetic near-black 1376×768 clip in the scratchpad (TESTED):

```bash
# interrogation — TESTED
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,pix_fmt,color_range,color_space,color_primaries,color_transfer,r_frame_rate,bit_rate \
  -of default=noprint_wrappers=1 in.mp4
ffprobe -v error -show_entries format=duration,bit_rate,format_name -of default=noprint_wrappers=1 in.mp4

# illegal-range check — TESTED
ffmpeg -i in.mp4 -vf "signalstats=stat=brng,metadata=print:file=-" -an -f null -

# waveform / vectorscope stills — TESTED (render standalone; stacking needs a matching-width scale first)
ffmpeg -i in.mp4 -vf "waveform=mode=column:mirror=1" -frames:v 1 waveform.png
ffmpeg -i in.mp4 -vf "vectorscope=mode=color3" -frames:v 1 vectorscope.png

# black / freeze checks — TESTED
ffmpeg -i in.mp4 -vf "blackdetect=d=0.1:pic_th=0.98:pix_th=0.10" -an -f null -
ffmpeg -i in.mp4 -vf "freezedetect=n=-60dB:d=0.5" -an -f null -

# loudness scan — TESTED (two-pass loudnorm recipe lives in files 11/17)
ffmpeg -i in.mp4 -af "ebur128=peak=true" -f null -
```

## BadCode fit

- **This session found a real, silent trap.** Tagging a file `-color_range pc` (full range)
  does **not** by itself rescale pixel values — a pure black/white source encoded with
  `-color_range pc -c:v libx264` measured `YMIN=16 YMAX=235` via `signalstats` (limited-range
  **content**, full-range **tag**: a mismatch). Fixing it needs an explicit conversion, not just
  the output flag:
  ```bash
  ffmpeg -i in.mp4 -vf "scale=out_range=full,format=yuv420p" -color_range pc out.mp4
  ```
  With that filter added, the same source measured `YMIN=0 YMAX=255` — tag and content agree.
  **A player resolving a mismatched tag either crushes blacks or clips whites — invisible until
  checked, worst exactly where BadCode's films live: the shadows.**
- Every Flow clip and ffmpeg plate here defaults to `color_range=unknown` (no tag at all) unless
  a step sets one — confirmed via `ffprobe` on this session's default-settings encode. Tag
  explicitly rather than hope.
- **A platform's own re-transcode is invisible to local QC.** `ffprobe`/`signalstats` on the
  upload prove nothing about the server-side re-encode that actually reaches the viewer, and
  heavy re-compression crushes shadow detail and bakes in banding hardest on the low-entropy
  gradients a near-black plate is made of. A light dither/grain pass before delivery
  (`noise=alls=N:allf=t`, TESTED in file 12) gives the platform's encoder texture to compress
  instead of a flat gradient — not verified end-to-end against a real re-encode this session.

## Traps

- 🔴 **`-color_range` alone is a tag, not a rescale.** See BadCode fit — reproducible with the
  commands given.
- **Local QC proves your encode is correct, not what the platform does to it afterward.**
- **TikTok's spec here is secondary** (Sprout Social, not TikTok's own page) — re-verify before
  it goes in `docs/video-fx/` as fact.
- **YouTube's primary loudness page wasn't reached** (same gap file 11 flags) — -14 LUFS is
  secondary-sourced consensus, not a quoted spec.
- **Lumetri Scopes and "Render at Maximum Depth" weren't confirmed live** — no Premiere session
  ran this pass; re-check the exact path against 26.3.2 before scripting around them.

## Sources

- [YouTube — Recommended upload encoding settings](https://support.google.com/youtube/answer/1722171) — 2026-08-21 — H.264, 4:2:0, bitrate ladder
- [YouTube — About YouTube Shorts](https://support.google.com/youtube/answer/10059070) — 2026-08-21 — Shorts: 1080p max, 3min
- [Meta — Instagram Graph API media reference](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media) — 2026-08-21 — Reels codec/bitrate/resolution, primary
- [Sprout Social — Social media video specs guide](https://sproutsocial.com/insights/social-media-video-specs-guide/) — 2026-08-21 — TikTok resolution, secondary source
- [Forasoft — LUFS targets per platform 2026](https://www.forasoft.com/learn/audio-for-video/articles-audio/lufs-targets-per-platform-2026) — 2026-08-21 — reused from file 11
- [ffmpeg.org — Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html) — 2026-08-21 — official filter reference, all names
- local: `ffmpeg -h filter=<name>` / `ffprobe` / range-mismatch test, this WSL box — 2026-08-21 — confirmed QC filters, tag/content mismatch

---

## Live findings on a real BadCode render, 2026-08-22

Shipped as **[`scripts/delivery-qc.sh`](../../../scripts/delivery-qc.sh)**; house page at
[`docs/video-fx/delivery.md`](../../../docs/video-fx/delivery.md).

### 🔴 The trap this brief predicted is already in a finished BadCode film

`D:\badcode-videos\camping\camping.mp4` — 1920x1080, 25fps, 215s, the delivered camping cut —
measures `YMIN=0 YMAX=255` with **`color_range=unknown`, `color_space=unknown`**. Full-range
content, no tag at all.

A player finding no tag assumes limited and expands 16–235 to 0–255. On content already at 0–255,
everything under 16 flattens. **The shadows are the entire BadCode register**, so this is the
picture, not a nuance. It was found by running the check, not by looking at it.

### 🔴 `out_range` alone is a silent no-op — the trap inside the trap

The brief's fix (`scale=out_range=full`) is only half of one. Measured on the same source:

| Command | Content | Tag | Verdict |
| --- | --- | --- | --- |
| `scale=out_range=limited` + `-color_range tv` | **4–249** | `tv` | 🔴 conversion did nothing, tag written anyway |
| `scale=in_range=full:out_range=limited` + `-color_range tv` | **18–231** | `tv` | ✅ agree |

Without `in_range`, ffmpeg assumes the input was already limited and skips the conversion — while
still writing the tag. **You manufacture the exact mismatch you were fixing**, now clipping whites
instead of crushing blacks. Both halves are load-bearing.

### 🔴 libx264 will not emit `yuv420p` at full range

Ask for full range and you get **`yuvj420p`**, the deprecated J-variant — *even with an explicit
`-pix_fmt yuv420p` output flag*. Confirmed both ways on the same slice.

This settles which direction to convert. Full range is tempting for a film made of shadows, but
it costs a deprecated pixel format, and a platform that ignores a `pc` tag crushes the film while
one that ignores a `tv` tag does nothing at all. **Convert to limited on the way out; keep the
extra precision in the master.** The house command:

```bash
ffmpeg -i in.mp4 -vf "scale=in_range=full:out_range=limited" \
  -pix_fmt yuv420p -color_range tv \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:v libx264 -crf 18 -c:a copy out.mp4
```

### Four mismatch cases, not two

The brief describes tagged-full/content-limited. There are four, and **the untagged pair is the
one that occurs in the wild** — every Flow clip and every default ffmpeg encode is untagged:

| Tag | Content | Result |
| --- | --- | --- |
| `pc` | limited | stretched, clips |
| `tv` | full | clipped whites |
| **untagged** | **full** | 🔴 **crushed blacks — this is `camping.mp4`** |
| untagged | limited | harmless; tag it anyway |

### The rest of the check, on the same file

Loudness **−12.5 LUFS** (inside 1.5 LU of the −14 consensus), true peak **−1.5 dBFS** (headroom
for the re-encode), AAC 48kHz, 16.99 Mbps — all clean. `blackdetect` found 7 near-black stretches
and `freezedetect` 4 frozen ones, both plausible for held comic frames rather than faults, which
is why they warn rather than fail.

**Still open:** Lumetri Scopes and "Render at Maximum Depth" remain unconfirmed against a live
26.3.2 session — the bridge was held by another session on 2026-08-22. No upload-and-redownload
test against a real platform.

---

**Gaps:** TikTok's own primary spec page (JS-rendered, unreachable via WebFetch this pass);
YouTube's primary loudness page (also unreachable); Lumetri Scopes and "Render at Maximum Depth"
not confirmed against a live 26.3.2 session; no upload-and-redownload test against a real
platform to confirm the dither/banding defence end-to-end.
