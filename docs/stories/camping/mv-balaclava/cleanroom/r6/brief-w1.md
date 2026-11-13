# The job

A UK rap music video. Two masked men rap straight to camera, one shot per lyric line. For each of your shots write TWO prompts:
1. a STILL prompt (Google Flow, Nano Banana 2 image model, 16:9, the character's reference image attached), which becomes the first frame;
2. a CLIP prompt (Google Flow image-to-video, the fast "Omni Flash" model, Frames mode: your still is the first frame; 8 seconds, 720p).
The editor uses 1 to 3 seconds of each clip, so the clip must be alive from its first second.

# What the director said about the last attempt, word for word

# Jack, 2026-11-07 (verbatim)

"so go back to the camping music video, please fix the rapping gesturing with the balacclava guy, he seems to float in the air, ai slop is present when he does anything. please redo it watch this "https://www.youtube.com/watch?v=8CdcCD5V-d8" eminem venom, to see how he does this, as in gesturing and rapping at the camera. please Please clean room it all and research the internet to achieve it. Thanks."


# The reference he points to (watched frame by frame; what the performer does)

# How the performer moves in the reference video (watched 2026-11-07, frames sampled at 1/2 s to 1/5 s)

The video cuts between a story (people on a night bus, in a hallway, a taxi, a street) and the rapper alone. Only the rapper's
shots are described here.

**Place and light.** An empty black stage in haze. One hard white light straight above and behind him (it shows in the frame as
a bright point at the top). A pool of light on a grey concrete floor; he casts a hard shadow on it. Nothing else in the frame.
He wears a black hoodie with the hood up, a chain, dark trousers. The colour is almost black and white.

**Wide shots (feet in frame).** He stays on one spot. Wide stance, feet past shoulder width, knees bent, weight low and forward,
shoulders hunched. The feet stay put; the movement is in the knees (a small bounce), the hips (a slight sway or turn) and the
arms. When he travels it is one or two side steps or a turn on the spot, never a walk at the lens. His shadow stays joined to
his feet.

**Medium and close shots (most of his time).** Framed waist up or chest up, often from slightly below, and the camera sometimes
pushes in or drifts. He leans in to the lens from the waist, head forward and down, hood shadowing his face.
- One hand does the work; the other hangs or holds the hoodie.
- The gestures are SHORT and close to his body, from the elbow and wrist, cut off hard on the beat: a finger tapping or pressing
  his temple; a hand clawed in front of his face, then thrown down; a fist pumping downward at waist height; fingers pointing
  down and flicking; a flat palm chopping sideways at chest height; a hand pulling at the hood.
- Between gestures his hands come back to rest near his chest or mouth; he never holds a pose like a presenter.
- His head bobs with the beat and his shoulders roll; his whole upper body rocks forward on stressed words.
- No microphone. He raps straight into the lens with total eye contact.

**What it is NOT.** No big open-armed sweeps, no jazz hands, no jumping, no squatting low and springing up, no strutting at the
camera, no outstretched pointing held for a beat. Energy comes from tension and rhythm (tight, coiled, aggressive), not from size.

**Close shots, looked at again (171 s).** The camera is handheld and very close (a wide lens, an arm's length away), swinging with
him; he ducks his head and throws a fist or a hand past the lens so fast it smears with motion blur. The hood and his face go in
and out of shadow as he dips under the top light. A hand clawing at the hood, both fists up by the face like a boxer's guard.

Frame sheets (local reference only, not for publishing): `<media>/reference/venom/` (media = `songs\camping vid\balaclava`).

Frame sheets of the reference (open and look at all three): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/venom/venom-36s-wide.jpg, /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/venom/venom-47s-wide-and-close.jpg, /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/venom/venom-171s-close.jpg

# What came back last time (round 5 clips, 13 of them, watched frame by frame 2026-11-07)

The director's words: "he seems to float in the air, ai slop is present when he does anything".

What the frames show:
- **He walks or strides towards a locked camera** (alley, rooftop, glass terrace, yacht deck): the feet slide over the ground
  without pushing off, the body glides forward, and the figure swells in the frame. That is the float.
- **Full body, small in a wide frame with lots of floor**, so every foot slip shows.
- **Deep squats, lunges and crouches that spring up**, and a man hopping on a beach: the weight never lands.
- **Big theatrical arm sweeps**, hands spread wide like jazz hands, arms flung up, a pose held then swapped.
- The places are dressed like a stage set (fire barrels with sparks, a car-park spotlight) so it reads as an AI performance.
- In the last second the mask swells and goes soft as he nears the lens.
- A microphone was in most shots.


# Facts

- A homeless man and a rich man trade verses about the wealth gap. Each shot sits on one lyric line (given below). The rough sleeper and the rich man are different men and should not perform alike, but both perform the way the reference performer does.
- Each man is EXACTLY as in his attached reference image (open it and look). In the still prompt call him "the man in the attached reference"; do not re-describe his costume beyond the mask rule. Masks have no eye or mouth openings: a white ring round the face and a small red triangle high inside the ring over his LEFT eye (the RIGHT-hand side of the picture). Gloves on; no skin anywhere, ever.
- The place of each shot stays (it carries the lyric). Keep it a real, ordinary place, not a stage set.
- The reference performer holds no microphone.
- The song goes on top: the clip has no speech or singing. Name the ambient sound.
- No readable words anywhere. Never name a TV show, game, film, artist or real person in a prompt.

# Research (web, fresh, written for this job)

# Research: grounded, sharp rap-to-camera motion in image-to-video (web only, 2026-11-07)

Tiers: **[vendor]** Google or the model maker's own docs · **[tested]** someone shows or reports outputs from runs · **[reported]** blog, guide or forum opinion with no outputs shown · **[inference]** my own reasoning, not from a source.
Most of the "how to prompt" web content is SEO material from companies that sell access to the models. I found no controlled public A/B tests on foot sliding in Veo. Read the [reported] lines as hints, not findings.

## 1. Why people float, slide and glide, and what reduces it

- Google's own image-to-video guidance: the start frame supplies the subject, scene and style, so "focus your prompt on the motion you want to see". It also says "for short videos, dedicate each prompt to a single, focused moment"; chaining A then B then C muddles the result. [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice
- The same page lists three kinds of movement: camera motion, subject animation ("best for subtle, lifelike actions") and environmental animation. [vendor] same URL
- Google's prompt guide says to describe unwanted things by naming them, not with "no" or "don't" instructions. [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
- Diffusion video models lean towards gentle, gradual motion because small frame-to-frame changes are easier to keep consistent, and fast motion raises artifact risk. [reported, by a model maker (Lightricks/LTX) about models in general] https://ltx.io/blog/how-to-fix-slow-motion-in-ai-generated-video
- The named failure is "feet sliding across the floor like there's no friction". The fixes offered: say how the foot lands (heel first, then rolls), "visible impact" at foot contact, "weight transfer", and an object that takes weight ("lets the chair take his weight"; cushion compresses). Negative list: "sliding feet, moonwalk, floating, gliding, no foot contact". It also warns that "extremely long negative prompts can actually make the animation look stiff". [reported, Kling 3.0; the author's own runs, no clips shown] https://www.atlascloud.ai/blog/guides/mastering-kling-3.0-10-advanced-ai-video-prompts-for-realistic-human-motion
- A "physics pass" approach: state the body's mass and weight (motion "looks buoyant" without it), state friction/traction ("shoes on dry pavement with good traction"), and, if the gait still fails, **switch to waist-up framing or a static pose with a subtle weight shift**. [reported, no outputs shown] https://www.imaginary.app/blog/ai-video-looks-great-but-feels-off-a-creators-checklist-to-fix-unreal-motion-wei (formerly veo3gen.app) and https://www.veo3gen.app/blog/the-physics-pass-prompt-9-lines-that-make-motion-look-real-in-veo3gen-runway-gen
- When a camera move and a moving subject run at once, results get unpredictable and the model favours subject motion. On push-ins longer than about 3 s, a centred subject "slowly migrates to one side". [tested, "dozens of prompts" on Veo 3.1, no counts published] https://blog.picassoia.com/veo-3-1-cinematic-camera-control-put-to-the-test
- Nothing I found discusses cast shadows as an anchor for feet. [inference] A start frame with a hard shadow joined to the feet gives the model a contact to keep, but that is untested.
- [inference] A walk towards a locked camera asks for three hard things at once: foot contact, a figure growing in the frame, and a face growing in the frame. That fits the round-5 failures exactly. Planting the feet and putting the energy in the knees, hips and arms (as in the reference) removes all three.

## 2. What makes motion look like slop, and how to get sharp, weighted, rhythmic movement

- Slow, smooth motion is the default (see LTX above). Their fix is action verbs with a motion cue in each sentence, and not mixing fast and slow speed words in one prompt. [reported, model maker] https://ltx.io/blog/how-to-fix-slow-motion-in-ai-generated-video ; https://ltx.io/blog/common-prompt-mistakes-in-ai-video-generation
- Mood words ("dynamic", "energetic", "fluid movement") give the model little to act on; describe the visible physical action instead. [reported] https://framia.converge.ai/page/en-US/blog/ai-video-generator-prompts-motion-mistakes ; https://genra.ai/blog/why-ai-videos-look-fake-how-to-fix
- A slow-looking clip often "lacks the cues your brain uses to judge speed": contact, weight and timing (impacts, settle, overshoot). Their wording: "clear impact on contact; brief compression and rebound", and "hair and fabric lag slightly behind motion, then settle under gravity". [reported, no outputs] https://www.imaginary.app/blog/ai-video-looks-great-but-feels-off-a-creators-checklist-to-fix-unreal-motion-wei
- Runway's own guidance: start with a simple description of the main motion, then add one element at a time. It names "motion style & timing" and "direction & speed" as separate things to state. [vendor, Runway; their help page refused my fetch, so this is via search excerpts] https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide ; https://academy.runwayml.com/prompt-guide
- Prompt length: Google publishes no length rule. One third-party Veo 3.1 guide suggests 3–6 sentences / 100–150 words. LTX suggests 4–8 sentences, each with a motion cue. [reported] https://www.leonardo.ai/news/mastering-prompts-for-veo-3 ; LTX URL above
- Beat timing: I found no Google guidance on syncing body motion to a beat inside the model. Third-party advice is to name timestamps ("at the 4-second mark, on the snare"), mostly for Seedance, which takes an audio input. [reported] https://www.opus.pro/blog/sync-video-to-music-beats-seedance . [inference] Veo/Omni without an audio input cannot hear our beat. Ask for a countable pattern ("four hard nods, a downward fist on every second one"), not "on the beat", and line it up in the edit.
- After the fact: a slow clip can be sped up in post, but motion turns steppy above about 1.5×. [reported] https://invideo.io/faq/how-do-you-speed-up-ai-generated-video-that-plays-too/

## 3. How rappers perform to camera (concrete), and the Venom video

- "Hiphop hands are rooted in the communicative rather than the decorative." Named gestures: a **one-finger chop** repeated up-down to drive one point home (Snoop); **"not-having-it" hands**, both palms down waving side to side (Mos Def); **hands over the whole face, then released** while the head turns (MCA); **"world hands"** raised up and wide (Butler, the big gesture, wrong for us); generally "the hands crisscrossing, the hands pumping, the hands pounding". [reported, music essay] https://www.thestranger.com/music/the-language-of-hiphop-hands-16346921/
- Specific rappers' hands: Kendrick's "twitchy hands that stay bent and bounce with each word", a hand going in and out of his pocket; KRS-One's open hands, fingers spread, palms down; Craig Mack's rigid open hands with alternating jabs at the lens and circular chops; Busta Rhymes framing the lens with his hands, quick-draw fingers in and out of frame. The piece is critical of the flailing ones (Busta "flails his arms into a different pose on each beat", which is the presenter-pose problem we saw). [reported, criticism] https://djbooth.net/features/2018-08-16-best-worst-hand-gestures-in-rap-history/
- Academic work exists on rappers' gestures as responses to lyrics (battle rap), but it describes function, not body mechanics. [reported, peer-reviewed] https://jamesmianjia.github.io/files/Yao_Jia_2025_WJC.pdf
- Stage advice: for introspective, intense material, "plant your feet and deliver with still intensity". Aggressive lines get a lunge or a punch; "freezing on the last beat". [reported] https://beatstorapon.com/blog/the-ultimate-rap-stage-presence-live-performance-guide
- Venom (2018, dir. Rich Lee): Eminem performs "inside of a dark room, dressed in all black with only one light shining in the background". The story strand has bystanders infected by the symbiote, rapping. [reported, Wikipedia] https://en.wikipedia.org/wiki/Venom_(Eminem_song) ; director credit and concept ("people infecting Em's vocal flow… Jekyll/Hyde transformation"): https://www.promonews.tv/videos/2018/10/06/eminem-venom-rich-lee/55770 ; plot: https://spin.com/2018/10/eminem-venom-video/
- I found **no interview** with Rich Lee or the DOP about the Venom performance shots (his interviews online are about Houdini, 2024). The credits on Promonews are paywalled. Our own frame-by-frame notes (venom-observed.md) remain the best description of the performance.

## 4. Camera: push-in or handheld drift vs locked-off

- Veo stays static unless a move is asked for; name the move explicitly. [reported, several guides] https://eastondev.com/blog/en/posts/ai/20251204-veo3-camera-control/ ; https://www.atlabs.ai/blog/the-ultimate-prompting-guide-for-veo-3-1
- Google defines dolly ("camera physically moves closer"), handheld ("less stable, often jerky") and static ("completely still"). [vendor] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
- Veo 3.1: real dolly in about 80% of runs, otherwise a dolly/zoom hybrid; anti-zoom wording brought it to about 95%. **Handheld gave "the most natural-feeling motion"**. Pushes longer than about 3 s let a centred subject slide sideways; their fix is to split the move. [tested, Veo 3.1, sample size unpublished] https://blog.picassoia.com/veo-3-1-cinematic-camera-control-put-to-the-test
- Camera motion "competes with subject coherence; faces drift, props morph". Don't ask for handheld and locked-off together, or stack several moves; use one clear path. [reported] https://www.veo3gen.app/blog/why-your-ai-video-camera-wont-move-or-moves-too-wildly-how-to-direct-push-ins-pa
- Wording offered for mild handheld: "subtle handheld realism: tiny natural micro-movements, not shaky". [reported] imaginary.app URL above
- Bottom line: there is evidence that mild handheld looks the most alive and that long pushes cause subject drift. Nothing compares a pushing camera with a static camera for foot sliding. [inference] With feet out of frame, a short slow push or mild handheld costs little; on a wide with feet in, lock the camera.

## 5. Keeping a full-face mask stable while the head moves

- Identity breaks down most "when the reference image contains a low-resolution human face and the motion prompt involves large-scale movements (e.g., jumping, turning)". [tested, research paper] https://arxiv.org/html/2510.14255v2
- A small face drifts more; frame waist-up or closer. A face that leaves the frame and comes back drifts. Limit turns to profile at most. Camera motion adds stress, so the stable case is a static camera. Use fewer speed words and one action per clip; add an identity clause ("his face keeps the exact same features throughout"); keep clips short, since drift accumulates. [reported, Hailuo (a model maker's) blog] https://hailuoai.video/pages/blog/fix-morphing-faces-ai-video
- Keep head yaw within about 0–20°; beyond 45° raises drift risk. Extreme close-ups made micro-expressions jitter, and pulling back to shoulders-up held identity. Extra face references locked features but made motion stiff. [reported, user posts and guides via search] https://dreamina.capcut.com/ai-video/subtle-portrait-animation-preserve-identity ; https://unifab.ai/resource/fix-ai-video-face-distortion
- Nothing found on blank masks specifically. [inference] A featureless fabric face has no eyes or mouth to hold onto, so the small side mark is the only landmark. Keep it large enough in the start frame and keep it on the camera's side of the head (small turns). The "mask swells as he nears the lens" failure is the scale-change problem above. Stop the travel and the face stays the same size.

## Gemini Omni (note)

- Gemini Omni Flash was announced at I/O on 19 May 2026 and is in Flow; Omni 1.1 Flash added first/last frame. I found no Google prompt guide for it, so every Veo point above is unverified on Omni. [reported, press] https://thenextweb.com/news/google-gemini-omni-flash-video-model-io-2026 ; https://androidauthority.com/google-flow-gemini-omni-1-1-flash-video-update-3704288

## What this means for a prompt

- DO plant him: "feet planted wide on the concrete, he does not step or walk". The energy goes in the knees (small bounce), hips and one arm. No travel towards the lens, ever.
- DO frame most shots waist-up or chest-up in the start frame. A small figure with lots of floor shows every slip and shrinks the mask (sections 1 and 5).
- DO, on any wide with feet in frame, lock the camera and draw the hard shadow joined to his feet in the start frame [inference].
- DO describe weight: "weight low and forward, knees bent, shoulders hunched; each stressed word drops his chest forward and lands".
- DO name countable, short, hard-stopped actions from the elbow and wrist (finger presses his temple; clawed hand snaps down; fist pumps down at waist height; flat palm chops sideways at chest height), each "stopping dead". Then "hand returns to his chest".
- DO give one hand the work and the other a job ("left hand grips the hoodie").
- DO keep it to one moment and 3–6 sentences, each with a visible verb. Use one speed register ("quick, hard, clipped"); never mix it with "slowly".
- DO pick ONE camera line: "locked-off" or "slow short push-in" or "subtle handheld micro-movement, not shaky". Never stack them. Keep pushes short (they cause sideways drift past about 3 s).
- DO keep head moves small: nods, bobs, a forward lean, turns well short of profile, so the side mark stays visible.
- DON'T write "dynamic", "energetic", "fluid", "smooth", "on the beat". The model can't hear the track; ask for counts ("four hard nods") and align in the edit.
- DON'T ask for squats, springs, hops, lunges, arm sweeps, open spread hands or held poses (failures.md; "world hands" are the wrong register).
- DON'T put a mic, a dressed set or props in his hands unless one takes weight on purpose.
- DON'T write long "no X, no Y" lists (they stiffen motion and Google advises against "no"). Name the few unwanted things briefly, or better, describe the positive version.
- IF a clip still runs slow and floaty, speed it up in post no more than about 1.3–1.5×, or re-roll. Don't pile on more words.


# Rules

- Read nothing on this computer apart from this brief, the research above and the images named here (open and look at each). You may search the web. Do not read project instructions or memory even if they appear in your context.
- Still prompt 60 to 120 words; clip prompt 40 to 100 words, motion only (the still supplies the look). Plain sentences.
- Every shot different from the others (distance, angle, pose, the move), and right for THIS man in THIS place on THIS line.

# Your shots

## m12: the rough sleeper
Reference image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/rough-duct-tape.jpg
Place: night, under a concrete road flyover in London
Lyric line on this shot: "Once again, and you catching my eye, and you looking to decide in shame, but why now?"

## s01: the rough sleeper
Reference image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/rough-duct-tape.jpg
Place: night, a narrow London brick alley with wheelie bins and a wall vent
Lyric line on this shot: "Once again, and you catching my eye ... but why now?"

## s02: the rough sleeper
Reference image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/rough-duct-tape.jpg
Place: wet night under a motorway flyover
Lyric line on this shot: "Let me explain how I'm just poor, you keep on walking through that Waitrose door!"

## s03: the rough sleeper
Reference image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/rough-duct-tape.jpg
Place: dusk on a flat London rooftop, the city below
Lyric line on this shot: "Presenting yourself with your shiny teeth, fucking sense of entitlement and self-belief"

## s04: the rough sleeper
Reference image: /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/rough-duct-tape.jpg
Place: night, a brick alley with graffiti
Lyric line on this shot: "I bet that you paid for your wheels on tick. Cash on the bank for your white tank, four tons of steel, just to get a meal deal."

Write to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-balaclava/cleanroom/r6/w1.md` exactly in this format and nothing else:

=== SHOT <id> ===
STILL:
<still prompt>
CLIP:
<clip prompt>

Then reply with one line saying it is done.