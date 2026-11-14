# Infinite Yous (a BadCode short)

> **A short is a project** (Kai, 2026-11-10): ID `short-infinite-yous`, Drive `Shorts/Infinite Yous` (row in
> `scripts/drive/folders.json`), each machine points the ID at its own folder (`drive.sh where`). Made with `new-short`,
> which runs `new-scene` on the one scene in `scenes/infinite-yous/`. The list: [`docs/marketing/badcode-shorts.md`](../../marketing/badcode-shorts.md) (#68).

## The idea (slate #68, Jack 2026-11-13, his words)

"it starts with that line [*one version of me gets home fine*], and it shows multiple versions of him on the same
screen, they all split off, then the badcode balaclava guy in a science lab coat grabs all of the lines separating the
different versions, squeezes them into one the original version, says there is only one and kicks him into a cab, it
cuts to the badcode logo and name screen, when taxi headlights illuminate it and car beeping happens, but not overly
annoying just in a cinematic way."

Look: the night-taxi photo Jack attached (bokeh city lights, glowing TAXI roof signs), as reference or described.
Method: clean room, web research.

**Point:** the Storyverse's "one stage, not a multiverse" (`docs/stories/storyverse/doctrine.md`; Everett is one
interpretation among several, its probability puzzle still open). The pop "infinite yous, so nothing matters" is
the excuse; there is one of you, and one mum waiting up. Stake: his life.

## Checks owed
- 🔴 **The balaclava** (`docs/brand/README.md`): reference + zoomed check of the triangle in every still and clip.
- 🔴 **The logo is never drawn by Flow**: the end card is the official file (`docs/brand/logo/`) over a Flow plate, lit in the edit.
- 🔴 **Drink-driving**: he is drunk and holding keys; the short is against it (BadCode stops him). Gatekeeper to confirm it reads that way.
- ⬜ Taxi livery: invented, no real firm's name or colours (the "TAXI" sign is generic).
- ⬜ `marketing-gatekeeper` before posting.

## State

| What | Where | Status |
| --- | --- | --- |
| Words | `scenes/infinite-yous/scene.json` beats | Jack's lines, 2026-11-13 |
| Look | [`look.md`](./look.md) | EXPLORING: Jack's night-taxi photo |
| Sound | [`sound.md`](./sound.md) | EXPLORING: Suno round `songs/r1-track` gated, NOT RUN (Suno sign-in) |
| Media | Jack: Desktop `Youtube Vids\animation\shorts\infinite-yous` · Drive `Shorts/Infinite Yous` | stills round 1 PICKED 2026-11-14 (LI1-b, SP1-a, SQ1-a to redo, CA1-a-fix-c, LO1-b; notes in `scenes/infinite-yous/picks.md`) |

## Resume here (2026-11-14)

1. **Suno round `songs/r1-track`** (Jack: "do the suno sounds and music in one"): the lines, sound effects and music in ONE 15 s track, six directions written by sealed writers and passed by the gate (`round.json`, stamped). **Not run yet.** Channel 1's Chrome (port 9222, signed in to Suno) has extensions whose background workers block Playwright's CDP attach, even after restarts; the Flow browser (channel 2, port 9223) attaches fine but is signed out of Suno. Once Jack has signed in there: `SUNO_CDP_ENDPOINT=http://localhost:9223 python3 scripts/variations/round.py run docs/stories/short-infinite-yous/songs/r1-track "infinite yous r1" --yes`, then post the links; the pick goes into `sound.md`.
2. **Stills owed** (Jack's notes): SQ1 redone with SP1-a's five vertical strips, the BadCode figure more of a scientist, no skin ever; CA1 with that same scientist; the logo goes on LO1-b's wall in the edit, lit by a headlight sweep.
3. Then animate the picks to the track, build the split and the line-grab in the edit, and put it on a timeline page.
