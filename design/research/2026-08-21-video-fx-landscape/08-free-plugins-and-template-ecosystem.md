# Free and cheap: plugins, presets, templates, stock

## What this covers

The free/cheap edge of Premiere for an 8-second-clip, near-black, documentary-style edit:
free transition/preset plugins, `.prfpset` preset packs and whether they're scriptable,
template marketplaces and subscription prices, two live GitHub projects, and the licence
traps that bite a small collective publishing repeatedly to YouTube. Not covered: paid VFX
suites and native Premiere AI — other briefs in this set. The single biggest fact for 2026:
**Adobe bought FilmImpact and folded its entire transition library into Premiere itself**,
which resets what "free plugin" means here.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
|---|---|---|---|
| Cinematic transitions (dissolve, push, glitch) | Native transition bin (post-25.5) | Already installed — was FilmImpact's paid library | Included |
| More transitions/titles/SFX, drag-and-drop | Motion Bro panel | Install panel, browse free 1,400-asset starter pack | Free (paid on top) |
| Same, via Adobe's own marketplace | Premiere Composer (Adobe Exchange) | Install UXP panel, drag starter-pack items to timeline | Free (paid on top) |
| One-click preset transitions/effects (AE-style) | AEJuice Pack Manager | Install Pack Manager, pull any of 26 free packs | Free (paid on top) |
| Extra transitions outside Adobe's own bin | CoreMelt Free | Download installer, restart Premiere | Free |
| GPU particles (fire, smoke, magic) without AE | Particle Illusion (standalone) | Render alpha video, import as a clip | Free — licence disputed, see Traps |
| Reusable colour/zoom/shake preset you built once | `.prfpset` file | Right-click Presets bin → Import Presets → drag onto clip | Free (self-authored) |
| Animated title/lower-third without After Effects | MOGRT from a marketplace | Subscribe, drag `.mogrt` onto timeline, edit in Essential Graphics | £–££/mo |
| Large stock + template + SFX library | Motion Array Everything plan | Subscribe, Standard Universal Licence covers the project | $24.99–39.99/mo |
| Same, broader library | Envato Elements | Subscribe, one licence per project (see Traps) | $16.50/mo (annual) |
| No-budget, commercial-safe templates | Mixkit | Download `.mogrt`, no account, no attribution | Free |
| Occasional premium template/LUT, no subscription | Adobe Stock trial/credits | 10 assets free month one, then $29.99/mo for 10/mo | Free trial → $29.99/mo |
| Dialogue-track cleanup in the audio mixer | ReaPlugs (Cockos) | Install VST, scan in Premiere audio prefs | Free |

## Named tools

### FilmImpact (now native)
Was a paid transition/effect plugin, acquired by Adobe. PRICE: **£0 — fully absorbed into
Premiere as of v25.5**, confirmed 2026-08-21; old paid licences keep working ~12 more
months, renewals switched off. Built in, nothing to install. Was the top "best free plugin"
recommendation everywhere in 2025 — those posts are now stale.

### Motion Bro / Premiere Composer / AEJuice — the drag-and-drop panel trio
All three follow one pattern: install a free panel, browse a bundled free starter pack,
drag items onto the timeline; paid packs sit on top (none of the three's paid-pack prices
were confirmed this pass — gap). **Motion Bro** (Win/mac, AE+Premiere): free panel + ~1,400
starter items; actively updated into 2026. **Premiere Composer**: one of Adobe Exchange's
most-downloaded free extensions, install via Exchange → Creative Cloud desktop; repeatedly
named the top free Exchange transitions extension in 2026 roundups. **AEJuice**: free "Pack
Manager" installer gates 26 currently-free packs (transitions, motion elements, AI voiceover,
captions, GIF export); still promoted as "the best free plugin" in 2026 coverage.

### CoreMelt Free
Standalone bundle of 44 transition/text/instant-montage effects. PRICE: **£0, no watermark,
no time limit** per vendor. Install: installer from coremelt.com/pages/get-free, restart
Premiere. Maturity: cited as a stronger free offer than FilmImpact's old "4 forever" — moot
now FilmImpact is native.

### Particle Illusion (free standalone)
Boris FX's GPU particle generator (fire, smoke, magic), spun out of Continuum. PRICE:
**£0 standalone**, no watermark; licence conflict — see Traps. Paid Pro/plugin editions on
top ($95/yr, $15/mo, or $295 perpetual per CGChannel/Boris FX — not re-verified for 2026,
possibly stale). No native Premiere panel — exports alpha video to import as a clip. The
standard Trapcode-Particular substitute for a Premiere-only workstation.

### Motion Array
Subscription marketplace — templates, footage, music, SFX, LUTs, plugins. PRICE:
**Everything plan $24.99/mo annual or $39.99/mo monthly**, seen 2026-08-21; plans "revise
frequently" per reviewers — treat as a snapshot.

### Envato Elements
Flat-rate subscription, 16M+ assets incl. 800,000+ templates/footage. PRICE: **$16.50/mo
annual**, seen 2026-08-21. The licensing model (Traps) matters more than catalogue quality.

### Mixkit
Free-asset site — stock video, music, SFX, `.mogrt` templates. PRICE: **£0**, no account or
attribution required. Maturity: the genuinely-free, commercial-safe baseline; smaller and
more generic-looking than the paid marketplaces.

### Adobe Stock (templates)
Adobe's own marketplace, integrated into Premiere's Libraries panel. PRICE: **first month
free (10 assets)**, then **$29.99/mo for 10/mo**, seen 2026-08-21; a separate always-free
collection sits at stock.adobe.com/free (90,000+ clips).

### ReaPlugs (Cockos)
Free, unlimited, no-registration VST suite (ReaEQ, ReaComp, ReaGate) — audio, not video.
PRICE: **£0**, genuinely free. Adjacent to this brief's video scope but named by multiple
2026 "free plugin" roundups anyway.

### GitHub / open-source
**OpenCut** (`SysAdminDoc/OpenCut`) — free/open extension aiming at AI editing automation,
captions, effects; positioned to "replace the leading paid Premiere extensions" but maturity
unverified, no adoption data pulled — flag as a gap. **jumpcut** (`cameron-astor/jumpcut`) —
small open-source silence/jump-cut remover. Neither was load-tested this session.

## Automation hook

**Premiere side.** No plugin ships documented "match names" — the list is undocumented
per-vendor. Discovery step, confirmed against the Premiere Pro Scripting Guide
(docsforadobe.dev): call `qe.project.getVideoEffectList()` (the unsupported-but-working QE
DOM) to enumerate every installed effect's `matchName`, then `getVideoEffectByName()` for one
by display name — e.g. native Gaussian Blur is `"AE.ADBE Gaussian Blur 2"`. Installed
third-party effects (FilmImpact-now-native, CoreMelt, Motion Bro items once dropped on a
clip) show up in that same list — filter for the vendor name. **Applying a saved `.prfpset`
programmatically is not directly exposed**: no documented API imports/applies a preset file;
the workaround is parsing the preset's XML by hand and replaying its values as parameter
calls. Budget the UXP bridge for a "parse `.prfpset` XML → replay as `setParamValue` calls"
adapter, not an assumed one-line apply.

**ffmpeg side** (skeletons only, closest free-tier equivalents; run in scratchpad, not repo):

```
# Cross-dissolve — the free-transition-pack equivalent — UNTESTED
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "xfade=transition=fade:duration=1:offset=7" out.mp4

# Apply a free/cheap LUT (.cube) — the marketplace colour-pack equivalent — UNTESTED
ffmpeg -i in.mp4 -vf "lut3d=file=pack.cube" out.mp4

# Lower-third text — the free MOGRT-template equivalent — UNTESTED
ffmpeg -i in.mp4 -vf "drawtext=fontfile=font.ttf:text='BADCODE':x=40:y=h-100:fontsize=36" out.mp4
```

None of these ran this session. Canonical xfade/zoompan/concat recipes already live at
`docs/flow/post-production.md` — validate against it, don't duplicate.

## BadCode fit

Near-black, one-thin-light, 8-second AI clips at 1376×768 punish anything decorative. Most
free transition packs (FilmImpact-legacy, CoreMelt, Motion Bro, AEJuice) lean glitch/light-
leak/whip-pan — wrong register for a flat documentary tone; the now-native FilmImpact set is
worth a filtered pass for the quiet options (plain dissolve, soft push) only. Particle
Illusion's free sims (embers, dust, smoke) could earn a place in the dark machine-hall
imagery — a thin drift reads as atmosphere, not decoration — but keep density low and colour
desaturated; defaults are colourful and will fight the grade. Mixkit and Adobe Stock's free
collection are the safest zero-cost start for lower-thirds/titles, but strip branding
defaults (bright accents, bouncy easing) down to BadCode's flatter motion language. Avoid
Motion Array/Envato's "trending" templates outright — generic corporate/social, the opposite
of the register.

## Traps

- **CEP is dying now, not eventually.** Premiere 2026 stopped natively loading legacy CEP
  extensions (live GitHub bug against a CEP auto-subs extension; Hyper Brew's 2026-03-31
  UXP-standard-release post). Confirm "UXP" explicitly before installing anything here.
- **Envato Elements: one licence per project, not per subscription** — reusing a downloaded
  asset across separate YouTube uploads technically needs a new licence certificate each
  time per the FAQ; a friction point for a channel publishing repeatedly.
- **Motion Array / Envato forbid redistributing assets as templates, stock, or standalone
  files** — the licence covers using an asset inside a finished project, not passing it on.
- **Particle Illusion's free licence is stated two ways by two Boris FX-adjacent sources** —
  one says free for any use including professional work, another says non-commercial/personal
  only. Unresolved from open search; confirm with Boris FX before shipping it in a release.
- **Adobe Stock's "10 free assets" is a trial, not a permanent tier** — auto-bills $29.99/mo
  from month two; don't confuse it with the separate, permanently-free stock.adobe.com/free.
- **Krock.io is a review/collaboration panel, not an effects plugin** — appeared in "free
  Premiere plugin" roundups (and this brief's source list) but does commenting, not effects.
- **FilmImpact's move to native Premiere makes older buy/price pages stale** — any 2024–25
  source quoting a FilmImpact subscription is superseded by the 2026 acquisition.

## Sources

- [FilmImpact — A New Chapter for Creativity](https://www.filmimpact.com/resources/blog/a-new-chapter-for-creativity) — 2026-08-21 — confirms Adobe acquisition, native-integration date
- [Hyper Brew — UXP Plugins in Premiere 2026](https://hyperbrew.co/blog/uxp-plugins-in-premiere-2026/) — 2026-08-21 — CEP deprecation timeline, UXP release date
- [Adobe — Apply effect presets in Premiere](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/apply-effect-presets.html) — 2026-08-21 — official `.prfpset` install steps
- [Premiere Pro Scripting Guide (docsforadobe.dev)](https://ppro-scripting.docsforadobe.dev/) — 2026-08-21 — matchName property, QE effect-list API
- [CoreMelt — Get Free](https://coremelt.com/pages/get-free) — 2026-08-21 — free 44-effect bundle, no watermark claim
- [Boris FX — Particle Illusion: Free Standalone & Premium](https://borisfx.com/videos/particle-illusion-free-standalone-premium-plugin/) — 2026-08-21 — free-standalone licence claim
- [Envato Elements — License FAQ](https://help.elements.envato.com/hc/en-us/articles/360000629346-Envato-Elements-License-FAQ) — 2026-08-21 — per-project licensing, redistribution ban
- [Motion Array — License](https://motionarray.com/license/) — 2026-08-21 — Standard Universal Licence, redistribution ban
- [Mixkit — free video templates](https://mixkit.co/free-premiere-pro-templates/) — 2026-08-21 — free, no-attribution commercial claim
- [GitHub — auto-subs issue #571](https://github.com/tmoroney/auto-subs/issues/571) — 2026-08-21 — live evidence of a CEP extension breaking under 2026

**Gaps:** exact paid-tier prices for Motion Bro, Premiere Composer, and AEJuice packs (only
free tiers documented); no independent 2026 re-check of Particle Illusion's plugin pricing;
no adoption signal for OpenCut/jumpcut beyond their own READMEs; whether a `.mogrt`'s
parameters are settable via the bridge's match-name mechanism is unresolved — MOGRTs are a
different insertion path from effects and no source reconciled the two.
