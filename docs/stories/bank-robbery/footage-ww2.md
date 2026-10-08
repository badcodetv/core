# The Bank Robbery — WW2 archive shots for the "proud to be British" montage

Sourced 2026-10-08 with the [`find-footage`](../../../.claude/skills/find-footage/SKILL.md) skill.
Seven cuts (six asked for, one spare), each one continuous shot, 1280×720, 24 fps, yuv420p,
libx264 crf 17, silent stereo 48 kHz AAC, `+faststart`. Black and white as found. **Picture only:
no source audio was used in any cut** (the audio track is `anullsrc`).

**Where the cuts are:**
`/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/clips/cut5/`

No money was spent. Nothing was taken from IWM, BFI or Pathé.

## The three source items

All three are archive.org FedFlix items. Receipts for all three already exist in
[`docs/footage/`](../../footage/README.md) from earlier sessions; no new receipt was written.

| Identifier | Film | Producer, year | Item URL |
| --- | --- | --- | --- |
| `gov.archives.arc.36070` | *The Battle of Britain* (Why We Fight no. 4), NARA ARC 36070, local id 111-OF-4 | U.S. War Department, Army Signal Corps, 1943 (dir. Frank Capra — director is from memory, **not fetched**) | https://archive.org/details/gov.archives.arc.36070 |
| `gov.fdr.25.4` | *Divide and Conquer* (Why We Fight no. 3), Part 4 | U.S. War Department; item dated 1945, creator "FDR Presidential Library" (film's release year 1943 is from memory, **not fetched**) | https://archive.org/details/gov.fdr.25.4 |
| `gov.archives.arc.39216` | *War Pictorial News* no. 213 [June 4], NARA ARC 39216, local id 208-WP-213 | 1945. NARA series "Motion Picture Films from 'War Pictorial News' Newsreels, compiled 1943–1945". The Magic Money Tree ledger records it as a **British Ministry of Information newsreel**; I did not re-verify the producer | https://archive.org/details/gov.archives.arc.39216 |

### What I actually fetched today (verified)

- `https://archive.org/metadata/<id>` for all three, live, non-empty. Each returned
  `uploader: carl@media.org`, `collection: FedFlix, usgovfilms, newsandpublicaffairs`, and
  `licenseurl: http://creativecommons.org/publicdomain/zero/1.0/` (CC0), `rights: null`.
- The item descriptions quoted in the table above (ARC numbers, local identifiers, "Office of the
  Chief Signal Officer", "War Dept. film") were read from that metadata.
- The `_512kb.mp4` derivative of each item, whole, **md5 matched** the metadata value. These were used
  only to find the shots.
- The cuts themselves come from the **original `.mpeg`** of each item, fetched as **HTTP byte ranges**
  (HTTP 206, about 45 MB per shot), not whole files. So the originals' whole-file md5
  (`4d57ed3c…` for 36070, `d5d23301…` for 39216, `95f87bb3…` for fdr.25.4) was **not** checked
  today. Every cut was looked at on a contact sheet after encoding.

### What I only read (not verified by me)

- That `carl@media.org` is Public.Resource.Org / FedFlix: from `docs/video-fx/footage-sources.md`.
- That *War Pictorial News* is British-made (MOI) and that its picture rests on the expired-Crown
  chain: from `docs/stories/magic-money-tree/footage.md` (row for `gov.archives.arc.39216`, marked
  "ruled 29 Sept"). The Crown reasoning itself (CDPA 1988 Sch. 1 para 7; Kai's ruling 2026-09-29,
  "Expired Crown copyright films are usable, 100%", picture only) is from `footage-sources.md`.
  I fetched none of the statute pages today.

## Licence basis, and the doubt that goes with it

- **`gov.archives.arc.36070` and `gov.fdr.25.4`:** U.S. War Department productions, so U.S. federal
  works (17 USC §105), on the trusted FedFlix prefix with CC0. Green by the house tier table.
- **`gov.archives.arc.39216`:** CC0 on a FedFlix item, and, if it is British MOI-made as the MMT
  ledger says, a Crown film of 1945 whose picture is covered by the 2026-09-29 ruling. Picture only.

🔴 **UNVERIFIED, and it applies to clips 01, 02, 03, 04 and 07.** The two Capra films are
*compilations*. The individual shots were not all filmed by the U.S. Army: they include British
footage whose first maker I have **not identified** for any shot (it could be Crown/MOI/service film
units, which the Crown ruling covers, or British commercial newsreel or feature-film material, which
it does not). `footage-sources.md` itself warns that a NARA/FedFlix public-domain tag reflects the
**US** position. I am treating these as green because the house procedure does (step 4, "compiled
by the US", and the existing ledger rows), not because I traced each shot. Capra compilations also
mix actuality with staged material: the pilots' scramble (02) in particular looks staged for camera.
I do not know whether it is.

🟡 **People in frame.** Clips 03, 04, 05 and 07 show identifiable ordinary people (no politicians,
no dead). In a montage that mocks flag-waving that is Kai's or Jack's call, not a licence question.

## The clips

Timecodes are **presentation timestamps in the original `.mpeg`** of each item (the `_512kb.mp4`
derivative runs about one second earlier). They are accurate to roughly a frame or two.

| # | File | Source | Timecode in original | Length | What is visible | sha256 of the cut |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | `ww2-01-spitfires-formation.mp4` | `gov.archives.arc.36070` | 17:23.00 – 17:25.50 | 2.5 s | Air-to-air: a formation of Spitfires over fields and cloud | `002a4cf35d8adc963067402316e87ef74450ac7fd507741d56a2a1bc2fc554c1` |
| 02 | `ww2-02-pilots-scramble.mp4` | `gov.archives.arc.36070` | 13:48.40 – 13:50.90 | 2.5 s | RAF pilots in life jackets sprinting away from camera to a line of fighters | `e43570f23fc3cad7209bedc4cf981e1d158aa677b4ba1418c3e170056317e616` |
| 03 | `ww2-03-home-guard-marching.mp4` | `gov.archives.arc.36070` | 11:00.50 – 11:03.00 | 2.5 s | Four men in battledress with rifles marching up a village lane towards camera, smiling (the film's Home Guard sequence) | `1bc9951ac7c644bf2273623628acda4e512e4e3a9cbfde777632421c76f1e17b` |
| 04 | `ww2-04-dunkirk-tommies-grinning.mp4` | `gov.fdr.25.4` | 05:04.50 – 05:07.00 | 2.5 s | Packed deck of British soldiers in tin hats grinning up at the camera (the Dunkirk evacuation block) | `29879553fd73ce58dc777bb846cda06252a37b1c679b010e49507ae8c71d37e2` |
| 05 | `ww2-05-ve-day-crowd-union-jacks.mp4` | `gov.archives.arc.39216` | 07:01.90 – 07:04.50 | 2.625 s | Camera tilts down a dense cheering London crowd to waving Union Jacks | `d455bc6da7103ba8e844d963a77f43fb0766800d1a3ccabc3d0139479a55cd9a` |
| 06 | `ww2-06-st-pauls-floodlit-ve-night.mp4` | `gov.archives.arc.39216` | 09:26.50 – 09:29.00 | 2.5 s | St Paul's dome and towers floodlit against a black sky, slow tilt. **This is the victory night, not the Blitz** | `fef74380963c49e73a34e61697ba233a3ec7b9a296428f64ed3a81696b2e71a7` |
| 07 (spare) | `ww2-07-tea-in-the-rubble-spare.mp4` | `gov.archives.arc.36070` | 29:53.35 – 29:55.85 | 2.5 s | Two men drinking from mugs in front of a bombed roof while a third climbs a ladder. **I cannot tell whether it is tea or beer** | `0be86192d25d9541615c279941b617857a3e8e18d8b8a580095858a0907100aa` |

"London" for clip 05 is from the item description (part 3, crowds outside Buckingham Palace) and
the surrounding shots of Trafalgar Square; the exact street in this shot is not identified.

## How each cut was made

Deinterlace (`fieldmatch,yadif=deint=interlaced,decimate` for the two Capra items, which are
3:2 telecined; plain `yadif` for War Pictorial News, which is not cleanly telecined), scale the 4:3
picture to 1280×960, centre-ish crop to 1280×720 (crop to fill, no pillar bars; the vertical offset
was chosen per shot), `fps=24`. About a quarter of the original frame height is lost to the crop.
Clip 04's source is only 368×480 coded, so it is the softest.

## Credit strings

None of the three items carries an attribution requirement (CC0 / US federal work). These are
**courtesy credits composed by me**, not strings a licence dictates:

- Clips 01, 02, 03, 07: `The Battle of Britain (1943), U.S. War Department. U.S. National Archives, ARC 36070, via archive.org`
- Clip 04: `Divide and Conquer (U.S. War Department). FDR Presidential Library, via archive.org`
- Clips 05, 06: `War Pictorial News No. 213 (1945). U.S. National Archives, ARC 39216, via archive.org`

## Looked at and not used

- `1946-06-10_Allied_Victory_Parade` (Universal Newsreels): the London victory parade is 1946, not
  wartime; not needed.
- `1942_Dover`, `gov.ntis.ava06858vnb1` (*Know Your Ally: Britain*), `gov.archives.arc.38651`
  (*Listen to Britain*): metadata fetched, films not watched.
- No St Paul's-in-the-Blitz shot was found that reads in one second; the Battle of Britain fire
  sequences (about 48:00–50:10) are mostly near-black.
