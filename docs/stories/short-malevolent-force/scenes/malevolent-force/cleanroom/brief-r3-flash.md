# Brief: the last shot of "The Malevolent Force", remade (clean room)

You write prompts for Google Flow: stills for **Nano Banana 2** (vertical 9:16) and image-to-video motion prompts for
**Omni 1.2 Flash** (Frames mode: the still is the start frame; 8 s; vertical 9:16). Research on the open web first.
Read ONLY this brief and the images listed; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16, on the old last shot)
"we need a different video to show the bread and the freddo changing pice, it needs to be a flash of lightning like in a horror way, then it changes price, but the bread and freddo need to be somewhere else in the shop. Thanks."

## The short
Buying bread at a British corner shop at night, shot like a haunting, about 15 s, no voice, then an end card
("Based on true events. Coming to a shop near you."). The ghost is inflation: the bread's price climbs 50p → £1 → £5
→ £50 and nobody is ever seen. **The point:** someone decides who gets the new money first, and you meet it last at
the till. **The force is never seen: no person, face, hand, figure or a person's shadow.**

The shots before this one (already made, look at them to match the shop and the look):
- `~/.cache/badcode/mf-anim/FO2-c.jpg` the shop from across the wet street
- `~/.cache/badcode/mf-anim/PR2-e.jpg` the glass door from inside
- `~/.cache/badcode/mf-anim/PR2-c.jpg` the aisle, stockroom door at the back
- `~/.cache/badcode/mf-anim/PR2-b.jpg` the loaf on a bare shelf, "50p" (this shot ends at £5 after flickers)
- `~/.cache/badcode/mf-anim/FO2-d.jpg` the convex mirror, blank notes on the floor
The look: the director's reference photo, `docs/stories/short-malevolent-force/scenes/malevolent-force/reference/jack-r2-shop-doorway.png`
(path from `/home/jackt/projects/badcode/badcode`): cheap colour film at night, grain, soft focus, fluorescent teal.

## This shot
A loaf of plain white sliced bread and a small purple chocolate bar (the "freddo": a cheap UK kids' chocolate bar
everyone remembers costing 10p; draw it **unbranded**: plain purple wrapper, no logo, no brand name) sit together
**somewhere in the shop we have not seen yet** (not the bread shelf, not the doorway mat). Lightning flashes, horror
style, and when the light comes back the prices have changed.

- **Before the flash:** bread £5, chocolate bar 10p.
- **After the flash:** bread **£50**; chocolate bar **10p crossed out, £12 beside it**.

**How it will be built (a fact, not a suggestion):** video models redraw writing badly, so the price change is a cut,
hidden in the white of the flash: a BEFORE still and an AFTER still of the same framing, each animated, cut together on
the flash frame. So for each option write: a BEFORE still prompt and an AFTER still prompt that are word-for-word the
same except for the price text (and anything else you deliberately want to have changed after the flash: a horror
jump-cut may change one more small thing); a BEFORE motion prompt where the lightning flash comes at about 2-3 s; an
AFTER motion prompt that starts just after the flash (the light settling, the room humming, one small event at most).

## Hard facts
- No dialogue, no voices, no people. Sound from the video model is not used.
- Camera locked in every clip; any push is added in the editor. One continuous shot, no cuts.
- Text must stay exactly as in the still in every clip.
- Lightning: a flash through a window or the glass door is the light source; no more than 3 flashes a second; nothing falling or flying through the air.
- No real brands, no real people. End every prompt (still and motion) with the word "Thanks."
- Keep the look of the reference photo and the shots above: same shop, cheap night colour film, grain, teal.

## Your task
1. Research: horror lightning-flash reveals and jump cuts (how films stage "the flash, then something has changed");
   how to prompt Nano Banana 2 for a candid colour-film night still and legible short price text; how to prompt
   lightning in image-to-video (Omni / Flow) while keeping the frame stable.
2. Write THREE genuinely different options (a, b, c): different places in the shop, different framing (insert,
   medium, wide), different way the lightning gets in.
3. Write JSON to `docs/stories/short-malevolent-force/scenes/malevolent-force/cleanroom/prompts-r3-flash.json`:
   `{"research": ["url — takeaway", ...], "notes": "...", "options": [{"id": "a", "place": "where in the shop", "label": "a few words", "still_before": "...", "still_after": "...", "motion_before": "...", "motion_after": "...", "risk": "..."}, ...3]}`
