# The river throw: review of rounds r11 to r15, and what to do next

Written 2026-11-27 by Fable 5.2 as a review. Nothing was generated for it and no other file was changed.
The shot: at night on the riverside walk, drunk Karen throws her phone into the river while Susan laughs,
and "Fuck you, Sean!" is voiced over it in post.

**The short answer.** The model did not get worse. The same recipe that made the take Kai picked on 24 Nov
still works on 27 Nov. Rounds r11 to r15 failed because we changed the start picture to one the throw
cannot happen in, and then tried to fix a picture problem with more words (the words did fix the glass by
r15, but not the throw). One of the four fresh takes
(`r15orig1`) is the strongest throw we have ever had and shows the phone splash into the river; it needs four
bad frames cut out. No take has Karen's wine glass, because the picture they start from has none.

## How this was checked

- Read: `docs/rules/flow.md`, `docs/google-flow/omni-flash.md`, `docs/google-flow/2026-11-09-omni-1-2-sweep.md`,
  `docs/stories/karen/prompts-river-drop.md`, the story's `badcode.md`, Kai's own notes in `cut-notes.json`.
- Read the recipe card (`.prov.json`) of all 30 throw clips. Every one: Omni 1.2 Flash, Frames mode (the still is
  frame one), 8 s, 720p, one output. The only things that vary are the start still, the Character and the words.
- Looked at frames. All six takes from the original still (`river-shout-b`) at 6 frames a second, and the
  release of each at every frame. From the glass still (`r11throw-a`), 7 of the 18 takes at 3 frames a second
  (r11throw, r12throwa, r14throw1, r14throw6, r15throw1, r15throw4, r15throw6), plus six frames from each of the
  six r15throw takes; for the r12 and r14 takes I did not open I rely on the frame-by-frame notes already in
  `cut-notes.json` (replies at1517 and at1548). All six r15k set-ups.
- Measured whether the railing and skyline hold still (frame 0 against later frames, same crop).

## 1. Why r11 to r15 failed

Ranked by how much each cause mattered.

### Cause 1: the start still (most of it)

The glass was added by making a new start still, `r6/moodboard/r11throw-a.jpg`, and that still cannot hold
this throw.

| | Original still `river-shout-b` | Glass still `r11throw-a` |
| --- | --- | --- |
| Where Karen is | At the railing, touching it | Mid-walk in the middle of the path, the railing about two metres away and behind her |
| Which way she faces | Away from us, towards the river | Straight at the camera |
| Where the river is | Fills the frame beyond the rail | A thin strip at the right edge, behind a mesh fence |
| Her hands | Right arm up with the phone; left hand planted on the rail | Both hands free in the air, phone in one, glass in the other |
| The phone | Pale, lit, against dark sky | Black, against a dark bridge |
| Faces | Hidden (hers), Character cast | Both fully visible, no Character |

In Frames mode the clip keeps the still's layout. From the original still the throw is the next thing that
happens: the arm is already up and the river is already in front of her. From the glass still the prompt had to
ask her to "swing round to the railing" first, which is a move to a place she is not, and then throw sideways
across the path. What came back, every time I looked: a side-arm flick while walking (r14throw6 at 1.3 to 1.7 s,
r15throw1 at 0.7 to 1.0 s), the phone leaving by the right frame edge at head height or dropping near the fence
(r11throw at 1.7 s), and no water for it to land in. In r15throw4 and r15throw6 the "splash far off" was drawn
on the fence itself at 2.7 to 3.0 s, because there was no river in view to put it on. That is Kai's "meek throw,
the phone just goes on the floor".

Engine notes that already said this:
- `omni-flash.md`, "Ask it to continue a state, never to reach one": look for the framing where what you want is
  already visible in the start image.
- `omni-flash.md`, "The change/adherence trade is a straight line": when both matter, change the starting frame
  so the ask can be small, not the prompt.
- `flow.md`, Jack 2026-11-20: "a clip keeps the still's geometry".

Score, from the recipe cards and the frames: **18 takes from the glass still, none usable past 3.4 s. 6 takes
from the original still: 2 strong throws, and 3 where the phone clearly goes over the rail (a fourth is unclear).**

### Cause 2: two things in two free hands, and too many things to do (r11 to r14)

Karen held a phone in one raised hand and a glass in the other, both hands loose, facing us, and the prompt
gave her five things to do in a row (swing round, throw, grip the rail, breathe hard, sip the wine). In r11,
r12 and r14 the glass changed hands or a second glass or phone appeared (r11throw: a glass in each hand from
3.0 s, and she sips from the wrong one at 4.0 s; r14throw6: the glass is in her other hand by 3.3 s; reply
at1517 records the other r14 takes). This is known behaviour of this model, not a new fault: the 9 Nov sweep
records "Props swap hands: a wrench went left to right, or became two wrenches, in 3 of 4 styles", with the fix
"the start image shows one prop in one named hand, and the prompt names that hand in every beat". "A
multi-waypoint trajectory duplicates the subject" covers the five actions: one subject, one motion.

**The r15 re-rolls fixed this part, and it is worth keeping.** Their prompts cut the action to one move and
parked the glass hand ("Her left hand keeps holding the same one wine glass, low at her side, the whole time";
"her left hand stays at her hip"). In all six `r15throw` takes one glass stays in the same hand to the last
frame (checked at six points in each take, at reduced size, not every frame). So the glass can be held. What
those six takes still had was cause 1, and one new fault of their own: the prompts took out the wind-up
("already has her right arm raised… snaps that arm forward once and lets go"), so the throw is a wrist flick.
The original prompt's "swings her arm back and flings" is what gives the full-body throw.

The prompt also grew from 84 words in the original to 103 in r11, 116 in r12/r14 and 136 in r15, mostly bans and
scenery ("Nothing appears or duplicates in anyone's hands", "No extra phones, no extra glasses", "The railing…
never move or shift"). I can't show these did harm. They did not do the job they were written for either: the
railing was never mentioned in the original prompt and does not move in any of the six takes from that still
(measured, section 2). The engine notes' advice for Frames mode is to cut the prompt down to the motion ("The
tab rule").

### Cause 3: no Character, and faces in full view

The original still was made with the `Karen` Character cast and shows her from behind. The glass still was made
by an image edit of a frame from the walking shot with no Character (`r11throw-a-a.png.prov.json`,
`"character": null`), and the six r15c stills were edits of that edit, again with no Character. An edit redraws
every face. So the r15k clips show two different women (r15k1 from 5.3 s, r15k3 and r15k6 throughout: younger,
long hair, a black top). That is Kai's "faces look completely different" and "it isn't Karen". The story's own
rule is "Cast, never describe a face"; `flow.md` (Jack, 2026-11-20) says a close-up built from a group shot
invents the face.

### Cause 4: the r15k stills start after the throw

Four of the six r15c stills show the phone already in the air (c1, c2, c3, c5). The clip then has no throw in
it, only a phone to keep flying, which is the hardest thing for the model ("Why falling objects fail": no
physics, errors compound each frame). r15k1: the phone simply drops (Kai: "no throw"). r15k2: it comes down
by the fence (Kai: "flops onto the floor"). Each set-up also got one take only, when the best recipe we have
lands about one time in three.

One of them is fine as a picture of the water: r15k5 (looking at the river, no faces) shows the phone hit the
water at 1.0 s and sink glowing until about 5 s. A hand and a bar hang in the top of the frame until 2.6 s.

### Cause 5: we re-rolled instead of going back

Kai's r12 note (at1548) said: "please look at the reference shot from before we changed it to this and just
re-cut the same shot a few times". We re-rolled the new glass still instead: 3 takes, then 8, then 6, then six
new stills built from it. The original recipe was not re-run until today. The engine notes' own summary of the
August fight is "nothing that has failed in motion has ever been rescued by describing it better".

### Is there any sign the model regressed?

**No.** The four `r15orig` takes use the 24 Nov recipe word for word (same still, same prompt, same `Karen`
Character, Omni 1.2 Flash, Frames, 8 s, 720p; checked in the recipe cards). They give the same framing, the same
woman, a railing and skyline that do not move, a committed throw into the river in one of four and a soft one
over the rail in a second. The spread was already there in
the first week: the 25 Nov re-roll from the same still (`r6-throw-river-shout-b.mp4`) threw the phone to the
right along the railing, which Kai flagged at the time (at1485). Six takes are too few to see a small change in
the model, but every failure in r11 to r15 follows something we changed.

What does defeat us on this shot is narrower than "the throw": it is a throw from a still where she isn't at
the rail and faces the camera, with no Character to hold her face.

## 2. Verdict on the original and the four fresh takes

All five start from `river-shout-b`. In none of them does Karen hold a glass (the still has none; Susan keeps
hers). In all five the railing and skyline hold still up to at least 4.3 s (similarity of the railing area to
frame 0 stays flat at 0.83 to 0.86 in every take; in the r14 take where Kai saw the railing move it falls from
0.87 to 0.69, a rough comparison because that is a different still).
Karen's face, when she turns, is the same dark-haired woman in all five; her hair is dark brown, not the
Character's auburn, because the still drew it that way.

| Take | The throw | Where the phone goes | Faults | Verdict |
| --- | --- | --- | --- | --- |
| **Original** `r4-shout-river-shout-b` | Shakes it to 2.3 s, winds back, lets go at 2.67 s. Committed | Up and out to the left over the rail; shrinks and dims by 3.2 s; what looks like a small dot drops to the water at 3.3 to 3.5 s, with a tiny splash at 3.8 s | None in the throw. From about 4.5 s the camera drifts (the skyline has shifted about 40 px by 7.9 s) and she turns to the camera at 5.3 s | **Usable. In 0.0, out 4.4** |
| **`r15orig1`** | Full-body wind-up from 1.4 s, leaning right back, lets go at 2.33 s. The most committed throw of all 30 clips | A clear high arc to the left, over the rail, into the water at 3.3 s, a big splash in the river from 3.4 to about 4.7 s | Four bad frames at the release, frames 56 to 59 (2.33 to 2.46 s): a ghost second arm, a wine-red streak in the sky, and for one frame she faces the camera. Her face shows during the wind-up (1.6 to 2.1 s), same woman | **Best take. In 0.0, out 4.9, with frames 56 to 59 dropped** |
| `r15orig2` | Shakes to 2.5 s, then tosses it straight up at 2.9 s. A lob, not a throw | Up out of the top of frame, back in at 3.3 s, falls just beyond the rail by her hand at 4.0 to 4.3 s. No splash | No morphs; her back is to us until 5.5 s | Clean but soft. Fallback only. In 0.0, out 4.5 |
| `r15orig3` | A toss straight up at 2.2 s | Falls back down beside her shoulder at 3.0 to 3.2 s; unclear whether it clears the rail | Susan's face is buried in her glass from 3.3 to 5.2 s | Not usable |
| `r15orig4` | Turns to the camera with the phone like a selfie (1.3 to 2.5 s), throws at 3.2 s | Drifts right across the sky towards Susan and lands on the boardwalk at her feet at 4.7 s | A lit phone is back in Karen's hands from 7.0 s | Not usable |

**Use `r15orig1`.** It is the only take that shows all of: a real throw, the phone's whole path over the
railing, a splash in the river, and nothing else moving.

How to use it in the cut:
- Drop frames 56 to 59 and close the gap (`select='not(between(n,56,59))',setpts=N/FRAME_RATE/TB`). Frame 55
  (arm at the top, phone in hand, her back to us) then meets frame 60 (arm pointing out, phone in the air, face
  in profile). **This is a guess that it reads as one fast snap; I looked at the frames, not at it moving.** Build
  it and step through. If the jump shows, try dropping only 57 and 58.
- In at 0.0 s, out at 4.9 s of the original clip (the splash has settled; her hand starts up to her face at 5.0).
- "Fuck you, Sean!" starts 1.84 s into the voice line. With the line starting when the clip does, it lands about
  0.3 s before the release at 2.33 s. That is closer than on the original take (0.6 s before).
- The splash sound belongs at 3.40 s of the clip (3.23 s once the four frames are gone).
- The flashback later in the film reuses the same clip, so it changes too.

**A guess about "the video quality looks really low"** (Kai at1528 on the original take, at1485 on the 25 Nov
re-roll): both are 1280x720 at about 3 to 4 Mb/s, and the shots either side (`old clips/28.mp4`,
`new clips/44.mp4`) are 1920x1080 at 5 to 10 Mb/s. Our rule keeps new clips at 720p until delivery. The free
check: run Flow's free 1080p upscale on `r15orig1` and put it next to the 720p file in the cut.

## 3. Plan for the next attempt

### First, what Kai has to pick

1. **Ship `r15orig1` as it is, with no glass in Karen's hand.** No new generation. The throw and the river are
   solved today.
2. **Try once more for the glass**, with the plan below, keeping `r15orig1` as the fallback.

My recommendation: put `r15orig1` in the cut now, and run the plan below once. It joins the two halves that
have each worked on their own: the still and throw words of the original (the throw), and the parked glass
hand of r15 (the glass). If it gives nothing, stop; the film reads fine without the glass.

### Shot design: one shot, the proven one

One locked shot from behind Karen at the rail, the same frame as `river-shout-b`. Not a cut of two or three:
Kai took the water shot out after the throw in r15 (at1560), and `r15orig1` shows the throw and the splash in one
frame. If Kai later wants a beat on the water, `r15k5` from 0.2 to 2.5 s (top of the frame cropped off to lose
the hand) is already made.

The only change to the picture: Karen's left hand, which already rests on the top rail, holds her glass there.
A glass held still in a hand that is planted on something, well away from the throwing arm, is the safest way
to carry a second object (engine note "Objects vanish on the occlusion round trip": "a mug held still is safe";
the 9 Nov sweep: one prop in one named hand). The six `r15throw` takes back this up: with the glass hand named
and parked, the glass held in all six, even from the bad still. **Whether it holds on this still is untested.**
In the six takes
from this still her left hand stayed on the rail through the throw in at least three (the original, `r15orig2`,
`r15orig3`); it is hidden during the wind-up in `r15orig1` and comes off the rail in `r15orig4`.

### Step 1: one new start still (Kai picks before any clip is made)

- Tool and model: the same as the accepted still. A `flow_queue` edit job, Nano Banana Pro, 16:9, 2 outputs.
- Reference image: `/mnt/d/badcode-videos/karen-story/clips/r4/moodboard/river-shout-b.png`.
- Character: `Karen`.
- Project: the story's own (`da8feea7-0574-437b-8ff9-97da233a0a4f`), because a Character is cast.
- What I changed from the accepted still's prompt, and why: the glass in her left hand on the rail (Kai's r10
  note); "camera position" added to the list of things kept from the reference, so the frame does not move; the
  phone's pale back named, because a black phone vanished against the dark in r11 to r15. The STYLE LOCK is the
  story's block, unchanged.
- I did not describe her hair, although it is dark brown in these takes and auburn on the Character. The rule
  is to describe nothing when a Character is cast. If the candidates come back dark again and Kai minds, the
  narrow exception in `flow.md` (a figure turned away, so the Character cannot bind) allows one hair clause.
- Check each candidate before showing it: one glass in Karen's left hand on the rail, one glass in Susan's hand,
  one phone, Karen's face turned away, the railing and bridge where they are in the reference. Run the QA
  scanner with `--ref` on the reference.

Paste into: the Flow image prompt box (as the `prompt` of the edit job).

```
STYLE LOCK (keep identical every time):

Capture look only (NOT time period): cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day.

Present-day constraint: modern clothing, modern vehicles, modern architecture, contemporary street design and signage; no retro/period props or era-specific styling.

Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.

Color: punchy, vibrant palette with warm skin tones; mild film-like color cast; deep but soft blacks (not HDR).

Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).

Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.

Output: high detail, natural imperfections, candid snapshot energy.

Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look, no historical setting/era shift.

Night by the river, the same railing, lit suspension bridge, skyline and camera position as in the reference image, present day. The woman from the character reference stands at the railing seen from behind and slightly to her right, her right arm thrust straight up above her head, a phone gripped high against the night sky with its pale back towards us, her head tipped back, shouting up at it. Her left hand rests on the top rail and holds a stemmed glass of red wine upright against the rail. Beside her, a second woman doubles over the railing laughing, a stemmed wine glass in her hand. The bridge lights bloom in the black water. A wide shot from behind the two of them, their faces turned away towards the river.

Thanks.
```

### Step 2: eight takes from the picked still

- Settings, the same as the take Kai picked: Omni 1.2 Flash, Frames, start frame = the picked still, Character
  `Karen`, 8 s, 720p, 16:9, one output per job, eight jobs, through the tab pool
  (`scripts/scene/pool.mts`). Character jobs stay on the main project.
- Why eight: from this still about one take in three is a strong throw, and some of those will lose the glass.
- The prompt is the 24 Nov prompt with two changes and nothing else. Added: one sentence that names the glass
  hand and gives it nothing to do. Removed: "wine slopping from her glass". With two women holding wine that
  clause can attach to either, and a wine-red streak is exactly what appeared at Karen's arm in `r15orig1`
  (**a guess**, one take). I did not add anything about the railing, the background, counts of phones or glasses,
  or what must not happen: the railing has not moved in any take from this still without being told.
- The same-prompt check will flag this as a repeat of the r4 prompt. It is kept on purpose.

Paste into: the Flow video prompt box (the job's `motion` in `video-jobs.json`), after the `@Karen` chip.

```
The camera does not move. The woman at the railing shakes the phone high above her head, shouting up at it, leaning back on her heels; then she swings her arm back and flings the phone in a high arc out over the railing towards the dark river. Her left hand stays on the rail the whole time, holding her wine glass still. Beside her the other woman doubles over laughing. Sound: river water lapping against the pilings, wind, distant traffic rumbling on the bridge. No dialogue, no music. The camera does not move.

Thanks.
```

### Step 3: judge each take against five checks, then stop

A take passes only if all five hold from the first frame to its out point (about 4.5 to 5 s; anything after
the out point does not matter):

1. One phone leaves her right hand once, passes above the top rail and goes out towards the water. A splash is
   a bonus.
2. One glass, in her left hand, on the rail, the whole time. Susan has one glass.
3. Step through the six frames either side of the release: two arms, one head, facing the river.
4. The railing and skyline match frame 0 at the out point.
5. She has not turned to the camera before the out point.

Then:
- **One or more pass:** show Kai the passes beside `r15orig1`. Upscale the pick to 1080p in Flow.
- **None pass, the glass held but the throws went sideways or were lobs:** one more round of eight with one
  change only, "flings the phone in a high arc far out to the left, over the railing, into the dark river".
- **None pass because the glass moved, swapped or doubled:** stop for good. The cut keeps `r15orig1`. Do not
  write a longer prompt.

Cost: eight takes at 24 credits is 192 credits (the 9 Nov sweep's price for 8 s at 720p on Omni 1.2).

## 4. What is wrong or missing in our rules and engine notes

Proposed text only. None of these files was edited.

### a. `docs/google-flow/omni-flash.md`: the top of the file says a Character cannot go with a start frame. It can

Wrong today: the table row "Flow's UI will not let you attach a character to a start frame… `[confirmed
2026-08-16]`", the box "The combined mode does not exist in Flow", the struck-through "Both" line under
"Choosing the mode", and "Still unknown: whether Flow's Frames tab now accepts a Character". The same file's
2026-10-04 entry records a Character chip attaching in Frames mode, `scripts/scene/run.mts` casts one with "@"
after the Start slot is filled, and all six takes from `river-shout-b` ran that way on Omni 1.2.

Proposed replacement for the table row and the box:

> **Superseded 2026-10-04, confirmed again on Omni 1.2, 2026-11-27.** A Flow Character does attach in Frames
> mode: fill the Start slot, then type "@" and the Character's name in the prompt box (`scripts/scene/run.mts`,
> `atCast`). The ingredients button is still absent in Frames mode; "@" is the only route. Six Karen river takes
> (24 to 27 Nov, Omni 1.2 Flash, 8 s) ran with a start still and the `Karen` chip.
> ⬜ **Not measured:** whether the chip changes the picture in Frames mode. In those takes Karen starts with her
> back to us and turns later; she turns into the same woman every time, with the still's dark hair rather than
> the Character's auburn. The test: the same still, four takes with the chip and four without, compare the face
> she turns with.

### b. `docs/google-flow/omni-flash.md`: new section, proposed

> ## 2026-11-27: a throw is decided by the start still (Karen river throw) `[observed, Omni 1.2 Flash, Frames, 8 s]`
>
> Thirty takes of one beat: a woman throws a phone over a railing into a river at night.
>
> | Start still | Takes | Strong throw | Phone clearly over the rail |
> | --- | --- | --- | --- |
> | Thrower already at the rail, back to camera, arm up with the phone, river filling the frame beyond | 6 | 2 | 3 (a fourth unclear) |
> | Thrower mid-walk facing camera, rail two metres away, river a strip at the frame edge, a glass in her other hand | 18 | 0 | 0 usable |
> | Six new angles, four with the phone already in the air | 6 | 0 | 2 or 3 (it falls; nobody throws it) |
>
> - **Put the thrower where the throw ends up needing her:** at the barrier, facing the target, the target large
>   in frame beyond it, the arm already raised. The throw is then the next thing that happens.
> - **Start the still before the action the shot is for.** A still with the object already in the air has no
>   throw in it. "Start the still where the clip must end" (`flow.md`) is about where a face points, not about
>   an action.
> - **A lit, pale object thrown away from the camera can stay in frame.** Its half-second arc held in 3 of 6
>   takes, and one drew a full splash unasked. This bounds "a real camera never catches the whole fall": that
>   rule came from a dark object dropped across the frame on the first Omni. Still expect one take in three.
> - **Two props in two free hands swap or double when the person is given several things to do.** Phone in one
>   raised hand, wine glass in the other, five actions in the prompt: the glass changed hands or a second one
>   appeared in the 12 takes of r11 to r14, by 3.5 s at the latest. **What held it:** one action only, and the
>   second prop's hand named and parked ("her left hand stays at her hip with the glass, the whole time"): one
>   glass in the same hand in 6 of 6.
> - **Keep the wind-up in the words.** "Already has her arm raised… snaps that arm forward" gave a wrist flick in
>   6 of 6; "swings her arm back and flings" gave the full-body throws.
> - **Scenery held when it was not mentioned.** The railing was never named in the 84-word prompt and did not
>   move in six takes. Naming it as fixed in a 136-word prompt did not help. (The still differed too, so this is
>   not a clean test.)
> - **The same still and words give very different takes:** of six, two strong throws, two lobs straight up, two
>   thrown sideways onto the deck. Roll at least six before judging a recipe.

### c. `docs/rules/flow.md`, section "Video model: Omni 1.2 Flash": the "untested" list is out of date

Proposed line to replace "Untested on 1.2: start+end frame, cast Characters, 'Do not X' phrasing":

> On 1.2 as of 2026-11-27: a cast Character runs in Frames mode (Karen, six takes); props swap hands or double
> when one person holds two in free hands and has several things to do (Karen, 12 takes), and hold when the
> second hand is named and parked (6 of 6); a splash and a short thrown arc can come out right. Still
> untested: start+end frame; a clean A/B of "Do not X" phrasing.

### d. `docs/rules/flow.md`: two working rules, proposed

> ## Three failed takes: change the picture, not the words
>
> When three takes of one still and prompt fail the same way, stop re-rolling and stop adding sentences. Change
> the start still or the shot. Karen's throw took 18 takes from a still that could not hold it, with a prompt
> that grew from 84 to 136 words, before the original still was tried again. The rewrites did fix one thing (the
> glass), which hid that the picture was the problem.
>
> ## Every re-roll round carries two takes of the last recipe that worked
>
> Same still, same words, same Character, same settings. If they still work, the model has not changed and the
> fault is in what we changed. On Karen's throw this would have answered "did the model regress?" on the first
> day instead of the fourth.

### e. `docs/rules/flow.md`, "Omni Flash video defaults": 720p next to 1080p

The rule says upscale to 1080p only for delivery. Jack's older clips in the Karen cut are 1080p and the new ones
are 720p. Proposed addition, **if the free check in section 2 bears it out**:

> A new clip that sits beside 1080p clips in a cut gets Flow's free 1080p upscale before it goes on the
> timeline. Kai called two 720p river clips "low quality" between 1080p neighbours (Karen, r7 and r11).

### f. `docs/rules/working.md`: reading "go back to the one before"

> When a note says to go back to the earlier shot and re-cut that, the next round's first job is re-rolls of the
> earlier recipe exactly as it was. Kai asked for this on the Karen throw in r12; it was done in r15.

### g. The story's `badcode.md`

It still says the cut keeps r14 take 6 and that "the throw is open". Once Kai picks, it needs the pick, and one
line for the story's own rules: "The river throw starts from `river-shout-b` (Karen at the rail, her back to
us). Never from a still where she faces the camera."
