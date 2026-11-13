# Cutting a UK rap / grime video to the beat: web research

2026-11-07. Clean-room web research. No repo files were read; every finding comes from the web.

The job: a 220 s UK rap / grime-leaning video. The beat tracker reads about 172 BPM. It was cut once with
"snap every cut to the nearest detected beat", and the director says the cutting does not match the beat.

Evidence tiers: **[pro]** editors, directors or editing educators. **[tested]** a demonstration with footage
or measurements (studies included). **[reported]** forum or blog opinion. **[inference]** my own reasoning.

Search caveat: much of the "cut to the beat" web is vendor marketing for AI beat-sync tools. Those pages
are marked [reported], and their numbers are treated as unsourced.

---

## 1. How professionals cut rap and grime videos to the beat

**What the evidence says about which hit to cut on**
- Cut on the snare backbeat. It falls in nearly every bar, is easy to hear, and has a sharp attack that
  shows as a peak in the waveform. [pro, but written for music editing, not picture]
  https://www.filmeditingpro.com/quick-tips-for-cutting-music-cues/
- If a bar ends in a drum fill, a cut on the bar line chops the fill. Move the edit point off the bar line
  instead. [pro] (same source)
- Cutting on the kick feels grounded. Cutting on the snare instead of the kick (an "off-beat" cut) gives a
  more sophisticated rhythm. Vendor guide, no named editor. [reported]
  https://beatsyncpro.ai/blog/boom-bap-music-video-editing-guide-2026.html
- Automatic tools treat every kick the same. Place markers by hand on the hits that matter: the big snare
  before a drop, a vocal chop, a bass impact. [reported] https://spliceapp.com/blog/best-video-editor-for-beat-drops-1

**Beat level or bar level: what real hip-hop videos do**
- Prétet, Richard and Peeters (2021) ran shot detection over 548 official music videos and compared the cuts
  with detected beats, downbeats and song sections. [tested] https://ar5iv.labs.arxiv.org/html/2108.00970
  - Average shot length was **4.76 s** across all genres. The average bar was 2.30 s and the average song
    section 19.73 s.
  - In the 95 hip-hop videos, the length of the typical shot matched the **beat** in 72.6% of videos and the
    **bar** in 12.6%.
  - Hip-hop had the highest rate of cuts landing near bar lines (downbeats) of the well-represented genres,
    a co-occurrence score of 0.25 ± 0.01. The pop score was 0.21. Pop scored highest on cuts at song-section
    boundaries (0.36); hip-hop scored only 0.19 there.
  - Performance videos had the *lowest* cut-to-bar co-occurrence (0.16). [tested] My reading is that
    performance cuts are placed by the vocal more than by the grid. [inference]
- The experts that paper interviewed: [pro] (same source)
  - Director Courtès: "Cuts have to follow the music's rhythm, even though they might not always co-occur
    with beats."
  - Editor Pozzi: off-beat cuts "surprise the viewer, and illustrate the music's emotional climax". He points
    to cuts just *before* the downbeat in Adele's "Rolling in the Deep" (02:20). Editing speeds up towards the
    climax of a chorus and slows down in bridges.
  - Composer Bartman: cuts "can happen at unconventional moments, like the first or last beat of a bar".
    Syncing cuts to audio events matters most around emotional climaxes.

**On the beat or against it**
- Cutting on every beat is "metronomic and overly predictable" (Mark Suszko). Others say: cut on the big hit
  and use smaller beats to break the rhythm; put freeze frames on drum fills; make a few on-beat cuts at the
  start and at key transitions, and let the rest breathe. [reported]
  https://creativecow.net/forums/thread/music-videos-edit-to-the-beat-or-lyrics-2/
- Carol Vernallis, the music-video scholar: the simple system cuts on the beat, but the main job of editing is
  to reflect how the sound feels, so it moves on and off the beat. [pro, through secondary summaries]
  https://www.slideshare.net/slideshow/carol-vernalliss-music-video-theory/73507931
- In a review of Vernallis's *Experiencing Music Video* (2004): performers in one video start by stressing
  beat one of the bar and end the song stressing beats two and four. So the accent can move during a song,
  and the cut can move with it. [pro, through a review]
  https://www-cambridge-org.ezproxyberklee.flo.org/core/journals/journal-of-the-society-for-american-music/article/experiencing-music-video-aesthetics-and-cultural-context-by-carol-vernallis-new-york-columbia-university-press-2004/03525367FEF94062FBC93303BE324A52
  (A proxy link to the Cambridge Core review. The text was seen only in a search snippet.)
- Editor Jamie Hodgson (Work Editorial) on performance videos: "people tend to want to make things more
  high-tempo, rather than let shots breathe." [pro, through a search snippet; the page did not load]
  https://promonews.tv/interviews/story-so-far-jamie-hodgson-work-editorial/75862
- Max Windows (Stitch/Homespun): "Often good editing is judged on the frequency of the edit, but this does not
  always constitute a quality cut." [pro] https://shots.net/news/view/cut-the-tempo-how-to-edit-for-music-video

**Performance and lyrics**
- Performance-to-camera editing exists so the eye sees the source of the sound and the viewer believes the vocal
  was recorded with the picture. [pro, Caston editing dossier, through a search snippet]
  https://repository.uwl.ac.uk/4706/1/EditingDossiermsmi.2017.6.pdf
- Cutting on lyrics is hard unless the footage matches the words. [reported] (Creative Cow thread above)
- **Not found:** a named pro source on cutting on a rapper's punchlines or line ends in particular. The best I can
  offer is reasoning: a punchline lands on the last stressed word of a line. Holding the rapper through it, then
  cutting on the next downbeat or the breath after it, keeps the joke on the face. [inference]

**Half-time or full tempo**
- UK drill is about 140 BPM, but many producers count it at about 70, with the snare on beat three. Grime is
  also about 140, with the snare on two and four, so it feels twice as fast. [reported, producer guides]
  https://beatstorapon.com/blog/how-to-make-a-drill-beat/ · https://orphiq.com/resources/what-is-grime-music
- 172 BPM does not fit the usual 140 grime grid at either octave. Either the song is really at drum-and-bass
  tempo (172, felt as 86), or it is an 86 BPM half-time beat that the tracker doubled. Tap along to find out
  (step 1 of the procedure below). [inference]
- With a half-time feel, use BPM/2 as the cutting tempo. [reported] https://www.toolsforfilm.com/blog/bpm-and-picture-editors-guide

## 2. Perception: exactly on the beat, or a frame or two early?

**Audio-visual sync tolerance (measured)**
- ITU-R BT.1359-1 for broadcast lip sync: [tested, a standard built from perception studies; read through a
  secondary source, the ITU PDF itself was not checked]
  https://www.forasoft.com/learn/audio-for-video/articles-audio/lip-sync-itu-r-bt-1359-tolerance-windows
  - Viewers first **detect** an error at sound **45 ms early** or **125 ms late**.
  - An error becomes **unacceptable** at sound **90 ms early** or **185 ms late**.
  - The window is lopsided: viewers forgive late sound (that is, picture first) about 2.7 times more than
    early sound.
  - EBU R37 end-to-end target: +40 ms / −60 ms.
- Some sources write the same window with the opposite sign. Check the sign before you compare numbers.
  [tested] https://en.wikipedia.org/wiki/Audio-to-video_synchronization · https://its.ntia.gov/publications/download/11-474.pdf
- Other studies put the detection threshold at sound 35 ms early / 100 ms late. [tested, through a trade article]
  https://www.tvtechnology.com/opinions/av-synchronization-how-bad-is-bad
- Hammer-on-peg videos: no error was noticed between about 75 ms sound-early and 188 ms sound-late. Speech:
  131 ms early to 258 ms late. [tested, Vroomen & Keetels review material, seen in snippets]
  https://core.ac.uk/download/420810866.pdf
- People moving to music: the window in which motion and beat feel synchronous averaged **300–450 ms**. The
  point that felt most in sync was usually on the sound-late side, so motion slightly ahead of the beat read
  as in sync. Individual viewers varied by about 200 ms. [tested] Takehana, Uehara & Sakaguchi 2019, PLoS One.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6711538/
- Cuts that land on the beats are more pleasing than cuts off them, even when viewers do not consciously
  notice the difference. [tested] Lin, Yeh & Shams 2022, *Neuroscience Letters*, doi:10.1016/j.neulet.2022.136623.
  The size of the shift and the sample were not retrieved. https://escholarship.org/uc/item/1rq255xj

**What this means for a cut**
- Every measurement above has the same shape: picture slightly ahead of the sound is forgiven, picture behind
  the sound is caught quickly. A cut **0–2 frames early** (0–83 ms at 24 fps) sits inside the forgiven side. A
  cut 2 frames *late* (sound 83 ms early) is already past the 45 ms detection threshold. [inference from the
  data above]
- Editors' rules of thumb disagree: "1–2 frames early", "2–3 frames early", "2–4 frames early". All are
  unsourced vendor pages. [reported]
  https://try.wideframe.com/blog/how-to-use-ai-to-match-cuts-to-music-beats/ · https://www.v8eo.com/blogs/how-to-edit-music-video-beat-sync
- Nudge single cuts by 1–3 frames; a 2-frame shift is said to be invisible to most viewers. [reported, unsourced]
  https://www.toolsforfilm.com/blog/bpm-and-picture-editors-guide
- Playback can add its own offset. One forum user measured a YouTube upload at 1–2 frames ahead of the beat.
  [reported] https://www.eoshd.com/comments/topic/46696-editing/

**Does cutting on every beat at fast tempo feel frantic?**
- No study found that measures this. Practitioners call every-beat cutting predictable or boring (Creative Cow
  above). The Prétet data shows hip-hop typical shot lengths near beat length in 72.6% of videos, yet an
  average shot across genres of 4.76 s. So beat-length shots are common in places but are not the whole video.
  [tested + inference]
- More cuts make time feel faster: viewers judged time as passing faster for videos with dense editing.
  [tested] https://labocinemedias.ca/wp-content/uploads/2024/10/The_Effect_of_Music_and_Editin.pdf
- At 172 BPM a beat lasts 349 ms, which is **8.4 frames at 24 fps** (8.7 at 25 fps). A video cut on every beat
  would give each shot about a third of a second. [inference, arithmetic]

## 3. Why automatic beat-snapped edits feel wrong

**Ways a beat tracker goes wrong (documented)**
- **Octave errors:** the phase is right but the tempo is half or double. If AMLt (which accepts half, double
  and off-beat answers) scores high while CMLt (which demands the annotated tempo and phase) scores low, the
  tracker is running at half or double tempo. madmom's DBN tracker has a default minimum tempo of 55 BPM. On
  21% of the SMC dataset tracks, that floor forced a double-tempo answer, and lowering it to 30 BPM fixed them.
  [tested] https://arxiv.org/html/2605.12287
- **Off-beat phase:** the beats are evenly spaced but sit halfway between the real ones. madmom's evaluation
  module tests "offbeat", "double", "half", "triple" and "third" variants for this reason. Its default phase
  and tempo tolerance is 0.175. [tested]
  https://madmom.readthedocs.io/en/v0.15/modules/evaluation/beats.html
- **Switching metrical level mid-song:** the tracker changes tempo level partway through. Standard metrics
  under-rate this. [tested] https://arxiv.org/pdf/2210.06817v1.pdf
- madmom can still jump to the wrong tempo despite tempo-range limits, when the activation has high peaks.
  [reported, GitHub discussion] https://github.com/CPJKU/madmom/discussions/503
- Beat This! (ISMIR 2024) has state-of-the-art F1 but is worse on continuity metrics, and it can fail on hard
  or under-represented genres. [tested] https://arxiv.org/html/2407.21658v1

**What "snap to nearest beat" does on top of that** [inference]
- On an off-beat grid, every cut lands half a beat from the real beat: 174 ms at 172 BPM. That is near the
  185 ms limit of acceptability. Half the snaps will be on the sound-early side, which viewers notice at 45 ms.
- At 172 BPM, nearest-beat snapping can move a cut up to ±174 ms. That can drag a cut across a lyric onset or
  the start of a fill.
- Snapping puts every cut on *a* beat, with no idea of the bar, so cuts land on beats 2, 3 and 4 as often as on
  the one. Section starts drift off the downbeat. Prétet's data says hip-hop cuts gather at the bar line.
- Rounding to whole frames adds up to ±21 ms at 24 fps. That stays small unless the grid itself is generated
  by adding up rounded beat lengths, which drifts. [reported] https://www.toolsforfilm.com/blog/bpm-and-picture-editors-guide
- Snapping keeps whatever rhythm the edit already had. If the shot lengths were chosen without the music, the
  pattern of cuts stays unmusical; only the edges move.

**How to check a beat grid against the real kicks and snares (tools and settings)**
- **librosa** `beat.beat_track(y, sr, onset_envelope=..., start_bpm=120, tightness=100, trim=True, units='time')`.
  It is Ellis's 2007 dynamic-programming tracker. `start_bpm` is only a first guess and is ignored if you
  pass `prior`. The documented example builds the envelope with
  `onset.onset_strength(..., aggregate=np.median)`. [pro, official docs]
  https://librosa.org/doc/latest/_modules/librosa/beat.html
  To test the 86 or 172 reading, set `start_bpm=86` and then `start_bpm=172`, and compare which grid sits on
  the onsets. [inference]
- **madmom**: `RNNDownBeatProcessor` feeding `DBNDownBeatTrackingProcessor(beats_per_bar=[4], min_bpm=55,
  max_bpm=215, fps=100)`. Defaults are min 55, max 215 and `beats_per_bar` [3, 4]. Narrow the range (for
  example `min_bpm=75, max_bpm=100` for an 86 feel, or `150–190` for 172) to force one octave, then compare
  the two. [pro, official docs] https://madmom.readthedocs.io/en/v0.16/modules/features/downbeats.html
- **Beat This!** (CPJKU): `File2Beats(checkpoint_path="final0", dbn=False)` returns beats and downbeats.
  [pro, repo docs] https://arxiv.org/html/2407.21658v1 · https://github.com/CPJKU/beat_this
- **Essentia**: `RhythmExtractor2013(method="multifeature")` returns bpm, beats and a confidence. It needs
  44.1 kHz input and searches 40–208 BPM. The official example on a dubstep track gave about 139.98 BPM with
  confidence about 3.94. [pro, official docs] https://essentia.upf.edu/tutorial_rhythm_beatdetection.html
  Informal confidence bands from a community notebook: under 1 very low, 1–1.5 low, 1.5–3.5 good, over 3.5
  excellent. [reported]
  https://nbviewer.org/github/JoseRZapata/MultiFeatureBeatTracking/blob/master/MultiFeatureBeattracking.ipynb
- **Separating the drums first:** training beat and downbeat trackers on separated drum and non-drum stems
  (Spleeter) improved results on unseen test sets. [tested] Chiu et al., EUSIPCO 2021,
  https://arxiv.org/pdf/2106.08703
  Demucs v4 is used to isolate drums for drum transcription. [tested] https://arxiv.org/html/2509.24853v1
  No source found that shows a Demucs drum stem improves a beat tracker at the time it runs. Running onset
  detection on a drum stem to *check* a grid is reasoning only. [inference]
- **A practical check** [inference]: compute onsets on the drum stem (librosa `onset.onset_detect`, or the
  low band for the kick and the 1–5 kHz band for the snare). For each grid beat, measure the distance to the
  nearest onset. A median near zero means the phase is right. A median near half a beat means the grid is on
  the off-beat. Kicks on beats 1 and 3 with snares on 2 and 4 tell you where the one is. A half-time
  86 BPM feel puts the snare on 3.

## 4. Patterns that make a cut feel musical

- **Phrases:** cut in 2-, 4- or 8-beat blocks. In quiet or emotional passages, cut every 2 or 4 beats. Put a
  marker on the bar-1 downbeat and re-anchor at every tempo change. [reported]
  https://www.toolsforfilm.com/blog/bpm-and-picture-editors-guide
- **Downbeats:** the hip-hop data shows cuts gathering at the bar line [tested, Prétet]. Pozzi cuts just before
  the downbeat at climaxes [pro].
- **Density follows energy:** add cuts as the song builds and hold shots to release tension [reported, LA editor
  through a search snippet, https://lbbonline.com/news/camera-obscura-when-to-cut-with-luis-caraza]. Cuts speed
  up towards a chorus climax and slow down in bridges [pro, Pozzi].
- **Fills and accents:** freeze frames, flashes and small zooms on drum fills, crashes and riffs [reported,
  Creative Cow]. Hold one shot across several beats, then cut hard on a big downbeat after a build or a
  silence [reported, vendor guide] https://www.v8eo.com/blogs/how-to-edit-music-video-beat-sync
- **Silence, black frames and stutters:** no pro or tested source found. That they read as musical on a
  fill or before a drop is reasoning only. [inference]
- **Hold the performance:** Hodgson's warning against reflexive high tempo [pro]. Performance videos have the
  lowest cut-to-bar co-occurrence in Prétet's data [tested].
- **Off-beat on purpose:** some editors' favourite work is "purposefully off beat, though not jarringly"
  (Scarlett Bovingdon). Esteban Pedraza prefers edits that move with the music without cutting straight on
  the beat. [pro, through search snippets; the pages returned 403]
  https://lbbonline.com/news/finely-sliced-finding-the-flow-with-scarlett-bovingdon

## 5. Rules of thumb with numbers

| Number | What | Tier |
| --- | --- | --- |
| 4.76 s | average shot length, 548 official music videos | [tested] Prétet 2021 |
| 72.6% / 12.6% | hip-hop videos whose typical shot length matches the beat / the bar | [tested] Prétet 2021 |
| 2–3 s | "most clips" in a grime video | [reported] student coursework, weak |
| about 2 s | average shot length in one pop video (Mike Posner) | [tested] Doxa Comunicación 2017 |
| +45 / −125 ms | lip-sync detection threshold, sound early / late | [tested] BT.1359-1 |
| +90 / −185 ms | lip-sync acceptability threshold, sound early / late | [tested] BT.1359-1 |
| 300–450 ms | window in which motion and music feel synchronous | [tested] Takehana 2019 |
| 1–4 frames early | anticipation, by various unsourced guides | [reported] |
| 8.4 frames | one beat at 172 BPM, 24 fps (16.7 frames at 86 BPM) | [inference] arithmetic |
| 1.40 s / 2.79 s | one 4-beat bar at 172 / at 86 BPM | [inference] arithmetic |
| 0.175 | madmom's default tempo and phase tolerance when scoring beats | [pro] docs |
| 55–215 BPM | madmom DBN default tempo range | [pro] docs |

Frames per beat = fps × 60 / BPM. [reported] https://www.toolsforfilm.com/blog/bpm-and-picture-editors-guide

---

## A procedure for this cut

1. **Settle the tempo by ear first.** Tap along to the hook for at least 16 bars. Decide which you nod your
   head to, 86 or 172: is the snare on 2 and 4 at 172, or on 3 at 86? Write the felt tempo down. This
   is the cutting tempo.
2. **Separate the drums** (Demucs or Spleeter) and keep the drum stem for checking. The stem is never used in
   the mix.
3. **Run two trackers** on the full mix: madmom `RNNDownBeatProcessor` + `DBNDownBeatTrackingProcessor(beats_per_bar=[4])`,
   and Beat This! `File2Beats(dbn=False)`. Run madmom twice, with `min_bpm`/`max_bpm` boxed round 86, then
   round 172.
4. **Check the phase against the drums.** Detect onsets on the drum stem, kick band and snare band
   separately. For each grid, find the median distance from each beat to the nearest onset. Near zero means
   the phase is right; near half a beat means an off-beat grid, so shift it by half a beat.
5. **Check the downbeats.** Kicks should fall on 1 (and 3), snares on 2 and 4 (or on 3 at a half-time feel).
   Where the two trackers disagree on the one, mark beat 1 by ear at each section start, then lock the grid
   to it.
6. **Check for drift.** Plot the inter-beat interval over the whole song. If the grid wanders more than
   about 20 ms from the onsets, re-anchor at each section start, or use the tracked beats instead of a
   fixed-BPM grid.
7. **Mark the song's map** on the timeline: intro, verses, hooks, bridge, drops, every bar line, every fill,
   every silence and drop-out, and the last stressed word of each rap line (the punchline).
8. **Throw away the old snapped cut points.** Keep the shot choices only, then re-place every cut from the map.
9. **Section starts go on the one,** 0–1 frame early. Every new section, hook and drop opens on a downbeat.
10. **Verses (performance):** hold the rapper for 2–4 bars, about 2.8–5.6 s at an 86 feel. Cut on the downbeat
    or on the snare *after* a punchline, never in the middle of a word. Put action cutaways at line ends and in
    the gaps between bars.
11. **Hooks:** cut more densely, every 2 beats to every bar. Cut on the snare (2 and 4) for push and on the kick
    for weight. Speed up into the last bar before the drop.
12. **Bridge:** cut least of all, with one or two long holds. Let the silence or the stripped beat breathe.
13. **Drops:** a hard cut on the downbeat of the drop, 1–2 frames early. Pre-roll the bar before with a short
    stutter, a flash or black frames on the fill, and come out of the black exactly on the one.
14. **Accent cuts:** any single cut can go on a fill hit, a vocal ad-lib or an off-beat for surprise, but only
    a few per section, so they read as choices.
15. **Check it by watching, at full speed with sound.** Scrub each section once on mute to look at the shot
    lengths. Then nudge any cut that feels late by 1–2 frames *earlier*, never later. Watch on the final
    platform as well, since playback can add its own offset.

## What nobody has measured

- How far a **cut** (as opposed to lip sync or a moving body) can be early or late before it feels off the
  beat. The 1–4-frames-early rule is practitioner lore with no study behind it.
- At what tempo cutting on every beat starts to feel frantic or out of sync.
- Shot-length statistics for **UK rap or grime** videos in particular. The only genre data found is
  "hip-hop" in Prétet 2021 (mostly US), plus one student's grime note.
- Whether cutting on the kick, on the snare or on the downbeat reads differently to viewers.
- Whether holding on a rapper through a punchline lands the joke better than cutting on it.
- Whether black frames or stutters on fills read as musical, or only as effects.
- Whether running a beat tracker on a separated drum stem at run time improves its accuracy. The only evidence
  is for training on stems.
- The size of the effect in Lin, Yeh & Shams 2022 (aligned cuts are more pleasing), and how far off-beat
  their incongruent cuts were: not retrieved.
