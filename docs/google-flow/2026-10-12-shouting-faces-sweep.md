# Shouting faces sweep — 2026-10-12

**Nothing here was tested by us.** Every item is reading. Web pass run before five one-second protest inserts
for The Bank Robbery (red scarves against blue across steel barriers, dusk, chest-up). It reports only what the
[10-08](./2026-10-08-anti-slop-sweep.md), [10-09 crowd](./2026-10-09-crowd-vault-accent-sweep.md) and
[10-09 dialogue](./2026-10-09-dialogue-and-morph-sweep.md) sweeps and the README's shot table do not hold.

**Headline: the yield is thin, and for question 2 it is close to nothing.** Ten searches and ten page
fetches found **no source, Google or otherwise, that tests a shouting or open-mouthed face on Nano Banana, Omni
or Veo.** No source confirms that low motion or using only the first second is a known workaround. What exists
is generic "why AI faces look fake" vendor advice, written for smiles and portraits, with no model named.
Most of the usable tactics in §4 are my inferences from that and from our own records, and are marked so.

**Tiers:** **VERIFIED-PRIMARY** is a Google page fetched today (read through a summarising tool, so re-open it
before ruling on exact wording). **PRACTITIONER** is a named non-Google source; all of them sell a tool and none
shows a test method. **UNVERIFIED** is my inference, a search summary only, or a different model.

## 1. Stills: mouths, teeth, skin, symmetry, extras

- **PRACTITIONER** MagicShot, "12 tells" (2026-08-06, no model named, no method shown):
  <https://magicshot.ai/blog/why-your-ai-images-still-look-fake-12-tells-and-how-to-kill-them>
  - Teeth come out "all identical, all the same blinding white". Its wording: "natural teeth, slightly
    off-white, subtle gaps". It also says to "favor a closed-mouth or soft smile when you can", which is the
    opposite of our shot.
  - Skin "looks like a mannequin dipped in wax". Wordings: "visible skin pores", "slight blemishes", "matte
    finish". (Pores and texture are already in `nano-banana-2.md`; "matte finish" is the new word.)
  - "Real faces are subtly lopsided." Wording: "natural facial asymmetry".
  - A dead-centre neutral gaze "reads as a doll"; give the subject somewhere to look, and a mid-action state
    ("mid-laugh"). Hands are "a numbers game": make more candidates than usual.
- **PRACTITIONER** CapCut (2026-06-05, no model named): <https://capcut.com/create/ai-generated-faces-realism-bias-artifacts>
  - Mouth faults it lists: "too many teeth, uneven gum lines, stretched smiles, blurred lip edges".
  - "a neutral or lightly expressive mouth is often safer than a wide smile".
  - Describe a job and a place, not a look: "A mid-career accountant reviewing receipts in a small office".
  - Before animating: "avoid images where teeth, lips, and jawline are already ambiguous."
- **PRACTITIONER** ZSky (2026-03-22, reviewed 2026-04-17; titled "8 Tested Methods" but shows no test):
  <https://zsky.ai/blog/fix-ai-image-faces-2026.html>
  - "Neutral and slight smile expressions generate most reliably because they are the most common in training
    data." Read plainly: **a shout is off the model's common ground, so expect a lower hit rate.**
  - "Multiple faces in a single image compound the difficulty. The AI may merge features between faces or
    create inconsistent lighting across different faces."
- **UNVERIFIED** (search summaries only) Generators draw teeth "as a texture", so the row is too regular; Nano
  Banana gallery prompts give the mouth its own clause, but only closed ("lips gently closed, relaxed").
- **Not found:** any wording for a shout, a strained neck or a pointing hand; anything on identical extras
  beyond the 10-08 anchor-figure item and the 10-09 invideo item.

## 2. Video: holding a shouting face for one to three seconds

- **VERIFIED-PRIMARY** The Omni API page says nothing about faces, mouths or expressions from a start image.
  The nearest lines are in its meta-prompt: "Be very specific about the people, items and objects in the scene"
  and "Consider micro-detail, expression and timing". The last 6,000 characters of the page were not read.
  <https://ai.google.dev/gemini-api/docs/omni>
- **PRACTITIONER** invideo review (2026-06-04, Omni **1.0**, talking avatars, not image-to-video):
  "Lip sync holds steady for 6-7 seconds, before drifting"; Omni is "still not ready for a big-screen
  close-up"; "Motion occasionally drops from fluid animation into a choppy 8 to 12 fps look".
  <https://invideo.io/blog/gemini-omni-flash-review/>
  - Reading, **UNVERIFIED**: mouth trouble is reported late in a clip, not early. That fits our own cut-5
    record (10-09 sweep: first second clean in all seven morphing clips). It is not evidence about a shout.
- **PRACTITIONER** (Google AI developer forum, 2025-12, **Veo 3.1**, a dental clinic's before-and-after clips,
  no fix offered by anyone) Even with reference images and first and last frames, Veo "changes the geometry and
  looks of the teath during camera moves"; the poster saw the same on other vendors' models.
  <https://discuss.ai.google.dev/t/veo-3-1-consistency-help-preventing-hallucinations-in-professional-dental-workflow-gemini-2-5-veo-pipeline/111898>
  - Reading, **UNVERIFIED**: the one report that names teeth names a **camera move** as the trigger. That
    agrees with the hybrid method (camera locked in the generator, moved in Premiere).
- **UNVERIFIED** (search summary, LTX 2.3 close-up workflow, a different model) Start from a sharp, evenly lit
  still and "avoid occlusion over the mouth". <https://www.runcomfy.com/comfyui-workflows/ltx-2-3-close-up-shots-in-comfyui-audio-and-2x-upscale>
- **Not found:** any test of an open-mouth start frame against a closed one; any statement that less motion
  keeps teeth stable, or that trimming to the first second or two is standard practice for faces.

## 3. Flow guidance on Frames and Ingredients: no change found

- **VERIFIED-PRIMARY** Flow help (answer 16894016), re-fetched today, reads as it did on 10-09. Frames: "create
  transitions, animate images, or generate a video that starts and ends with specific images." Ingredients:
  location and style references should not hold "extra subjects, unless that is your creative intent". Voice:
  "only to video generations that use ingredients". Still says "By default, Google Flow sets the model to Nano
  Banana Pro" and still does not mention 2.1. No advice on faces, motion amount or clip length. The page shows
  no revision date, so "unchanged" means "same sentences as we quoted before".
  <https://support.google.com/flow/answer/16894016?hl=en>
- **VERIFIED-PRIMARY** Gemini API changelog: no Omni or Veo entry since Omni 1.1 Flash (2026-08-27). The newest
  image entry is still the 6 October Nano Banana 2.1 release. <https://ai.google.dev/gemini-api/docs/changelog>
  - Same page, 8 October: "gemini-3.5-flash is deprecated and has been replaced by gemini-3.6-flash" (see §5).
- **Not found:** a Flow release-notes page or a blog.google post for October 2026. Search results stop at the
  27 August Omni 1.1 post. The 10-09 open question (is "Nano Banana 2" still in the picker) is still open.

## 4. What this suggests for the five inserts (all UNVERIFIED inferences, none tested)

1. **Two or three faces a frame, not a row.** One face sharp and nearest the lens, one behind it soft, the rest
   scarves and shoulders. ZSky's merged-features warning plus the 10-08 anchor-figure item.
2. **Cast each sharp face by job and age, not by look** ("a roofer in his fifties", "a care worker in her
   thirties"), one clause each, and give the two faces different ages. CapCut's wording.
3. **Give the mouth its own clause, about the teeth:** "mouth wide open mid-shout, lower teeth showing, teeth
   slightly off-white and uneven". MagicShot's teeth wording moved onto a shout. Untested on any model.
4. **One skin clause:** "matte skin, visible pores, cold-reddened cheeks and nose". No "perfect", no "detailed".
5. **Ask for a lopsided face** ("natural facial asymmetry", or describe it: one eye narrower, jaw pushed to one
   side) and **pick the least symmetric candidate**. ZSky says pick the most symmetric; that is the slop route.
6. **Eyes on a target in the frame** ("glaring across the barrier at the man opposite"), never at the lens.
7. **Hands:** the README table already says a hand prop on a surface fails. A pointing arm that crosses the
   mouth is occlusion (10-09 sweep and the LTX note). Keep the pointing hand low or at the frame edge.
8. **Expect a low hit rate on shouts and budget for it:** more candidates a still than usual, and reject on the
   mouth first. A still whose teeth or lip edge are unclear is not animated (CapCut).
9. **The still already shows the shout at its peak** (README: continue a state, do not reach one). The clip
   prompt asks for the shout to carry on, one hold-still sentence, "No camera movement.", and crowd noise with
   no words.
10. **Cut from the first second.** Our own cut-5 record and invideo's late-drift report point the same way. No
    source confirms it for faces. Check at four frames a second or more before trusting it.
11. **For a one-second insert, the still alone may do:** a slow Premiere push-in on the frozen shout has no
    mouth to morph. Whether a frozen face reads as a photograph among moving clips is the director's call.

## 5. Contradicts the repo or the earlier sweeps

| # | We hold | Source says | Tier | Proposed handling |
| --- | --- | --- | --- | --- |
| 1 | The shot needs open, shouting mouths | Closed or lightly expressive mouths are safer (MagicShot, CapCut, ZSky) | PRACTITIONER | Keep the shot. Mix in one or two clenched-jaw or mid-breath faces so not all five depend on teeth |
| 2 | 10-09 crowd sweep §5: the 8 October changelog entry is a Deep Research deprecation | Same date also deprecates gemini-3.5-flash and 3.7-flash | VERIFIED-PRIMARY | Not a Flow matter. Check the listening tool's model string |

## 6. Cheap tests this suggests (none run)

1. One protest still with the teeth clause against the same prompt without it, four candidates each.
2. One shouting still animated as "keeps shouting" and as "holds the shout, barely moving", sheeted at four
   frames a second; note the first frame where the teeth change.
