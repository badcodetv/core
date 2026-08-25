---
story: karen
kind: brief — written in-repo, fired by hand; each block is the deliverable
engine: Nano Banana Pro (plates) → Gemini Omni Flash (clips)
flow_project: TODO — exact project name as it appears in Flow
updated: 2026-08-18
---

# Karen — Act 3, Viral

Plate and clip prompts for the act where the world finds out and **she never leaves the box**.
[`story.md`](./story.md#act-3--viral-aarron-the-train-the-crowd) §Act 3. Section numbers run at
**§3a**.

> ## 🖐 A brief, not a record
>
> Same standing as the other scene briefs: [`prompts.md`](./prompts.md) is the **ledger**, this
> is not one. It inherits the conventions — the casting rule (`**Cast:** @Karen` — never
> describe a face), no legible text, one reference maximum, and the closing *"Thanks."*
>
> **Fired by hand, not by the automation** (Kai, 2026-08-16).
>
> ### ⚠️ Every prompt ends with *"Thanks."* — plates and clips alike
>
> The last line of every block pasted into Flow is `Thanks.` on its own line, images and videos
> both. Where a prompt is pasted as two blocks, only the **final** block carries it.
>
> ### Clip duration: **8s** (Kai, 2026-08-18) — the clips get narrated.
>
> **Engine research does not live here** — it goes to
> [`docs/google-flow/`](../../google-flow/README.md).

---

## ⚠️ What makes this act hard: it is the first act with two people in it

Acts 1 and 2 are a woman alone. **Act 3 puts Aarron next to her, then a crowd.** That runs
straight into the hardest limit we have found:

> **Two figures in relative motion interpenetrate**, and it is not fixable by prompting. Karen
> §2h.7v tried letting two pedestrians exit the frame (they merged), then asked them to hold
> order and spacing (they merged), and was only fixed by **removing them from the picture inside
> the first second**. [The full finding](../../google-flow/omni-flash.md).

**The threshold is precise, and it is what makes this act possible:** *two figures **in relative
motion***. A moving figure beside a still one is a single tracking problem and has held every
time. So:

| | Rule |
| --- | --- |
| **Plates** | Two people is fine. Interpenetration is a video failure, not an image one. |
| **Clips** | **Only one person may move.** Karen stands still while Aarron moves, or the reverse. Never both. |
| **The crowd (§3a.3)** | **Never animate a crowd.** It is many figures in relative motion — the failure mode at scale. The drone trick is cut between *stills*, which is what the storyboard already asks for. |

**This is not a compromise, it is the coverage.** A real film shoots a two-hander as singles and
cuts between them; the engine's limit is pushing us toward the edit we would have made anyway.

## The other standing rules, carried forward

0. **⚠️ Never describe a cast member's appearance** when their Character is attached — no
   clothes, no face, no build. The casting rule is in every character file; breaking it made
   Aarron a different man in every frame. **Describe the shot only.**
1. **One reference, described relations minimal** (Kai, 2026-08-18). Attach the canon corner
   [§2j.0](./prompts-act2-escalation.md#2j0-the-corner-with-karen-in-it--plate) and describe
   everything else. A second image costs more than a role label buys back.
2. **Never re-describe the reference.** *"Keep it exactly as it is"* then a numbered change-list;
   enumerating the set is an instruction to redraw it.
3. **Name where the photographer stands**, using a spot the reference contains. Abstract framings
   make the model build the space they need.
4. **Nothing in the atmosphere family gets named** — no dust, steam, haze or reflections. They
   render for free and overdeliver when asked for.
5. **Whatever the shot is *for* leads its own sentence**, with a duration attached.

---

## 3a.0 He walks towards the camera — plate

**Cast:** `@Aarron`. **Attach:** the accepted **§2j.0** still as image 1 — **setting only.**
**One reference.** **Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### ✅ Kai's call: Aarron alone, the kiosk out of shot. It is the better beat as well as the safer one.
>
> **The sound arrives before the picture.** With Karen off-screen, the audience hears the
> shouting before they see her — **they discover her with him, at the same moment** — and his
> stop is motivated by something we can hear and cannot see. The cut to §3a.1's two-shot is then
> a reveal instead of a repeat.
>
> **And it removes the act's hardest constraint from this shot entirely.** One figure in frame
> means no [two-figures-in-relative-motion](../../google-flow/omni-flash.md) problem for the clip
> that follows, and no way for Karen to wander into a shot she is not supposed to be in.
>
> **Camera behind the kiosk, back turned to it**, so she is not merely out of frame but behind
> the lens. That is a geometry the model cannot accidentally undo.

> ### ⚠️ Round 1 fired 2026-08-18 — the camera and the staging landed, the street did not.
>
> Kai: *"use this for the setting, making it match more; keep the camera angle and his
> positioning."* Round 1 came back as **an open intersection with a wide crossing and a large
> pale panel** where the canon corner is a **narrow side street between tall blocks** with
> plywood hoarding on the scaffolding.
>
> **Third time this exact drift has happened** — §2h.7 built a plaza, §3a.0's earlier version put
> a man in a road, and now this. The pattern is the same:
> [the set gives way to whatever the shot requires](../../google-flow/nano-banana-2.md), and a
> camera looking *down a street* invites the model to open the street up so there is something to
> look down. **The counter is to state the street's character as a fact**, the way §2h.7 was
> fixed: *"a narrow side street between tall blocks, not an open intersection or a plaza."*
>
> **The camera and his position are described in words, not carried by a second image** — Kai's
> standing rule, and it worked cleanly last round: the framing came back right, only the world
> was wrong.

> ### ⚠️ Round 2, 2026-08-18 — *"remove the scaffolding poles, they are not consistent with §2j.0."*
>
> **The word had to go from the keep-list, not just from the shot.** §2j.0 does have pavement
> scaffolding, so *"the same pavement scaffolding with plywood hoarding"* was sitting in the
> setting clause **inviting poles into every frame** — and what came back was a sculptural tangle
> that matches nothing. **This block of pavement simply does not have it.** Round 3 does not use
> the word at all.
>
> **That costs the frame its foreground occluder**, which is a real
> [anti-slop lever](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit-community) — depth
> comes from something close and out of focus. **Nothing replaces it this round, deliberately:**
> the guidance is not to change two things at once, and Kai's note was about the poles only. **If
> the frame reads flat**, the canon-consistent replacement is the nearest green globe post at the
> right edge, close and out of focus — one sentence, next round.

```prompt
Image 1 is the reference for the setting only. Keep the street exactly as it is — the same narrow Midtown side street, the same subway entrance with its steel railings and green glass globes on their posts, the same shopfronts and awnings, the same paving, the same flat overcast mid-morning light and the same grainy super-8 film look. It is a narrow side street running between tall blocks, not an open intersection and not a plaza. Redesign nothing about the street.

The phone kiosk and the woman are not in this shot. The camera is standing on the pavement in the block behind the kiosk with its back to the kiosk, looking away down the street, so the kiosk is out of shot behind the camera.

The shot: a young man walking straight towards the camera down the middle of the pavement, on an 85mm lens at f/2.8, framed from chest height with his whole body in frame from his head to his shoes. He is about eighteen feet away, dead centre, caught mid-stride with one foot off the ground. The subway entrance runs along the right-hand side of the frame in the middle distance, and the buildings on both sides come close enough to fill the frame from edge to edge behind him. He is sharp and everything behind him is soft.

He is wearing his rig, his hands are down by his sides and his phone is in his pocket. He is looking straight ahead past the camera, not at anything in particular.

He is the only person in the frame and the pavement is empty behind him. Natural skin texture with visible pores. No readable lettering anywhere. No border around the image.

Thanks.
```

**What to watch:**

1. **Are the poles gone?** The round-2 note. No scaffolding anywhere in the frame — the word is
   no longer in the prompt at all, which is the actual fix.
2. **Is it a narrow side street?** The round-1 failure. Tall blocks close on both sides, no wide
   crossing and no plaza. The edge-to-edge clause is now doing that job as well as replacing the
   lost foreground.
3. **Is he alone, with no kiosk?** Nobody else on the pavement, and no phone box anywhere.
4. **Hands empty, phone in pocket?** Still the most important detail in the cameo — he gets it
   out *because of what he hears*, and the audience only feels that if they saw it put away.
5. **Same camera and position?** Dead centre, full body, chest height, 85mm. That part has
   worked twice and should not move.
6. **Is he mid-stride?** A standing figure reads as arrived; this shot exists to show him passing
   through.

> ### The clip that follows
>
> **§3a.0v carries him from here to the stop.** He keeps walking towards the camera, slows, and
> his head turns off-screen towards the sound. **One mover, locked camera, and Karen is audio
> only** — the whole reveal happens on his face.

## 3a.0b He walks along the pavement — plate `[accepted 2026-08-18]`

**Superseded as the opening frame by §3a.0**, but accepted and worth keeping: it is the middle of
the walk, and a usable alternate if the crossing turns out to be too far away to read.

> ### ⚠️ The headphones stay on, and no beat touches them.
>
> A man in over-ear headphones hearing a woman shout is a small logic problem, and the tempting
> fix — **he lifts one cup off his ear** — is a lovely beat that **breaks continuity with the
> accepted §3a.1 still**, where both cups are on. Not worth it. She is shouting at the top of her
> voice on an empty street. **The "he heard it" moment is carried by his head turning and by the
> narrator's line.**

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman in the kiosk, her clothes, the flat overcast mid-morning light, and the grainy super-8 film look. Redesign nothing.

Change three things:

1. A wide shot of the whole corner on a 50mm lens at f/5.6, taken from the pavement about thirty feet away at chest height, with the kiosk on the left of the frame and the subway entrance and the pavement beyond it running away to the right.

2. The woman is in the kiosk on the left, closest to the camera, with the receiver at her ear, her mouth open in mid-shout and her free hand out in front of her off the shelf.

3. A young man is walking along the pavement on the right, past the subway entrance and towards the kiosk, caught mid-stride with one foot off the ground. He is wearing his rig, his hands are down by his sides and his phone is in his pocket. He is looking straight ahead along the pavement, not at her, and he has not noticed her.

The pavement is otherwise empty. Natural skin texture with visible pores. No readable lettering anywhere. No border around the image.

Thanks.
```

## 3a.1 The sample — plate

**Cast:** `@Aarron`. **Attach:** the accepted **§2j.0** still as image 1. **One reference.**
**Time:** flat overcast mid-morning. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### Five seconds, and the whole film turns on them.
>
> [`story.md`](./story.md#31-the-aarron-cameo--redo-five-seconds-total): *"Aarron happens to
> wander past the phone box — **he is not looking for anything.**"* The narrator's line is
> *"Aarron just heard a great sample."*
>
> **The believable version is the accidental one**, and the canon says so twice — *resist making
> him part of the attraction.* So this is not a hero shot of a young producer discovering a
> star. **It is a man who has stopped walking.**

> ### ⚠️ Rounds 1 and 2, 2026-08-18. **Aarron kept changing, and the cause was in this file's own rules.**
>
> **I described him.** Both rounds said *"a hoodie, a jacket and trainers with a small backpack
> on one shoulder."* [`characters/aarron.md`](./characters/aarron.md#flow-character) forbids
> exactly that:
>
> > **Casting rule:** these prompts are never pasted into a scene prompt. Scene blocks say
> > `**Cast:** @Aarron` and describe the shot only — **a face described in prose competes with
> > the Character binding instead of reinforcing it.**
>
> **And the description was wrong as well as forbidden.** His canon look is a **patterned
> crewneck sweater** and the **wearable rig** — harness, chest-mounted keyboard, over-ear
> headphones, a shoulder mic, real straps and cables. A hoodie and a backpack is a different
> young man, described twice, in two different sets of words. **The prose was not merely
> competing with the Character; it was overruling it with a stranger.**
>
> **Why Karen never drifts, by contrast:** her face is never described, *and* she is in the
> attached reference still as well as the Character. **Two sources agreeing.** Aarron had one
> source being argued with.
>
> ### ✅ The rig is the identification, which is why over-the-shoulder works.
>
> His file: *"the wearable rig **is** the character — it is what makes him legible as a roaming
> street producer in a single frame, so the harness, keyboard, mic and cables are load-bearing,
> not costume detail."*
>
> **So Kai's framing solves the likeness problem from the other end.** Round 1 failed from behind
> because there was no face *and* no rig — nothing to recognise. **From behind with the rig on,
> he is unmistakable**, and we get the over-the-shoulder that puts Karen where she belongs: in
> front of the camera, sharp, being watched.
>
> **He stays on the pavement.** Round 2 put him in the road. Stated outright, because the corner
> has a kerb and the model will use the road as free space if nothing stops it.

> ### ⚠️ Round 3, 2026-08-18 — ✅ the Character bound, ⛔ I had been misreading the note.
>
> **Dropping the clothing description worked immediately.** He came back in the patterned
> crewneck with the headphones and his own hair — the first time `@Aarron` has actually appeared
> in this film. **That rule is settled and is not to be broken again.**
>
> **The composition note was mine to get wrong three times.** Kai has said *"behind and to the
> side"*, then *"he should be behind her looking at her, next to the subway entrance."* I read
> the first two as **camera** instructions — put the lens behind him — when they were always
> **staging** instructions: *where Aarron stands in the world.*
>
> **He is a figure in the background.** The camera stays on Karen's side of the corner; he is
> beyond her, by the subway railings, watching. That is what makes the cameo accidental — a man
> who happens to be standing there — rather than a scene about a man with a phone.
>
> ### Naming the spot fixes the road problem too.
>
> Round 2 put him in the road because *"further down the pavement"* is a direction, not a place,
> and the model treats unclaimed space as free. **"Standing on the pavement beside the subway
> entrance railings, between the kiosk and the green globe posts"** is a spot that exists in the
> reference and can be checked against it — the same fix as
> [naming where the photographer stands](../../google-flow/nano-banana-2.md#3c--name-where-the-photographer-stands-not-what-the-shot-looks-like),
> applied to a subject instead of a camera.

**The angle: a 135mm three-quarter from the side.** Long enough to keep Act 3's
watched-from-a-distance language and to **stack him up close behind her** while he stands ten or
fifteen feet further back — which is exactly the composition the note asks for. Off-axis rather
than dead-on, because the straight-on front of the kiosk is spent. Prompt order follows the
convention: **angle → lens → composition**.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman in the kiosk, her clothes, the flat overcast mid-morning light, and the grainy super-8 film look. Redesign nothing.

Change three things:

1. A three-quarter shot from the side of the kiosk on a 135mm lens at f/5.6, taken from the pavement about twenty feet away at chest height, so the kiosk, the subway entrance and the block behind them are compressed and stacked up close together. Everything in the frame is in focus.

2. The woman is in the kiosk in the left half of the frame, closest to the camera, with the receiver at her ear, her mouth open in mid-shout and her free hand out in front of her off the shelf. She does not know anyone is watching her.

3. A young man has stopped ten or fifteen feet behind her, standing on the pavement beside the subway entrance railings between the kiosk and the green globe posts, well back from the kerb. He is wearing his rig and holding his phone up in both hands to film her, and he is facing her, so his face is turned towards the camera and clearly visible. He is smaller in the frame than she is.

The pavement is otherwise empty. Natural skin texture with visible pores. No readable lettering anywhere, and nothing readable on the phone screen. No border around the image.

Thanks.
```

**What to watch:**

1. **Is he behind her, by the railings?** The note, three rounds running. He should be a smaller
   figure in the background beside the subway entrance — **not** a foreground presence, and not
   in the road.
2. **Is she the nearest and largest thing in frame?** The canon forbids making him part of the
   attraction twice over. She is the subject; he is a man who happened to stop.
3. **Does the rig read?** Headphones, harness, the chest-mounted keyboard, the shoulder mic. With
   no clothing in the prompt the Character supplies all of it — round 3 proved that works.
4. **Is it compressed?** 135mm should stack the block up behind the kiosk. A wide-looking frame
   means the lens instruction lost.
5. **Blank phone screen, mouth open.** The screen is where text and policy blocks come from; the
   shout is what the narrator's line sits on.

> ### ⚠️ Standing rule, relearned the hard way
>
> **Never describe a cast member's clothes, face or build in a scene prompt** when their
> Character is attached. It is written in every character file and it was still worth two
> generations to relearn. **The shot only** — where they are, what they are doing, where the
> camera is.

## 3a.1v The sample — clip

**Cast:** none — **Frames takes no Character.** **Attach:** the accepted §3a.1 still as the
**starting frame**. **Engine:** Gemini Omni Flash · **Frames to Video** · 8s · native audio ·
**Enhance Prompt off**.

**Tab: Frames.** Two faces and a set full of thin geometry — railings, green globes, the straps
and cables of the rig. **Ingredients would re-stage all of it**, and it took four rounds to get
this staging. Frames pins frame 0, and with both subjects nearly static there is very little
runway for identity to drift.

> ### The act's rule bites, and the funniest version is also the safest one.
>
> **Only one person may move** — [two figures in relative motion
> interpenetrate](../../google-flow/omni-flash.md), and no prompt fixes it. Here that costs
> nothing, because **the joke is that he does not react much.** She is exploding at a stranger on
> the end of a phone; he is standing on a pavement quietly recording it. **Stillness is funnier
> than a reaction**, and it is what a real person filming something on their phone actually does.
>
> **His feet never move.** The rule is about *relative* motion, so a planted figure beside a
> gesturing one is one tracking problem, not two. **The one thing he is allowed is his face** —
> facial motion on a static body has never failed here, and *"oh sh—"*, the canon beat, is a
> small grin arriving as he works out what he has got.

**The traffic is frozen and lives in the audio.** Vehicles have failed three times in this film
and the [demote-to-sound fix is four for four](../../google-flow/omni-flash.md#demote-it-to-sound).
Parked cars holding still is a much smaller lie than cars driving through each other.

> ### ⚠️ Her line is not in this clip, on purpose.
>
> Canon gives her *"I've got ALL DAY to complain — all day to complain!"* and **that line is the
> hook of the song** — it wants to arrive as the record, laid in at the edit, not as whatever
> Omni's native audio invents. So the block asks for **a raised voice with the words unclear**.
>
> **If Kai wants to gamble on hearing it**, swap the audio clause for *"a woman shouting 'I've
> got all day to complain' at the top of her voice"* — but expect the
> [audio lottery](./prompts-morning-after.md#2h6v-karen-listens-in-the-kiosk--clip): wrong words
> come back as often as right ones, and re-rolling is the only fix.

```prompt
Use the attached image as the starting frame. One continuous shot.

The camera does not move.

She is mid-rant and stays mid-rant for the whole eight seconds. Her mouth moves continuously, her free hand moves as she talks, and she leans a little towards the phone and back again. She stays in the kiosk with the receiver at her ear and she never looks away from the street in front of her. She does not notice the young man.

He stays exactly where he is on the pavement, standing still with his phone held up in both hands, filming her. His feet do not move and he does not walk. The only thing that changes about him is his face: a small delighted smile arrives as he works out what he is recording.

Everything else in the frame holds still. The kiosk, the railings, the green globe posts, the straps and cables on his rig, her handbag and the parked cars all stay exactly where they are and exactly as they are, and the pavement stays empty apart from the two of them.

Real-time pace, 24fps with a 180-degree shutter. Fine film grain.

Audio is the street: a woman's voice raised and carrying but not clear enough to make out the words, traffic, and the rumble of a train under the pavement. No other dialogue.

Thanks.
```

**What to watch:**

1. **Does he stay planted?** The one thing that would break it. If he walks, drifts or turns, the
   two of them become two moving figures and the failure is the one nothing fixes — **cut the
   smile and give him nothing at all** on the next pass.
2. **Do the rig's cables and the railings hold?** The most fragile geometry in the frame, and the
   reason this is on Frames rather than Ingredients.
3. **Is she actually ranting the whole time?** Her mouth moving from first frame to last. It
   leads its own sentence for exactly that reason.
4. **Do the parked cars stay parked?** Frozen traffic is the deliberate choice; cars driving
   through each other is the failure it avoids.
5. **Does he look at the camera?** He must not. He is looking at his phone screen, and she never
   looks at anything but the street.

## 3a.2 Karen shouts the line — three ways

**The line is the hook of the song**, so this beat gets covered three times rather than once and
the edit picks. Kai's call, 2026-08-18. All three are **her single** — Aarron is not in frame,
which costs nothing in continuity because **this is the shout he is still walking towards.**

| § | Shot | Why |
| --- | --- | --- |
| **3a.2a** | Long lens from across the street, paparazzi grammar | *she is being watched now*, made literal |
| **3a.2b** | Through the side panel, her face broken by the glass | the "we watch her through things" motif, and she is about to be split into millions of copies |
| **3a.2c** | The phone-screen version — Aarron's actual recording | the artefact itself; Act 3's formal device |

### 3a.2a Across the street — plate

**Cast:** `@Karen`. **Attach:** the accepted **§2j.0** still as image 1 — **one reference.**
**Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### ⚠️ Rounds 1–4 all failed, plus a location turnaround. The diagnosis was wrong every time.
>
> | Round | Approach | Result |
> | --- | --- | --- |
> | 1 | *"from the opposite pavement, across the road"* | stayed on the near pavement |
> | 2 | moved the camera back to the same pavement | correct, and not what was asked for |
> | 3 | named the road and crosswalk in the foreground | camera dropped into the middle of the road |
> | 4 | stated the near-to-far stacking order | flipped the subway entrance to the wrong side |
> | §2j.0t | a three-panel location turnaround, to build the far side as canon | the kiosk came back redesigned in all three panels |
>
> **The error was treating this as a geometry problem.** Every round tried harder to specify a
> corner the reference has never seen — and
> [a reference wins ties](./prompts-act2-escalation.md#2j11-she-is-alone-in-it--plate), so each
> attempt bought more invented street rather than less.
>
> ### ✅ The fix: at this focal length **the setting is a blur**, so stop asking for it.
>
> A real 200mm wide open from a hundred feet renders **the subject sharp and everything else to
> mush.** That is the actual look being chased — and it means **the corner's accuracy stops
> mattering**, because there is no corner in the picture. Only Karen and the kiosk around her
> need to be right, and both are things the reference *does* contain.
>
> **The road stops being geometry and becomes a grey blur across the bottom of the frame.** That
> is what says *across the street*, and a blur cannot be drawn wrong.
>
> ### Two more corrections from the research
>
> - **Natural language beats technical specification.** Testing found *"a telephone with a shallow
>   depth of field"* outperformed f-stops and focal lengths, because these models parse
>   description better than camera data. **The block below says *"a long-lens photograph taken
>   from a long way off"* instead of *"200mm at f/2.8."***
> - **Describe what is visible, not where the camera stands.** The documented camera form is
>   *"[shot type] of image 1"* with the reference carrying the rest — and every round here got
>   longer while getting further from the target.

```prompt
Image 1 is the reference. Keep the same phone kiosk exactly as it is — the same scuffed aluminium frame, the same chipped paint and rust, the same glazed sides and steel shelf — and the same woman, the same clothes, the same flat overcast light and the same grainy super-8 film look.

A long-lens photograph of her taken from a long way off, as if by somebody watching her from across the street. She is in the kiosk with the receiver at her ear, caught at the top of a shout with her mouth wide open and her free hand thrown out in front of her.

Only she and the kiosk around her are sharp. Everything else is thrown completely out of focus: the road in the foreground is a soft grey blur across the bottom of the frame, and the whole street behind her is a wash of soft shapes with no detail in it. The frame is a few degrees off level and the kiosk sits right of centre.

She is the only person in the frame. Natural skin texture with visible pores and shine. No readable lettering anywhere. No border around the image.

Thanks.
```

**What to watch:**

1. **Is everything except her genuinely soft?** The whole point. **If the street behind her comes
   back detailed, the shot is back to being a geometry problem** — and the lever is more blur, not
   more description: *"the background is unrecognisable, just soft shapes and colour."*
2. **Is the kiosk right?** It is now the only thing in frame that has to match, which is the
   entire reason this approach should work.
3. **Is there a grey blur along the bottom?** That is the road, and it is what says the camera is
   on the other side of it.
4. **Is she at the top of the shout?** Mouth wide open. The line is the hook of the song.

> **If this fails too, stop.** [§3a.2c](#3a2c-the-phone-screen-version--plate) already covers
> *she is being watched* — literally, and as the artefact rather than the metaphor. Four seconds
> of screen time does not owe us five rounds.

### 3a.2b Through the side panel — plate

**Cast:** `@Karen`. **Attach:** the accepted **§2j.0** still as image 1 — **setting only, one
reference.** **Time:** flat overcast mid-morning. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### The frame member cuts her face in two, at the moment she is about to be copied a million times.
>
> **The metaphor is free and it is never said out loud.** She is seconds from being cut up,
> sampled, looped and reposted; the shot puts a hard aluminium edge straight down the middle of
> her face. Nobody has to notice for it to work — **and if anyone asks, it is just where the
> kiosk's upright happens to be.**
>
> It also continues the motif [§2h.6](./prompts-morning-after.md#2h6-the-news-lands--plate--re-fired-against-the-canon-kiosk)
> started: **we watch her through things.** Through glass, across a pavement, from a helicopter,
> from a room she is not allowed into — and now through a scratched panel with a bar across her
> face.

**How this differs from §2h.6, which is the same panel:** that one is a clean profile with a soft
background and nothing crossing her. **This is much closer, and the frame members are the
subject.** If it comes back looking like §2h.6 it has failed, however pretty it is.

> ### ⚠️ Glass rules, learned over three rounds on §2h.6
>
> 1. **Never name a reflection.** [Atmosphere renders for
>    free](../../google-flow/nano-banana-2.md) and overdelivers the moment it is asked for — a
>    named reflection came back as a double exposure smeared over her face. **Only the geometry
>    and the surface get described**: the upright, the frame member, the scratches, the chipped
>    paint. Whatever the panel does with the light on its own is a bonus.
> 2. **State that the front is open.** A shot that needs glass invites the model to build glass;
>    saying *"no door and no glass across the front"* is what stopped it growing one.
> 3. **Name what stays sharp.** A subject inside something transparent stacks every available
>    layer unless one is nominated — *"only her face is sharp"* is what collapses them back into a
>    photograph.

```prompt
Image 1 is the reference for the setting. Keep the kiosk exactly as it is and redesign nothing about it: the same scuffed aluminium frame, the same chipped paint and rust, the same glazed side panels, the same worn steel shelf and coiled handset cord, the same flat overcast mid-morning light and the same grainy super-8 film look. The front of the kiosk is open, with no door and no glass across it, exactly as in image 1.

The shot is a tight close-up taken from the pavement at the side of the kiosk, right up against the glazed side panel, on a 50mm lens at f/2 at her eye level. She is seen through that panel and fills most of the frame. The kiosk's aluminium upright runs vertically down the frame and across her face, cutting it in two, and a horizontal frame member crosses below her chin. The glass she is seen through is old, scratched and grubby, with chipped paint along the edges of the frame. Only her face is sharp; the open front of the kiosk and the street beyond it fall away soft behind her.

She is caught at the top of a shout, mouth wide open, the receiver hard against her ear. Her eyes are fixed on nothing out in the street and she does not know the camera is there.

She is the only person in the frame. Natural skin texture with visible pores and shine. No readable lettering anywhere. No border around the image.

Thanks.
```

**What to watch:**

1. **Does the upright actually cross her face?** The entire idea. If it sits beside her head
   instead, the shot is just a close-up through glass — the consequence to add is *"the upright
   passes over her nose and mouth."*
2. **Is her face clean of ghosting?** No double exposure, no smeared street laid over her.
   Reflections *in* the panel are fine; a reflection *over* her is the round-2 failure from §2h.6.
3. **Did it grow a door?** The front stays open.
4. **Is only her sharp?** If the street behind is as crisp as her face, the layers have stacked
   again.
5. **Is it much closer than §2h.6?** She should fill the frame. Same distance means we have made
   the same shot twice.

### 3a.2c The phone-screen version — plate

**Cast:** `@Karen`. **Attach:** the accepted **§2j.0** still as image 1 — **setting only, one
reference.** **Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### This is the artefact. Everything else in the act is about it; this is it.
>
> Twenty million people are about to watch **this exact picture**, and the film has never shown
> it. **It also gives Act 3 a formal device of its own** — the way the aerial belonged to Act 2 —
> and it is the one frame here that can be lifted verbatim into the music video and the social
> cuts, because in-world it is a real object rather than a shot of one.

> ### ⚠️ The `STYLE LOCK` is deliberately **off** for this plate. It is the only one.
>
> Every other frame in this film is super-8: grain, halation, soft edges, shallow focus. **A
> phone camera is the exact opposite** — deep focus front to back, over-sharpened, digital noise
> in the shadows, blown highlights, careless framing. **That contrast is the whole point.** If it
> comes back looking like the rest of the film, the device has failed and it is just another shot
> of Karen.
>
> **So the keep-list carries the street and explicitly not the look**, which is a first for this
> project: *"do not use image 1's film look."*

**The thumb is the realism token.** Everything else could be faked; a thumb sliding over the
corner of the lens is what nobody stages. It does the job that
[grain and imperfect framing](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit-community)
do everywhere else.

**⚠️ No interface, anywhere.** We are **inside** the recording, not looking at a phone, so there
is no reason for a timer, a record button or a battery icon — and
[legible on-screen text is both our standing rule and the most reliable policy block there
is](../../flow/README.md). The block says so outright rather than trusting the absence.

**Vertical picture, black either side.** The output is still 16:9; the *content* is a portrait
video sitting in the middle of it. **This is the one plate where a border is wanted**, so the
usual *"no border"* clause is gone — deliberately, not by oversight.

```prompt
Image 1 is the reference for the setting only. Keep the street exactly as it is and redesign nothing about it: the same narrow Midtown side street, the same phone kiosk, the same subway entrance behind it with its dark green railings and green glass globes on cast-iron posts, the same pre-war masonry, the same paving and the same flat overcast mid-morning light.

Do not use image 1's film look. This picture is modern phone video, not film.

The frame is 16:9 and mostly plain black. In the middle of it stands a tall vertical video picture about half the width of the frame, with plain black on either side of it.

Inside that vertical picture: the woman in the kiosk, filmed on a phone from about fifteen feet away along the pavement, handheld. Everything in the picture is in focus from front to back. It looks exactly like modern phone footage — bright, over-sharpened, a little noisy in the shadows, with the white sky blown out to pure white. The framing is careless: she is off to one side, the horizon is tilted, and the tip of a thumb intrudes over the bottom right corner of the picture, dark and out of focus.

She is caught at the top of a shout, mouth wide open, the receiver hard against her ear and her free hand thrown out in front of her. She has no idea she is being filmed.

She is the only person in the vertical picture. Natural skin texture. Keep every sign, notice, hoarding and shopfront free of readable lettering, and keep the picture free of any icons, buttons, timers or on-screen markings.

Thanks.
```

**What to watch:**

1. **Does it look like phone footage, or like our film?** Deep focus, sharp, bright, blown sky.
   **Any grain, halation or shallow focus means the register break failed** — and this shot is
   worth nothing without it.
2. **Is the picture vertical, with black either side?** The one plate where the bars are the
   design.
3. **Is the frame careless?** Tilted, her off to one side. A well-composed phone video is a
   contradiction and reads instantly as fake.
4. **Is the thumb there, and is it a thumb?** Bottom right, dark, out of focus. It is the single
   most convincing detail available.
5. **Any interface at all?** A timer, a red dot, a battery icon — reject. Text is the standing
   rule and the most common policy block.

## 3a.3 The train — plate

**Cast:** none — **no Characters exist for these two, and none should.** **Attached:** nothing.
**Engine:** Nano Banana Pro, 16:9, 3 candidates. **Register:** super-8 `STYLE LOCK`.

> ### The joke of the act: the tune went stratospheric and she never left the box.
>
> [`story.md`](./story.md#32-the-train--keep-as-is-play-the-real-tune): two riders listening to
> **our actual song, in-world.** *"You heard this Karen tune? It's gone viral."* — *"She's still
> there. The phone-box lady. Still. There."*
>
> **The whole act turns on this being ordinary.** Nobody is impressed, nobody is reporting it;
> two people on a train are just passing on a thing they heard. **The idea travelled because it
> became a song, not a speech** — which is BadCode's thesis, and this is the only frame that
> states it.

> ### ⚠️ Two rulings this shot needs
>
> **1. No Flow Characters for these two.** They appear here and again in
> [§3a.4](#what-this-act-still-owes) as the first two people in the crowd, and **canon says their
> role ends there.** Two Characters, two reference sets and two more likenesses to police is a
> lot of machinery for four seconds — so instead, **shoot §3a.4 wide enough that their faces do
> not have to match.** Cheaper, and the crowd wants to be wide anyway.
>
> **2. ⚠️ *"Mate"* is a Britishism and it is in the canon line.** Nobody on the A train says
> *"Mate. She's still there."* The
> [standing audit](./prompts-act2-escalation.md#2j7-rung-2-interior--the-borough-office--plate)
> that caught *"car park"* and buff folders catches this too. **Kai's call** — the American
> versions are *"Bro. She's still there."* or *"Dude. She's still there."* — but it should be
> fixed in `story.md` rather than silently in a prompt.

**The phone screen is the key light**, and that is the choice that saves the shot. Real subway
lighting is flat overhead fluorescent, which is
[exactly the light that erases skin texture](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit-community)
and made §2j.5's receptionist look like stock photography. **Lighting their faces from below off
the screen they are both looking at is both motivated and directional** — one named source, doing
story work.

**Sharing a single pair of wired earbuds** is the clearest possible picture of *two people
hearing the same thing*, and wired is a deliberate period-correct nuisance: it forces them to sit
close.

**⚠️ A subway car is the most text-dense location in the film** — maps, ads, door notices, route
strips. Every one gets blanked, and the phone screen with it.

```prompt
STYLE LOCK (keep identical every time):

Capture look only (NOT time period): cinestyle 800+, grainy, super 8, vintage, polaroid, vibrant colours — apply only as film-emulation texture/color, while the depicted world remains present-day.

Present-day constraint: modern clothing, modern vehicles, modern architecture, contemporary street design and signage; no retro/period props or era-specific styling.

Texture: visible film grain, slight gate-weave/micro-jitter feel, occasional dust/specks, gentle halation around bright highlights.

Color: punchy, vibrant palette with warm skin tones; mild film-like color cast; deep but soft blacks (not HDR).

Optics: slightly soft edges, mild vignetting, shallow-to-moderate depth of field; highlights bloom subtly (not foggy).

Exposure: preserve highlight detail; avoid crushed shadows; keep the main subject readable.

Output: high detail, natural imperfections, candid snapshot energy.

Exclusions: no added text, no logos, no watermark, no AI "hyper-sharp HDR" look, no historical setting/era shift.

SCENE:

Subject: two men in their twenties sitting side by side on a subway bench, sharing a single pair of wired earbuds, listening to something on one of their phones.

Composition: 16:9 on a 40mm lens at f/2.8, from the bench seat directly opposite them at seated eye level. They fill the middle of the frame with the car window behind them; a vertical stainless steel grab pole crosses the near left of the frame close to the lens and out of focus; the frame is slightly off level.

Action: the one holding the phone is turned towards the other and is mid-sentence; the other is looking down at the screen with his eyebrows raised. Neither of them is aware of the camera.

Location: the inside of a New York subway car — moulded plastic bench seats, brushed stainless steel panelling, vertical grab poles and overhead rails, a scuffed floor, a strip light along the ceiling, and the dark tunnel wall going past the window behind them. The car is otherwise almost empty.

Light: the phone screen lights both their faces from below, cold and slightly blue. The ceiling strip light is weaker and flat above them. The window behind them is dark with tunnel lights smearing past.

Style: a still from a 35mm independent film — two strangers, overheard. Available light only, unretouched, natural skin texture with visible pores and shine.

Constraints: keep every sign, route map, notice, advertisement, sticker and the phone screen free of readable lettering; no border or frame edge around the image.
```

**What to watch:**

1. **Is the phone lighting their faces?** The whole reason this is not a flat fluorescent
   nothing-shot. If their faces are lit from above, the light instruction lost and the frame will
   look like stock photography.
2. **Are they sharing one set of earbuds?** One wire, two ears. It is the single image that says
   *they are both hearing this.*
3. **Is anything readable?** A subway car is the most text-dense place in the film. Maps and ads
   are where it will creep back.
4. **Is the car nearly empty?** More riders means more faces to hold and, for the clip, more
   figures in relative motion.
5. **Do they look ordinary?** Nobody is performing amazement. Two people passing on something
   they heard.

## What this act still owes

> ### ⚠️ Gap found 2026-08-18 (Kai): the cameo was built middle-first.
>
> [`story.md` §3.1](./story.md#31-the-aarron-cameo--redo-five-seconds-total) has **four on-screen
> beats** and §3a.1 covers the third:
>
> | Canon beat | Piece |
> | --- | --- |
> | *"Aarron happens to wander past the phone box — he is not looking for anything"* | **§3a.0 — missing** |
> | *"Karen, mid-hold, shouts her line"* | **§3a.2 — planned, not written** |
> | *"Aarron stops, gets his phone out, records a few seconds"* | ✅ §3a.1 / §3a.1v |
> | *"— 'oh sh—' — and walks off"* | the *"oh sh—"* is §3a.1v's smile; **the walk-off is a ruling, below** |
>
> **§3a.0 is the load-bearing one.** He has to be **going somewhere else** before he stops.
> Without it he is a man standing at a phone box filming a woman, which reads as *intent* — and
> the canon warns twice that the believable version is the accidental one. **The walk is what
> makes it an accident.**
>
> **Ruling on the walk-off: cut away on the smile instead.** Canon's own line is *"we never see
> him again"*, and the cleanest way to say that is to not show him leaving. If it is wanted, the
> cheap version is a reverse from behind him walking away with the kiosk small behind — one
> mover, Karen static and tiny — but the cut is stronger and the cameo is only five seconds long.

| § | Piece | Notes |
| --- | --- | --- |
| **3a.0** | He walks towards the camera — plate | ✅ written, **round 3** — Aarron alone, kiosk behind the lens, no scaffolding |
| **3a.0b** | He walks along the pavement — plate | ✅ **accepted 2026-08-18** — the middle of the walk; kept as an alternate |
| 3a.0v | Crossing to the stop — clip | **only he moves**: up onto the pavement, along, slowing, head turning towards the kiosk |
| **3a.1** | The sample — plate | ✅ written, **round 4** — 135mm three-quarter; he stands by the subway railings behind her |
| **3a.1v** | The sample — clip | ✅ written — **only she moves**; he is planted and the one change is a smile |
| **3a.2a** | Across the street — plate | ✅ **accepted 2026-08-18** as the **dusk long exposure**, after ten rounds; see the ledger below |
| **3a.2a-v** | The dusk frame, moving — clip | ✅ **worked round 6** — *"continue that same timelapse"* |
| **3a.2b** | Through the side panel — plate | ✅ written — the upright cuts her face in two |
| **3a.2c** | The phone-screen version — plate | ✅ written — **`STYLE LOCK` off**, the only plate in the film without it |

| **3a.3** | The train — plate | ✅ written — phone-screen key light, one set of earbuds between them |
| **3a.4** | The crowd — the drone trick | ⏭ **next** — **stills only, cut between.** Altitude up/down, the crowd bigger each time. Never animated. |
| 3a.5 | News vans | the end of the act; the world has arrived and she is still on hold |


---

## ⚠️ The §3a.2a ledger — ten rounds, and what it taught

**The longest single fight in the project.** Worth keeping because almost none of it was about
this shot.

**Rounds 1–4 + a location turnaround: trying to move the camera across the road.** Every attempt
specified the corner harder; each bought more invented street. **A reference cannot move the
camera somewhere it has never seen** — §2j.0 is a pavement-level view, so it has no information
about the far side, and it wins ties.

**Rounds 5–7: trying to hide the setting.** Blur, bokeh, zoom burst, flash-and-drag. All
underdelivered for one physical reason: **light streaks need lights**, and flat overcast
mid-morning has no point sources. The engine was right and the prompt was wrong.

**Round 8: dusk + a thirty-second exposure. ✅ Accepted.** Real light sources, the traffic drawn
into unbroken ribbons, and every passer-by **vanished** — nobody stands still long enough to
register. *She is the only person in the picture because she is the only one who stayed.*

### The clip took six more rounds, and the lesson is the one worth keeping

| Attempt | Result |
| --- | --- |
| describe the ribbons in my own words (*bands, flowing along their length*) | reverted to a bus with motion blur |
| tell it *"never resolve into cars — no vehicle is ever visible"* | put **car**, **headlight** and **vehicle** in the prompt three times; got a bus |
| freeze everything, 50-word prompt | trails still reverted |
| Ingredients + `@Karen` | held her face, **re-staged the entire shot** |
| a full day-to-night timelapse | produced the effect and **abandoned the frame** |
| ✅ *"The attached image is a frame from a timelapse. **Continue that same timelapse** from this exact frame."* | **worked** |

> ### ✅ Ask the engine to *continue* a state, not to *reach* one.
>
> Every failed version asked for a transformation — become a long exposure, become night, become
> a timelapse. **The accepted version asked for nothing to change**: the still already *was* a
> long-exposure timelapse frame, so the instruction was to keep going.
>
> **And "timelapse" was the missing word all along.** *Long exposure* is a stills concept with no
> video equivalent — [it cannot be shot, only made in
> post](https://nofilmschool.com/2017/08/how-create-long-exposure-video-effect-after-effects) — so
> the engine had nothing to reach for and fell back to its prior: a bus. **Timelapse is a video
> form the model knows from thousands of hours of night-city footage**, and light trails are
> native to it.
>
> ### ⚠️ The general rule: **the more change you ask for, the less the start frame holds.**
>
> Small asks keep the frame and refuse the effect; big asks deliver the effect and abandon the
> frame. **When both matter, find the framing where the effect is already present in frame 0 and
> ask only for continuation.**
