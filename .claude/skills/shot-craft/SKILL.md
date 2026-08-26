---
name: shot-craft
description: Use when deciding or judging what a shot should BE — designing a frame, choosing an angle or a light, planning a scene's shots, re-cutting footage that already exists, or diagnosing why something looks flat, boring, generic or "like AI". Triggers on "what's a more interesting shot for this", "how should we frame this beat", "this feels flat / boring / generic", "why does this look like AI", "give me a better angle", "how do we make this exciting", "alternate way of cutting X", "let's discuss the cinematography for <scene>", "what should this scene look like", "is this shot working", or any shot-design step inside make-comic, badcode-art-direction, new-image, music-video-short, animate-slide, flow-prompt or premiere-automation. Tool-agnostic craft only — HOW to phrase it for a generator is flow-prompt, WHICH tool is video-fx, what the BadCode look is stays with badcode-art-direction and new-image, and whether the STORY grips is story-craft.
---

# Shot Craft (BadCode)

Make the picture grip. This skill owns **what the shot should be** — the judgement layer,
decided before any tool is asked for anything, and deliberately tool-agnostic so it survives the
next generator.

Three modes, one knowledge base:

- **Design** — a shot or a scene does not exist yet. Work from the gates outward.
- **Diagnose** — something exists and is not working. Start at the symptom.
- **Re-cut** — the clips are made and the cut is flat. The shot inventory is fixed.

## What is not this skill's job

| Question | Goes to |
| --- | --- |
| How do I phrase this so the generator obeys? | `flow-prompt` |
| Which tool — Flow, ffmpeg, Premiere, archive footage? | `video-fx` |
| What does a BadCode *panel* look like? | `badcode-art-direction` |
| What does a BadCode *brand image* look like? | `new-image` |
| What is this story's cast, style and canon? | `docs/stories/<story>/prompts.md` |
| Does the **story** grip? Is the beat earning its place? | `story-craft` |
| Is the file ready to upload? | `video-fx` → `docs/video-fx/delivery.md` |

**A finished shot is register + design + phrasing.** Register comes from the story's canon and
the art-direction skills; design comes from here; phrasing comes from the tool skill. Do not do
all three in one breath — the design decision is the one that gets skipped, and it is the one
that decides whether the shot is interesting.

## The knowledge base lives in `docs/cinematography/`

Read on demand. Never reproduce it into a reply and never lecture the user about it.

| File | Read when |
| --- | --- |
| [`symptoms.md`](../../../docs/cinematography/symptoms.md) | **Any complaint.** The user's own words → cause → fix. Start here in Diagnose mode |
| [`principles.md`](../../../docs/cinematography/principles.md) | First use in a conversation; whenever two pieces of advice conflict. Carries the three gates, eight house rulings, and the open ruling |
| [`frame.md`](../../../docs/cinematography/frame.md) | Designing or judging one image — composition, depth, staging, light, colour, lens, height |
| [`motion-and-cutting.md`](../../../docs/cinematography/motion-and-cutting.md) | Any sequence; **§4 is the re-cut method** |
| [`stills.md`](../../../docs/cinematography/stills.md) | A held image under narration; choosing between generated candidates |
| [`registers.md`](../../../docs/cinematography/registers.md) | Anything monumental; the documentary register; the social-realism question |
| [`evidence.md`](../../../docs/cinematography/evidence.md) | **Before any claim or number reaches a note, a brief or public copy.** Carries the never-cite list |
| [`briefs.md`](../../../docs/cinematography/briefs.md) | The long version of anything |

Raw research: `design/research/2026-08-26-cinematography/`. It is research, not policy — the
toolkit lowered several of its grades. Never quote a brief over the toolkit.

---

## The three gates

Before designing anything. A shot failing one is not designed further.

1. **What is this shot FOR?** Not what it shows — what it does to the viewer that the previous
   shot did not. "It looks good" means there is no shot yet.
2. **🔴 Is there a visible cost in frame?** Mandatory on any monumental shot — scale, symmetry,
   a machine, an institution. Wreckage, exhaustion, a body that failed, someone the system is
   failing. Without one, the grammar of power reads as celebration of it, and meaning it
   ironically does not protect you. *(This is the picture version of `the-reader.md`'s standing
   rule: never raise a fear without naming the beneficiary.)*
3. **Where does the light come from?** Name the source in the world. "It's just lit" produces
   the generic read before anything else registers.

---

## Design mode

For a shot that does not exist yet. Output a **shot spec**, not a prompt.

1. **The job.** One sentence: what this shot does that the last one did not.
2. **The register.** Monumental, documentary, or the human-scale exception *(ruling R2)*. Get
   this from the story's canon, not from here.
3. **Depth.** What is in the foreground, midground, background. Never leave the foreground empty
   — it is the most common cause of a flat frame and it is free.
4. **The focal point.** The one thing the eye rests on, and what it is winning with — light,
   space, or depth position.
5. **The light.** Source, direction, and **where the falloff goes**. On near-black: name the one
   bright anchor, or the frame reads as a broken file.
6. **Camera.** Height (a slider, not three boxes), angle, distance. State height and angle
   separately — they are different variables.
7. **Scale reference.** For any machine or building: the known-size object that makes size
   legible. Without it, size is abstraction.
8. **What is withheld.** A frame that shows everything has nothing to discover.
9. **What moves, if anything.** Default is nothing. *(See the motion budget below.)*

Then hand the spec to `flow-prompt` (or whatever tool skill applies) for phrasing. **Never write
the spec and the prompt in one step** — the spec is what a human can argue with.

### The motion budget

Most of our shots are stills or 8-second clips. **A single moving shot in a still body of work
lands with outsized force, and only if the stillness around it is real.** *La Jetée* spends 26
minutes as photographs and spends its one moving shot exactly once.

- Motivated stillness: free, always available.
- Motivated movement: worth spending roughly once per sequence.
- The push-in is the one move an 8-second clip executes cleanly, and it means one thing —
  narrowing attention toward a realisation. Put something at the end of it worth arriving at.

---

## Diagnose mode

Something exists and is not working.

1. **Take the complaint literally** and find it in
   [`symptoms.md`](../../../docs/cinematography/symptoms.md). It is written in ordinary words
   for exactly this.
2. **Name the cause before the fix.** "It's flat" is almost always one depth plane, or light with
   no traceable source — not a resolution or quality problem, and never fixed by regenerating.
3. **Give one change, not five.** The corpus is explicit that when a shot is not landing, the fix
   that works most often is *removing* a clause, not adding one.
4. **Check the gate.** If the shot is monumental, run gate 2 before anything else.

**Do not diagnose the frame when the problem is the story.** If a shot is technically fine and
still inert, the beat may not be earning its place — hand to `story-craft`.

---

## Re-cut mode

The clips exist, they are on a timeline, and the cut is flat. **Do not start by generating more
footage.** Full method: `motion-and-cutting.md` §4. In short:

1. State the argument the scene makes. One sentence. Can't? The problem is upstream — `story-craft`.
2. List what exists as **jobs, not clips**: establish, escalate, reveal, dwell, punctuate, or
   nothing. Shots doing nothing are usually the answer.
3. Lay out the shot sizes in order. Is there a direction, or is it random? Imposing one is free
   and is usually the biggest single improvement available.
4. Test the button — does the last shot close what the first opened? Often the real ending is
   already in the middle of the cut.
5. Cut shots that repeat a job. That is where the length comes out.
6. Re-time before re-shooting. Most "it drags" is duration, not footage.
7. **Only then** name the gaps — usually one or two shots, not a re-shoot.

Free upgrades that need no new footage: order, duration, a J-cut or L-cut, a beat of black, a
caption carrying the beneficiary, a bookend made by repeating an existing frame at the end.

---

## Working rules

- **Never claim the register question is settled.** Whether our near-black monumental look is
  right for a working-class UK reader is an **open ruling** (`principles.md` §R1). Nobody has
  evidence either way. Do not assert it in canon or public copy.
- **Check `evidence.md` before any claim or number leaves this skill.** The never-cite list is
  long and includes several things that sound authoritative — the rule of thirds as perception,
  fixed colour meanings, "low angle equals power" as law, the popular Kuleshov story, "handheld
  is truthful".
- **Say the grade when it matters.** A **p**-grade craft opinion and an **A**-grade optical fact
  should not be delivered in the same tone.
- **One change at a time** when iterating on a frame, so the variable is known. Same discipline
  as the Suno session method.
- **All candidates go to Kai** before any video credit is spent — the still-approval gate. This
  skill says what to look at; it does not pre-filter his choice.
- **Write back.** Something learned in production goes into `docs/cinematography/` graded **H**,
  with the date and what happened. Our own measured findings outrank the briefs — the GPOM
  `vantage` discovery that an aerial cannot carry emptiness predates the research that later
  explained it.
