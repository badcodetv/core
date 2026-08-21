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

Four lanes. Pick by what the job actually needs, not by habit.

| Lane | Reach for it when | Why |
| --- | --- | --- |
| **Flow** | The thing does not exist yet and must be **invented** — fire, smoke, sparks, weather, a crowd, a city, an impossible camera move | We have no particle systems and are not buying any. Flow is free at the margin on the Ultra plan and it is genuinely good at elements |
| **ffmpeg** | The result must be **exact, repeatable and headless** — conform, concat, trim, retime, LUT, grain, contact sheet, delivery encode | Deterministic, scriptable, no GUI in the loop. The recipe book is [`docs/flow/post-production.md`](../flow/post-production.md) |
| **Premiere** | It is part of **the edit** — cuts, dissolves, keyframed motion, a grade you want to see against the cut, compositing a Flow element over a plate, titles | Real-time preview, the effect catalogue, and the session can `export_frame` and *look* |
| **After Effects** | True 3D, planar tracking, complex motion graphics | 🔴 **AE is not installed on this machine.** Flag it as out of scope; do not design around it |

**The tie-breaker:** if a human will iterate on it by eye, it belongs in Premiere. If it is a
transform with one right answer, it belongs in ffmpeg. If it does not exist, it belongs in Flow.

### The house answer for atmospherics

Asked for fire, smoke, sparks, rain, fog, dust, embers, explosions:

1. **Generate the element in Flow on a pure black background** (`flow-prompt` skill,
   [`docs/flow/`](../flow/README.md)).
2. Import it and put it on a video track **above** the plate.
3. Key the black out with **Luma Key** (`AE.ADBE Legacy Key Luma`) or **Extract**
   (`PR.ADBE Extract`); soften with **Edge Feather** if it reads as cut out.
4. Or, headless: ffmpeg `blend=screen` / `overlay`.

Free stock (Mixkit, Pexels, Videvo free tiers) is the fallback if Flow will not produce it.
**Buying Sapphire or ActionVFX is not on the table.**

---

## Where the answers live

| Question | Go to |
| --- | --- |
| "What effect does X?" (Premiere) | [`../premiere/effects-catalogue.md`](../premiere/effects-catalogue.md) — **all 106 effects and 118 transitions installed**, harvested live and grouped by what you would ask for |
| "How do I apply it from here?" | [`../premiere/recipes.md`](../premiere/recipes.md) — concrete tool calls |
| "What ffmpeg filter does X?" | [`docs/flow/post-production.md`](../flow/post-production.md) first (it owns the everyday recipes), then brief `12` below |
| "Why did the API do that?" | [`../premiere/api-notes.md`](../premiere/api-notes.md) |

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

🟡 **This index is the delivered slice of T17.** The per-lane pages it originally specified —
`premiere-builtins.md`, `premiere-plugins.md`, `ffmpeg-recipes.md`, `lane-choice.md` — are **not
written**. The lane-choice decision and the paid-tool position are captured here; the Premiere
"which effect" question is answered more concretely by the live
[`effects-catalogue.md`](../premiere/effects-catalogue.md) than a distilled page would have been;
and ffmpeg recipes still live in [`docs/flow/post-production.md`](../flow/post-production.md) plus
briefs 12–18. There is also **no `video-fx` skill yet** — reach for `premiere-automation` for the
edit and `flow-prompt` for the element.

Plan and remaining scope:
[`design/2026-08-21-premiere-bridge-and-video-fx.md`](../../design/2026-08-21-premiere-bridge-and-video-fx.md).
