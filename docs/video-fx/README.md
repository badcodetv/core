# video-fx — which tool, which lane, and what it costs

**The judgement half.** [`docs/premiere/`](../premiere/README.md) is *how* to drive Premiere; this
is *what to reach for*. If you already know the effect and just need the call, you want
[`docs/premiere/recipes.md`](../premiere/recipes.md).

> **🔴 The standing ruling, 2026-08-21 (Kai): NO PAID PLUGINS.**
> *"We don't really need any paid plugins because they all sound far too advanced, and for smoke
> and fire we could use Flow anyway."*
> This toolkit is for **the free stack**: Premiere built-ins, Lumetri, the absorbed Film Impact
> transitions, MOGRTs, ffmpeg — and **Flow for anything that has to be invented**. Paid tools get
> one reference section at the bottom, saying what we deliberately don't own and the free route we
> take instead. **Never propose a purchase as the answer.**

---

## Lane choice — the decision that comes first

> **🔴 The lanes are LAYERS, not alternatives. Ruled 2026-08-26 (Kai).**
> Where the world moves *and* the camera moves, you build all three: **Veo animates the world with
> the camera locked, Premiere moves the camera over the finished clip, ffmpeg does what must be
> exact.** Read **[`hybrid-method.md`](hybrid-method.md)** before choosing a lane — it also carries
> the rule that **8 seconds is not a limit** (chain the last frame into the next clip's first) and
> an audited list of what ffmpeg can do that Premiere cannot.

Five lanes. Pick by what the job actually needs, not by habit — and remember they compose.

| Lane | Reach for it when | Why |
| --- | --- | --- |
| **Flow** | The thing does not exist yet and must be **invented** — fire, smoke, sparks, weather, a crowd, a city, an impossible camera move | We have no particle systems and are not buying any. Flow is free at the margin on the Ultra plan and it is genuinely good at elements |
| **ffmpeg** | The result must be **exact, repeatable and headless** — conform, concat, trim, retime, LUT, grain, contact sheet, delivery encode | Deterministic, scriptable, no GUI in the loop. The recipe book is [`docs/flow/post-production.md`](../flow/post-production.md) |
| **Premiere** | It is part of **the edit** — cuts, dissolves, keyframed motion, a grade you want to see against the cut, compositing a Flow element over a plate, titles | Real-time preview, the effect catalogue, and the session can `export_frame` and *look* |
| **After Effects** | True 3D, planar tracking, complex motion graphics | 🔴 **AE is not installed on this machine.** Flag it as out of scope; do not design around it |
| **Sourcing** | The thing is **real, already filmed, and its being real is the point** — an Apollo launch, a 1950s factory floor, the fall of France | Inventing it in Flow would be both worse and a lie. There is a genuinely free tier (US federal film, newsreel, NASA, Commons CC0) — but **"free to download" and "free to publish" are different questions**, so it comes with a licence gate. Skill: `find-footage`. Reference: [`footage-sources.md`](footage-sources.md) |

**The tie-breaker:** if a human will iterate on it by eye, it belongs in Premiere. If it is a
transform with one right answer, it belongs in ffmpeg. If it does not exist, it belongs in Flow.
**If it already exists and really happened, source it** — and check the licence before you cut it.

### The house answer for atmospherics

Asked for fire, smoke, sparks, rain, fog, dust, embers, explosions:

1. **Generate the element in Flow on a pure black background** (`flow-prompt` skill,
   [`docs/flow/`](../flow/README.md)).
2. Import it and put it on a video track **above** the plate.
3. Key the black out with **Luma Key** (`AE.ADBE Legacy Key Luma`) or **Extract**
   (`PR.ADBE Extract`); soften with **Edge Feather** if it reads as cut out.
4. Or, headless: ffmpeg `blend=screen` / `overlay`.

Free stock is the fallback if Flow will not produce it — but reach for it through the
`find-footage` skill and [`footage-sources.md`](footage-sources.md), not from memory. The stock
tier is amber, not free-for-all: **Pexels and Pixabay both carry an explicit political-context
exclusion**, Adobe Stock Free bars implied political endorsement, Mixkit mixes free and
non-commercial licences in one result set, and **Videvo and Mazwai are dead** (both 301 to
freepik.com — any blog post describing their old CC tiers is stale).
**Buying Sapphire or ActionVFX is not on the table.**

---

## Where the answers live

| Question | Go to |
| --- | --- |
| "How do I build a shot that needs both a living world and a moving camera?" · "Can we go longer than 8 seconds?" · "What can ffmpeg do that Premiere can't?" | 🟢 **[`hybrid-method.md`](hybrid-method.md)** — the three-layer method, the frame-chaining rule, and the audited ffmpeg/frei0r surface |
| "Is this file ready to upload?" | 🟢 **[`delivery.md`](delivery.md)** — delivery specs and QC, plus `scripts/delivery-qc.sh`. **Run it before anything ships** |
| "Is there a template for X?" | [`../premiere/mogrt-catalogue.md`](../premiere/mogrt-catalogue.md) — **77 MOGRTs already installed**, free, with every field they expose |
| **"What effects can we apply?"** | 🟢 **BOTH catalogues, always** — [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md) (106 effects, 118 transitions) **and** [`ffmpeg-catalogue.md`](ffmpeg-catalogue.md) (319 video filters, 133 frei0r plugins). Ruled 2026-08-26: never list one without the other |
| "What effect does X?" (Premiere) | [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md) — **all 106 effects and 118 transitions installed**, harvested live and grouped by what you would ask for |
| "How do I apply it from here?" | [`../premiere/recipes.md`](../premiere/recipes.md) — concrete tool calls |
| "What ffmpeg filter does X?" | 🟢 **[`ffmpeg-catalogue.md`](ffmpeg-catalogue.md)** to browse (incl. the frei0r shelf and the eight things only ffmpeg can do), then [`docs/flow/post-production.md`](../flow/post-production.md) for a tested recipe |
| "Why did the API do that?" | [`../premiere/api-notes.md`](../premiere/api-notes.md) |
| "Is there a royalty-free clip of X?" · "Is this clip safe to use?" | 🟢 **[`footage-sources.md`](footage-sources.md)** — **68 sources tiered green/amber/red**, counts dated, with the licence traps that look nothing like traps — and a verification table separating what was proven live from what was only read. The procedure is the **`find-footage`** skill; this is its reference |

---

## The research briefs

Twenty briefs from the 2026-08-21 sweep, in
[`design/research/2026-08-21-video-fx-landscape/`](../../design/research/2026-08-21-video-fx-landscape/README.md).
**They are raw research, not house policy** — they were written before the no-paid-plugins ruling,
so every price and every paid-tool recommendation in them is superseded by the box at the top of
this file. Read them for the *technique*, not the shopping.

**Premiere side**

| # | Brief |
| --- | --- |
| 01 | Built-in video effects |
| 02 | Transitions, Essential Graphics, MOGRTs, titles |
| 03 | Lumetri, LUTs, film looks |
| 04 | Particles, fire, smoke, weather VFX |
| 05 | Maps, motion graphics, kinetic text |
| 06 | Premiere's AI features and captions |
| 07 | Paid suites — **superseded, reference only** |
| 08 | Free plugins and the template ecosystem |
| 09 | After Effects crossover — **AE not installed here** |
| 10 | Speed, retime, stabilise, warp |
| 11 | Audio ducking, denoise, narration mix |

**ffmpeg side**

| # | Brief |
| --- | --- |
| 12 | The filter map, organised by need |
| 13 | Colour, LUT, grain |
| 14 | `xfade`, overlay, blend, chroma |
| 15 | `drawtext`, subtitles, ASS |
| 16 | `zoompan`, `vidstab`, `minterpolate` |
| 17 | Audio filters |
| 18 | Adjacent: frei0r, VapourSynth, MLT, gl-transition |

**Commissioned after the critic found them missing**

| # | Brief |
| --- | --- |
| 19 | Delivery specs and QC scopes — what Shorts/TikTok/Reels want, how to check levels |
| 20 | Beat-synced and audio-driven cutting — **the most BadCode-relevant of the four gaps**, since the shorts are cut to drum & bass |

---

## The procedure

**Toolkit first → web on a miss → record back.**

1. **Check this folder and [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md).**
   106 effects and 118 transitions are already installed; the answer is usually there.
2. **Check the briefs** for technique.
3. **Only then search the web** — and when you find something, **write it back** into the
   catalogue or a brief, dated, so the next session does not pay again.
4. **Never end at "buy X".** State the free route. If there genuinely isn't one, say so plainly
   and let Kai decide.

**On prices:** a price without a live vendor page is quoted as *unconfirmed*, never as a number.
The critic found four outright contradictions between briefs (Dehancer, Sapphire, Mocha Pro,
CoreMelt), all on paid tools. The no-paid-plugins ruling makes them moot; the rule stands for the
reference section anyway.

---

## What we deliberately don't own

| Not installed | The free route we take instead |
| --- | --- |
| Sapphire, ActionVFX, ProductionCrate (fire/smoke/explosions) | **Flow on black, keyed in** |
| Trapcode (particles) | Flow, same route |
| Element 3D (3D text) | Flow for the render; Simple Text or a MOGRT for flat type |
| Mocha Pro (planar tracking) | Corner Pin by hand, or reshoot the plate in Flow |
| Dehancer, FilmConvert (film emulation) | Lumetri Looks + `Input LUT`, or an ffmpeg LUT pass |
| Neat Video (denoise) | `AE.Mettle SkyBox Denoise`, or ffmpeg `hqdn3d` / `nlmeans` |
| Twixtor (optical-flow retime) | Premiere's Time Interpolation, or ffmpeg `minterpolate` |
| After Effects | 🔴 Genuinely out of scope — flag it, don't work around it |

---

## Status

🟡 **This index plus [`delivery.md`](delivery.md) are the delivered slice of T17.** The per-lane
pages it originally specified — `premiere-builtins.md`, `premiere-plugins.md`, `ffmpeg-recipes.md`,
`lane-choice.md` — are **not written**. The lane-choice decision and the paid-tool position are captured here; the Premiere
"which effect" question is answered more concretely by the live
[`effects-catalogue.md`](../premiere/effects-catalogue.md) than a distilled page would have been;
and ffmpeg recipes still live in [`docs/flow/post-production.md`](../flow/post-production.md) plus
briefs 12–18. The **`video-fx` skill now exists** (`.claude/skills/video-fx/`, 2026-08-23) and is
the way in: it owns lane choice, routes "what effect does X" into the catalogues, and carries the
delivery gate. This page is its reference. Alongside it: `premiere-automation` for driving the
edit, `flow-prompt` for the element, and `find-footage` for anything real we might source instead
of inventing.

Plan and remaining scope:
[`design/2026-08-21-premiere-bridge-and-video-fx.md`](../../design/2026-08-21-premiere-bridge-and-video-fx.md).
