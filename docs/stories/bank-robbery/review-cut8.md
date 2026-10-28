# The Bank Robbery — Jack's notes on cut 8, and what cut 9 does (12 October 2026)

## His words

> there is a lot of dead air, it needs to be trimmed so it is fast and funny, only pause when needed for comedic
> effect, otherwise the whole thing should be fast. also please make a new narrator, his voice is so weird, still a
> working class londoner voice but one that's more normal, also he needs to say it deadpan and straight so it's funny.
> also the background music needs to be more chill and lofi, so that it fits each scene's mood more, use royalty free
> stuff. also the newspaper bit needs to be trimmed to only the important parts, also have boats on the newspaper,
> empty dinghies, nothing too provocative, maybe use a real image on the newspaper. some of the parts in this video
> drag and are unnecessary ... keep the drunk compilation, the beginning part about england is great keep that, keep
> the badcode sign at the end in the kebab shop, as well as keeping the part where the guy buys the house above the
> shop that closes down and denise looks up at the rain. However the rest needs work. the bank scene is way better
> keep that, i think the rest is basically filler.

## How cut 8 was watched

The render was transcribed with word times (faster-whisper, `scripts/bank-robbery/words-cut8.json`), read as contact
sheets at one frame every two seconds, and laid against the timeline clip by clip. Every stretch with no words in it
was listed and either cut, shortened, or kept on purpose.

## Where the time went (cut 8 was 5:53; cut 9 is 4:31)

| Cut 8 | What it was | Cut 9 |
| --- | --- | --- |
| 0:00 to 0:05 | Café pan with nobody speaking | 2.9 s |
| 0:19 to 0:44 | Three narrator lines over held shots | Same lines, shots cut to the length of each line |
| 0:56 to 1:01 | Denise at the night window; the shut shops | **Out** (no words, and the ending shows it better) |
| 1:01 to 1:06 | Title and "three weeks earlier" | 1.9 s and 1.2 s |
| 1:15 to 1:20 | "Help at the food bank ... or consultancy." | **Pause kept**: it is the joke |
| 1:30 to 1:43 | Five name cards and two shots with no lettering | Five cards at 1.5 s; the two unlettered shots out |
| 1:55 to 2:04 | Two front pages, 5 s and 4.2 s | 2.5 s each, with the real photograph (below) |
| 2:07 to 2:14 | "I need them to reply", then 3 s of nothing | Cut on the last word |
| 2:15 to 2:18 | "Nothing. ... We put it in." | **Pause kept** |
| 2:46 to 2:58 | The drunk compilation | Kept (four shots a little shorter, the bucket whole) |
| 3:10 to 3:15 | "Remember that, because nobody on a stage is about to." | **Out** (end of narrator 17) |
| 3:15 to 3:20 | "They agree on the first line..." (narrator 18) | **Out**: the megaphone line says it |
| 3:30 to 3:34 | The two of them laughing at the window | 1.7 s |
| 4:06 to 5:03 | The bank and the strongroom | Kept. Shots under a narrator line cut to the line; Denise's three shots lose about a second in all |
| 5:03 to 5:21 | The keys; the flat above the café | Kept |
| 5:21 to 5:36 | The standoff ("This is your mess!", "for balance", "It's policy") | **Out, whole.** It is the old grey look, the only scene Jack had already called pointless, and the film now goes from "including one above a café" straight to Denise in the rain |
| 5:36 to 5:53 | Denise in the rain, looks up; the kebab shop | Kept (0.7 s off the first rain shot) |

**Mine, for Jack to rule:** cutting the standoff (narrator 32 and "It's policy" go with it), narrator 18, and the
tail of narrator 17. Each goes back as one block in `scripts/bank-robbery/build-cut9.py`.

## The narrator

Eight AI Studio voices read the café line with one note (below). Files: `narrator\v9-auditions\`. The listening model
scored all eight as working-class London; it rated **Sadaltager** most "ordinary" and most deadpan (9 and 9 of 10),
then Charon and Schedar. **Sadaltager was used.** Only a machine has judged this; the other seven are there to play.

```
Accent: British (London, working class, an ordinary bloke from Walthamstow in east London; everyday, not posh, not stagey cockney).
Style: deadpan and completely straight. A middle-aged man stating plain facts. Flat, dry, matter-of-fact, never amused, never performs or signals a joke, no smile in the voice.
Pace: brisk and even, clear articulation, short pauses.
```

Model `gemini-3.1-flash-tts-preview`. Lines: `scripts/bank-robbery/br-narration-v9.json` (the old words; line 17
shortened, line 29 in Jack's wording). Pauses inside a line longer than 0.38 s were closed to 0.38 s, except the
opening line (untouched, it is timed to the montage) and lines 8 and 14 (0.6 s, the pause carries the joke).
Finished files: `narrator\v9\`. Every line was transcribed and compared with its script; the speech model heard a
dropped H as a different word in four places ("'ate", "'ouses"), which is the accent.

## The music

All six cues are by **HoliznaCC0** (Free Music Archive, CC0 1.0), sourced and licence-checked in
[`music-lofi.md`](./music-lofi.md). The six first choices were played to the listening model before use.

| Scene | Tune | From | Why |
| --- | --- | --- | --- |
| Opening and café | Busking In the SunLight | 0:10 | Warm jazzy boom-bap. Its spoken sample (0:04, 2:11) is avoided |
| Hearing, cards, plan, garage | Busted Jazz | 0:10 | Sly guitar groove, no vocals |
| The night before | Happy, but a little off | 0:08 | Foggy Headed was heard as "far too calm" for a drinking montage |
| The march | Never Sleeping | 0:11 | Brooding, not an action cue |
| The walk, the bank, the keys | Cellar Door | 0:11 | "Mellow, sneaky, calm" |
| Denise in the rain, the kebab shop | All The Way Sad | 0:00 | Solo guitar for the rain, the beat arrives as she looks up |

Each cue is one pre-ducked WAV (`clips\cut9\m9-*.wav`): about 12 dB down under any speech, up in the clear, 0.6 to
0.8 s fades into each other on alternate tracks. No credit is required for CC0.

## The newspapers

The two front pages are the cut 4 pages with their small generated boat replaced by **one real photograph, the same
on both**: three empty inflatable dinghies moored at a quay, in black and white. Same picture, opposite headline.
Stills: `images\scenes-v9\`. The spin is ffmpeg (0.5 s in, then a slow push), 2.5 s a page.

- **Photo:** Ann Wuyts, Kos harbour, 2015, CC BY 2.0. Ledger: [`footage-dinghy.md`](./footage-dinghy.md).
- 🔴 **Credit owed on screen:** `Photo: Ann Wuyts (vintagedept) / Flickr, CC BY 2.0 — cropped and converted to black and white`
- **It is Kos, not the Channel.** No open-licence photo of empty dinghies in Kent was found. Fine on a prop front
  page; never caption it as Dover.
- The photographer's own note asks users to "be thoughtful what you use them for". Not a licence term. Jack and Kai
  should know it is there.
- A real Channel dinghy photo (Home Office, Dover, CC BY 2.0) is in the folder and was **not** used: there is a pair
  of small trainers in the boat.
