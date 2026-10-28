# The Bank Robbery — tenth-pass shots (12 October 2026)

**Asked for by Jack, 12 October 2026,** after cut 9: "when it says nobody films it at 3 mins 1 second, there is a clip
of people filming, instead it should be people shouting at each other in the crowd, but make it quick, this could be
ai slop territory so make a few versions of the two sides arguing and cut them together quickly."

- **Settings, stills:** Flow project `63d22c4b`, Nano Banana 2, 16:9, one candidate each, reference `br5-riot-look`.
- **Settings, clips:** Omni 1.1 Flash, Frames, 720p, 8 s, one take, no speech.
- **Prompts:** [`scripts/bank-robbery/br-stills-v10.json`](../../../scripts/bank-robbery/br-stills-v10.json) and
  [`br-clips-v10.json`](../../../scripts/bank-robbery/br-clips-v10.json). Runners: `br-stills-v10.mjs`, `br-clips-v10.mjs`.
- **Files:** `images\scenes-v10\`, `vids\v10\`.
- **Web pass:** [`docs/google-flow/2026-10-12-shouting-faces-sweep.md`](../../google-flow/2026-10-12-shouting-faces-sweep.md).
  Thin, and nothing in it was tested by us. Used from it: the still already shows the shout at its peak, two or three
  readable faces a frame, the camera locked, and only the first second or so of each clip is used.

## The design

**Job of the run:** under "Nobody films it. Every phone in the street is pointed at a neighbour", show the two sides
busy with each other. Six shots, one second each, wide to tight.

| Order | Shot | Camera | Who is sharp |
| --- | --- | --- | --- |
| 1 | `s08m-low` | On the cobbles in the gap, steeply up, tilted; a flare by the lens | Two men over the barriers, one red, one blue |
| 2 | `s08o-row-red` | Long lens along the barrier | A man in a flat cap, red scarf, two more behind |
| 3 | `s08p-row-blue` | The same, mirrored | A woman in a rain hood, blue scarf, two more behind |
| 4 | `s08l-red` | In the crowd, past the back of a blue bobble hat | A grey-haired woman, red scarf (came back wider than asked) |
| 5 | `s08n-blue` | In the crowd, past the back of a red hat | A man in hi-vis, blue scarf, a phone held up at her (lands on "every phone") |
| 6 | `s08k-noses` | On the barrier rail, tilted | A woman in red and a man in blue, nose to nose |

**The reader rule.** Both sides are the same sort of people in the same coats, as angry as each other, and get the
same number of shots. Nobody on either side is made the fool. Light in every shot: the flare on the cobbles (pink)
against the dusk sky (blue) and amber street lamps.

## Results

- **Stills:** six, no refusal. 🟡 They carry the rounded film-frame border again; the pieces are cropped 4%.
- **Clips:** six, first take each. Read at five frames a second over the first 2.4 s: faces, teeth and hands hold.
  Seconds 2.4 to 8 of each clip were **not** read and are not used.
- 🔴 **One or two video generations were wasted.** `cast-many-v4.mjs` types into whatever mode the composer is in.
  Flow had been left in video mode, so the first still prompt made a video of the reference image, and the helper
  saved the reference as the still. Run `npx tsx br-image-mode.mts "Nano Banana 2"` before any stills run, and look at
  the first still before running the rest.
- **Nobody has watched these at speed.** I read frames only.

Where they sit in the cut: [`assembly.md`](./assembly.md), "Cut 10".
