---
name: suno-v6-set-duration-auto-runs-long
description: On Suno v6 always set Duration explicitly — Auto runs long, and a set target is obeyed to about a second.
metadata:
  type: reference
---

**Proven 2026-09-18 (Camping r47 vs r48, same lyrics, same day).**

- **Duration Auto on v6 runs long** — takes came back at **4:38 and 4:55** from a song whose
  reference take was 2:46.
- **A set Duration is obeyed tightly**: a 195 s target gave **12 takes out of 12 at 3:14–3:16**,
  across three different Style boxes and two weirdness settings. About ±1 s.

This supersedes the v5.5-era reading that duration "shortens but does not obey". **Always set the
number**, aiming slightly above the target, since it still shortens more readily than it stretches.

⚠️ Still unknown: whether Custom duration doubles the credit cost (r17's suspicion) — the credit
counter read `null` on both rounds, so two uses have gone by unpriced. Related:
[[listening-setup-jacks-machine]].

⚠️ **The ±1 s obedience loosens when the target squeezes the words (2026-09-21, Camping r55).** At
195 s the hit rate was 12/12 then 24/24 within a second. At **155 s** — the same ~60 lines, 20%
less room — nine of fourteen landed at 2:34–2:36, but `action` w30 came back at **2:43** (both
takes) and `adventure` w30 at **2:58**, a 23-second overshoot. ⬜ Unverified as a rule; one more
round decides it. **Practical effect: when duration is being used as a pacing lever, check the
returned length before blaming the prompt** — a long take simply had more room to slow down in.
