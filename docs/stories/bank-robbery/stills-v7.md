# The Bank Robbery — seventh-pass shots (9 October 2026)

**Asked for by Jack, 9 October 2026,** after cut 6. His words and the diagnosis are in
[`review-cut6.md`](./review-cut6.md). In short: the vault scene and the riot scenes re-made so each is one place
in one light, strange camera positions, and every line the listener heard as American re-made with the
speaker's own saved voice.

- **Settings, stills:** Flow project `63d22c4b`, 16:9, one candidate each. 🟡 **The model picker now reads
  "Nano Banana 2.1".** The runner asked for "Nano Banana 2" and Flow selected 2.1; plain 2 was not checked for by
  hand. Whether 2.1 costs credits on this account was not read off the page.
- **Settings, clips:** Omni 1.1 Flash, 720p, 8 s, one take. **Talking clips are Ingredients** (the still as the
  scene, the speaker's Character attached for its voice); silent clips are Frames (the still as the start frame).
- **Prompts:** [`scripts/bank-robbery/br-stills-v7.json`](../../../scripts/bank-robbery/br-stills-v7.json) and
  [`br-clips-v7.json`](../../../scripts/bank-robbery/br-clips-v7.json).
- **Files:** `images\scenes-v7\`, `vids\v7\`.
- **References attached:** `br5-riot-look` (the barrier shot Jack chose) on every riot still; **`br7-vault`**
  (new: `s11-00-vault`, the vault empty) on every vault still.
- **Research:** the two earlier sweeps, plus today's
  [`docs/google-flow/2026-10-09-crowd-vault-accent-sweep.md`](../../google-flow/2026-10-09-crowd-vault-accent-sweep.md).
  It found little that is new and nothing we tested. Used from it, all unverified: a crowd seen from above hides
  the legs that break first; money as plain banded bricks seen edge-on, never a note face; a handful of deposit
  boxes, not a wall; one fixed lamp with people moving through it.

## The design of each shot

**The vault: one room, one builder's work lamp on the floor, nothing else lit.** The lamp is low, so every shadow
goes up the wall. That is the scene's look and it does not change between shots.

| Shot | Job | Camera | The detail that could only be here |
| --- | --- | --- | --- |
| `s11-00-vault` | The place, empty. Reference only | On the floor inside, looking at the open round door | A coil of orange extension cable |
| `s11a-drill` | He is working very hard at a door | On the corridor floor at the foot of the door, looking up | Steel swarf, and a pair of polished shoes waiting at the edge |
| `s11b-key` | It opens with a key | Macro on the door face | A drill bit resting in its one scratch, beside a door key on a bit of string |
| `s11c-why` | "Why am I drilling?" | From a shelf inside the vault, looking out | Goggles pushed up, the drill hanging |
| `s11d-better` | "It looks better." | Waist height, close, looking up | The key going into his breast pocket; lamp under his chin |
| `s11e-in` | The money goes in, and the guard watches it | On the vault floor between the pallet wheels | The guard has a mug of tea |
| `s11f-count` | "Count it in the morning." | From a shelf, through a gap between two stacks | His hand flat on the stack |
| `s11g-top` | The vault filling up, under "there isn't a crime number for that" | The ceiling corner, looking down | The Fixer sitting on the empty pallet, eating |

**The riot: dusk, wet cobbles, flare light, from the first placard to the bank door.**

| Shot | Job | Camera | The detail that could only be here |
| --- | --- | --- | --- |
| `s08h-corridor` | Where everyone is: two crowds, one empty strip, and the bank at the end of it | A first-floor window, looking down and along | Pigeon spikes on the sill |
| `s08a-placards2` | The same five words, made by two different people | On the cobbles, looking up | Brush on brown box card; marker on white card |
| `s08d-presenter2` | The Presenter, his back to the bank | On the cobbles by a tripod leg | A finger on his earpiece |
| `s08f-above` | Two men filming each other while the money goes between their phones | A first-floor window, straight down | Neither phone points at the pallet |
| `s09d-door2` | The masks go on after the walk | On the lobby floor, looking out at the street | The doorman's white glove on the door |

**The gate (`shot-craft`, gate 2: a visible cost on anything grand).** The vault shots show the money as paper
being stacked by men who are bored; the riot wides show the crowd shut out behind barriers while the strip to the
bank stays empty. No shot is built to make the bank or the crew look good.

## Results

**Stills:** fifteen made (the thirteen above plus two close-ups for the standoff, below), all first time. Read by
eye; **not seen by Jack.**

| File | Read |
| --- | --- |
| `s11-00-vault` | Steel room, round door, one caged lamp on the floor, orange cable. The reference for the rest |
| `s11a-drill` | The Accountant on his knees at the door, swarf in the foreground, polished shoes at the edge. Same room |
| `s11b-key` | A door key on string in a keyhole, the drill bit resting beside it |
| `s11c-why`, `s11d-better`, `s11f-count` | Each man alone in the same room and light |
| `s11e-in` | Pallet wheels close, the guard with his mug in the doorway. 🟡 **The corridor behind him is brightly lit,** where every other shot has it black |
| `s11g-top` | From the ceiling corner: three men passing bricks, the Fixer on the pallet eating |
| `s08h-corridor` | From a window: blue flags left, red flags right, an empty strip, the bank at the top, two officers |
| `s08a-placards2` | Brush on brown card and marker on white card, the same five words, both spelt right |
| `s08d-presenter2` | The Presenter by a tripod leg, the bank and the smoke behind him |
| `s08f-above` | Red scarf and blue scarf leaning over their barriers with phones out; the pallet between them |
| `s09d-door2` | Four silhouettes pulling masks on in the doorway, the doorman's white glove in the foreground |
| `s12j-blue`, `s12k-red` | Added after Flow refused the standoff clip twice: each man close, lit by the red alarm lamp, **no pistol in frame** |

**Clips:** thirty-two attempts, twenty-seven usable files in `vids\v7\`. Run log: `vids\v7\00-run-log.txt`.

| What | Result |
| --- | --- |
| **Sixteen talking clips in Ingredients** (still as scene, speaker's Character attached, accent in the speech clause, one speaker a clip) | All sixteen came back. The listening model heard **every one as British** (`docs/listening/log/2026-10-09-133611-talk-all.md`, `…135424-talk-b.md`). 🔴 It is a machine; it has been wrong about accent before. Jack's ear decides |
| Framing in Ingredients | Kept closely in twelve. **Re-staged** in four: `s05h-table-a` (closer), `s05d-donor` (a wide of all three), `s11d-better` (square on, the door rim lost), and `s05d-bastard` (🔴 two men who are not in the film; re-made as `s05d-bastard2` from the last frame of `s05d-donor` with all three Characters attached) |
| Stumbles | `s05e-red` says "Hang on" twice (the first is cut off in the edit). `s08d-presenter2` said "high here, high here"; re-rolled once as `s08d-presenter3`, clean |
| 🔴 `s12g-talk` (the standoff, three men with pistols) | **Refused twice**, Ingredients and Frames: "This generation might violate our policies". Replaced by three close-ups with no pistol in frame (`s12j-who`, `s12k-he`, `s12j-lot`), which all passed first time |
| 🔴 `s08d-presenter2`, first wording | **Refused:** "Unable to generate videos that might cause reputational risk or misrepresent current events". Passed when "television newsreader" came out and "an actor playing a made-up character… in a made-up town" went in |
| 🟡 `s08f-above` | Flow would not accept the still as an upload, three times (`UPLOAD_REFUSED`). The same picture re-saved at 1280 wide under a new name uploaded and animated first time. Cause not found |
| Silent clips in Frames | `s11b-key`, `s11g-top`, `s08h-corridor`, `s08a-placards2`, `s08f-above`, `s09d-door2`, `s11e-in`: all stable, no prop changing shape in any of them at one frame every two seconds |

What became of each in the cut is in [`assembly.md`](./assembly.md), "Cut 7".
