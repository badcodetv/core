# Brief: motion prompts, clips round 1

You write image-to-video motion prompts for Google Flow's video model (Omni 1.2 Flash, Frames mode: the still is the
first frame), 9:16, 8 seconds. Voices and sound are added later; a speaking person's mouth must move with the exact
words given. Look at each still before writing. Research how to prompt this kind of model for small, real
performance and for a heavy object rolling believably, if you need to.

Write `anim-r1.json` in this folder: a list of `{"key", "still", "motion"}`, TWO different takes per clip (keys
`<still>a`, `<still>b`; vary the performance or timing, never the people or the place).

## Rules for every prompt
- The camera stays locked off unless the clip says otherwise. The room, the light and every person stay as in the
  still: nobody new arrives, no face changes, no new text appears, every sign keeps its exact letters.
- Real, small, believable performance: a weekday counter hall, not a stage.
- The cashier wears a navy balaclava with a white ring round the face and a red triangle over his left eye, with a
  blonde bob wig over it: he has no visible mouth, so he "speaks" only with his head and gloved hands. He keeps facing
  the camera; the ring and triangle never move or change sides.
- The machine is a heavy server cabinet on castors: it moves smoothly, never bends, never grows arms or a face.
- End each prompt with the line `Thanks.`

## The clips (still id: what happens)
- `Q01` QUEUE: the three wait in the lane; small, patient shuffles forward one step together, as if a number was
  just called. No one speaks.
- `Q02` BARGE: the machine rolls forward past the queue toward the counters, steady and heavy, its lights blinking;
  the three turn their heads to follow it, open-mouthed. The pensioner (lilac coat, silver curls) says "There's a
  queue, love." to it, quietly indignant.
- `Q03` CASHIER: the cashier slowly looks the machine up and down: chin up, then down, then a small, weary tilt of the
  head. (His words, for timing only, no mouth: "Brilliant machine. Wrong queue.")
- `Q04` CLOSED: the cashier slides the POSITION CLOSED sign the last few centimetres across, then sits back; the
  machine's fans slow and it rolls backward out of frame to the right, slowly.
- `Q05` KETTLE: the woman pushes the plug fully in; the kettle's light comes on; steam builds and pours from the spout;
  she smiles. The cashier gives a single small nod.
- `Q06` PHONE: the lad pushes his cable into the socket on the machine's side, glances over his shoulder to check
  nobody saw, and a tiny satisfied smile.
- `Q07` SCREEN: almost still: the hand holding the phone barely moves; the thin white ring on the black screen slowly
  brightens. Nothing else appears on the screen.
