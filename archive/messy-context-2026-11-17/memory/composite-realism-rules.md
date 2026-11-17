---
name: composite-realism-rules
description: What made an AI person sit in real footage for Jack (2026-10-18) — scale by a same-depth reference, track the person's own plane, defocus by depth
metadata:
  type: feedback
---
Putting an AI character into real footage: Jack called the first Denise "crazy" (random size) and Barry under a near-locked sign shot "somewhat realistic".

**Why:** on a handheld plate the near and far planes move differently, so tracking the whole frame left her the wrong size as the camera pushed in. She was also an extra in a real person's shot, with nothing at her depth to measure her against.

**How to apply:**
- Pick the steadiest plate.
- Put a real person or object at the character's depth and prompt "head the same size and level with X".
- Add "Do not zoom, crop, reframe or move anything" to the Nano Banana prompt, or it reframes.
- Track only the character's depth plane (composite2.py's tracking box).
- Defocus the character by depth.
- Clip the keep-box above invented props.

Turning the character away from the lens hides the face, which is the most AI-looking area, and also avoids Flow's "prominent people" block. See [[bank-robbery-resume]].
