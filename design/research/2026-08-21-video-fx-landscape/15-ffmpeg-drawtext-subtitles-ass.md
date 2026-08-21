# ffmpeg text: drawtext, subtitles, ASS/SSA, typewriter and terminal effects

## What this covers

Everything [`post-production.md`](../../../docs/flow/post-production.md) never touches: putting
text *onto* a frame. It has a crop-off-a-*stray* burned-in subtitle hatch (§3.8) but no route for
burning text in on purpose. This brief is that route: `drawtext` (fonts, fontconfig, position/
time/fade expressions, text files, live reload), `subtitles`/`ass` (libass, styling, karaoke), the
typewriter effect (two routes), and terminal-green text for `git push origin master` — relevant to
the GPOM git-register scenes.

Every skeleton below was **run on this WSL box** (ffmpeg 4.4.2, libass9 1:0.15.2-1) against a
1376×768 near-black plate standing in for Flow output, verified by pulling a frame:
box/border/shadow, the `font=` fontconfig-name route, alpha-fade, a chained-`drawtext` typewriter,
ASS `\k` karaoke, and `subtitles` with `force_style`. `reload` on a live-updated text file was
**not** exercised end-to-end (needs a writer synced to ffmpeg's frame clock) — UNTESTED.
ImageMagick 6.9 (`convert`, no `magick` binary) and Python 3 + Pillow 12.1.1 were smoke-tested as
the per-frame-render alternative.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Static caption/title on a clip or still | `drawtext` | `text=`, position via `x`/`y` expr | free |
| Styled box behind text | `drawtext box=1` | `boxcolor`, `boxborderw` | free |
| Outline + drop shadow | `drawtext borderw`/`shadowx`/`shadowy` | `bordercolor`, `shadowcolor` | free |
| Fade text in/out | `drawtext alpha=<expr>` | piecewise `if(lt(t,…),…)` | free |
| Reveal text in a time window | `drawtext enable='between(t,a,b)'` | per-filter gate, chainable | free |
| Text from an external file | `drawtext textfile=` | avoids shell-escaping | free |
| Live-updating text (ticker) | `drawtext textfile= reload=1` | re-reads file; **UNTESTED** | free |
| Font by system name, no path | `drawtext font='Name'` | resolves via fontconfig; confirmed | free |
| Typewriter, exact/deterministic | chained `drawtext`, `enable=gte(t,…)` | 1 filter per substring; confirmed | free |
| Typewriter, styled (cursor, jitter) | Python + Pillow → PNG seq → `-framerate` | full per-frame control | free |
| Subtitle burn-in from SRT/VTT/ASS | `subtitles=file.srt` | libass render | free |
| Override subtitle styling | `subtitles=...:force_style=` | ASS style string; confirmed | free |
| ASS burn-in incl. karaoke fill | `ass=file.ass` | `\k`/`\kf` switch colour on schedule; confirmed | free |
| Styled PNG text overlay (non-ffmpeg) | ImageMagick `convert -annotate` | alpha PNG, then `overlay=` | free |
| Terminal/phosphor-green prompt text | `drawtext fontcolor=0x39d353` + mono font | DejaVu/Ubuntu/Liberation Mono installed | free |
| Scanlines, CRT bloom, noise over text | not this brief — see grain-texture, motion-graphics-primitives briefs | `geq`/`frei0r`/`noise` | free |
| Same look inside Premiere | Essential Graphics, Source Text keyframes | no typewriter preset — manual only | included w/ CC |

## Named tools

### `drawtext` (libavfilter, ffmpeg core)
Per-frame text renderer using libfreetype (+ fontconfig/fribidi). Free, bundled — no separate
install. Seen 2026-08-21. This build has `--enable-libfreetype --enable-libfontconfig
--enable-libfribidi`. Stable for years; current online docs describe **newer `reload` semantics**
than this box's — see Traps.

### `subtitles` / `ass` filters (wrapping libass)
Hand frames to **libass** for ASS/SSA rendering — `subtitles` accepts SRT/VTT/ASS and
auto-converts, `ass` expects native `.ass`. Free, ISC licence (libass GitHub, 2026-08-21). This box
has libass9 `1:0.15.2-1`, ~2 years behind upstream's **0.17.5** (2026-06-24). Already installed.
The reference ASS/SSA renderer (mpv, VLC), active CI, de facto standard.

### fontconfig (system library)
Lets `drawtext font='Name'` resolve without a `fontfile=` path. Free, system package. Seen
2026-08-21: `fc-list` shows 179 registered fonts; `fc-match "DejaVu Sans Mono"` resolves correctly.
Already installed alongside `fonts-*` Ubuntu packages (dejavu, liberation, noto, ubuntu, urw-base35).

### ImageMagick `convert` (6.9.11-60 Q16, this box)
Alternative to `drawtext` for a styled/anti-aliased text PNG with alpha, composited via `overlay`.
Free. Seen 2026-08-21. This box ships the **v6** binary set — **no `magick` binary here** (`which
magick` empty). Already installed. Decades-old, reliable.

### Python 3 + Pillow (12.1.1, this box)
The "per-frame rendering" route: draw each typewriter frame (cursor blink, jitter, per-glyph
colour) with `ImageDraw.text`, encode with `ffmpeg -framerate N -i frame_%04d.png`. Free. Seen
2026-08-21. Already installed. Reach for this once `drawtext`'s expressions can't do it cheaply.

### Premiere Pro Essential Graphics — Source Text (comparison only)
A typewriter effect means hand-keyframing **Source Text** character by character — **no built-in
preset**, per a 2026 tutorial survey (techyorker.com / freevisuals.net, 2026-08-21, secondary, not
independently re-fetched). Included with the existing CC subscription on this box — **no per-seat
price obtained live this session; a stated gap.**

## Automation hook

**Premiere side.** No match name was found for Source Text/Essential Graphics this pass — a forum
thread on effect component names (creativeclouddeveloper.com, 2026-08-21) covers only classic
video-effect names, not graphics/text. **Discovery step:** create one titled clip by hand, select
it, run `VideoFilterFactory.getMatchNames()`. Treat as unconfirmed, not absent, until that's run.

**ffmpeg side** — TESTED on this box unless marked otherwise.

```bash
# TESTED — box/border/shadow, static text
ffmpeg -loop 1 -i plate.png -t 2 -vf \
 "drawtext=fontfile=/path/DejaVuSansMono.ttf:text='git push origin master':\
fontcolor=0x39d353:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.5:boxborderw=10" \
 -frames:v 1 out.png

# TESTED — fontconfig name resolution, no fontfile= at all
ffmpeg -loop 1 -i plate.png -t 1 -vf "drawtext=font='DejaVu Sans Mono':text='hi':fontcolor=white:fontsize=40" \
 -frames:v 1 out.png

# TESTED — fade via alpha expression (in 0-1s, hold, out 3-4s)
ffmpeg -loop 1 -i plate.png -t 4 -r 25 -vf \
 "drawtext=...:alpha='if(lt(t,1),t,if(lt(t,3),1,if(lt(t,4),4-t,0)))'" -c:v libx264 -pix_fmt yuv420p out.mp4

# TESTED — typewriter: generate a chained-drawtext string, one filter per revealed substring
python3 -c "
text='git push origin master'; step=0.12
print(','.join(
  f\"drawtext=fontfile=/path/mono.ttf:text='{text[:i]}':fontcolor=0x39d353:fontsize=48:enable='gte(t,{(i-1)*step:.2f})'\"
  for i in range(1, len(text)+1)))" > chain.txt
ffmpeg -loop 1 -i plate.png -t 3 -r 25 -vf "$(cat chain.txt)" -c:v libx264 -pix_fmt yuv420p out.mp4

# TESTED — ASS karaoke burn-in; \k40 = 0.40s block, colour flips at block START (not a sweep)
ffmpeg -loop 1 -i plate.png -t 2 -r 25 -vf "ass=karaoke.ass" -c:v libx264 -pix_fmt yuv420p out.mp4

# TESTED — SRT burn-in with a full style override, no .ass file needed
ffmpeg -loop 1 -i plate.png -t 2 -vf \
 "subtitles=cap.srt:force_style='FontName=DejaVu Sans Mono,FontSize=32,PrimaryColour=&H0053D339,MarginV=60'" \
 -c:v libx264 -pix_fmt yuv420p out.mp4

# UNTESTED — live-reloaded ticker text; writer must update cmd.txt ATOMICALLY (tmp file + mv)
ffmpeg -i plate.mp4 -vf "drawtext=fontfile=/path/mono.ttf:textfile=cmd.txt:reload=1" out.mp4

# TESTED — ImageMagick alternative: styled transparent PNG, then overlay in ffmpeg
convert -size 600x100 xc:none -font DejaVu-Sans-Mono-Bold -pointsize 40 \
 -fill '#39d353' -annotate +10+60 'git push' text.png
ffmpeg -i plate.png -i text.png -filter_complex overlay=40:40 out.png
```

## BadCode fit

On a near-black 1376×768 8s Veo plate, phosphor-green (`0x39d353`) or plain white DejaVu/Ubuntu
Mono at 40–56px reads clean, no visible hinting problems — checked directly. `box=1` with
`boxcolor=black@0.4-0.6` guarantees contrast over whatever the plate is doing underneath, cheaper
than fighting the background. Chained-`drawtext` typewriter is exact and free but **scales
linearly with character count** — 23 filters for "git push origin master" is fine; a full
paragraph should move to Pillow/PNG-sequence instead. Karaoke `\k` timing suits narration-synced
text well and composes cleanly with the pipeline: burn text on a still **before** it enters
post-production.md's §3.4 zoompan chain, so text rides the camera move. Keep text-bearing crops
under the ~1.07× native ceiling (post-production.md §4) for the same softness reason as elsewhere.

## Traps

- **`reload` changed meaning across ffmpeg versions.** This box's `-h filter=drawtext` shows
  `reload <boolean>` (any non-zero = reload every frame). Current ffmpeg.org docs (accessed
  2026-08-21) describe it as a **frame-interval integer** instead — `reload=10` meaning "every 10
  frames" elsewhere is just truthy here. Check the actual box, not a blog. It also needs an
  **atomic write** (temp file + `mv`), per the docs — a half-written read is a real failure mode.
- **Simple `\k` is a hard colour-flip per block, not a sweep** — a smooth per-letter fill needs
  `\kf`. Confirmed here: "push" was already fully green mid-syllable. `\ko` untested.
- **`fontfile=` is mandatory when fontconfig is compiled out** — this box has it, so `font='Name'`
  works, but a minimal/static ffmpeg build elsewhere may not.
- **This box's libass (0.15.2) is ~2 years behind upstream (0.17.5, 2026-06)** — verify a style
  feature with `ffmpeg -h filter=ass` before assuming it exists here.
- **Chained-`drawtext` typewriter is O(characters) in the filtergraph** — long text makes the
  `-vf` string unreadable and easy to mis-escape. Generate it with a script, never by hand.
- **No `magick` binary on this box** — use `convert`/`mogrify`/`montage` (IM6 naming).
- **Premiere's typewriter has no preset** — manual Source Text keyframing per character; the
  ffmpeg/Pillow routes are strictly less labour at any length.

## Sources

- <https://ffmpeg.org/ffmpeg-filters.html#drawtext-1> — 2026-08-21 — drawtext options, fontconfig, reload semantics
- <https://ffmpeg.org/ffmpeg-filters.html#subtitles-1> — 2026-08-21 — subtitles/ass filters, force_style
- <https://github.com/libass/libass> — 2026-08-21 — ISC licence, latest release 0.17.5 (2026-06-24)
- `ffmpeg -h filter=drawtext`/`ass`/`subtitles` on this box — 2026-08-21 — local option set, version skew
- `fc-list`, `fc-match`, `dpkg -l | grep fonts-` on this box — 2026-08-21 — 179 fonts confirmed
- WebSearch of techyorker.com / freevisuals.net Premiere tutorials — 2026-08-21 (secondary) — no built-in typewriter preset
- <https://forums.creativeclouddeveloper.com/t/effect-component-names/10611> — 2026-08-21 — match names cover video effects only

**Gap:** Premiere's per-seat price wasn't obtained live this session (helpx.adobe.com timed out
twice) — don't quote a figure without re-fetching. The Source Text match name wasn't found; needs
the `getMatchNames()` step above before Premiere-side text automation is attempted.
