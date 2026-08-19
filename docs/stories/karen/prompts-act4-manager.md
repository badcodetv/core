---
story: karen
kind: brief — written in-repo, fired by hand; each block is the deliverable
engine: Nano Banana Pro (plates) → Gemini Omni Flash (clips)
flow_project: TODO — exact project name as it appears in Flow
updated: 2026-08-19
---

# Karen — Act 4, The Ultimate Manager

Plate and clip prompts for the act where a television show escalates Karen to the one man with
no manager above him, and an AI fires him live on air.
[`story.md`](./story.md#act-4--the-ultimate-manager) §Act 4. Section numbers run at **§4a**.

> ## 🖐 A brief, not a record
>
> [`prompts.md`](./prompts.md) is the **ledger**; this is not one. Conventions inherited: the
> casting rule (`**Cast:** @X` — never describe a face), no legible text, **one reference by
> default**, and the closing *"Thanks."* on the final block of every paste.
>
> **Fired by hand, not by the automation** (Kai, 2026-08-16). **Clips are 8s** (Kai,
> 2026-08-18) — they carry narration.
>
> **Engine research does not live here** — it goes to
> [`docs/google-flow/`](../../google-flow/README.md).

---

## ⚠️ Two rulings this act needs before anything is fired

### 1. It is a **film crew** and a **film set**. The word "news" is banned.

**Ruled 2026-08-19 (Kai), bought with four refusals in Act 3.** Flow blocks on *"reputational
risk or misrepresent current events"*, and **deleting journalism words is not enough** — the
classifier infers *news* from a microphone, a mast, a person speaking. What cleared it was
**asserting a different category**:

> This is a behind-the-scenes shot of **a film crew shooting a scene for a movie**.

**So this whole act is written as a film set**, not a television studio: **actress**, **crew**,
**camera operator**, **boom pole**, **production van**, **the set**, **delivering her lines**.
Never *news*, *reporter*, *broadcast*, *live*, *television*. **The picture may look like
anything; the prompt may not say so.** Full note:
[`failure-modes.md`](../../flow/failure-modes.md).

### 2. ⚠️ The President is **fictional and must not resemble anyone**

Canon never names him, and he must stay unnamed. The documented rewrite for a real or named
person is *"a fictional adult … **do not resemble any real person**"*, and every plate in this
act that includes him carries that line verbatim.

**He is also easier to shoot than he sounds.** Canon gives him **two words** — *"Hello — this is
the President."* — so he needs **no dialogue on screen** and can be shot the way Act 2 shot the
Chief of Staff: **from behind, from a distance, or as a figure in a chair**. The less of his face
the film sees, the safer and the funnier: *the ultimate manager is a shape in a suit.*

### 3. The look changes, and that is the point

[`story.md`](./story.md#41-the-tv-studio--new): *"A whole new world. No visual link back to the
crowd — cutting cold to a place we've never seen."* Everything so far is grey pavement and flat
overcast daylight. **This act is warm, interior, lit and expensive** — carpet, glass, coffee,
lamps. The `STYLE LOCK` still runs, so it is the same film; the *world* is what changes.

---

## 4a.1 The production office — plate

**Cast:** none — no Characters exist for these people and none are needed. **Attached:** nothing —
**prose only**, so the `STYLE LOCK` goes in full. **Engine:** Nano Banana Pro, 16:9, 3 candidates.

> ### The shot is the silence after *"we need an idea."*
>
> Canon calls for it outright: *"Beat of silence (narrator: the traditional moment of silence that
> follows 'we need an idea')."* **That is a photograph.** A room of well-paid people who have just
> been asked to think of something, all of them very carefully not looking at each other.
>
> **Nobody is talking, and nobody is panicking visibly.** The comedy is in the stillness — the
> ceiling, the middle distance, a pen, a phone under the table. Give one of them a raised eyebrow
> and it becomes a sitcom.

**The intern is in the frame and nobody has noticed her.** She is at the edge with a tray of
coffees, and she is the only person in the room who is going to say anything useful. **She is not
doing anything yet** — no raised hand, no open mouth. She is just there, which is the joke, and
it is the same grammar as the pedestrians who never look at Karen.

**Warm and expensive**, against nine months of grey street: lamps, carpet, a glass wall to a
corridor. **One named light** — a big window on one side, blinds half down — because
[flat overhead office lighting is what made §2j.5's receptionist look like stock photography](../../google-flow/nano-banana-2.md#the-anti-slop-toolkit-community).

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

Subject: six adults sitting round a long table in a production office, none of them speaking, in the silence after somebody has asked for an idea.

Composition: 16:9 on a 35mm lens at f/2.8, from the end of the table at seated eye level, so the table runs away from the camera into the room. Three people down each side, cut off by the edges of the frame at the near end. A young woman stands at the far right edge holding a cardboard tray of coffee cups, half out of frame, not part of the group. The ceiling shows across the top of the picture. The frame is slightly off level.

Action: nobody is talking and nobody is looking at anybody else. One is looking at the ceiling, one is looking out of the window, one is turning a pen over, one is looking at a phone held low under the edge of the table, one has both hands flat on the table looking at them. The young woman with the coffee tray is just standing there, waiting, and nobody has noticed her.

Location: a mid-sized production office in a modern building — a long scratched table, mismatched chairs, laptops open and pushed aside, takeaway cups, a whiteboard wiped almost clean, a glass wall onto a corridor behind them, a low bookcase with box files on it, carpet tiles.

Light: a wide window along one side with the blinds half down, throwing a broad soft light across one side of the table and leaving the other side and the far end of the room in shadow. One desk lamp is on. The ceiling lights are off.

Style: a still from a 35mm independent film — a room full of clever people with nothing to say. Available light only, unretouched, natural skin texture with visible pores and shine.

Constraints: adults only; ordinary present-day office clothes, no suits and ties; keep the whiteboard, the laptops, the cups, the box files and every notice free of readable lettering; no border or frame edge around the image.
```

**What to watch:**

1. **Is anybody performing?** No raised eyebrows, no heads in hands, no exasperated faces. **The
   joke dies the moment somebody acts it.** If it comes back as a sitcom, the line to add is
   *"every face is completely blank."*
2. **Has the intern been noticed?** She should be at the edge, unremarked, doing nothing. If the
   room is looking at her, the beat has fired two shots early.
3. **Is the light from the window?** If the ceiling lights are on and the room is flat, the frame
   will look like stock photography — that failure is documented and it is always the lighting.
4. **Is the room ordinary?** Scratched table, mismatched chairs, carpet tiles. A glossy boardroom
   is the wrong kind of world; these are people making a television programme, not running a bank.
5. **Any readable writing on the whiteboard?** It is the most likely place for text to appear.

## What this act still owes

| § | Piece | Notes |
| --- | --- | --- |
| **4a.1** | The production office — plate | ✅ written — the silence after *"we need an idea"* |
| 4a.1v | …— clip | **nobody moves much**: a pen turns, someone breathes out. The intern speaks off-screen |
| 4a.2 | The intern says it — plate | her, finally noticed; the room turning towards her |
| 4a.3 | The executives discover their own genius | canon lands the joke **here**, before the call |
| 4a.4 | The set — the show | **a film set, never a studio.** Lights, a desk, two chairs, a crew |
| 4a.5 | The ultimate manager | ⚠️ fictional, non-resemblance line mandatory; **shot from behind** |
| 4a.6 | The call | two lines of dialogue in the whole act |
| 4a.7 | Sean AI takes the screen | same UI as §1.4, **gold** icon now — the bookend |
