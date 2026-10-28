# The Bank Robbery — fifth-pass shots (8 October 2026, evening)

**Asked for by Jack, 8 October 2026,** after watching cut 3:

> "the montage bit showing everyone should only show a few it is a bit too long, also have the name on the screen
> for it to be long enough to be read. forget the way of showing stop the boats, it should be a newspaper headline
> spinning graphic made in flow to make both of them, the model house arent working. also the night before the
> robbery, they get pissed, this should funnier than it is, just a compilation of these characters drinking,
> throwing up, playing darts and pool. also the part where the person is looking out the window and the
> protest/riot looks very ai slop like, change that to more of the david lynch type of cinematography instead.
> also the image shared here should be the vibe of the protest/riot, the other clips of it looks awful, it should
> look like this, like realistic and gritty, the flares, the camera being low to make it look scary, maybe add a
> dutch angle ... it should look really disorientating and cinematic. show real footage of the cafe instead of the
> model where they talk about buying it that looks terrible. the scene with the guns looks like ai slop fix that
> please. also the cafe being sold should be the cleaner outside in the rain, like the scene in blade runner where
> he looks up at the sky and the camera pans up, once it has shown the shop being sold. keep the cool kebab shop at
> the end spelling badcode."

**The image he shared is a frame of our own `s08-march` clip** (the officer laying the barrier, second pass). That
still (`images\scenes-v2\s08-march.jpg`) was uploaded to the Flow project as `br5-riot-look` and attached to every
riot prompt as the look reference. The `s08-march` clip itself stays in the cut.

- **Settings:** Nano Banana 2, 16:9 (the two front pages 3:4), one candidate each. Flow project `63d22c4b`.
  Clips: Omni 1.1 Flash, start frame, 720p, 8 s.
- **Prompts:** stills in [`scripts/bank-robbery/br-stills-v5.json`](../../../scripts/bank-robbery/br-stills-v5.json),
  motion in [`br-clips-v5.json`](../../../scripts/bank-robbery/br-clips-v5.json). The window, the two front pages
  and `s08e-bank-noref` went through the `flow_generate_image` tool; their prompts are the same JSON bodies
  (the front pages' are in the table below, since they are not in the JSON).
- **Files:** `images\scenes-v5\` and `vids\v5\`.
- **Research used:** [`docs/google-flow/2026-10-08-anti-slop-sweep.md`](../../google-flow/2026-10-08-anti-slop-sweep.md)
  (web sweep, nothing in it tested by us) and `docs/cinematography/symptoms.md` ("It looks like AI": break one axis
  hard, one traceable light, obstruct part of the frame, one detail that could only be here).

## What each shot is for (the design, before the prompt)

| Shot | Job | Camera | Light | Foreground / the detail |
| --- | --- | --- | --- | --- |
| `s08a-placards` | Both sides hold the same sentence | On the cobbles, 20mm, steeply up, tilted | The flare on the ground, from below | The flare and a barrier leg |
| `s08c-megaphones` | Two men blame each other across an empty road | On the cobbles in the gap, 18mm, tilted | The flare, from below; dark eye sockets | Flare and a trampled cup |
| `s08e-bank` | "It's got BANK written on it" | At the foot of the bank, 16mm, steeply up | A flare out of frame, raking the stone | **The cost in frame:** a trampled placard with a boot print |
| `s09-walk` | They stroll through; nobody looks | On the cobbles in the gap, 20mm | One flare in the crowd, behind them | A police officer's yellow back fills a third |
| `s08b-remote-window` | One man decides when the row starts | Locked off, low, far back in the room; he is small and off-centre | Flare glow through the glass; one dim lamp | Lamp and dial telephone; red curtains; a wide empty floor |
| `s07d-pints`, `s07e-darts`, `s07f-pool`, `s07g-bucket` | The crew gets pissed (four gags) | A cheap camcorder, too close, tilted | Its own lamp, falling off to black | Shot glasses; darts in the wall; the balls; the chocolate fountain |
| `s05e-papers` | "Which one's true?" without the model town | 85mm between two newspapers | One bare bulb | The newspapers' backs |
| `s12g-standoff` | Guns up on the man each already hated | On the marble floor, 24mm, tilted, **full figures a way off** | One red alarm lamp behind them: rim light, dark faces | A mask and a banknote band |
| `s12h-denise-rain` | She sees the board | Knee height on the pavement, behind her | One orange street lamp | Denise's back |
| `s12i-denise-face` | She looks up | 85mm, low, below her chin | The same lamp, behind her | Rain |
| `s11e-cafe-for-sale` | The café itself, where the narrator says a price went up | Knee height across the road (reference: `s12h`, uploaded as `br5-cafe`) | Flat grey morning | A hand with tagged house keys |

**The guns:** the old plate had a pistol the size of a head at the lens. The new one keeps the pistols small, in
rim light, a corridor away. That is the whole fix: the less of a hand and a gun the model has to draw, the less it
gets wrong.

## The two front pages (3:4, made in Flow; the spin is ffmpeg)

Both prompts: "A flat, straight-on scan of the whole front page of a British tabloid newspaper, filling the frame
edge to edge, printed in black ink on cheap off-white newsprint. Across the top is a solid {royal blue | red} band
with the paper's name in heavy white capitals: "{THE DAILY TRUMPET | THE PEOPLE'S VOICE}". Under it … the headline
in enormous heavy black condensed capitals on three lines …" then one halftone photograph of a small inflatable
boat far off on a flat grey sea with nobody visible, four columns of unreadable text, no price, date or barcode.

| File | Headline | Read |
| --- | --- | --- |
| `s05f-paper-blue` | THEY'RE / LETTING / THEM IN | Spelt right, first time |
| `s05g-paper-red` | WE DESTROYED / THEIR / HOMES, then "Now you turn the victims away" | Spelt right, first time (came back on two lines) |

**The paper names are mine and are placeholders.** Jack writes the jokes. The red headline was a social media post
in the script; Jack asked for a newspaper for both.

**The spin** (`clips\cut4\c4-paper-*.mp4`): three turns in 0.9 s from a speck to full frame, landing 3° off level,
then a slow push. An ffmpeg `rotate` + `scale` + `overlay` with per-frame expressions; the command is in the
ledger. A video model would have re-drawn the words.

## Results

All sixteen stills came back first time, no blocks. Read by eye, not seen by Jack.

| File | Read |
| --- | --- |
| `s08a-placards` | Both placards spelt right. Low, tilted, flare on the cobbles. The look matches the reference |
| `s08c-megaphones` | Both men match their portraits; arms point across; flare in front |
| `s08e-bank`, `s08e-bank-noref` | **`-noref` is used:** its BANK is larger and reads at a glance, and it kept the boot-printed placard |
| `s09-walk` | The Ex walking down the gap, the officer's back, a flare behind |
| `s08b-remote-window` | Silhouette at the window, red curtains, lamp and telephone, pink and blue smoke |
| `s07d` to `s07g` | All four read as flash photographs of a bad night. The Governor with his sherry; the dart in the horse painting |
| `s05e-papers` | 🔴 **First try rejected:** one newspaper carried a real paper's masthead. Second try has none. 🟡 In it the papers hang in the foreground with no hands on them and he reads a third on the table |
| `s12g-standoff` | Three full figures, red rim light, the Presenter with a pistol on each |
| `s12h-denise-rain` | Reads. The board is small in frame but legible |
| `s12i-denise-face` | Reads as café Denise |
| `s11e-cafe-for-sale` | Same corner, window and pot plant as `s12h`; FOR SALE spelt right |
| 🟡 Mr Red's glasses | On in the megaphone, pints and papers shots; he had none at the party in the fourth pass |

What happened to each in the cut is in [`assembly.md`](./assembly.md), "Cut 4".

## Clips

Made the same evening; the run, the refusals and the standoff workaround are in [`assembly.md`](./assembly.md),
"Cut 4". Read from one frame a second:

| Clip | Read |
| --- | --- |
| `s08b-remote-window` | Holds the frame; very little moves, which suits it. Whether the remote is seen to rise is not clear at that size |
| `s08c-megaphones`, `s08e-bank`, `s08a-placards` | Smoke and flare move, lettering holds |
| `s09-walk` | He walks toward the lens. The officer in the foreground bends down to the barrier, unasked; it matches the barrier shot that precedes it |
| `s07d-pints` | Mr Blue finishes, bangs the glass and roars at 5 s; the Governor sips |
| `s07e-darts` | Throw at 3 s, arms up at 5 s |
| `s07f-pool` | Miscue, then his forehead goes down on the cloth at 3 s |
| `s07g-bucket` | Two heaves; the hand pats; the Proprietor does not move |
| `s12i-denise-face` | She tips her head back and the camera tilts up to rain in the lamp light by 7 s. The one camera move asked of the model, and it held |
| `s11e-cafe-for-sale` | Keys swing; the board holds |
