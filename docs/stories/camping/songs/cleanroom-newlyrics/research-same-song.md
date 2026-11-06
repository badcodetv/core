# Same song, new lyrics: what Suno (late 2026) can actually do

Web-only research, 2026-11-06. Tags: [vendor] Suno's own pages · [tested] someone published a controlled test · [reported] a user/blog account · [inference] my reasoning, not evidenced.

## Answer (ranked)

1. **Suno Studio, on the ORIGINAL song: extract stems → select only the vocal region of one verse → Replace (or Cover-on-region) with new lyrics + the original vocal style text, high Audio Influence, Follow Track Tempo.** The instrumental stems are never regenerated, so the beat is bit-safe by construction; only the vocal is new. Best-evidenced route for "same singer". Premier plan. Do it verse by verse.
2. **Song Editor → Edit Lyrics / Replace Section on the original song, section by section (v6 re-generates older songs' edits with v6).** Keeps the rest of the song, but the replaced region regenerates beat AND vocal together; voice drift and seams are reported. Officially 10-30 s per replacement (2024 notes; v6 limit not found).
3. **Custom model trained on the song itself (≥6 uploads), then regenerate with new lyrics.** One blog calls it the closest; single source, unverified, and it is a regeneration, so the beat will not be identical.
4. **Fallback outside Suno: write/record (or generate) the new vocal, then voice-convert it with an RVC model trained on our own separated vocal stems, and align per section to the original instrumental.** Feasible; rap quality depends on clean stems and enough minutes per voice.
5. Persona/Voice from the song + Add/Edit vocals: weak. Voices are built for *your own* voice; making one from a generated song is contested in 2026 and one Persona = one singer, so two rappers need two passes.
6. Remaster, Extend, Cover: none changes only the lyrics. Cover with max settings "usually lands pretty close" per one blog (not used here, noted only).

## 1. Working on the original song directly (Replace Section / Edit / Edit Lyrics)

- Song Editor: highlight a region → **Edit Lyrics** → type new words in "Replace Lyrics" → **Replace Section**; alternates appear in an Edits Library; you can drag the boundary to tune the transition. [vendor] https://help.suno.com/en/articles/6141505
- Older path: More Actions → Edit → Replace Section → drag-select → edit lyrics → **Recreate Section**; Suno makes **two** versions, the chosen one becomes a new Full Song; the original stays. [vendor] https://help.suno.com/en/articles/3271873
- **Length: "must be 10-30 seconds long"** (Oct 2024 release note, Pro/Premier). [vendor] https://suno.com/release-notes/replace-section — whether v6 changed this I could NOT find. One test saw the editor's working range expand past the selection (0.4 s lyric pick became ~2.6 s). [tested] https://acltracks.com/2026/10/acltracks/editing-a-song-in-suno-v6-what-actually-changes/
- At 174 BPM one bar = 1.38 s, so 30 s ≈ 21-22 bars [inference]: one verse per replacement probably fits; a long verse 3 may need two chained replacements.
- v6 claims: "Change one section while preserving everything else", "update one lyric without regenerating the song" (v6 launch, 2026-09-09). [vendor] https://suno.com/release-notes · v6 FAQ: https://help.suno.com/en/articles/13924481
- **Older songs:** pre-v6 models are retired; old songs stay unchanged in the library; "any new iterations will be made with our latest models". So a June-2026 v5 song can be edited, but the replaced section is a **v6** generation [vendor] (same FAQ). Mismatch of v6 timbre against v5 surroundings is likely [inference].
- Changing the displayed lyrics alone does not change what is sung. [vendor] https://suno.com/release-notes
- **Bit-identical rest of song: NOT established anywhere.** The one controlled test did not complete an audio comparison and calls it unknown. [tested] acltracks link above. Suno says the original is written into take lanes as a "non-destructive safety net". [reported] https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/song-editor-in-suno-v5-workflow — practical fix [inference]: only keep the replaced bars; splice them into the original WAV ourselves at bar lines, so the rest IS bit-identical.
- Same voice: no guarantee. "No guaranteed one-click ... swap this singer and keep every other detail identical" [reported] https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/change-voice-in-suno-without-restarting ; Studio users: new lyrics on a section "always generates it with a different voice than the rest of the track" [reported] (Reddit snapshot via search, https://reddit.sentinel-team.org/posts/1rvm5zv/snapshots/2026-03-17T01%3A21%3A22.866161Z); v6 one-phrase swap came back "a different track with the same voice, three times" [reported] https://heho.ai/blog/suno-v6-what-changed-for-lyrics ; the Editor "can change the melody too" [reported] https://sunogpt.ai/blog/change-lyrics-suno-without-ruining-song
- Seams: "seam quality varies between takes"; pick boundaries on a bar line or lyric-line edge; Replace "keeps the timing". [reported] https://www.suno-api.io/en/blog/suno-studio-mute-cut-replace-section/ (2026-10-31). Turn Variety down so only the edit moves. [reported] https://heho.ai/blog/suno-v6-what-changed-for-lyrics
- Chaining every verse: nothing forbids it; no source tested it. Each pass makes a new full song, so run them in sequence on the chosen output [inference].
- **Adding a 4-line hook over a drop that currently has no vocal**: the region has no lyrics to edit, so it is the same Replace on an instrumental region with new lyrics typed in [inference]; not tested by anyone I found. The drop's beat would be regenerated unless done on the vocal stem only in Studio (§3).

## 2. Personas / Voices

- v5.5 (2026-03-26) moved Personas into a **Voices** tab; Voices = "record or upload your own audio", with a spoken verification phrase. [vendor] https://suno.com/release-notes ; https://help.suno.com/en/articles/11362305 ; verification: [reported] https://www.mindstudio.ai/blog/suno-5-5-voice-cloning-ai-music-generator
- Persona from an existing song (More Actions → Create → Make Persona / "Create > Voice"): sources conflict on whether it still exists; one says "You can no longer make new persona/voice from existing songs"; greyed out for uploads/covers/extends. [reported] https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-personas-update-dec-2025-what-changed-how-to-use-it , https://diyai.io/ai-tools/audio-generation/suno-persona-not-working/
- A song Persona carries "voice, style, and related traits" — the song's essence, not a clean timbre lock. [reported] change-voice link above.
- With Add Vocals: Audio Influence acts on every vocal source, so vocals in the source pull as hard as the Persona; "the original vocal seems to dominate". [reported] https://reddit.sentinel-team.org/posts/1salh45/snapshots/2026-04-03T23%3A40%3A05.740169Z ; upload audio carries "timing, melodic contour, feel", not vocal identity. [reported] https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-add-your-own-voice-guide
- **Two singers:** found nothing on a two-voice Persona or using two Personas in one song. [not found] Inference: one Persona per pass, so verses must be done per rapper.
- Whether a "Voice" from a generated (non-human) vocal passes Suno's own-voice verification: not found; the policy is own voice only [reported], so likely not [inference].

## 3. Suno Studio (stem-level vocal regeneration)

- Studio: open song → **Extract Stems** (Vocals + Instrumental or all) → duplicate the vocal track → select it → enable **Follow Track Tempo** → choose Vocals → singing style + new lyrics → **Recreate**, Audio Influence raised. Instrumental untouched. ~3 rounds (6 takes) for a usable Japanese re-sing. Tempo drift still happened; Follow Track Tempo "sometimes better off". [reported, Oct 2025, Premier] https://note.com/highdrama/n/n5976b6474d6d?hl=en
- Same route with Cover on the vocal region + copying the original vocal style prompt: "sounded way, way better than the editor ... sounds like the same singer". [reported 2026-07-29] https://sunogpt.ai/blog/change-lyrics-suno-without-ruining-song
- Studio 2.0 (2026-08-13, Premier): chat bar "can generate instruments and vocals in Studio". [vendor] https://suno.com/release-notes ; split up to 12 stems, rework them in Studio or Song Editor. [vendor] https://suno.com/products
- Why this beats our failed run [inference]: our run fed an instrumental into Add/Edit vocals as a NEW song (beat regenerated, voice described from scratch). Studio regenerates only the vocal lane against the original song's own context and vocal, so the beat cannot drift; the voice has the original take beside it as reference.
- Not found: whether Studio region-replace has the 10-30 s limit; whether it can keep TWO voices in one vocal stem (likely do one rapper's lines per region [inference]).

## 4. Other routes

- **Custom model on the song itself:** upload the WAV ≥6 times to train a custom model, then remix with new lyrics — "gets closest to the same song with new words". [reported, single source] sunogpt link above. Custom models need ≥6 tracks [vendor] https://suno.com/release-notes ; v5.5 custom models auto-upgrade to v6 [vendor] v6 FAQ. Still a regeneration: arrangement/timing will not be identical [inference].
- **Max Mode**: recommended for "covers that should stay close to the original" and "keeping vocals and style consistent across a track". [vendor] v6 FAQ.
- **Remaster**: re-renders audio; no lyric input. Not a lyric route. [vendor, by omission] v6 FAQ.
- **Extend from a point**: regenerates everything after the point. Loses the beat after it. [inference]
- **Cover** (not used by us): weirdness 0, style + audio influence 100 "usually lands pretty close"; Studio author found Cover "changed the melody and structure even at high-fidelity settings". [reported] sunogpt + note.com links.
- v6 takes vary a lot run to run with identical settings. [reported] https://moelueker.com/blog/suno-v6-vs-wild-vs-mini-150-song-test

## 5. Fallback outside Suno (brief)

- **Align a new vocal to the original instrumental:** cut the new vocal per section at bar lines and time-stretch to the grid (Premiere/ffmpeg rubberband, or VocAlign/Revoice Pro-style tools which align one take's timing to a guide take — here the original vocal stem is the guide). [inference; tool behaviour well known, not re-sourced]
- **Voice conversion:** RVC v2 / so-vits: train a model per rapper on that rapper's separated, clean, single-speaker vocal ("5+ minutes ... no background music ... single speaker per model" is a typical requirement). [reported] https://www.fiverr.com/asmodeus22/do-professional-ai-song-covers-and-custom-rvc-voice-models , training guide https://voicechanger.live/hub/how-to-train-rvc-model ; few samples → inconsistent output. [reported] https://apatero.com/blog/best-rvc-voice-models-guide-comparison-2026
- **Data problem** [inference]: one 3:35 song with two rappers gives roughly 1-1.5 min per voice, under typical minimums; add more takes of the same voice from our Suno library if any exist. Gravelly timbre and run-on flow: RVC carries timbre well, not flow; flow comes from the source performance (a human or TTS/Suno take rapped to the grid).
- **Legality:** paid Suno subscribers get commercial use of output made while subscribed; Suno warrants no copyright vests; terms reshaped after the Warner deal (Nov 2025). [reported] https://www.musicinafrica.net/magazine/suno-adjusts-ai-music-ownership-terms-after-warner-music-partnership , https://terms.law/ai-output-rights/suno/ . Training a private RVC model on our own Suno stems: found no clause forbidding it, and no real person's voice is involved [inference]; read suno.com/terms (not fetched).
- Rap-specific RVC quality evidence: not found.

## Could NOT find

- v6's current Replace Section length limit (only the 2024 10-30 s figure).
- Any audio-diff proof that unedited parts stay bit-identical.
- Any test of chaining replacements across a whole song, or adding vocals over an instrumental drop via Replace.
- Two-singer Personas; whether a Voice can be made from a generated vocal.
- Whether Studio's region replace keeps a v5 voice when the new take is v6.
- Rap-specific RVC results; current Suno ToS text (only secondary summaries).
