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

**The angle: an 85mm over-the-shoulder.** Long enough to keep Act 3's compressed, watched-from-a-
distance language, short enough that the camera does not have to stand a block away to make the
frame. Prompt order follows the convention — **angle → lens → composition** — so the spatial
rules land before any detail.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman in the kiosk, her clothes, the flat overcast mid-morning light, and the grainy super-8 film look. Redesign nothing.

Change three things:

1. An over-the-shoulder shot on an 85mm lens at f/4, taken from just behind a young man's shoulder at his head height. He fills the near left of the frame from behind, large and out of focus, and everything beyond him is sharp.

2. He has stopped mid-walk on the pavement a few steps in front of the kiosk, wearing his rig, holding his phone up in both hands to film her. He is standing well back from the kerb and every part of him is on the pavement.

3. The woman is in the kiosk beyond him, in the right half of the frame and sharp, with the receiver at her ear, her mouth open in mid-shout and her free hand out in front of her off the shelf. She does not know he is there.

The pavement is otherwise empty. Natural skin texture with visible pores. No readable lettering anywhere, and nothing readable on the phone screen. No border around the image.

Thanks.
```

**What to watch:**

1. **Is the rig there, and does it read?** Headphones, the harness straps across his back, the
   chest mic, cables. **It is the only thing identifying him in this framing**, and with the
   clothing description finally gone the Character should supply all of it.
2. **Is he on the pavement?** Round 2 put him in the road. The kerb is the tell.
3. **Is she the sharp one?** He is the blur; she is the subject. If the focus has swapped, it has
   become his scene, which the canon forbids twice.
4. **Is her mouth open?** Mid-shout is what he is recording and what the narrator's line sits on.
5. **Blank phone screen?** Screens are where text appears and where policy blocks come from.

> ### ⚠️ Standing rule, relearned the hard way
>
> **Never describe a cast member's clothes, face or build in a scene prompt** when their
> Character is attached. It is written in every character file and it was still worth two
> generations to relearn. **The shot only** — where they are, what they are doing, where the
> camera is.

## What this act still owes

| § | Piece | Notes |
| --- | --- | --- |
| **3a.1** | The sample — plate | ✅ written, **round 3** — 85mm over his shoulder; the rig identifies him, no clothing described |
| 3a.1v | The sample — clip | **only he moves**: he stops, lifts the phone, lowers it, walks out of frame. Karen holds. |
| 3a.2 | Karen shouts the line — plate | her single; the counter-shot, so the two-hander never shares a moving frame |
| 3a.2v | …— clip | **only she moves.** This is the *"I've got ALL DAY to complain"* shot |
| 3a.3 | The train — plate | two riders, a phone between them, the tune playing in-world |
| 3a.4 | The crowd — the drone trick | **stills only, cut between.** Altitude up/down, the crowd bigger each time. Never animated. |
| 3a.5 | News vans | the end of the act; the world has arrived and she is still on hold |
