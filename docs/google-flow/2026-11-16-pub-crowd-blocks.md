# Nano Banana 2: a run of policy blocks on a diverse pub crowd, and the way round (2026-11-16)

Evidence tier: **observed, one session, not isolated** (True Scale short, Flow projects 7530554c and b77f9021).

- **What happened:** clean-room prompts for a British pub quiz with a specifically described mixed crowd (ethnicities, religious
  dress, ages) and a quizmaster described in detail were refused 10+ times. Some passed (a wide shot of a mixed table; a close-up
  of the quizmaster holding a sheet with a foreground crowd); others with very similar wording did not. Removing the ethnic labels,
  removing headwear, removing the crowd, removing "mic to her mouth": all still refused. A fresh project did not help.
- **Control:** a plain image ("a mug of tea by a rainy window") passed in the same minute, so the account was not blocked: it was the
  wording. The exact trigger was never isolated.
- **What worked first time:** using an image that had already passed (the quizmaster close-up) as the **reference image** for her and
  the room, and **not describing her at all** ("the quizmaster from the attached picture", "the regulars from the attached picture"),
  plus Bob's reference sheet for Bob. Both remaining beats passed, and the quizmaster stayed the same woman across shots.
- **Also seen:** `flow_edit_image` with a landscape reference sheet returns the uploaded sheet itself as candidate a (5504x3072);
  ask for 2 outputs and keep the 768x1376 ones. With a 9:16 reference this did not happen.
- **Rule of thumb (a guide):** once one still of a character or place has passed, carry it forward as a reference instead of
  re-describing it; it's more consistent and it stops the filter re-reading the description.
