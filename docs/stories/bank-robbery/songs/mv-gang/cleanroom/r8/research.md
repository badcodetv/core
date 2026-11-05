# r8 web research: stable masks, rap-plus-action cutting, drop-only beat cuts, a believable getaway car

Sealed web research, 2026-11-05. Read: `r8/jack.md` (Jack's words) and the web only.
Grades: **STRONG** = official docs, or several independent sources agree. **MEDIUM** = one credible practitioner source, or vendor guides that agree. **WEAK** = my inference, labelled as such.

Honest headline: nobody on the web has published tests on keeping a *masked face's small graphic* stable in Veo. The nearest evidence is about logos, labels and printed text on clothing and products, which fail the same way (a small, flat, high-detail mark that the model redraws every frame). Everything below is carried over from that.

---

## 1. Keeping the mask's ring and triangle stable in image-to-video

### What the sources say

**1.1 The first frame holds, the end drifts.** Veo follows the start frame closely and treats an end frame "as a guide rather than a hard constraint"; endpoint adherence is tighter on short (4 s) clips. **MEDIUM** (one developer guide, matches the logo guides below).
- https://dev.to/akaranjkar08/veo-31-developer-guide-timestamp-prompting-multi-shot-video-and-full-api-june-2026-3l5i

**1.2 Small marks get redrawn and garbled, even in Frames mode.** A Reddit post (mirrored) reports "smaller text always gets garbled in Veo 3, even when using image to video (Frames)", and the fix is to composite it in post and plan for that at the shot list. A product-video guide says the same for logos: no vendor publishes a logo-fidelity rate for any video model; check frame by frame. **MEDIUM.**
- https://reddit.sentinel-team.org/posts/1rxytpu/snapshots/2026-03-19T18%3A10%3A01.537681Z
- https://blog.laozhang.ai/en/posts/fix-logo-distortion-ai-product-video

**1.3 Fine pattern flickers; anchor to big, simple traits.** Prompt guides tell you to anchor identity to "outfit color, hairstyle, silhouette" rather than tiny detail, and warn that intricate patterns (embroidery) flicker: use simpler textures. **MEDIUM** (vendor guides, consistent with each other).
- https://www.atlascloud.ai/hi/blog/guides/veo-3.1-prompt-guide
- https://getimg.ai/blog/google-veo-3-1-review

**1.4 Less rotation, less zoom on the mark, locked camera.** The logo guide gives turning by 15° or less as the safe zone. It counts "spin", "360" and "dramatic zoom into label" as warning signs, says to move the light or the camera rather than the object, and says a locked-off shot is the easiest case both for the model and for fixing it later. Orbits make the model invent unseen geometry, so things warp. **MEDIUM.**
- https://blog.laozhang.ai/en/posts/fix-logo-distortion-ai-product-video
- https://www.overseeros.com/blog/why-ai-videos-look-fake

**1.5 Lock the camera and the subject in words, one action only.** A first/last-frame guide recommends "Locked camera, tripod-stable, no zoom/pan/tilt", "single continuous shot, no cuts", "keep framing identical from start to end", a subject lock sentence, and *removing* extra style adjectives, because competing descriptors cause identity drift. Limit the prompt to one action beat and add "no extra props, no additional actions". **MEDIUM.**
- https://www.imaginary.app/blog/veo-31-firstlast-frame-2026-a-creators-guide-to-seamless-transitions-outfit-chan

**1.6 Frames with both ends supplied: matched bookends.** The most common first/last failure is bookends that don't line up. Overlay the two at 50% and check that key points (eyes, logo centres) sit in the same place. Large differences between the two frames cause interpolation artifacts. Supplying the same image as both start and end is a known Flow trick to bring a scene back to its starting state (used for loops). One Adobe bug report says it can throw errors on Veo 3.1 Fast. **MEDIUM** for "matched bookends hold better". **WEAK** (my inference) for "the same still at both ends pins the mask": no one has tested that for identity.
- https://www.imaginary.app/blog/veo-31-firstlast-frame-2026-a-creators-guide-to-seamless-transitions-outfit-chan
- https://www.veo3ai.io/blog/veo-3-seamless-looping-video-guide-2026
- https://community.adobe.com/bug-reports-403/generic-error-when-using-two-reference-frames-for-video-looping-in-veo-3-1-fast-1553443

**1.7 Ingredients vs Frames.** Google: Ingredients is for "consistently us[ing] the same images for your character and key objects from one clip to the next". Frames is for "a video that starts and ends with specific images". References work best "on a plain or segmented background". The prompt should "complement, not contradict, your visual inputs". **STRONG** (Google help). Practitioner guides boil it down to: Ingredients = "match this character exactly", Frames = "go from this frame to that one". **MEDIUM.** Sources disagree on whether reference images work on Veo 3.1 *Fast* at all (one says last-frame only, another says multi-reference works), so this is **unresolved**: test it in Flow.
- https://support.google.com/flow/answer/16353334?hl=en
- https://getimg.ai/blog/google-veo-3-1-review

**1.8 The detail must be fully visible in the first frame.** One creator found a name on a mascot costume came out misspelled in the follow-up if it wasn't fully visible in the first frame. **MEDIUM** (one source, but it matches 1.1).
- https://theaifilmmaker.substack.com/p/testing-the-limits-of-ai-video-with

**1.9 Re-roll counts.** Generate 4 to 6 takes and judge them the same way every time: the first frame, frames 5 to 10, and the last frame. **MEDIUM** (one guide; no source gives a measured success rate).
- https://blog.laozhang.ai/en/posts/fix-logo-distortion-ai-product-video

**1.10 High-contrast, clear starting image.** Several hosting guides recommend clear, bright, high-contrast start images and high-resolution inputs. **MEDIUM** (vendor).
- https://www.atlascloud.ai/models/google/veo3.1-fast/image-to-video

**1.11 Describing the detail in the motion prompt.** Guides split. One camp says to say what must stay fixed ("label position, minimal logo mark"). The other says to keep the motion prompt short, because adjectives compete and cause drift (1.5), and the text must not contradict the image (1.7). **MEDIUM** that the prompt should *state the lock briefly*. **WEAK** (my inference) that one short sentence ("the mask does not change: white ring, one red triangle over his left eye, no holes") beats both silence and a long description. A long description invites the model to redraw.

### Why dark and red masks fail worst (my reading)

**WEAK, inference.** A red triangle on a red or dark-red knit is a small mark with little brightness difference from its ground. That is the "fine detail with low contrast" case the sources say flickers (1.3, 1.10). A white ring on a dark knit holds better than the triangle because it is large and high-contrast, which matches what Jack sees. Small-in-frame heads make the triangle a few pixels wide, and the model can't hold a mark it barely sees (1.2). Head turns rotate the mark past the ~15° safe zone (1.4) and show the side of the head that isn't in the start frame, which the model has to invent (1.4, orbit point).

### Post-production fixes

- **Use the clean stretch only.** If the mark is fine until the last second or two, "hold a clean frame or shorten the clip", cutting "before it breaks". The first-last guide says the same: trim before the model "adds ideas". **MEDIUM.** https://blog.laozhang.ai/en/posts/fix-logo-distortion-ai-product-video
- **Cut around it with an insert.** A brief smear while the rest holds: cover it with an insert or cutaway. **MEDIUM**, same source.
- **Composite the mark.** Wrong through most of the clip, camera locked, flat surface: put a static overlay on top. Camera moving or the head turning a little: planar track (Mocha AE inside After Effects, or DaVinci Resolve), which handles position, scale, rotation, shear and perspective. AE's point tracker keeps the graphic flat on a z-turn and looks wrong. Cloth deforms, so Resolve's **Surface Tracker** (plus Patch Replacer to paint out the bad mark first) is built for logos on clothing and faces. **STRONG** (several independent tutorials agree).
  - https://www.graduateschool.edu/learn/after-effects/replacing-logo-mocha
  - https://dvresolve.com/tutorial/logo-replacement-surface-tracker/
  - https://community.adobe.com/t5/after-effects-discussions/add-logo-on-moving-shirt-which-tracking-method/m-p/12442029
- **Premiere on its own.** Premiere's mask tracking (Effect Controls, track forward/back) follows a region with an *effect* on it, for example a blur or colour fix. It does not carry a graphic, and many forum threads report it stalling (workarounds: nest the clip, hide other tracks). It can hide a stray eye hole (darken or blur the region) but cannot redraw a triangle. **MEDIUM.**
  - https://www.adobe.com/nz/learn/premiere-pro/web/blur-face-masking-tracking
  - https://community.adobe.com/t5/premiere-pro-discussions/mask-tracking-not-working/m-p/15040918
- **ffmpeg.** An `overlay` of a PNG triangle at a fixed position works only on a locked shot where the head barely moves. Anything that moves needs tracked coordinates. **WEAK** (my inference from how the overlay filter works; no source tested this).

### Ranked recipe (the practical order)

1. **Design the still to survive.** Head large in frame (chest-up or closer for rapping shots), face square to camera, the triangle clearly separate in colour and brightness from the knit (white ring, red triangle on a mid or light knit, not red on red or red on near-black). Plain or simple background behind the head. *(1.2, 1.3, 1.7, 1.10; dark-mask point WEAK)*
2. **Frames mode, start frame = the approved still, and supply an end frame that matches it.** For rap-to-camera, use the same still or a near twin (same framing, a tiny change of mouth or hand). For action, use a second still made in the same session with the mask fully visible. Overlay-check the two. *(1.1, 1.6, 1.8)*
3. **Lock the camera and limit the head.** "Locked camera, tripod-stable, no zoom, pan or tilt; single continuous shot; he faces camera throughout, head turns no more than a little." One action per clip. Let the hands, body, light, smoke and background carry the energy, not the head. *(1.4, 1.5)*
4. **One short lock sentence for the mask, no extra style adjectives.** *(1.5, 1.11; WEAK on the exact wording)*
5. **Shorter where it matters.** Ask for the motion to finish early. Plan to use only the first 2 to 4 s of a 6 s clip for the hardest shots (small heads, turns). *(1.1, post: clean stretch)*
6. **Re-roll 4 to 6 takes per hard shot.** Check frame 1, around frames 5 to 10 and the last frame, and pick on the mask first. *(1.9)*
7. **Ingredients only when Frames can't hold the character entering mid-shot**, and test first whether references work on the Fast model you're on. *(1.7)*
8. **In the edit:** trim to the clean stretch → cover a brief break with an insert → track a triangle patch (Resolve Surface Tracker / Mocha AE) for a hero shot that can't be re-rolled. Premiere mask tracking only to hide an eye hole. *(post fixes)*

---

## 2. Rapping to camera alongside action

**2.1 There is no published standard ratio.** Academic work (Vernallis) holds that music-video editing is not continuity editing and that "editing works to keep any single element, such as narrative, performance, or star, from dominating". No source gives a hip-hop shot ratio. **STRONG** that there is no rule. **MEDIUM** on the Vernallis reading (the summaries are secondary).
- https://repository.uwl.ac.uk/4706/1/EditingDossiermsmi.2017.6.pdf
- https://www.everand.com/book/338685541/Experiencing-Music-Video-Aesthetics-and-Cultural-Context

**2.2 A working split for AI music videos.** One AI music-video guide sets the split before generating, e.g. 40% performance / 40% story / 20% atmosphere: "a production constraint that prevents the AI from deciding the balance for you". Its map by section: verses "story-led with selected artist inserts", pre-chorus story with short performance inserts, the **chorus as the performance anchor**, a bridge that drops performance. Don't automatically end on more singing. The failure it names is "endless generated singing… the viewer gets the same information from every scene even though the backgrounds change". **MEDIUM** (one guide, but it targets exactly this workflow).
- https://jackrighteous.com/en-gb/blogs/ai-art-visuals-creatives/atlabs-performance-vs-story-scenes-ai-music-video

**2.3 Lip-sync selectively.** Use performance "where the face and delivery actually matter". Before using a performance shot, ask whether seeing the mouth improves the meaning, whether the face should be remembered, and whether the shot is long enough to read. **MEDIUM**, same source.

**2.4 Editors: performance sets the pace, story takes over.** Editor Ryan McCally: performance drives the pace at the start, then it's adjusted to serve the story once all the scenes are in. Others cut the performance first as a spine and lay the narrative over it. **MEDIUM.**
- https://www.lbbonline.com/news/finely-sliced-understanding-the-essence-of-the-story-with-ryan-mccally
- https://lbbonline.com/news/more-than-just-cutting-to-the-beat-the-nuance-of-editing-music-videos (403 to fetch; summary from search)

**2.5 Hybrid is the default, so give it a reason.** A production blog calls performance+narrative hybrids "probably the most common and overused type". The fix is to make the two halves talk to each other, not to drop one. **MEDIUM.**
- https://www.silvertipfilms.co.uk/latest-blog-music-video-production-london-narrative-vs-performance/

### Applying it to an action-first heist video (my synthesis, WEAK unless noted)

- **Ratio, action-first:** about **60–65% action, 25–30% rapping to camera, ~10% texture** (money, hands, signs, smoke). Shift from 2.2's 40/40/20 toward action because Jack asked for it. Performance stays present by **owning the hooks** (2.2) and appearing as inserts in the verses. *(WEAK)*
- **Rap inside the action location, not a separate set.** The robber raps to camera *in the vault, in the back of the car, at the counter*, with the heist still happening behind him: a mate wheeling the safe past, sirens, sacks. That turns a performance shot into an action shot and kills the "same information every scene" failure (2.2). *(WEAK: inference from 2.2 and 2.5.)*
- **Reaction shots as the hinge.** Action shot → the rapper glances off, line lands → back to the action he reacted to. It links the two halves without stacking performance. *(WEAK)*
- **Alternation pattern for verses:** A-A-P-A-A-P (two action, one performance), with the performance shot landing on a punchline. Never two performance shots in a row unless the rapper changes (a hand-off between two robbers trading bars counts as one exchange). Never the same robber in the same framing twice within a verse. *(WEAK)*
- **Hooks:** performance-led, but alternate rappers and locations each hook bar, and every hook shot has action behind it. *(WEAK, extends 2.2)*
- **Split screen / picture-in-picture:** an option for one moment (e.g. a two-way split of rapper | action at a hook landing, or 1920s iris/matte panel styles that suit the period). Use it once or twice, not as a system: it repeats fast. *(WEAK; no source tested it.)*
- **Mask bonus:** rapping shots inside action locations can still be framed chest-up and square to camera (§1 recipe step 1). The action behind does the moving, so the mask holds. *(WEAK)*

---

## 3. Holding shots and cutting on the beat only at big drops

**3.1 Don't cut on every beat.** Cutting on every beat "quickly becomes predictable". Hold the important moments and "save faster patterns for parts of the song that actually increase in energy". Drops call for a stronger transition; breakdowns call for slower pacing or a longer hold. **STRONG** (several independent editing guides agree).
- https://www.capcut.com/create/music-video-pacing-emotional-montage-rhythm
- https://www.soundonsound.com/node/4905278
- https://autoeditai.net/blog/how-to-edit-your-own-music-video-premiere-pro-ai

**3.2 Cut on phrases, not mid-phrase.** Music runs in 4- and 8-bar phrases. Cut on full bars or phrase ends, because a cut mid-phrase "feels off". If a cut sounds wrong, move it to the phrase boundary 4 bars back. **STRONG.**
- https://artlist.io/blog/how-to-add-music-to-a-video/
- https://blog.motionarray.com/learn/premiere-pro/cut-music-to-video-premiere-pro/
- https://licensing.routenote.com/blog/?p=9560

**3.3 Burst length and what follows.** A beat burst = a cut on every beat for **4 to 8 beats**, "then return to 2- or 4-beat cuts". The pre-drop build uses longer holds (~4-beat cuts). The drop itself gets "1 clip change exactly on drop" using the strongest shot, plus at most one motion accent. Use bursts only if the footage supports them. **MEDIUM** (one detailed guide; it matches 3.1).
- https://cursa.app/en/page/beat-based-editing-in-capcut-syncing-cuts-transitions-and-motion-to-music

**3.4 Finding the drop in a hip-hop track.** A drop is "a reintroduction of the full bass line and drums after pulling them back for a verse or buildup". Hooks are the fullest section (usually 8 bars), and verses are stripped back for the vocal (usually 16 bars). Pointers into a drop: a snare roll or fill in the last bar, or a muted 808 that leaves a hole the drop fills. Many trap-style tracks put a beat break before the final hook. **MEDIUM.**
- https://hiphopmakers.com/how-to-make-beats-song-arrangements
- https://www.futureproducers.com/forums/threads/how-to-identify-hooks-and-verses-on-a-hip-hop-instrumental-beat.547876
- https://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq.ipfs.4everland.io/wiki/Bass_drop.html

**3.5 Finding it by measurement.** Onset/novelty detection (spectral flux: summing band-energy rises frame by frame, then peak-picking) marks new events. A big flux spike after a low-energy stretch is the signature of drums re-entering. **STRONG** for the method (signal-processing literature). **WEAK** that it marks *drops* reliably: nobody tested that.
- https://www.audiolabs-erlangen.com/content/05_fau/professor/00_mueller/02_teaching/2018w_mpa/2018_Mueller_MPA_BeatTracking.pdf
- https://archives.ismir.net/ismir2004/paper/000191.pdf

### Recipe for this track (~92 BPM; 1 beat ≈ 0.65 s, 1 bar ≈ 2.6 s; my synthesis)

- **Verses: hold.** At 92 BPM a 6 s clip is ~2.3 bars. Holding "as long as you have been" means cuts land every 2 bars (~5.2 s) on a downbeat, with most clips used nearly whole. Cut on bar 1 of a phrase, not on every snare. *(3.1, 3.2; numbers are arithmetic)*
- **Mark the drops first** (listen, then check against a flux/energy plot): (a) each hook entry after a verse, (b) the drums coming back after any break, (c) the final hook. Expect 3 to 5 real drops in 3.5 minutes. Not every hook is a "big drop". Pick the 2 or 3 biggest for bursts. *(3.4, 3.5; counts WEAK)*
- **The bar before the drop:** hold, or one longer shot through the fill. The hold makes the burst land. *(3.3)*
- **On the drop:** one hard change exactly on the downbeat to the strongest action shot, then a burst of 4 to 8 one-beat cuts (2.6 to 5.2 s). These are where the short, clean first-seconds of hard-to-hold clips (§1 step 5) earn their place: a burst only needs 0.65 s per shot. *(3.3; the §1 link is WEAK, my inference)*
- **After the burst:** step down to 2-beat cuts for a bar, then back to holds. Don't burst again until the next marked drop. *(3.3)*

---

## 4. The getaway-car opener: what reads as slop, and a more believable staging

### Slop tells (what the viewer notices)

- **Wheels whose spin doesn't match the car's speed**, reflections in paint and glass that don't match the surroundings. **MEDIUM.** https://whichoneisreal.com/mode/videos/vehicles/
- **Cars sinking into the road or hovering; heavy objects moving "like foam"; impacts with no reaction.** Weightless debris is the obvious one for a car bursting through doors. **MEDIUM.** https://sites.google.com/view/physics-failure-detection · https://www.overseeros.com/blog/why-ai-videos-look-fake
- **Unmotivated camera moves** (orbits, crane rises) and vague "cinematic camera" language. Orbits make backgrounds warp. Vehicles stretch or shrink in the background. **MEDIUM.** https://www.overseeros.com/blog/why-ai-videos-look-fake
- **Too many moving elements at once** (smoke + particles + debris + car): one dominant motion per shot reads better. **MEDIUM**, same source.
- **Warped signage or plates.** **MEDIUM.** https://www.popsci.com/diy/how-to-spot-ai-generated-video/
- **My reading of "bursting out" specifically (WEAK):** a door smashing open is the hardest physics there is (splinters, hinge failure, weight transfer), and the model usually gives a door that melts or opens itself. A car that starts parked and "launches" also shows the model inventing acceleration from zero.

### What reads as real (practical film grammar)

- **Practical camera positions:** low front or rear bumper mount (greatest sense of speed; *Bullitt* did it), offset, with little sky in frame. Wide lens on the rig. A process trailer keeps the car at its normal height. **MEDIUM.** https://strikeengine.com/?p=1978 · https://new-blog.artlist.io/blog/?p=2996 · https://www.taylorfrancis.com/books/9781136046742/chapters/10.4324/9780080517049-24
- **Inside the car:** *Gun Crazy* (1950) shot its bank-robbery getaway as one take from the back seat, camera never leaving the car, which was new for robbery scenes then. *Bonnie and Clyde* (1967) shows its escapes with a cloud of dust behind the car and close-ups held inside the car. **MEDIUM** (TCM and a Lehigh film breakdown, via search; TCM page 403 to fetch).
  - https://www.tcm.com/articles/581437/pop-culture-101-gun-crazy
  - https://history-on-trial.lib.lehigh.edu/trial/reels/films/list/2_63_8_4829
- **Rig reflections on bodywork** are a real-shoot tell. In AI, the matching tell is reflections that don't match the street. So keep the paint reflecting what is actually in the frame (street lamps, a shopfront). **MEDIUM** (4kshooters) / **WEAK** for the AI parallel. https://4kshooters.net/2015/07/22/tips-and-tricks-on-rigging-cameras-to-cars

### A staging for the opening shot (WEAK, my synthesis of the above)

Pick one, all built to dodge the tells:

1. **Already moving, locked camera, across the street.** Tripod-height, static camera on the far kerb. The garage or bank-side doors are *already open* and the car is *already rolling* through them in the start frame, nose out, rear wheels still inside. It swings out and past, left to right, with dust and newspaper lifting behind it, then exits frame. One dominant motion (the car), one secondary (dust). Ask for "heavy, with visible weight and momentum; the body rolls on its springs as it turns".
2. **Low bumper-height, car coming at camera.** Camera locked low at street level just outside the doors. The car, already moving, comes out and passes close over or beside the lens. Dust and grit kick up. Plate unreadable or out of frame.
3. **Back seat, *Gun Crazy* style.** Camera locked in the back seat, looking forward over two masked heads (the masks face away or show only from behind: the triangle problem disappears). Through the windscreen the street lurches, and the driver yanks the wheel. The world outside the glass does the moving. Strong as an opener because it puts the viewer in the gang.

What to drop: doors being smashed, flying debris, a camera orbiting the car, a car starting from stationary, sparks, and more than one moving vehicle in frame.

---

*Sources not fetchable (403) were read only through search summaries and are marked where cited. No source anywhere tested a face mask graphic in Veo: §1's mask rules are transferred from logo, label and costume-text evidence.*
