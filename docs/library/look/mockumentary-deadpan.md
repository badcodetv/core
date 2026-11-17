---
slug: mockumentary-deadpan
name: Mockumentary (deadpan fly-on-the-wall)
kind: look
family: Television and contemporary screen grammar
checked: 2026-10-28, references and engine notes (see Web check)
---

# Mockumentary (deadpan fly-on-the-wall)

> Handheld, naturalistic workplace or community footage where people talk straight to a camera that is supposedly documenting them.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Parodies the observational documentary: a crew follows ordinary people, catches awkward looks, and cuts to sit-down interviews. In the UK it was defined by the 2001 The Office, shot on video with fluorescent light and no score. It works through the gap between what people say to camera and what the frame shows them doing. Later strands (People Just Do Nothing, What We Do in the Shadows) add genre premises but keep the format.

## Signature traits

- Handheld camera with small reframes, occasional late focus pulls and slow digital zooms to catch a reaction
- Talking-head interviews: subject off-centre, looking just past lens, static background of real office or kitchen clutter
- Flat practical lighting: overhead fluorescent or window light, no motivated cinematic key, slightly clipped highlights
- The glance to camera: a held look straight into the lens after an absurd remark, 1-2 seconds
- No non-diegetic score; music only from radios, speakers, car stereos
- Cuts hold on awkward silence longer than a drama would
- Lower-third name captions and mundane job titles in plain sans type
- Soft video-grade 4:3 or 16:9 with muted greens and beiges

## References

- *The Office (UK)* — Ricky Gervais and Stephen Merchant (BBC), 2001. The reference for deadpan UK workplace mockumentary: fluorescent light, glances, no score.
- *This Is Spinal Tap* — Rob Reiner, 1984. The template for the feature-length fake documentary.
- *People Just Do Nothing* — Allan Mustafa, Steve Stamp (BBC), 2014. Working-class UK community mockumentary on camcorder-style footage. **(Corrected: Created and performed by Allan Mustafa, Steve Stamp, Asim Chaudhry and Hugo Chegwin. First series on BBC Three in 2014; it grew from earlier web shorts. Attributing it to Mustafa and Stamp alone is incomplete.)**
- *What We Do in the Shadows* — Jemaine Clement and Taika Waititi, 2014. Shows the format carrying a high-concept premise with deadpan confession interviews.

## What it carries

Awkward, funny, humane, quietly tragic. Carries cringe and small-scale cruelty well. Fights against spectacle, grandeur and anything that needs an omniscient camera.

## What it suits, and what it would undermine

Satire of managers, landlords, councils, boardrooms and quango people who reveal themselves by explaining themselves. Excellent for a 'minor functionary sincerely justifying the unjustifiable' story that lets a working-class viewer recognise their own workplace. Undermines epic, apocalyptic or future-dystopia scale, and risks laughing at the ordinary people in frame rather than at the decision-maker.

## Asking Flow (Nano Banana stills, Veo clips) for it

Describe it as plain observational footage rather than 'mockumentary': 'handheld documentary camera, fluorescent office lighting, subject seated off-centre glancing at camera, shallow clutter background, no music, 16:9, slightly soft video look'. Name the setting concretely (stained carpet tiles, laminated notices, kettle). Veo handles the glance and awkward pause reasonably and generates room tone, so ask for 'no score' and put 'awkward pause, holds look to lens' in the motion prompt. For Nano Banana stills, name the sit-down interview framing explicitly. Exclude/negative: cinematic teal-orange grade, anamorphic flare, dramatic rim light, orchestral score, shallow bokeh portrait look, beauty lighting.

## How generators get it wrong

Generators default to glossy cinematic portraits with beautiful lighting, which kills the format; fix by specifying fluorescent, flat, slightly ugly light and cluttered real rooms. Faces look too attractive and symmetrical; ask for ordinary, tired, specific faces and ages. The to-camera glance often becomes a smiling stare or the eyes drift; use short clips and re-roll. Fake lower-third text tends to garble in video; add captions in post, not in Veo. Character identity drifts across clips, which hurts a format built on recurring interviewees; use reference images.

## Production cost

Recurring interviewees need strong character consistency across many 8-second clips, and the humour depends on timing (the held beat) that Veo does not reliably hit, so you will re-roll or trim in the edit. Lip-sync dialogue is heavy; many films cheat with cutaways and voice-over. Moderate cost overall, because the camera is simple and locations are mundane.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Flow has no dedicated negative-prompt or Exclude field in its UI. Only the Veo API exposes a separate negativePrompt parameter, so in Flow the 'Exclude' items must be folded into the prompt as positive descriptions, such as 'flat fluorescent light' instead of 'no dramatic rim light'. Veo generates audio, so asking for no score or room tone is plausible.

Sources:
- <https://en.wikipedia.org/wiki/People_Just_Do_Nothing>
- <https://www.veo3ai.io/blog/veo-3-negative-prompts-guide-2026>
- <https://en.wikipedia.org/wiki/People_Just_Do_Nothing>
