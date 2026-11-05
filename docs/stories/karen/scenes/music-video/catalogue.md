# Karen music video: footage catalogue (2026-11-05)

Every visual file on D: for Karen, classified by look for the re-cut rule (Kai): **choruses = cartoon, verses = photographic**. Machine-readable version: [`catalogue.json`](./catalogue.json). Thumbnails (4-frame strips) and contact sheets: `D:\badcode-videos\karen-music\recut\catalogue\` (`thumbs/<id>.jpg`, `sheets/v01-v27.jpg` videos, `s01-s11.jpg` stills). Every sheet was looked at; nothing is classified from its filename.

## Counts

| Source | Videos | Stills | Cartoon | Photo | Unclear |
|---|---|---|---|---|---|
| `mv-clip` karen-music/clips | 34 | 0 | 0 | 34 | 0 |
| `mv-hitch` karen-music/clips/hitchcock (+images) | 11 | 14 | 25 | 0 | 0 |
| `mv-maybe` karen-music/clips/new maybes (+images) | 14 | 10 | 0 | 22 | 2 |
| `mv-img` karen-music/images | 0 | 37 | 0 | 37 | 0 |
| `mv-other` karen-music/other | 2 | 0 | 0 | 2 | 0 |
| `st-new` karen-story/new clips (+images) | 47 | 37 | 1 | 83 | 0 |
| `st-old` karen-story/old clips | 28 | 0 | 0 | 28 | 0 |
| `st-vids` karen-story/vids/vids (Jack) | 22 | 31 | 0 | 53 | 0 |
| **Total** | **158** | **129** | **26** | **259** | **2** |

Video seconds (identical files counted once): **cartoon 110.0 s** (11 clips), **photo 1217.8 s** (1146.4 s without the drafts flagged `working`), **unclear 16.0 s**. All video is 24 fps; music-video clips are 1920x1080, Jack's story shots mostly 3840x2160.

## The cartoon pool (choruses)

All eleven are the `hitchcock/` set: flat mid-century poster illustration, navy against amber (the story's illustrated register in look.md). Each is 10.0 s.

| id | s | shows | used in music cut now |
|---|---|---|---|
| `mv-hitch-1` | 10.0 | woman silhouette in lit phone box in rain cuts to rotary phone on empty desk, push in | 4.4-5.64, 69.84-73.4 |
| `mv-hitch-2` | 10.0 | spiralling coiled phone cord, hypnotic Vertigo-style zoom | 19.28-23.8, 25.08-27.24 |
| `mv-hitch-3` | 10.0 | top-down grid of endless cubicles/desks, slow drift | 49.96-53.6, 56.32-57.8 |
| `mv-hitch-4` | 10.0 | woman silhouette in glowing phone box on rainy street, push in | 238.64-248.64, 73.12-76.88 |
| `mv-hitch-5` | 10.0 | legs in heels walk across crosswalk, long shadow | 41.56-44 |
| `mv-hitch-6` | 10.0 | tiny figure beside towering paper stack, papers flying | 85.04-88.36 |
| `mv-hitch-7` | 10.0 | silhouettes on spotlit plinths on phones, some falling | 94-97.72 |
| `mv-hitch-9` | 10.0 | crowd of silhouettes on phones under spotlights, push in | 235.68-238.64, 105.16-108.04 |
| `mv-hitch-10` | 10.0 | looking up an endless lit office-tower atrium, tiny workers at desks, rising | 131.64-137.12 |
| `mv-hitch-11` | 10.0 | phone receiver on coiled cord sinks underwater, bubbles rising | 141.64-148.04 |
| `mv-hitch-12` | 10.0 | redhead woman silhouette at bar with martini, push past her to jazz trio on stage | 4.4-8 |

Cartoon stills (could be moved in Premiere, or animated in Flow in the same register): `mv-hitch-img-1`…`14` (the hitchcock source plates; `img-10` phone-line buttons, `img-11` rotary dial, `img-12` corridor of lit windows and `img-14` overhead figure on a dial ring have **no clip yet**; there is no `hitchcock/8.mp4`), and `st-new-img-32` (the pixel-art Sean AI government card, text-heavy).

## Unclear

- `mv-maybe-2` (8.0 s): montage: photoreal wet phone cord, illustrated corridor and street map, photoreal woman screaming into payphone. Why unclear: mixes registers inside one clip. Could be trimmed to its cartoon section for a chorus.
- `mv-maybe-3` (8.0 s): Karen in payphone on rainy street; frame morphs from photoreal to illustrated. Why unclear: style morph mid-clip. Could be trimmed to its cartoon section for a chorus.

## The photo pool (verses)

Everything else is photoreal AI (no live-action footage at all). By subject, ids only; full notes in the JSON:

- **Karen at the payphone (POV, seasons, booths, time passing)**: `mv-clip-2`, `mv-clip-9`, `mv-clip-10`, `mv-clip-11`, `mv-clip-12`, `mv-clip-13`, `mv-clip-15`, `mv-clip-16`, `mv-clip-20`, `mv-clip-33`, `mv-clip-34`, `st-new-11`, `st-new-14`, `st-new-15`, `st-new-17`, `st-new-19`, `st-new-21`, `st-new-22`, `st-new-23`, `st-new-24`, `st-new-26`, `st-new-27`, `st-new-28`, `st-new-29`, `st-new-30`, `st-new-38`, `st-new-45`, `st-new-46`, `st-old-6`, `st-old-7`, `st-old-8`, `st-old-9`, `st-old-10`, `st-old-11`, `st-old-14`, `st-old-21`, `st-old-23`, `st-vids-crowd`, `st-vids-police`, `st-vids-red-pin-map-part-1`, `st-vids-red-pin-map-red-pin-zoom-map`, `st-vids-still-on-hold`, `st-vids-time`
- **Clerks, offices, desk-behind-desk, case files**: `mv-clip-3`, `mv-clip-4`, `mv-clip-5`, `mv-clip-6`, `mv-clip-7`, `mv-clip-8`, `mv-clip-18`, `mv-clip-19`, `mv-clip-28`, `mv-clip-29`, `mv-clip-30`, `mv-clip-31`, `st-new-13`, `st-new-16`, `st-new-18`
- **President / high office / TV studio**: `mv-clip-21`, `mv-clip-27`, `mv-clip-32`, `st-new-20`, `st-new-36`, `st-new-37`, `st-old-17`, `st-old-18`, `st-old-19`, `st-old-20`
- **Aarron and the music (jazz club, street producer, Vivaldi)**: `mv-clip-1`, `mv-clip-17`, `mv-maybe-4`, `mv-other-1`, `mv-other-2`, `st-new-25`, `st-old-12`
- **Crowd, virality, aftermath**: `mv-maybe-6`, `mv-maybe-12`, `mv-maybe-14`, `st-new-7`, `st-new-31`, `st-new-33`, `st-new-34`, `st-new-35`, `st-new-41`, `st-old-13`, `st-old-22`, `st-vids-train`
- **Complaining (vendor, restaurant, neighbour, Susan)**: `mv-clip-22`, `mv-clip-23`, `mv-clip-24`, `mv-clip-25`, `mv-maybe-5`, `st-new-2`, `st-new-4`, `st-old-1`, `st-old-4`, `st-old-5`, `st-old-24`, `st-old-25`, `st-vids-cleaner`, `st-vids-water-throw`
- **Automation / Sean AI / firing**: `mv-clip-14`, `mv-clip-26`, `st-new-5`, `st-new-6`, `st-new-39`, `st-new-40`, `st-new-42`, `st-new-43`, `st-new-47`, `st-old-3`, `st-vids-ending-credits`
- **Other (walks, bar nights, maps, aerials, drafts)**: `mv-maybe-1`, `mv-maybe-7`, `mv-maybe-8`, `mv-maybe-9`, `mv-maybe-10`, `mv-maybe-11`, `mv-maybe-13`, `st-new-1`, `st-new-3`, `st-new-8`, `st-new-9`, `st-new-10`, `st-new-12`, `st-new-32`, `st-new-44`, `st-old-2`, `st-old-15`, `st-old-16`, `st-old-26`, `st-old-27`, `st-old-28`, `st-vids-cleaner-test`, `st-vids-cleaner-vid-1`, `st-vids-cleaner-vid-2`, `st-vids-opening-shot`, `st-vids-phone-throw`, `st-vids-red-pin-map-part-2`, `st-vids-seagull`, `st-vids-seagull-vid-part-1`, `st-vids-seagull-vid-part-2`, `st-vids-yellow-pin-map-part-1`, `st-vids-yellow-pin-map-part-2`, `st-vids-yellow-pin-map`

## Duplicates

Byte-identical files (md5):

- `st-new-1` = `st-vids-opening-shot`
- `st-new-2` = `st-old-1`
- `st-new-3` = `st-old-2`
- `st-new-4` = `st-vids-cleaner`
- `st-vids-ending-credits-first-frame-img` = `st-vids-still-on-hold-last-frame-of-vid-img`
- `st-vids-red-pin-map-map-reference-image-not-real-one-img` = `st-vids-yellow-pin-map-map-reference-image-not-real-one-img`

Near-identical (same shot, different take or file):
- Drafts beside finals in Jack's folders: `st-vids-cleaner-test` ≈ `st-vids-cleaner-vid-1` (cleaner turns to camera), `st-vids-cleaner-vid-2` ≈ second half of `st-vids-cleaner`; `st-vids-seagull-vid-part-1/2` = the two halves of `st-vids-seagull`; `st-vids-red-pin-map-part-1/2` and `st-vids-yellow-pin-map-part-1/2` = halves of the joined map zooms. All flagged `working`.
- `st-new-47` and `st-vids-ending-credits` are two takes of the same courthouse-to-BADCODE-windows aerial (`st-new-47` spells it complete; the other is caught mid-word).
- `st-old-23` (students rap by the bronze Karen statue) and `st-vids-still-on-hold` (aerial of the same scene) are a pair.
- Every `mv-img-*` and `mv-maybe-img-*` still is the first frame of a music clip (e.g. `mv-img-2` = `mv-clip-2`); most `st-new-img-*` are first frames of `st-new-*` clips.
- **No file is shared between the two cuts**: the music cut uses only music-folder media and the story cut only story-folder media.

## Noteworthy

- **Cartoon is short.** 110 s of cartoon video in total against ~70 s of chorus, so the choruses can be covered only by using nearly all eleven hitchcock clips, most of them at length, or by repeating some. Each clip opens on a held plate and several morph or blur mid-shot (`mv-hitch-3` breaks up around the 50% mark), so the clean usable seconds are fewer than 110. Room to grow: the 14 hitchcock stills (four have no clip), the cartoon portions of `mv-maybe-2` / `mv-maybe-3`, or new Flow clips in the same register.
- **The current music cut already mixes registers**: about 57 s of cartoon, 170 s of photo and 21 s of the two unclear clips are visible (higher tracks counted over lower ones).
- **There is no live-action footage.** "Photo" here always means photoreal AI.
- **Photo clips the music cut doesn't use:** `mv-clip-18`, `-20`, `-32`, `-34`, `mv-maybe-6`, `mv-other-1`, `mv-other-2` (the last two are Karen singing to camera with Aarron, which fits the verses). The whole story pool (~678.4 s of final takes) has never been used in the music video.
- **Defects to watch:** Veo sparkle watermark bottom-right on many story clips (`st-new-1`, `st-old-13`…`20`, `st-old-23`, `st-vids-crowd`, `-police`, `-time`, `-still-on-hold`, `-opening-shot`); readable text, some of it intended (case-file labels, SEAN AI screens, SoundCloud page, Late Night title, BADCODE windows); `st-vids-yellow-pin-map-google-earth-reference-img` looks like a real Google Earth capture: reference only, do not publish.
- `st-old-18`/`-19`/`-20`: the Late Night guest (grey-haired statesman) is the closest thing to a "President" on screen; `mv-clip-32` (senior woman in a high office picking up the phone) is the other candidate.
