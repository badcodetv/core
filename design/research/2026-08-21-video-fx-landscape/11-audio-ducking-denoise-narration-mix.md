# Audio: narration over music, ducking, denoise, loudness

## What this covers

Getting narration to sit cleanly over a Suno music bed: Essential Sound panel tagging + auto-
ducking, Enhance Speech (cloud dialogue repair), native DeNoise/DeReverb, per-platform loudness
targets, the Constant Power crossfade, manual-keyframe ducking, iZotope RX as the deep-restoration
tier, Suno's own stem extraction (use instead of remixing in Premiere), and what the UXP
`AudioComponentChain` API can confirm today. `docs/flow/post-production.md` already owns the
video-side ffmpeg recipes and strips all audio from Flow clips (`-an`) — this fills the silence.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Duck music under narration, GUI | Essential Sound panel | Tag Dialogue/Music → Ducking → "Duck Against" → Generate Keyframes | included (CC) |
| Duck music under narration, scripted | ffmpeg `sidechaincompress` | Narration track sidechains and compresses the music track | free |
| Duck at known timestamps | Manual volume keyframes, or ffmpeg `volume` with `enable=` windows | Keyframe the clip's Volume line, or write one gain window per segment | included / free |
| Remove hiss/hum | DeNoise (native) | Audio Effects → Noise Reduction/Restoration → DeNoise, "Reduce Noise By" | included |
| Remove room echo | DeReverb (native) | Same category; apply **before** DeNoise in the chain | included |
| One-click AI dialogue repair | Enhance Speech (Adobe Podcast engine) | Essential Sound → Repair → Enhance Speech, or podcast.adobe.com | free / $9.99 mo |
| Deep spectral repair, dialogue isolate | iZotope RX (standalone/plugin) | Export clip → repair in RX → reimport | $99–$1,399 |
| Deliver at correct loudness | ffmpeg `loudnorm`, two-pass | Pass 1 measures, pass 2 applies against the platform LUFS target | free |
| Crossfade music cues, GUI | Constant Power (native transition) | Audio Transitions → Crossfade → Constant Power, drop on the edge | included |
| Crossfade, scripted | ffmpeg `acrossfade` | Approximate equal-power via `c1=qsin:c2=qsin` | free |
| Isolate vocal/instrumental from a Suno track | Suno stem extraction | Library → More Actions → Get Stems → Extract Stems → download WAV | included in plan |
| Remix/rebalance a finished mix | RX Advanced "Music Rebalance", or re-pull Suno stems | Separate stems, adjust levels | $1,399 / free |
| Script effect changes from outside the UI | UXP `AudioComponentChain` | Class exists in the DOM API; enumeration method unconfirmed | free (dev time) |

## Named tools

### Essential Sound panel (native)
Tags a clip Dialogue/Music/SFX/Ambience and exposes type-specific controls, including one-click
auto-ducking that writes editable volume keyframes. Included with any Premiere Pro / Creative
Cloud seat (2026-08-21). Premiere Pro, Win/Mac, built in. Long-standing native feature; the
Generate Keyframes ducking flow is the standard citation across 2026 how-tos (Adobe helpx,
Freepik, Hollyland).

### Enhance Speech / Adobe Podcast
Cloud neural speech-repair engine, reachable from podcast.adobe.com or the Essential Sound panel.
Free tier: 1hr/day, 30-min files, 500MB cap. Premium: $9.99/mo or $99.99/yr — 4hr/day, 2-hr files
to 1GB, batch upload, video support, strength slider (seen 2026-08-21, per toolsforhumans.ai /
aitoolsdevpro.com; Adobe's own price page wasn't directly reachable this pass — gap). Cloud +
Premiere panel. At least one 2026 source describes the in-Premiere panel as CEP-built — worth a
version check (see Traps). Actively developed, cited as the cheaper answer to iZotope.

### DeNoise / DeReverb (native)
Built-in restoration pair under Audio Effects → Noise Reduction/Restoration. DeReverb tightens
room echo; DeNoise pulls constant hiss/hum via a "Reduce Noise By" slider. Included, no separate
charge. Premiere Pro, built in. Mature, widely cited 2026 workflow (pixflow.net, Hollyland);
correct chain order is DeReverb then DeNoise.

### iZotope RX 12
The reference deep-restoration suite — spectral repair, dialogue isolate, ambience match, music
rebalance. Perpetual licence (2026-08-21, toolfarm.com / creatorstackclub.com): Elements $99 (6
plugins, no standalone editor), Standard $399 (standalone editor, 18 plugins), Advanced $1,399
(pro dialogue tools, ambience match, music rebalance). Standalone + VST/AU/AAX, Win/Mac. The
benchmark every 2026 cleanup roundup measures against.

### Waves (Ultimate / Essential / Creative Access)
200+ plugin catalogue usable as VST3 in the Audio Track Mixer. Subscription tiers exist but **no
reliable 2026 price was found this pass** (gap — check waves.com/subscriptions directly). Overkill
for a narration-over-music mix; relevant only if BadCode masters music separately from Suno.

### Constant Power (native transition)
Premiere's default crossfade — equal-power curve keeps combined loudness roughly constant, unlike
a linear (Constant Gain) fade's dip. Included. Effects panel → Audio Transitions → Crossfade →
Constant Power. Default since early Premiere versions; filmdaft.com's 2026 piece is the clearest
citable breakdown vs Constant Gain / Exponential Fade.

### Suno stem extraction
Library → track's "More Actions" → Get Stems → Extract Stems (or a 12-track split), downloadable
as WAV/MP3. Included with an active Suno plan. Web only. Suno's own 2026 hub page names it as the
recommended route — reach for this before ever trying to un-mix a bounced MP3 by ear.

### ffmpeg `loudnorm` / `sidechaincompress`
Free, scriptable substitutes for Essential Sound's GUI ducking and for a batch loudness pass.
Already installed (v4.4.2). `loudnorm` is the standard citation in every 2026 loudness writeup
found; `sidechaincompress` is the standard scripted-ducking answer, confirmed working here.

## Automation hook

**Premiere side.** No documented audio equivalent of `VideoFilterFactory.getMatchNames()` was
found. The UXP DOM API lists an `AudioComponentChain` class, but its enumeration/keyframe methods
were not reachable this session — **unconfirmed, not absent**. Discovery step: in the UXP
Developer Tool console, on a clip with DeNoise/DeReverb already applied, walk its component chain
and log each component's `.matchName` — same technique the video bridge uses via
`VideoFilterFactory`, pointed at an audio clip instead. Do this once, live, before scripting an
audio-effect insert.

**ffmpeg side** — run against synthetic tones in the scratchpad this pass (TESTED):

```bash
# Loudness, two-pass — TESTED
ffmpeg -i in.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -   # pass 1: measure
ffmpeg -i in.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=<x>:measured_TP=<x>:measured_LRA=<x>:measured_thresh=<x> -ar 48000 out.wav   # pass 2
```

```bash
# Sidechain ducking: narration compresses the music bed — TESTED
ffmpeg -i music.wav -i voice.wav -filter_complex \
 "[0:a][1:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[d];[d][1:a]amix=inputs=2:duration=first[out]" \
 -map "[out]" mixed.wav
```

```bash
# Crossfade two cues (approximates Constant Power) — TESTED
ffmpeg -i a.wav -i b.wav -filter_complex "acrossfade=d=2:c1=qsin:c2=qsin" out.wav
```

```bash
# Manual duck at a known window instead of sidechain — UNTESTED
ffmpeg -i music.wav -af "volume=0.25:enable='between(t,3,9)'" ducked.wav
```

## BadCode fit

Every scene starts as a silent Veo/ffmpeg clip (`-an` strips it on arrival), so narration and
Suno music are always laid on after — no location room-tone to match, only a clean narration read
sitting over a Suno instrumental. `sidechaincompress` or Essential Sound auto-ducking both work; a
tighter release (200–300ms) suits BadCode's pacing better than a slow broadcast duck. Target
**-14 LUFS integrated** for YouTube (its stated normalization target per multiple 2026 secondary
sources — the primary Google page wasn't reachable this pass, gap) and treat TikTok/Instagram the
same, since neither publishes a hard number (informal 2026 testing clusters -14 to -15 LUFS for
both). Master to that, don't rely on platform normalization to pull a hot track down.

## Traps

- **Enhance Speech's Premiere panel may be CEP.** Premiere 2026 no longer loads legacy CEP
  extensions by default — check the panel opens in 26.3.2; podcast.adobe.com is the fallback.
- **DeNoise before DeReverb is backwards.** Order is DeReverb first, DeNoise last, or artefacts
  get baked under the reverb tail.
- **TikTok/Instagram LUFS numbers are informal**, reverse-engineered from testing, not a published
  spec — don't state them with YouTube's confidence.
- **`sidechaincompress` needs explicit channel layouts.** Bare lavfi tones threw `No channel
  layout for input 1` here (a warning, not a failure); real Suno/recorder WAVs won't trip it.
- **Constant Power's exact curve isn't published** — `acrossfade=c1=qsin:c2=qsin` is an
  approximation, fine for a rough mix, not a final crossfade under scrutiny.
- **Don't hand-remix a bounced Suno MP3.** Pull real stems via Get Stems; reconstructing them by
  EQ/notch-filtering a stereo bounce is RX Advanced's job, not a two-minute fix.
- **The UXP audio match-name story is unverified.** Do the live console enumeration before
  scripting against an assumed `AudioComponentChain` method signature.

## Sources

- [Automatic audio ducking – Adobe Premiere Pro help](https://helpx.adobe.com/premiere-pro/how-to/automatic-audio-ducking.html) — 2026-08-21, tag/Duck Against/Generate Keyframes
- [Advanced noise and reverberation reduction – Adobe Premiere Pro help](https://helpx.adobe.com/premiere-pro/how-to/advanced-noise-reverberation-reduction.html) — 2026-08-21, DeNoise/DeReverb order + controls
- [Apply audio crossfade transitions – Adobe Premiere Pro help](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-transitions/audio-crossfade-transitions.html) — 2026-08-21, Constant Power is default
- [Constant Gain vs. Constant Power — FilmDaft](https://filmdaft.com/crossfades-in-premiere-pro-explained/) — 2026-08-21, equal-power curve explained
- [ffmpeg loudnorm — local `ffmpeg -h filter=loudnorm`, v4.4.2](https://ffmpeg.org/ffmpeg-filters.html#loudnorm) — 2026-08-21, params verified live
- [Two-pass loudnorm — DEV Community](https://dev.to/masonwritescode/two-pass-loudness-normalization-with-ffmpeg-loudnorm-the-right-way-1nm3) — 2026-08-21, two-pass workflow confirmed
- [LUFS targets per platform 2026 — Forasoft](https://www.forasoft.com/learn/audio-for-video/articles-audio/lufs-targets-per-platform-2026) — 2026-08-21, YouTube -14 LUFS, TikTok/IG informal
- [Adobe Podcast pricing — G2](https://www.g2.com/products/adobe-podcast/pricing) — 2026-08-21, free vs $9.99/mo tiers
- [iZotope RX Elements — Toolfarm](https://www.toolfarm.com/buy/izotope_rx_elements/) — 2026-08-21, RX 12 tier pricing
- [Stem separation — Suno Hub](https://suno.com/hub/best-stem-separation-software) — 2026-08-21, Get Stems/Extract Stems flow
- [Premiere API — UXP for Adobe Premiere](https://developer.adobe.com/premiere-pro/uxp/ppro-reference/) — 2026-08-21, AudioComponentChain class confirmed, methods not

**Gaps:** exact 2026 Waves subscription price; whether Enhance Speech's Premiere panel is CEP or
UXP in 26.3.2 specifically; a directly-fetched YouTube primary page for -14 LUFS (relied on
secondary sources); documented `AudioComponentChain` enumeration methods; a free/low-cost VST
denoise plugin comparable to DeNoise (search cut short by the session's web-search budget limit).
