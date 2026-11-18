---
name: suno-check-form-mode
description: "2026-08-27 — Suno's create-form MODE and attachments survive a box fill; an inherited Cover form silently generates covers. Check mode BEFORE the boxes. Kai: one Suno tab, ever."
metadata:
  type: feedback
---

🔴 **The create form has four mode tabs — Simple · Audio · Custom · Cover — plus an
`Audio / Voice / Inspo` attachment row. Filling the four boxes clears NONE of it.**

An inherited **Cover** form with a source attached **silently generates covers of someone
else's track**, carrying that track's arrangement, while `status` reports style, excludes,
lyrics, sliders, title and workspace all correct.

**What it cost (2026-08-27):** two GPOM narration pairs — revisions A and B, **40 credits** —
generated as covers of a Camping source another session left attached. Both void.

🔑 **And it produced a confident false diagnosis.** "There is music under my dry read" was
blamed on the My Taste box (which did wrongly describe a cello) and on audio-influence bleed
from a Voice cloned off an orchestral track. Both were real bugs worth fixing — **but the
cover attachment was the dominant cause, and nobody had looked at the form's mode.**
Generalise it: **`status` reads the boxes, not the KIND of thing being made. A green-looking
form is not a safe form.**

**Fixed in `scripts/suno/suno.mts`:** `load` calls `formMode(page)` before filling anything and
aborts on a wrong mode or any attachment; `SunoSpec.mode` defaults to `'custom'`.
⬜ It reports, it does not clear — removing an attachment is a human act, and the selectors
have had one live read only.

🔴 **Kai's ruling, 2026-08-27: ONE Suno tab, ever.** *"we're never going to run more than one
Suno tab at a time… we're getting in a real mess here."* Not one per channel — one, full stop.
The form, its mode and attachments, My Taste, the Voice list and the credit pool are all
account-level. The `MUST_REPLACE_HERE` freedom token manages handover BETWEEN sessions; it does
not make them concurrent. If another session is working, **wait**.

Related: [[suno-one-session-at-a-time]], [[suno-four-box-atom]], [[dry-and-separate-narration]]
