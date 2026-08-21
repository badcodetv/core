# What needs After Effects, and the alternatives

## What this covers

The honest boundary between what Premiere Pro (2026, native + plugins) can do and what genuinely
requires After Effects (AE) — advanced particles, 3D camera/object work, planar tracking and
rotoscoping, expressions-driven motion graphics, Cinema 4D-linked 3D. Covers the Dynamic Link
workflow and its real cost, AE's subscription price, and the non-AE alternatives for someone who
will not install it: Premiere-native plugins, Blender/Natron/Fusion, Cavalry, Rive, and MOGRTs
authored by others. AE is **not installed** in the BadCode pipeline (Media Encoder 2026 is) — this
brief exists to confirm that's a defensible choice, not an accident, and to name the escape hatches
if a specific shot ever needs it.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Advanced particle systems | Trapcode Particular (AE) | Real 3D particle sim, physics, emitters | £ subscription (Maxon One) |
| Cheap fake particles in Premiere | Boris FX Continuum Particles Unit, or CoreMelt free pack | Pre-baked particle overlays / 2D emitters | £ or free |
| 3D camera tracking of live footage | AE 3D Camera Tracker | Solves camera + scene geometry, exports null/camera | included with AE |
| Planar / object tracking outside AE | Mocha Pro (standalone or Premiere plugin) | Independent planar tracker, feeds Premiere masks | £ subscription/perpetual |
| Rotoscoping a moving subject | Premiere Object Mask (native, 2026) or Mocha Pro | Hover-click AI mask + auto-track ahead | included / £ |
| Advanced roto AE used to require | AE Roto Brush / Refine Matte (being superseded by Object Matte) | Per-pixel edge refine, motion-aware | included with AE |
| Expressions-driven procedural motion | AE expressions (JS-like) | Link one property's value to code/other layers | included with AE |
| No-AE equivalent of expressions | Cavalry (parametric/state-machine rigs), Rive (state machine) | Visual parametric rigging, no AE needed | free–£ |
| 3D object/text render (Element 3D-class) | AE + Element 3D, or Cinema 4D via AE | True 3D import, lighting, camera-linked render | £199 one-time (Element 3D) |
| Node-based compositing outside AE | Blackmagic Fusion (standalone or Resolve's Fusion page), Natron | Node graph: keying, tracking, comp | free |
| Motion graphics templates without authoring | MOGRT from Motion Array / Envato Elements / Adobe Stock | Drop-in .mogrt, edit via Essential Graphics | £ subscription per library |
| Author your own MOGRT | AE (Essential Graphics panel export) | Only AE can *export* a .mogrt; Premiere can only *use* one | AE required to author |
| Poor-man's glow/bloom on a still (no AE, no plugin) | ffmpeg split+gblur+blend | Blur a copy, screen-blend over original | free (TESTED, this brief) |

## Named tools

### After Effects
The compositing/motion-graphics application Dynamic Link connects to. Single-app subscription:
**£21.98/month (UK, inc. VAT, annual plan billed monthly)**, seen on adobe.com/uk 2026-08-21 via
search cache (direct fetch of adobe.com timed out twice — treat as **unconfirmed primary**, cross-checked
against a US figure of $22.99/month annual-billed, $34.49/month-to-month, both quoted by multiple
2026 pricing-roundup sites). Licence model: subscription only, no perpetual option since CC2019.
Platform: Win/Mac. Not installed in the BadCode toolchain.

### Dynamic Link
Adobe's live-composition bridge between Premiere and AE — no export/re-import, edits in one show
in the other's timeline in real time. **Requires both applications installed and licensed**, ideally
on the same machine (Adobe doesn't document a supported cross-machine mode for it). Cost is not a
licence fee — it's the standing RAM/CPU overhead of running two Adobe apps' background processes
(the AE Dynamic Link server) for the life of the project, plus every AE-linked clip re-rendering on
scrub instead of playing a cached preview. Source: helpx.adobe.com Dynamic Link page — could not be
fetched directly (two timeouts); summarised from search-indexed content and cross-referenced with
Adobe-partner explainer sites (schoolofmotion.com, Wondershare's 2026 writeup). **Gap: I could not
verify against Adobe's own page text — flag as second-hand.**

### Cavalry
Node/parametric motion-design app, positioned as an AE alternative for kinetic type and procedural
rigs (the visual equivalent of AE expressions, no code). **Free for individuals including
commercial use** since Canva's 2026 acquisition; Professional/team tier **$16/month billed
annually**, seen 2026-08-21 (cgchannel.com, superrendersfarm.com, toolradar.com, April 2026
acquisition coverage). Platform: Mac/Win. Install: direct download, no Adobe account. Maturity:
young but actively developed; reviewers note it's strong at 2D kinetic/parametric work, weak at
compositing/roto — it is not a Trapcode or Mocha substitute.

### Rive
Real-time, state-machine-driven animation tool for app/game UI, not film compositing — the other
no-code substitute for AE-expression-style reactive motion. **Free tier** (unlimited personal
projects, 3-file collab cap); paid Cadet **$9/mo**, Voyager **$32/mo**, Enterprise **$120/mo**, seen
2026-08-21 (rive.app/pricing). Platform: web app + runtime SDKs. Output is a `.riv` interactive
file, not a rendered clip — a poor fit for BadCode's linear pipeline; listed for boundary
completeness, not as a recommendation.

### Mocha Pro
Standalone planar tracker/roto tool (also ships as an AE/Premiere plugin) — the professional answer
to "AE has Roto Brush and a 3D camera tracker, Premiere doesn't." 2026.5 release added an
AI point-tracking mode ("Point Track ML") aimed at surfaces occluded by other objects. Pricing:
annual subscription **$325/yr** (single-host plugin) to **$655/yr** (standalone + all plugins);
perpetual **$765** (standalone + multi-host plugins) or **$1,095** with a year of upgrades/support —
seen 2026-08-21 (motionmedia.com reseller pages, cgchannel.com, therookies.co). Platform: Win/Mac,
OFX + native Adobe plugin. Maturity: industry-standard, Academy Award credit cited by Boris FX
itself; 2026 reviews frame it as racing Premiere's new native Object Mask rather than losing to it.

### Blackmagic Fusion (standalone / Resolve's Fusion page)
Node-based compositor covering tracking/keying/comp work that would otherwise need AE. **Fully
functional in DaVinci Resolve's free edition** — Fusion, titles, tracking, keying, VFX all included
free; Resolve **Studio** (one-time **$295**, perpetual, no subscription) adds Magic Mask
rotoscoping, noise reduction, finishing tools, seen 2026-08-21. Platform: Win/Mac/Linux, direct
download, no subscription account needed for the free tier. Maturity: used professionally on
film/TV; a stronger *node-based compositor* than AE, weaker at AE's layer-based motion-graphics
strengths.

### Natron
Free, open-source node compositor, AE/Nuke-alike. Free, MIT/GPL-family licence, seen 2026-08-21.
Platform: Win/Mac/Linux, scriptable (Python), good for automation/batch rendering. Maturity flag
from sources: development has slowed noticeably and it's explicitly weak at motion graphics/3D —
a compositing fallback only, not a general AE substitute.

### Element 3D (Video Copilot)
The plugin that gives AE true 3D object import/render/lighting without a full 3D app — the named
"AE-only" capability in the brief. **$199 one-time** (perpetual), ~5% reseller discount common
(~$189.95 at Toolfarm), seen 2026-08-21. **AE-only**, no Premiere version; no drop-in non-AE
equivalent at this price point (Cavalry/Cinema 4D are the nearest, at a much higher cost/learning
bar).

### Trapcode Particular / Trapcode Suite
AE's reference-standard 3D particle system — no native Premiere equivalent exists. **No more
perpetual licence**: bundled-only via **Maxon One** subscription or **Red Giant Complete**; a
standalone perpetual price of **€1,150.05** appears in some 2026 listings but sources flag it as a
legacy figure, not the current buy path. Seen 2026-08-21. **Gap: no clean current single-product
price found — Maxon has folded it into bundle-only sales.**

## Automation hook

**Premiere side.** None of the AE-only tools above run inside Premiere — there is no match name for
Trapcode Particular, Element 3D, or AE expressions, because Premiere never loads them. Where a
*substitute* plugin ships as a real Premiere effect (Continuum Particles Unit, Mocha Pro's Premiere
plugin), the discovery step is the same as any other plugin in this toolkit: enumerate
`VideoFilterFactory.getMatchNames()` after install, then filter by vendor name (`"Mocha"`, `"BCC"`
for Boris Continuum's historical prefix). **UNTESTED** — no licensed copy of either was available to
pull the actual string; treat the prefix as a starting filter, not confirmed.

**ffmpeg side.** ffmpeg cannot substitute for AE's roto/tracking/3D/particle work. What it *can*
fake, cheaply, is a look AE would otherwise be reached for:

```
# Poor-man's AE "Glow": blur a copy, screen-blend over the original.
# TESTED 2026-08-21 in scratchpad on a synthetic 1376x768 near-black frame.
ffmpeg -i in.png -filter_complex \
  "[0:v]split=2[a][b];[b]gblur=sigma=20[blur];[a][blur]blend=all_mode=screen:all_opacity=0.8" \
  -frames:v 1 out.png
```

For everything else this toolkit already needs from a still or clip — zoompan moves, ping-pong
loops, retiming, grain — see `docs/flow/post-production.md`; this brief does not duplicate those
TESTED recipes.

## BadCode fit

On near-black, 1376×768, 8-second AI (Veo) footage: the AE-only capabilities above (real 3D
particle sim, true 3D object compositing, expression-driven procedural rigs) are built for
VFX-heavy, multi-shot compositing — not the BadCode register, one locked-off or slow-drift camera
on a single monumental subject with one thin light. The glow/bloom ffmpeg substitute above is
closer to what actually gets reached for: a subtle bloom on the one light source, not a particle
field. **Avoid** any particle-system look (dust motes, sparks, embers) as a reason to bring in AE
or Trapcode — it reads as generic AI-comic sparkle, the look `badcode-art-direction` already flags
to calibrate against. If a shot genuinely needs planar tracking, Mocha Pro's Premiere plugin or
native Object Mask are the routes to reach for before AE — both stay inside apps already installed
or a bounded, named cost.

## Traps

- **Don't say "Premiere can't do X" without checking the 2026 native feature set first.** Object
  Mask (Jan 2026) and Generative Extend already absorbed a chunk of the automatic "that needs AE"
  answer — re-check the native-toolkit brief before reaching for a plugin or AE.
- **Dynamic Link isn't free once used** — it requires both apps licensed and running; there's no
  way to get its live-composition behaviour with Premiere alone. AE isn't in this toolchain, so
  Dynamic Link is moot; don't let a tutorial's "just Dynamic Link it" imply a Premiere-only shortcut.
- **Trapcode/Element 3D pricing pages are stale or bundle-only.** The perpetual-looking Trapcode
  figure in search results is a leftover listing; the real 2026 buy path is Maxon One or Red Giant
  Complete. Don't quote it as current without checking maxon.net directly.
- **Two `helpx.adobe.com` fetches timed out** this pass (Dynamic Link, Object Mask pages) — the
  Dynamic Link summary is second-hand, search-indexed rather than page-verified; re-verify before
  treating it as primary-source in public-facing copy.
- **MOGRTs can only be *authored* in AE**, even though they're *used* in Premiere — a no-AE editor
  can re-colour someone else's .mogrt but never build a new one from scratch.

## Sources

- [adobe.com/uk/products/aftereffects.html](https://adobe.com/uk/products/aftereffects.html) — 2026-08-21 (search cache; fetch timed out) — UK AE subscription price
- [helpx.adobe.com Dynamic Link page](https://helpx.adobe.com/premiere-pro/using/dynamic-link-after-effects.html) — 2026-08-21 (search cache; fetch timed out) — Dynamic Link mechanics
- [helpx.adobe.com Object Masking (beta)](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/object-masking.html) — 2026-08-21 — native Object Mask docs
- [helpx.adobe.com 3D Camera Tracker](https://helpx.adobe.com/in/after-effects/using/tracking-3d-camera-movement.html) — 2026-08-21 — AE-only feature confirmation
- [borisfx.com/products/mocha-pro](https://borisfx.com/products/mocha-pro/) — 2026-08-21 — Mocha Pro product page
- [motionmedia.com Mocha Pro pricing](https://www.motionmedia.com/mocha-pro-standalone-plus-multi-host-annual-subscription/) — 2026-08-21 — subscription/perpetual prices
- [cgchannel.com Cavalry acquisition](https://www.cgchannel.com/2026/04/canva-makes-motion-graphics-and-animation-app-cavalry-free/) — 2026-08-21 — Canva bought Cavalry, now free
- [rive.app/pricing](https://rive.app/pricing) — 2026-08-21 — Rive tier breakdown
- [ffmpeg.org filters doc, `blend`/`gblur`](https://ffmpeg.org/ffmpeg-filters.html) — 2026-08-21 — glow filter chain reference, TESTED locally
- [DaVinci Resolve free-vs-Studio comparison](https://www.gappsy.com/tools/davinci-resolve/) — 2026-08-21 — Fusion free, Studio adds Magic Mask
