# Clean-room sweep: Nano Banana 2.1 stills and Omni Flash clips (2026-10-29)

Bank Robbery's MV ALT cut ("The Speakeasy Mint"): 33 scenes, stills then clips, prompts written by sealed
writers from fresh web research (never the repo's prompts). Engine findings only; the look is the story's
(`docs/stories/bank-robbery/look.md`). Full record: `docs/stories/bank-robbery/songs/mv-speakeasy-mint-alt/picks.md`.

## The method

`[confirmed 2026-10-29]` Jack, on the round-2 stills: *"i love this new style … this unlocks so much more."*
After a round he called AI slop, this broke it in one go:

1. Fresh web-only research on the engine.
2. An honest list of what came back wrong last round.
3. Sealed writers, each reading one brief file.
4. Their prompts run verbatim.

The research the writers worked from, both web only and tiered inside:
- `songs/mv-speakeasy-mint-alt/cleanroom/nb21-research.md`: Nano Banana 2.1 stills.
- `songs/mv-speakeasy-mint-alt/cleanroom/omni-psych-research.md`: Omni or Veo clips that are psychedelic but filmed.

## Nano Banana 2.1 (stills)

- `[confirmed 2026-10-29]` These four counters cleared the slop look on 64 of 64 stills (one story, by eye):
  - Narrative prose with the details written in.
  - Dry ground instead of wet, mirror-gloss streets.
  - One motivated light.
  - A real object causing each strange colour (frost, a goldfish bowl, a decanter, a mirror ball).
- `[confirmed 2026-10-29]` NB 2.1 still paints a readable shop sign when a shop front is in frame: 2 of 4 takes of
  one prompt read "BAKERY", even though the prompt said the name was "illegible". Keep shop fronts out of frame, or
  turned away from the camera.

## Omni Flash (clips, Frames start image, 8 s, 2 takes, 16:9)

- `[vendor]` Omni cuts between shots unless told "single continuous shot, no scene cuts".
  - `[confirmed 2026-10-29]` 64 clips with that line: no cuts seen on a contact sheet.
  - The repeat-checker flags it as a habit phrase. It's deliberate.
- `[confirmed 2026-10-29]` **Policy blocks; what each one was, and the fix that passed.** Each block took effect on the first try.
  - **A tommy gun firing** ("spits flashes", "muzzle flash"), even pointed at the sky: blocked twice. Dropping the
    gun from the prompt passed, though the start frame still showed it. A gun held upright and not firing passed
    in two other clips.
  - **A young-looking face plus a mouth habit**: "red-haired lad … chewing his toothpick" was blocked twice. "Red-haired
    man in his twenties" passed. (`[untested]` whether "gangster" on its own mattered; a scene with "gangsters" passed.)
  - **"The slumped stoker stays still"** reads as a body: blocked. "Leans back, wiping his brow, breathing slowly" passed.
  - **A cigarette was not the trigger.** Scene 5 passed with the cigarette kept, once "gangster" became "man".
- `[confirmed 2026-10-29]` **`UPLOAD_REFUSED` follows the picture, not the project.** Three stills (all crowd or
  street scenes) were refused in every fresh project, and once after re-saving at 1280 wide. Other stills uploaded
  fine in between. The fix: use a different still.
- `[confirmed 2026-10-29]` **A project goes bad after about two video calls.** The two symptoms:
  - A save timeout (`locator.evaluate: Timeout 30000ms`).
  - Take b of the third call harvested as a byte-identical copy of the previous call's b (twice). Check with `md5sum`.
  - A block in the project makes the next call time out.
  - Fix: open a fresh project before every clip.
- `[confirmed 2026-10-29]` The first video call in a fresh project can fail with `VIDEO_OPTION_UNAVAILABLE: Frames on Omni 1.1 Flash`.
  It passes on an identical retry, with no credits spent.
