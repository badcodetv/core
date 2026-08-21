# Maps, data/motion graphics, kinetic typography, UI/terminal graphics

## What this covers

Map zooms and travel-route graphics as MOGRTs or as rendered-elsewhere footage; charts/data-viz
inside Premiere; kinetic typography (title packs and the native alternative); on-screen
terminal/CRT graphics (the "title typed as a git command" case); and screen-replacement/UI
mockup work. Scoped to Premiere 26.3.2 (no After Effects) and ffmpeg 4.4.2 on 1376×768,
near-black, 8s AI clips.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Animated pin-to-pin travel route | Map Route Generator (VideoHive) | Drop `.mogrt` in, plot up to 20 pins | $29 one-off |
| Stylised world/region map + markers | World Map ToolKit / Pro | `.mogrt`, edit in Properties panel | Envato Elements |
| Photoreal 3D terrain flyover | Google Earth Studio | Free browser tool, export as footage | Free, **non-commercial only** |
| Brand-styled custom map render | Mapbox GL JS | Script dark style + camera path, capture frames | Free tier + dev time |
| GIS flyover/choropleth | QGIS (Time Manager / Atlas / 3D) | Render frame sequence to video | Free |
| Bar/line/pie/KPI chart overlay | Infographics / Chart Creator MOGRTs | Insert via Graphics Templates panel | Marketplace, ~$20–60 |
| Kinetic title / lower third | Kinetic-type MOGRT, or Title Studio for 3D | Insert `.mogrt`, or author and import | Paid; Mixkit has a free tier |
| Title typed as a terminal command | Native Crop typewriter, or ffmpeg mask+overlay | Reveal left-to-right, blink a cursor | Free / native |
| CRT scanlines, VHS damage | ProductionCrate CRT Factory / VHS Master | Installed plugin, drag onto clip | Subscription, ~$25–39/mo |
| Screen replacement | Mocha Pro (planar track) or Object Mask (2026) | Track the plane, key in replacement | Paid (Mocha) / included in CC |

## Named tools

### Map Route Generator (Marcobelli)
Premiere-native `.mogrt`, up to 20 pins, animated route line. **$29 USD, single-use "Regular
License," seen 2026-08-21 (VideoHive).** Premiere CC 2019+. **Trap:** the listing itself says
After Effects "MUST be installed, even in trial mode" — see Traps.

### World Map ToolKit / World Map Pro
Vector world-map `.mogrt` family: pins, animated lines, country highlight. Bundled in an
**Envato Elements subscription, $16.50/mo annual or $33/mo monthly, seen 2026-08-21** — cheaper
than one-off VideoHive buys past one template a month. AE-dependency unverified per-listing.

### Google Earth Studio
Free, browser-based (Chrome only) camera animator over real Earth imagery; exports an image
sequence or video. **Free, application-gated access, seen 2026-08-21.** **Commercial use of the
imagery is not licensed** — Google's FAQ: no commercial licence currently offered. Hard blocker
for a public release unless separately cleared.

### Mapbox GL JS
Not a Premiere plugin — a JS mapping library: script a dark custom style and camera path, capture
canvas frames, encode with ffmpeg. Full control of the near-black register no MOGRT offers.
Free tier, cost scales with map loads. Higher setup cost, no licensing ambiguity.

### QGIS
Free, open-source desktop GIS. Time Manager or the Atlas/3D view exports a PNG frame sequence
for ffmpeg to assemble. No output-licensing restriction — you own the map data. Best fit when
the map must be *data-accurate*, not just cinematic.

### Infographics / Chart Creator MOGRT packs
Bar/pie/waterfall/radar/KPI-gauge `.mogrt` templates ("Chart Creator V2": 16 styles, up to 30
columns; "Infographics" bundles: 150+ scenes). Roughly **$20–60 each, or in Motion Array's
Everything plan ($24.99/mo annual, $39.99/mo monthly, seen 2026-08-21)** — the practical
Premiere-native stand-in for AE data-viz. No Rive-to-Premiere integration found; treat as closed.

### Boris FX Title Studio
Standalone 3D title app in the Continuum suite — extruded type, camera-animated titles, callouts
the flat Properties/Graphics-Templates panel can't do natively. Ships in the **Boris FX Suite,
$1,495/yr or $219/mo per one 2026 source**; no standalone price confirmed — flag as a gap.

### ProductionCrate — CRT Factory & VHS Master
Vintage-monitor and tape-damage plugin pair: phosphor trails, scanlines, tracking errors.
Subscription pages disagreed **($29/mo, $39/mo, $25/mo-annual all appeared, seen 2026-08-21)** —
state the source with whichever figure you quote. Strong, purpose-built retro-FX reputation,
cited alongside CoreMelt in 2026 roundups.

### Mocha Pro / Premiere Object Mask
Full detail in the tracking/rotoscoping brief; worth repeating here — **Mocha Pro is the only
third-party planar tracker Premiere has**, used to track a phone/monitor plane and key in a
replacement. Native **Object Mask** (2026, AI hover-click) increasingly covers the simple cases
free.

## Automation hook

**Premiere side.**

- **MOGRTs (maps, charts, kinetic titles):** the bridge inserts `.mogrt` files directly — this
  bypasses `VideoFilterFactory.getMatchNames()` entirely, since a MOGRT is a container asset,
  not a registered effect. Discovery step: enumerate Graphics Templates panel MOGRTs by file
  path, insert, then read/set its parameters via the Properties-panel-exposed list — scripting
  surface not independently verified here.
- **Native Crop-effect typewriter:** discovery step — "list effects, filter 'Crop'"; match name
  is commonly `ADBE Crop` elsewhere but **not confirmed against this build**.
- **CRT/VHS plugin effects:** discovery step — "list effects, filter 'CRT'/'VHS'" once
  installed; third-party plugins register their own match names.

**ffmpeg side.**

- **Terminal typewriter reveal — TESTED, run 2026-08-21 in scratchpad.** Two flat-colour overlay
  layers (a "curtain" box the background colour, and a thin cursor bar) composited on top of
  `drawtext`, both driven by expressions in `t`:

  ```bash
  ffmpeg -f lavfi -i color=c=BG:s=1376x768:d=DUR \
    -f lavfi -i color=c=BG:s=CURTAIN_Wx70:d=DUR \
    -f lavfi -i color=c=FG:s=4x50:d=DUR \
    -filter_complex \
    "[0:v]drawtext=fontfile=MONO.ttf:text='TEXT':fontcolor=FG:fontsize=54:x=X0:y=Y0[txt];
     [txt][1:v]overlay=x='X0+(t/REVEAL_S)*TEXT_W':y=Y0-20[masked];
     [masked][2:v]overlay=x='min(X0+(t/REVEAL_S)*TEXT_W,X0+TEXT_W)':y=Y0-10:enable='lt(mod(t,0.6),0.3)'[out]" \
    -map "[out]" -c:v libx264 -pix_fmt yuv420p out.mp4
  ```

  🔴 **Trap found while testing:** the obvious version uses `drawbox` with an animated `x`/`w`
  expression instead of `overlay`. On ffmpeg 4.4.2 that silently fails — `drawbox` has no `eval`
  option in this build (added later upstream), so its geometry is evaluated **once**, at init,
  and never moves. `overlay`'s `x`/`y` **are** evaluated per frame natively, which is why this
  recipe masks with a solid-colour overlay layer instead. Confirmed by extracting frames at four
  timestamps.

- **CRT scanlines — TESTED (runs clean; look not benchmarked against a reference).**

  ```bash
  ffmpeg -i in.mp4 -vf "geq=lum='lum(X,Y)*(0.82+0.18*mod(Y\,2))':cb='cb(X,Y)':cr='cr(X,Y)'" out.mp4
  ```

  Per-pixel darkening of every other scanline. Cheap, no plugin, flatter than a phosphor-glow
  plugin — fine for a brief beat, not a substitute for ProductionCrate on a sustained look.

- **Map/travel footage (Earth Studio, Mapbox, QGIS exports):** once rendered these are just
  clips or stills — no map-specific ffmpeg step exists. Use the eased-zoom (§3.4), crop (§3.8)
  and normalise-then-concat (§3.6) recipes already in
  [`docs/flow/post-production.md`](../../../docs/flow/post-production.md); not repeated here.

## BadCode fit

- **Near-black kills most stock map templates on sight.** World-map MOGRTs default to a light
  base map with saturated pins — every one needs its base-map colour and pin/line palette
  overridden to the muted cool-neutral register before it reads as BadCode, not corporate deck.
- **The terminal-typing recipe is a direct hit for GPOM** — "the title is typed as a git
  command" is exactly the overlay+drawtext pattern above: 1376×768, one thin light (the cursor),
  one line of monospace on black, no plugin.
- **8s clips are too short for most kinetic-type packs**, built for 3–5s title cards inside a
  longer edit — expect to trim mid-animation or pick a pack's shortest preset.
- **Chart/infographic MOGRTs read as pitch-deck, not documentary** — restyle hard (thin lines,
  no drop shadows, no gradient fills) or the panel breaks the 35mm-documentary register the rest
  of the piece sits in.

## Traps

- **Map Route Generator (and likely other VideoHive map MOGRTs) require After Effects installed,
  even though it never runs** — confirmed on the listing itself. AE is **not installed** here;
  check per-listing before buying.
- **Google Earth Studio footage cannot be used commercially** — confirmed in Google's own FAQ.
  Treat a flyover as reference/storyboard only unless a separate licence is obtained.
- **`drawbox` geometry expressions do not animate per-frame on ffmpeg 4.4.2** — no `eval` option
  in this build. A tutorial's "obvious" drawbox-mask typewriter recipe produces a frozen mask
  silently. Use `overlay` instead (Automation hook, above).
- **Rive was searched for explicitly and found nothing** — no Premiere/MOGRT integration turned
  up. Don't assume one exists.
- **Pricing is inconsistent across a vendor's own pages** — ProductionCrate alone returned three
  different monthly figures in one pass. State the source and date for whatever you quote.
- **"Essential Graphics panel" no longer exists as a single panel** as of Premiere 25.0 — split
  into the Properties panel (editing) and Graphics Templates panel (browsing). Workflow is the
  same; the panel name and location are not.

## Sources

- [Map Route Generator — VideoHive listing](https://videohive.net/item/map-route-generator-for-premiere-pro/25704898) — 2026-08-21 — price, licence, AE-required trap
- [Google Earth Studio](https://www.google.com/earth/studio/) — 2026-08-21 — free, Chrome-only, AE camera export
- [Google Earth Studio FAQ](https://earth.google.com/studio/) — 2026-08-21 — access model, no commercial imagery licence
- [Properties panel — Adobe Helpx](https://helpx.adobe.com/premiere-pro/using/about-properties-panel.html) — 2026-08-21 — post-25.0 home for graphics editing
- [New Properties Panel in Premiere 25 — Larry Jordan](https://larryjordan.com/articles/the-new-properties-panel-in-adobe-premiere-pro-25-0/) — 2026-08-21 — details the Essential Graphics split
- [mTitle product pages — MotionVFX](https://www.motionvfx.com/store/adobe-premiere-after-effects) — 2026-08-21 — per-title pricing ($89–$119)
- [Boris FX Suite 2026 Release — Toolfarm](https://www.toolfarm.com/news/boris-fx-suite-2026/) — 2026-08-21 — Suite price bundling Title Studio
- [Envato Elements pricing — StackScored](https://www.stackscored.com/pricing/stock-media/envato-elements/) — 2026-08-21 — annual/monthly figures
- [Motion Array Unlimited](https://motionarray.com/unlimited/) — 2026-08-21 — Everything plan price
- [ffmpeg overlay filter docs](https://ffmpeg.org/ffmpeg-filters.html#overlay-1) — 2026-08-21 — per-frame x/y expression evaluation, used above
