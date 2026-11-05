# The job

You write image-to-video motion prompts for a glossy 1920s Prohibition music video: masked robbers in sharp suits rapping to camera over a cockney woman's rap about money printing and inequality. Each prompt animates one approved still for 6 seconds. These two replace clips the director rejected.

# Facts about these clips

- Each still becomes the FIRST frame of a 6-second clip (Google Flow, its fast video model, 16:9). The editor cuts fast on the beat (about 92 beats a minute, a beat every 0.65 s) and may use any 0.6 to 2.6 seconds of it, so the performing must start in the first half second and never stop: a new move every beat or two, no standing still, no slow build.
- The man (or men) in the still are rapping at the camera. They wear knitted balaclavas with NO mouth hole, so there are no lips to sync: the rapping is all in the body, head, shoulders and hands. Big stage-rapper moves done sarcastically, mock-serious, too much: see the gesture research below. More than pointing.
- Name the moves in order, on the beat ("on the first beat… on the next…"), and make them big, sharp and readable at a glance. Nothing he holds may vanish or turn into something else; if he holds something, he keeps it.
- Masks keep their shape: a white ring round the face and a small red triangle high on the RIGHT side of the picture (the man's left eye). Gloves stay on. Suits, hats and masks never change.
- The camera stays still (locked off); the editor adds camera moves later. Say so.
- No speech or singing; the song goes on top. Sound effects are fine (stamps, claps, cloth, the room).
- Nothing new enters the frame. Other people in the still stay where they are and react little; no new people appear.

# Your 2 shots

## v05x-a — 2:55 in the song — the lyric: "Hungry people feed a revolution, then it's retribution, perhaps some execution"
Still (open it and look): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/gang/moodboard/v05r5-a.jpg
Jack on the current clip: "when he spins around he kind of teleports please fix thanks". No spin, no full turn: keep him facing the lens.

## v11x-a — 3:05 in the song — the lyric: "It's time to give, not just to take, but for heaven's sake, don't just eat cake"
Still (open it and look): /mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/gang/moodboard/v11r5-a.jpg
Jack on the current clip: "\"don't just eat cake\" the gesturing doesnt match this line please fix thanks". The gestures must clearly play the cake line (mimed is fine: nothing new may appear in his hands unless it is in the still).


# Web research: fixing image-to-video failures

## 3. Fixing image-to-video failures (Veo-family, Flow)

### General rules that apply to every fix

- **STRONG (Google).** For image-to-video, "Your source image already provides the subject, scene, and style. Focus your prompt on the motion." Re-describing the character, background or lighting makes prompts redundant that "confuse the model and lead to poor results". Refer to the character as "the subject", "he", "they". ([Google Cloud, Veo best practices](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice))
- **STRONG (Google).** Camera movement with a static scene is "the simplest and most reliable way to add dynamism". Subject animation is "best for subtle, lifelike actions". (same page)
- **STRONG (Google).** "A sharp, clear, and well-composed" source image gives a more coherent video, because the model takes character detail from it. (same page)
- **MEDIUM.** Characters drift because the model puts motion ahead of consistency once the prompt gets complex. A character can look right for the first frames, then slowly change. Keep prompts short, and change one variable per retry. ([veo3gen.app](https://www.veo3gen.app/blog/veo-31-image-to-video-this-week-the-first-frame-lock-workflow-for-consistent-cha); [Artlist](https://artlist.io/blog/consistent-character-ai/))
- **STRONG (research).** Google DeepMind's Physics-IQ benchmark found video models' physical understanding "severely limited" and *unrelated* to how realistic they look. Sora scored highest on realism but only about 10 % on physics. Realistic-looking destruction is exactly where these models fail. ([arXiv 2501.09038](https://arxiv.org/html/2501.09038v3))

### 3a. A mask pattern that drifts, vanishes or changes mid-clip (k02, k06, k11)

- **MEDIUM.** Lock the camera (tripod / locked-off) or use only a slow dolly-in. These are the most stable options. ([veo3gen.app](https://www.veo3gen.app/blog/veo-31-image-to-video-this-week-the-first-frame-lock-workflow-for-consistent-cha))
- **MEDIUM.** One guide recommends explicitly asking the model to keep the same face shape and outfit throughout and to avoid morphing during camera moves. ([Veo 3 negative prompt guide](https://veo3-ecru.vercel.app/blog/veo-3-negative-prompt-guide-2026))
- **WEAK (inference, from the drift mechanism above):**
  1. **The still must show the mask clearly**: large in frame, facing camera, the ring and the triangle sharp. A tiny mask in a wide car shot (k02, k06) gives the model too few pixels to keep. For car interiors, frame **medium-close through the windscreen**, not a wide of the car.
  2. **Keep the head turn under about 30°.** The triangle sits over one eye. A big turn hides it, and the model re-invents it on the way back. Favour shoulders, hands and the body for the motion.
  3. **No occlusion**: no hand passing over the face, no wind-whipped scarf, no smoke across the mask. Anything that covers the pattern lets the model redraw it.
  4. **Slow and small**: one action per clip ("he grips the wheel and glances to the side, then back to the road"). Don't stack actions.
  5. **Motion prompt names the mask only as something to keep**, without describing it, e.g. "his knitted mask stays exactly as it is". This follows Google's "don't re-describe" rule while flagging the item to keep.
  6. **The plane hang (k11):** wind and violent movement attack a soft knitted mask. Shoot it **from above, looking down at the gripping gloves and the top of the masked head**, with the camera moving and the body swaying, not thrashing. Or hold the mask face-on with only the background (clouds) moving.
  7. For a shot that must be wide and fast, accept that the mask is unreadable. **Cut it short (under 1 bar)** so the drift never shows. Cutting before the drift is a legitimate fix.

### 3b. A character "teleporting" in a spin (v05)

- **MEDIUM.** Practitioner guides say a turnaround should be a *gentle* orbit from the front to a slight side angle, and suggest wording like "moves like a smooth dolly, not a teleport". Interpolation breaks on chaotic motion. ([Veo 3 camera control guide](https://veo3-ecru.vercel.app/blog/veo-3-camera-control-prompts-2026); [Veo 3 negative prompt guide](https://veo3-ecru.vercel.app/blog/veo-3-negative-prompt-guide-2026))
- **WEAK (inference) on why:** during a full 360° the model loses sight of the reference face and costume for most of the turn. On the way round it re-generates the figure from scratch and lands it in a slightly different place, size or pose. That is the "teleport".
- **WEAK (inference) on fixes, in order of reliability:**
  1. **Half turn, then cut.** He turns his back to camera (180°) and the clip ends there. Cut to a second clip that starts with his back to camera and turns to face. The cut hides the hidden side.
  2. **A partial pivot**: a quarter turn of the shoulders with the head staying on camera (a swagger turn, not a spin).
  3. **The camera orbits slowly** round a planted figure instead of the figure spinning. Describe it as one continuous move ("the camera slowly circles a quarter of the way round him while he keeps rapping").
  4. **Fake the spin in the edit**: a whip pan or flash-frame transition between two clips (facing away, then facing camera). This is a classic music-video spin and needs no generation of the turn at all.

### 3c. People at the wrong scale in the still (p08, the giant in the alley)

- **MEDIUM (forum).** Nano Banana 2 users report wrong proportions even with references. The advice is explicit proportion wording, or pinning scale with a reference that already has the right layout. One user got accurate scale by roughing a composite first and using it as a reference. ([Reddit snapshot](https://reddit.sentinel-team.org/posts/1rxkwfn/snapshots/2026-03-20T21%3A15%3A59.791656Z); [Skool post](https://chat.skool.com/pro-grade-ai-training/scaling-products-in-an-image))
- **STRONG (Google).** Describe the scene in rich, specific prose, and use the "shot from a [camera angle] with a [lens]" pattern. ([Google AI Studio image docs](https://aistudio.google.com/docs/image-generation))
- **WEAK (inference) on wording that fixes scale:**
  - **Give the camera a height and distance:** "shot at eye level from across the alley, about six metres back, 35 mm lens". A defined lens and distance gives the model a perspective to obey.
  - **Anchor each figure to the architecture:** "all three men stand on the same cobbles, the tops of their heads level with the bottom of the first-floor window; the doorway behind them is a head taller than them". Real objects of known size (doors, windows, a lamp post, a barrel) are the scale ruler.
  - **"Three men of the same ordinary height, shoulder to shoulder in one line"**, rather than "the leader in the middle". "Leader", "central" and "dominant" invite the model to make him bigger.
  - **Fewer people in the shot.** Three in an alley is safer than six. The rest of the gang can be in a separate shot.
  - **A different staging that sidesteps the problem:** one performer framed medium with the others soft behind, or a low angle that makes the alley loom. Scale errors are hardest to see when figures stand at clearly different depths.

### 3d. Destruction that looks real, not "AI slop"

- **MEDIUM (practitioners).** Generators have no rigid-body physics; they reproduce patterns. A vague prompt gives a "screensaver" look. Describing the *specific material and its failure* works better ("the beam buckles" rather than "debris flies"). Short prompts beat stuffed ones. Plan on 2–3 rerolls per physics shot, and a complex multi-object success rate of about 50 % in one vendor's tests. ([Hailuo field notes](https://hailuoai.video/knowledge/simulating-impact-prompting-debris-gravity); [Reddit snapshot](https://reddit.sentinel-team.org/posts/1stsfx4/snapshots/2026-04-24T22%3A04%3A53.789389Z); [invideo FAQ](https://invideo.io/faq/how-accurately-do-ai-video-generators-simulate-physics/); [CapCut](https://www.capcut.com/create/ai-video-physics-realism-whats-fixed-and-whats-broken))
- **STRONG.** Models that look realistic still fail physics (Physics-IQ, above). The best fix is to **stage destruction so the model needs little physics**:
  - one material;
  - one direction of motion;
  - a camera close to the detail;
  - the cause off-screen or implied;
  - the rest left to the edit and the sound.

**WEAK (inference) on stagings, most reliable first:**

**Bullets through a wooden door (k26):**
1. **From inside the room, camera locked on the door.** Beams of hard daylight punch through new holes one after another, so dusty light shafts appear across the dark room. The light *is* the bullet hole, and light shafts are something the model renders well. Small splinters puff from each hole towards the camera. Two or three holes, not twenty.
2. **The reaction.** A masked robber presses flat against the wall beside the door, and splinters spit past his shoulder. The destruction stays small at the frame edge, and the performance carries it.
3. **The aftermath.** A slow push-in on the door riddled with holes, smoke drifting through the light beams, then it swings open on its own with a creak.
4. **Avoid:** a wide shot with the door exploding into planks, any axe or tool stroke (repeated tool contact is where it looked fake), and splinters flying in every direction.

**Barrels off a truck / down stairs:**
1. **One barrel, close.** A single barrel rolls off the tailgate in the foreground, at low angle, and the camera tracks it a short way. One rigid object on one path is the most reliable.
2. **The aftermath plus one detail.** The barrels are already down, one is split, and liquor glugs out across the cobbles, with the camera low in the spreading puddle. Liquid spreading on a surface is a strong pattern for these models; tumbling multi-body physics is not.
3. **The reaction.** The driver in the cab glances at the mirror, which shows the barrels bouncing away, small and soft in the reflection.
4. **Down stairs:** shoot from the bottom step looking up, with **one** barrel thumping down two steps towards the lens, then cut. Don't ask for a cascade of many barrels.

**The safe from the wall:**
1. **Through the hole, from inside the wall, looking out.** The chain is hooked on and goes taut, the plaster cracks in one line, and dust trickles. Then **cut** to the truck pulling away, then to a wide of the empty hole. The pull happens in the cut.
2. **The blown door instead of the whole safe.** Close on the safe door, a puff of smoke from the hinges, and the door sags open a few inches. Small, one part, slow.
3. **The aftermath.** A clean, neat rectangular hole in the wallpaper, the dangling chain swinging, and a robber dusting off his gloves to camera. That is a joke as well as an image.
4. **A practical action.** The robbers simply wheel the safe out on a sack truck, straining, ironically calm. It needs no destruction physics at all.

- **WEAK (inference).** For all three, the **sound does half the work**: splinter cracks, wood thuds, a groaning chain. A short clip on the beat with a hard sound effect reads as violent where a long clip of AI debris reads as slop. These are good candidates for a flurry (§1).

---



# Web research: gestures for these lines

## 4. Gestures that match specific lyrics

- **MEDIUM-STRONG.** Rap performers use beat gestures most, then iconic gestures (miming the line's image), pointing gestures, and gestures aimed at the viewer. ([Chodakova & Podhorná-Polická](https://is.muni.cz/publication/1686116/en?lang=en))
- **WEAK (inference).** Sarcasm reads through an iconic gesture done **too politely or too grandly**, a beat of stillness, then a look into the lens. A masked face can't smirk, so the irony goes into a **head tilt** and **timing**: the gesture lands, then he holds still for half a beat. Every idea below is staged for a locked camera with the mask kept face-on (§3a).

### "don't just eat cake" (the closing line, after "it's time to give, not just to take, but for heaven's sake")

1. **The refused slice.** He holds a dainty slice of cake on a china plate at chest height and lifts it to the mouth hole of the mask. He stops, tilts his head to the lens, and slowly turns the plate round to offer it to the camera, to the viewer. "Don't just eat it: give it." It closes the give/take couplet.
2. **The Marie Antoinette.** One gloved hand on his chest, the other pointing with a cake fork like a lecturer, a tiny wagging fork on "don't". He finishes by dropping the fork onto the plate with a clink. The cake line is the famous "let them eat cake" misquote, and the posh gesture sends it up.
3. **Cutting it fairly.** A big tiered cake on the table. On "for heaven's sake" he looks up to the ceiling; on "don't just eat cake" he cuts it into many even slices with a knife and slides one towards camera. That is redistribution as a gesture. It also suits the camera locked over the table, hands only, with the mask framed above.

### "hungry people feed a revolution"

1. **The empty plate to the raised fist.** He taps an empty tin plate twice on the beat on "hungry people". On "feed a revolution" the hand that held it rises into a slow, deliberately theatrical clenched fist. One continuous motion, no turn.
2. **The bread roll as a grenade.** He tosses a bread roll up and catches it like a grenade, then mimes pulling a pin with his teeth at the mask's mouth hole. A deadpan look to camera.
3. **Spoon-feeding.** He spoon-feeds an imaginary person below frame, mock-tender. On "revolution" he flips the spoon and raps it on the table like a gavel.

### "the right and the left both witness the theft"

1. **The two hands.** He holds both gloved hands out at shoulder height, palms up like weighing scales, and his head turns slightly to each: right, then left. On "theft" both hands snap shut together, and he opens one to show it is empty. A pickpocket's trick. Keep the head turns small.
2. **Hands over eyes.** He covers the right eye-hole with one glove ("the right"), then the left eye-hole ("the left"), then makes a slow "I saw that" point into the lens with two fingers to his own eyes and then out. **Caution:** a hand over the face risks the mask drifting (§3a). Use it only in a close, slow clip, or split the line across two cuts.
3. **Two witnesses.** Two other robbers stand frame left and frame right, each with a hand over their mouth in mock shock. The rapper in the middle opens his coat to show it lined with banknotes, and shrugs. It plays the line as a group gag and keeps any one head from moving much.

- **WEAK (inference) on the cut.** These lines are punchlines, so per §2 they go to **performance shots held for the whole bar** (2.6 s, or the whole 6 s clip for the closing line). The final "don't just eat cake" is the outro's hero shot: hold it, then cut to the logo or to black.

---



# Rules

- Read nothing on this computer apart from this brief and the still images listed for your shots (open them and look). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist or real person in the prompt. No readable words. Guns point up or away, never at the camera or anyone; no one hurt.
- One motion prompt per shot, written for exactly what that still shows. 50 to 100 words, plain sentences.

Write to `/home/jackt/projects/badcode/badcode/docs/stories/bank-robbery/songs/mv-gang/cleanroom/r7/clip-fx.md` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

(<id> is the shot id exactly as given in its heading, e.g. v05x-a.) Then reply with one line saying it is done.