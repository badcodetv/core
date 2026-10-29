# Sketched white shadow — Flow exploration (2026-10-21)

> 🗄️ **Archive — a record of one 2026-10-21 exploration, not a template.** The prompts below describe
> BadCode as "making drum and bass", and some carry a near-black ground and a club setting: that was
> one story's sound and look leaking into the brand at the time. There is no BadCode house sound or
> look ([`docs/stories/STYLE.md`](../../../stories/STYLE.md)); the logo is the only house mark
> ([`docs/brand/README.md`](../../README.md)). Do not reuse these prompts' style words.

Jack asked for the logo with **white shadows, as if sketched, but subtle**, on the ring, the red triangle and
`badcode`, in his variant of the o (red o + small white triangle + thick white outline, bench style
"Red o + white triangle + outline"). This is an **exploration, not the logo** — Kai's ruled logo is still
"Saved version 5" (`docs/brand/README.md`).

Two routes exist:

- **Code (exact):** the logo bench's **Sketched shadow** control (bench v7) — geometry can never drift.
- **Flow (this file):** Nano Banana 2, one reference. Can look more hand-made, but the engine may redraw the
  letters, which the brand rules forbid (*always the drawn letters*). Judge every candidate against the reference
  at 100% before keeping it.

## Shot spec (shot-craft)

- **Job:** the mark reads as touched by a hand — a person drew this — without losing its flat, exact shape.
- **Register:** flat graphic artwork on near-black paper. Not a photograph, not a mock-up.
- **Gate 2 (visible cost):** not applicable — a logo is not a monumental shot.
- **Light:** implied, from the upper left; the shadow falls down and to the right. One direction for every part.
- **Focal point:** the logo, winning on brightness. The shadow is about a third as bright.
- **Withheld:** everything else — no scene, no wall, no paper edge, no props.

## Phrasing decisions (flow-prompt + 2026-10-21 web research)

- One reference with its job stated; keep / add written positively (`docs/google-flow/nano-banana-2.md`, fourth pass).
- One named medium and one paper (white chalk pencil on black paper), stroke behaviour described: one hatching
  direction, uneven pressure, overshoot, pencil lifts, a finger smudge at one end. Uniform line weight and evenly
  applied hatching are the reported AI-pencil tells `[community, weak]`.
- The logo itself named as flat with no gloss, bevel or glow — glossy effects and fake 3D shadows are the
  reported AI-logo tells `[community]`. One short exclusion clause only.
- No "realistic", "highly detailed", "textured" (over-rendering words) `[unverified]`.

## Prompt — round 1

Settings: Nano Banana 2 · 1:1 · 2 outputs · Attach: `reference-white-tri-outline-o.png`

```
Image 1 is our logo: a white ring with a rounded red triangle inside it, and the word "badcode" underneath in thin round lowercase letters, where the o is a red disc with a white rim and a small white triangle. Keep the logo exactly as it is in image 1, every shape, line thickness, gap, position and colour, flat and crisp on the same near-black paper.

Add only one thing: a faint shadow drawn by hand in white chalk pencil on the black paper, falling a little down and to the right of every part of the logo, the ring, the red triangle, each letter and the o, as if lit from the upper left. The shadow is loose diagonal hatching in one direction, strokes of uneven pressure and length, a few overshooting the edge, small gaps where the pencil lifted, softened with a finger smudge at one end only, the grain of the paper showing through. It is quiet, about a third as bright as the logo, so the logo is still the first thing you see.

The logo stays flat graphic artwork with no gloss, bevel or glow, and the background stays plain near-black paper with nothing else on it and no other text. Square, 1:1. Thanks.
```

## Revision log

| Round | Date | Change | Result |
| --- | --- | --- | --- |
| 1 | 2026-10-21 | first prompt, `flow_edit_image`, NB2, 1:1, x2, project 53c32ef8 | `r1-a.jpg`, `r1-b.jpg`. **The hatching reads as genuinely hand-drawn** (one direction, uneven pressure, overshoot, smudge) — the medium words worked. **But the logo drifted in both:** the letters were re-set as a heavier typeface (brand rule: always the drawn letters), the triangle came back sharper, the ring thinner on b. **Not subtle:** the shadow is roughly as bright as the logo, not a third; on a it also fills the inside of the ring up-left, against the stated light. As predicted, NB2 does not hold exact geometry. |
