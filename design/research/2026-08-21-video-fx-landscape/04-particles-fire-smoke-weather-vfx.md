# Particles, fire, smoke, sparks, weather, compositing VFX

## What this covers

Putting fire, smoke, sparks, dust, rain, snow, fog, lightning, and explosions into a Premiere Pro timeline, on a stack that already generates near-black 1376×768 8-second clips via Google Flow (Veo 3.1) and cuts in Premiere Pro 26.3.2 with no After Effects installed. Four routes, roughly in order of friction: (1) Premiere's own built-ins — blend modes, the native Lightning generator; (2) stock-element libraries composited with Screen/Add blend or a luma key; (3) paid plugin suites (Boris FX Continuum/Sapphire, Red Giant VFX Suite — the After-Effects-only Trapcode Particular is explicitly out of reach here); (4) generating the element with AI (Veo, Firefly Video Model) instead of compositing a pre-shot one. Titling, tracking/roto, grading, and audio are other briefs in this set.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
|---|---|---|---|
| Lightning bolt/flash | Premiere native **Lightning** effect | Apply to a Transparent Video clip, keyframe Origin/Direction | Free (included) |
| Screen flash / muzzle flash / glow | Blend modes (Screen, Add/Linear Dodge, Lighten) | Overlay a black-bg clip, set blend mode on it | Free (included) |
| Fire, smoke, sparks, dust, explosions (real footage) | ActionVFX / ProductionCrate stock overlays | Subscribe or buy, drop pre-keyed clip above, Screen/Add blend | Free–£79/mo+ |
| Fire, smoke, dust (CC/free footage) | Mixkit, Pexels, Videvo | Download, same Screen/Add blend workflow | Free |
| In-app particle systems (fire, snow, magic) | Boris FX **Continuum Particles Unit** / **Particle Illusion** | Apply as a Premiere effect, pick a preset emitter, keyframe | Free (personal) – £215–£765/yr |
| Advanced organic FX (glows, rays, atmosphere) | Boris FX **Sapphire** | Apply per-clip Premiere effects from the Sapphire category | £545–£985/yr, or £1,865+ perpetual |
| Light wraps, heat blur, volumetric fog | Red Giant **VFX Suite** (Maxon One) | Apply as Premiere effects, bundled via Maxon One | ~£1,199/yr (Maxon One) |
| Trapcode-style particle sim | ✗ not available in Premiere | Trapcode Particular is After-Effects-only | N/A |
| Bespoke element to spec | Google Flow (Veo 3.1) | Prompt element on black, comp with Screen blend | Already in the Flow workflow |
| Generated B-roll element | Adobe **Firefly Video Model** | Beta, 5s/1080p cap at launch; comp same as stock | Firefly credits (Creative Cloud) |

## Named tools

**Premiere Lightning effect (native)** — built-in "Generate" effect drawing a procedural bolt between two keyframed points on a Transparent Video clip. Free, included. Any current Premiere version. No install. Long-standing; still the go-to before reaching for a plugin. [Adobe Help — lightning effects](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/add-lightning-effects.html), 2026-08-21.

**Blend modes (Screen / Add-Linear Dodge / Lighten)** — clip-level compositing property, not an effect; overlays a black-bg element additively with no key needed. Free, native. Standard technique per trade explainers (PremiumBeat, ProVideo Coalition) — **gap: not verified against Adobe's own docs this pass**, only secondary sources.

**ActionVFX** — pre-keyed 4K RED-shot fire/smoke/explosion/dust. AVFX+ subscription: freelancer **$24–$79/mo**, studio **$249–$897/mo**; à la carte also sold. Host-agnostic footage. Vendor blog, not the pricing page itself (**403'd to fetch, secondary-sourced**). [ActionVFX — AVFX+](https://www.actionvfx.com/blog/introducing-the-actionvfx-subscription-the-best-vfx-elements-at-the-best-price), 2026-08-21.

**ProductionCrate / FootageCrate** — 10,000+ elements plus ~30 Premiere/AE plug-ins, large free tier (500+ HD+ clips). Plans reported **$9–$29/mo** or **$100–$299/yr**; sources disagreed on tier names — **approximate, pricing page returned HTTP 403.** [productioncrate.com](https://www.productioncrate.com/), 2026-08-21.

**Mixkit / Pexels / Videvo** — free stock, usable fire/smoke/dust/weather clips. Mixkit's Free License allows commercial use, no attribution, but some clips carry a per-clip "Restricted License." Pexels License: commercial use free, no attribution, no reselling the raw clip. Videvo splits Attribution (credit, no re-hosting) vs CC BY 3.0 (adapt/share, no resale) — licence is per clip. [Mixkit Terms](https://mixkit.co/terms/), [Pexels License](https://www.pexels.com/license/), 2026-08-21 — Videvo's terms here are third-party-corroborated, not fetched from Videvo directly (**gap**).

**Boris FX Continuum — Particles Unit** — Premiere/AE/Avid/Resolve/Nuke/Vegas unit bundling Particle Illusion, Fracture, and weather organics as native Premiere effects. Continuum overall: perpetual **$365–$2,195**, subscription **$32–$112/mo** or **$215–$765/yr**, varies by host bundle — standalone Particles Unit price not found. Actively updated through May 2026. [Continuum Particles Unit](https://borisfx.com/products/continuum-units/particles/), [Toolfarm](https://www.toolfarm.com/buy/boris_continuum_subscription_license/), 2026-08-21.

**Particle Illusion** — standalone 3D particle emitter (fire, smoke, magic, sparks); export and Screen-blend, or install as a Continuum-hosted effect. Standalone is **free, non-commercial/personal use only**, no watermark; Pro/plug-in needs a paid Continuum licence for commercial use. Cited repeatedly as the strongest genuinely-free particle tool for Premiere-only editors. [Boris FX — Particle Illusion](https://borisfx.com/products/particle-illusion/), 2026-08-21.

**Boris FX Sapphire** — essentials VFX suite (glows, rays, stylize, atmosphere) as native Premiere effects. Subscription **$545–$985/yr** ($80–$144/mo) or perpetual **$1,865–$3,075**, single- vs multi-host. Actively developed (Nov 2025, May 2026 releases). [Sapphire](https://borisfx.com/products/sapphire/), [CG Channel](https://www.cgchannel.com/2026/05/boris-fx-releases-sapphire-2026-5/), 2026-08-21.

**Red Giant VFX Suite (Maxon One)** — 9 tools for AE **and Premiere Pro**: light wraps, heat blur, volumetric fog, particle organics. Not sold standalone in sources found; bundled in **Maxon One at ~$1,199/yr** (carried over, not re-verified — **gap**). [CineD](https://www.cined.com/red-giant-vfx-suite-released-9-tools-for-killer-vfx-in-after-effects-and-premiere-pro/), 2026-08-21.

**Trapcode Particular — NOT usable from Premiere.** Maxon/Red Giant's flagship particle sim, part of Maxon One. Every 2025–26 source (Maxon's own page, School of Motion) shows **After Effects only**, no Premiere host. Since AE isn't installed here, it's out of reach — Continuum Particles Unit or free Particle Illusion are the substitutes. [Maxon — Trapcode Particular](https://www.maxon.net/en/product-detail/red-giant/particles-and-3d/trapcode-particular), 2026-08-21.

**Veo (Google Flow)** — prompt the element (or whole weather-bearing scene) directly instead of compositing one. 2025–26 prompting guides say Veo handles smoke/fire/dust/atmospherics with physics-descriptor language. Already inside the existing Flow workflow, no new tool. **Gap:** only third-party prompting guides checked, not a primary Google doc; untested against BadCode's specific near-black register. [Replicate — prompting Veo 3](https://replicate.com/blog/using-and-prompting-veo-3), 2026-08-21.

**Adobe Firefly Video Model / Generative Extend** — in-Premiere text/image-to-video; Adobe's own materials name "fire, smoke, or water" as an explicit atmospheric-element use case. Firefly generative credits, bundled in Creative Cloud (per-generation cost not found — **gap**). Beta caps at launch: 5s, 1080p — **not reconfirmed for 2026, figures are from the 2024/2025 announcement.** [Adobe Newsroom](https://news.adobe.com/news/2024/10/101424-adobe-revolutionizes-professional-video-editing-with-premiere-pro), 2026-08-21.

## Automation hook

**Premiere/UXP:**
- Lightning: no match name confirmed. Discovery: `VideoFilterFactory.getMatchNames()`, filter for `"Lightning"` — likely an `AE.ADBE …` prefix by convention, but **unverified**.
- Blend modes: not a filter — a clip/track `Opacity` component property, not reachable via `getMatchNames()`. Discovery: inspect the clip's `components` array for `AE.ADBE Opacity` and its Blend Mode parameter.
- Boris FX / Red Giant filters: enumerate `getMatchNames()` after install, grep the vendor prefix (Boris FX often `"BCC…"`). **No strings confirmed this pass — needs a live session with the plugins installed.**

**ffmpeg (comping a rendered element onto a Veo clip):**

Screen-blend, **TESTED** this session at 1376×768:
```
ffmpeg -i base.mp4 -i element.mp4 \
  -filter_complex "[0:v][1:v]blend=all_mode=screen:all_opacity=1[out]" \
  -map "[out]" -map 0:a? -c:v libx264 -crf 18 out.mp4
```
Verified against two synthetic `lavfi` sources on ffmpeg 4.4.2/WSL; real footage needs matched duration/fps first.

Luma-key a black-bg particle render instead of blending, **UNTESTED**:
```
ffmpeg -i base.mp4 -i element.mp4 \
  -filter_complex "[1:v]format=rgba,colorkey=black:0.1:0.2[fg];[0:v][fg]overlay[out]" \
  -map "[out]" -c:v libx264 -crf 18 out.mp4
```

## BadCode fit

- Near-black plate is the best case for additive blend compositing: Screen/Add on a black-bg fire/smoke/spark element reads clean against near-black, without the grey-halo problem Screen causes on lighter shots.
- 8-second Veo ceiling vs 3–15s stock elements: trim/loop to match using the existing ping-pong/retime recipes in `docs/flow/post-production.md` — don't duplicate that logic here.
- Prompting Veo for the element directly (generative route) keeps one continuous camera move and one grain/light register, avoiding a compositing seam — prefer it over stock overlay when the shot allows it.
- Avoid bright warm-white sparks/fire shot against a lit stage — fights the muted cool-neutral palette and reads as generic-AI-comic; grade any composited element through the same look pass as the base plate.
- Particle Illusion's free tier is non-commercial only — a licensing risk for a published release; confirm commercial terms or use the paid Continuum-hosted version before shipping anything public.

## Traps

- **Particle Illusion free = non-commercial only.** Using its exports in a released piece without the paid licence is a violation, not just a missing-credit gap.
- **Trapcode Particular never appears in Premiere**, however installed — it's AE-exclusive; don't hunt for a Premiere host.
- **ActionVFX and ProductionCrate pricing pages 403'd to automated fetch** — every price for those two is from a search snippet or vendor blog post, not the live page. Re-verify before quoting publicly.
- **No match names confirmed** for Lightning, Boris FX, or Red Giant filters — the UXP bridge needs a live `getMatchNames()` pass with plugins installed.
- **CEP-based stock panels may not load in Premiere 26** (cross-brief finding) — if ProductionCrate's or ActionVFX's panel is CEP not UXP, it may silently fail to appear; not checked directly here.
- **Vendor pricing is inconsistent within one company's own materials** — Continuum and Sapphire both show wide spreads by host bundle in this pass; always state which bundle a price is for.

## Sources

- [Adobe Premiere Pro Help — Add lightning effects](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/add-lightning-effects.html) — 2026-08-21 — confirms native Lightning generator
- [Boris FX — Continuum Particles Unit](https://borisfx.com/products/continuum-units/particles/) — 2026-08-21 — Particle Illusion, Premiere host, effects
- [Boris FX — Particle Illusion](https://borisfx.com/products/particle-illusion/) — 2026-08-21 — free standalone vs paid plug-in terms
- [Boris FX — Sapphire](https://borisfx.com/products/sapphire/) — 2026-08-21 — suite scope, Premiere host support
- [Maxon — Red Giant Trapcode Particular](https://www.maxon.net/en/product-detail/red-giant/particles-and-3d/trapcode-particular) — 2026-08-21 — confirms AE-only host
- [CineD — Red Giant VFX Suite Released](https://www.cined.com/red-giant-vfx-suite-released-9-tools-for-killer-vfx-in-after-effects-and-premiere-pro/) — 2026-08-21 — confirms Premiere Pro support
- [ActionVFX — AVFX+ Subscription](https://www.actionvfx.com/blog/introducing-the-actionvfx-subscription-the-best-vfx-elements-at-the-best-price) — 2026-08-21 — subscription tier pricing
- [Mixkit — Terms](https://mixkit.co/terms/) — 2026-08-21 — free-licence commercial terms
- [Pexels — License](https://www.pexels.com/license/) — 2026-08-21 — free-licence commercial terms
- [Adobe Newsroom — Firefly Video Model in Premiere](https://news.adobe.com/news/2024/10/101424-adobe-revolutionizes-professional-video-editing-with-premiere-pro) — 2026-08-21 — Generative Extend, fire/smoke B-roll use case
- [Replicate — Prompting Veo 3](https://replicate.com/blog/using-and-prompting-veo-3) — 2026-08-21 — Veo particle/weather prompting (secondary source)
- ffmpeg 4.4.2 `blend` filter — self-tested 2026-08-21, WSL, 1376×768 screen-mode compositing confirmed
