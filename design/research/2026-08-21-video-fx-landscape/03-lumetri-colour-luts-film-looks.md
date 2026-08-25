# Lumetri, colour management, LUTs and film looks

## What this covers

Premiere's native Lumetri Color panel and 2026 colour-management/tone-mapping stack; the `.cube`
LUT workflow (Input vs Creative, install paths); free LUT packs; the paid film-emulation market
(FilmConvert Nitrate, Dehancer, Magic Bullet Looks, Cinegrain-style overlays); and grain/halation/
bloom, both native and ffmpeg-side. Framed for BadCode's actual footage — near-black, low-key,
1376×768, 8-second Veo 3.1 clips — where the risk is crushing already-compressed shadow detail,
not adding more "cinematic" contrast.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
|---|---|---|---|
| Primary grade | Lumetri Color (native) | Basic Correction + Curves tabs, per-clip or adjustment layer | included |
| Technical/log LUT | Lumetri Input LUT | Drop `.cube` in the Technical folder, pick from Basic Correction | included |
| Stylised look LUT | Lumetri Creative LUT | Drop `.cube` in the Creative folder, pick from Creative tab | included |
| Mixed-gamut sequence | Sequence Color Management | Direct 709 / Wide Gamut (Tone Mapped) preset auto tone-maps | included |
| Camera-accurate film stock | FilmConvert Nitrate | Camera profile + film LUT plugin, adjustable grain | $119 one-time |
| Deep analog emulation | Dehancer Pro/Lite | Ordered stack: negative → print → grain → optics | $199–449 |
| Preset "movie look" | Magic Bullet Looks | 300+ preset browser, node-customisable | subscription only |
| Scanned grain overlays | Cinegrain-style packs | Overlay clip, blend mode, opacity | $76–$999/pack |
| Free starting LUTs | RocketStock / IWLTBAP | `.cube` files into Creative folder | free |
| No-plugin grain | "Noise HSL Auto" effect | Apply, switch Noise type Uniform → Grain | included |
| Scriptable batch grade | ffmpeg `lut3d`+`curves`/`noise`/`vignette` | Filter chain on export | free |

## Named tools

### Lumetri Color (native)
Six tabs: **Basic Correction** (WB, Exposure/Contrast/Highlights/Shadows/Whites/Blacks,
Saturation), **Creative** (Creative LUT, Faded Film, Sharpen, tint wheels), **Curves** (RGB,
Hue-vs-Sat/Hue/Luma, Luma-vs-Sat), **Color Wheels & Match** (3-way wheels + AI Color Match),
**HSL Secondary**, **Vignette**. Price: included with any Premiere/CC seat. Platform: Win/Mac,
built in. Maturity: default grading tool for most editors; 2026 builds added improved tone-mapping/
gamut-compression math and an "Apply Inverse Tone Mapping and Gamut Compression" advanced toggle —
sourced from a search-index summary of the Adobe helpx page, the live fetch itself timed out, so
treat exact toggle wording as **unverified paraphrase**.

### FilmConvert Nitrate
Camera-sensor profile + film-stock print-density plugin with adjustable grain and a custom
response curve. Price: **$119** (RRP $149), one-time, 3 activation seats; Pro→Nitrate upgrade $29
— filmconvert.com/purchase, 2026-08-21. Platform: Win/Mac, Premiere/AE/OFX. Install: plugin
installer, appears in Effects panel (not inside Lumetri). Maturity: long-standing, well-reviewed
camera-profile look tool (ProVideoCoalition), not a 2026 newcomer.

### Dehancer (Pro / Lite)
Ordered analog pipeline — negative → print → halation/bloom → grain → optics (aberration,
vignette, gate weave) — not a single LUT. Price: **Pro $449 perpetual**; **Lite** quoted two
conflicting ways in the same pass — "$199 perpetual" on one page, "subscription plans only, no
perpetual option" on another — both dehancer.com, 2026-08-21. **Check dehancer.com/pricing
directly before quoting Lite.** Platform: Win/Mac, Premiere/AE/Resolve/FCP. Maturity: reviewed
2025–26 as the most process-correct analog emulation (Henry David Photography, Theotivity), the
"deep/technical" option versus FilmConvert's faster presets.

### Magic Bullet Looks
Preset-driven "match this movie" grading, node-based, part of Red Giant's Magic Bullet Suite.
Price: **no longer sold standalone/perpetual** — bundled only in Red Giant Complete or Maxon One;
figures across Red Giant's own site ranged $30–32/mo, ~$199/yr, and $214/yr for the wider Universe
line in one pass (source page 2026-02, re-seen 2026-08-21) — vendor pricing is genuinely
inconsistent, state the exact page when quoting. Platform: Win/Mac, Premiere/AE. Maturity: 300+
Looks, well known; the subscription-only shift is the bigger story than the feature set.

### Cinegrain-style scanned grain/look packs
Licensed scans of real film stocks (35/16/8mm grain, light leaks, splices), applied as overlay
clips via blend mode, not a plugin. Price: **roughly $76–$999** per full pack, seen 2026-08-21,
flagged by the source itself as a pricier corner of the market. **Caveat**: the page returning this
pricing was under the domain `cinegrams.com`, not a confirmed `cinegrain.com` — the domain match is
**unverified**, a gap. Cheaper comparables exist: Jonny Elwyn, PremiumBeat, Melior Studios all list
free–$99 grain packs in the same pass.

### RocketStock & IWLTBAP free LUT packs
RocketStock's 35 free cinematic/vintage `.cube` LUTs (Bourbon 64, Contrail, Korben…); IWLTBAP's
10-LUT preview (sampler for a 99+-LUT paid set). Free, both seen 2026-08-21. Maturity: both
recur across independent 2025–26 "best free LUTs" roundups (StudioBinder, FilmDaft, PresetPro) —
reliable as a baseline, not a finished BadCode look.

## Automation hook

**Premiere side.** Lumetri's match name is reported on Adobe's own community forum as
**`AE.ADBE Lumetri`** (`effect.matchName === "AE.ADBE Lumetri"` in ExtendScript) — community-
sourced, not an official API reference, verify before hard-coding. None of Nitrate/Dehancer/Magic
Bullet/Cinegrain publish a documented match name. Discovery step for any of them: apply once by
hand to a throwaway clip, enumerate `VideoFilterFactory.getMatchNames()`, diff against a clean-
project baseline — the new entry is the match name. Cache per plugin version; vendors rename
internally across majors without announcing it.

**ffmpeg side** — all five recipes ran against a synthetic 1376×768 near-black test clip this
session, exit code 0 (`fx-test/`, ffmpeg 4.4.2):

- **Apply a `.cube` LUT** — TESTED: `ffmpeg -i in.mp4 -vf "lut3d=file=look.cube" out.mp4`
- **Film grain** — TESTED: `ffmpeg -i in.mp4 -vf "noise=alls=20:allf=t+u" out.mp4`
- **Vignette** — TESTED: `ffmpeg -i in.mp4 -vf "vignette=PI/4" out.mp4`
- **Halation/bloom** (threshold highlights → blur → screen-blend back) — TESTED:
  `ffmpeg -i in.mp4 -filter_complex "[0:v]split=2[a][b];[b]lutyuv=y='if(gt(val,180),val,0)',gblur=sigma=12[glow];[a][glow]blend=all_mode=screen" out.mp4`
- **Shadow lift + cool cast without crushing near-black to 0** — TESTED:
  `ffmpeg -i in.mp4 -vf "curves=master='0/0.02 0.5/0.5 1/1',colorbalance=rs=-0.05:bs=0.08" out.mp4`

Full options for `lut3d`/`noise`/`vignette`/`curves`/`colorbalance`/`gblur`/`geq`: `ffmpeg -h
filter=<name>` locally — verified present in this environment's ffmpeg 4.4.2 build.

## BadCode fit

- **Grade off the near-black floor, not off 0.** Veo output already sits near the crush point; an
  Input LUT or hard contrast push can flatten shadow detail permanently. The tested curves skeleton
  (`0/0.02 …`) never maps pure black to pure black.
- **Order matters.** Grain before a Creative LUT gets crushed/recoloured by it; grain after sits on
  top as texture. Dehancer's pipeline encodes this order; ffmpeg doesn't — sequence LUT → lift →
  grain → vignette deliberately.
- **Don't stack grain on Veo's own noise.** 8s clips at 1376×768 already carry generation
  artifacts; a second grain pass can double up rather than read as one film stock. Test low
  `alls`/opacity on real footage — the synthetic test clip here can't reveal Veo's actual noise
  floor, a live unknown.
- **Halation suits the single-light, monumental-dark register** — the screen-blend skeleton only
  blooms above-threshold pixels, the right shape here; a flat vignette or grain wash isn't.
- **Blend-mode overlay grain is riskier than filter grain on near-black** — Screen blend lifts
  blacks by definition wherever the grain noise floor isn't exactly 0. Test Overlay/Soft Light
  against the real dark base before buying a pack.

## Traps

- Lumetri's `AE.ADBE Lumetri` match name is forum-sourced, not documented — confirm by enumeration
  before the bridge depends on it.
- Vendor pricing is inconsistent within one vendor's own site (Dehancer Lite, Red Giant/Magic
  Bullet both confirmed above) — always state source page + access date, never pick one silently.
  Cinegrain's domain itself is unconfirmed — a gap.
- LUTs need a full Premiere restart after copying `.cube` files into system folders, not just a
  panel refresh — a script expecting instant availability fails silently (Adobe community, 2026-08-21).
- Creative-folder vs Technical-folder placement changes which dropdown (Creative Look vs Input LUT)
  the same `.cube` shows in — easy to "successfully" install a LUT nobody can find.
- Magic Bullet Looks has no one-time perpetual licence any more — a cost estimate built on an old
  perpetual price will be wrong.
- ffmpeg filter syntax here was verified against the local 4.4.2 build, not re-fetched from
  ffmpeg.org this session (search budget ran out first) — low-risk gap, these options are stable
  across 4.x–6.x.

## Sources

- https://helpx.adobe.com/premiere-pro/using/lumetri-color-panel-effects.html — accessed 2026-08-21, Lumetri panel tabs/params (search-index summary; live fetch timed out)
- https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/tone-mapping-in-premiere.html — accessed 2026-08-21, 2026 tone-mapping/gamut-compression presets
- https://community.adobe.com/questions-729/faq-premiere-pro-lumetri-color-custom-lut-directory-and-location-1345790 — accessed 2026-08-21, Windows/Mac LUT install folder paths
- https://community.adobe.com/t5/premiere-pro-discussions/javascript-api-to-change-premiere-pro-lumetri-color/m-p/9045922 — accessed 2026-08-21, `AE.ADBE Lumetri` match name (community, unverified)
- https://www.filmconvert.com/purchase — accessed 2026-08-21, Nitrate $119/RRP $149 one-time price
- https://www.dehancer.com/pricing — accessed 2026-08-21, Pro $449 perpetual, Lite pricing conflict
- https://phoenix-3d-art.blogspot.com/2026/02/red-giant-magic-bullet-suite-software.html — accessed 2026-08-21, Magic Bullet subscription-only shift
- https://borisfx.com/blog/how-to-add-film-grain-in-premiere-pro-3-methods/ — accessed 2026-08-21, native Noise HSL Auto grain method
- ffmpeg 4.4.2 local binary, `-h filter=lut3d|noise|vignette|curves` — verified 2026-08-21, primary source for filter syntax (ffmpeg.org docs not independently re-fetched this session)
