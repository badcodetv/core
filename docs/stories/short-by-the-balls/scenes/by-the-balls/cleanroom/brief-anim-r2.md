# Brief: By the Balls, clips round 2 (and two new start stills)

You write prompts for Google Flow: Nano Banana 2.1 stills (9:16, edits of attached images) and Omni 1.2 Flash clips
(Frames mode: the clip starts on its still, 8 s, 9:16). Read ONLY this brief and look at the images it names (all in
this folder). Research freely how image-to-video prompts keep a scene still except for one moving object, and how to
frame a shot from inside a claw machine looking down.

## The director's notes on round 1, verbatim
- On the "claw goes limp" shot (round 1's clips started from `start-LIMP.jpg`; frames of one in `r1clip-LIMPa.jpg`):
  "stuff keeps falling out of the machine, make sure only the mini house moves also have the people still be there,
  maybe do a close up of the house falling, mayube from the claws perspective if that is possible thanks"
- On the unlock shot (clips from `start-UNLOCK.jpg`; frames of one in `r1clip-UNLOCKa.jpg`: the dial's face changed into
  a different gauge mid-clip, and in the other take it turned into a safe lock): "fix this, thanks"
- On the win shot (clips from `start-WIN.jpg`; frames of one in `r1clip-WINb.jpg`): "the lid falls after they take it
  just keep the lid out not much moves keep it simple, fix it thanks"

## Facts that hold in every shot
- Inside the claw machine: only small model houses and money (coins, banknotes); the prize is the small white two-storey
  house with a red roof. In the limp shots ONLY that house moves: the pile, the coins, the other houses and the machine
  stay exactly where they are.
- The couple are `CAST-HER.jpg` and `CAST-HIM.jpg`; the masked arcade worker is `CAST-BADCODE-2.jpg` (never describe their
  looks, only what they do). His mask keeps facing the way it faces in the still.
- Sound in every clip: effects and room tone only, never speech, singing, laughter or voices.
- No readable text, logos or brand names anywhere.

## What to write
1. Two NEW start stills (edits), ids `LIMPPOV` and `LIMPWIDE`:
   - `LIMPPOV`: looking straight down from just above the claw inside the glass (the claw's point of view): the open
     prongs at the top edge of the frame, the white house just released and falling towards the pile of houses and coins
     below. Edit from `start-GRAB.jpg` (the same claw, house and pile).
   - `LIMPWIDE`: the couple at the machine as in `start-PLAY.jpg`, the claw now near the top of the glass with its prongs
     slack and the white house dropping from them; both of them watching it. Edit from `start-PLAY.jpg` with the two portraits.
2. Clips, two takes each (ids `<SHOT>a`, `<SHOT>b`): `LIMPPOV` (the house falls away from the camera onto the pile;
   only the house moves), `LIMPWIDE` (the house falls back onto the pile; only the house moves and the couple's faces
   fall a little; nothing else in the machine moves), `UNLOCK` (from `start-UNLOCK.jpg`: he finishes swinging the steel
   cover open; the dial behind stays exactly the same dial, face and needle unchanged, and nothing else changes),
   `WIN` (from `start-WIN.jpg`: they lift the house a little and smile; the prize hatch's flap stays open the whole time;
   very little moves).

## Rules
- Camera locked or a very slight push-in. Under ~110 words each. Clips end with one "Sound:" sentence. Describe what
  moves and what stays; never name the thing to leave out. No sign-off.

## Output
Write `anim-r2.json` in this folder: {"stills": [{"id", "prompt", "attach": []}], "clips": [{"id", "still", "motion"}]}
(`still` = the start still's id: LIMPPOV, LIMPWIDE, UNLOCK or WIN). Reply with one line.
