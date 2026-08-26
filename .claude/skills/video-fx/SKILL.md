---
name: video-fx
description: >
  Use when CHOOSING how to achieve a video effect or finish — "what effect does X",
  "how do I make it look like X", "which tool should I use for this", "can Premiere do
  X", "is there a filter for X", "add fire / smoke / rain / sparks", "make this black
  and white", "zoom into a map", "make it look like the transmission is failing", "do
  we need a plugin for this", "is this file ready to upload", "what should I export
  as", "why does this look crushed on YouTube". Owns the JUDGEMENT — which of the five
  lanes, which installed effect, what it costs, and the delivery gate before anything
  ships. Mechanics live elsewhere: driving Premiere is premiere-automation, driving
  Flow is flow-automation, writing a Flow prompt is flow-prompt, sourcing real footage
  is find-footage, and what the shot should LOOK like is badcode-art-direction.
---

# video-fx — which lane, which effect, and what it costs

**The judgement half.** You have been asked for a *result* — fire, a map zoom, a film look, a
glitch, a file that survives YouTube. This skill decides **what to reach for**. It does not
drive anything.

> **🔴 THE STANDING RULING (Kai, 2026-08-21): NO PAID PLUGINS. NO PAID FOOTAGE.**
> *"We don't really need any paid plugins because they all sound far too advanced, and for smoke
> and fire we could use Flow anyway."*
> **Never end an answer at "buy X."** State the free route. If there genuinely isn't one, say so
> plainly and let Kai decide. The free stack is: Premiere built-ins (106 effects, 118 transitions,
> 77 MOGRTs — all installed), Lumetri, ffmpeg, Flow for anything invented, and the green tier of
> `find-footage` for anything real.

## What this skill is not

> **🔴 "Why does this look flat / boring / generic / like AI?" is NOT this skill.**
> That is a shot-*design* question and belongs to **`shot-craft`**
> (`docs/cinematography/symptoms.md`). Reaching for an effect to fix a badly designed frame is
> the most expensive wrong turn available here — no filter fixes a frame with one depth plane
> and no motivated light.

| Question | Skill | It answers |
| --- | --- | --- |
| **What should I reach for?** | **this skill** | Which lane, which effect, what it costs, is it even installed |
| How do I make the call succeed? | `premiere-automation` | Bridge state, tool surface, why a call failed |
| How do I make Flow generate it? | `flow-automation` | Browser up, MCP tools, recovering a hung call |
| What do I write in the Flow prompt? | `flow-prompt` | Veo/Nano Banana platform craft, policy blocks |
| Does real footage of this exist? | `find-footage` | Sourcing and licence clearance |
| What should the shot look like? | `badcode-art-direction` | The BadCode visual register |

---

## Step 1 — Lane choice, before anything else

**Five lanes.** Pick by what the job actually needs, not by habit.

| Lane | Reach for it when | Why |
| --- | --- | --- |
| **Flow** | It does not exist yet and must be **invented** — fire, smoke, sparks, weather, a crowd, a city, an impossible camera move | We have no particle systems and are not buying any. Free at the margin on Ultra, and genuinely good at elements |
| **Sourcing** | It is **real, already filmed, and its being real is the point** — an Apollo launch, a 1950s factory floor, the fall of France | Inventing it would be both worse and a lie. `find-footage`, and mind the licence gate |
| **ffmpeg** | The result must be **exact, repeatable and headless** — conform, concat, trim, retime, LUT, grain, delivery encode | Deterministic, scriptable, no GUI in the loop |
| **Premiere** | It is part of **the edit** — cuts, dissolves, keyframed motion, a grade judged against the cut, compositing a Flow element over a plate, titles | Real-time preview, the effect catalogue, and the session can `export_frame` and *look* |
| **After Effects** | True 3D, planar tracking, complex motion graphics | 🔴 **Not installed on this machine.** Flag it as out of scope; do not design around it |

**The tie-breakers:**

- If a human will iterate on it **by eye** → Premiere.
- If it is a transform with **one right answer** → ffmpeg.
- If it **does not exist** → Flow.
- If it **already exists and really happened** → source it, and check the licence before you cut it.

---

## Step 2 — "What effect does X?"

🔴 **Check the catalogue before searching the web.** 106 effects and 118 transitions are already
installed, harvested live and grouped by what you would actually ask for:
[`docs/premiere/effects-catalogue.md`](../../../docs/premiere/effects-catalogue.md).

| The ask | Go to |
| --- | --- |
| Colour, grade, film look, LUT | effects-catalogue § *Colour and grade* |
| The BadCode near-black register | effects-catalogue § *The BadCode near-black register*, and recipes § *the BadCode near-black look* |
| Glitch, decay, "the transmission is failing" | effects-catalogue § *Glitch, decay* |
| Blur, focus, depth | effects-catalogue § *Blur and focus* |
| Push in, pan, reframe, stabilise, retime | effects-catalogue § *Movement, framing, stabilisation*; recipes § *a push-in, a pan, a fade* |
| Keying a Flow element over a plate | effects-catalogue § *Compositing and keying* |
| Text on screen | effects-catalogue § *Text and graphics without a MOGRT*, **or** the 77 installed templates in [`mogrt-catalogue.md`](../../../docs/premiere/mogrt-catalogue.md) |
| Dissolves and which one | effects-catalogue § *The ones you will actually use* |
| A concrete tool call for any of it | [`docs/premiere/recipes.md`](../../../docs/premiere/recipes.md) — the cookbook |
| An ffmpeg filter | [`docs/flow/post-production.md`](../../../docs/flow/post-production.md) first, then briefs 12–18 |

**Not in the catalogue?** Read [`docs/video-fx/README.md`](../../../docs/video-fx/README.md)
§ *What we deliberately don't own* — it names the free route for every paid tool we refuse.

---

## Step 3 — The house answer for atmospherics

Asked for **fire, smoke, sparks, rain, fog, dust, embers, explosions**:

1. **Generate the element in Flow on a pure black background** (`flow-prompt` for the wording).
2. Import it and put it on a video track **above** the plate.
3. Key the black out — **Luma Key** (`AE.ADBE Legacy Key Luma`) or **Extract** (`PR.ADBE Extract`);
   soften with **Edge Feather** if it reads as cut out.
4. Or headless: ffmpeg `blend=screen` / `overlay`.

Full walkthrough: recipes § *fire, smoke, sparks — the free route*.

🟡 **Free stock is the fallback if Flow will not produce it — but go through `find-footage`, not
from memory.** That tier is amber, not free-for-all: Pexels and Pixabay both carry an explicit
political-context exclusion, Adobe Stock Free bars implied political endorsement, Mixkit mixes
non-commercial clips into the same results, and **Videvo and Mazwai are dead** (both 301 to
Freepik — any blog post describing their old CC tiers is stale).

---

## Step 4 — 🔴 The delivery gate

**Nothing ships unmeasured.** This is the step that silently ruins near-black films.

```bash
scripts/delivery-qc.sh RENDER.mp4 shorts     # youtube · shorts · reels · tiktok
```

Read-only, needs only ffmpeg, exits non-zero on a real fault. Reference:
[`docs/video-fx/delivery.md`](../../../docs/video-fx/delivery.md).

### The one that actually bit us

`camping.mp4` — the finished film — shipped **full-range content with no colour tag at all**
(`YMIN=0 YMAX=255`, `color_range=unknown`). A player that finds no tag assumes limited range and
expands 16–235 to 0–255. Applied to content already at 0–255, **everything below 16 flattens to
black.** BadCode's whole register lives in the shadows, so this is not a subtle grading difference
— it is the picture. It is invisible until you measure it.

```bash
ffmpeg -i in.mp4 \
  -vf "scale=in_range=full:out_range=limited" \
  -pix_fmt yuv420p -color_range tv \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:v libx264 -crf 18 -c:a copy out.mp4
```

🔴 **`out_range` alone is a silent no-op.** Drop `in_range=full` and ffmpeg assumes the input was
already limited, does nothing — **but still writes the `tv` tag.** You manufacture exactly the
mismatch you were fixing, and now it clips the whites. **Both halves are load-bearing.**

🔴 **Deliver limited range, not full.** libx264 will not produce `yuv420p` at full range — you get
deprecated `yuvj420p` even with an explicit `-pix_fmt`. Keep the shadow precision in the *master*;
convert on the way out.

🟡 **No scope readback exists inside Premiere.** No UXP API exposes Lumetri Scopes values, so QC
happens on the rendered file. Hand the eyeball check to the human.

---

## Step 5 — Record what you learn

**Toolkit first → web on a miss → write it back.**

1. Check the catalogues and this skill. The answer is usually already installed.
2. Check the 20 research briefs in
   [`design/research/2026-08-21-video-fx-landscape/`](../../../design/research/2026-08-21-video-fx-landscape/README.md)
   for technique. 🔴 They predate the no-paid-plugins ruling — read them for the *technique*, never
   the shopping.
3. **Only then search the web** — and when you find something, write it back into the catalogue or
   a brief, **dated**, so the next session does not pay for it again.
4. **Never end at "buy X."**

**On prices:** a price without a live vendor page is quoted as *unconfirmed*, never as a number.

---

## Where everything lives

| | |
| --- | --- |
| Lane choice, the paid-tool position | [`docs/video-fx/README.md`](../../../docs/video-fx/README.md) |
| Delivery specs and QC | [`docs/video-fx/delivery.md`](../../../docs/video-fx/delivery.md) + `scripts/delivery-qc.sh` |
| Free-to-publish footage, 68 sources tiered | [`docs/video-fx/footage-sources.md`](../../../docs/video-fx/footage-sources.md) |
| Every installed effect and transition | [`docs/premiere/effects-catalogue.md`](../../../docs/premiere/effects-catalogue.md) |
| Every installed MOGRT | [`docs/premiere/mogrt-catalogue.md`](../../../docs/premiere/mogrt-catalogue.md) |
| Concrete tool calls | [`docs/premiere/recipes.md`](../../../docs/premiere/recipes.md) |
| Why the API did that | [`docs/premiere/api-notes.md`](../../../docs/premiere/api-notes.md) |
| Cutting to the beat | recipes § *cut to the beat* + `scripts/beat-grid.py` |
| Everyday ffmpeg | [`docs/flow/post-production.md`](../../../docs/flow/post-production.md) |
