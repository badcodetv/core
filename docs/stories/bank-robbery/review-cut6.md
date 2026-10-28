# The Bank Robbery — review of cut 6, and the plan for cut 7 (9 October 2026)

**Asked for by Jack, 9 October 2026,** after watching cut 6: "There are still american accents and ai artifacts/ai
slop, with objects morphing and changing and not looking realistic. Please change the platform to english. the
whole vault scene is a bit of a mess and looks like ai slop, along with the crowd riot/protest scenes, please redo
a lot of them. Watch and listen to it all first… make it as cinematic and to not look like ai made it as
possible, use the david lynch interesting camera angles, comedic timing… it doesnt have a film vibe, even if it
looks like a collection of comedy skits that tells the story, that would still be better, since it feels like
random ai footage at the moment. that being said we are getting somewhere."

**Ruled by Jack in that message:** The Platform is English.

## How it was reviewed

- **Picture:** the Premiere render `renders\bank robbery - cut 6-20261009-1036.mp4`, all 6:22, one frame a
  second on thirteen contact sheets, read by eye.
- **Sound:** the soundtrack in eight 48 s parts through the listening tool (Gemini 3.5 Flash, `voice` lens),
  every line logged with the accent it heard. Logs: `docs/listening/log/2026-10-09-124*-aud-0?.md`.
- 🔴 **Nobody heard it with human ears in this session.** A machine cannot settle accent
  (`docs/google-flow/2026-10-09-dialogue-and-morph-sweep.md` §4). The list below is what it flagged this time;
  Jack's ear outranks it.

## Why it reads as "random AI footage" (my diagnosis, not his words)

| # | What | Where | The cause |
| --- | --- | --- | --- |
| 1 | **One scene, three different worlds.** The riot is dusk with pink flare smoke; the shot after it is flat grey daylight; the door after that is white daylight | 3:17 to 4:33 | Each clip was made alone, so time of day and weather change at the cut. A viewer reads that as footage from different films |
| 2 | **The vault is three different vaults.** A corridor with a round door, a round door seen through a ring, a fluorescent room with shelves, then a hatch | 5:00 to 5:40 | No one reference for the place, and a different light in each |
| 3 | **Shots come round twice.** The hoover shot and the men's backs both play again inside the vault scene, under a narrator line they have nothing to do with | 5:24, 5:30 | Filler from cut 2, never replaced |
| 4 | **A frozen still in a moving scene** | 4:11 (the two protesters) | Flow refused the clip three times |
| 5 | **Two placards in the same handwriting** | 3:17 | One still |
| 6 | **Mouths that barely move on a line** | 5:06 ("Why am I drilling?") | Two speakers in one Frames clip |
| 7 | **Voices that change country between shots** | list below | Every talking clip was made in Frames mode, where a Character's saved voice is (per Google's help page) not used; the model invents one per clip |

`docs/cinematography/symptoms.md` has these as "it's a pile of nice shots, not a scene", "I'm lost, I don't know
where we are" and "it feels random". The fix for all three is the same: one place, one light and one time of day
a scene, one wide early, and every shot a step.

## Lines the listener called American this time

| Time | Line | Who |
| --- | --- | --- |
| 0:44 | "She should bloody well earn it." | Mr Blue |
| 1:43 | "The biggest vault in the city. Everyone's life savings, right there." | The Ex |
| 1:50 | "Security isn't a problem. I am the security. The problem is eyes." | The Governor, The Ex |
| 2:04 | "Hang on. Which one's true?" | Mr Red |
| 2:14 | "And how much do we take?" | The Donor |
| 2:22 | "You bastard." | The Donor |
| 2:57 | "The thing is, off the record, I agree with all of you." | The Presenter |
| 5:50 | "Who talked? He talked! You lot always talk!" (heard as a New York caricature) | Mr Blue, Mr Red |

It heard The Platform's line (2:07) as English this time; he is being changed to English anyway, on Jack's word.
Everything else was heard as London, Estuary or RP.

## The plan for cut 7

1. **Every flagged line is re-made in Ingredients mode with the speaker's Character attached** (so its saved
   English voice is used), **one speaker a clip**, the accent written into the speech clause. The one exception
   is the standoff, which needs both men shouting in one shot.
2. **The vault is re-shot as one skit in one place:** a master still of the vault (`s11-00-vault`, one builder's
   work lamp on the floor, nothing else lit) is attached to every vault still. No recycled shots.
3. **The riot stays at dusk from the first placard to the bank door.** One high wide early for the geography; the
   two protesters filming each other re-staged from above with the pallet passing between their phones; the
   Presenter and the door re-made in the riot's light.
4. **Kept on Jack's word:** the opening, the old eating walk (`s09-walk`), the guns still, the kebab shop.

Shot designs, prompts and results: [`stills-v7.md`](./stills-v7.md).
