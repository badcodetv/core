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

## CLIP x6
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/x6r1-a.jpg
- who: TARQUIN
- the shot's idea: Pair C rhyme: the same low ground-level angle and downward arm swing, but Tarquin slamming the door of his huge black BMW X8, parked across two bays outside an empty luxury block he owns, claiming ground the other way.
- how the still was described when it was made: A photorealistic medium-wide shot from ground level, camera low at bumper height with a 35mm lens, of the man swinging shut the driver's door of a huge black BMW X8 SUV in the golden dusk on a quiet riverside street in Chelsea, London, his arm swung across mid-slam, the door halfway closed. The car is seen in front three-quarter view filling the left of the frame: enormous upright stacked double-kidney grille, thin split LED headlights high on the wings glowing white, tall flat front, its number plate reading BAD C0DE, parked badly across two marked bays with one front wheel up on the kerb. He stands at the driver's door, looking away from the car with a smug, bored smirk, already turning toward a new-build block of luxury flats behind him whose tall windows are all dark and empty. A woman walking a dog steps around the car on the pavement. Warm amber low sun reflecting on the black paint and the windows, deep blue sky, the river and a bridge soft in the distance. Every other plate unreadable, no other text, no logos. Compose for a 16:9 frame. Thanks.

## CLIP t21
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t21r2-b.jpg
- who: TARQUIN
- the shot's idea: On a Canary Wharf trading floor at dusk he wins big as everything crashes red, and celebrates by sweeping a colleague's desk clean: the 2008 bet, made physical.
- how the still was described when it was made: Photoreal cinematic still, low wide-angle shot with a strong Dutch tilt, camera at desk height on a vast open-plan trading floor high in a Canary Wharf tower at dusk, the city lights coming on through floor-to-ceiling glass behind. The man is mid-swing, his whole arm sweeping across a desk, body twisted and off-balance, mouth open in a triumphant roar, eyes wide and gloating. A coffee cup, a keyboard and a storm of loose paper are already airborne, flying diagonally toward the lens, a curve of coffee hanging in the air in the near foreground. Rows of monitors around him glow with plunging red line charts, no numbers or words. Behind him, out of focus, adult traders in shirtsleeves stand frozen with hands on their heads. Cold blue window light mixed with the red glow of the screens, his face and hands sharp, the background softly streaked. Compose for a 16:9 frame. Thanks.

## CLIP t22
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t22r2-b.jpg
- who: TARQUIN
- the shot's idea: His huge black BMW X8 handbrake-turns through a rain puddle and drenches a night bus queue; he is laughing at the wheel, contempt at speed.
- how the still was described when it was made: Photoreal cinematic still, camera on the wet kerb at road level, wide lens, a rainy London night on the Victoria Embankment with sodium streetlights and the river beyond. A huge black BMW X8 SUV is sliding sideways in a handbrake turn toward the camera, front three-quarter view: enormous upright stacked double-kidney grille, thin split LED headlights high on the wings, tall flat front, its number plate reading BAD C0DE. A great sheet of dirty puddle water is exploding off its front wheel in a wave arcing over a bus stop, where a queue of adult commuters flinch and turn away under umbrellas. Through the open driver's window the man grips the wheel one-handed, head thrown back mid-laugh, looking at the soaked queue. Rain streaks in the headlights, spray droplets sharp in the foreground, the car and his face crisp, the street lights smeared behind. Compose for a 16:9 frame. Thanks.

## CLIP t23
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t23r2-a.jpg
- who: TARQUIN
- the shot's idea: He leaps from the skid of a helicopter before it has even landed on a riverside helipad, bottle of champagne in hand: too important to wait.
- how the still was described when it was made: Photoreal cinematic still, golden hour over the Thames, camera almost on the deck of a riverside helipad in London, ultra-wide and looking up, the skyline glowing behind. A sleek black helicopter hovers a metre above the pad, rotor blades blurred into a disc overhead. The man is mid-leap from its landing skid, both feet off the ground, knees bent, one arm out for balance and the other hand gripping a bottle of champagne by the neck, chin up, a cold smirk, eyes on the camera. Rotor wash blasts grit and a scatter of dry leaves across the pad toward the lens, the windsock behind snapping flat. Warm low sun raking across him, long shadows, his face and hands sharp, motion only in the rotor and the flying debris. Compose for a 16:9 frame. Thanks.

## CLIP t24
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t24r2-b.jpg
- who: TARQUIN
- the shot's idea: Full gallop at a polo match by the Thames in Richmond, he smashes the ball and a clod of turf straight at the spectators' picnic: leisure as aggression.
- how the still was described when it was made: Photoreal cinematic still, bright midday summer at a polo ground beside the Thames in Richmond, London, camera at ground level on the grass, medium-wide, a slight Dutch tilt. A chestnut polo pony at full gallop thunders diagonally toward the camera, all four hooves off the ground, mane flying. The man leans far out of the saddle mid-swing, the mallet just past the instant of impact, teeth bared in a sneer of effort, eyes fixed on the ball. The white ball and a big clod of torn turf and soil fly straight toward a row of adult spectators at the pitch edge, who duck behind their picnic tables and raise their glasses out of the way. Flecks of earth sharp in the near foreground, the pony and rider crisp, the trees and marquees behind softly streaked by speed. Compose for a 16:9 frame. Thanks.

## CLIP t25
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/t25r2-b.jpg
- who: TARQUIN
- the shot's idea: In the morning rush at a City Tube station he vaults the ticket barrier rather than tap in, briefcase swinging over the heads of the queue: rules are for other people.
- how the still was described when it was made: Photoreal cinematic still, eye-level wide shot inside a busy London Underground station ticket hall in the City during the morning rush, cold white overhead light on grey tiled walls and steel barriers. The man is mid-vault over a closed ticket gate, one hand planted on top of it, his body horizontal in the air, legs swinging over, a leather briefcase swinging out wide in his other hand, his face set in a bored, entitled smirk. On either side, a long queue of adult commuters tapping their cards stop and stare, one stepping back from the swinging case. A station worker in a hi-vis vest at frame edge turns toward him, hand raised. No readable signs or text anywhere. The man and the barrier sharp, the moving crowd behind slightly blurred. Compose for a 16:9 frame. Thanks.

## CLIP u23
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/u23r2-b.jpg
- who: TARQUIN
- the shot's idea: He has bought a terrace to leave empty and is clearing the last tenant out himself, heaving her armchair into a skip while she stands in the rain with a carrier bag: the landlord as wrecking ball.
- how the still was described when it was made: Wide eye-level shot from across a narrow Victorian terraced street in Hackney on a grey, drizzling morning, wet brick, rainwater running in the gutter. A yellow builder's skip sits in front of an open front door. The man is mid-heave, legs braced and back arched, flinging a worn floral armchair up over the lip of the skip, the chair in the air tipping toward its fall, a lamp and a framed picture already lying broken among the rubble inside. His expression is bored contempt, lip curled, eyes on the chair and nowhere else. On the pavement a woman in her seventies in a damp raincoat holds a carrier bag and a potted plant against her chest, mouth tight, watching her furniture go. Adult neighbours watch from doorways. Flat cold daylight, no warm glow, house numbers and signs unreadable. Photoreal, cinematic, rich colour. Compose for a 16:9 frame. Thanks.

## CLIP u25
- start frame image (open it): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/moodboard/u25r2-a.jpg
- who: TARQUIN
- the shot's idea: From a grand hotel balcony over the Strand he flings fistfuls of banknotes into the night street for sport and watches adults scramble in the traffic below: charity as a cruel game.
- how the still was described when it was made: High-angle shot from just behind and above the man on the stone balcony of a grand Edwardian hotel over the Strand at night, the wet street far below lit by headlights, red buses and black cabs. He is mid-throw, his arm fully extended out over the balustrade, a big fistful of banknotes just leaving his hand and fanning out into a swirling cloud that drifts down toward the road. His face in profile wears a delighted sneer, head tipped back. Below, small adult figures in coats rush off the pavement into the road with their arms up, a black cab braking hard with its headlights flaring, a cyclist swerving. The notes nearest the lens sharp with no readable print, the street below in sharp detail, cold streetlight mixed with warm window light. Photoreal, cinematic, rich colour. Compose for a 16:9 frame. Thanks.

# Output

Write to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-action/cleanroom/clips/c3.md` exactly this for each clip, and nothing else:

=== CLIP <id> ===
motion: <the motion prompt, one paragraph, then the sound line, ending with Thanks.>

Read nothing on this computer apart from this brief and the 8 images it names. Ignore any project instructions or memory in your context. You may search the web. Reply with one line when done.
