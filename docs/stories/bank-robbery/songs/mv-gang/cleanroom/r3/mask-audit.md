# Mask audit of Balaclava Gang 4 (2026-11-04)

Jack: "the masks are wrong in a lot of the clips, watch and look for it then replace it" and "make sure you analyse the clips properly for the wrong masks to replace, i dont want to waste credits or time".

Method: every gang clip in `edit-plan-r4.json` (65 clips; the 10 Colour Noir `cn:` clips and f02-a have no gang mask). Full-size frames at 0.5–0.7 s, 3 s and 4–5.5 s, judged against the rule: a white ring; one small red triangle high on the right of the picture (the wearer's left eye); no eye holes, mouth or skin. A fault only counts if it can be seen at normal size.

## Wrong, to be replaced (37)

Gesture redos (cut 4):
- d01g-a: the mouth opens at the end.
- d06g-a: triangle in the middle.
- f01g-a: Crimson's triangle on the wrong side.
- g11-b: two red eye holes.
- v03g-b: no triangle.
- v05g-b: triangle in the middle, and he turns his back.
- v06g-b: triangle in the middle.
- v11g-b: triangle in the middle.

Older clips:
- a01-a: most men have no triangle.
- a01-b: eye shapes, no triangles.
- a02-a: red eye or face shapes.
- a02-b: the men at the back have eyes.
- a03-a: Marine has eye holes; Rust has no ring.
- a03-b: eye holes.
- d02-b: triangle in the middle.
- f03-b: triangle in the middle.
- v07f-b: goggle-like eye hole.
- v12-b: triangle on the left.
- k01-a: no triangles at all (this is the held ending shot).
- k02-b: goggles and eye holes.
- k03-a: triangle in the middle.
- k04-a: Crimson has none; Rust has eye holes.
- k09-a: a crescent, no triangle.
- k12-a: eye and mouth holes.
- k13-b: red eyes.
- k18-a: eye holes.
- k19-a: red eye marks.
- k21-a: no triangles; Marine's face is black.
- k22-b: triangle in the middle.
- k26-a: three men with no triangle.
- k27-b: Plum's triangle in the middle.
- k29-a: two red marks.
- k30-a: Silver has two eyes.
- k31-b: Plum's triangle in the middle.
- k36-b: three wrong.
- x03-b: eyes and eye holes.
- x07-b: Silver has eye holes.

## Right, or too small to read (28; keep)

c02-a, c02-b, c03g-a, c03g-b, c04-b, c04g-a, d01-b, d05-a, d11-a, d12-b, g08-b, g09-b, g10-b, k06-b, k07-a, k10-a, k11-a, k16-a, k23-a, k24-a, v01g-b, v08-b, v13g-b, x02-a, x04-a, x06-a, plus f02-a (no gang) and the Colour Noir clips.

## Fix order (cheapest first)

1. New stills: Nano Banana 2, at no credit cost. The new reference is `~/.cache/badcode-refs/gang/gang-lineup-heads.jpg`, the line-up with each mask enlarged. Each prompt is the shot's own prompt plus one precise sentence on where the triangle goes (`make_mask_fix.py`).
2. Check every new still by eye at full size. Only a still that passes goes to video.
3. Make one clip per passed still, with the same motion prompt as before. These cost credits.
