# The Bank Robbery — WW2 *action* archive for the short's opening

Sourced 2026-10-15 with the [`find-footage`](../../../.claude/skills/find-footage/SKILL.md) skill,
because Jack wanted the opening more action-heavy than the calm montage in
[`footage-ww2.md`](./footage-ww2.md). Seven cuts. Each is one continuous shot of British forces in
action against the Germans, and one of them (`wa-end`) is the ending shot whose last frame becomes
the oil painting. Each cut is 1280×720, 24 fps, yuv420p, libx264 crf 17, with silent stereo 48 kHz
AAC (`anullsrc`) and `+faststart`. The footage is black and white, as found. **Picture only: no source
audio was used in any cut.**

**Where the cuts are:**
`/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/clips/short3/archive/`
(plus `contact.png` and `wa-end-alamein-soldier-through-smoke-last.png`)

No money was spent. Nothing was taken from IWM, BFI or Pathé.

## The source items

| Identifier | Film | Producer, year | Item URL |
| --- | --- | --- | --- |
| `gov.dod.dimoc.30126` | *Battle of North Africa, Part 1*, DoD PIN 30126 | US Army, *The Big Picture* TV series (end card: "Produced by Army Pictorial Center… Presented by the United States Army"); metadata date 1960 | https://archive.org/details/gov.dod.dimoc.30126 |
| `gov.fdr.25.4` | *Divide and Conquer* (Why We Fight no. 3), Part 4 | U.S. War Department (already in `footage-ww2.md`) | https://archive.org/details/gov.fdr.25.4 |
| `gov.archives.arc.39174` | *War Pictorial News* no. 91, NARA ARC 39174, local id 208-WP-91 | 1943. Same NARA series as no. 213 in `footage-ww2.md` | https://archive.org/details/gov.archives.arc.39174 |

New receipts written today: `docs/footage/archive.org--gov.dod.dimoc.30126.json`,
`…--gov.archives.arc.39174.json` and `…--gov.archives.arc.39141.json` (the last was watched and not
used). I also added ledger rows to `docs/footage/README.md`.

### What I actually fetched today (verified)

- `https://archive.org/metadata/<id>` for all three, live and non-empty. Each returned
  `uploader: carl@media.org`, `collection: FedFlix, usgovfilms, newsandpublicaffairs`,
  `licenseurl: http://creativecommons.org/publicdomain/zero/1.0/` (CC0).
- The `_512kb.mp4` derivative of each item, whole, **md5 matched** the metadata. These were used only
  to find the shots.
- The cuts come from the **original `.mpeg`** of each item, fetched as **HTTP byte ranges** (HTTP
  206, 23 to 96 MB per window), not whole files. So the originals' whole-file md5 was **not**
  checked. Every cut was looked at frame by frame (0.1 s contact sheets) before it was chosen, then
  again on `contact.png` after encoding. An ffmpeg scene-change pass (threshold 0.3) found **no cut
  inside any clip**.
- The end card of `gov.dod.dimoc.30126` reads "Produced by Army Pictorial Center" and "was Presented
  by the United States Army" (seen on my contact sheet at about 28:00).

### What I only read, or infer (not verified)

- 🔴 **The Alamein shots were not filmed by the US Army.** *Battle of North Africa* is a 1960
  compilation. Its El Alamein sequence (22:24 to 25:48) shows British Eighth Army troops, and the
  shots look like the well-known ones from ***Desert Victory*** (1943, Army Film and Photographic
  Unit / Ministry of Information), but **that is from memory, and I traced no shot to it.** If they
  are *Desert Victory*, the picture is a 1943 Crown film, which is covered by the 2026-09-29 ruling
  (picture only). If any shot came from a commercial newsreel instead, that ruling does not cover
  it. I am treating these shots as green on the same basis `footage-ww2.md` used for the Capra
  compilations (the house procedure's "compiled by the US"), **not because I traced them**.
- 🔴 **Some of them may be staged.** It is widely said that *Desert Victory*'s night-barrage and
  infantry-advance shots include material re-staged for the camera. `wa-end`, `wa-02` and `wa-05`
  look like that kind of shot: the camera is low and in front of advancing men, and the smoke is
  dense and carefully composed. This is **from memory and unverified**. It is not a licence
  question, but don't caption any of them as "actual combat".
- The Dunkirk Stuka shot (`wa-01`) is inside a Capra compilation, so the same compilation doubt
  applies. I do not know who first filmed it, or whether it was filmed at Dunkirk at all.
- That *War Pictorial News* is British-made (MOI) comes from the MMT ledger via `footage-ww2.md`.
  I did not re-verify it. The tank in `wa-03` is from the issue's Libya and Tripoli story (title card
  "The Last Lap"). That it is British armour comes from the NARA description ("Brit. tanks cross a
  desert area"), not from identifying the tank.
- I did not identify any vehicle by type myself. The tank in `wa-04` *looks like* a Crusader. That is
  my guess, and the filename uses it.
- `wa-end` shows a lone infantryman in silhouette. That he is British is **inferred from context**:
  he is in the Alamein advance sequence, between shots of men in Brodie helmets. In silhouette the
  helmet shape alone does not settle it.

## Licence basis

All three items are CC0 on the trusted FedFlix prefix (`carl@media.org`). `gov.fdr.25.4` and
`gov.dod.dimoc.30126` are US War Department / US Army productions (17 USC §105). That makes all three
green by the house tier table, **with the compilation doubt above** for every shot from 30126 and
25.4. If the underlying footage is British Crown film of 1940–43, its picture is clear under the
2026-09-29 ruling either way. The only route that fails is commercial newsreel material, and I have no
evidence of any.

🟡 **People in frame.** No one is identifiable: every figure is in silhouette, at distance, or seen
from behind. There are no faces in close-up and no dead. **One note on `wa-06`:** a shell bursts beside
two advancing soldiers and they go to ground. In the last half-second they are low in the dust. I
trimmed the cut at 1.58 s so it ends before they are lying flat. Even so, someone could read it as
men being hit. Kai's or Jack's call.

## The clips

Timecodes are **presentation timestamps in the original `.mpeg`**, the same convention as
`footage-ww2.md`. Each original has `start_time` 1.0 s, so the `_512kb.mp4` derivative runs exactly
1.0 s earlier. They are accurate to about a frame. "Crop" is the vertical offset of the 1280×720
window taken from the picture scaled to 1280×960.

| # | File | Source | Timecode in original | Length | What is visible | sha256 of the cut |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | `wa-01-dunkirk-stuka-bombs-beach.mp4` | `gov.fdr.25.4` | 04:00.05 – 04:02.15 | 2.125 s | A Stuka dives over a line of silhouetted troops under black smoke. The bomb bursts and fills the frame (the Dunkirk block) | `5942a7733f6acd16a5c03cf1ce8ef526be6d430342bbd5ca19f1c75ab61d3b1b` |
| 02 | `wa-02-alamein-infantry-advance-smoke.mp4` | `gov.dod.dimoc.30126` | 22:35.40 – 22:37.90 | 2.5 s | Infantry advance at a crouch through barbed wire under black smoke. Shell smoke rises behind them | `2f06a6f3b990fa22f9db665376d2862e926109b16006416893b1d533f0b896ff` |
| 03 | `wa-03-desert-tank-through-shellburst.mp4` | `gov.archives.arc.39174` | 00:35.10 – 00:37.60 | 2.5 s | A tank drives through a big shell burst on the open desert, throwing dust and debris | `e7e2bcd9434e07fc2a35783335626f56d9a749388638b88bda821c758a059d43` |
| 04 | `wa-04-alamein-crusader-tank-charge.mp4` | `gov.dod.dimoc.30126` | 25:00.60 – 25:03.25 | 2.667 s | A cruiser tank charges out of the dust and past the lens. It ends in a motion-blur wipe | `448efd248c239bceac8f1bde3402caaa309c669bf8f4ca762b3de5bf63d5f4f3` |
| 05 | `wa-05-alamein-bayonet-charge.mp4` | `gov.dod.dimoc.30126` | 24:50.58 – 24:52.98 | 2.417 s | Soldiers in Brodie helmets charge with fixed bayonets past the camera, in silhouette against the smoke | `54a574e3dd74c423899421a609117fe4956ec8b1d0b15ccde8e1f386498004c7` |
| 06 | `wa-06-alamein-advance-shell-burst.mp4` | `gov.dod.dimoc.30126` | 25:25.06 – 25:26.65 | 1.583 s | Two soldiers with slung rifles walk away from camera. A shell bursts between them and they drop. See the note above | `41ca02b25d468684673d5700f7debb00bb2adb37116ad6480da22213a8501369` |
| **end** | `wa-end-alamein-soldier-through-smoke.mp4` | `gov.dod.dimoc.30126` | 24:28.97 – 24:30.78 | 1.792 s | A lone infantryman in silhouette strides through billowing white smoke with his rifle slung. The last frame is mid-stride | `628a023473fb7d4510acde7042ee6992e21258f87dd8e8f4b65fe9269a6a40fa` |

Last frame of the end shot: `wa-end-alamein-soldier-through-smoke-last.png`, 1280×720, sha256
`6ed3d59616883e513c358dcefa7d490e5eb49a04331511864388b2f512611aad`. Its source frame is at about
24:30.74 in the original. **Why this one is the ending:** it has one figure, sharp and fully readable,
with legs at full stride, the rifle in silhouette, head to boots in frame, and the smoke rolling
behind. It is a high-contrast silhouette, so it will take an oil-painting treatment cleanly. The
shot's earlier frames are similar but have more smoke over him. Near-identical alternates exist at
24:36–24:38 (two men climbing over a parapet with bayonets) and 25:22.5 (a lone figure in dust),
neither encoded.

## How each cut was made

The source was decoded from the byte-range chunk with `-copyts`, so the trim times are absolute
presentation timestamps. Deinterlacing: `fieldmatch,yadif=deint=interlaced,decimate` for 30126 and
25.4 (field order `tt`, 3:2 telecined), and plain `yadif` for *War Pictorial News* (field order `bb`).
Each picture was then scaled to 1280×960 and cropped to 1280×720 with a per-shot vertical offset (01:
80, 02: 120, 03: 180, 04: 120, 05: 100, 06: 100). Then `fps=24`. The end shot was scaled to 1312×984
and cropped at x 26, y 120, to remove a dark film-edge bar on the left. That is a 2.5% zoom, so it is
very slightly tighter than the others. The originals are 720×480 coded (368×480 for 25.4, so `wa-01`
is the softest).

## Credit strings

No attribution is required (CC0 / US federal work). These are **courtesy credits I composed**:

- 02, 04, 05, 06, end: `Battle of North Africa, Part 1 (The Big Picture), U.S. Army. Via archive.org (DoD PIN 30126)`
- 01: `Divide and Conquer (U.S. War Department). FDR Presidential Library, via archive.org`
- 03: `War Pictorial News No. 91 (1943). U.S. National Archives, ARC 39174, via archive.org`

## Looked at and not used

- `gov.archives.arc.39141` (*United News* roll 1023, 1944): British and Canadian troops at Overloon,
  including a tank destroyer firing at 02:21–02:23 (PTS) and a mortar crew. Every action shot is under
  1.5 s, so I used none.
- Further shots in 30126 that would cut in: a bayonet run at 22:32.9–22:34.2 (1.3 s, too short); a
  heavy gun firing at 24:10 and 24:13 (each about 1.3 s); infantry rising from a trench, 24:17–24:22;
  an aircraft hit on gun-camera, about 23:28–23:40 (not checked for which side).
  Earlier parts of the film are Italian and German footage (Oran, Graziani's advance, Rommel's
  arrival), so check which side is in any shot before using it.
- *War Pictorial News* no. 91 also has a Beaufighter strafing a ship at sea (about 04:19–04:23 PTS).
  It is good, but small in frame.
- `gov.ntis.ava02725vnb1` and `gov.dod.dimoc.20363` (*The True Glory*, 1945, joint US/UK): both
  live, CC0, about 81 min. I downloaded the 512kb file and did not watch it. Probably the best source
  for Normandy-to-Germany combat if more is wanted.
- `gov.archives.arc.36070` (*The Battle of Britain*): downloaded, not re-watched for action today.
