# The Den

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A short (9:16, about 20 s): a parody of a TV investors' pitch show. A smooth government minister asks for £2bn to take
every teenager round a prison and "scare them straight"; asked how he'll know it works, he has "a good feeling", and
every investor is out. A nervous nurse pitches one ward for six months with the number that would prove her wrong;
BadCode is in. The point: no policy without its test. It ends on the evidence: Scared Straight-type programmes were
tested, and the Cochrane and Campbell reviews found they increased offending.

## Look
Jack, 2026-11-22: "use unsplash" and "dragons den warehouse set please". Real-looking photographs of a TV pitch
show's set: a dark converted warehouse loft, exposed brick, tall industrial windows, wooden floor, a row of leather
armchairs for the investors with stacks of cash on the side tables, the pitcher's mark in the middle, an iron staircase
the pitchers come up. The feel of that kind of show, never its name, its logo, the word "Dragons", or its theme music.
Reference (Jack, 2026-11-22: "use actaul dragons den images as reference images, and use unsplash to match the images"):
the real set's empty photos (the set designer's portfolio, no people) in the media folder's `reference/show-set/`
(private: never in git, never published, never given to Flow); each is matched with an Unsplash photo, and the
Unsplash pick is what Flow gets. The real photos may go to the sealed writer to describe the layout.
Status: EXPLORING (stills not made). Flow project: `c9bd669c-40b7-4009-b17c-24f38362ad89` ("Nov 22 - 16:03"). Stills Nano Banana 2.1, 9:16.

## Cast (all invented)
- **The panel (LOCKED, Jack 2026-11-22)**, reference stills in the media folder's `cast/`:
  - **Investor A** `INV-A-a`: early sixties, Black British, grey crop, half-moon glasses on a chain, burgundy skirt suit, gold bangle; oxblood armchair.
  - **Investor B** `INV-B-b`: late forties, British Indian, neat beard, slicked hair greying, navy three-piece, pocket square; black bentwood armchair.
  - **Investor C** `INV-C-b`: about seventy, white, bald with a white fringe, ruddy, mustard cardigan, checked shirt, knitted tie; brown leather armchair.
  - **Investor D** `INV-D-a`: mid thirties, British Chinese, black bob with fringe, black polo-neck, silver rings, tablet; slim black armchair.
  - **BadCode** `BADCODE-fix2-c`: navy ribbed balaclava, charcoal suit, white shirt, dark tie, black gloves; brown leather armchair. Its triangle points down but sits upper-centre (Jack picked it as is).
  - All invented; never a lookalike of any real panel member. Round glass side tables on chrome frames with stacks of cash.
- **The minister**: invented; never a real politician's likeness, name or party.
- **The nurse**: invented; scrubs, a clipboard.

## Sound
Not decided: run story-style. Voices: every spoken line is an AI Studio voice, cast fresh with voice-casting
(narrator, minister, nurse, BadCode, investors). Any Suno track is music and sound effects only, workspace `short-the-den`.

## Story-only rules
- The script comes first; nothing is generated until Jack agrees it ([script.md](./script.md)). Lines are Claude's drafts until Jack or Kai rewrites them.
- The closing card is Jack's wording, sourced: Petrosino et al. 2013 (Cochrane CD002796 / Campbell 2013:5).
- The nurse's numbers (one ward, six months, a tenth) are the joke's, never shown as a statistic.
- 🔴 Parody only: our own title on release (to decide), no show name, logo, theme or real person's face.

## Library pieces in use
- **Real photo as the look**: find the layout on Unsplash (`python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>"`), give the picked photo to Flow as the reference; the prompt says what happens.
- **Clean room**: every prompt by a sealed writer (`clean-room-writer` agent) from a brief of raw facts and one look line; never earlier prompts.
- **The BadCode balaclava**: anyone in it is BadCode. Fixed: a large white ring round the whole face; ONE solid red triangle with rounded corners inside the ring at its upper right (the wearer's left eye), pointing down; no skin anywhere (gloves, cuffs over the wrists, collar over the neck); no robot features. Attach `docs/brand/balaclava/mask-reference.jpg` with `docs/brand/balaclava/shared-wording.txt` verbatim. In motion, write "his mask keeps facing the camera" and check the triangle zoomed in at three points per clip.

## Where the detail is
[README.md](./README.md) · [script.md](./script.md) · [look.md](./look.md) · [sound.md](./sound.md) · scene: [scenes/the-den/](./scenes/the-den/)
