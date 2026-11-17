# Same Bench

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode Short, portrait 9:16. A top-hatted fat cat on a park bench tells a one-legged veteran "Forget it." (1919).
Same bench, now, the same fat cat, a nurse: "Forget it." He hasn't aged a day ("Same bench."). The point: the people
who carry the cost are thanked, then forgotten; the fat cat is the decision-maker, never the soldier's or nurse's
fault. State: rough cut 3 (26 s, target ~15 s) on the timeline page and in Premiere
(`short-same-bench-1-same-bench-r3`), awaiting Jack's notes. Nothing uploaded.

## Look
**LOCKED for every beat.** One surviving frame of a lost 1919 silent horror reel: night, a cast-iron bench under a
single gas lantern whose flame pours straight down like a spotlight; the fat cat's eyes are black pits under the hat
brim above a chalk-white courteous smile. Hand-cranked nitrate: blown whites against pure black, clotted grain,
vertical scratches, dust, a round iris mask. Monochrome. **Today is shot on the same stock**: the joke is that nothing
changed. Anchor still `moodboard/A2-b.jpg` (Flow media 00064fd8). Clips: Omni 1.2 Flash, 9:16.

Anchor prompt (A2-b, verbatim):
```
One surviving frame of a lost 1919 horror reel, upright portrait framing. Night in a public garden, everything gone except a cast-iron bench and a single gas lantern hanging on a bracket straight above it, so its flame pours down like a spotlight from the ceiling of the dark. On the bench, directly under that flame, a bloated plutocrat in a stovepipe silk hat, black frock coat strained over his belly, a gold fob chain catching one spark. The overhead glare drops the hat brim's shadow across his eyes, leaving two bottomless black pits where they should be, while below them a powdered, chalk-pale face holds a courteous little smile that glows almost white; his lip rouge prints as ink, as red always did on that blue-only stock. Wearily, a gloved hand dangles and flaps once at the man beside him: a hollow-cheeked infantryman home from the front, army greatcoat too big, one leg ending at the knee with the trouser folded and pinned, a plain wooden crutch laid across his lap. The veteran sits past the edge of the lamplight and dissolves into the night, only his fingers on the crutch and the line of one cheekbone faintly showing. Static camera at seated eye level, square-on, a medium shot of the pair placed in the lower half of the frame, the upper third an unbroken black void above the lantern kept clear for a caption. The emulsion of a hand-cranked early nitrate print: blown-out whites slamming into pure black with almost nothing in between, coarse clotted grain, hairline scratches running top to bottom, flecks of dust, edges going soft, a round iris mask darkening all four corners. Monochrome, photochemical, no smooth digital finish, no lettering anywhere. Thanks.
```
- **The fat cat is Flow Character `SB Fat Cat`** (project 0f0d05fd). Cast him in every frame; never describe his
  appearance, only position, action and expression.
- The veteran must read as one-legged (trouser pinned at the knee): Flow gives him two legs, check every frame.
- Top third kept as black void for dates and captions. Dates and plaque words are made in the edit
  (`scripts/shorts/same_bench_dates.py`), never drawn by Flow.

## Sound
**Fat cat voice LOCKED: AI Studio `Algenib`**, profile `scenes/same-bench/voices/profiles/cat-a-algenib.md` (a plummy
old Englishman, 60s, low purr, velvet contempt), rendered with `scripts/aistudio-tts.py`. His lips never move, so no
lip-sync. **Music:** Not decided — run story-style.

## Story-only rules
- 🔴 Not a copy of the 1919 *Life* panel: our own staging; never attach or describe that cartoon.
- No AI likeness of a real person; the fat cat is a type. Still C2-b resembles a real politician: never use it.
- Never name the horror game that inspired the mood, or use its monsters, places or imagery.
- Nurse line is about pay and the clapping, not the pandemic as news. `marketing-gatekeeper` before anything goes out.
- No Flow speech.
- Unclear: the second date card reads "Now." (script.json) or "2026" (look.md, RESUME.md).

## Library pieces in use
- none yet

## Where the detail is
- [RESUME.md](./RESUME.md), [look.md](./look.md), [sound.md](./sound.md), [README.md](./README.md)
- [scenes/same-bench/script.json](./scenes/same-bench/script.json) (dialogue 1B), [scenes/same-bench/scene.json](./scenes/same-bench/scene.json), [picks.md](./scenes/same-bench/picks.md)
- Timeline page: https://claude.ai/artifact/2DdWL1U98tLQSFsoGVroGC · mood board: https://claude.ai/artifact/QM1RiEUHBSYKwurMtpeMgP
