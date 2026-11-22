# Brief: The Den, the clips, round 1 (common to every writer)

You write motion prompts for Google Flow's Omni 1.2 Flash video model in Frames mode: each clip starts on a still
(described below; the model sees it), 8 seconds, 9:16. Read ONLY this brief and `geometry.md` (same folder). Research
freely how a TV pitch show is shot and cut (describe in your own words; never name any show).

## How talking works (rules from testing this engine)
- A speaking clip carries the EXACT words, written as `He says: <words>` or `She says: <words>`, no quotation marks,
  nothing added. The mouth is animated to those words; the voice is replaced later, so the words must match exactly.
- Keep the face where it is in the still: same size, facing the same way, camera nearly still, so the mouth stays readable.
- A clip where nobody speaks ends its sound sentence with "no talking".
- Never end a prompt with any sign-off or thanks (the model speaks it).
- The masked investor (BadCode) wears a full balaclava: no mouth shows. Write "his mask keeps facing the camera, the white
  ring and the red triangle unchanged" in his clips. He never speaks on screen; his voice is laid over.
- Each prompt ends with one "Sound:" sentence (room tone of a big brick loft, a chair creak, a murmur; for speaking
  clips, the speaker's voice and the room).

## The clips (one prompt each; the story in order)
1. **STAIRS** (still: the minister halfway down the iron stairs, looking up from the floor, grinning): he walks down
   the last steps towards camera, confident, one hand trailing on the rail, and steps off onto the floorboards. No talking.
2. **MIN1** (still: the minister standing on the mark, medium shot, hands open, the staircase and brick behind):
   He says: Two billion pounds. Every teenager in the country, taken round a prison. Scare them straight.
   Big salesman's gestures, all teeth, eyes on the panel just off camera.
3. **BCASK** (still: the masked investor seated in his leather armchair, three-quarter angle, gloved hands on the arms):
   he tilts his head slightly and leans a few centimetres forward, perfectly calm, one gloved finger lifting off the
   chair arm. He does not speak on screen (no talking).
4. **MIN2** (same still as MIN1): his grin holds a beat too long, the smile freezes, then He says: I've got a good feeling.
   (with a small confident nod).
5. **INVA** (still: the woman in the burgundy suit, early sixties, arms folded, in her oxblood armchair): she looks at
   him over her half-moon glasses, unimpressed, and She says: I'm out.
6. **INVC** (still: the heavy-set older man in the mustard cardigan, leaning forward, hands on his knees): he sits back
   heavily and He says: I'm out.
7. **INVD** (still: the woman in the black polo-neck with a tablet on her knee, bored): she glances down at her tablet,
   then up, and She says: I'm out.
8. **NURSE** (still: the young nurse on the mark, clipboard held to her chest, the staircase and brick behind):
   nervous but steady, She says: One ward. Six months. If readmissions don't fall by a tenth, you stop paying me.
9. **BCIN** (same still as BCASK): a long still beat, then he leans slowly forward towards her, gloved hands together.
   No talking on screen.
10. **WIDE** (still: all five investors in their arc of armchairs, the factory windows glowing behind): a slow push in
    towards the panel; small natural movements (a glance, a leg uncrossed, a hand on a stack of cash); the masked one
    in the centre stays perfectly still. No talking.

## Rules for every prompt
- One paragraph, your own words, under ~120 words, describing only motion, camera and sound (the still already holds the look).
- Describe only what should happen; never name the thing to avoid.
- No readable text or logos appear.

## Output
Write `anim-r1.json` in this folder: a JSON array of {"id","still","motion"} with the ids above; "still" is the id's
start frame: STAIRS, MIN (for MIN1 and MIN2), BC (for BCASK and BCIN), INVA, INVC, INVD, NURSE, WIDE. Reply one line each.
