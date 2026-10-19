# Lip sync for dubbed AI clips — 2026-10-19

**Reading, not testing, except where marked `[observed]`.** Run for The Bank Robbery short: Omni 1.1 Flash talking
clips are muted and dubbed with AI Studio TTS in the character's own voice (Flow's voices drifted American). Some dubs
sync perfectly, some badly. This file says why, ranks the fixes for our machine (RTX 4070 12 GB, WSL with ~7 GB RAM,
Python 3.12, no paid plugins), and lists what makes a dub read as fake.

**Tiers:** `[vendor]` the maker's own page; `[paper]` a paper or standard; `[practitioner]` a named third party
(most sell a lip-sync tool and show no method); `[observed]` our own clips; `[inference]` my reading, **unverified**.
Pages were read through a summarising fetch tool: re-open a page before ruling on exact wording.

**Already in the repo** (not repeated here): `docs/google-flow/omni-flash.md` — "No audio-driven lip-sync" (2026-10-03),
`He says:` + the bare line gives the exact words lip-synced (2026-10-04), Frames mode for a clip that will be dubbed
(2026-10-18), and Omni's audio not following its own picture (2026-10-19); lip measurement in
`scripts/bank-robbery/lips.py` (MediaPipe Face Landmarker on a 2x face crop).

## Headline

**The single biggest cause is whether the mouth on screen was animated to the same words as the dub.** Omni draws
mouth shapes for the line in its prompt. If the prompt line *is* the TTS line, the visemes already match and only the
start time has to be found; if the wording differs, no amount of shifting fixes it, because closures (p, b, m), round
vowels and pauses sit in the wrong places. `[observed]` (a) exact-words Frames clip synced, (b) different-wording
Ingredients clips did not; `[inference]` the viseme explanation — we have n of a handful, not a test.

## 1. Why some dubs sync and others don't

- `[observed]` Exact wording in the prompt → good sync; different wording → bad sync (see headline).
- `[inference]` **Viseme mismatch is not a timing problem.** Shifting or stretching audio can line up *when* the mouth
  moves, never *what shape* it makes. A dub with a different word count also has different syllable rhythm, so a
  global offset fits at one word and fails at the next.
- `[observed]` **Omni's own audio is not a reliable guide to its picture**: a clip "said" a phrase at 5.5 s while the
  lips moved only at 2.6–3.5 s. So aligning the TTS to the clip's *audio* (by transcript or waveform) can be wrong
  even when the words match. Align to the **lips**, measured from the picture.
- `[vendor]` Omni 1.1 Flash: "Uploading audio references is unsupported", "Voice editing is not supported"; the model
  generates audio from the prompt. Nothing on lip sync to supplied audio. <https://ai.google.dev/gemini-api/docs/omni>
- `[practitioner]` Omni (1.0) lip sync "holds steady for 6-7 seconds, before drifting".
  <https://invideo.io/blog/gemini-omni-flash-review/> — so a line placed late in an 8 s clip is at more risk.
- `[practitioner]` Veo 3.1 native audio gives "broad speech rhythm" and "exact frame-level lip sync is not
  guaranteed". <https://skills.sh/krishamaze/skills/google-flow-labs>
- `[practitioner]` A Google developer forum user hit our exact problem (own voice laid over a Flow clip in Premiere,
  lips would not match); the only reply pointed to the feedback button.
  <https://discuss.ai.google.dev/t/lip-sync-in-google-flow/179960>
- `[paper]` **How much error is visible.** ITU-R BT.1359: detectable at about +45 ms (audio early) to −125 ms (audio
  late); acceptable to about +90 / −185 ms. ATSC is stricter: audio never more than 15 ms early or 45 ms late. The
  thresholds come from newsreader clips; sign conventions differ between summaries.
  <https://en.wikipedia.org/wiki/Audio-to-video_synchronization>, <https://www.tvtechnology.com/opinions/av-synchronization-how-bad-is-bad>
  - `[inference]` At 24 fps one frame is 42 ms: **audio one frame early is already at the detection edge; audio
    late is forgiven about three times more.** When in doubt, nudge the dub later, never earlier.
- `[practitioner]` "Lip sync only has to be off by a few frames for the whole clip to feel dubbed." (sync. labs,
  2026-07-14) <https://sync.so/blog/why-ai-lip-sync-looks-fake>

## 2. Fixes, ranked for our setup

### 1. Prompt the exact dub line, then place it on the lips (free, no install) — **do this first, always**

- Write and render the TTS line *first*. Put the identical words in the Omni prompt (`He says:` + bare line, Frames
  mode). Mute the clip. `[observed]` this is the case that synced.
- Find the onset from the picture, not the clip audio: mouth-open curve from `lips.py`, place the first TTS word at
  the first mouth opening, then slide ±1–2 frames by eye. `[inference]` bias later, per BT.1359 above.
- `[inference]` Keep the TTS line about the same length as the clip's mouth activity; if the TTS read is longer, ask
  AI Studio for a quicker read rather than stretching hard.

### 2. Word-level time-warp of the TTS onto the lips (free, a script, no new model)

- Word times for the TTS: WhisperX / faster-whisper word timestamps (already used in this repo for `words-*.json`).
  Mouth events from MediaPipe (`lips.py`): openings, and closures for p/b/m.
- Map each TTS word (or syllable cluster) to the matching mouth segment and time-stretch per segment with ffmpeg's
  `rubberband` filter (present in our ffmpeg build, checked 2026-10-19) or `atempo`; insert/trim silence between words.
- `[practitioner]` This is what the paid ADR tools do: VocALign "applies varying amounts of time-stretching and
  compression to the 'Dub' to align its energy peaks and troughs with a 'Guide' signal".
  <https://www.synchroarts.com/manuals/VocAlign6Standard/Manual/HTML/what-is-vocalign-6-standard.html>
  No maintained free equivalent was found; `[paper]` the method (audio-visual features + DTW) is published:
  <https://arxiv.org/abs/1808.06250>. VocALign / MTrackAlign are paid plugins — **stop and ask**, price not checked.
- `[inference]` Only rescues **same-wording** clips. Stretch beyond roughly ±15–20% per word starts to sound processed.

### 3. Re-animate the mouth to the TTS (free model, real install) — for a clip we must keep whose words differ

| Model | Version (as of 2026-10) | Fits 12 GB? | Licence | Notes |
| --- | --- | --- | --- | --- |
| **LatentSync** (ByteDance) | 1.6 (2025-06-11); 1.5 (2025-03-14) | **1.5 yes (8 GB min); 1.6 no (18 GB min)** `[vendor]` | Code Apache-2.0 `[vendor]`; weights openrail++ on the HF card `[vendor]` | Latent diffusion on the face crop; 1.6 trained at 512² "to mitigate the blurriness problem", so **1.5 is softer**. `guidance_scale` 1.0–3.0: higher = better sync "but may cause distortion or jitter" |
| **MuseTalk** (Tencent Lyra) | 1.5 (2025-03-28) | **Yes** — demo tested on a 4 GB laptop GPU, ~5 min per 8 s in fp16 `[vendor]` | Code MIT; weights "available for any purpose, even commercially" `[vendor]` | Single-step inpainting of a **256×256** face region; README admits lost "mustache, lip shape and color" and jitter; suggests GFPGAN (itself a slop risk) |
| Wav2Lip | old (2020) | yes | **Commercial use "strictly prohibited"** (LRS2-trained) `[practitioner]` | Excluded. Teeth as "white smudges" `[practitioner]` |
| InfiniteTalk (MeiGen) | — | `[inference]` **no** in 7 GB RAM: built on Wan2.1-I2V-14B; low-VRAM/quant modes exist | Weights Apache-2.0 per HF card `[practitioner summary]` | Regenerates the whole frame (head, body, camera "not identically") → re-rolls the shot; colour shift with SDEdit `[vendor via search]` |
| LivePortrait | — | yes | — | Not audio-driven: a lip-open scalar. Used as a pre-pass to neutralise old mouth motion before MuseTalk `[practitioner]` <https://www.sievedata.com/blog/sievesync-zero-shot-lipsync-api-developers> |

Sources: <https://github.com/bytedance/LatentSync>, <https://huggingface.co/ByteDance/LatentSync-1.6>,
<https://github.com/TMElyralab/MuseTalk>, <https://www.creativeainews.com/articles/open-source-lip-sync-licenses-commercial-use-2026/>
(2026-09-16), <https://sync.so/blog/what-is-latentsync> (2026-07-16), <https://github.com/MeiGen-AI/InfiniteTalk>.

- **Pick: LatentSync 1.5** for quality within 12 GB; **MuseTalk 1.5** as the lighter, cleanest-licence fallback.
- `[practitioner, unverified]` A ComfyUI wrapper suggests `chunk_frames` 32 for 12 GB cards — the only route to 1.6 on
  our card, and nobody showed it working. <https://comfyai.run/custom_node/ComfyUI-LatentSyncEnhanced>
- `[inference]` 7 GB WSL RAM is the tighter limit than VRAM for model loading; raising `memory=` in `.wslconfig` on
  the Windows side is the usual fix. Both repos want Python 3.10 (MuseTalk also torch 2.0.1 + mmcv 2.0.1) — use a
  separate conda/venv, not our 3.12.
- `[inference]` openrail++ normally permits commercial use with behavioural use restrictions; read the text before
  publishing. MuseTalk's test data is non-commercial, which does not touch inference.
- Install, one line each (from the READMEs, not run by us):
  - LatentSync: `git clone https://github.com/bytedance/LatentSync && cd LatentSync && source setup_env.sh` then
    fetch the 1.5 `latentsync_unet.pt` + `whisper/tiny.pt` into `checkpoints/`; run `./inference.sh` or `python gradio_app.py`.
  - MuseTalk: `conda create -n musetalk python=3.10` → `pip install torch==2.0.1 …cu118` → `pip install -r requirements.txt`
    → `mim install mmengine "mmcv==2.0.1" "mmdet==3.1.0" "mmpose==1.1.0"` → `sh download_weights.sh`.

### 4. Speech-to-speech conversion of the clip's own audio (keeps Omni's timing) — **ranked last for us**

- Why it tempts: Omni's own speech is already timed to *some* mouth, so converting its voice keeps that timing.
- Why it is last: `[observed]` Omni's audio does not always follow its picture, so the timing it keeps can be wrong;
  and the accent we are escaping is *in* that audio.
- `[practitioner]` RVC carries content and pitch from the source (HuBERT content + pitch tracking); pronunciation tends
  to carry over. `[paper]` a 2026 study found RVC and kNN-VC both retain some source accent.
  <https://arxiv.org/pdf/2604.25332> → `[inference]` an American Omni read stays American-ish in Barry's timbre.
- `[vendor]` **Seed-VC** V2 is the only free one claiming accent conversion (`--convert-style`: "AR model for accent &
  emotion conversion"); 1–30 s reference; **GPL-3.0**; repo **archived 2025-11-21**. <https://github.com/Plachtaa/seed-vc>
  `[inference]` an AR model regenerates rhythm, which would undo the timing that was the point.
- `[vendor]` OpenVoice V1/V2: MIT, "free for both commercial and research use"; a tone-colour converter (timbre only).
  <https://github.com/myshell-ai/OpenVoice>

## 3. Native Flow / Omni / Veo options (2026)

- `[vendor]` **None.** Omni API: audio references unsupported, voice editing unsupported, audio in video references
  ignored, and "you cannot extend an uploaded video where someone is talking to add additional dialogue".
- `[practitioner]` Artlist (2026-08-27) lists Omni audio-to-video as "coming soon". Watch for it; it would replace
  fixes 2–4. <https://help.artlist.io/hc/en-us/articles/38948837028125-Gemini-Omni-1-1>
- `[practitioner]` Flow Music accepts uploaded beats (2026-07-16) — audio only, not lip sync.
- `[vendor]` Flow Character Voices (custom voice on a Character) work only in Ingredients mode (already in
  `omni-flash.md`); the accent did not hold for us, which is why we dub.

## 4. What makes a dubbed or lip-synced face read as fake

- `[practitioner]` (sync. labs 2026-07-14; vendor blogs, consistent across them) **Borrowed teeth** ("someone else's
  teeth are inside it"); **side profiles** (training is frontal); **timing off by a few frames**; **seams** where a
  regenerated mouth patch meets the original; **flattened performance** — models trained on calm speech lose
  shouting, crying, laughing. <https://sync.so/blog/why-ai-lip-sync-looks-fake>
- `[practitioner]` Mouth-region models favour "a blurry mouth in roughly the right place"; missed lip closures on
  b/p/f; small faces look "smudged or plasticky"; occlusion and hard shadows on the mouth break tracking.
  Recommended: mouth visible, face ~10–40% of frame, even light, constant 24/25/30 fps.
  <https://sync.so/blog/how-ai-lip-sync-actually-works>, <https://dubly-ai.support.site/article/lip-sync-artifacts-fix-guide>
- `[inference]` For us, in order:
  1. **Never re-animate a mouth you can avoid.** Fixes 1–2 leave Omni's own pixels untouched; every post lip-sync
     model adds the blur/teeth/seam tells above. Use fix 3 only on a clip we cannot regenerate.
  2. **Cut away rather than fake.** When the line outlasts the lips, go to the listener or an insert (already our
     rule in `omni-flash.md`); off-screen dialogue cannot be out of sync.
  3. **Shots that hide sync**: three-quarter angle, mouth partly in shadow (our one-light rule helps), wider shot,
     speaker turning away on the tail of the line. Close-up frontal shouting is the worst case for every tool.
  4. **Put a voice in a room**: TTS is dry; a short room reverb and the clip's own ambience bed (with speech
     removed) under it make the voice belong to the picture — "sounds dubbed" is often acoustics, not lips.
  5. Check sync at full speed on the delivered file, then frame-step the p/b/m closures.

## Open

- Not tested by us: any of fixes 2–4. The first test worth running: the same TTS line on one mismatched clip through
  LatentSync 1.5 and MuseTalk 1.5, judged by Jack against a regenerated exact-words Frames clip.
- Whether Omni's audio-to-video ("coming soon", third-party claim) reaches Flow, and whether it lip-syncs to the upload.
