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

## CLIP b25
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b25r2-b.jpg
- who: BOB
- the shot's idea: He gathers thrown-out cardboard behind a closing market and lunges as the wind tears a sheet away. Scavenging his bed for the night is hard, unglamorous work.
- how the still was described when it was made: Photoreal cinematic still, long telephoto shot from across a narrow street, early winter evening behind Borough Market in London under the railway viaducts. Traders are hosing down stalls and stacking crates in the cold white work lights. The man has a stack of flattened cardboard boxes clamped under one arm, and he lunges sideways with his free hand outstretched as a gust whips the top sheet away. The sheet is in mid-air just beyond his fingertips and his coat-tail swings with the motion. His brow is lowered, his mouth is closed in a hard line, and his breath streams in the cold. Wet cobbles shine under the arches, a train is a blurred streak of lit windows on the viaduct above, and the traders in the background are busy and do not look. Compressed, layered depth in cold white and deep brick red. Compose for a 16:9 frame. Thanks.

## CLIP b26
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/b26r2-a.jpg
- who: BOB
- the shot's idea: At 1am the steel gate of a Tube entrance comes down on the last warm place in the city, and he slams a hand flat against it. Shut out, angry and proud.
- how the still was described when it was made: Photoreal cinematic still, low wide-angle shot from inside a London Underground station entrance looking out to the street, 1am in winter. A steel lattice gate is sliding shut across the stairway. The man stands on the top step outside it, his palm slammed flat against the cold bars at the moment of contact, his shoulder driving into it and his fingers spread. His jaw is clenched, his nostrils flared, and his eyes are red-rimmed and lock straight through the bars into the warm light behind the camera. On the inside, a staff member's gloved hand pulls the gate along at the edge of frame. Behind him the street is wet and black under a single sodium lamp, and a night bus streaks past as a blur of red. Warm tiled light inside, cold dark outside, his face and hand sharp. Compose for a 16:9 frame. Thanks.

## CLIP t2
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t2r1-a.jpg
- who: TARQUIN
- the shot's idea: Speed: at night he throws a private speedboat full throttle down the Thames past Tower Bridge, spray flying, a man who has never been told to slow down.
- how the still was described when it was made: A photorealistic wide shot at night from a low angle just above the water, 24mm lens, of a sleek dark private speedboat racing down the River Thames in London toward camera, Tower Bridge lit up behind it and the glowing glass towers of the City on the bank. The man stands at the wheel, one hand shoving the chrome throttle lever forward, the bow just starting to lift out of the water, a white fan of spray beginning at the hull; his face is exhilarated, mouth open in a laugh, wind pushing at him. A river police launch with a blue light is small and far behind, and adults on the riverside path turn to look. Black water broken into gold and white reflections of the bridge lights, a few drops of spray on the lens. Sharp boat and man, the water and lights giving the speed, open river ahead of the bow. No readable text or logos on the boat. Compose for a 16:9 frame. Thanks.

## CLIP t3
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t3r1-a.jpg
- who: TARQUIN
- the shot's idea: Property: on the steps of an empty white stucco terrace he owns, he tosses a fat ring of house keys in the air like loose change, every window behind him dark.
- how the still was described when it was made: A photorealistic full-figure shot at eye level from across the street, 85mm lens, of the man standing on the black-and-white tiled steps of a grand white stucco Georgian terrace house in Belgravia, London, at golden hour. He has just flicked a heavy ring of dozens of brass house keys up into the air with one hand, the keys at the top of their rise, his other hand open and ready to catch them without looking, a lazy smirk on his face. The whole terrace behind him is empty: every tall window dark, shutters half-closed, no curtains, a dry dead plant in a window box, a tidy row of the same empty houses running down the street. Warm low sun raking across the cream columns, long shadows, a couple of adult passers-by on the pavement in soft focus, one glancing up at the dark windows. Sharp subject, natural colour, no estate agent boards, no readable text. Compose for a 16:9 frame. Thanks.

## CLIP t4
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t4r1-a.jpg
- who: TARQUIN
- the shot's idea: Ownership of space: early misty morning on Rotten Row in Hyde Park, he kicks a big chestnut horse into a gallop, scattering joggers off the track that was never his alone.
- how the still was described when it was made: A photorealistic medium-wide shot at eye level from the side of the track, 200mm telephoto lens, of the man riding a large glossy chestnut horse along the sand riding track of Rotten Row in Hyde Park, London, in thin early-morning mist. He is leaning forward in the saddle, heels just driving into the horse's flanks, reins short, the horse gathering itself in the first stride of a gallop with one foreleg lifted and sand kicking up; his face is fierce and pleased, chin up. Two adult joggers on the edge of the track have stepped smartly back onto the grass, one with hands raised. Tall plane trees in rows, pale low sun burning through the mist, dew on the grass, the distant rooftops of Knightsbridge faint beyond the park. Sharp rider and horse, mist and joggers softer, open track ahead for the gallop. No readable text or logos. Compose for a 16:9 frame. Thanks.

## CLIP t6
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t6r1-a.jpg
- who: TARQUIN
- the shot's idea: Money with no cost: at a crowded London property auction he lazily lifts his paddle to outbid a young couple, without looking up from his phone.
- how the still was described when it was made: A photorealistic medium close-up, 135mm telephoto lens, shot from the back of a packed London property auction room in a grand hotel ballroom on a weekday afternoon, looking between the shoulders of seated bidders. The man sits in the middle of a row, slouched, scrolling his phone with one hand while the other lifts a plain white bidding paddle lazily into the air, the paddle halfway up, his face not even turning toward the auctioneer's rostrum. In the row in front of him a young adult couple turn back to look at him, the woman's own paddle sinking, dismay on their faces. Chandeliers and tall curtained windows, rows of gilt chairs, adult bidders holding catalogues, an auctioneer far off in soft focus with a raised gavel. Soft warm interior light mixed with grey afternoon daylight from the windows, shallow depth of field, the man and the couple sharp. Blank paddles and catalogues, no readable text or screens. Compose for a 16:9 frame. Thanks.

## CLIP x2
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/x2r1-c.jpg
- who: TARQUIN
- the shot's idea: Pair A rhyme: the same side-on pour, but it is a decanter of very old French red into an oversized crystal glass at a lunchtime table under Leadenhall Market's painted roof, the excess doing the talking.
- how the still was described when it was made: A photorealistic close-up of the man seated at a white-clothed table under the ornate painted Victorian roof of Leadenhall Market in the City of London at lunchtime, tilting a heavy crystal decanter to pour deep red wine into an absurdly large bowl-shaped glass held up in his other hand, the dark ribbon of wine just leaving the lip of the decanter. He watches the pour with a satisfied, slightly bored smirk, little finger raised. Shot side-on at chest height with a 50mm lens, decanter and glass sharp in the left third of the frame, room to the right. Behind him, softly out of focus, the cream and maroon ironwork arcades, warm hanging lamps, busy office workers in suits eating at other tables and a waiter in a long white apron waiting at his shoulder, ignored. Warm golden midday light falling through the glass roof, rich colour, a crumb and a ring of wine on the tablecloth. No readable text, no logos. Compose for a 16:9 frame. Thanks.

## CLIP x4
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/x4r1-a.jpg
- who: TARQUIN
- the shot's idea: Pair B rhyme: the same low pavement-level stride toward the left, but Tarquin cutting across Bank junction in the morning rush, coat flaring, phone held away from his ear while he barks, treating the whole City as his corridor.
- how the still was described when it was made: A photorealistic wide shot from pavement level with a 24mm lens of the man striding across the busy crossroads at Bank junction in the City of London in the bright morning rush, mid-stride with his front heel just landing, a long tailored overcoat flaring open behind him, one hand holding a phone slightly away from his ear as if mid-shout, the other arm swinging a slim leather document case. His expression is a sneering, impatient half-laugh, eyes fixed ahead past the camera. He is in the right third of the frame walking toward the left, with space ahead of him. Behind him the columned facade of the Royal Exchange and the old stone bank buildings, a tower of glass rising above, a crowd of office workers parting around him, a cyclist braking, a red bus waiting. Crisp low sunlight raking across the stone, long shadows, cold clear blue sky. Subject sharp, a slight motion blur on the crowd. No readable text, no logos. Compose for a 16:9 frame. Thanks.

# Output

Write to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-action/cleanroom/clips/c2.md` exactly this for each clip, and nothing else:

=== CLIP <id> ===
motion: <the motion prompt, one paragraph, then the sound line, ending with Thanks.>

Read nothing on this computer apart from this brief and the 8 images it names. Ignore any project instructions or memory in your context. You may search the web. Reply with one line when done.
