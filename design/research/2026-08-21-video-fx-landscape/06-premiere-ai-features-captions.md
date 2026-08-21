# Premiere 2026 AI features and captions

## What this covers

Premiere Pro's own AI editing surface as of 26.3.2 (Aug 2026): the Firefly-powered generative
tools (Generative Extend), assistive-AI tools (Auto Reframe, Scene Edit Detection, Color Match,
Media Intelligence search, Remix), transcript-driven workflows (Text-Based Editing, Auto
Captions, caption-to-graphics), one legacy tool (Morph Cut), Enhance Speech, and Object Mask.
For each: what it does, cost model, 2025–26 review reputation, and UXP exposure. Counterpart to
`docs/flow/post-production.md` (ffmpeg recipes) — doesn't repeat its reverse/ping-pong/zoompan/
retime/concat/crop recipes except where an AI feature needs its own ffmpeg fallback.

## What's possible

| Need | Tool/route | How (one line) | Cost tier |
| --- | --- | --- | --- |
| Grow a clip that's too short | Generative Extend | Right-click clip edge → Generative Extend | £ (Firefly credits, metered) |
| Reframe 16:9 to vertical/square | Auto Reframe | Right-click sequence → Auto Reframe | Included |
| Clean up muddy dialogue | Enhance Speech | Essential Sound → Enhance Speech (cloud) | Included tier / Podcast sub for heavy use |
| Split a flattened export into shots | Scene Edit Detection | Right-click clip → Scene Edit Detection | Included |
| Cut by editing text | Text-Based Editing | Window → Text → Transcribe, delete words | Included (local) |
| Auto-generate captions | Auto Captions | Transcribe → Create Captions | Included |
| Style captions consistently | EGP Track Style | Style one caption → "Create Style" | Included |
| Animate captions | Caption-to-Graphics | Right-click item → Upgrade to Graphic, keyframe | Included |
| Find a shot by description | Media Intelligence | Search panel, natural-language query | Included |
| Match grade across shots | Color Match | Lumetri → Color Match, pick reference/target | Included |
| Smooth a talking-head jump cut | Morph Cut | Video Transitions → Dissolve → Morph Cut | Included |
| Retime a music bed | Remix | Essential Sound → tag "Music" → Remix | Included |
| Isolate/track a subject for a mask | Object Mask | Effect Controls → Object Mask, hover-click | Included |
| Burn captions without Premiere | ffmpeg `subtitles` | See Automation hook | Free |
| Fake "extend" without Firefly | ffmpeg `tpad` | See Automation hook | Free |
| Fake reframe without Premiere | ffmpeg crop+scale | See Automation hook | Free |

## Named tools

### Generative Extend (Firefly Video Model)
Extends a clip's head/tail by generating new frames in-timeline. Firefly Standard $10/mo =
2,000 credits, Firefly Pro $29.99/mo = 7,000 credits (seen 2026-08-21); one video generation
reported ~20 credits for 1080p/24fps/5s — credits shared with Photoshop/Illustrator use.
Win/Mac, cloud, built in. "The killer feature" in 2026 write-ups; Adobe's FAQ documents min
source durations (video ≥2s, audio ≥3s) and a Regenerate/Revert flow — iteration is expected.

### Auto Reframe
Sensei motion tracking that regenerates crop keyframes on aspect-ratio change. Included, no
credits. Win/Mac, native, Sequence menu. Reviewers converge on "80–90% there" for single-
subject/talking-head shots; busier frames need manual cleanup.

### Enhance Speech (Adobe Podcast)
Cloud neural dialogue cleanup from Essential Sound. Podcast Premium $9.99/mo or $99.99/yr
(4 hrs/day enhanced speech; seen 2026-08-21); free tier 1 hr/day, 30-min files. Win/Mac, cloud
— also shipped as a standalone CEP panel per one source, notable given CEP's 2026 decline (see
Traps). Quick dialogue rescue, not full restoration.

### Scene Edit Detection
Analyzes an already-flattened clip and inserts edit points at detected cuts. Included. Win/Mac,
native, right-click a clip. 2026 coverage frames it as a recut/repurposing tool; a 40%+
time-saving claim traces to a vendor blog, not Adobe — unverified.

### Text-Based Editing (Transcript panel)
Local speech-to-text; editing the transcript ripples cuts into the sequence. Included, local.
Win/Mac, native, Window → Text. Mature since ~2022; entry point for Auto Captions and Media
Intelligence text search.

### Auto Captions / caption styling / caption-to-graphics
Transcribe → Create Captions → style once, push via EGP "Track Style" → optionally "Upgrade
Caption to Graphic" for a keyframable graphic. Included. Win/Mac, native, Text panel + EGP.
Solid for static styled captions; kinetic/animated captions still mostly need a plugin or
CapCut round-trip — upgrading to a graphic enables keyframing, it doesn't auto-animate.

### Media Intelligence search
Local semantic index, searchable by natural-language description (image or sound). Included;
Adobe states local analysis, no training use (secondary coverage — no primary Adobe page
confirmed, flagged as a gap). Win/Mac, native, Search panel. Standout 26.0 (Jan 2026) feature;
UXP exposure explicitly unresolved — an open Adobe thread asks if it'll ever be scriptable.

### Color Match
One-click grade match: pick reference + target frame, adjusts tone wheels/saturation, optional
face-detection for skin tone. Included, part of Lumetri Color. Win/Mac, native. Reliable on
same-lighting multicam/interview work; degrades on high-contrast or unusually lit references.

### Morph Cut
Legacy (pre-Firefly) face-tracked, frame-interpolated transition smoothing a jump cut in a
talking-head shot. Included, native transition. Win/Mac, Video Transitions → Dissolve. Still
shipped but visibly the oldest tool here — 2026 threads report unrealistic hand transitions and
open requests to rebuild it; GPU-heavy, Adobe flags <2GB VRAM as slow.

### Remix (Essential Sound)
Analyzes a music track's phrase structure and re-edits (not time-stretches) it to a target
duration. Included. Win/Mac, native. Mature since v22.2; works best on instrumental/lightly-
vocal tracks, degrades on vocal-forward or structurally loose music.

### Object Mask
Hover-click AI subject isolation with built-in tracking over time, applied via Effect Controls.
Included. Win/Mac, native (26.0+, Jan 2026; API extended in 26.3). Fast on clean single
subjects ("kills 90% of rotoscope jobs" per one reviewer) but weaker than Roto Brush or Mocha
Pro on crowded scenes, fine hair, or motion blur — editorial-grade, not VFX-grade.

## Automation hook

**Premiere/UXP side.** None of these are documented match names the way Gaussian Blur is —
they're panel/menu actions, so discovery is the entry point, not a known string:
- **Object Mask**: `ObjectMaskUtils` class confirmed added in **v26.3.0** (Adobe's own
  changelog, fetched 2026-08-21) — method surface not itemized. Discovery step: enumerate
  `ObjectMaskUtils` members at runtime once the bridge has 26.3+ loaded.
- **Transcript / captions**: `Transcript` gained `querySupportedLanguages` and `hasTranscript`
  in 26.3.0 (same changelog). A `CaptionTrack` exists but an open Adobe community thread
  (2026-08-21) reports no documented way to read/modify individual caption item properties.
  Discovery step: `getTrackItems({ trackItemType, includeEmptyTrackItem })` returns caption
  items; property-level editing is UNTESTED.
- **Generative Extend, Auto Reframe, Scene Edit Detection, Color Match, Remix, Morph Cut,
  Enhance Speech, Media Intelligence**: no UXP class or match name found this pass — they read
  as UI-only actions. Discovery step for the bridge: try `VideoFilterFactory.getMatchNames()`
  filtered for `"Morph"` / `"Reframe"` to see if any register as an applyable effect object
  versus a menu-only command. Biggest open question for the automation project — flagged as a
  **gap**, not asserted either way.

**ffmpeg side** (mechanical fallbacks, none reproduce AI quality):

- Burn styled captions from an SRT — **TESTED** 2026-08-21, 1376×768 dummy clip:
  ```
  ffmpeg -i in.mp4 -vf "subtitles=captions.srt:force_style='FontName=Arial,FontSize=28,PrimaryColour=&H00E8E8E8,Outline=2,Alignment=2,MarginV=60'" -c:a copy out.mp4
  ```
- Freeze-frame "extend" a clip's tail (no generative fill) — **TESTED** 2026-08-21:
  ```
  ffmpeg -i in.mp4 -vf "tpad=stop_mode=clone:stop_duration=2" out.mp4
  ```
- Center-crop "reframe" 16:9 → 9:16 (no subject tracking) — **TESTED** 2026-08-21:
  ```
  ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920" out.mp4
  ```

## BadCode fit

- **Generative Extend** stacks a second model's guesses on already-Veo-generated 1376×768
  clips — expect seams at high-motion points; the ≥2s minimum means it can stretch, not rescue,
  a too-short beat. Prefer regenerating in Flow for load-bearing shots (title card, key beat).
- **Auto Reframe** is low-risk on BadCode's static, monumental-architecture shots but check
  edges by eye — near-black palette gives Sensei little contrast to key motion off.
- **Color Match** helps hold the cool-neutral grade across separate Flow generations, but the
  near-black/one-light look is the high-contrast condition sources flag as degrading it — a
  starting point, not a final grade.
- **Remix**: BadCode's Suno tracks are vocal-forward D&B, the profile every source says Remix
  handles worst — scratch/temp timing only, never a release track.
- **Morph Cut**: no single-subject talking-head footage in the pipeline — skip it.
- **Object Mask**: plausible for isolating a character against near-black for a compositing
  move — "solo subject, clean background" is its reported strength.

## Traps

- **CEP is breaking now, not eventually.** Premiere Pro 2026 no longer loads legacy CEP
  extensions by default (multiple 2026 sources, incl. a live GitHub bug report). Enhance Speech
  is documented as a CEP panel in one source — verify before automating around it.
- **"Included" still meters at volume.** Enhance Speech past the free daily cap and Generative
  Extend both fall into paid tiers/credit pools under heavy use.
- **The credit-cost figure is thin** — 20-credits-per-5s-1080p came from a secondary
  aggregator, not Adobe's pricing page; Adobe's own FAQ timed out on repeated fetch attempts
  this pass. Re-verify before quoting externally.
- **UXP method-level detail for `ObjectMaskUtils`/`CaptionTrack` is undocumented publicly** —
  classes confirmed to exist, callable surface not found; start with runtime introspection.
- **Media Intelligence's API exposure is an open question at Adobe itself** — don't plan
  automation around it being UXP-reachable.

## Sources

- [Adobe — Generative Extend overview](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-overview.html) — accessed 2026-08-21 — official feature description, Firefly-powered
- [Adobe — Add frames using Generative Extend](https://helpx.adobe.com/ca/premiere/desktop/edit-projects/edit-with-generative-ai/add-frames-using-generative-extend.html) — accessed 2026-08-21 — min clip durations, regenerate/revert
- [Adobe — Object masking in Premiere](https://helpx.adobe.com/lv/premiere/desktop/add-video-effects/work-with-masks/object-masking.html) — accessed 2026-08-21 — official Object Mask workflow docs
- [Adobe — Morph Cut overview](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/morph-cut-overview.html) — accessed 2026-08-21 — official Morph Cut mechanics, GPU caveat
- [Adobe — Scene Edit Detection](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/detect-edit-points-using-scene-edit-detection.html) — accessed 2026-08-21 — official feature page (found via search; direct fetch timed out)
- [Adobe — Text-Based Editing: transcribe video](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/transcribe-video.html) — accessed 2026-08-21 — Transcript panel workflow
- [Adobe UXP Premiere Pro changelog](https://developer.adobe.com/premiere-pro/uxp/changelog/) — accessed 2026-08-21 — confirms ObjectMaskUtils + Transcript API additions in v26.3.0
- [AI Tools DevPro — Adobe Podcast guide (secondary)](https://aitoolsdevpro.com/ai-tools/adobe-podcast-guide/) — accessed 2026-08-21 — Premium tier price/limits, not a primary Adobe pricing page
- [Community thread — Media Intelligence API exposure](https://community.adobe.com/questions-729/will-media-intelligence-new-search-panel-be-exposed-to-premiere-pro-api-1416453) — accessed 2026-08-21 — confirms UXP exposure is an open/unanswered question
- [Puget Systems — Premiere Pro Media Intelligence explainer](https://www.pugetsystems.com/blog/2025/02/27/premiere-pro-media-intelligence-what-is-it/) — accessed 2026-08-21 — independent reviewer explanation of the feature
- [ffmpeg.org — Filters documentation](https://ffmpeg.org/ffmpeg-filters.html) — accessed 2026-08-21 — official reference for subtitles/tpad/crop filters used above
