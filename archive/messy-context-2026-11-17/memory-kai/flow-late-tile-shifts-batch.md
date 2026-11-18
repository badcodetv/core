---
name: flow-late-tile-shifts-batch
description: Flow can save the PREVIOUS call's output under the new name (batch timeouts AND plain single video calls, 2026-11-10) — check mediaId, duration, md5 and a frame strip after every call
metadata:
  type: feedback
---

On 2026-10-16 a flow_generate_batch item timed out (dump said only "Failed / Failed to load image"). Re-running the rest in a new batch returned 8 files in ~2 minutes, but file 00 was the late finisher of the *failed* prompt, so every output was off by one and the final prompt's image was never saved.

**Why:** the harvest takes the newest finished tile; a late tile from the previous call jumps the queue.
**How to apply:** after any TIMEOUT in a batch, make a contact sheet of the re-run and check each frame against its prompt before naming files; regenerate the missing tail item alone. Related: [[flow-policy-blocks]], [[flow-moved-to-flow-google-com]].

**2026-11-10 (GPOM E rounds 8-9): it happens with single flow_generate_video calls too, no timeout needed.** Three times in one session a call returned the PREVIOUS call's mediaId (or a 6 s file where 10 s was asked) and saved the previous clip under the new name; the requested clip arrived on the next call. Tells: a repeated mediaId, a duration that doesn't match durationSeconds, an md5 equal to another file. **How to apply:** after every video call, md5 + duration + a 1 fps strip against the prompt before naming; rename by content, fix the recipe card's source_id, and expect one stray clip left in the Flow project.
