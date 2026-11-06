# Image-to-video for fast physical action: Omni 1.1 Flash and Veo 3.x (web research, 2026-11-06)

Web-only clean-room research. Tags: [vendor] = Google's own docs/blog; [tested] = someone ran it and showed results;
[reported] = third-party guide, forum or reseller claim; [inference] = my reasoning, not a finding.

## Answer
1. In image-to-video, the prompt describes **only what changes**: one action, the camera, what the environment does, and the sound. Don't re-describe the still [reported, LTX, fal].
2. Slow motion is the default failure. Cut it with **force/contact physics words** (weight, impact, momentum, planted feet, recoil) and **one** explicit "real-time speed" line. Avoid any wording that suggests drift [reported].
3. Use **one action per 8 s**, with timed beats (`[00:00-00:02] …`). Google documents this for Veo 3.1, and it likely transfers to Omni [vendor for Veo; inference for Omni].
4. For hard action (horse legs, water, debris, hands on objects), **lock or simplify the camera** and let the subject move. Fast camera moves over busy backgrounds are what warp faces and geometry [reported].
5. For audio, write separate sound sentences naming the actual SFX and ambience. Google advises listing exclusions as plain nouns, not "no/don't" [vendor]. Expect music to leak in anyway, so plan to mute it or replace it in the edit [reported].
6. Omni-specific prompting docs are thin. Google's 1.1 post (27 Aug 2026) covers features (keyframes, 10 s-context extension, 360p drafts, 4K), not action craft. **I found nothing Omni-specific dated Nov 2026** [vendor].

## 1. Writing the motion prompt
- **Describe the change, not the frame.** "The prompt in image to video mode describes the motion, camera behavior, and audio. You do not need to re-describe everything visible" [reported] https://ltx.studio/blog/veo-prompt-guide
- **Components, in order.** Google's Veo formula is subject, action, style, plus optional camera, composition, focus, ambiance [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide . Omni guides use subject → action → camera → look → sound, written "as direction to a crew rather than descriptions of a finished frame" [reported] https://fal.ai/learn/tools/how-to-use-gemini-omni-flash-1-1 , https://www.atlabs.ai/blog/ultimate-gemini-omni-flash-prompting-guide-2026
- **Timing beats.** Veo 3.1 officially supports timestamp prompting: `[00:00-00:02] … [00:02-00:04] … SFX: …` [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
  For 174 BPM cuts where only ~1-2 s is used, put the peak of the action (impact, splash, slam) in the **first 2-3 s**. Don't spend the opening on a wind-up [inference].
- **Don't overfill the clip.** Too much change in too little time reads as rushed or garbled. Use the 8 s setting, or split the action and chain the pieces [reported] https://ltx.studio/blog/veo-prompt-guide . Single-action prompts beat multi-action ones [reported].
- **Why things go floaty.** "AI video models default to slow motion because gradual frame-to-frame changes are easier to maintain consistently" [reported] (LTX, "how to fix slow motion", https://ltx.io/blog/how-to-fix-slow-motion-in-ai-generated-video , fetch failed and quoted from the search excerpt).
- **Physics beats time words.** Creators report that "real-time speed" gets drowned out in long prompts and advise "Stop using 'Time' words, start using 'Physics' words" [reported, Reddit r/generativeAI "action shots are always slow-mo"].
  Words that add weight: *momentum, weight, impact, inertia, recoil, braced, planted, snaps, slams, jolts, shudders* [reported] https://obsidian-pub-9uo.pages.dev/en/blog/ai-video/prompt-terms/speed-physics
- **Ready-made weight patches** [reported] https://www.imaginary.app/blog/ai-video-looks-great-but-feels-off-a-creators-checklist-to-fix-unreal-motion-wei :
  - "Feet make firm contact with the ground."
  - "The object has noticeable weight and inertia."
  - "Brief compression and rebound on landing."
  - "Hair and fabric lag slightly behind motion, then settle under gravity."
  - "Fingers wrap and grip; slight knuckle tension; object resists slightly before moving."
- **One explicit speed line is fine:** "shot in real time at normal speed", "filmed at standard speed" [reported, Reddit]. Never pair it with anything that implies slowness. "Slow-motion fast-paced action" is a contradiction that confuses the model [reported].
  Words that pull toward slow-mo: *gracefully, gently, floats, drifts, cinematic slow, epic, dreamlike, ethereal*. So does a "slow dolly" camera move [inference from the above].
- **Name the physics of the medium.** Omni guides say to name "the weight, the collision, or how a fluid should move" [reported] https://www.imagine.art/insights/gemini-omni-flash-prompts-guide . Reviewers list Omni as "strong on water, cloth, collisions" [reported, atlabs].
- **Verbs for this shoot** [inference]:
  - Rough sleeper: *hauls himself up, drops, splashes, stamps, flattens, lunges after, slams, hammers, trudges head-down*.
  - Trader: *guns the throttle, the hull slams the chop, the horse's hooves strike, swings through, leaps, vaults, sweeps, heaves, hurls, flings*.
  - Use concrete counts: "three hard stamps", "two hammer strikes".

## 2. Camera
- **With no stated move, Veo falls back to static or subtle handheld.** Put the move in its own sentence [reported] https://ltx.studio/blog/veo-prompt-guide . Omni guides suggest a 3-8-word camera clause at the end [reported, Framia].
- **Moves the docs name and the models recognise.** Static, pan, tilt, dolly, truck, pedestal, zoom, crane, aerial/drone, handheld, whip pan, arc [vendor, Vertex guide]. Omni examples add snap zoom, dolly zoom and 360 orbit [reported, fal].
  Google warns some advanced angles and lenses "aren't officially supported", so results may vary [vendor].
- **Lock vs move.** Fast camera moves over busy scenes magnify warping and identity drift [reported, atlabs + imaginary]. Omni consistency "can drift during big scene changes or fast camera moves" [reported, atlabs].
  Rule of thumb [inference]: for **complex bodies** (horse, polo, pull-ups, vault, helicopter jump), use a **locked or tracking-alongside** camera that matches the subject's speed, so relative motion stays low.
  For **simple shapes** (speedboat, car, skip), use a hard move: handheld chase, whip pan, snap zoom.
- **A locked camera can look like an ad.** "A locked-off frame reads as a tripod, and a tripod reads as an ad" [reported, fal]. For grit, try "handheld, slight shake, camera braced", not a full move [inference].
- **Naming both ends of a move** ("starts on the hooves, ends on his face") "fixes the destination and leaves the middle negotiable" [reported, fal].
- **Speed on screen.** For speed, use foreground parallax (barrier, railings, rain streaks, spray), not a faster camera. This is [inference], consistent with the above.

## 3. Identity, scene stability, expression
- **Image-to-video with a strong anchor frame is the main lever.** Pick a frame where the face is already correct, the pose is "animatable (not extreme)" and the background is simple [reported, imaginary]. Prefer a start frame **just before** the action peak, not mid-contortion [inference].
- **Name what must survive.** Fal's sample prompt: "Nothing about the mirror, the shelf or either light source should change from the still" [reported]. For this shoot, try "his face, clothes and the street stay exactly as in the image" [inference].
- **Lock identity with a reference.** Omni takes reference images (`keep the character from image_0`) and, since 1.1, ≤3 s video references for character consistency [vendor: blog.google 1.1 post; reported: fal/atlabs].
- **Big-movement words** (turn, rotate, twist, jump) raise face-warp risk [reported] https://www.vo3ai.com/blog/veo31-image-to-video-tutorial-from-photo-to-cinematic-animation . Turning heads away from camera is safer than turning towards it [inference].
- **Crowds** (bus queue, ticket hall): keep them small or soft. Put them in the **background, out of focus, not interacting**, and give them a single shared action ("the queue flinches back") [inference]. I found no sourced fix.
- **Keeping him unsmiling.** I found no Veo- or Omni-specific fix. Negative instructions ("don't smile") often backfire [reported, Reddit]. State the expression positively, and give the face a job [inference]:
  - "jaw clenched, eyes narrowed against the rain"
  - "breathing hard through his teeth"
  - "expression flat and set throughout"
- **Watch for spontaneous smiles.** These models tend to drift faces towards a smile [inference from general reports; unverified]. Check the last frames of every take.

## 4. Audio: SFX and ambience only
- **Google's guidance.** "use separate sentences in your prompt to describe the audio"; "Clearly specify if you want audio" [vendor, Vertex].
  Format: `SFX: thunder cracks in the distance`, `Ambient noise: …` [vendor] https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- **Negatives.** Google advises against "no"/"don't". List unwanted elements as plain terms instead, or describe the absence positively ("a desolate landscape with no buildings" rather than "no man-made structures") [vendor].
  Applied here [inference]:
  - A full, concrete soundscape: "SFX: rain hammering on tarp, boots splashing, gate clangs. Ambience: wet traffic hiss."
  - Then an exclusion line in plain terms: "Audio contains only these sound effects; silence between them" or "speech, music, singing, score" in a negative field if one exists.
- **"No music" leaks.** A r/VEO3 thread reports Veo 3.1 adding music despite "no music". A commenter suggests stating it in the main body and again in an Audio line. Unconfirmed [reported] https://www.imaginary.app/blog/veo3gen-audio-keeps-going-wrong-9-fixes-for-dialogue-sfx-timing-and-music-mix-as (originally veo3gen.app).
  Undescribed audio "leaves half the output to chance": the model fills gaps with dialogue or music [reported, atlabs, veo3gen].
- **Omni examples.** They include "no music," "no voice," "no dialogue," "No captions". Whether these are needed or just good practice is not stated [reported, fal].
  Google's own 1.1 post claims no audio feature at all [vendor], yet fal says "Picture and sound come out of one generation" [reported]. Check a take in Flow before relying on either.
- **Subtitles.** Any hint of speech can trigger burned-in subtitles [reported] https://yapper.so/articles/remove-veo3-subtitles . Keeping speech out of the prompt avoids it [inference].
- **Practical.** For a DnB edit, the clip audio is almost certainly replaced or ducked, so **music leakage is cheap to fix in the edit**. Burned-in captions and talking mouths are not [inference].

## 5. Action failure modes and mitigations
| Failure | Mitigation | Tag |
|---|---|---|
| Floaty / slow-mo | physics + contact words, one real-time line, short prompt, peak early | reported |
| Warping during fast moves | simpler background, camera tracks with subject, "keep background geometry stable" | reported (imaginary) |
| Horse legs | "close-up gallops are the weakest because fast four-leg cycling is where anatomy drifts". Go wide/silhouette or tight on hooves, mane, thrown turf | reported (Morphic, vendor marketing) https://morphic.com/resources/videos/horse-stock-footage |
| Hands / objects passing through bodies | the object already in hand in the still; grip/resistance words; one object only | reported (partial) + inference |
| Water / spray / debris | name the fluid behaviour ("a sheet of brown puddle water arcs over the queue and splatters"); Omni reportedly strong here | reported |
| Thrown objects (armchair, notes) | start with object in hands at the top of the swing; say where it lands ("crashes into the skip, splinters") | inference |
| Identity loss | reference image/video, no head-turn to camera, image-to-video anchor | reported |
| Cardboard/paper in wind | name the wind direction and gusts, "tumbles end over end along the pavement" | inference |
| Rushed garble | too much in 8 s: cut to one action or chain with first/last frame | reported (LTX) |
- **First + last frame** (Veo 3.1, and Omni 1.1 keyframes) pins both ends of a hard action. The middle is still negotiable. "Almost is worse than obviously different" for the end frame: edit the start still into the end still [vendor for feature; reported for tip, fal].
- **Draft cheaply first.** 360p drafts cost ~⅓ and run up to 60% faster in Omni 1.1 [vendor]. That only matters if drafts are allowed in this workflow.

## 6. Omni in Flow, what is actually known
- Omni Flash launched at I/O on 19-20 May 2026, in Gemini, Flow and Shorts. It takes text, image, audio and video in, and makes clips up to ~10 s [reported: Decrypt, SiliconANGLE].
- Omni 1.1 Flash was announced on **27 Aug 2026**. It adds:
  - keyframes (start + end frame)
  - extension using 10 s of prior context (steps of 10 s to 40 s)
  - 360p drafts
  - 1080p/4K
  - ≤3 s video references
  It is in Flow for AI Plus/Pro/Ultra [vendor] https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
- I found **no Google-published Omni prompting guide** with action, slow-mo or audio-negation advice. The Omni-specific tips above come from resellers (fal, atlabs, imagine.art, Framia), and none show controlled tests.
- **Nothing found specific to Omni in Flow in Nov 2026.** Fal mentions a "1.2" exists, with no details [reported, unverified].
- Veo 3.1 guidance (timestamps, SFX/Ambient lines, negative phrasing, camera vocabulary) is the best-documented proxy. It probably transfers because both models are Google's and sit in the same Flow UI, but that is [inference].
