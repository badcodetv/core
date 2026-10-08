# The Bank Robbery — fourth-pass stills (8 October 2026)

**Asked for by Jack, 8 October 2026:** "make the changes you were going to make to bank robbery." These are the
re-made shots from [`review-cut1.md`](./review-cut1.md), "What I would do next", item 2.

**Stills only. No video has been made from them.** Jack picks first; then each pick is animated and swapped
into cut 2.

- **Settings:** Nano Banana 2, 16:9. Flow project `63d22c4b`. Two candidates for the uncast shots and for the
  two Mr Blue re-rolls; one for the other cast shots.
- **Prompts:** [`scripts/bank-robbery/br-stills-v4.json`](../../../scripts/bank-robbery/br-stills-v4.json), built
  the same way as the third pass (`pre` when a Character is attached, the shot's `body`, then the colour lock).
- **Runner:** `scripts/bank-robbery/br-stills-v4.mjs` for the cast shots; the two uncast shots went through the
  `flow_generate_image` tool, which also put the compose bar back on images and Nano Banana 2 (it had been left
  on Video).
- **Files:** `Desktop\Youtube Vids\animation\bank robbery\images\scenes-v4\`.

## The shots, and what each one is for

| Shot | What was wrong | The new design | Light |
| --- | --- | --- | --- |
| `s12e-sold` | The SOLD board was a few pixels wide | Same view, out of the staff-room window, on a long lens: the board fills a third of the frame, one word on it, a gloved hand and a drill at its corner, her dark window and one pot plant beside it | One orange street lamp, from below |
| `s12b-count` | Denise looked fifteen years older, and a SOLD board was already behind her | Camera on the table looking up past the open savings book at her face as she counts. No window in frame, so nothing gives the ending away | Blue dusk from a window out of frame |
| `s12f-kebab` | The sign was cursive neon, not the logo | The same low view across the wet road, square on, with a plain dark-blue sign board and no writing anywhere. The real logo is added afterwards with ffmpeg (preview: `s12f-kebab-a-with-logo-PREVIEW.png`) | The bulbs over the sign and the shop window |
| `s09c-pallet` | Daylight and a white sky after a dusk shot with flares; two men carrying four tonnes by hand | Dusk, the crowd's backs, pink and blue smoke, and the load on a hand pallet truck: Mr Blue hauls, Mr Red pushes, both shouting | One red hand flare in the crowd |
| `s04i-drivers-freeze` (a, b) | Mr Blue did not look like Mr Blue | The third-pass prompt, unchanged, rolled twice more | As before |
| `s07-night-before` (a, b) | The same | The second-pass prompt, unchanged, rolled twice more | As before |

**Not re-made: `s12a-standoff`.** The review listed it, but on a second look the man at the left edge matches the
Mr Blue portrait (heavy, grey, navy tie). The plate also drives two talking clips. Left alone unless Jack says
otherwise.

## Results

All eight came back first time, no blocks. Read by eye, not yet seen by Jack.

| File | Read |
| --- | --- |
| `s12e-sold-a`, `-b` | SOLD is spelt right and readable at a glance in both. **b** is the stronger: the arm and drill are in frame, the board is larger |
| `s12b-count` | Reads as the café Denise. A window shows at the right edge with plain dusk sky in it and no board. She has two books open, not one |
| `s12f-kebab-a`, `-b` | Both signs are blank. **a** is squarer on and takes the logo cleanly (see the preview file) |
| `s09c-pallet` | Dusk, flare, pink and blue smoke, pallet truck. Both men match their portraits |
| `s04i-drivers-freeze-a`, `-b` | Mr Blue matches his portrait in both. **b** is closer to the breakfast Mr Blue |
| `s07-night-before-a`, `-b` | Mr Blue matches in both. In **a** Mr Red wears tortoiseshell glasses he has nowhere else; **b** has no glasses on him at all |

## What happened next (8 October 2026, late afternoon)

Jack: "use the new stuff, but i liked the old kebab badcode ending, dont replace that." So:

- **Animated and in cut 3:** `s12e-sold-b`, `s12b-count`, `s09c-pallet`, `s04i-drivers-freeze-b`,
  `s07-night-before-b`. The pick of each pair was mine. Clips in `vids\v4\`; motion prompts in
  [`scripts/bank-robbery/br-clips-v4.json`](../../../scripts/bank-robbery/br-clips-v4.json); where each sits is
  in [`assembly.md`](./assembly.md), "Cut 3".
- **Not used:** `s12f-kebab-a`, `-b` and the logo preview. The ending keeps the old neon sign.
