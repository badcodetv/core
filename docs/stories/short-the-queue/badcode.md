# The Queue

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16 offered, not ruled; aim 15-20 s). A Post Office-style queue where every window says POWER
("Cashier number three, please"); a giant data centre pushes in front; the cashier (BadCode in the balaclava) sends it
to the back: "Brilliant machine. Wrong queue." "Households first." The point: homes come first on the grid; big
new loads switch down first and pay for their own wires. From the BadCode government's Energy and Climate policy
`households-first`, in that minister's voice (the engineer who can't stop being excited, sharp when someone profits
from a shortage). State (2026-11-21): **rough cut 1**, 24.7 s, on https://claude.ai/artifact/GP42gfZhpUKiPHdCbizQsp. Rebuild: `scripts/shorts/queue_logo.py` then `scripts/shorts/queue_cut.py --round 1` (args in scene.json `cut.script`). Owed: music, Premiere, export.

## Look
Status: EXPLORING (stills round 1). Jack, 2026-11-21: "show me stills, using unsplash": real-photo look, a British
post-office-style counter hall where every window says POWER; weekday daylight and strip lights, a little drab, never
glossy. Layouts (Unsplash): `V50uAd5i-Ag` (queue hall with barrier lanes), `GbY1IcKPvS0` (lanes to the counters),
`Y63M9ZI29JM` (old wooden counter window). Only readable words: POWER, 3, POSITION CLOSED, DISCOUNT APPLIED.
- Cast (portraits first): the cashier (BadCode in the navy balaclava, dressed as a 60-year-old 'Karen' at Jack's ask: a blonde
  stacked-bob wig over the mask, never covering the ring or triangle; reading glasses on a beaded chain; coral floral
  blouse; beige cardigan; pearls; blank badge; gloves. Keep him facing the camera so the triangle stays on his left eye), the woman with
  the kettle (~42, mustard raincoat), the pensioner (~75, lilac coat, fan heater), the lad (~19, ginger buzz cut, grey
  hoodie, phone on 1%), the machine (a van-sized server bank on castors, no face). No children.
- **Logo ending (Jack, 2026-11-21: "The phone charging"):** close on the lad's phone; the charging ring fills and becomes
  the BadCode ring with the red triangle, the name beneath. The real logo file is laid on in the edit; Flow only makes a
  plain phone screen with a thin white ring.
Flow project: `c0e7c075-1dc4-4d65-bd20-84860de322f8` (shown in Flow as "Nov 21 - 14:37"). Stills Nano Banana 2.1, 9:16.

## Sound
Voices (designed, gemini-3.8-flash-tts, plain; Claude's picks, Jack to veto on https://claude.ai/artifact/23LrpLyR1MAaAW1gGu4GXD):
tannoy `tannoy-a` (style "flat, automated announcement"), pensioner `pensioner-b`, cashier `cashier-a` (a stern Home
Counties woman's voice, for the Karen look). Ids in `voices/casting/designed-voices.json`. A two-tone chime before each
tannoy call. Music: not decided; any Suno track is music and sound only.

## Story-only rules
- Jack and Kai write the jokes; Claude drafts only when asked, marked as Claude's.
- Never write "post office" in a Flow prompt: it pulls in the real Post Office's branding. Say "a public counter hall".
- No children in this short (Jack, 2026-11-21: "no kids").
- The data centre is a thing, not a villain person: no real company, no logo, no real politician.
- The fact, if said: ministers plan discounts of UP TO £24 per megawatt-hour for AI data centres in AI Growth Zones from
  April 2027, still subject to legislation; ministers say other billpayers won't fund it (disputed). Never say it is
  law, never say households pay for it as fact. Re-check before posting.
- Run `scripts/variations/fresh.py --story short-the-queue` over every new prompt and line, and say the result.

## Library pieces in use
- **Real photo as the look** (Jack, "using unsplash"): an Unsplash photo is each Flow still's layout; new pictures built
  from it, never an AI figure pasted into a real photo.
- **Clean room:** prompts written by a sealed writer from one brief (`scenes/the-queue/cleanroom/`).
- **The BadCode balaclava:** the cashier. Attach `docs/brand/balaclava/mask-reference.jpg` with the line "The balaclava
  exactly as in the attached image: no holes, no skin, gloves." On a turned head check which EYE the triangle is over.

## Where the detail is
- [README.md](./README.md), [script.md](./script.md), rulings [scenes/the-queue/picks.md](./scenes/the-queue/picks.md)
