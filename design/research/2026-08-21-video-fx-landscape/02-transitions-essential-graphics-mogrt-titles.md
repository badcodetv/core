# Transitions, Essential Graphics, MOGRT templates, titles

## What this covers

Built-in Premiere Pro video transitions and how to name them for automation; the panel that used to
be called "Essential Graphics" and what replaced it in current Premiere; .mogrt motion-graphics
templates — what they are, where they live on disk, Adobe Stock's free/paid split, and third-party
marketplaces; text/title tools including the native transcript-driven captions workflow; and what a
script or the UXP bridge can actually drive versus what stays manual. ffmpeg equivalents
(crossfades, text overlays) are included for the post-production half, tested against the clips
this project produces (1376×768, near-black, 8s).

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
|---|---|---|---|
| Cut between two clips with a dissolve | Premiere native transition ("Cross Dissolve") | Drag from Effects panel onto the cut point | included |
| 90+ extra stylised transitions/effects (glitch, kaleidoscope, 3D) | Premiere native, ex-Film Impact | Now built into the Effects panel / Film Impact Dashboard as of Premiere 25.5 | included |
| Drag-in animated title / lower-third | .mogrt template | Graphics Templates panel → drag to timeline → edit in Properties panel | free–£ (see Named tools) |
| 3D extruded / kinetic titles | Boris FX Title Studio | Standalone or Continuum unit, applies as a Premiere effect | £ (paid) |
| Simple flat lower-third/title text | Native Type tool + Properties panel | Draw text box on canvas, style in Properties, no MOGRT needed | included |
| Burned-in captions from spoken audio | Text panel → Transcribe → Create Captions | Native transcript-to-caption pipeline, no plugin | included |
| Bulk free transition/text presets | Premiere Composer (Adobe Exchange) or CoreMelt V2 free tier | Install extension, drag preset onto clip | free |
| Licensed MOGRT library at scale | Adobe Stock templates, Motion Array, Envato Elements | Browse in-panel (Stock) or on the marketplace site, license/subscribe, drop into Graphics Templates panel | £–£££/mo |
| Script-insert a MOGRT onto a track | `insertMogrtFromPath` (UXP/ExtendScript scripting API) | Call from a script with a `.mogrt` path, track index, time | included (dev time only) |
| Crossfade two rendered clips outside Premiere | ffmpeg `xfade` filter | `xfade=transition=fade:duration=D:offset=T` between two inputs | free |
| Overlay title text outside Premiere | ffmpeg `drawtext` filter | Font file + text + timed alpha fade via `enable`/`alpha` expressions | free |

## Named tools

### Premiere Pro native transitions (ex-Film Impact, absorbed)
90+ GPU transitions/effects (glitch, VHS, kaleidoscope, 3D) folded into the Effects panel after
Adobe acquired Film Impact, replacing a former $15–30/mo plugin. **Free**, included with CC, seen
2026-08-21. Win/Mac. Install: none. Maturity: brand-new (Sept 2025); some 2026 reports of the
"Film Impact Dashboard" misbehaving in v26.0.

### Boris FX Title Studio
3D vector titling (Continuum unit or standalone) — OBJ/C4D import, 2D/3D lower thirds, 70 new 2026
presets. **Price not confirmed** — no figure surfaced; treat as paid Continuum-tier, verify on
borisfx.com. Win/Mac, Premiere/AE/Resolve/Vegas. Maturity: established, actively updated.

### MotionVFX mTitles
Drag-and-drop title packs (20–30 presets each), sold individually. **$89–$99/pack**, perpetual,
seen 2026-08-21 motionvfx.com. Win/Mac. Maturity: long-running, incremental releases.

### CoreMelt V2 packs
PolyChrome Transitions V2, Motion Graphics Box V2, Editors Tools V2, ImageFlow FX V2 — **$79 each,
or $199 for the 8-pack bundle**, seen 2026-08-21 coremelt.com. A free tier is referenced elsewhere
("CoreMelt Free", 44 effects) but its URL 404'd — **gap, unconfirmed**. Win/Mac. Maturity:
established, V2 line current.

### Motion Array (Everything plan)
Subscription, 2M+ assets incl. MOGRT/AE/FCP/Resolve templates, 50+ plugins, a "Premiere Hub" panel.
**≈$24.99/mo annual (≈$21.42/mo effective)**, team $27/mo/member, seen 2026-08-21 — vendor pages
disagree with each other, this is the pricing-page figure. Maturity: large, active catalogue.

### Envato Elements
Subscription stock library (26M+ assets), deep template section. **Core $16.50/mo ($129/yr), Plus
from $39/mo, Ultimate from $109/mo**, annual; student $11.50/mo, seen 2026-08-21. AI credits
(10/100/unlimited) added post-Feb-2026. Maturity: deepest AE/Premiere catalogue per reviews.

### Adobe Stock motion graphics templates
Adobe's own in-app marketplace, browsable in the Graphics Templates panel with drag-to-license.
**Mixed free and paid, individually licensed** (helpx.adobe.com confirms the flow); exact price
points and free/paid ratio — **gap, not surfaced**. In-app only. Maturity: official, integrated.

### Premiere Composer (Adobe Exchange)
Most-downloaded free Exchange extension — transitions, text-motion presets, title boxes, SFX,
auto-scales 16:9–1:1 up to 4K. **Free base; paid expansion packs** (prices — gap). Win/Mac,
**CEP-era extension** — verify it still loads under 2026's CEP restrictions (see Traps).

## Automation hook

**Premiere side — transitions.** No documented match-name table for native transitions was found
(helpx describes the UI, not identifiers; `"ADBE Cross Dissolve"`-style searches returned nothing
authoritative). **Discovery step, not asserted names:** enumerate installed transitions/effects at
runtime via Premiere's `VideoFilterFactory`/effect-listing calls in the UXP scripting API, filter
the returned name/matchID list for the string you want (e.g. `"Dissolve"`), and record whatever
matchID comes back rather than guessing one — cross-check against `AdobeDocs/uxp-premiere-pro` on
GitHub (the file path tried in this pass 404'd; re-resolve before relying on it) — **gap**.

**Premiere side — MOGRT insertion.** Community-sourced, not confirmed against primary docs:
`sequenceItem.importMGT(path, trackIndex, ...)` and `importMGTFromLibrary(...)` were named in a
2026 Adobe community thread, a maintainer confirming `importMGT` works despite being missing from
published docs. This project's expected name, `insertMogrtFromPath`, appears only in secondary
summaries — **treat both spellings as unverified until checked against the live UXP `types.d.ts`**;
secondary param shape: `(mgtPath: string, time: TickTime, videoTrackIndex: number,
audioTrackIndex: number)`. `getMGTComponent()` on an inserted `TrackItem` reaches its exposed
parameters afterward. Installed-template location: Windows `%APPDATA%\Adobe\Common\Motion
Graphics Templates\`, Mac `~/Library/Application Support/Adobe/Common/Motion Graphics Templates/`.

**ffmpeg side.** Crossfade — **TESTED** (1376×768 near-black clips, ffmpeg 4.4.2, WSL; 3s+3s clips,
1s overlap → correct 5s output):
```
ffmpeg -i a.mp4 -i b.mp4 \
  -filter_complex "[0:v][1:v]xfade=transition=<name>:duration=<D>:offset=<T>[v]" \
  -map "[v]" -c:v libx264 -pix_fmt yuv420p out.mp4
```
`<name>`: `fade`, `dissolve`, `wipeleft/right/up/down`, `slideleft/right`, `circleopen`, `pixelize`
— full list via `ffmpeg -filters | grep xfade` or ffmpeg.org's `xfade` doc. `offset` is absolute
from the start of input A; the overlap eats into total runtime, worth budgeting against an 8s clip.

Title overlay — **TESTED** (drawtext, timed fade-in/out alpha):
```
ffmpeg -i in.mp4 -vf "drawtext=fontfile=<path.ttf>:text='<TEXT>':fontcolor=white:fontsize=48:\
x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t,<start>,<end>)':\
alpha='if(lt(t,<start>+0.5),(t-<start>)/0.5,if(gt(t,<end>-0.5),(<end>-t)/0.5,1))'" \
  -c:v libx264 -pix_fmt yuv420p out.mp4
```
Needs a real `.ttf`/`.otf` path (no by-name font lookup in this build) — confirmed
`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf` present; use a licensed brand font for release.
No MOGRT concept — animated/responsive templates stay Premiere-only.

## BadCode fit

- Near-black footage crossfades cleanly with `fade`/`dissolve` — low contrast hides xfade's classic
  double-exposure ghosting (plausible from tested output; not checked against real Flow footage).
- Marketplace MOGRT titles are designed for bright broadcast footage — strip drop-shadow/glow/bevel
  defaults to flat single-weight type; don't keep a template's stock colour scheme.
- An 8s Flow clip leaves little room for a long overlap — a 1s dissolve costs an eighth of the clip;
  keep transitions short (0.3–0.6s) or plan the overlap at the edit-plan stage.
- Native ex-Film Impact glitch/kaleidoscope/3D transitions read as generic-AI/stock-footage — avoid
  for BadCode's documentary register; stick to Cross Dissolve, cuts, sparing wipes.
- Don't wire `insertMogrtFromPath`/`importMGT` into the UXP bridge before a live API check — the
  call and parameter contract are unconfirmed against primary docs (see gaps).

## Traps

- **CEP-era extensions are already degrading.** Premiere Pro 2026 no longer natively loads legacy
  CEP extensions by default (Adobe: CEP 12 is the last major version, no hard deprecation date
  published). Verify Premiere Composer or any pre-UXP panel still loads before depending on it.
- **"Essential Graphics panel" is the wrong name to automate against now.** As of v25.0 it split
  into a **Properties panel** (editing) and a **Graphics Templates panel** (browsing/importing) —
  docs/tutorials referencing "Essential Graphics" describe a workflow this app no longer has.
- **Pricing pages disagree with themselves.** Motion Array, Boris FX, and CoreMelt's free-tier
  naming all showed gaps across sources — quote one figure with source/date, don't average.
- **Film Impact's own product page still markets a paid pack** even though the same content is now
  built into Premiere natively for free — likely stale marketing, don't quote its old $15–30/mo
  price as current without checking directly.
- **`xfade`'s `offset` is absolute, not relative** — compute `offset = durationA - overlap` before
  scripting a batch, or the transition misses the overlap or clips past the shorter input.

## Sources

- [Effects and transitions reorganization in Adobe Premiere](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/effects-and-transitions-reorganization.html) — 2026-08-21, official transition category naming
- [Premiere Pro 25.5 adds 90+ new effects](https://alternativeto.net/news/2025/9/premiere-pro-25-5-adds-90-new-effects-fast-gpu-playback-and-major-timeline-upgrades/) — 2026-08-21, Film Impact absorption details
- [Adobe acquires Film Impact](https://www.provideocoalition.com/adobe-acquires-film-impact-premiere-pro-25-5/) — 2026-08-21, acquisition + free pricing
- [Reinstate the Essential Graphics Panel (Adobe Community)](https://community.adobe.com/feature-requests-730/reinstate-the-essential-graphics-panel-in-premiere-pro-2025-1327922) — 2026-08-21, confirms panel split in v25.0
- [Use Adobe Stock MOGRTs in Premiere](https://helpx.adobe.com/premiere/desktop/add-text-images/use-motion-graphics-templates/use-motion-graphics-templates-from-adobe-stock.html) — 2026-08-21, official Stock free/paid workflow
- [Best way to insert MOGRT into sequence? (Adobe Community)](https://community.adobe.com/t5/premiere-pro-discussions/best-way-to-insert-mogrt-into-sequence-are-docs-out-of-date/td-p/13274031) — 2026-08-21, `importMGT` community confirmation
- [FilmImpact — We have joined Adobe](https://www.filmimpact.com/premiere-pro-transitions-pack) — 2026-08-21, acquisition banner detail
- [CoreMelt — Buy Now](https://coremelt.com/pages/buy-now) — 2026-08-21, V2 plugin pack pricing
- [Motion Array Pricing 2026](https://checkthat.ai/brands/motion-array/pricing) — 2026-08-21, Everything plan pricing
- [Envato Elements Pricing 2026](https://www.stackscored.com/pricing/stock-media/envato-elements/) — 2026-08-21, Core/Plus/Ultimate tiers
- [MotionVFX Store](https://www.motionvfx.com/store/adobe-premiere-after-effects) — 2026-08-21, mTitle pack pricing
- [ffmpeg Filters Docs — xfade](https://ffmpeg.org/ffmpeg-filters.html#xfade) — 2026-08-21, transition enum (cross-checked vs local ffmpeg 4.4.2)

**Gaps:** authoritative ADBE-style match names for native transitions; confirmed primary-source
signature for `insertMogrtFromPath` vs `importMGT`/`importMGTFromLibrary` (community-sourced only);
Boris FX Title Studio's price; CoreMelt's free-tier product name/URL; Adobe Stock MOGRT price range
and free/paid ratio; Premiere Composer's expansion-pack prices.
