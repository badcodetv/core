# The Bank Robbery — lo-fi music ledger

Sourced 2026-10-12 after Jack's note: *"the background music needs to be more chill and lofi, so
that it fits each scene's mood more, use royalty free stuff"*. Replaces the Kevin MacLeod spy/heist
cues as the candidate score.

Files: `C:\Users\jackt\OneDrive\Desktop\Youtube Vids\animation\bank robbery\music\lofi\`
(WSL: `/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/music/lofi/`)

## What is and is not verified

- **Licence: verified per track** for the twelve HoliznaCC0 files. Each track's own Free Music
  Archive page was fetched and carries the sentence "*<title>* by HoliznaCC0 is licensed under a
  CC0 1.0 Universal License" with a link to `creativecommons.org/publicdomain/zero/1.0/`. The FMA
  account is the artist's own page. The files were downloaded from the `fileUrl` on those same pages.
- **Licence: verified at catalogue level only** for the two Kevin MacLeod files. Both titles are in
  incompetech's own catalogue (`pieces.json`) and were downloaded from incompetech.com. The
  incompetech licence page generates the CC BY 4.0 credit for any title in that catalogue. There is
  no separate static per-track licence page that I could read (the per-track pages are script-rendered).
- **Nobody has listened to any of these. UNVERIFIED by ear:** mood fit, tempo feel, and "no vocals".
  Picks were made from titles, FMA genre tags and (MacLeod) the composer's own description. All
  twelve FMA pages are tagged Instrumental; that is a tag, not a listen. The mood notes below are
  guesses from those tags. Listen before cutting.
- **Content ID: UNVERIFIED.** CC0 does not stop a third party registering a track with YouTube
  Content ID. Not checked. If a claim appears, the FMA page is the evidence to dispute with.
- Measured locally with ffprobe / ffmpeg `ebur128`: duration, integrated loudness, true peak. All
  fourteen are real stereo MP3 audio.

## Ledger

| File | Slot | Artist | Title | Source item URL | Licence | Duration | Loudness (I) | Verified how |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `01-cafe-holiznacc0-morning-coffee.mp3` | 1 Opening + café | HoliznaCC0 | Morning Coffee | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/morning-coffee/ | CC0 1.0 | 3:12 | -12.2 LUFS | FMA track page read |
| `01-cafe-holiznacc0-busking-in-the-sunlight.mp3` | 1 Opening + café | HoliznaCC0 | Busking In the SunLight | https://freemusicarchive.org/music/holiznacc0/city-slacker/busking-in-the-sunlight/ | CC0 1.0 | 4:23 | -9.7 LUFS | FMA track page read |
| `02-plan-holiznacc0-busted-jazz.mp3` | 2 The plan | HoliznaCC0 | Busted Jazz | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/busted-jazz/ | CC0 1.0 | 2:29 | -9.7 LUFS | FMA track page read |
| `02-plan-holiznacc0-pretty-little-lies.mp3` | 2 The plan | HoliznaCC0 | Pretty Little Lies | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/pretty-little-lies-1/ | CC0 1.0 | 3:30 | -17.2 LUFS | FMA track page read |
| `03-night-holiznacc0-foggy-headed.mp3` | 3 The night before | HoliznaCC0 | Foggy Headed | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/foggy-headed/ | CC0 1.0 | 4:06 | -8.2 LUFS | FMA track page read |
| `03-night-holiznacc0-happy-but-a-little-off.mp3` | 3 The night before | HoliznaCC0 | Happy, but a little off | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/happy-but-a-little-off/ | CC0 1.0 | 1:57 | -13.2 LUFS | FMA track page read |
| `04-march-holiznacc0-tension-in-the-air.mp3` | 4 The march | HoliznaCC0 | Tension In The Air | https://freemusicarchive.org/music/holiznacc0/beats-from-the-crypt/tension-in-the-air/ | CC0 1.0 | 5:15 | -15.6 LUFS | FMA track page read |
| `04-march-holiznacc0-never-sleeping.mp3` | 4 The march | HoliznaCC0 | Never Sleeping ( Lofi , Dark , Sad ) | https://freemusicarchive.org/music/holiznacc0/public-domain-lofi/never-sleeping-lofi-dark-sad/ | CC0 1.0 | 3:05 | -13.2 LUFS | FMA track page read |
| `05-bank-holiznacc0-cellar-door.mp3` | 5 The bank | HoliznaCC0 | Cellar Door | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/cellar-door/ | CC0 1.0 | 2:12 | -11.2 LUFS | FMA track page read |
| `05-bank-holiznacc0-waiting-around.mp3` | 5 The bank | HoliznaCC0 | Waiting Around ( LoFi , Calm ) | https://freemusicarchive.org/music/holiznacc0/public-domain-lofi/waiting-around-lofi-calm/ | CC0 1.0 | 2:32 | -10.9 LUFS | FMA track page read |
| `05-bank-kevin-macleod-thief-in-the-night.mp3` | 5 The bank (or 2 The plan) | Kevin MacLeod | Thief in the Night | https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1600019 | CC BY 4.0 | 3:05 | -18.3 LUFS | Catalogue level: incompetech `pieces.json` + licence page. No per-track licence page read |
| `06-ending-holiznacc0-all-the-way-sad.mp3` | 6 The ending | HoliznaCC0 | All The Way Sad | https://freemusicarchive.org/music/holiznacc0/lo-fi-and-chill/all-the-way-sad/ | CC0 1.0 | 3:06 | -12.6 LUFS | FMA track page read |
| `06-ending-holiznacc0-canon-event.mp3` | 6 The ending | HoliznaCC0 | Canon Event ( Lofi , Sad , Reflection ) | https://freemusicarchive.org/music/holiznacc0/public-domain-lofi/canon-event-lofi-sad-reflection/ | CC0 1.0 | 2:33 | -14.8 LUFS | FMA track page read |
| `06-ending-kevin-macleod-dd-groove.mp3` | 6 The ending | Kevin MacLeod | DD Groove | https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100492 | CC BY 4.0 | 3:41 | -13.6 LUFS | Catalogue level: incompetech `pieces.json` + licence page. No per-track licence page read |

Licence URLs: CC0 1.0 — https://creativecommons.org/publicdomain/zero/1.0/ ·
CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/ (incompetech's statement:
https://incompetech.com/music/royalty-free/licenses/)

The two incompetech source URLs are built from the ISRC in the catalogue and were not opened in a
browser. The download URLs used were
`https://incompetech.com/music/royalty-free/mp3-royaltyfree/<Title>.mp3`.

## On-screen credits

CC0 needs no credit. We credit anyway (ruled 2026-09-12), one line covers all twelve:

```
Music by HoliznaCC0 (freemusicarchive.org/music/holiznacc0), CC0 1.0
```

Required, only if the MacLeod track is used. This is the wording incompetech's licence page generates:

```
"Thief in the Night"
Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0
http://creativecommons.org/licenses/by/4.0/
```

```
"DD Groove"
Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0
http://creativecommons.org/licenses/by/4.0/
```

## What the tags say (not heard)

| File | Tags / description at source | Notes |
| --- | --- | --- |
| Morning Coffee | lo-fi hip-hop, chill-out, easy listening, minimalism | |
| Busking In the SunLight | lo-fi hip-hop, jazz, modern jazz, soul | Loud master, very flat (LRA 1.3) |
| Busted Jazz | lo-fi hip-hop, lounge, soul | Loud master |
| Pretty Little Lies | lo-fi hip-hop, chill-out | Quietest Holizna file |
| Foggy Headed | lo-fi hip-hop, jazz, experimental pop | Loudest file, flat (LRA 1.1) |
| Happy, but a little off | lo-fi hip-hop, chill-out | Short: 1:57 |
| Tension In The Air | trip-hop, lo-fi hip-hop, goth, from a Halloween beat tape | Wide dynamics (LRA 10); may be spookier than wanted |
| Never Sleeping | lo-fi, "dark, sad" in the title | |
| Cellar Door | lo-fi hip-hop, jazz, lounge, minimalism | Wide dynamics (LRA 11.8) |
| Waiting Around | lo-fi hip-hop, "calm" | Wide dynamics (LRA 8.9) |
| Thief in the Night | 65 BPM; guitar, bass, drums, organ; "Laid-back, grooving, and cool" | Not lo-fi; a slow clean groove. Same composer as the rejected score |
| All The Way Sad | lo-fi hip-hop, minimalism, soul | |
| Canon Event | lo-fi, "sad, reflection" | |
| DD Groove | 96 BPM; guitars, drum kit, bass, organ; "indicative of a loss, or possibly carelessness" | Not lo-fi, not piano |

## Mix notes

- Integrated loudness runs from -8.2 to -18.3 LUFS, a 10 LU spread. Level each cue by ear or by
  meter under the narration; do not drop them in at one fader value.
- Most files peak at or above 0 dBFS true peak (up to +0.7). Leave headroom; they will be turned
  down under narration anyway.
- Nothing here was confirmed as rainy piano. Slot 6 is the weakest match on paper: the request was
  sad rainy lo-fi piano and the tags only say "sad".
