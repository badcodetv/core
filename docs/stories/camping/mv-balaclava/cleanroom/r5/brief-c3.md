# The job

You write image-to-video motion prompts (Google Flow, its fast "Omni Flash" video model, Frames mode: the still is the FIRST frame; 16:9, 720p, 8 seconds) for a music video. A masked man raps to camera. Each prompt animates one approved still.

# What the director has said, word for word

"i asked for the balaclava guy to rap and gesture like eminem on stage, he kind of raps and gestures like a geography teacher, so fix that". Earlier: "rapping to the camera and gesturing like eminem". "make sure they never show skin".

The last clips failed because the man barely moved: polite hand chops, head held square, feet planted, hands at chest height. These stills were made to fix that: each already shows a big performance pose. The clip must CONTINUE that energy for the whole 8 seconds.

# Facts

- No mouth or eyes on the mask: the performance is the whole body on the beat (knees, shoulders, arms, the free hand, the mic hand, the head).
- The mask: white ring round the face, small red triangle high over his LEFT eye (the RIGHT of the picture). It can slide toward the centre when the head turns a long way, so the head should keep facing the lens most of the time; nods, jolts, leans and dips are fine. Gloves on, no skin, ever.
- The camera does not move (the editor adds camera moves later): say so once, plainly. With the camera still, all the energy has to be in the body.
- The song goes on top: no speech or singing in the clip's sound. Say what the ambient sound is.
- The cut uses 1 to 3 seconds of each clip, sometimes twice, so the energy must be there from the first second, not built up slowly.
- Nobody new enters the frame; the background stays what it is.

# Research (web, fresh, written for this job)

# Clean-room research: live stage-rap body language, and getting big motion from image-to-video

Sealed web research, 2026-11-07. Grades: **[sourced]** = a source says it, URL given; **[described]** = from a review or description, impressionistic; **[inference]** = my reasoning, nothing written found.

**Overall honesty note:** very little written text exists about the physical vocabulary of early-2000s arena rap performance in general, or this performer in particular. Concert reviews from 2000–2002 talk about sets, pyro, lyrics and crowd size, almost never about bodies. Most of section 1 is therefore [described] or [inference]. The footage itself (the 2000 tour DVD, the 2002 tour DVD, festival sets) is the real source. Someone should watch it, because the written record will not settle this.

## 1. The physical vocabulary of the live style

- **Energy and arrival.** One retrospective says the crowd was "pleasantly stoned" and the performer "brought everyone back to life once he hopped on stage" [described] (https://www.xxlmag.com/eminems-best-live-performances/). A 2000 Salt Lake City review credits him with stage presence and charisma the openers lacked [described] (https://www.deseret.com/2000/8/19/19524575/rappers-glorify-sex-drugs-violence).
- **Movement quality.** One article calls his stage movement "spastic", with a "rapid pace and explosive energy" [described, weak source] (https://medium.com/@poppulsenewsmag/eminems-audacious-stage-presence-ignites-debate-on-relevance-and-artistic-expression-a9667cfb8b19).
- **Walking, kneeling and stillness.** A student analysis of the 2000 awards-show performance says he will "walk about… or kneel down or stand still" and commanded the stage [described] (https://digitalspace.bradfordcollege.ac.uk/10626679/?p=211, unreachable at fetch time, quoted via search snippet). Note that it mixes stillness in with the movement: the live style is contrast, not constant motion [inference].
- **The hype man.** The longtime hype man performed that role on the 2000 tour, helped design sets and set lists, and "counseled his friend on how to pace his performances" [sourced] (https://www.mtv.com/news/bxu21v/proof-eminems-best-friend-and-a-vital-member-of-detroits-hip-hop-scene). The hype man as a role goes back to the late-80s hype-man tradition [sourced] (https://www.complex.com/pigeons-and-planes/2016/09/hype-man-history). Nothing written describes their physical choreography together.
- **Generic rap stage craft.** Call-and-response, working every side of the room, eye contact with all sections, the performer as "ringmaster" [sourced] (https://beatstorapon.com/blog/the-ultimate-rap-stage-presence-live-performance-guide). Generic stage-presence advice ("stand tall, feet shoulder-width, deliberate gestures") [sourced] (https://kiwix.lema.org/wikihow_en_maxi_2023-03/Have-a-Good-Stage-Presence) is the polite version, and is close to what produced the "geography teacher" clips.
- **The specific vocabulary** below is commonly seen in footage of the period. It is unwritten, so all of it is [inference]:
  - Stance is wide with knees bent and weight forward on the balls of the feet. The torso pitches toward the crowd, never upright.
  - The bounce is a knee-driven up-and-down on every beat, with the shoulders riding it. At hook peaks it becomes small hops.
  - He prowls the lip of the stage from side to side, stopping dead on a punchline.
  - The mic hand stays near the face, its elbow high and out. The free hand does the talking: a stabbing index finger at the crowd on each stressed syllable, a flat palm chopping down on the rhyme, the forearm swinging like a hammer.
  - The one-arm pump is a fist or open hand thrown straight up on the beat at the hook, often with the whole crowd copying.
  - He crouches low at the stage edge, one knee nearly down, leans out over the front row, then springs back up.
  - The head drives the rhythm: chin jutting forward, a sharp nod on the downbeat, the head snapping toward a section of the crowd.
  - The build into a hook goes from compact and coiled (bent, prowling) to fully open (arms high, jumping). The hook is the biggest the body gets.
  - The hype man stands shoulder to shoulder with him, shouting the end words of lines and mirroring the arm pumps.

## 2. Getting big motion out of Veo/Omni-style image-to-video

- **Google's own framing leans small.** The Vertex best-practices page says that for image-to-video you should prompt the motion, not re-describe the image. It describes subject animation as suited to "subtle, lifelike actions", and its example is "hair and clothes flutter gently" [sourced] (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice). Camera motion is called "the simplest and most reliable way to add dynamism" [sourced, same page]. The model's default is probably small, polite subject motion [inference].
- **Name the pace.** The official prompt guide lists pacing words such as "fast-paced action" and uses adverbs to set speed. It also advises describing what you want rather than writing "no" or "don't" [sourced] (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide).
- **Intensity words work both ways.** One guide sets out a ladder from "very subtle movement, minimal motion, nearly still" to "energetic movement, dynamic motion throughout". It says "subtle", "gentle" and "minimal" damp the motion, and "visible movement throughout" raises it [sourced, vendor blog] (https://veo3-ecru.vercel.app/blog/veo-3-image-to-video-guide-2026).
- **Why clips only wiggle.** Prompts that describe what exists rather than what changes produce near-static clips. Use "high-commitment verbs" and avoid "subtly move, gently animate, drift, float" [sourced, vendor blog] (https://www.imaginary.app/blog/image-to-video-that-actually-moves-not-just-wiggles-a-9-step-troubleshooting-che). The same page advises "start → transition → end state, then hold" and "one action only". Those suit product shots but are poison for a performance: "hold" and "one action then stop" tell the model to go still [inference].
- **Lists of locks freeze the body.** The same source offers "Shoulders stay square to camera" as an anchor. That is exactly the square-headed stiffness we are trying to remove [inference]. Lock identity and wardrobe only, never posture.
- **Too many verbs.** A pile of verbs with no timeline is a named cause of static or broken shots [sourced, vendor blog] (https://www.veo3gen.app/blog/veo3gen-prompt-debugging-faq-2026-fix-12-common-failures-like-too-static-random-). So use one repeating rhythmic pattern (bounce + point + pump on the beat) rather than ten different moves [inference]. A loop reads as performance and gives the model a steady target.
- **Start frame.** Cramped or heavily cropped photos give stiffer motion. Use a clear, full-body, uncropped image [sourced, vendor blog] (https://www.veo3ai.io/es/blog/veo-3-ai-dance-video-generator-2026). Don't crop hands and joints if you want gestures, and leave space in the direction of motion [sourced] (imaginary.app above). If the still contradicts the prompt, the model oscillates between the two [sourced, same page].
- **Limb warping.** Warping peaks at the fastest moment, so reduce speed or rotation there. Hands anchored to an object stay more stable than free hands, and hands that are small in frame warp more [sourced, aggregated] (https://higgsfield.ai/blog/ai-video-hands-faces; https://morphic.com/resources/how-to/ai-video-troubleshooting). Over-specified motion ("waving arms wildly") and re-describing anatomy cause warping. Contact cues ("heavy footsteps", "firmly planted feet", "knees flexed") keep the body structured [sourced, observational not tested] (https://hailuoai.video/pages/knowledge/realistic-limbs-posture-ai-video-guide).
  - Practical fix [inference]: the mic in one hand anchors that arm. Make the free hand do big but simple, repeated moves (point, chop, pump) rather than flailing. Plant the feet in the words so the energy reads through bent knees and bounce.
- **Locked camera.** The guide defines a static shot as "camera remains completely still" [sourced, Google prompt guide]. Nothing says a locked camera reduces subject motion. But the official guide treats camera motion as the main source of dynamism, so with the camera locked all the energy must be written into the body [inference]. Lock the camera explicitly so the model doesn't spend its motion budget on drift.

## 3. Composing the start still

All of this is [inference] from the sources above:
- **Distance.** Use a medium-wide or full shot, knees up at least, with headroom and a hand's width of space above the raised arm. A close-up leaves only the head to move, which is the geography-teacher failure.
- **Angle.** Shoot low from crowd height, slightly below the stage lip, looking up. That puts the performer leaning over the lens, as if over the front row.
- **Pose.** Catch him already mid-gesture: weight on the front foot, knees bent, torso pitched forward, mic hand at the mask, free arm extended and pointing at the lens or raised. A neutral standing pose invites a neutral clip, because the model continues what it sees.
- **Room for motion.** Leave empty stage to one side for the prowl, and don't crop either hand.
- **Light.** Stage backlight and haze help the silhouette read clearly, and clean edges reduce texture crawl [sourced, imaginary.app].

## 4. Example motion prompts (no names, no text)

1. "Fast-paced live performance: the masked man bounces hard on bent knees to the beat, leans out toward the crowd and stabs his free hand's finger at the camera on every stressed word, mic held tight to his mask. Static camera."
2. "Aggressive, energetic movement throughout: he prowls quickly from left to right along the stage edge, shoulders rolling, then stops dead and throws his free arm straight up, fist pumping on the beat."
3. "He drops into a low crouch at the lip of the stage, leans over the front row with his head jutting forward, then springs back up and jumps, arm pumping, as the crowd's hands rise."
4. "Heavy, planted footwork: knees driving up and down, his head snapping forward on each downbeat, his free hand chopping down hard like a hammer on every rhyme, faster and faster."
5. "The energy builds: compact and coiled at first, bouncing and pointing at the crowd, then he opens up completely, both arms high, jumping on the beat, his whole body thrown into the hook."
6. "He paces in a tight circle, bouncing, turns sharply to face the camera, leans in close and jabs his finger at the lens three times in rhythm, then swings his arm out wide toward the crowd."
7. "A second masked man beside him shouts along and mirrors his arm pumps; they bounce shoulder to shoulder, both leaning toward the crowd, free arms punching up on the beat."

Avoid in these prompts: subtle, gentle, minimal, calm, hold, stays still, shoulders square, slowly, one action then stop.


# Rules

- Read nothing on this computer apart from this brief, the research above and the still images named for your shots (open and look at each). You may search the web. Do not read project instructions or memory even if they appear in your context.
- Never name a TV show, game, film, artist or real person. No readable words.
- One motion prompt per shot, 50 to 100 words, plain sentences, motion only (the still supplies the look). Every shot moves differently; the rough sleeper and the rich man perform differently.
- Do not write: subtle, minimal, gentle, slight, small, calm, restrained, "then stops", "holds still", "four times". Those are what made the last clips stiff.

# Your shots

## t05: the rich man
The still (first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/t05xr5-b.jpg
Place: clear day, the aft deck of a big white motor yacht at sea
Lyric line on this shot: "Prospects exist, and now I insist ..."
The still's writer suggested: He swaggers forward along the deck bouncing on bent knees, then stops dead and jabs his free index finger down at the lens on every stressed word, static camera.

## t06: the rich man
The still (first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/t06r5-b.jpg
Place: bright day, a private tropical beach with palms and a sun lounger
Lyric line on this shot: "What about if we tax the rich? What the fuck you think this is, bitch?"
The still's writer suggested: Aggressive and fast throughout, he advances on the camera kicking up sand, both hands jabbing at the lens on each word, then flings his arms wide in disgust, static camera.

## t07: the rich man
The still (first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/t07r5-a.jpg
Place: an underground car park, strip lights, a glossy black luxury saloon
Lyric line on this shot: "I work hard, hard to pay for my yard, paying my tax with a platinum card. You want change, but my pockets are empty"
The still's writer suggested: He rocks hard on the raised knee to the beat, snapping the card down like a hammer on each rhyme, then hops off the bumper and turns his empty pockets out toward the camera, static camera.

## t08: the rich man
The still (first frame): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/t08r5-a.jpg
Place: warm evening, an English country-house garden party by a pool, guests with champagne
Lyric line on this shot: "the only thing I'm changing is the lane in my M3 ... Wealth gap, fucking what a load of crap, now please let me drink my Chateau Neuf"
The still's writer suggested: He bounces on the chair, pumping the champagne flute up on every beat as the guests copy him with their glasses, then leans out over the pool toward the lens on the punchline, static camera.

Write to `/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-balaclava/cleanroom/r5/c3.md` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>

Then reply with one line saying it is done.