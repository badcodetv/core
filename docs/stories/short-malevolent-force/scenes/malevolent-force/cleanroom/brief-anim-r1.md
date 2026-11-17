# Brief: animate six stills for a BadCode short, "The Malevolent Force" (clean room)

You write image-to-video motion prompts for Google Flow's **Omni 1.2 Flash** video model, in **Frames** mode: each
still below is the clip's start frame, the clip is **8 seconds, vertical 9:16**. Research the model and the craft
on the open web first. Read ONLY this brief and the six images listed; open no other file on this machine.

## What the director said (verbatim, Jack, 2026-11-16)
"animate them please. thanks Please clean room it all and research the internet to achieve it. Thanks."
Earlier the same day, on the words: "No voice, one end card".

## The short
Buying bread at a British corner shop at night, shot like a haunting. About 15 s of picture, then an end card
("Based on true events. Coming to a shop near you."). The ghost is inflation: the price climbs 50p → £1 → £5 → £50 and
nobody is ever seen. **The point:** someone decides who gets the new money first (whoever is in the back room with
the printer), and you meet it last at the till. **The force is never seen: never a person, a face, a hand, a figure
or a shadow of one.** It shows only in what it does: doors, lights, prices, paper.

The music will be a slow, eerie horror track with hits on events, so motion should be sparse, slow and readable, with
one clear event per clip that a sound hit can land on. Each clip will be cut to about 2-4 s in the edit; the event
should happen within the first 4 seconds.

## The stills, in film order (look at each image)
1. `~/.cache/badcode/mf-anim/FO2-c.jpg` (0-2 s): the only lit corner shop on a dead terraced street at 3am, from across the wet road. (Its window card's text will be blurred in the edit.)
2. `~/.cache/badcode/mf-anim/PR2-e.jpg` (2-4 s): from inside the shop, the glass front door ajar onto the black street. Event: the door swings open by itself.
3. `~/.cache/badcode/mf-anim/PR2-c.jpg` (4-6 s): down the aisle, one tube dead, the stockroom door half open onto black.
4. `~/.cache/badcode/mf-anim/PR2-b.jpg` (6-10 s): one loaf on a bare shelf, label "50p". Event: the fluorescent tube flickers. The label's new prices (£1, £5) are added in the edit on the flicker frames, so the label itself must stay exactly as it is.
5. `~/.cache/badcode/mf-anim/FO2-d.jpg` (10-12 s): a convex security mirror; the aisle in it is empty, blank banknotes on the floor.
6. `~/.cache/badcode/mf-anim/FO2-e.jpg` (12-15 s): the doorway, "BREAD £50" on the glass, the stockroom door wide open at the back with cold light.

## Hard facts (from the makers and from what has failed before)
- **No dialogue, no voices, no people** in any clip. Sound from the video model is not used.
- **The camera stays locked** in every clip: any push, drift or zoom is added later in the editor, where it can be eased. Say so in each prompt.
- **Text must not change.** Video models redraw writing badly; every price label and sign must stay as it is in the still. All price changes happen in the edit.
- The look must stay as the still: a cheap colour-film night snapshot, grain, soft focus, teal fluorescent light. No glossy clean-up.
- Nothing falling or flying through the air in shot (these models render falls badly).
- Flashing/flicker: no more than 3 flashes a second.
- One continuous shot, no cuts (this model sometimes adds a cut of its own).
- No real brands, no real people. End every prompt with the word "Thanks."

## Your task
1. Research first: how Omni / Google Flow image-to-video behaves and how practitioners prompt it (start-frame
   fidelity, keeping text stable, locked camera, subtle motion); how horror films make an empty room feel occupied
   with tiny events (a door, a light, a draught); flicker as a scare device.
2. For EACH of the six stills write **two genuinely different** ways to animate it (options `a` and `b`): different
   events, not two wordings of one. 60-110 words per prompt.
3. Write JSON to `docs/stories/short-malevolent-force/scenes/malevolent-force/cleanroom/anim-r1.json` (path from
   `/home/jackt/projects/badcode/badcode`):
   `{"research": ["url — takeaway", ...], "notes": "...", "frames": [{"n": 1, "still": "FO2-c", "job": "what the shot does for the story, one line", "options": [{"id": "a", "label": "a few words", "idea": "one plain sentence", "event_at": "seconds where the hit lands, e.g. 1.5", "risk": "what might go wrong", "prompt": "the full motion prompt"}, {"id": "b", ...}]}, ... 6 frames]}`
