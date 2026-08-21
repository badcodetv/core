# Video-fx landscape sweep

Twenty research briefs mapping what Premiere Pro 26.3.2, ffmpeg 4.4.2, and the free plugin/tool
ecosystem can actually do to Flow/Veo footage and Suno tracks — the raw material for
`docs/video-fx/` and the future `video-fx` skill. Commissioned as T16 of
[`design/2026-08-21-premiere-bridge-and-video-fx.md`](../../2026-08-21-premiere-bridge-and-video-fx.md);
T17 (toolkit distillation) is what turns this pile into the doc set and the skill. Briefs 19 and
20 close two of the sweep's own [Gaps](#gaps), commissioned 2026-08-21 under a same-day ruling:
**BadCode buys no paid plugins** — the free stack (Premiere built-ins, the ex-Film-Impact
transitions, Lumetri, MOGRTs, ffmpeg) plus Flow is the whole toolkit, so briefs 19–20 name no
prices and no paid tools.

**Correction to the brief:** the task that launched this pass listed `17-ffmpeg-audio-filters.md`
as failed to write. It exists (11,296 bytes, 7 sources, tested skeletons) and is included below
as a full row — treat it as delivered, not missing.

## Briefs

| # | Brief | Summary | Tools named | Paid tools | Sources |
| --- | --- | --- | --- | --- | --- |
| 01 | [premiere-builtin-video-effects](01-premiere-builtin-video-effects.md) | Premiere's native effect bins (Blur, Distort, Keying, Stylize, Warp Stabilizer…) with match names and GPU-accel status where documented | 14 | none | 11 |
| 02 | [transitions-essential-graphics-mogrt-titles](02-transitions-essential-graphics-mogrt-titles.md) | Native transitions (Film Impact now free/built-in), the Properties/Graphics-Templates panel split, MOGRT sourcing, transcript captions | 10 | MotionVFX mTitles $89–99; CoreMelt V2 $79 (+6 more) | 12 |
| 03 | [lumetri-colour-luts-film-looks](03-lumetri-colour-luts-film-looks.md) | Lumetri's six tabs, LUT install workflow, five film-emulation tools, near-black grading recipes | 7 | FilmConvert Nitrate $119; Dehancer Pro $449 (+3 more) | 9 |
| 04 | [particles-fire-smoke-weather-vfx](04-particles-fire-smoke-weather-vfx.md) | Native/stock/plugin/AI routes to fire, smoke, sparks, weather; Trapcode Particular confirmed AE-only | 12 | ActionVFX $24–79/mo; Boris FX Continuum $365–2,195 (+5 more) | 13 |
| 05 | [maps-motion-graphics-kinetic-text](05-maps-motion-graphics-kinetic-text.md) | Map/chart/kinetic-type MOGRTs, Google Earth Studio (commercial-use ban flagged), a working terminal-typewriter ffmpeg recipe | 9 | Map Route Generator $29; World Map Pro $16.50/mo (+3 more) | 10 |
| 06 | [premiere-ai-features-captions](06-premiere-ai-features-captions.md) | Generative Extend, Auto Reframe, Enhance Speech, Object Mask, Auto Captions, and which of these have any UXP hook at all | 11 | Firefly Video Model $10–29.99/mo; Adobe Podcast Premium $9.99/mo | 11 |
| 07 | [paid-suites-boris-redgiant-maxon-filmconvert-dehancer](07-paid-suites-boris-redgiant-maxon-filmconvert-dehancer.md) | 16-tool price/compatibility comparison of the big plugin suites; confirms no vendor publishes Premiere match names | 16 | Boris FX Continuum $325/yr; Dehancer Pro $449 (+12 more) | 14 |
| 08 | [free-plugins-and-template-ecosystem](08-free-plugins-and-template-ecosystem.md) | Free/cheap plugin and template ecosystem, reset by Adobe folding Film Impact natively into 25.5 | 13 | Motion Array $24.99/mo; Adobe Stock templates $29.99/mo (+2 more) | 10 |
| 09 | [after-effects-crossover-dynamic-link](09-after-effects-crossover-dynamic-link.md) | The honest AE-only boundary (particles, 3D comp, planar tracking) vs Premiere-native and non-AE routes (Cavalry, Rive, Resolve/Fusion) | 8 | After Effects £21.98–34.49/mo; Mocha Pro $325–655/yr (+5 more) | 10 |
| 10 | [speed-retime-stabilise-warp](10-speed-retime-stabilise-warp.md) | Time Remapping, Optical Flow, Warp Stabilizer, Morph Cut vs Twixtor/Mercalli/ReelSteady vs free ffmpeg equivalents | 8 | Twixtor Pro $595; Mercalli V6 SAL ~$199–299 (+1 more) | 8 |
| 11 | [audio-ducking-denoise-narration-mix](11-audio-ducking-denoise-narration-mix.md) | Essential Sound auto-ducking, Enhance Speech, DeNoise/DeReverb, iZotope RX, per-platform LUFS targets (Premiere GUI side) | 10 | iZotope RX 12 Standard $399; Adobe Podcast Premium $9.99/mo (+3 more) | 11 |
| 12 | [ffmpeg-filter-map](12-ffmpeg-filter-map.md) | By-need index of ffmpeg 4.4.2's whole filter graph; nothing needs a newer ffmpeg, the real gap is uninstalled external tools | 8 | Premiere Pro $22.99/mo; CC Pro $69.99/mo | 10 |
| 13 | [ffmpeg-colour-lut-grain](13-ffmpeg-colour-lut-grain.md) | LUTs, curves, procedural grain, halation, vignette, HDR tonemap traps at the ffmpeg↔Premiere colour-tagging boundary | 18 | Dehancer Film $12–99/mo (Pro $449, Lite $199); FilmConvert Nitrate $149 | 7 |
| 14 | [ffmpeg-xfade-overlay-blend-chroma](14-ffmpeg-xfade-overlay-blend-chroma.md) | xfade's 43 transitions, PIP/split-screen, blend modes, chroma/luma keying, procedural masks — 9 of 13 recipes live-tested | 13 | none | 7 |
| 15 | [ffmpeg-drawtext-subtitles-ass](15-ffmpeg-drawtext-subtitles-ass.md) | drawtext, ASS/libass subtitle burn-in with karaoke timing, two typewriter routes, the GPOM terminal-green look | 7 | none | 7 |
| 16 | [ffmpeg-zoompan-vidstab-minterpolate](16-ffmpeg-zoompan-vidstab-minterpolate.md) | Rotation/parallax, vidstab stabilisation, minterpolate, motion blur, and the Real-ESRGAN/RIFE/Topaz upscale routes past Flow's 1376×768 ceiling | 14 | Topaz Video AI Personal $299/yr; Pro $699/yr | 6 |
| 17 | [ffmpeg-audio-filters](17-ffmpeg-audio-filters.md) | ffmpeg counterpart to brief 11: sidechaincompress ducking, two-pass loudnorm, afftdn/anlmdn denoise, rubberband retime | 9 | none | 7 |
| 18 | [ffmpeg-adjacent-frei0r-vapoursynth-mlt-gl-transition](18-ffmpeg-adjacent-frei0r-vapoursynth-mlt-gl-transition.md) | 10 tools adjacent to ffmpeg; frei0r and ImageMagick live-verified and recommended now, VapourSynth/MLT flagged as a future pilot | 10 | Remotion Company $100+/mo; Enterprise $500+/mo | 10 |
| 19 | [delivery-specs-and-qc-scopes](19-delivery-specs-and-qc-scopes.md) | YouTube/Shorts, TikTok, Instagram Reels delivery specs (resolution, codec, bitrate, loudness) and how to QC a finished file (ffprobe, signalstats/waveform/vectorscope, blackdetect/freezedetect); live-tested a real full/limited-range mismatch trap in near-black footage | 5 | none — no paid tools in scope | 7 |
| 20 | [beat-synced-and-audio-driven-cutting](20-beat-synced-and-audio-driven-cutting.md) | Tempo/beat-grid extraction from a Suno track (aubio, librosa, Essentia tested live; madmom's install failed) and turning it into Premiere markers or an ffmpeg cut plan; D&B phrase-structure editing craft | 6 | none — no paid tools in scope | 8 |

## Gaps

What an editor would ask this toolkit that no brief actually answers:

- ✅ **CLOSED — "What codec/aspect-ratio/bitrate does this need to hit for YouTube Shorts / TikTok / Instagram, and how do I check it before I ship?"** Answered in [brief 19](19-delivery-specs-and-qc-scopes.md), which also fulfils brief 12's promise that this content lands in "briefs 13–18."
- ✅ **CLOSED — "Cut this to the beat"** — answered in [brief 20](20-beat-synced-and-audio-driven-cutting.md).
- **"Give me rotating 3D text / an extruded logo"** — brief 09's decision table is honest that this is AE-only territory (no Premiere-native 3D text engine) but doesn't resolve whether a MOGRT can fake it acceptably; MOGRT-side 3D text templates were never checked.
- **"Read/set a MOGRT's exposed parameters from the bridge"** — briefs 02, 05, and 08 each raise this and each leave it unresolved (Properties-panel scripting surface unconfirmed); it's the single most-repeated unresolved question in the whole sweep and would block MOGRT automation specifically, not just text-styling automation.

## Contradictions

- **Dehancer Lite price and licence model.** Brief 03 flags this as *internally* contradictory on Dehancer's own site (perpetual $199 vs subscription-only, same domain) and leaves it unresolved. Brief 07 then states flatly "$199 subscription-only," and brief 13 states flatly "perpetual 'Lite' $199" — so the sweep now has two briefs asserting opposite licence models at the same price point, neither flagging the other's claim. Needs one resolving check against dehancer.com before this price appears in `docs/video-fx/`.
- **Boris FX Sapphire price.** Brief 04 gives specific figures ("$545–$985/yr or $80–$144/mo; $1,865–$3,075 perpetual"). Brief 07, researching the same product later, says the price is "not published (gap) — bundle only." One of these is wrong, or Sapphire's sale structure changed between the two research passes on the same day.
- **Mocha Pro perpetual ceiling.** Brief 07 puts the top perpetual tier at "$1,645"; brief 09 puts it at "$1,095 with 1yr upgrades/support" for what reads as the same top tier. A $550 gap on the same product on the same day.
- **CoreMelt's product line.** Brief 02 names "V2 plugin pack ($79 single / $199 8-pack)"; brief 07 names different tier labels ("Lock & Load," "Everything Bundle") as unconfirmed. Either CoreMelt sells both lines or the two briefs found different vendor pages for the same product — not reconciled.

## Weak briefs

No brief fell under the 5-source floor (range is 6–14), so the risk here is unsourced/thin-sourced *prices* and vendor-marketing claims dressed as fact, not overall thinness:

- **04** (particles/fire/smoke) — ActionVFX and ProductionCrate's pricing pages both 403'd; every price for those two vendors is a search-snippet or vendor-blog figure, not the live pricing page. Also carries a Red Giant VFX Suite price forward from prior notes without re-verifying. Fix: re-fetch both pricing pages with a different user-agent/route, or drop to "price unconfirmed" rather than a specific figure.
- **06** (Premiere AI features) — the "Scene Edit Detection gives a 40%+ efficiency gain" figure is sourced to a vendor/blog post, not Adobe or an independent benchmark, and is stated in the brief's body without a hedge. Fix: either hedge it inline ("per [vendor]'s own claim") or cut it before it lands in `docs/video-fx/` as fact.
- **09** (AE crossover) — the UK After Effects price (£21.98/month) is sourced only to a search cache, never a live fetch of adobe.com/uk. Fix: re-fetch before quoting a GBP figure anywhere public-facing.
- **10** (speed/retime/stabilise) — Mercalli V6 SAL's price is self-conflicting across proDAD's own pages ($199–$299) and ReelSteady's is self-conflicting across GoPro's own channels ($99/yr plugin vs $99.99 one-time IAP); both already flagged inline but neither resolved. Fix: one direct checkout-page check per product before quoting.
- **16** (zoompan/vidstab/minterpolate) — lowest source count in the sweep (6), and it's the brief carrying Topaz Video AI's only pricing ($299–$699/yr); the rest of the brief is heavily self-tested so the low count is less alarming than it looks, but the Topaz figures specifically ride on a single source. Fix: cross-check Topaz's price against a second source before quoting.
