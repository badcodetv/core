# Camping — the song files

Consolidated 2026-08-27. **Three live files, one archive.** Before this, eight sheets sat side by
side and two of them could both supply lyrics to a generation — which is how the first verse ended
up carrying a cue (`[sarcastic, high pitched]`) that nobody reading `camping.md` could see.

| File | What it is | Who reads it |
|---|---|---|
| [`camping.md`](./camping.md) | **The words canon**, and the story behind them. The `` ```lyrics `` block here is the guard: every runner compares the page's words against it and refuses to spend a credit if they have drifted. **Words only — cues are not its business.** | every runner, as the guard |
| [`camping-sheet.md`](./camping-sheet.md) | **The live prompt.** Style lanes (one Style + Taste + Exclude each), the single lyric cue sheet, sliders, and the round log. Editing this file *is* editing the prompt. | [`scripts/suno/camping.mts`](../../../../scripts/suno/camping.mts) |
| [`camping-released.md`](./camping-released.md) | The released take, kept as a fidelity reference | humans |
| [`archive/`](./archive/) | Finished experiments, kept for their round logs and revert targets | nobody automated |

🥇 **The lane to start from is `modrb`** — the 1960s mod R&B holler, ruled by ear on 2026-09-08
(*"the song I liked the most"*). It carries its own lyric variant `lyricsD` and ran on **v4.5+**,
not v5.5, so reproducing it takes two edits and not one — both spelled out in the sheet.

## The one rule that matters

🔴 **Lyrics have exactly one source: `camping-sheet.md` § Lyrics.** `camping.md` owns the words;
the sheet owns the cues. If you ever find a second file supplying cues to a generation, that is the
bug — not a filing preference.

## The archive

| File | What it was |
|---|---|
| `archive/camping-halftime.md` | the half-time direction and rounds h0–h12; the accepted take `Camping HT AJ rap-rock W45 (h12)` came from here |
| `archive/camping-halftime-cover.md` | cover-mode genre overlays on that take, rounds c1–c4 (the "too early 2000s cheesy" pass, and the flair round) |
| `archive/camping-cover.md` | the earlier cover A/B set |
| `archive/camping-style.md` | the non-cover scouting set |
| `archive/camping-prompt-history.md` | what failed in each of the 17 duet rounds, and the previous cue sets as revert targets |

Their runners moved with them, to [`scripts/suno/archive/`](../../../../scripts/suno/archive/),
with their sheet paths repointed. They still run; nothing automated depends on them.
