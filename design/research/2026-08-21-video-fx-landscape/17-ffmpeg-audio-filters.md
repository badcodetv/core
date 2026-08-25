# ffmpeg audio: mixing narration over music, ducking, loudness, cleanup

## What this covers

The audio half `docs/flow/post-production.md` never touches — that file only ever *strips*
audio from Flow clips (§3.1, `-an`). This is the scripted route to mix a Suno bed with
narration, duck music under speech, master to a delivery loudness target, clean up narration,
and keep audio synced through §3.7's retiming. `11-audio-ducking-denoise-narration-mix.md`
covers the same job from Premiere's GUI (Essential Sound, DeNoise, Enhance Speech) — this is
its ffmpeg counterpart, naming the same `sidechaincompress`/`loudnorm`/`acrossfade` filters
that file only gestures at.

All filters were confirmed present via `ffmpeg -filters` (4.4.2-0ubuntu0.22.04.1,
`--enable-librubberband`). Every **TESTED** skeleton ran against synthetic tone WAVs
(`sine=` via `-f lavfi`) in the scratchpad, not real Suno/Flow audio — treat levels/thresholds
as starting points, not final numbers.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Duck music under narration | `sidechaincompress` | Narration feeds the sidechain input, compresses the music stream | free |
| Two-track mix | `amix` | Sums N inputs; `duration=`/`weights=` control length/balance | free |
| Multi-channel merge (not sum) | `amerge` | Interleaves N streams into one wider-channel stream | free |
| Master to platform loudness | `loudnorm`, two-pass | Pass 1 measures, pass 2 applies the measured values | free |
| Fade in/out a track | `afade` | `t=in`/`t=out`, start + duration, choose a curve | free |
| Crossfade two tracks | `acrossfade` | Overlaps A's tail with B's head over `d` seconds | free |
| Gain automation without keyframes | `volume` `eval=frame` | Time/sample gain expression | free |
| Cut rumble / hiss | `highpass` / `lowpass` | 3dB-point single-pole filters, cheap first pass | free |
| Surgical EQ | `equalizer` / `anequalizer` | Peaking band at `f=`/`w=`/`g=`; multi-band variant | free |
| Broadband denoise | `afftdn` | FFT spectral denoiser, `nf=` noise floor in dB | free |
| Gentler denoise | `anlmdn` | Non-local-means, `s=` strength | free |
| Trim dead air | `silenceremove` | Threshold + duration gates removal | free |
| Offset a track in time | `adelay` | Per-channel ms delays, `\|`-separated | free |
| Fix AV drift after a retime | `aresample=async=` | Stretches/trims to match timestamps | free |
| Time-stretch, no pitch shift | `rubberband` | `tempo=` ratio; no `atempo` artefacts at extremes | free |
| Isolated stem from a Suno track | Suno "Get Stems" | Not ffmpeg — Suno UI, download WAV, mix with filters above | included in plan |

## Named tools

### `sidechaincompress`
Two-input compressor: input 2 controls gain reduction on input 1 — the ducking mechanism.
Free, ffmpeg core (checked 2026-08-21). CLI, any platform ffmpeg runs on. Mature — the same
technique Premiere's Essential Sound auto-ducking wraps in a GUI (file 11), scripted here.

### `loudnorm`
EBU R128 loudness normalizer with true-peak limiting; single-pass "dynamic" or two-pass
(measure then apply, accurate). Free, ffmpeg core. CLI. The de facto ffmpeg loudness standard,
documented on ffmpeg.org's own filter reference.

### `amix` / `amerge`
`amix` sums N streams with per-input weights and a `duration=` policy; `amerge` concatenates
channels (2 mono → 1 stereo) without summing levels. Free, ffmpeg core. CLI. Both mature —
`amix` to blend mixes, `amerge` to build a multichannel bus from mono sources.

### `afade` / `acrossfade`
`afade` ramps gain in/out on a chosen curve (15 curve shapes in this build: `tri`, `qsin`,
`exp`, `log`, …); `acrossfade` overlaps two tracks with independent curves per side. Free,
ffmpeg core. CLI. Mature; `qsin`/`hsin` approximate Premiere's "Constant Power" crossfade
(file 11) — no filter is literally named equal-power, and formal equivalence beyond the
curve-shape similarity is unsourced (gap).

### `highpass` / `lowpass` / `equalizer` / `anequalizer`
Single-pole `highpass`/`lowpass` for cheap rumble/hiss cuts; `equalizer` (one peaking band);
`anequalizer` (many bands, higher-order). Free, ffmpeg core. CLI. Standard corrective EQ, not a
de-esser or multiband compressor substitute.

### `afftdn` / `anlmdn`
`afftdn` is FFT-domain spectral-subtraction denoise (`nf=` assumed noise floor in dB);
`anlmdn` is non-local-means (patch-similarity, gentler, less "watery" than spectral
subtraction). Free, ffmpeg core. CLI. Both documented ffmpeg algorithms, neither a learned/AI
model like Adobe's Enhance Speech (file 11) — no independent ffmpeg-vs-Enhance-Speech quality
comparison found (gap).

### `silenceremove`
Gates and strips silent regions by start/stop threshold and duration; trims edges or (with
`stop_periods`) closes mid-file gaps. Free, ffmpeg core. CLI. Mature, standard.

### `rubberband`
Rubber Band Library's time-stretch/pitch-shift, present because this build was compiled
`--enable-librubberband` (confirmed in `ffmpeg -version`). `tempo=` changes speed while
holding pitch. Free (GPL/commercial dual-licence upstream; the ffmpeg filter path is free),
wherever this ffmpeg build runs. `atempo` is capped 0.5–2.0× per instance and pitch-shifts
audibly at extremes (ffmpeg docs); Rubber Band's broader "reference implementation"
reputation is asserted by its wide use elsewhere (Audacity and similar) but has no single
citation gathered here (gap).

### Suno stem extraction
Not ffmpeg — Suno's Library → More Actions → Get Stems, already documented in file 11 and
`docs/suno-gpt/`. Named here because "stem layering from Suno" means: pull stems in Suno's UI,
then mix with the filters above.

## Automation hook

**Premiere side:** ducking, EQ, denoise and crossfade all map to native Premiere
effects/panels, not standalone match-name effects needing the UXP bridge — see file 11 for
click-paths and `AudioComponentChain` limits. If the bridge ever needs to touch audio effects
directly: list effects, filter for "Ducking"/"DeNoise"/"DeReverb"/"Parametric Equalizer" via
`getMatchNames()` (unrun here — no Premiere session in this pass, gap).

**ffmpeg side** — skeletons only, run against synthetic tones in the scratchpad:

```bash
# Duck music under narration — TESTED (levels need re-tuning by ear on real audio)
ffmpeg -i music.wav -i narration.wav -filter_complex \
 "[1:a]asplit=2[sc][voice];\
  [0:a][sc]sidechaincompress=threshold=0.05:ratio=8:attack=5:release=300[ducked];\
  [ducked][voice]amix=inputs=2:duration=first:weights='1 1'" out.wav
```
⚠️ Pad the shorter input with `apad` first — see Traps.

```bash
# Two-pass loudnorm — TESTED
ffmpeg -i mix.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -
# read measured_I/measured_TP/measured_LRA/measured_thresh from stderr, then:
ffmpeg -i mix.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=<i>:measured_TP=<tp>:\
measured_LRA=<lra>:measured_thresh=<th>:linear=true -ar 48000 out.wav
```

```bash
# afade / acrossfade — TESTED
ffmpeg -i in.wav -af "afade=t=in:st=0:d=1,afade=t=out:st=5:d=1" out.wav
ffmpeg -i a.wav -i b.wav -filter_complex "acrossfade=d=1:c1=tri:c2=tri" out.wav
```

```bash
# EQ + denoise for narration — TESTED
ffmpeg -i narration.wav -af \
 "highpass=f=80,lowpass=f=12000,equalizer=f=3000:t=q:w=1:g=3,afftdn=nf=-25" out.wav
ffmpeg -i narration.wav -af anlmdn=s=0.0001 out.wav   # gentler alternative
```

```bash
# trim dead air — TESTED
ffmpeg -i narration.wav -af \
 silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.1:detection=peak out.wav
```

```bash
# offset / fix drift after a §3.7 retime — TESTED (adelay); UNTESTED (aresample on a real retimed clip)
ffmpeg -i narration.wav -af "adelay=delays=500|500" out.wav
ffmpeg -i drifted.wav -af "aresample=async=1:first_pts=0" out.wav
```

```bash
# pitch-preserving time-stretch, timed to a retimed visual — TESTED
ffmpeg -i music.wav -af "rubberband=tempo=0.8" out.wav
```

## BadCode fit

Synthetic-tone tests only prove the graphs parse and run — they say nothing about how these
settings sound on a real Suno mix under narration.

- **Ducking on a sparse, near-black scene reads as sudden if release is too short.** A slower
  `release` (250–400ms) suits BadCode's held shots better than a fast music-video release,
  which pumps against long silences between lines.
- **Loudness targets are a platform choice, not a BadCode-specific one.** Commonly cited:
  streaming ~-14 LUFS, EBU R128 broadcast -23 LUFS — state the target per delivery, current
  per-platform 2026 figures are a gap (see Sources).
- **`afftdn` on Suno vocal stems risks the "watery" artefact** since Suno audio is already
  synthetic; start conservative (`nf=-30` or gentler) and check by ear.
- **The 8s Flow clip cap means narration rarely aligns to one clip** — build the narration bed
  across the whole concatenated scene (§3.6), then duck once against the full music bed.

## Traps

- 🔴 **`sidechaincompress` truncates output to the shorter of its two inputs, ignoring a
  downstream `amix`'s `duration=` policy.** Confirmed: a 6s main track compressed against a 4s
  sidechain produced a 4s output even with `amix duration=first` set (first input the longer
  one). Pad the shorter track with `apad` before feeding the sidechain, or the mix loses its tail.
- **`atempo` is capped 0.5–2.0× per instance** and pitch-shifts audibly beyond that — use
  `rubberband` when timing a track to a §3.7 retimed visual.
- **`-v error` suppresses `loudnorm`'s pass-1 JSON.** It prints at info level; confirmed a
  `-v error -f null -` measurement pass returns nothing — drop `-v error` for that pass.
- **`afade`/`silenceremove` thresholds are dBFS, not LUFS** — don't reuse a `loudnorm` LUFS
  number as a `silenceremove` threshold.
- A stray AAC stream can already sit in a Flow clip — §3.1's `-an` strip must run first, or
  these filters compete with silent-but-present Veo audio in the container.

## Sources

- https://ffmpeg.org/ffmpeg-filters.html#loudnorm — accessed 2026-08-21 — loudnorm two-pass workflow and options
- https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress — accessed 2026-08-21 — sidechain compressor parameters
- https://ffmpeg.org/ffmpeg-filters.html#afade-1 — accessed 2026-08-21 — afade/acrossfade curve list
- https://ffmpeg.org/ffmpeg-filters.html#atempo — accessed 2026-08-21 — atempo 0.5–2.0 range limit
- https://ffmpeg.org/ffmpeg-filters.html#aresample — accessed 2026-08-21 — async/first_pts AV-sync options
- local: `ffmpeg -filters` / `ffmpeg -h filter=<name>` / `ffmpeg -version` on this WSL box — accessed 2026-08-21 — confirmed filter presence and build flags
- `design/research/2026-08-21-video-fx-landscape/11-audio-ducking-denoise-narration-mix.md` — accessed 2026-08-21 — Premiere-side counterpart

**Gaps:** current per-platform LUFS targets for 2026 (YouTube/TikTok/Instagram specifically);
independent `afftdn`/`anlmdn` vs. Enhance Speech quality comparison; formal equivalence of
`acrossfade`'s `qsin` to Premiere's Constant Power; Rubber Band's "reference implementation"
reputation beyond its use elsewhere; Premiere UXP match names for file 11's audio effects (no
live Premiere session run here).
