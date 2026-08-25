# Sound and delivery: the narrator's voice against music and silence

## What this covers

How a narrated piece is paced in the ear: words per minute, pause length and placement, when music recedes under a voice and when it's allowed to compete or lead, and how a performance — human or synthetic — communicates a fixed character (sarcastic, authoritative, secretly caring) through delivery rather than words alone. Also covers resting narration on a 170–180 BPM drum & bass bed, and TTS markup (SSML-style tags, stability/style sliders) as a way to direct a generated voice like a human performer. Leaves alone: what the words say (voice/register, sibling briefs), scene structure and beat mapping, and the comic's visual grammar. This is the sound channel only — what happens between the words, and under them.

## Top findings

1. **Silence is a budgeted, scarce resource.** Walter Murch uses full silence only "three or four times in every film" because "I can't use it more often or it would become predictable," reserved for where "I want the audience to use their own sonic imagination" (filmsound.org, Murch interview). A true pause-to-black should be rationed across a whole script, not sprinkled at every clause break.
2. **Sound can lead the picture, not just follow it.** Murch pulled the sound of spinning tape into an elevator scene in *The Conversation* before the cut to its visual source — "we do not yet know what sound it is" when it starts. A line of VO or a music sting arriving a beat before the panel it belongs to does anticipation work a hard sync cannot.
3. **Cut points breathe: hold ~30% longer at a transition than mid-scene.** Murch: the outgoing shot "is held 30% longer than it would if it were a cut within the body of the scene… like in music, where the rhythm usually slows down a bit before we go into the next movement." A narration line that closes a scene should decay, not clip straight into the next beat.
4. **Fight the "100% theory."** Randy Thom's name for every department (dialogue, music, effects) assuming it must fill every moment, producing "a logjam of uncoordinated visual and aural product, each craft competing for attention." The fix is explicit space allocation — "in certain areas the track was going to be driven by the music, in other areas by effects" — never all three at once (filmsound.org).
5. **Loud, at length, reads as empty.** Thom: constant intensity is "a newspaper… printed entirely in capital letters," and "great roller coaster rides last a few minutes (not thirty), and set up each fast moment with a slow one." Direct answer to how a sarcastic narrator sits on a relentless 170 BPM bed: the bed cannot run hot throughout — it needs its own slow sections for the voice to occupy.
6. **A performance can be "bad at the register" and still work, if consistent.** Ira Glass on his own voice: "I don't have a good radio voice. But this thing happens now… that's the force of repetition" (Wikipedia). Familiarity, not vocal beauty, builds trust — a synthetic narrator doesn't need to sound conventionally good, just consistently itself.
7. **Structure by pulling back to a bigger thought, then returning.** Glass learned this editing *All Things Considered* with Noah Adams: "step back from the action and move to some bigger thought and then return to the plot." A pacing device as much as a writing one — mark the beat where register shifts from event to commentary and back.
8. **Audio-only writing puts the entire load on the words.** Tim Crook's *Radio Drama: Theory and Practice*, on the medium being "auditory in the physical dimension but equally powerful as a visual force in the psychological dimension" — with the corollary that "bad lines cannot be obscured with stagecraft" (Wikipedia, quoting Crook). A narrated video built mostly on stills carries proportionally more weight in the script than live-action does.
9. **Flat, protocol-style delivery reads as more menacing/funnier than emotive, and its cracks are where humanity shows.** Ellen McLain built GLaDOS by first imitating a synthesised reference voice Valve played her, run through further modulation — warmth deliberately withheld until specific beats (a "turret voice" repurposed for her breakdown, per Erik Wolpaw) let something human leak through. Kim Swift called McLain "super likable," and writers banked that likeability *underneath* the cold delivery, not instead of it (Wikipedia, GLaDOS) — exactly BadCode's "nurturing underneath the snark."
10. **TTS is now directable with a director's vocabulary, typed instead of spoken.** ElevenLabs v3 reads inline bracketed cues (`[whispers]`, `[sarcastic]`, `[laughs]`) plus punctuation-as-pacing (capitals for emphasis, ellipses for weight), with a stability slider trading expressiveness against reliability. Google Cloud TTS instead offers literal `<break time="750ms"/>` and `<prosody rate="slow" pitch="+2st">` tags plus named styles (calm, firm, lively) on specific voices.
11. **Audiobook narration has a borrowable industry pace.** ACX: "most performers narrate about 9,300 words per hour" — roughly 155 WPM, ~2.6 words/second. A narrator built to sound unhurried and authoritative should sit noticeably under that, not at or above it.
12. **Drum & bass already answers where a narrator's voice belongs on its own bed.** Wikipedia: "old-school DnB usually included an MC providing vocals" but "this practice has declined"; structurally, the drop is "the point in a track where a switch of rhythm or bassline occurs and usually follows a recognisable build section and breakdown," where drums thin out and other elements carry the track. The genre's own grammar puts a voice in the breakdown, not fighting the drop.

## The techniques in detail

### Sound leading picture, and the 30% hold

**What it is.** Two Murch principles: a sound can be introduced before its visual source appears, priming the ear ahead of the eye; and at a transition, the outgoing shot/sound is held roughly a third longer than an internal cut would need, "like in music, where the rhythm usually slows down a bit before the next movement."

**Why it works.** Both manage anticipation. An unexplained sound creates a question the mind wants answered — a stronger hook than sound the eye has already accounted for. The extended hold gives the audience a moment to finish processing before a new beat starts; cutting exactly on the dramatic beat with no decay reads as abrupt, not punchy.

**Worked example.** Murch brings tape-spinning sound into *The Conversation*'s elevator scene ahead of the cut that explains it.

**Failure mode.** Done every time, sound-leads-picture trains the audience to expect it and stops working — the same "predictability" problem Murch names for silence itself.

### The "100% theory" and deliberate space allocation

**What it is.** Thom's name for every sonic department filling every moment on the assumption more layers equal more impact.

**Why it works.** Three departments fighting for one moment produces "a logjam… each craft competing for attention." The alternative: an explicit carve-up where "in certain areas the track was going to be driven by the music, in other areas by effects" — one element leads at a time, by design.

**Worked example.** Thom, on Zemeckis: "one of the few directors out there who doesn't think you have to fire every one of your guns simultaneously to make an action sequence work."

**Failure mode.** The mirror failure: a script that never lets music or effects carry anything, so narration runs wall-to-wall — words playing the exact role Thom is criticising sound effects for.

### Loudness/intensity as a pacing problem, not a volume problem

**What it is.** Thom's argument that audiences want contrast, not unbroken intensity: "peak levels, per se, are not the issue. Sustained, prolonged, unrelentingly high average levels are the issue."

**Why it works.** Contrast is what makes a peak a peak. His analogy: text in all-capitals stops reading as emphatic and starts reading as noise — the same logic applies to a bed that never breaks stride, leaving the drop nothing to punctuate.

**Worked example.** "Great roller coaster rides last a few minutes (not thirty), and set up each fast moment with a slow one."

**Failure mode.** Read as "make it quieter" rather than "make it vary" — Thom is explicit that levels aren't the issue, sustained intensity is. A quiet track that never varies is as flat as a loud one.

### The flat/synthetic register as a performance choice (GLaDOS)

**What it is.** McLain's approach: imitate a synthesised reference voice, deliver it flat, let processing push it further from natural speech, with narrative beats allowed to break the flatness.

**Why it works.** A cold, procedural delivery reading cruel or threatening content is where both comedy and menace live — content and tone mismatched. McLain's underlying likeability let the writers spend warmth sparingly rather than perform it on the surface.

**Worked example.** Wolpaw describes GLaDOS's voice evolving as her "morality core" is removed — moving toward something more human, using a "sultry" register originally written for turrets, repurposed for her breakdown scene.

**Failure mode.** A narrator performed as only flat, with no planned crack, is a gimmick with nowhere to go — the technique depends on a reserved place to spend the human moment.

### TTS direction: markup as stage direction

**What it is.** Two vocabularies for the same job. Google's SSML: numeric `<break>` tags; `<prosody rate="slow" pitch="+2st">…</prosody>` wrapped around a *full sentence only* (partial-phrase wrapping "may cause unwanted pauses," per Google's own docs); named `<google:style>` deliveries on specific voices. ElevenLabs v3: inline bracketed cues in the script text itself, plus punctuation as delivery, plus a stability slider (creative/natural/robust).

**Why it works.** Both turn a spoken director's note ("hold there," "say that flat") into text the script itself carries, so revisions don't need re-recording from separate notes.

**Worked example.** ElevenLabs dropped SSML breaks in v3 because stacking them "can cause instability" — markup *reliability*, not just expressiveness, is still a live problem.

**Failure mode.** Treating markup as a guarantee: partial-phrase `<prosody>` wrapping misfires per Google's docs; narrative asides like "her voice trembling with sadness" can leak into ElevenLabs' spoken output and need cutting in post.

## Disagreements and caveats

- **What "good narration" sounds like is genuinely contested.** Glass says his own voice isn't suited to radio and that trust comes from repetition, not polish. McLain's GLaDOS deliberately performs *worse* than natural speech as a character choice. ACX's audiobook norms assume trained, smooth, controlled delivery as default professional standard. BadCode's brief sits closer to the McLain end than the ACX end — worth stating so it isn't second-guessed against "proper" pacing norms later.
- **Source strength is uneven.** The Murch and Thom material is genuinely primary — their own essays and an interview, hosted at filmsound.org, with exact quotes; treat these as load-bearing. The Ira Glass, Tim Crook, GLaDOS, Herzog, Adam Curtis and Kurzgesagt material is Wikipedia-grade — real attributed quotes, but secondary compilation, because several intended primary sources (Transom.org's Ira Glass essays, BBC Radio 4/Academy pages, Attack Magazine's/Point Blank's D&B tutorials, Epic Mountain's own account of scoring Kurzgesagt) returned dead links or were unreachable this session; search-engine access was also exhausted early, narrowing discovery to direct URL guesses and Wikipedia.
- **D&B vocal-hosting mechanics, and the natural-history "2–3 words/second" convention, are (unverified) at practitioner-source level.** Wikipedia confirms the MC tradition and drop/breakdown structure exist, but no fetched source gives producer-level detail on laying a half-time vocal over 170 BPM, or names the 2–3 words/second figure directly — the ACX ~2.6 words/second figure is a *different*, verified data point that happens to land nearby, not confirmation of the natural-history number.
- **Kurzgesagt/Epic Mountain's scoring workflow: not found.** Nothing here should be read as describing their process specifically; the Thom "space allocation" principle is the transferable idea, not a claim about their method.

## How this applies to BadCode

1. **Ration true silence to emotional turns, not sentence breaks.** In a ~20-scene GPOM episode, pick 2–3 places (the discovery-timeline pivot, the coda) for a full stop-the-bed silence; everywhere else gets a beat-pause, not dead air.
2. **Reserve a breakdown for every scene where the narrator carries plot; treat the drop as wordless punctuation.** Script narration into half-time/thinned sections; let full-tempo drops land on scene cuts or the visual punchline, VO silent or reduced to one stinger word.
3. **Give the narrator exactly one reserved "crack in the register" per episode, GLaDOS-style.** Keep flat/certain/sarcastic as baseline throughout, per "nurturing underneath the snark" — bank one moment (probably late, echoing the coda) where delivery visibly softens. More than once burns the effect.
4. **Treat ACX's ~155 WPM as a ceiling, not a target.** An authoritative voice with nothing to prove should read closer to 120–140 WPM baseline, with faster passages reserved for urgency — so speed itself signals rising stakes.
5. **Write scenes as radio, because the video is mostly stills.** Crook's "bad lines cannot be obscured with stagecraft" applies directly — the script does work a live-action film would spread across blocking and cutting. Read every draft line aloud, eyes shut, before approving it.
6. **Adopt Glass's "zoom out, then back" as an explicit scene-boundary marker.** Mark beats where the narrator steps from plot to bigger thought and back — natural places to duck the music further and shift register colour (dry aside vs cosmic certainty).
7. **If the narrator is (or becomes) TTS, write inline delivery tags now.** Bracket cues (`[flat]`, `[dry]`, `[warmer]`, `[whispers]`) and punctuation-as-pacing directly in the canon script file, so it's both human-readable and machine-directable without a second pass.
8. **Adopt a house VO markup convention, applied to the next GPOM script:**

   | Mark | Meaning | Use |
   |---|---|---|
   | `/` | Short beat, comma-weight | ~0.2–0.3s, inside a sentence |
   | `//` | Full-stop beat | ~0.5–0.8s, between sentences |
   | `///` | Held pause — earn it | ~1–2s, reserved for a real turn |
   | `[SIL n s]` | True silence, bed and VO both stop | Murch's 3–4-per-film discipline; max 2–3 per episode |
   | `[BREAKDOWN]…[/BREAKDOWN]` | VO sits in a half-time/thinned bed section | Default home for plot-carrying narration |
   | `[DROP]` | Full-tempo hit, wordless (or one word) | Scene-cut punctuation, not exposition |
   | `[DUCK -Xdb]…[/DUCK]` | Music explicitly attenuated under this span | Named level, not "turn it down a bit" |
   | `{FLAT}…{/FLAT}` | Baseline register: certain, dry, administrative | Default narrator voice |
   | `{WARM}…{/WARM}` | The reserved crack — caring shows through | Spend once per episode |
   | `[whispers]` `[sarcastic]` `[laughs]` | Bracketed performance cues (ElevenLabs-style) | Portable straight to TTS |
   | CAPS | Hard emphasis, one word only | Never a whole line (Thom's warning) |

   Reads as a normal script, directs a human VO artist without extra notes, and drops into an SSML/ElevenLabs pipeline unchanged if the narrator is ever synthesised.

## Diagnostic questions

1. Does the script name, per scene, which single element (VO/music/effects) is driving — or are two-plus fighting for the same moment ("100% theory")?
2. Is there a marked `[BREAKDOWN]` for every scene where the narrator delivers plot over the D&B bed, or does VO compete with a full-tempo section?
3. Does every `[DROP]` land wordless or on one word, or is dense narration written straight through a full-tempo hit?
4. How many true `[SIL]` silences are marked across the episode — close to Murch's 2–4, or absent/overused to predictability?
5. Is there exactly one `{WARM}` moment per episode where the flat baseline cracks — not zero, not more than one or two?
6. Read cold, does average pace sit under ~155 WPM, with faster passages clearly signalling urgency rather than accident?
7. At every transition, is the outgoing line given a beat to decay (Murch's ~30% hold), or cut hard on the last word?
8. Does any sound or line arrive *before* its visual referent, priming anticipation — or is everything strictly synced to what's already on screen?
9. With visuals switched off, does the scene still make complete narrative sense (the radio-drama test)?
10. Is the sarcastic/authoritative register consistent enough that a listener could identify the narrator blind?
11. Are CAPS/hard-emphasis marks used on one word only, never stacked across a whole line?
12. If this narrator will ever be TTS-generated, does the script already carry inline delivery tags rather than leaving pacing to be discovered at recording time?
13. Does the script vary intensity across the episode — slow sections clearly set up before fast ones — rather than sustaining one energy level throughout?

## Sources

1. [Randy Thom, "Designing a Movie for Sound"](http://www.filmsound.org/articles/designing_for_sound.htm) — practitioner. The "100% theory," sound shaping picture from pre-production. Load-bearing for finding 4.
2. [Randy Thom, "A Few Notes on Music in the Final Mix"](http://www.filmsound.org/randythom/finalmix.htm) — practitioner. Space-allocation in the mix; the Zemeckis quote.
3. [Randy Thom, "Are Movies Getting Too Loud?"](http://www.filmsound.org/randythom/loud-movies.htm) — practitioner. Loudness vs contrast; "capital letters"/"roller coaster." Load-bearing for finding 5.
4. [Walter Murch, "Stretching Sound to Help the Mind See"](http://www.filmsound.org/murch/stretching.htm) — practitioner. Metaphoric distance between sound/image; the *Godfather III* silent-scream example.
5. [Walter Murch, interview, filmsound.org](http://filmsound.org/murch/interview-with-walter-murch.htm) — practitioner. Sound-leads-picture, the 30% hold, the 3–4-silences rule. Load-bearing for findings 1–3.
6. [Wikipedia, "Walter Murch"](https://en.wikipedia.org/wiki/Walter_Murch) — journalism/reference. *In the Blink of an Eye*, "Rule of Six," editing-as-psychology.
7. [Wikipedia, "Ira Glass"](https://en.wikipedia.org/wiki/Ira_Glass) — journalism/reference, direct quotes. "Force of repetition," Noah Adams structural lesson. Load-bearing for findings 6–7.
8. [Wikipedia, "Radio drama"](https://en.wikipedia.org/wiki/Radio_drama) — journalism/reference, quoting Tim Crook directly. Load-bearing for finding 8.
9. [Wikipedia, "GLaDOS"](https://en.wikipedia.org/wiki/GLaDOS) — journalism/reference, quotes from McLain, Swift, Wolpaw. Load-bearing for finding 9.
10. [Wikipedia, "Werner Herzog"](https://en.wikipedia.org/wiki/Werner_Herzog) — journalism/reference, thin. Confirms deadpan self-narration and "ecstatic truth"; no direct performance-technique quote found.
11. [Wikipedia, "Adam Curtis"](https://en.wikipedia.org/wiki/Adam_Curtis) — journalism/reference, thin. "Patrician economy and assertion"; reason for found-music scores over an original one.
12. [Wikipedia, "Drum and bass"](https://en.wikipedia.org/wiki/Drum_and_bass) — journalism/reference. Tempo range, drop/breakdown definition, MC tradition's decline. Load-bearing for finding 12.
13. [Google Cloud Text-to-Speech, SSML docs](https://docs.cloud.google.com/text-to-speech/docs/ssml) — official documentation. Break/prosody/style tag syntax and constraints.
14. [ElevenLabs, prompting/controls docs](https://elevenlabs.io/docs/best-practices/prompting/controls) — official documentation. Bracketed cues, punctuation-as-pacing, stability slider. Load-bearing for finding 10.
15. [ACX Help, "Producing and Recording Your Audiobook"](https://help.acx.com/s/article/producing-and-recording-your-audiobook) — official industry guidance. ~9,300 words/hour benchmark. Load-bearing for finding 11.
16. [Wikipedia, "Kurzgesagt"](https://en.wikipedia.org/wiki/Kurzgesagt) — journalism/reference, thin. Confirms narrator name and visual style only; no scoring-process detail found.
