# Lip sync: why it keeps failing, and what to try (sweep, 2026-11-18)

Date: 18 November 2026. For Kai. Asked for by Kai the same day: "we're missing a trick".

How this was made: twelve web researchers, one angle each, then this plan. Nobody ran any tool for this
document. Every number from outside is someone else's claim, with its date, and graded in the appendix:

- **official**: the maker's own documentation.
- **tested**: the source ran a test and shows the result (often one run, often their own product).
- **community**: a blog, forum or guide that states things without showing a test.
- **marketing**: a vendor selling the thing.
- **guess**: a researcher's or my own inference. Marked every time.

Our own records are the other evidence: `.claude/skills/lip-sync-dub/SKILL.md`, `docs/rules/voices.md`,
today's run (`docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/lipsync-2026-11-18.md`) and
Kai's picks (`.../feedback/lipsync-picks-2026-11-18-r2.json`).

Three standing rules are flagged wherever an idea touches them. Nothing here decides them for you:
**never speed or slow the picture, never chop the voice line, never LatentSync.**

---

## The short answer

There is no timing prompt we have missed. Google documents no way to pin words to times in Omni or Veo, and
no way to feed Flow our audio (official, read 2026-11-18).

The trick we are missing is bigger than a prompt. **We make the mouth and the voice separately, each blind
to the other, then try to slide one onto the other.** People who get this right do not do that. They make
one side *from* the other:

- the voice first, then a picture model that draws the mouth to that audio, or
- the clip first, then a voice made from the clip's own performance.

Inside Flow plus Gemini alone, neither is possible today. So the choice is: step outside Flow for talking
close-ups, or stay inside and accept "better odds", not "solved".

---

## Why it keeps failing

**1. Omni talks at its own pace and we cannot set it. (Finding, ours and theirs.)**
Our record: Omni mouths a line 1.2 to 2.0 times faster than the Gemini voice. "Calmly and unhurriedly" in
the prompt was ignored (skill table, 2026-10). "Slowly" still came back at about 1.0 s. A 7-word line was
mouthed in 1.4 to 1.7 s against a 2.9 s voice take (2026-11-15). Today, "I'm really sorry, love." fitted
only at the 1.14 to 1.15 cap on every take.
Outside: Google's prompt guide has no timestamp syntax, no pace control and no lip-sync section (official).
The one measured test found the model picks its own rate: 8 words took 4.3 s, a 39-word line was rushed at
about 4 words a second and lost its last 8 words (tested, one run each, Veo 3.1 Fast, 2026).

**2. Neither side can hear the other. (Finding.)**
Flow takes no audio file: "Uploading audio inputs or audio references is unsupported in the current version
of the API" (official). Gemini TTS takes no target length and gives back no word times (official page is
silent on both; a Google forum thread, Oct to Nov 2026, calls it a known limit: community).
So 10 clips x 10 takes is a hundred dice rolls, hoping two land alike.

**3. One start plus one speed is two knobs. A line with a pause needs more. (Finding, arithmetic.)**
Line 7-0 fitted at tempo 1.00: the length was right. You still called it "just off". So the total matched
and the rhythm inside did not. (Guess: the pause after "underground," sits in a different place in the
clip.) No single speed can move one pause without moving everything after it.

**4. Front-on close-ups are the strictest case there is. (Finding, from published tolerance tests.)**
People notice audio about 45 ms early or 125 ms late. They accept up to about 90 ms early or 185 ms late
(ITU-R BT.1359, as reported by two secondary sources). A newsreader-style face is the least forgiving
picture (tested, 2022 paper). Our shots of Sandra and Derek are exactly that.
Human dubbing never matches every syllable either. It pins the start of a phrase, the end, and the b, p and
m lip closures, and lets the middle flow (community, dubbing craft). Our skill already says this.

**5. Our score may be ranking the wrong thing. (Guess, small sample.)**
The fit score is loudness against mouth opening. The skill itself calls that "too blunt". Today you picked
the third-ranked pair on two of the four lines you picked (6-0 and 7-2). Four lines is not proof.

**6. Short lines in long clips. (Guess.)**
"I'm really sorry, love." is 4 words in a 5 s clip. Omni says it in about a second and the voice cannot
get that fast inside 1.15x. Our own rule is "size the clip to the voice". Omni 1.2 now goes down to 3 s.

**7. The voice side is on old settings. (Finding, from `docs/rules/voices.md`, 18 Nov.)**
Today's takes used `gemini-3.1-flash-tts-preview` with a long prose profile. Google's current page lists
`gemini-3.8-flash-tts` and advises short style strings, with `<short pause>` and `<long pause>` tags placed
exactly where the pause should be (official). Whether 3.8 follows pace directions better is a researcher's
reading of the docs, untested by us.

**What it is not:** timestamp or JSON prompting. Google shows `[00:00-00:02]` blocks for shots and sound
effects only. One guide calls them "budgets, not frame-accurate edit points" (community, 2026-11). Nobody
shows them moving a word.

**One thing our own record already proved:** an on-screen *event* does move the mouth. On 2026-11-04 the
prompt "lips pressed together, thinking for a moment, then says: ..." held the lips shut for 1.5 s. That
matches the one outside claim that event cues land better than timecodes (community). Pace *words* do not
work; an *action before the line* does.

---

## Do this first: a free measurement (1 to 2 hours, no money, no credits, no rule touched)

Before buying anything, find out what kind of "off" each line is. All the files exist already.

For scene A's five lines, on the pair you picked (and the best-scored pair for 7-0):

1. Word times for the Gemini take (forced alignment, Montreal Forced Aligner or WhisperX) and for the
   clip (its own audio, corrected to the tracked mouth as `voice-row-fit.py` already does).
2. A table per line: each word, how many ms the voice is early or late against the mouth.
3. Mark each word: inside the 45 early / 125 late window, marginal (to 185 late), or out.

What it tells us:

- **Errors bunch up after a pause, words either side are fine:** the pause is in the wrong place. Bets 2
  and 4 can fix that.
- **Errors spread through every word:** the syllable pace differs. Only bets 1, 3 or 5 can fix that.
- **Everything is inside the window and it still looks off:** the mouth shapes are wrong, not the timing
  (guess: possible on 7-0). Then only a new mouth (bets 1 and 5) or a side shot helps.

It also gives a pass/fail number to replace the blunt score, and a fair reason to send a line to a cover
shot without another round of re-rolls.

---

## What to try, best bet first

### 1. Best bet: voice first, picture made to it (for talking close-ups only)

**What.** Give a picture model the approved still and the whole Gemini take. It draws the whole shot, mouth
included, to that audio. Candidates: OmniHuman 1.5, Kling Avatar 2.0, Hedra Character-3, Seedance 2.0
(image plus audio plus prompt). Flow still makes every other shot.

**Why it should work.** The mouth is built from our audio, so there is nothing to line up afterwards. The
voice stays whole and untouched. It is a real generated mouth, not a patch over one (your objection to
LatentSync on 2026-11-11 was "not her actual natural mouth").
- Tested: Curious Refuge's hands-on comparison (2026-05-11, one clip per test) says make the audio first,
  then pair it with an image. Seedance 2.0 with image plus audio gave accurate sync; OmniHuman 1.5 was their
  pick for animation, HeyGen for live action.
- Tested by its own authors: Kling Avatar 2.0 paper (2025-12) claims better lip sync than OmniHuman 1.5.
- Official: OmniHuman 1.5 takes image, audio and a text prompt (Replicate page, read 2026-11-18).
- Marketing: the prices below.
- Nothing was tested on our stills or our look.

**Cost.** About 5 to 16 US cents per second (marketing figures: OmniHuman 1.5 on fal $0.16/s, Kling avatar
resellers $0.05 to $0.12/s, Hedra about 5 c/s at 720p). Scene A's five lines are about 28 s, so one take of
each on one model is roughly $1.50 to $4.50. A three-model bake-off with two takes each: about $15 to $25.
No Flow credits. Half a day.

**Risk.** The shot is no longer a Flow shot: the look, the acting and the face can drift from the still.
These are avatar models; evidence on stylised, cinematic and two-person shots is thin. The acting may be
plain "talking head". Seedance can invent extra words. Clips go to an outside service.

**Standing rules.** Picture speed: not touched. Voice: whole. LatentSync: not used. **Flags for you:** it
leaves Flow for these shots; it needs a new account and money (accounts and money are your call); and
whether "audio-driven face models" fall under the spirit of the LatentSync ban is yours to say.

**Cheap first test.** All five lines of scene A, from sandra-SB07b and derek-SB07c, with the voice takes
you already picked, on two or three of the models. Put them on a picks page beside today's best pairs,
unlabelled. It passes if you pick them on sync *and* they still look like the film. It dies if the look or
the acting is wrong, however good the lips are.

### 2. Best bet that stays inside Flow and Gemini: close the loop

**What.** Four cheap changes, run together, no new tools or accounts:

- **a. Size and shape the clip from the voice take.** Pick the Gemini take first. Set the clip length to
  the take plus about a second (Omni 1.2 moves in 1-second steps from 3 s). If the take has one clear
  pause, write it as an action: "she glares at him for a moment, then says: ...". Not as "[0.5s pause]".
- **b. Re-voice to the clip with pause tags.** Where the picked clip pauses, put `<short pause>` or
  `<long pause>` at that exact spot in the Gemini text, on `gemini-3.8-flash-tts`, short style string.
- **c. Roll more clips cheaply and let the measurement choose.** Rank every clip by how close its own
  rhythm is to the take (word gaps and pause position), then show you only the top two.
- **d. Score by anchor points.** Phrase start, phrase end, and b/p/m closures, against the tolerance
  window from the free measurement. Voice 0 to 85 ms late, never early.

**Why it should work.** It attacks causes 3, 5, 6 and 7 without touching a rule.
- Official: Gemini pause tags and punctuation move pauses; Omni duration is settable per second.
- Ours: the action-before-the-line prompt held a mouth shut for 1.5 s (2026-11-04). "Re-voice to the clip"
  landed a take within 0.25 s (2026-11-04).
- Community only: `[beat]` and `[0.3s pause]` tokens in the Flow prompt. No measurement anywhere. Worth
  one control arm, not belief.
- **Honest ceiling (guess):** this raises how often a line fits. It will not make it reliable, because
  cause 1 stays: we still cannot set Omni's syllable pace.

**Cost.** No money beyond normal TTS. Flow credits: Omni 1.2 at 720p is 3 a second, so a 5 to 6 s clip is
15 to 18 credits; ten more clips for each of five lines is about 750 to 900 credits (figures from our
2026-11-09 sweep; check the compose bar). Drafting at 360p costs a third, if the mouth tracker still reads
a 360p face (guess, check on one clip first). About a day of scripting and running.

**Risk.** Low. Mostly that it gives a small gain and reads as "another round of the same".

**Standing rules.** None touched.

**Cheap first test.** Lines 7-0 and 7-2 only (the two with an internal pause, and the two you sent to a
side shot). Three prompt arms from the same still, eight clips each: plain; action-anchored pause; `[beat]`
token. Measure whether the pause moves by more than the spread between plain clips. If the action arm does
not move it, drop 2a and keep b, c, d.

### 3. The clip's own performance in the Gemini voice (voice conversion)

**What.** Take the clip's own muted audio and run it through a speech-to-speech changer whose target is a
clone of the cast's Gemini voice. Out comes the clip's exact timing in (roughly) our voice.

**Why it should work.** The new voice copies the pace and pauses of the source, so it moves with the mouth
by construction.
- Official (the vendor's own claim, not independently measured): ElevenLabs Voice Changer keeps cadence,
  delivery and emotion; takes audio or video up to 5 minutes; can target a cloned voice.
- Community: about $0.0037 a second through one reseller; it copies mumbles and accent traces too.
- Tested by its own authors: the open tool Seed-VC (repo archived 2025-11-21, GPL-3.0).
- From our record: Omni's audio sits 0.45 to 0.7 s off its own picture on some clips. So the converted
  voice still needs one whole-take slide onto the mouth. That is inside the current method.

**Cost.** About a dollar of conversion for the test, plus whatever plan voice cloning needs (not checked).
An hour or two.

**Risk.** The big one: it carries Omni's *acting*. If what puts you off the video voice is the delivery,
this fails at once. If it is the tinny sound and the voice changing between clips, this may pass. Only
your ear can tell. Also: check ElevenLabs' and Google's terms on cloning a TTS voice before anything ships.

**Standing rules.** Picture speed: not touched. Voice: not chopped. LatentSync: not used. **Flag:** the
voice is then no longer the Gemini take. That changes the reason we use Gemini at all. Your call.

**Cheap first test.** One line each for Sandra and Derek. A blind listen: the Gemini take, the Omni
original, the converted one. If you cannot bear the converted one, the idea is dead for a dollar.

### 4. A gentle, continuous stretch of the voice (not one speed)

**What.** Keep the take in one piece, but let its speed vary smoothly along the line so that word starts
land on the mouth: mostly by lengthening or shortening the *silences*, hardly touching the words. Done
with Rubber Band's time map (free, local).

**Why it should work.** This is how film dubbing software does it.
- Official: VocAlign builds a warp path between guide and dub and applies varying stretch; Rubber Band's
  `--timemap` and `pyrubberband.timemap_stretch` do the same from a list of anchor pairs.
- Tested (tiny set, 2018): Halperin and others warped audio to lip video and kept the drift under about
  0.1 s; 1 to 2 percent of frames fell outside the broadcast window.
- Against: our own `dtwsync.py warp` squeezed a word away and sounded robotic (2026-10-19). That warp had
  no clamp and chased the clip's audio. The paper also admits hard warps degrade the sound. Dubbing
  research prefers getting durations right inside the TTS over warping afterwards (community reading).
- Guess: pauses take far more stretch than vowels before the ear objects. No source gives a figure.

**Cost.** Free. About a day to build and run on today's 10 x 10 set.

**Risk.** Warble if the clamp is loose. It only helps lines the free measurement shows as "pause in the
wrong place". It cannot make a 1.7x gap fit.

**Standing rules.** Picture speed: not touched. LatentSync: not used. **Flags:** nothing is cut or
spliced, but the speed is no longer uniform, so the "one tempo, 0.97 to 1.15" rule would become a
per-stretch clamp. And you heard "choppy" when a line was cut into four on 2026-11-04. Whether a smooth
stretch counts as chopping is yours to rule on.

**Cheap first test.** Line 7-0 only, the take that scored best. Two versions: silences only; silences
plus words clamped to 0.9 to 1.15. A blind listen against the untouched take for warble first, then
against the picture.

### 5. Redraw only the mouth with a hosted tool (sync-3)

**What.** Send the muted Flow clip and the whole Gemini take to a mouth-redraw service. Same idea as
LatentSync, different engine.

**Why it might work.**
- Official (the vendor's own docs, read 2026-11): Sync Labs sync-3 lists side profiles, over-the-shoulder
  shots, hands in front of the face and 4K. Its older lipsync-2-pro works on a 512 px face crop and is
  weak on profiles. Kling Lipsync takes a 2 to 10 s clip plus audio.
- Tested: Curious Refuge found Freepik Speak best on live action for video plus audio, and Sync misdubbed
  two-speaker scenes.
- Nothing independent on Omni footage. Most comparisons are written by the vendors.

**Cost.** sync-3 about $0.11 to $0.13 a second: scene A's five lines about $3.50 a pass. An hour.

**Risk.** The same complaint you already made: it is a redrawn mouth, not hers. Soft teeth, a seam, a
changed face. Jack's note of 2026-11-16 is that the last tool of this kind "does not work".

**Standing rules.** Picture speed and voice: not touched. **Flag, the strongest in this list:** this is
the LatentSync family. Sync's own blog names LatentSync as the open-source option, and tools like Magic
Hour and Freepik Speak do not say what engine they use. Do not run this unless you say the ban is on
that one tool and not on the idea. New account and money too.

**Cheap first test.** Only if you lift the flag: line 7-0 (the one with no pick), one pass on sync-3,
judged against the side shot you proposed.

### 6. Keep regardless: plan the cover, do not improvise it

**What.** What you already chose on 7-0 and 7-2, made a habit:

- Front-on close-ups only for short lines. Long lines and lines full of b, p, m go to a three-quarter,
  over-the-shoulder or the side two-shot, decided in the shot list.
- A cover set per speaker from the approved still: side two-shot, listener, hands or prop. Prompted
  silent, so no mouth moves.
- Let the voice run across the cut: start the line on the listener and cut to the face mid-line, or leave
  the face before the line ends (a J or L cut: sound leads or trails the picture). The face then only has
  to match the middle of the line. The take stays whole.
- A scored gate: a line that fails the tolerance window after one round goes to cover. No third round.

**Why.** Community and marketing sources all say it, and none tested it: off a close-up, plain dubbing
is "often indistinguishable" from lip sync (community, 2026-08). A study of 54 professional dubs found
dubbers put a natural voice ahead of exact lips (tested, 2022). No source confirms that true profile
syncs better in Omni. Our own note says side-on talking is "always off screen".

**Cost.** One extra clip per cover shot (15 to 18 credits at 720p). No money. **Risk.** Too much of it
and a scene of two people arguing never shows a face talking. Jack once asked for the face back
(skill table). **Standing rules.** None touched.

**Cheap first test.** Already running: your side shot for 7-0 and 7-2.

### 7. Long shots inside Flow (minutes each, mostly free)

All guesses unless marked.

- **Look for an audio slot in Flow's Omni menu.** A forum post (community, 2026-09-11) says an audio
  option shows but does not work. Try one Gemini wav. Ten minutes.
- **A Flow custom voice with slow performance notes.** Flow voices are a preset plus short notes
  (community, a third-party wrapper's docs). Pace words in the *prompt* failed for us; pace notes on the
  *voice* are untried. One batch.
- **An Omni edit turn on a picked clip:** "same shot, she says the line slower, pausing after
  'underground'". 3 credits a second. Untried anywhere we found.
- **Watch for audio input.** Google's launch post says other audio inputs come "soon" (official, no
  date). Audio references are behind an allowlist on Google Cloud (official, 2026-11-06). When that
  opens, it is likely the real fix. Check the Omni docs each month.

### Not worth the time

| Idea | Why not |
| --- | --- |
| Timestamp or JSON prompts for dialogue | Documented for shots and sound effects only; no evidence for words |
| Asking Omni to speak slowly | Failed three times in our own record |
| A wider speed range on the voice | We heard warble past 1.15 to 1.3; research agrees large rate changes distort speech |
| Speeding or slowing the picture | Standing rule; you saw it as "speeded up" on 2026-11-05 |
| MuseTalk, Wav2Lip | 256 px face crop, jitter, lost detail (its own model card); Wav2Lip weights are non-commercial |
| Lip-reading the clip for word times (Auto-AVSR) | About 20 percent word errors, no word times documented |
| Synchformer as a scorer | Steps of 0.2 s, too coarse |
| Open TTS with exact durations (MAGIC-TTS, IndexTTS2) | Would not be the Gemini voice; licences unchecked |
| Extend, or first plus last frame | No source shows either controlling speech timing |

A possible later upgrade to the scorer: SyncNet (free, MIT) run in 1-second windows shows where along a
line the sync slips. It is old and matches human judgement poorly in several papers, so check it against
your picks before trusting it. A better one (PVSync, 2026-10) has no code out yet.

---

## Suggested order

1. The free measurement (today's files).
2. In the same sitting, the one-dollar listen for bet 3. It is the cheapest thing that could change the
   whole plan.
3. If you agree to an outside account: the bet 1 bake-off on scene A's five lines.
4. Bet 2 on lines 7-0 and 7-2, whatever happens above. It costs only credits and improves every later
   Flow talking clip.
5. Bet 4 only if the measurement says "pause in the wrong place" and you rule a smooth stretch is not
   chopping.
6. Bet 5 only if you lift the flag.

## Decisions only you can make

1. May talking close-ups come from a model outside Flow (bet 1)? New account, about $15 to $25 to test.
2. Is a smooth, uncut stretch of the voice "chopping" (bet 4)?
3. Is the LatentSync ban on that tool, or on redrawing mouths at all (bet 5)? And does it reach
   audio-driven models (bet 1)?
4. Is the Gemini *take* the point, or the Gemini *sound* (bet 3)?

## Housekeeping found on the way (not changed)

- `.claude/skills/lip-sync-dub/SKILL.md` still opens with "Redraw the mouth first: LatentSync" and still
  tells the reader to cut the voice into phrases at tempo 0.85 to 1.30. Both contradict the standing
  rules. `docs/rules/voices.md` also keeps the older phrase-by-phrase advice and `flow-align.py`, which
  "eases the picture" by up to 12 percent.
- Today's run used `gemini-3.1-flash-tts-preview`; `docs/rules/voices.md` (same day) says 3.8.

---

# Appendix: every source, by angle, with its grade

Grades are the researchers' own. Where two researchers graded one page differently, both are shown.
"Snippet" means the researcher saw a search summary and did not read the page.

## A. Timing prompts in Veo and Omni

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide | official | read 2026-11-18 | "Speaker says: line"; no timestamps, pace or lip-sync guidance |
| https://aistudio.google.com/docs/omni | official | read 2026-11-18 | 3 to 15 s; duration value overrides the prompt; no audio input; no voice editing |
| https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/ | official (also graded marketing) | 2026-11-05 | "Clearer lip-sync"; 1-second voice samples as cues; 1-second duration steps |
| https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available | official | 2026-11-06 | Audio references behind an allowlist |
| https://www.wireflow.ai/blog/veo-3-prompts | tested | 2026 | 8 words in 4.3 s; 39-word line rushed and cut; one run each |
| https://www.imaginary.app/blog/veo-31-dialogue-sfx-prompts-that-actually-sync-a-creator-workflow-for-clean-mout | community (also graded marketing) | 2026-04-30 | `[beat]`, `[0.3s pause]`, 6 to 10 word lines; no measurements |
| https://dev.to/akaranjkar08/veo-31-developer-guide-timestamp-prompting-multi-shot-video-and-full-api-june-2026-3l5i | community | 2026-06-05 | Timestamps direct shots; model picks cut timing; nothing on dialogue |
| https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3 | community (also graded marketing) | 2026 | Overlong lines rush, cut off or drift; transcribe and compare |
| https://www.atlascloud.ai/blog/guides/gemini-omni-1.2-flash-multi-speaker-dialogue | community | 2026-11 | Read the script aloud; about 20 to 25 words per 12 to 15 s |
| https://developer.tenten.co/veo-331-pro-json-prompting-step-by-step.md | community | 2026 | JSON prompt fields; no dialogue field, no sync evidence |
| https://roo.beehiiv.com/p/gemini-omni-complete-guide-2026 | community | 2026 | Sync said to hold about 6 to 7 s; anecdote |
| https://ai.google.dev/gemini-api/docs/speech-generation | guess | 2026-11-18 | Pause tags belong to Gemini TTS, not Omni (researcher's inference) |

## B. Can Flow take our audio?

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://aistudio.google.com/docs/omni | official | read 2026-11-18 | Audio upload unsupported; `[0-5s]` ranges exist for actions |
| https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/ | official | 2026, undated | Only voice references at first; other audio inputs "soon" |
| https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/ | marketing | 2026-11-05 | Demo with mouth and voice references |
| https://discuss.ai.google.dev/t/critical-regression-gemini-omni-1-1-flash-update-destroyed-conversational-voice-continuity-for-ugc-creators/182433 | community | 2026-09-11 | Audio option shows in Flow but does not work; @voice tag |
| https://useapi.net/docs/api-google-flow-v1/post-google-flow-voices | community | 2026 | Flow voices are a preset plus text notes, not an upload |
| https://useapi.net/docs/articles/omni-flash-bash | community | 2026 | A voice must attach to a character image |
| https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation | official | undated | Only an audio on/off output switch |
| https://aivideopicks.com/posts/google-flow-review-2026.html | community | 2026-05 | No voiceover upload in Flow |
| https://www.mindstudio.ai/blog/gemini-omni-1-2-flash-video-generation | community | 2026-11-06 | Paraphrase of Google's post; 7 cents a second |
| https://support.google.com/flow | official | 2026-11-18 | Help index only; sub-articles not reached |

## C. Voice conversion

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://elevenlabs.io/docs/creative-platform/playground/voice-changer | official | read 2026-11-18 | Keeps cadence and delivery; 5 minutes; audio or video in; cloned target |
| https://blog.segmind.com/elevenlabs-voice-changer-how-to-convert-voices-in-2026/ | community | 2026 | About $0.00375 a second; copies mumbles |
| https://elevenlabs.io/blog/speech-to-speech/ | marketing | 2025 to 2026 | Conversion does not fix weak acting; not read in full |
| https://github.com/Plachtaa/seed-vc | official | 2025-11-21 | Zero-shot, GPL-3.0, archived |
| https://gitcode.com/GitHub_Trending/se/seed-vc/blob/main/EVAL.md | tested (own figures) | 2025 | Similarity 0.868, word errors 11.99 percent |
| https://github.com/resemble-ai/chatterbox | official | 2026-08 | MIT, retired, watermarked |
| https://www.resemble.ai/resources/best-open-source-ai-voice-cloning-tools | community | 2026 | RVC needs more training audio; no independent comparison |
| https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice | official | 2026 | Google has cloned TTS, no speech-to-speech |
| https://www.mindstudio.ai/blog/elevenlabs-voice-cloning-replace-ai-generated-voices | community | 2025 to 2026 | Hand alignment lands within about 100 to 200 ms |
| https://ndurner.substack.com/p/google-veo-31 | community here (tested in angle L) | 2025-10-26 | "About 80 percent single speaker" figure is a snippet, unverified |

## D. Audio-driven video (voice first)

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://replicate.com/bytedance/omni-human-1.5/readme | official | read 2026-11-18 | Image plus audio plus prompt; multi-character |
| https://fal.ai/models/fal-ai/bytedance/omnihuman/v1.5 | marketing | 2026-11 | $0.16 per second |
| https://www.emergentmind.com/papers/2508.19209 | community | 2025-08 | Works on animated characters; conflicting claims on full scenes |
| https://arxiv.org/abs/2512.13313 | tested (own figures) | 2025-12 | Kling Avatar 2.0 claims best lip sync |
| https://piapi.ai/blogs/kling-ai-avatar-guide-standard-vs-pro | marketing | 2026 | About $0.05 to $0.12 a second through resellers |
| https://www.hedra.com/models/video/hedra/character-3 | marketing | 2026 | 2.5 to 6.25 cents a second; stylised demos; figures from snippets |
| https://huggingface.co/Wan-AI/Wan2.2-S2V-14B | official | 2025 to 2026 | Open, Apache 2.0, needs 80 GB of video memory |
| https://arxiv.org/abs/2508.14033 | tested (own figures) | 2025-08 | InfiniteTalk: keeps the clip, redrives the mouth to new audio |
| https://lilting.ch/en/articles/infinitetalk-comfyui-lipsync | community | 2025 to 2026 | Setup list; no quality numbers |
| https://www.cometapi.com/can-veo-3-1-do-audio-and-how-should-you-use-it-professionally/ | community | 2025-10 to 2026 | No own-audio input in Veo 3.1 |
| https://help.runwayml.com/hc/en-us/articles/42311337895827 | community | 2025 to 2026 | Act-Two needs a driving video; page not fetched |

## E. Redrawing the mouth afterwards

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://sync.so/docs/models | official | read 2026-11 | sync-3 and lipsync-2-pro limits, prices, the need for speaking motion |
| https://fal.ai/docs/model-api-reference/video-generation-api/kling-video-lipsync | official | 2026-11 | Kling Lipsync: 2 to 10 s clips, $0.014 per 5 s |
| https://sync.so/blog/what-is-musetalk | marketing | 2026 | MuseTalk limits; names LatentSync as the open quality pick |
| https://huggingface.co/TMElyralab/MuseTalk/blob/main/README.md | official | 2025 to 2026 | 256 px crop, detail loss, jitter |
| https://curiousrefuge.com/blog/ai-lip-sync-workflows | community here (tested in angle J) | 2026-05-11 | Freepik Speak best on live action; Sync misdubbed two speakers |
| https://magichour.ai/blog/best-lip-sync-apis | marketing | 2026 | Says to test angles yourself; engine not named |
| https://toolradar.com/guides/best-ai-lip-sync-tools | marketing | 2026-09 | sync.so listed as the developer pick |
| https://higgsfield.ai/academy/how-to-use/how-to-make-ai-lipsync-videos-look-realistic | marketing | 2026-06-19 | Nothing usable |
| https://sync.so/docs/models | guess | 2026-11 | A redrawn mouth removes the one-speed problem; unproven on Omni footage |

## F. Timing control in the voice (TTS)

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://aistudio.google.com/docs/speech-generation | official | read 2026-11-18 | Pause tags, punctuation, pace style; no duration, no word times; 3.8 models |
| https://discuss.ai.google.dev/t/feature-request-word-character-timestamps-for-gemini-tts-output-caption-sync/186189 | community | 2026-10-01 to 2026-11-13 | No timestamps from Gemini TTS; use a separate aligner |
| https://livekit.com/blog/gemini-3.1-flash-tts-prompting-guide | community | 2026-04-27 | Punctuation for pauses; notes sometimes get spoken |
| https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-can-i-add-pauses | official | 2026-11 | Exact breaks only on older ElevenLabs models |
| https://docs.cartesia.ai/build-with-cartesia/sonic-3/volume-speed-emotion | official | 2026-11 | Speed 0.6 to 1.5, "guidance" only |
| https://arxiv.org/abs/2604.21164 | tested (own figures) | 2026-04 | MAGIC-TTS: per-word duration control, open research model |
| https://ojs.aaai.org/index.php/AAAI/article/view/40820 | community | 2026 | IndexTTS2, duration-controlled; snippet |
| https://arxiv.org/html/2406.04281v1 | tested | 2024 | Plain rate scaling can hurt quality; snippet |
| https://replicate.com/google/gemini-3.1-flash-tts/readme | community | 2026 | Bracket pause tags with lengths; conflicts with the official syntax |
| https://www.pkgpulse.com/guides/elevenlabs-vs-openai-tts-vs-cartesia-text-to-speech-2026 | community | 2026 | OpenAI TTS has no word times; weak source |

## G. Stretching the voice non-uniformly

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://www.synchroarts.com/manuals/VocAlignUltraV1.1/Manual/HTML/what-is-vocalign-ultra.html | official | undated | Warp path, varying stretch on the dub only; no limits given |
| https://synchroarts.com/manuals/legacy/VocALignProject3.3/Standalone/Manual/G_Important_tips.htm | official | undated | Best on short regions; snippet |
| https://ar5iv.labs.arxiv.org/html/1808.06250 | tested | 2018 | Audio warped to lip video, drift under about 0.1 s; tiny data set |
| https://www.forasoft.com/learn/audio-for-video/articles-audio/lip-sync-itu-r-bt-1359-tolerance-windows | community | undated | Tolerance: 45 early / 125 late to notice, 90 / 190 to accept |
| https://breakfastquay.com/rubberband/usage.txt | official | 2022 on | `--timemap`; finer R3 engine |
| https://pyrubberband.readthedocs.io/en/0.3.0/generated/pyrubberband.pyrb.timemap_stretch.html | official | undated | Python wrapper for the time map |
| https://breakfastquay.com/news/20220707.html | official | 2022-07-07 | R3 better on voices, by its author |
| https://www.media.mit.edu/speech/old/papers/1994/Stifelman_AVIOSJ94_rate_discrimination.pdf | community | 1994, 2007 | Whole-line tempo change noticed at about 5 percent; nothing on local stretch |
| https://arxiv.org/html/2406.19363v1 | community | 2024 | Montreal Forced Aligner beat WhisperX on word edges; numbers unread |
| https://arxiv.org/pdf/2206.03206 | community | 2022 | Warping afterwards did worse than durations set inside the TTS; snippet |

## H. Dubbing and ADR craft

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://tvtechnology.com/opinions/av-synchronization-how-bad-is-bad | official (article summarising ITU-R BT.1359-1) | figures 1951 to 2001 | The tolerance window; film rule of one frame early, two late |
| https://www.forasoft.com/learn/audio-for-video/articles-audio/lip-sync-itu-r-bt-1359-tolerance-windows | community | EBU R37, 2007 | 40 ms early / 60 ms late end to end |
| https://arxiv.org/pdf/2212.01686 | tested | 2022 | Close-up faces are the strictest case |
| https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4117430/ | tested | 2013 to 2014 | Sound late is tolerated more than sound early |
| https://sites.google.com/site/dubbingdoublage/the-dubbing-process/sync-editing | community | undated | Anchor phrase start and end and b/p/m; "the impression of sync"; automatic aligners fail across different rhythms |
| https://ejournals.vdu.lt/index.php/SM/article/download/4767/3034/20682 | community | 2023 | Do not put a new b/p/m under an open mouth |
| https://arxiv.org/abs/2212.12137 | tested | 2022 | 54 professional dubs: natural voice ranked above exact lips; full text unread |
| https://digilib.phil.muni.cz/sites/default/files/pdf/BSE2025-2-4.pdf | community | 2025 | Dubbing fixes sync by rewriting the words |
| https://arxiv.org/pdf/2302.12979 | community | 2023 | Fit the text first; large rate changes distort speech; full text unread |
| https://screens.tv/blog/lip-sync/ | marketing | undated | Vendor rules for m, b, p; "under 30 ms" target, no evidence |

## I. Hiding it in the edit

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://hackernoon.com/ai-dubbing-for-filmmakers-a-checklist-that-turns-one-ai-generated-video-into-ten-languages | community | 2026-08-26 | Off a close-up, plain dubbing is often enough |
| https://invideo.io/faq/why-does-ai-lip-sync-fail-or-drift-on-longer-video-clips/ | marketing | 2026-08-10 | 6 to 7 s ceiling; cut at pauses; reaction shots reset sync |
| https://invideo.io/faq/how-do-you-avoid-the-two-talking-heads-problem-in-ai/ | marketing | 2026-08-01 | Props, over-the-shoulder, reaction shots |
| https://www.atlabs.ai/blog/prompt-guide-for-ai-film-dialogue-scenes-using-180-degree-rule | marketing | 2026-01-16 | Name left and right and whose shoulder in the prompt |
| https://www.imaginary.app/blog/veo-31-dialogue-sfx-prompts-that-actually-sync-a-creator-workflow-for-clean-mout | marketing | 2026-04-30 | Hold on the speaker; narration over other shots |
| https://skywork.ai/blog/how-to-prompt-lip-synced-dialogue-google-veo-3/ | community | 2026 | Three-quarter or profile suggested; unconfirmed |
| https://spotlightfx.com/blog/what-are-j-cuts-and-l-cuts-professional-dialogue-editing-explained | community | 2025-05-12 | J and L cuts; not tied to sync repair |
| https://accenture.thegnomonworkshop.com/tutorials/facial-animation-for-feature-animated-films | community | unknown | Nothing direct on profile staging to save lip sync |
| https://invideo.io/faq/what-is-split-frame-compositing-in-ai-video-editing/ | marketing | 2026 | Two speakers in one composite drift apart |

## J. What working AI filmmakers do

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://curiousrefuge.com/blog/ai-lip-sync-workflows | tested (one clip per test) | 2026-05-11 | Three routes; audio first; Seedance 2.0 with image plus audio; OmniHuman for animation |
| https://curiousrefuge.com/blog/ai-lip-syncing-tutorial | tested | September, year not stated | Voice first plus HeyGen; dropped frames |
| https://sync.so/blog/kling-lip-sync | marketing | 2026-07-07 | sync-3 runs on any model's video |
| https://elevenlabs.io/nl/blog/how-to-bring-veo-2-videos-to-life-with-elevenlabs-voiceovers-and-sound-effects | marketing | 2025-05-07, updated 2026-10-08 | 12 to 15 words per 5 s; narration only, no lip step |
| https://dev.to/akaranjkar08/veo-31-developer-guide-timestamp-prompting-multi-shot-video-and-full-api-june-2026-3l5i | community | 2026-06-05 | End-frame tighter on 4 s clips; no dialogue timing control |
| https://www.veo3gen.app/blog/veo-31-dialogue-sfx-prompts-that-actually-sync-a-creator-workflow-for-clean-mout | community | 2025 to 2026 | One speaker, one short line; snippets |
| https://vizard.ai/blog/veo-3-1-flow-review-2025-what-it-is-how-to-access-it-key-features-use-cases-limits-verdict | community | 2025-10-16 | No uploaded voice in Flow |
| https://kling.ai/blog/best-lip-sync-video-ai | marketing | 2026 | Kling lip sync on an existing clip |
| https://maikbelieve-landing.pages.dev/blog/ai-lip-sync-workflow | marketing | 2026 | Script, voice, picture, mouth pass; snippet only |
| (no page) | guess | 2026-11 search | No first-hand Reddit, X or festival-maker account could be retrieved |

## K. Measuring sync

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://github.com/joonson/syncnet_python | official | undated | SyncNet: offset, distance, confidence; MIT; runs on a CPU |
| https://arxiv.org/pdf/2008.10010 | official | 2020 | Where the two standard lip-sync scores come from |
| https://arxiv.org/pdf/2505.11391 | community | 2025-05 | Those scores match human judgement poorly; snippet |
| https://arxiv.org/abs/2610.09223 | official | 2026-10 | PVSync: far closer to human ranking; code not released |
| https://github.com/guankaisi/FATE | official | 2026-08 | Frame-level score; no clear command, no licence |
| https://github.com/v-iashin/Synchformer | official | 2024, read 2026-11 | Steps of about 0.2 s; too coarse |
| https://github.com/mpc001/auto_avsr | official | read 2026-11 | Lip reading at about 20 percent word errors; no word times |
| https://arxiv.org/abs/2511.08613 | official | 2025-11, v2 2026-02 | Test a score with the wrong audio as a control |
| https://arxiv.org/abs/2511.04520 | official | 2025-11 | A talking-head test suite; details not visible |
| https://montreal-forced-aligner.readthedocs.io/en/latest/ | official | 2026-11 | The standard forced aligner; formats not confirmed |

## L. Making the picture to the voice inside Flow

| Source | Grade | Date | What it gave |
| --- | --- | --- | --- |
| https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1 | official | undated | Timestamps for shots and sound effects only |
| https://morphic.com/resources/how-to/gemini-omni-flash-1-2-guide | community | 2026-11 | Timecodes are "budgets"; event cues land better; no test shown |
| https://help.scenario.com/articles/5851558176-the-gemini-omni-family-the-essentials | community | 2026 | No audio input on any Omni model |
| https://docs.comfy.org/zh/tutorials/partner-nodes/google/gemini-omni-flash-1-2.md | official | 2026-11 | Audio is output only; extend limits |
| https://aistudio.google.com/docs/video | official | 2026-10-22 | Veo 3.1 Preview shut down; no audio input |
| https://ndurner.substack.com/p/google-veo-31 | tested | 2025-10-26 | No consistency between runs, even with a fixed seed |
| https://www.imaginary.app/blog/veo-31-dialogue-sfx-prompts-that-actually-sync-a-creator-workflow-for-clean-mout | marketing | 2026 | Pause tokens asserted, never measured |
| https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3 | marketing | 2026 | "80 percent", "under 120 ms" figures; unverified, sources disagree |
| https://arxiv.org/abs/2605.12179 | official | 2026-05-12 | Sync in joint audio-video models is being fixed in training, not by prompts |
| https://arxiv.org/pdf/2403.06421 | official | undated | The standard scores shift with audio encoding; keep preprocessing identical |
| https://www.arxiv.org/pdf/2512.09299 | community | undated | A benchmark that includes Veo 3; not opened |
| https://arxiv.org/pdf/2508.18621 | official | 2026 | Wan-S2V claims better sync than OmniHuman (paper's own claim) |
