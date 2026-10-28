# docs/images — standalone images (GPOM's anchors)

The home for **standalone BadCode images** outside a specific comic: site headers,
openers, social frames. Images here are produced with the **`new-image`** skill
(`.claude/skills/new-image/`), which drives Google Flow to generate them.

**There is no BadCode house look** (Kai, 2026-10-28; [`../stories/STYLE.md`](../stories/STYLE.md)).
The images indexed below are **GPOM's anchors** — the near-black, one-thin-light,
monumental-machine register is GitPush Origin Master's look (its
`docs/stories/gitpush-origin-master/look.md`), not BadCode's. They stay in this folder
so existing links keep working; use them only when the job is GPOM's look. A brand image
for anything else takes its look from the story it belongs to, or from a variation round.

**Convention:** every generated image is `<slug>.jpg` with a sibling `<slug>.md`
record holding the exact Flow prompt, media id, and revision log — so "just like
that, but change X" is one cheap `flow_refine`. Brand images that live elsewhere
(a story dir, an `apps/web` asset path) still get an index row here.

## Index

| Image | Record | Note |
| --- | --- | --- |
| [`register-anchor.jpg`](./register-anchor.jpg) | [`register-anchor.md`](./register-anchor.md) | **GPOM's register anchor** (its MACHINE register). Near-black server hall, one thin blade of light, LED constellations — originally gpom-short panel 1 (story folder deleted 2026-08-06; relocated here), with its exact Flow prompt in the record. The calibration reference for GPOM stills only — not for other stories. |
| [`gpom-short-opener.jpeg`](./gpom-short-opener.jpeg) | — (predates the skill) | A comic-viewer screenshot of the anchor above, with browser/UI chrome baked in. Kept for history; use the raw `register-anchor.jpg` instead. |
| [`server-hall-monolith.jpg`](./server-hall-monolith.jpg) | [`server-hall-monolith.md`](./server-hall-monolith.md) | GPOM anchor variant with the hall slightly more readable — door-slit light at the aisle's end, rack faces just catching the spill. First image produced by the `new-image` skill. |
