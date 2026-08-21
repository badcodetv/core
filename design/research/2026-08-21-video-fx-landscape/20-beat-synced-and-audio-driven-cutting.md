# Beat-synced and audio-driven cutting

## What this covers

Getting a tempo/beat grid out of a track BadCode already has — the Suno-generated drum & bass
`.mp3` — and turning that grid into cut points: Premiere markers via this repo's own bridge
(`premiere_add_marker`), an ffmpeg concat/trim plan, or a quantiser that snaps existing cuts to
the nearest beat. Named in the sweep's [Gaps](README.md#gaps): "no brief covers audio-driven/
beat-synced editing." Mixing/mastering the track stays with files 11/17 — this is about *when to
cut*, not how the audio sounds.

## What's possible

| Need | Tool/route | How | Cost tier |
| --- | --- | --- | --- |
| Detect every hit, isolated stem only | `aubio aubioonset` | CLI, prints onset times | free |
| Detect every hit, isolated stem only (ffmpeg-only) | `silencedetect` | gap-end = next hit, needs real silence | free |
| Infer a beat/tempo grid | `aubio aubiotrack` | CLI, prints beat times — tempo-halving risk, see Traps | free |
| Infer a beat/tempo grid | `librosa.beat.beat_track` | Python, returns tempo + beat frames | free |
| Infer a beat/tempo grid, fastest | `essentia RhythmExtractor2013` | Python, tempo + beats + confidence | free |
| Infer a beat/tempo grid, strong reputation elsewhere | `madmom` DBNBeatTracker | Python — install failed this session, see Traps | free (if it installs) |
| Turn a beat grid into Premiere markers | this repo's bridge, `premiere_add_marker` | one call per beat/bar timestamp | free (dev time) |
| Turn a beat grid into an ffmpeg cut plan | script timestamps into post-production.md §3.6's `list.txt` | one `trim`/`concat` entry per segment | free (dev time) |
| Quantise an existing cut to the nearest beat | round an edit point to the nearest grid value | `min(beat_times, key=lambda t: abs(t-cut))` | free (dev time) |
| Retime music to fit a video's duration, GUI | Premiere Remix (Adobe Sensei) | Essential Sound → Remix — not a beat-grid export, see Traps | included |
| Mark beats manually while listening | Sequence → Add Marker on playback | no automation, always available | included |

## Named tools

### aubio (`aubiotrack`, `aubioonset`)
Onset/beat-detection library with a CLI. Free, GPLv3. Linux/Mac/Windows. Installed this session
via `apt install aubio-tools` (0.4.9-4.1build2, Ubuntu 22.04 universe) — trivial, no compile.
Mature but low-velocity (same 0.4.9 cited across recent years).

### librosa
Python audio-analysis library; `librosa.beat.beat_track` is the standard MIR (music information
retrieval) citation for beat tracking. Free, ISC licence. `pip install librosa`. Installed this
session (1.0.0), pulled numpy/scipy/soundfile with no issues. Actively maintained.

### Essentia
C++ audio-analysis library with Python bindings; `RhythmExtractor2013` (`multifeature`/`degara`)
is its beat/tempo estimator, needs 44.1kHz input. Free, AGPLv3. `pip install essentia`. Installed
this session with no issues. Active, backed by an academic research group (MTG-UPF).

### madmom
Python audio/music-analysis library; `DBNBeatTracker` has the strongest published-accuracy
reputation of the four tools tried here. Free, BSD 3-Clause. **Installation failed this
session** — see Traps. Last meaningfully active ~2022, a known-stale but still-cited package.

### ffmpeg `silencedetect` / `astats` (a technique, not a tool)
Already in this repo's ffmpeg 4.4.2. `silencedetect` reports gap-end timestamps aligning with
hits **only when there's real silence between them**; `astats` with `metadata=1:reset=1` gives a
per-frame RMS stream a caller could peak-pick by hand. Both TESTED, both clean against an
isolated click — see Traps for why that doesn't generalise to a real mix.

### Premiere Remix (Adobe Sensei)
Analyses a music track and retimes/restructures it toward a target duration while preserving
phrasing. Included. **Not what this brief needs, and not live-verified this session** — it
retimes music *to* a duration, it doesn't expose a beat grid to script against. No evidence was
found this session for an automatic beat-marker feature in Premiere; treat as unconfirmed.

## Automation hook

**Premiere side.** This repo's bridge already carries what's needed:
`premiere_add_marker({ name, time, duration, comments })` is in the tool table
(`design/2026-08-21-premiere-bridge-and-video-fx.md`, T9). **No new UXP surface is required** —
compute the beat grid outside Premiere with any tool above, then call that one existing tool once
per beat/bar. No confirmed native API exposes a beat grid from inside Premiere itself.

**ffmpeg side** — run against a synthetic 174 BPM click track (30s, isochronous 1kHz clicks, a
typical D&B tempo) built in the scratchpad:

```bash
# per-hit onsets via silence gaps — TESTED (isolated click only, needs real silence, see Traps)
ffmpeg -i in.wav -af "silencedetect=noise=-30dB:d=0.05" -f null -

# per-frame RMS as a DIY onset heuristic — TESTED (needs a peak-picker on top)
ffmpeg -i in.wav -af "astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null -
```

```bash
# aubio: per-hit onsets — TESTED, exact (87/87 clicks at the correct 0.345s spacing)
aubioonset -i in.wav
# aubio: beat/tempo grid — TESTED, tempo-halved (numbers in Traps)
aubiotrack -i in.wav
```

```python
# librosa: beat/tempo grid — TESTED, closest to ground truth
import librosa
y, sr = librosa.load('in.wav', sr=None)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beats, sr=sr)
```

```python
# essentia: beat/tempo grid — TESTED, fast, tempo-halved (numbers in Traps)
import essentia.standard as es
audio = es.MonoLoader(filename='in.wav', sampleRate=44100)()
bpm, beats, confidence, _, _ = es.RhythmExtractor2013(method='multifeature')(audio)
```

## BadCode fit

- **The tempo is never a mystery.** BadCode writes the Suno prompt, so the D&B tempo range
  (commonly 160–180 BPM, this brief's own test track built at 174) is known before the track
  exists. Every tool above accepts a tempo prior — pass it rather than trust blind detection,
  exactly where this session's own tests went wrong (Traps).
- **Flow's 8-second clip cap doesn't respect bar boundaries.** A clip built to a beat grid still
  ends where the cap says, not on a downbeat — trim clips to bar-length multiples when possible,
  or let a hard cut hide a boundary that lands mid-bar.
- **D&B phrases in 8- or 16-bar blocks; the drop lands on a phrase boundary, not any beat.**
  Cutting mechanically on every beat of the grid reads as amateurish, strobing editing — the
  craft is holding a shot across several bars and reserving hard per-beat cutting for the drop or
  a deliberate high-energy passage. Use the grid to place a cut precisely, not to generate one.

## Traps

- 🔴 **Tempo-halving ("octave error") is real, reproduced twice this session.** Against a clean
  174 BPM click, both `aubiotrack` (default) and Essentia's `RhythmExtractor2013`
  (`multifeature`) locked onto **≈87 BPM — exactly half tempo**. Only `librosa.beat.beat_track`'s
  default got close: **172.3 BPM** (86 beats vs 87 expected). **Always sanity-check a detected
  tempo against the tempo you told Suno to make.**
- **`silencedetect`/`astats` need real silence between hits.** Clean against an isolated click; a
  real D&B mix (kick, bass, pads together) essentially never has true silence between hits — this
  route only applies to an isolated stem (Suno Get Stems, file 11), not a finished mix.
- **`madmom` would not install.** `pip install madmom` fails on stock Python 3.12 here: its
  legacy `setup.py` needs `distutils`, removed from the stdlib in 3.12. Needs an older Python
  (pyenv/conda) or a fork — not attempted this pass.
- **Nothing here was tested against real BadCode content** — every number is from a synthetic
  click, not an actual Suno D&B track. A busy mix with syncopated hi-hats and rolling basslines is
  a harder problem; re-test before trusting these tools at face value.
- **Quantising every cut mechanically to the beat is a rookie edit** — see BadCode fit. The grid
  is a placement aid, not a cutting rule.

## Sources

- local: `aubio-tools` 0.4.9 (apt), `aubiotrack`/`aubioonset` tested against a synthetic 174 BPM click, this WSL box — 2026-08-21 — onset exact, tempo halved
- local: `librosa` 1.0.0 (pip), `beat_track` tested against the same click — 2026-08-21 — closest tempo estimate, 172bpm
- local: `essentia` (pip), `RhythmExtractor2013` tested against the same click — 2026-08-21 — fast, also tempo-halved
- local: `madmom` install attempt via pip, this WSL box — 2026-08-21 — failed, distutils removed py3.12
- [aubio.org — Command line tools manual](https://aubio.org/manual/latest/cli.html) — 2026-08-21 — aubiotrack/aubioonset option reference
- [Essentia — RhythmExtractor2013 reference](https://essentia.upf.edu/reference/streaming_RhythmExtractor2013.html) — 2026-08-21 — algorithm inputs, tempo range
- local: `ffmpeg -af silencedetect`/`astats` tested against the same click, this WSL box — 2026-08-21 — onset heuristic works, needs silence
- [`design/2026-08-21-premiere-bridge-and-video-fx.md`](../../2026-08-21-premiere-bridge-and-video-fx.md) — 2026-08-21 — `premiere_add_marker` tool table, T9

**Gaps:** no real Suno/D&B track tested against any tool (synthetic click only); `librosa`'s
official docs page 404'd this session (cited from the local test only); no live Premiere session
to confirm or deny an automated beat-marker feature or check Remix's UI path against 26.3.2;
`madmom`'s accuracy reputation is asserted from its general MIR standing, not verified here since
it wouldn't install.
