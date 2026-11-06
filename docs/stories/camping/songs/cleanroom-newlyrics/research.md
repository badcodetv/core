# New lyrics over the same instrumental in Suno (web research, 2026-11-06)

Clean-room: web only (7 searches, 7 page fetches). Tags: [vendor] Suno's own help; [tested] someone ran it; [reported] blog/forum; [inference] mine.

## Answer
No Suno route is certain to keep the instrumental bit-for-bit. Add Vocals is the intended route but it regenerates the song and may change the beat. The only route that keeps the original instrumental unchanged is to mix new vocals over the original ourselves (route 3).

## 1. Add Vocals
- Exists, beta, Pro and Premier only. Works on uploaded tracks, Instrumental-toggle generations, or stems. [vendor] https://help.suno.com/en/articles/6882817
- Click path: Library/Workspace -> song (...) More Actions -> Remix dropdown -> Add Vocals -> enter lyrics -> Create. [vendor] same page
- Style box: describe the instrumental AND the vocal you want. Audio Strength slider (advanced options) sets how closely the result follows the original instrumental. [vendor] same page
- Models: the Suno help page does not say. Third-party API docs list V4_5PLUS, V5, V5_5 for add-vocals (API, not the app). [reported] https://docs.sunoapi.org/suno-api/add-vocals . A v6 guide says it is still current. [reported] https://jackrighteous.com/en-gb/blogs/guides-using-suno-ai-music-creation/suno-v45-plus-video-demo-add-vocals-spark-flip (v6 specifics: thin).
- Length limit: not stated by Suno for Add Vocals. Uploads max 8 min on Pro/Premier (see 4). A 3:35 track is inside it.
- Is the instrumental kept exactly? Suno does not claim so; the only control is the Audio Strength slider. [vendor] Reddit user: it "often completely changes the instrumental". [reported, anecdotal] https://reddit.sentinel-team.org/posts/1scy3ov/snapshots/2026-04-09T19%3A10%3A59.878122Z . A Chinese tutorial says it regenerates the whole song and recommends Replace Section if the original must stay. [reported] https://lilys.ai/notes/zh/suno-ai-v5-20251020/suno-ai-vocals-various-uses . Treat as: will drift, even at high strength [inference].
- Guide advice: write section labels that fit section length, check lyric density against the space the arrangement leaves, say what the source is in the style box. [reported] https://jackrighteous.com/de/blogs/guides-using-suno-ai-music-creation/suno-v45-plus-features-guide
- NOT found anywhere: any test of rap through Add Vocals, off-beat rap, tempo being ignored, singing instead of rapping, how to get two voices. Thin to nothing.
- Two-voice tips (general Suno, not Add Vocals): put "Duet" in style; [Male Vocal]-type tags before sections; keep voice changes to about 4-6. [reported, Reddit-sourced, 2025] via search summary of https://roo.beehiiv.com/p/suno-ai-prompt-guide-2026-copy-paste-templates-the-formula-that-actually-works (not opened; thin).

## 2. Clean instrumental from the existing song
- Suno stems: Get Stems (Workspace/Library ... menu) or Studio right-click -> Split Stems. "Split from Mix" gives a chosen element plus the rest: 10 credits per extraction, 20 for both. Auto Split 50 credits, up to 12 stems. Paid plan needed (Pro for Auto/Split from Mix, Premier for Advanced). [reported] https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-stem-separation-auto-split-split-from-mix-advanced-split (credits/plans from one blog; check in the app).
- Important: that guide says Suno's newer stems are REGENERATED to match the source, not extracted, so timbre, low end and timing feel can drift. [reported, quoting Suno] same URL. Not proven for DnB. [inference] a regenerated bass/drum stem is a risk for an exact instrumental.
- Local separators: htdemucs_ft is the usual best open choice for vocals/drums/bass in benchmarks; MDX-Net/UVR is strong on vocals but weaker on drums/bass. [reported] https://dev.to/stevecase430/best-free-ai-stem-splitters-in-2026-a-developers-benchmark-2dam ; https://pypi.org/project/audio-separator . Multiple-pass chaining is common. [reported] https://gearspace.com/threads/stem-splitter-comparison.1430416/
- DnB-with-rap specifically: no comparison found. [inference] Expect faint vocal ghosts/reverb tails in the hats and snare, and smeared transients. Our original instrumental (the Suno project/stems from June, if the instrumental was ever exported) is better than any separation: check whether the June song has a stem set or an Instrumental version before separating.
- Suno stems vs Demucs head to head: not found.

## 3. Other Suno routes
- Replace Section: select a section, edit lyrics in the box, Recreate Section; two options; result is a new full song. Pro/Premier. [vendor] https://help.suno.com/en/articles/3271873 . Suno does not say if the rest is untouched (implied). Original limit was a 10-30 s section [reported] via search summary; seams at edit points reported by one changelog [reported, unreplicated]. With 25% more lyrics plus a hook, this means redoing nearly every section, so it is not a true fit [inference]. Reddit user's workaround: stem, regenerate vocals, splice in a DAW [reported, anecdotal] https://reddit.sentinel-team.org/posts/1s7pj8j/snapshots/2026-04-03T23%3A40%3A05.740169Z
- v6 editing: plain-language edits while "preserving the rest". [reported] https://jackrighteous.com/es-us/blogs/guides-using-suno-ai-music-creation/suno-v45-plus-video-demo-add-vocals-spark-flip . Not for rewriting all lyrics; thin.
- Voices (v5.5, Pro/Premier): record/upload your own voice so Suno sings on creations; private. Needs a real voice, not two rap characters. [vendor] https://suno.com/release-notes/introducing-v5-5-voices-custom-models-and-my-taste . Custom Models: train on 6+ of your tracks (one source says fewer); steers style, does not keep an instrumental. [vendor] same page.
- Cover, "Use as inspiration", Extend: ruled out or do not preserve audio [inference]; no source claims otherwise.
- Studio vocal re-record: Studio 2.0 (Premier, Aug 2026) is a DAW; nothing found on re-recording vocals with new lyrics. [reported] same v6 guide. Thin.

## 4. Uploading
- Max 8 min for Pro/Premier, 60 s for Basic (older pages say 6-60 s). [reported] https://jackrighteous.com/blogs/ai-music-distribution-guide/suno-blocked-my-own-song-copyright-upload-errors (formats: not found).
- Uploads are copyright-screened; own material can be blocked; Suno has not said what system is used. Our own Suno-generated tracks being blocked: no report found either way. If blocked: contact support, do not alter the audio to dodge it. [reported] same URL. Rule: only upload what you own. [vendor-quoting guide] https://jackrighteous.com/de/blogs/guides-using-suno-ai-music-creation/suno-v45-plus-features-guide

## 5. Matching structure and the music video
- Nothing found that ties lyric line counts to the instrumental's bars. General advice only: BPM as a number in the style box, sparse section tags, one vocal cue per section. [reported] https://roo.beehiiv.com/p/suno-ai-prompt-guide-2026-copy-paste-templates-the-formula-that-actually-works
- [inference] Plan: mark the original's section start times; write each new section to the old section's line count and syllable load; the 25% extra goes into a hook that fits an existing gap. If the track length or any section start moves, the video cut will not line up, so check section start times of the output against the original before animating anything.

## 6. Fallback: new vocals over the original instrumental
- Feasible, and the only way to keep the instrumental exact [inference]. Method: make a Suno take of the new lyrics (Add Vocals on the instrumental is the best source because the vocal is written to the same beat), split vocals with Suno Split from Mix or Demucs, then place them over the ORIGINAL instrumental in Premiere/DAW. If the new take's tempo is the same (174 BPM, same bar grid) the vocal lines up; slight drift needs per-section nudges. A time-stretch of a few percent is common practice [inference]. The Reddit workaround above is the same idea [reported, anecdotal].
- Risks: vocal stem carries instrument bleed and reverb of the new take's own beat (flams against the original drums); two male voices are one stem unless split by section [inference].
- Need a clean instrumental first: see section 2.

## Could not establish
- Whether Add Vocals keeps the uploaded audio unchanged at max Audio Strength (nobody tested it with rap/DnB).
- Models available to Add Vocals in the current app; v6 behaviour.
- Rap, two-voice and tempo behaviour of Add Vocals.
- Suno stems vs Demucs on DnB; whether our own Suno upload is blocked.
- Upload formats; Studio vocal re-record.

## Ranked recommendation
1. Add Vocals on the original instrumental (cheapest, single click path), run 2-3 takes at high Audio Strength, then decide per take: use as is if the beat is intact, otherwise take only its vocal stem (route 3).
2. Original instrumental + new vocal stem mixed ourselves (guaranteed instrumental, alignment work). Best if a June instrumental/stem export exists.
3. Replace Section chain: poor fit for a 25% longer rewrite; use only for fixing single sections.

### Route 1 click path (as documented by Suno, check in app)
1. Get an instrumental: June song -> (...) -> Get Stems -> Split from Mix (instrumental), or upload an existing instrumental file (Pro/Premier, under 8 min).
2. Library/Workspace -> that track -> (...) More Actions -> Remix -> Add Vocals.
3. Pick the newest model offered; open advanced options, set Audio Strength high.
4. Style box: describe the existing instrumental (dark drum and bass, 174 BPM) and the vocal (two male rappers trading verses, duet).
5. Lyrics box: new lyrics with section tags in the original order; hook as its own tagged section.
6. Create; compare section start times and tempo with the original before keeping.
