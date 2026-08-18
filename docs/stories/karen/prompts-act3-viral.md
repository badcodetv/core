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

## 3a.0 He walks past — plate

**Cast:** `@Aarron`. **Attach:** the accepted **§2j.0** still as image 1. **One reference.**
**Time:** flat overcast mid-morning. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### The walk is the accident.
>
> [`story.md`](./story.md#31-the-aarron-cameo--redo-five-seconds-total): *"Aarron happens to
> wander past the phone box — **he is not looking for anything.**"* Without this frame he is a
> man who came to a phone box to film a woman, and the canon warns twice that **the believable
> version is the accidental one.** Everything the cameo means rests on him having been on his way
> somewhere else.
>
> **So the tell is his hands: the phone is in his pocket.** He is not filming, not scrolling, not
> looking for content. He gets it out *because of what he hears*, and the only way an audience
> feels that is if they saw it put away first.

**A proper cut needs a different size, so this one is wide.** §3a.1 is a 135mm three-quarter from
twenty feet; this is **a 50mm on the whole corner from thirty**. Wide establishes the geometry —
her in the box, him coming along the pavement, the distance between them — and then the cut goes
tighter as he stops. Same-size shots cut like a stutter.

**Karen stays the near, dominant figure**, as in every frame of this act. He is small, further
away, and walking.

> ### ⚠️ The headphones stay on, and the beat does not touch them.
>
> A man in over-ear headphones hearing a woman shout is a small logic problem, and the tempting
> fix — **he lifts one cup off his ear** — is a lovely beat that **breaks continuity with the
> accepted §3a.1 still**, where both cups are on. It is not worth it. She is shouting at the top
> of her voice on an empty street; that is loud enough. **The "he heard it" moment is carried by
> his head turning in the clip and by the narrator's line, not by the headphones.**

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman in the kiosk, her clothes, the flat overcast mid-morning light, and the grainy super-8 film look. Redesign nothing.

Change three things:

1. A wide shot of the whole corner on a 50mm lens at f/5.6, taken from the pavement about thirty feet away at chest height, with the kiosk on the left of the frame and the subway entrance and the pavement beyond it running away to the right.

2. The woman is in the kiosk on the left, closest to the camera, with the receiver at her ear, her mouth open in mid-shout and her free hand out in front of her off the shelf.

3. A young man is walking along the pavement on the right, past the subway entrance and towards the kiosk, caught mid-stride with one foot off the ground. He is wearing his rig, his hands are down by his sides and his phone is in his pocket. He is looking straight ahead along the pavement, not at her, and he has not noticed her.

The pavement is otherwise empty. Natural skin texture with visible pores. No readable lettering anywhere. No border around the image.

Thanks.
```

**What to watch:**

1. **Are his hands empty and his phone away?** The single most important thing in the frame. A
   phone already in his hand and the cameo stops being an accident.
2. **Is he looking away from her?** Eyes down the pavement. If he is already looking at her, the
   shot has skipped to the next beat.
3. **Is he mid-stride?** One foot off the ground. A standing figure reads as arrived, and this
   shot exists to show him *passing*.
4. **Is she still the nearest and largest?** He is a small figure on the right.
5. **Does the rig read at this distance?** Harness, headphones, the chest keyboard. If it is
   unreadable at 50mm the fix is to bring him a little closer along the pavement, **not** to
   describe it.

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
| **3a.0** | He walks past — plate | ✅ written — 50mm wide, phone in his pocket, not looking at her |
| 3a.0v | He walks past — clip | **only he moves**: he walks, slows, and his head turns towards the kiosk |
| **3a.1** | The sample — plate | ✅ written, **round 4** — 135mm three-quarter; he stands by the subway railings behind her |
| **3a.1v** | The sample — clip | ✅ written — **only she moves**; he is planted and the one change is a smile |
| 3a.2 | Karen shouts the line — plate | ⚠️ **owed** — her single; the sound the whole film hangs on, and it keeps the two-hander out of one moving frame |
| 3a.2v | …— clip | **only she moves.** This is the *"I've got ALL DAY to complain"* shot |
| 3a.3 | The train — plate | two riders, a phone between them, the tune playing in-world |
| 3a.4 | The crowd — the drone trick | **stills only, cut between.** Altitude up/down, the crowd bigger each time. Never animated. |
| 3a.5 | News vans | the end of the act; the world has arrived and she is still on hold |
