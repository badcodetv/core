# docs/cinematography — how a frame is designed, and why one grips

The **judgement** layer for pictures. What the shot should *be*, decided before anyone asks a
tool for it — and deliberately tool-agnostic, so it outlives whatever generator we use next.

Driven by the **`shot-craft`** skill (`.claude/skills/shot-craft/`).

## What this is not

| Question | Lives in |
| --- | --- |
| How do I phrase this so Veo/Nano Banana obeys? | `flow-prompt` → [`../flow/`](../flow/README.md) |
| Which tool — Flow, ffmpeg, Premiere, sourcing? | `video-fx` → [`../video-fx/`](../video-fx/README.md) |
| What does a BadCode *panel* look like? | `badcode-art-direction` |
| What does a BadCode *brand image* look like? | `new-image` |
| Does the **story** grip? | `story-craft` → [`../story-craft/`](../story-craft/README.md) |
| Who is this for? | [`../marketing/the-reader.md`](../marketing/the-reader.md) |
| Is the file ready to upload? | [`../video-fx/delivery.md`](../video-fx/delivery.md) |

A finished shot is **register** (from a story's canon and the art-direction skills) + **design**
(here) + **phrasing** (the tool skill). Three separate jobs.

## The files

| File | What | Read when |
| --- | --- | --- |
| [`symptoms.md`](./symptoms.md) | **Start here when something looks wrong** — the complaint in ordinary words → the cause → what to change | "this is flat" / "it looks like AI" / "it's boring and I don't know why" |
| [`principles.md`](./principles.md) | **What we hold to be true** — 26 graded principles, the three gates, eight house rulings, and the one open ruling | First use in a conversation; when two pieces of advice conflict |
| [`frame.md`](./frame.md) | Composition, depth, staging, light, colour, lens, height | Designing or judging a single image |
| [`motion-and-cutting.md`](./motion-and-cutting.md) | Movement, sequence design, the cut, **and the method for re-cutting footage that already exists** | Any sequence; any "this cut isn't working" |
| [`on-screen-time.md`](./on-screen-time.md) | **Putting the year (or the place) on screen** — the six families, the fixed-slot decisions, and what we can actually render | A film jumps in time; a caption or title card is proposed |
| [`stills.md`](./stills.md) | The static frame — what holds a held image, word-and-picture, the gutter, duration | Our dominant form; choosing between generated candidates |
| [`registers.md`](./registers.md) | The monumental register **and its problem**, awe, documentary, British social realism | Anything monumental; the money film; the register question |
| [`evidence.md`](./evidence.md) | Grades, the corrections applied during distillation, **the never-cite list** | Before any claim or number reaches a brief, a note, or public copy |
| [`briefs.md`](./briefs.md) | The 20-brief index, and what the sweep never covered | Whenever you want the long version |

## The three things that save the most time

1. **Darkness reads as depth only when one small region inside it is deliberately brighter.**
   Uniform black reads as a broken file, not as mood — and there is now a perceptual mechanism
   for why (lightness anchoring), not just craft lore. This is our register's central technical
   problem and its fix in one sentence.
2. **Before any monumental shot ships: is there a visible cost in frame?** Wreckage, exhaustion,
   a body that failed. Absent one, the grammar of power reads as celebration of it — and doing it
   ironically on purpose does not protect you. This is the picture version of a rule we already
   ruled in writing.
3. **A scene is a small argument; every shot is a step in it or it is decoration.** Most "this is
   flat" notes about a cut are really "these shots do not step."

## 🔴 One open ruling

The corpus contains material arguing against our own near-black monumental register — it is the
visual opposite of the tradition closest to our reader, and it carries a documented misreading
risk. Neither brief proves the house look wrong; nobody has evidence either register works on
this specific reader. Stated in full in [`principles.md`](./principles.md) §R1. **Do not treat it
as settled in any canon file or public copy.**

## Provenance

Distilled 2026-08-26 from a 20-brief parallel sweep with two adversarial critic passes —
[`briefs.md`](./briefs.md). Twenty briefs, 141 web searches, zero AI-prompt-vocabulary leaks
across both waves.

**Grades were lowered during distillation.** Wave one built **P** grades from content-mill
convergence; where that happened, [`evidence.md`](./evidence.md) §1 records the correction. This
toolkit is the authority over the briefs.

## Writing back

Found something in production? Add it here, graded **H** (house), with the date and what actually
happened. Our own measured findings outrank anything in the briefs — the GPOM `vantage`
discovery ("an aerial cannot carry emptiness") predates the research that later explained it, and
that is the pattern to repeat.
