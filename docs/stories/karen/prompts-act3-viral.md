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

**Shot from behind and slightly to one side of him**, so we get his phone screen, a sliver of his
face, and **Karen small in the kiosk beyond, mid-shout**. Three things this buys:

1. **Her face is far enough away not to need `@Karen`** — one Character, one reference, a short
   prompt. Everything this file has learned says that is the shot most likely to come back right.
2. **The phone screen is the story.** What he is doing is more important than what he looks like,
   and a screen held up between us and her is the image the next twenty million views come out of.
3. **He is facing away from us, which is where he is going.** We never see him again.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman in the kiosk, her clothes, the flat overcast mid-morning light, and the grainy super-8 film look. Redesign nothing.

Change three things:

1. A young man in his twenties has stopped on the pavement a few steps in front of the kiosk, seen from behind and slightly to his left, filling the left of the frame and close to the camera. He is holding his phone up in front of him in both hands, filming, and only a sliver of the side of his face is visible. He is in a hoodie, a jacket and trainers, with a small backpack on one shoulder.

2. The woman in the kiosk is beyond him, small and sharp in the middle distance, with the receiver at her ear and her mouth open in mid-shout. She is not looking at him and does not know he is there.

3. The camera is at his shoulder height on the pavement, standing under the scaffolding, on a 35mm lens. He is out of focus in the near foreground and she is the sharp thing in the frame.

The pavement is otherwise empty. Natural skin texture with visible pores. No readable lettering anywhere, and nothing readable on the phone screen. No border around the image.

Thanks.
```

**What to watch:**

1. **Is he anonymous?** A sliver of face, from behind. **If it has turned him round into a
   portrait, reject it** — the canon is explicit that he is not part of the attraction, and a
   face here makes him a character instead of an accident.
2. **Is she the sharp one?** The focus is the whole argument of the frame: he is the blur, she is
   the subject. If he is sharp and she is soft, it has made this his scene.
3. **Is her mouth open?** Mid-shout is what he is recording. A woman standing quietly gives the
   narrator's line nothing to sit on.
4. **Is the phone screen blank?** Screens are the most reliable place for text to appear, and a
   legible screen is also the most reliable policy block there is.
5. **Same kiosk and same corner?** As ever. It is the fixed point of the whole film.

## What this act still owes

| § | Piece | Notes |
| --- | --- | --- |
| **3a.1** | The sample — plate | ✅ written — over his shoulder, she is the sharp one |
| 3a.1v | The sample — clip | **only he moves**: he stops, lifts the phone, lowers it, walks out of frame. Karen holds. |
| 3a.2 | Karen shouts the line — plate | her single; the counter-shot, so the two-hander never shares a moving frame |
| 3a.2v | …— clip | **only she moves.** This is the *"I've got ALL DAY to complain"* shot |
| 3a.3 | The train — plate | two riders, a phone between them, the tune playing in-world |
| 3a.4 | The crowd — the drone trick | **stills only, cut between.** Altitude up/down, the crowd bigger each time. Never animated. |
| 3a.5 | News vans | the end of the act; the world has arrived and she is still on hold |
