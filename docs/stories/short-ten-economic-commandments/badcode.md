# Ten Economic Commandments

> Read this first for any work on this story. It is everything that applies to it. Nothing from another
> story, from memory, or from a shared doc's examples applies unless it is written here.
> Library pieces this story uses are listed below; nothing else from `docs/library/` applies.

## What it is
A BadCode short (9:16, 74 s): a 90s East Coast rap inspired by a famous "ten commandments" track, about who controls the
money printer. All ten numbered rules (Jack's lyric, 2026-11-19), then the fix. The point: whoever holds the money printer
will get high on their own supply; the fix is that no human controls the printer.

**State (2026-11-20):** rough cut 3, the **62 s version** (`scripts/shorts/tec_cut_r3.py`, `<media>/cut/r3/`), on the timeline page
https://claude.ai/artifact/2vysJs9o1JJyPC4HztqzjG, awaiting Jack. All ten rules and the fix, no beat-out; each rule cuts from BadCode
rapping on location (number bar) to a rough-cut-1 clip (next bar); logo on the last bar. "Add the clips from the last version on top"
was read as intercut (a guess, flagged on the page). Rapping takes default to a until Jack's round-5 picks on
https://claude.ai/artifact/5CWLPYrPzkLK9fjHd9vvzf are read (dump `picks`, then `tec_cut_r3.py --picks <json>`). Rough cut 2 (74 s,
`tec_cut_r2.py`, `<media>/cut/r2/`) is kept. In Premiere as `short-ten-economic-commandments-1-tec-r3` (23 finished shots frozen in `premiere/r3/`, in sync, saved) and on
Drive (agreed list). Open: lyric captions; bodega neon reads LOTTO / ATM; export from Premiere + delivery QC. Rough cut 1 (old 29 s song) is in Premiere as `short-ten-economic-commandments-1-tec-r1` and is superseded.

## Look
- Status: the 2026-11-19 look is BadCode rapping on real-NYC-style locations, rebuilt in Flow from Jack's Unsplash photos, with
  the nightfever finish (below). Everything from here to the Sound section down to "Stills Nano Banana 2" is the rough-cut-1 look, kept as history.
- Settings from Jack's four reference photos (an 80s NYC fence-and-bench street portrait, a subway platform with a train
  blurring past, a dusk street crowd with traffic-light bokeh, a cobbled street framed on a suspension-bridge tower);
  they sit in `reference/` in the media folder. The subway photo carries stock watermarks: describe it, never attach it.
- The BadCode figure: a street-interviewer's outfit and posture (a baggy beige thrift suit, a plain cap, a street-interview
  mic), never a real person's name or face; the BadCode balaclava covers the face. No skin anywhere: full-length trousers,
  black socks, a black roll-neck, gloves into the cuffs.
- Picks: RU4-1-b (doorstep, chalkboard), RU4-2-a (red studio), RU4-3-a (fence bench), RU4-5-b (dusk crowd, mic),
  SU4-1-a (subway, banknotes), SU4-3-b (bridge street, falling notes), FX4-1-b (streetlight, empty gloved hands).
  FX5-a / FX5-b (fire-escape wide redone) are on the board, unpicked.
- Stills Nano Banana 2.1; clips Omni 1.2 Flash, Frames, 9:16, 8 s. Flow project `17b708f8-d9d6-41ae-b562-8d161797b542`.

## Sound
- **PICKED 2026-11-19 (Jack, all ten):** `tec-all10-A-number-gets-its-bar` take 2, https://suno.com/song/e689e000-f4db-43c0-85cb-2388d4f866ef
  (1:14; round `songs/r4a-rap`, prompt verbatim in its `round.json`; lyric `songs/r4a-rap/lyrics.txt`). The jazz1 rapper slowed, each
  number on its own bar. Replaces jazz1 for the cut. Recorded: `<media>/audio/tec-all10-a-number-gets-its-bar-v6-w25-e689e000.wav`.
  Grid (scripts/beat-grid.py): 89.1 BPM, bar 2.6935 s, first downbeat 2.0317 s. Rules start (Whisper; two-four estimated):
  Uno 6.2, two ~12.3, three ~17.4, four ~22.6, five 28.2, six 32.5, seven 37.4, eight 43.1, nine 47.4, ten 52.2, fix 58.4;
  vocals end 61.0, beat out to 74.4.
- Before (rough cut 1): the rap = **jazz1**, Suno https://suno.com/song/e4cb9be5-5c68-484d-ace0-e0fed5592f59 (round
  `songs/r2-rap`, writer `jazz-phrasing`; prompt verbatim in `songs/r2-rap/round.json`). v6, Duration set 20 s, came back 29.0 s.
- jazz1 sections: intro 0-5, rule one 5-10, rule two 10-15, rule three 15-21, the fix 21-24, beat out to 29.
- jazz1 lyrics: [songs/r2-rap/lyrics.txt](./songs/r2-rap/lyrics.txt), three rules numbered 1-3 plus "And the fix, from the future? No hand on the printer."
- Vocals are wanted on this short (a rapped male vocal); no other voices.

- **Finish (Jack, 2026-11-19, stills page round 4): nightfever** (`scripts/shorts/tec_finish.sh nightfever`): heavy glow, red light streaks, saturated night; "lots of lights, kind of like taxi driver, where it's kind of overwhelming". The logo card is never filtered.
- **Rapping motion:** clean-room `scenes/ten-economic-commandments/cleanroom/perform-r8.json` (a = big chops and pointing, b = laid
  back), clips `video/ec-r8-<location>-<take>-*.mp4`, 22 of them. The writer found no proven way to make Flow move on the beat.
- **BadCode on location (round 4 picks):** Empire State top F7-fix1-a, Wall Street F7-r3-press2-a (sign lettered by hand), bodega F7-vibe6-b, columns F6-r10-bailout2-b, walkway F6-vibe3-b, boombox F6-vibe4-b, court F6-vibe7-a, taxi F6-vibe8-a, fire escape F6-vibe9-b, stoop seated F8-vibe2 (a or b). All new Flow pictures built from Jack's Unsplash photos as layout guides; never an AI figure pasted into a real photo.

## Story-only rules
- Never write "trousers a little too short" (or anything that bares ankles, wrists or neck) for the figure.
- When fixing masks, attach the still only: with the navy mask reference attached the masks turned navy.
- No real rapper or real currency in any still. Blur the fast-food logo on RU2-a-a if it is ever used.
- Check every clip at three frames for suit, cap, mask and no skin; a clip that turns side-on late is used from its start.
- The logo is a card at the tail, laid in by the edit. `marketing-gatekeeper` before posting.

## Flow project
- `17b708f8-d9d6-41ae-b562-8d161797b542` — scenes/ten-economic-commandments

Open the part's project before its first Flow call; never use it for another story.

## Library pieces in use
- none yet

## Where the detail is
- [README.md](./README.md), [look.md](./look.md), [sound.md](./sound.md)
- Rulings: [scenes/ten-economic-commandments/picks.md](./scenes/ten-economic-commandments/picks.md); takes: [songs/r2-rap/takes.md](./songs/r2-rap/takes.md)
- Timeline https://claude.ai/artifact/2vysJs9o1JJyPC4HztqzjG · stills, clips and filters https://claude.ai/artifact/5CWLPYrPzkLK9fjHd9vvzf · mood board https://claude.ai/artifact/DL4FFqF8ia1K2GerAX4uBi · rap picks https://claude.ai/artifact/8g5haV7wncRBKwKmtgcPaR
