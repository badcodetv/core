# Crowd, vault and accent sweep — 2026-10-09

**Nothing here was tested by us.** Every item is reading. Web pass run after the director's notes on The Bank
Robbery cut 6: still "AI slop", props morphing, American accents on English characters, and the vault and the
riot scenes looking worst. It reports only what
[`2026-10-08-anti-slop-sweep.md`](./2026-10-08-anti-slop-sweep.md) and
[`2026-10-09-dialogue-and-morph-sweep.md`](./2026-10-09-dialogue-and-morph-sweep.md) do not already hold.

**Headline: the yield is thin.** For five of the six questions no source newer or better than the two earlier
sweeps was found. The one real change is in the Flow image picker (§5). Most of the usable tactics below are
inferences, and are marked as such.

Read first: both sweeps in full; headings of `omni-flash.md` and `nano-banana-2.md`; `nano-banana-2.md` §3 to
§3c (camera-angle templates, "name where the photographer stands"); `docs/flow/camera-vocabulary.md` tiers.

## Tiers

- **VERIFIED-PRIMARY**: a Google page fetched today, quoted, with URL. Pages were read through a summarising
  fetch tool, so quotes are as that tool returned them. Re-open the page before building a hard rule on wording.
- **PRACTITIONER**: a named non-Google source with URL. Most sell a competing tool.
- **UNVERIFIED**: inferred by me, seen only in a search summary, or measured on a different model.

## 1. Crowds, protest and riot

No Google page mentions crowds. The Omni API page, the Flow help page and the Runware Omni prompting guide were
all checked today and say nothing on crowds, background people, smoke, fire or sign text.

- **PRACTITIONER** One head-to-head (RuntimeWire, Omni 1.1 Flash image-to-video against LTX-2.3) reports Omni
  gave a convincing **overhead** crowd with pedestrians moving independently and stable geometry, where LTX
  ghosted and warped. One judged test set, read through a search summary only.
  <https://runtimewire.com/article/head-to-head-gemini-omni-flash-1-1-image-to-video-vs-ltx-2-3-22b>
  - **UNVERIFIED** reading: the crowd shot Omni is reported to hold is the high one, where a person is a
    head and shoulders and legs are hidden by the bodies behind. That lines up with the 10-08 note on broken
    legs in background extras, and with Jack's request for high and strange angles. A high corner view of the
    riot is the cheapest thing to try.
- **PRACTITIONER** invideo FAQ (updated 2026-08-01, no model named): "AI video models infer every detail you
  don't specify — and background characters are almost never specified"; "extras are pure inference". Its
  advice: add one dedicated line giving the extras' **period, class and emotional state**, and state era,
  geography and social situation, because geography "sets faces, signage, and architecture".
  <https://invideo.io/faq/why-do-ai-video-tools-generate-more-accurate-background/>
  - **UNVERIFIED** reading for the still: one sentence such as "the crowd are ordinary people from an English
    town in 2026, in work coats and anoraks, cold, tired and angry" in the Nano Banana prompt, in place of a
    headcount.
- **UNVERIFIED** (LTX blog, page would not load; search summary only; written about LTX, not Omni) The model
  cannot count extras, so name a precise location and a density word ("sparse", "packed") and do not give a
  number; a moving camera over a busy crowd smears faces, so pick one. <https://ltx.io/blog/crowd-scene-generation>
  - Agrees with our hybrid method (Veo/Omni camera locked, Premiere moves it). Nothing to change.
- **UNVERIFIED** (veo3gen blog titles and search summary, Veo 3.1) A named failure is the start frame's small
  background people freezing while the subject moves; its fix is a "motion contract" of one mover, one action,
  one camera, plus an explicit statement of what stays still.
  <https://www.veo3gen.app/blog/why-imagetovideo-freezes-the-wrong-90-and-animates-the-wrong-thing-a-creator-tro>
- **Placards:** nothing new. The 10-08 sweep already holds "small print degrades into gibberish as soon as the
  lighting moves" and the house rule is to composite sign text in post (`scripts/camping-mv2/signtext.py`).
  **UNVERIFIED** inference: generate riot stills with **blank** cardboard placards angled to the lens and add
  the words afterwards, so there is no lettering for Omni to mutate.
- **Smoke and flares:** nothing found. Our own rain and fluid notes in `omni-flash.md` remain the best evidence.

## 2. The vault: dark interior, steel, deposit boxes, stacked banknotes

**No source addresses this for Nano Banana or Omni.** Three searches returned generic "how to spot AI images"
pages. What they say, all **PRACTITIONER** and none model-specific or dated to the last three months:

- Generators "lose count or change size across a row"; real repeated objects hold their spacing. Cloned handles,
  latches, labels and dents across units are a tell, and so is repetition that is too perfect.
  <https://isitai.com/how-to-spot-ai-generated-images>
- Reflections are "overly simplistic" and do not correspond to the light source. Real photos get messier as you
  zoom in; generated ones get smoother. <https://caniphish.com/blog/how-to-spot-ai-images>
- Numbers and labels on doors are a weak point (letters that almost read).
- One prompt-gallery banknote prompt asks for material, not design: "matte cotton-fiber paper" and engraved
  intaglio lines and guilloche patterns. <https://prompts.oomol.com/p/20-yuan-banknote-guilin-landscape-edition-bc6bddab>

**UNVERIFIED** tactics inferred from those tells and from findings already in the repo (none tested):

1. **Shrink the grid.** A wall of two hundred identical deposit boxes is a counting-and-spacing test the model
   fails. Frame so that six to twelve boxes are in the picture, at an angle, with the rest lost in the dark.
   One open drawer, one bent door, one missing number plate break the cloning.
2. **Do not show a banknote face.** The 10-08 sweep already records that undefined lettering gets invented
   (our dollar-bill observation). Show money as **banded bricks seen edge-on**, shrink-wrapped pallets, or
   notes face down, so the frame holds paper edges and paper bands and no printed design. Bands are plain.
3. **Break the stack.** Uneven heights, one brick fallen, one torn wrapper, a pallet half emptied. Describe the
   stack as a thing with a history, not as "stacks of cash".
4. **One torch, and say what it hits.** A single torch beam landing on one named surface gives the "one small
   region deliberately brighter" that `docs/cinematography/` asks for, and leaves most of the steel in the dark
   where a wrong reflection cannot be read. Brushed or scuffed steel, not mirror-polished: a mirror surface is
   a reflection test.
5. **Keep numbers out or make them few and large.** Three box numbers near the lens, quoted in the prompt.
6. **In the clip, the torch should not sweep.** The 10-08 sweep holds "small print degrades into gibberish as
   soon as the lighting moves"; a moving beam re-lights every box and every note. Fix the torch on a surface
   and move a person through it.

Realistic currency may also be filtered. Nano Banana's policy on banknote images was not confirmed either way.

## 3. English accent

Nothing found that beats the 10-09 dialogue sweep. What is new is small.

- **VERIFIED-PRIMARY** Flow help, re-fetched today, unchanged: "You can add voice references only to video
  generations that use ingredients." and "For all other kinds of generations, you'll get an error." Voice is a
  "single-speaker voice reference", called in the prompt by typing `@Voice`. The page still does not say
  whether a **Character's** attached voice applies in Frames. <https://support.google.com/flow/answer/16894016?hl=en>
- **VERIFIED-PRIMARY** Omni API page: "English (EN) is fully supported, but other languages have not been
  evaluated". Accents and speaker count are not mentioned anywhere on the page. "Uploading audio references is
  unsupported in the current version of the API." <https://ai.google.dev/gemini-api/docs/omni>
- **PRACTITIONER** (Google AI developer forum, 2026-08-28, one user, Flow **Avatar** mode, not Characters) A
  face that rendered correctly with the wrong voice was fixed by putting the voice instruction **first** in the
  prompt: "@me, use my voice, do not use any other voices". No Google reply; the user says the bug stayed open.
  <https://discuss.ai.google.dev/t/google-flow-avatar/179475>
  - **UNVERIFIED** reading: in Ingredients, open the prompt with the voice call ("`@Voice` speaks every line.
    Use this voice only.") before any scene description.
- **PRACTITIONER** (same forum, 2026-09-11) A reply in the voice-drift regression thread (already cited
  in the 10-09 sweep) says the `@voice` tag was found by asking the Flow agent what prompt it had used, that
  chaining each clip from the last frame of the one before "works fairly well" for voice, and that he could
  **not get a tuned custom voice to save** in Flow. One user. Worth knowing if a Voice Performance edit appears
  not to stick. <https://discuss.ai.google.dev/t/critical-regression-gemini-omni-1-1-flash-update-destroyed-conversational-voice-continuity-for-ugc-creators/182433>
- **PRACTITIONER** (Veo 3.x two-character guide, already cited in the 10-09 sweep) "voice follows character
  description"; its template has an accent field with the options "neutral American" and "British / regional".
  <https://www.veo3ai.io/blog/veo-3-two-character-dialogue-guide-2026>
  - **UNVERIFIED** reading: American is the model's unmarked default, so an accent has to be stated every clip.
- **PRACTITIONER** Runware, re-read: name the accent in the same sentence that quotes the line, "so the words
  arrive as written rather than improvised". Already in the 10-09 sweep.
- **UNVERIFIED** inference, mine, from the 10-09 anecdote that the accent follows the picture: put English
  evidence in the **frame** of a talking clip (a UK three-pin socket, a mug of tea, a pub, a UK plate), and
  write the line with British words ("mate", "quid", "bloody") and British spellings.
- **Not found:** any test of regional labels (Estuary, Yorkshire, Scouse) against "British" on Omni or Veo; any
  statement that Character voices work in Frames; anything new on two speakers.

## 4. Object permanence and morphing

Nothing new of substance. No Google page addresses it.

- **PRACTITIONER** fal's Omni 1.1 guide (2026-09-06): on image-to-video, "name the parts of the still that must
  survive"; the model "has no way of knowing which parts of your frame were expensive to get right". Same
  advice as the Atlas Cloud and Runware items already filed. <https://fal.ai/learn/tools/how-to-use-gemini-omni-flash-1-1>
- **PRACTITIONER** fal, same page, on a pinned end frame: "Naming both ends of a move fixes the destination and
  leaves the middle negotiable." This is the opposite emphasis to our never-pin-an-end-frame rule; see §7.
- **PRACTITIONER** MindStudio hands-on (2026-08-29): failure "was concentrated in the character animation and
  object permanence" (a head detached mid-animation) while backgrounds held; its only workaround is cheap 360p
  drafts and retries. <https://www.mindstudio.ai/blog/gemini-omni-1-1-flash-video-model>
- **UNVERIFIED** inference, mine: every source places the failure on the articulated thing in motion, and our
  own cut-5 observation places it at the main action. So for a prop that must survive, the clip's action should
  belong to something else (a head turn, a line, a look) while the prop rests on a surface. Cut the prop's own
  action (the flip, the lift) as a separate, shorter insert, where a morph can be trimmed.

## 5. Changes in Flow in the last week

- **VERIFIED-PRIMARY** Gemini API changelog, fetched today: the only image or video entry since 25 September is
  the 6 October Nano Banana 2.1 release already in the 10-08 sweep. The 8 October entry is a Deep Research
  deprecation. **No Omni or Veo entry.** <https://ai.google.dev/gemini-api/docs/changelog>
- **VERIFIED-PRIMARY** Flow credits page: its table lists only video models and upscaling. **No image model has
  a published credit cost**, and the page does not call image generation free. Omni Flash 720p is 7 / 10 / 12 /
  15 credits for 4 / 6 / 8 / 10 s; 360p is 4 / 5 / 6 / 7; editing a video is 40.
  <https://support.google.com/flow/answer/16526234?hl=en>
- **PRACTITIONER** aifreeapi (published 6 October, updated 8 October): Flow "no longer lists Nano Banana 2".
  The picker is said to hold **Nano Banana 2.1** as the standard model, **Nano Banana 2 Lite** as the no-charge
  default, and **Nano Banana Pro** as the default for Ultra. "Credit cost per 2.1 image isn't published." It
  says to read the cost in the prompt-box settings before generating. <https://www.aifreeapi.com/en/posts/nano-banana-2-1>
- **PRACTITIONER** OrcaRouter (6 October): screenshots of 5 October show the picker as Pro, 2 Lite and 2.1; one
  user saw zero credits taken for a 2.1 image, which the article says shows that account's plan and nothing
  more. <https://www.orcarouter.ai/blog/nano-banana-2-1-google-flow>
- **UNVERIFIED and in conflict:** aifreeapi says Flow's help page lists those three models. The Flow help page I
  fetched today (answer 16894016) still says "By default, Google Flow sets the model to Nano Banana Pro" and
  does not mention 2.1. Either a different help page carries the list or the claim is wrong.
- 🔴 **What this means for the standing rule "always Nano Banana 2, it is free"** (UNVERIFIED until someone looks
  at the picker): the entry named Nano Banana 2 may be gone. If so the choice is 2.1 at an unknown credit cost
  or 2 Lite at none, and 2 Lite is a weaker model (Google's API page: "Not optimized for multiple reference
  inputs or multi-turn sequential editing"). The Flow tool passes a model name, so a missing "Nano Banana 2"
  entry may also break or silently redirect the runner. **Open the picker and read the credit line by hand.**

## 6. Strange camera angles in Nano Banana

`nano-banana-2.md` §3 and §3c and `camera-vocabulary.md` already hold the working templates. New:

- **PRACTITIONER** Segmind six-shot test (2026-04-12, **Nano Banana Pro**, not 2 or 2.1), prompts opening with
  a `CAMERA ANGLE:` line:
  <https://blog.segmind.com/camera-angle-generation-test-seedream-5-lite-vs-nano-banana-pro-across-6-shot-types/>
  - Obeyed: "Camera positioned at knee height, looking steeply upward"; extreme close-up; over-the-shoulder
    "just behind the character's right shoulder" (the most consistent of the six).
  - **Under-delivered: "Dutch angle (camera tilted 35 degrees)"**. The tilt came out "more subtle than a true
    35-degree Dutch angle".
  - **Under-delivered: "Overhead bird's-eye view, directly above looking straight down"**. "A true 90-degree
    vertical top-down was not achieved"; it gave a high angle.
  - Its conclusion: spatial rotations "are interpreted rather than executed"; "the issue is execution precision
    at the extremes".
- **VERIFIED-PRIMARY** Google's image-generation page gives one angle wording in its photoreal example: "Shot
  from a low perspective with a wide-angle lens." Nothing on Dutch tilt, foreground occluders or high corners.
  <https://ai.google.dev/gemini-api/docs/image-generation>
- **PRACTITIONER** (search summary; the page returned 403) A Nano Banana Pro angle guide orders the camera
  clause as angle, lens and distance, camera height, then focus, and puts it **first** in the prompt, ahead of
  style. <https://sider.ai/en/blog/ai-image/advanced-camera-angle-prompts-for-nano-banana-pro>
- **Not found:** any source on a CCTV or high-corner view, or on shooting through a foreground object, for any
  Nano Banana version.

**UNVERIFIED** wordings built from the above and from §3c (none tested):

- Floor: "The camera lies on the vault floor, lens two centimetres above the concrete, looking steeply up at …
  The floor fills the bottom third of the frame, out of focus."
- High corner: "The camera is fixed where the ceiling meets two walls, looking down across the whole room. The
  people are small and seen from above and behind." A place, not the word "CCTV", which may summon a timestamp
  overlay and video noise.
- Through an object: "The camera is inside the open deposit box, looking out. The dark edges of the box frame
  the picture on all four sides." Name the object the camera is in or behind.
- Tilt: since a stated degree is under-delivered, describe the result ("the door frame leans hard to one side;
  the floor line runs from the bottom corner to halfway up the opposite edge") or tilt in Premiere, which is
  exact.
- True top-down is unreliable; ask for a steep high angle and accept it.

## 7. Contradicts the two existing sweeps or the repo

| # | We hold | Source says | Tier | Proposed handling |
| --- | --- | --- | --- | --- |
| 1 | 10-08 sweep §2.1: unknown whether Flow shows 2.1; the picker held Pro, NB2 and NB2 Lite on 2026-09-30 | Flow no longer lists Nano Banana 2; picker is Pro, 2 Lite, 2.1 | PRACTITIONER, two sites | Look at the picker. The standing rule names a model that may not be there |
| 2 | 10-08 sweep: reports say 2.1 "costs credits in Flow" (apidog) | No cost is published; one user saw zero credits; 2 Lite is the no-charge one | PRACTITIONER, conflicting | Unresolved. Read the credit line |
| 3 | `camera-vocabulary.md` Tier 1 "dependable": Dutch angle, bird's-eye | Dutch tilt and true top-down were both under-delivered on Nano Banana Pro | PRACTITIONER, one test, older model | Do not demote on one test. Check the tilt and the top-down in the first still of each |
| 4 | Never pin an end frame, it morphs (hybrid method; 10-09 sweep §1) | fal: naming both ends "fixes the destination and leaves the middle negotiable" | PRACTITIONER, vendor | No change. "Negotiable middle" is where our morphs were observed |
| 5 | 10-08 sweep: Hedra's rule to keep unspecified signage out of frame | (agrees) invideo: unspecified extras and signage are filled from generic priors | PRACTITIONER | Not a contradiction; a second source |

## 8. Checked and not found

- Any Google statement on crowds, smoke, flares, dark interiors, banknotes or object permanence.
- Any Omni update since 1.1 Flash (2026-08-27), in the changelog or on the Omni API page.
- A Flow release-notes page for October 2026; a blog.google post for Nano Banana 2.1.
- Any test of accent labels on Omni; any account of Character voices in Frames.
- Reddit was not searched directly, and no Reddit thread came back in any result.

## 9. Cheap tests this suggests (none run)

1. Open the Flow image picker; note the entries and the credit line for each.
2. Riot still from a high corner against the same scene at eye level, same prompt otherwise; animate both.
3. Vault still with banded bricks edge-on against one that shows note faces.
4. One Ingredients talking clip with the voice call as the first sentence against the same clip with it last.
5. A still asked for "tilted 35 degrees" against one that describes where the floor line runs.
