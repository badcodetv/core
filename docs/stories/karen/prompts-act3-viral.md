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

> ### ⚠️ Round 1 fired 2026-08-18 — three notes from Kai, and they resolve into one shot.
>
> | Note | Cause |
> | --- | --- |
> | *"Aarron should not be in front of Karen, maybe behind and to the side"* | round 1 put him in the near foreground, which made it his scene |
> | *"it did not use his likeness from `@Aarron`"* | **my error: I asked for the back of his head.** A Character has nothing to apply a face to when there is no face in the frame |
> | *"the same shot directly in front of Karen is getting boring"* | true — every frame in this film so far is 28–35mm from in front of her |
>
> ### The likeness rule, now explicit: **a Character needs a face in the shot.**
>
> The consistency guidance asks for *"a sharp image with neutral lighting that clearly shows the
> face"* on the reference side; the same is true of the **output** side. **`@Aarron` on a shot of
> the back of a head is a wasted attachment.** Round 1's whole design — anonymity, a sliver of
> face, *"he is not part of the attraction"* — was faithful to the canon and incompatible with
> using his Character at all.
>
> **Resolved by putting him behind her rather than in front:** further down the street, **facing
> back towards the camera as he films her**, so his face is toward us and the Character binds,
> while she is still the near, dominant figure. Kai's first note fixes the second.
>
> ### ✅ The new angle: go long. 135mm from down the pavement.
>
> **A long lens is how you photograph someone who does not know you are there**, which is exactly
> what this act is about — so the change is motivated, not decorative. It also
> [compresses the block and stacks the layers](https://www.gensgpt.com/blog/camera-angles-composition-ai-image-generation-2026-guide),
> which puts Aarron visually close to her while keeping him ten or fifteen feet behind, and it
> gives Act 3 **a visual language of its own**: everything up to now is a wide standing on the
> corner; from here the camera is watching from a distance, because so is everybody else.
>
> **Prompt order matters and is now followed:** the field convention is **angle → lens →
> composition → lighting → style**, so that spatial rules are set before any detail is added.
>
> **Anti-slop levers in this frame:** telephoto compression (unusual and hard to fake), a
> deliberate blurred foreground occluder, an off-centre subject, and a candid distance rather
> than a composed portrait.

```prompt
Image 1 is the reference. Keep it exactly as it is — the same kiosk, the same subway entrance immediately behind it, the same scaffolding, the same corner, the same woman in the kiosk, her clothes, the flat overcast mid-morning light, and the grainy super-8 film look. Redesign nothing.

Change three things:

1. The shot is taken from a long way down the pavement on a 135mm lens at f/5.6, from a photographer standing back against the scaffolding at chest height and looking along the street, so the whole block is compressed and stacked up behind the kiosk. A scaffolding pole crosses the very near edge of the frame, blurred. Both people described below are in focus.

2. The woman is in the kiosk, a little left of centre, with the receiver at her ear, her mouth open in mid-shout and her free hand out in front of her off the shelf. She does not know anyone is watching her.

3. A young man in his twenties stands further down the pavement, beyond the kiosk and off to the right, ten or fifteen feet behind her. He has stopped mid-walk and is holding his phone up in both hands, filming her, so he is facing back towards the camera and his face is clearly visible. He is in a hoodie, a jacket and trainers with a small backpack on one shoulder.

The pavement is otherwise empty. Natural skin texture with visible pores. No readable lettering anywhere, and nothing readable on the phone screen. No border around the image.

Thanks.
```

**What to watch:**

1. **Is his face visible and is it Aarron?** The round-1 failure and the whole reason for the new
   geometry. If it is turned away again, `@Aarron` has nothing to bind to and the attachment is
   wasted.
2. **Is it actually compressed?** 135mm should stack the block up behind the kiosk and make the
   buildings look close and flat. If it comes back looking like a 35mm wide, the framing lost to
   the reference and the fix is a consequence — *"the buildings behind the kiosk look stacked
   right up against it."*
3. **Is she still the near, dominant figure?** He is behind and smaller. If he has come forward
   again it has become his scene, which the canon forbids twice.
4. **Is her mouth open?** Mid-shout is what he is recording, and it is what the narrator's line
   sits on.
5. **Blank phone screen?** Screens are the most reliable place for text to appear and the most
   reliable policy block there is.

## What this act still owes

| § | Piece | Notes |
| --- | --- | --- |
| **3a.1** | The sample — plate | ✅ written, **round 2** — 135mm down the pavement; he is behind her, facing back, so `@Aarron` binds |
| 3a.1v | The sample — clip | **only he moves**: he stops, lifts the phone, lowers it, walks out of frame. Karen holds. |
| 3a.2 | Karen shouts the line — plate | her single; the counter-shot, so the two-hander never shares a moving frame |
| 3a.2v | …— clip | **only she moves.** This is the *"I've got ALL DAY to complain"* shot |
| 3a.3 | The train — plate | two riders, a phone between them, the tune playing in-world |
| 3a.4 | The crowd — the drone trick | **stills only, cut between.** Altitude up/down, the crowd bigger each time. Never animated. |
| 3a.5 | News vans | the end of the act; the world has arrived and she is still on hold |
