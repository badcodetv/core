# Illustrations to make in Flow (prompts; nothing generated yet)

Nine plates. Until each exists, its grey placeholder (`clips/cards/PH-<name>.png`) holds its place
on the timeline, so the rough cut plays without them. **Kai approves every plate before any video
credit is spent** (house rule), and nothing here shows a real, living person.

The storyboard leaves the illustration look open (*"Their appearance is deliberately undecided"*,
§2). Two looks are offered for the scene-03 fable; pick one at the plate gate and use it for all
five, so the builder is the same man in every frame.

| Look | What it is | Why |
| --- | --- | --- |
| **A · period print** | A flat, two-colour lithographic print, as on a 1930s British public-information poster: bold simplified shapes, visible paper grain, off-white and one muted brick red | Reads at once as *illustration*, never as archive, and belongs to the decade it describes |
| **B · ink and wash** | A loose pen-and-ink drawing with grey wash on cream paper, like a reportage sketchbook | Quieter; sits well beside the black-and-white archive without imitating it |

Every prompt is 16:9, **no text or lettering in the image** (the cards carry the words), and names
the look at the end so one line swaps A for B.

## Scene 03 — the builder (five plates, one man)

Character line, repeated in each: *a British builder in his forties, 1930s, flat cap, rolled
sleeves, braces, a lean tired face, a trowel in his belt.*

| Plate | Prompt |
| --- | --- |
| **03-A** idle | A British builder in his forties, 1930s, flat cap, rolled sleeves, braces, a lean tired face, a trowel in his belt, sitting on an upturned crate in an empty builder's yard, hands hanging between his knees, waiting. Stacks of timber and a cold cement mixer behind him. Wide shot, grey morning light. *{look}* |
| **03-B** family | A British family in the early 1930s, a mother, a father and two children, crowded into one small rented room: a bed, a table, washing hanging on a line across the ceiling, damp on the wall. The mother looks out of the one window. Medium-wide shot, dim window light. *{look}* |
| **03-C** bricks | A neat stack of new red bricks and a pile of sand in a builder's yard, 1930s Britain, a wheelbarrow leaning against them, nobody there. Close, low angle, still. *{look}* |
| **03-D** at work | The same British builder in his forties, flat cap, rolled sleeves, braces, now laying bricks on a house going up on an open plot: the walls waist-high, a line strung true, a mate carrying a hod behind him. Morning sun. Medium shot. *{look}* |
| **03-E** empty plot | An empty plot of grass and rubble between two rows of 1930s terraced houses, a For Sale board lying flat, nobody there. Wide, flat grey light. *{look}* |

`{look}` A = *Flat two-colour lithographic print in the style of a 1930s British public-information
poster, bold simplified shapes, visible paper grain, off-white and one muted brick red, no text.*
`{look}` B = *Loose pen-and-ink drawing with grey ink wash on cream paper, reportage sketchbook style,
no text.*

Scene 04 opens on 03-D "with a thousand plots multiplying": make it in Premiere (scale 03-D down
and tile it), not in Flow.

## Scene 11a — the yacht

| Plate | Prompt |
| --- | --- |
| **11A-Y** | A large two-masted sailing yacht at anchor in a calm blue bay, seen from a distance, white hull, sails furled, no people visible, no name on the hull, no flags. Plain, even daylight. *Drawn as a simple, flat vector illustration with no detail that identifies a particular vessel, no text.* |

🔴 It must not be, or look like, a photograph of *Lady M* (or either of the other yachts of that
name). Plain illustration only, labelled `ILLUSTRATION` on V4. Waits on the scene-11a legal read
like the rest of the scene.

## Scene 15 — the coda (in GPOM's near-black look)

⚠️ **Borrowed from GPOM — a candidate, not inherited; Kai to rule (2026-10-29 audit).** This is GPOM's
MACHINE register (written when the `new-image` skill called it the brand register; anchor
`docs/images/register-anchor.jpg`), not an MMT or BadCode look — MMT's look is in [`../look.md`](../look.md).
The plates as drafted: near-black, one
thin light, and one small region deliberately brighter than the rest so the dark reads as depth.
The coda is the one hopeful image set in the film: calm, not menacing, and never "the machines are
coming".

| Plate | Prompt |
| --- | --- |
| **15-A** seed | A single seed resting in dark, freshly turned soil, one thin shaft of cold light falling on it from above, everything else near-black. Extreme close-up, shallow depth. |
| **15-B** machines | Slender robotic arms in a vast dark hall, calmly laying bricks for a small house, one thin light across the work, the rest near-black, patient and unhurried, not menacing. Wide shot, the arms small against the space. |
| **15-C** sapling | A young green sapling standing where the seed was, the same dark soil, the same thin light now slightly warmer, near-black around it. Close-up, same framing as the seed. |

15-A and 15-C must share framing so the cut between them reads as time passing: generate 15-C by
editing 15-A (`flow_edit_image`, reference-anchored), not from scratch.

## Animation (only after Kai approves a plate)

Per the hybrid method: Veo animates with the camera **locked**, and Premiere moves the camera. Only
15-A→15-C (the sapling growing, locked-off) and 15-B (the arms working) are worth animating; the
scene-03 plates hold as stills with a PUSH.
