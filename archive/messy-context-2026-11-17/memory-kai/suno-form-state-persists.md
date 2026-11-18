---
name: suno-form-state-persists
description: "2026-08-27 general law — filling Suno's four boxes changes NOTHING else; mode, attachment, Voice and duration all persist. Omitting a spec field is not clearing it."
metadata:
  type: feedback
---

🔑 **THE LAW: omitting a field is not the same as clearing it.** Filling style/excludes/lyrics/
taste changes those four boxes and **nothing else**. Every other piece of Suno form state
survives into the next run. Three instances, all on 2026-08-27:

| State | How it bit | Guard now in `suno.mts` |
|---|---|---|
| **Mode + attachment** | an inherited **Cover** form made two narration pairs into covers of a Camping track — 40 credits + a confident false diagnosis | `formMode()` aborts on wrong mode or any attachment |
| **Saved Voice** | an *instrumental* run carried `badcode newsreader` because the spec had no `voice` key | aborts if a Voice is on and the spec wants none |
| **Duration** | **8 takes at 1:05 from specs with no `durationSec`** — an earlier round set 65 | `setDurationAuto()` runs whenever `durationSec` is absent |

**Any spec field mapping to form state needs an explicit "off" path.** Assume anything not
actively set is whatever the previous session left.

⚠️ **`status.durationSec` is unreliable** — it kept reading `65` after the input was verified
empty. Authoritative read: `input[placeholder="Auto"][type=number]`; its placeholder is *Auto*,
so **empty IS Auto**.

🔑 **Suno replaced the Advanced duration SLIDER with a `Duration / Custom / Auto` number box**
(1–300), so `setSlider(page,'Duration',…)` had been writing to nothing — which is why a 9-line
spoken block could run to 7:59 with no lever to stop it.

⚠️ **Anchoring on that block's text is unreliable** — it reads "DurationCustomAuto" or just
"Duration" depending on toggle state. Anchor on the input.

Related: [[suno-check-form-mode]], [[suno-four-box-atom]], [[suno-one-session-at-a-time]]

**2026-09-16 (v6):** clicking Custom mounts a `Duration` slider (default 180) and THAT is what Suno obeys; the number box read 80 while takes came out at 3:00. `setDuration` now drives the slider. Same day: the workspace picker prefix-matched `gpom-story` → `gpom-story-recut`; now exact-row real click, read back, blocking.
