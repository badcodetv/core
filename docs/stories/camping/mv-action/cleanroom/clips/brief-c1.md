# The job

Write the MOTION prompt for each of the 8 clips below. Each clip is made in Google Flow with the image-to-video model Omni 1.1 Flash: the still is the first frame, your text says what happens over the next 8 seconds. The clips are cut fast (often 1.5 to 3 seconds of each is used) into a UK drum and bass music video (174 BPM) about inequality in London.

# What the director said, word for word

"ive picked the stills, please make the videos and put them in premiere in the new sequence. Please clean room it all and research the internet to achieve it."
Earlier, about these characters: "it presented bob as too happy in some of them, he leaves a bleak life it should refelect that. Tarquin is doing basically nothing so more action like action shots please."

# The two men

- BOB: a Liverpool man in his fifties sleeping rough in London. Bleak, cold, wet, tired, proud. Never smiling, never laughing; dignity, never pity.
- TARQUIN: a rich, posh, sneering City trader. Reckless, greedy, contemptuous. His clips must be ACTION: fast, physical, with impact.

# Hard rules

- The man in each still is a fixed character: NEVER describe his face, hair, age, build or clothes. Say only what he does, his expression, and what moves around him. Call him "the man".
- No speech, no singing, no music in the clip. Sound effects and ambience only (say which), on their own line. No readable text.
- One clear action per clip; the strongest moment early (first 2 to 3 seconds), then it continues or follows through for the rest of the 8 seconds. Real speed, not slow motion.
- Keep the place and everything in the still consistent: nothing morphs, no new people appear from nowhere, hands and faces stay intact.
- End every prompt with the word: Thanks.

# Web research (web only, 2026-11-06, on animating action stills)

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


# The clips

## CLIP b1
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b1r1-a.jpg
- who: BOB
- the shot's idea: Dawn at the free outdoor gym in an East London park, he hauls himself up on the pull-up bar before the city wakes: proud, stubborn, keeping himself strong when nobody is counting on him to.
- how the still was described when it was made: A photorealistic wide shot from ground level at the outdoor gym in Victoria Park, East London, at dawn, a 24mm lens low in the frosty grass looking up. The man hangs from a green steel pull-up bar, mid-pull with his elbows bending hard and his chin rising toward the bar, teeth gritted, eyes fixed upward with a fierce, proud look, breath steaming in the cold. Behind him the park lies in pale pink mist, bare plane trees, a lake catching the first light and the distant towers of the City and Canary Wharf on the skyline; low sun rakes sideways and lights his outline. A couple of adult joggers in the background pass along the path, slightly soft, while he stays sharp. Dew on the rubber matting, a scuffed bench in the foreground, open sky above the bar for him to rise into. Compose for a 16:9 frame. Thanks.

## CLIP b2
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b2r1-a.jpg
- who: BOB
- the shot's idea: Nine in the morning at a day-centre washroom, he throws cold water in his face to start the day: the plain discipline of keeping himself decent.
- how the still was described when it was made: A photorealistic medium close-up at eye level in a worn day-centre washroom in south London, morning, a 50mm lens. The man leans over a chipped white ceramic sink, both cupped hands full of cold water rising toward his face, eyes squeezed half shut, mouth tight, bracing for the shock. Hard cool light from a frosted window on the left, a scratched steel mirror above the sink catching a sliver of his shoulder, green tiles with cracked grout, a folded thin towel waiting on the edge. Water drips from his fingers in sharp beads. Behind him, out of focus, another adult waits by the door with a towel over his arm. Natural, slightly flat colour with the warmth only on his skin. Compose for a 16:9 frame. Thanks.

## CLIP b6
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b6r1-b.jpg
- who: BOB
- the shot's idea: Two in the morning in a shuttered Strand doorway, he strikes a match to light a tiny camping stove for tea: resourceful, making a home out of nothing while the city's feet pass.
- how the still was described when it was made: A photorealistic close-up from ground level in a shop doorway on the Strand at two in the morning, a 40mm lens resting almost on the pavement. The man crouches over a small camping gas stove with a dented steel kettle on it, one hand cupped around a match he has just struck, the flame flaring bright and the blue ring of the burner about to catch, his face lit warm from below, concentrating, a small satisfied twist at the corner of his mouth. A rolled-down metal shutter behind him, a flattened cardboard mat and a folded blanket beside him. Out of focus in the foreground, the legs and shoes of late-night adult passers-by on wet pavement, red and white streaks of a passing night bus beyond. Cold blue street light against the warm match light. Compose for a 16:9 frame. Thanks.

## CLIP x3
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/x3r1-a.jpg
- who: BOB
- the shot's idea: Pair B, the stride: Bob hauling his whole life, tent rolled on his back and a bulging bag in his fist, across Waterloo Bridge into the rain after being moved on, head up, defiant.
- how the still was described when it was made: A photorealistic wide shot from pavement level with a 24mm lens of the man striding fast across Waterloo Bridge in London on a wet late afternoon, mid-stride with his front heel just landing, a rolled tent strapped across his back and a heavy bulging holdall dragged in one hand, the other arm swinging. His jaw is set and his chin is up, a grim defiant grin, eyes fixed ahead past the camera. He is in the right third of the frame walking toward the left, with space ahead of him. Behind him the long grey bridge, red buses and black cabs passing in the spray, commuters under umbrellas hurrying the other way, and the river with the towers of the City soft in the mist on the skyline. Grey-blue light, rain streaking, puddles on the pavement reflecting tail-lights, a few drops on the lens. Subject sharp, background traffic with a slight motion blur. No readable text, no logos. Compose for a 16:9 frame. Thanks.

## CLIP x5
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/x5r1-b.jpg
- who: BOB
- the shot's idea: Pair C, the claim of ground: Bob on one knee at night, swinging his shoe down to hammer a tent peg into a verge at the edge of the car park in a gusty wind, fixing his home in place with his own hands.
- how the still was described when it was made: A photorealistic medium shot from ground level, camera low on the wet tarmac with a 35mm lens, of the man kneeling on one knee at the edge of a London supermarket car park at night, his arm raised high and swinging down with a worn boot held by the toe like a hammer, about to strike a metal tent peg pushed into a strip of muddy grass. His other hand grips the taut guy line, the small dome tent beside him bellying in the wind. His face is screwed up in fierce, comic determination, tongue between his teeth. He fills the left half of the frame. Behind him, out of focus, the bright glass front of a closed supermarket glowing white, empty parking bays under tall orange lamps, a lone night shopper pushing a trolley to a car, wind blowing leaves and a crisp packet across the tarmac. Night palette of sodium orange and cold white, rain-slick ground reflecting the lamps. No readable text, no logos. Compose for a 16:9 frame. Thanks.

## CLIP b22
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b22r2-a.jpg
- who: BOB
- the shot's idea: Moved on before dawn, he swings his rolled bedding onto his shoulder while a guard's torch holds him. He is ignored by day and evicted by night, and he leaves with his head up.
- how the still was described when it was made: Photoreal cinematic still, eye-level medium shot at blue hour before dawn on the stone forecourt outside King's Cross station in London. The man is mid-swing, heaving a tightly rolled bundle of blankets and a tarp up onto his right shoulder, his body twisting with the weight and one foot already stepping away. A security guard's torch beam cuts in from the left edge of frame and lands across his chest, and the guard is only a hi-vis shoulder and an arm at the frame's edge. The man's brow is lowered, his jaw tight, his lips pressed thin, and his eyes are fixed straight ahead past the guard. Early commuters with wheeled cases cross the cold blue background under the station's arched brickwork, which is lit a flat white. Cold steel-blue and white light, a still and dignified composition. Compose for a 16:9 frame. Thanks.

## CLIP b23
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b23r2-b.jpg
- who: BOB
- the shot's idea: Rain floods his tent in the supermarket car park and he bails it out with a cut-down bottle. This is home, and home is a puddle under floodlights.
- how the still was described when it was made: Photoreal cinematic still, side-on medium-wide shot with the camera at tent height, dusk in heavy rain in a floodlit London supermarket car park. The man crouches half inside the open flap of a small sagging dome tent, his arm flung outward at the peak of a scoop as he throws a sheet of muddy water out of a cut-down plastic bottle. The water arcs through the air, lit hard white by the floodlights. Rain hammers the flysheet and bounces off the tarmac, and a pool of water has spread under the groundsheet. His face is wet and grey, his eyes narrowed against the rain, his jaw set and his mouth closed. Parked cars sit in rows behind him, blurred with their headlights on, and shoppers hurry to their cars under umbrellas without looking over. Hard white floodlight and wet black tarmac. Compose for a 16:9 frame. Thanks.

## CLIP b24
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b24r2-b.jpg
- who: BOB
- the shot's idea: A bench built so he cannot lie on it, so he stamps a sheet of cardboard flat on the ground beside it. Defensive architecture, met with stubborn practicality.
- how the still was described when it was made: Photoreal cinematic still, low wide-angle shot from knee height, a grey overcast winter morning on the South Bank in London under bare plane trees, the river a dull pewter colour behind. Beside a sleek stone bench divided by metal armrests, the man brings his boot down hard onto a folded sheet of damp cardboard to flatten it on the paving. The stamping foot is a hand's width from impact, his weight dropping onto it and his arms out for balance. A puff of grit and water has already lifted from the stones. His jaw is tight, his eyes are dark-ringed and fixed on the cardboard, and his cheeks are windburnt. Joggers and office workers pass along the river walk behind him, soft in the distance. Flat, cold grey daylight, muted and desaturated, the bench's armrests catching the light in the foreground. Compose for a 16:9 frame. Thanks.

# Output

Write to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-action/cleanroom/clips/c1.md` exactly this for each clip, and nothing else:

=== CLIP <id> ===
motion: <the motion prompt, one paragraph, then the sound line, ending with Thanks.>

Read nothing on this computer apart from this brief and the 8 images it names. Ignore any project instructions or memory in your context. You may search the web. Reply with one line when done.
