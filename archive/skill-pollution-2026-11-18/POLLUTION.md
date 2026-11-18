# Skill pollution archive (2026-11-18)

Jack, 2026-11-18: "put all the pollution in a file called archive, just so we can save all the old shit and go
through it if we need it."

What was removed: story-specific material inside `.claude/skills/` — a story's name tied to its look, sound,
voice, genre or instruments, and "worked example" links into one story's folder. Skill descriptions load into
every session, so story names there were the worst case. `CLAUDE.md` and `.claude/agents/` were checked and were
clean (`scripts/style-lint.py` also passes, but it lets any line that names a story through by design).

- `<skill>/SKILL.md` in this folder: the skill exactly as it was before the clean-up (commit a7af6256).
- Below: each passage taken out, by skill, with what replaced it.

## drive-sync

- **Line 3**, original:

> Triggers on "here's where my karen story lives", "my <story> is in <folder>", "my Karen music folder is …", "push karen music", "pull the camping story",

  → replaced with: Triggers on "here's where my <story> lives", "my <story> is in <folder>", "my <story> music folder is …", "push <story> music", "pull the <story> story",

- **Line 41**, original:

> ("my Karen story is in
> C:\Users\jackt\OneDrive\Desktop\Youtube Vids\Karen", "Camping music lives in /mnt/c/.../camping")

  → replaced with: ("my <story> story is in C:\Users\...\Youtube Vids\<story>", "<story> music lives in /mnt/c/.../<story>")

- **Line 43**, original:

> If it could be two (Karen Music or Karen Story), ask.

  → replaced with: If it could be two (a story's Music and Story folders), ask.

- **Line 59**, original:

> such as `bank-robbery-music`

  → replaced with: such as `<story>-music`

- **Line 61**, original:

> "Karen" alone is ambiguous: ask whether it's Karen Music or Karen Story.

  → replaced with: A bare story name is ambiguous when it has both a Music and a Story folder: ask which.


## flow-automation

- **Line 229**, original:

> it broke the Bank Robbery gang run on 2026-11-17)

  → replaced with: it broke a story's run on 2026-11-17)

- **Line 248**, original:

> corrected by Jack 2026-09-28 during the Camping mv2 run, and a 10 s reload-retry was enough there.

  → replaced with: corrected by Jack 2026-09-28 during a 26-clip run, and a 10 s reload-retry was enough there.

- **Line 512**, original:

> Render it with ffmpeg. Worked example:
> `docs/stories/gitpush-origin-master/storyboard/img/s00-pullback-post-12s.mp4` — 12s at 1080p,
> after Veo failed at it four times.

  → replaced with: Render it with ffmpeg. One 12 s pull-back was made this way at 1080p, after Veo failed at it four times.

- **Line 641**, original:

> Worked example — GPOM's project is `/mnt/d/badcode-videos/gitpush-origin-master/gpom-story.prproj`,
> so the plant-room scratch is `/mnt/d/badcode-videos/gitpush-origin-master/clips/plant-room/`, and
> the bulletin's is `.../clips/bulletin/`.

  → replaced with: Example: a project at `/mnt/d/badcode-videos/<story>/<story>.prproj` puts a scene's scratch in `/mnt/d/badcode-videos/<story>/clips/<scene>/`.

- **Line 644**, original:

> anything still pointing at `~/Desktop/gpom-*`
> is stale.

  → replaced with: anything still pointing at the Desktop is stale.

- **Line 698**, original:

> > ✅ **BUILT 2026-08-21** as [`scenes/s00-awakening.md`](../../../docs/stories/gitpush-origin-master/scenes/s00-awakening.md).
> > Diverged from this board: no descent, no Dubai, no lens flare — the cut ends on Earth from orbit.

  → replaced with: > ✅ **BUILT <date>** as [`scenes/<scene>.md`](<link to the scene's record>). > Diverged from this board: <what the shoot dropped or changed, in one line>.


### flow-automation: second pass (GPOM)

- **Line 93**, original:

> Veo can only make it worse — GPOM scene 0 burned

  → replaced with: Veo can only make it worse — one scene burned

- **Line 299**, original:

> Measured on GPOM scene 0: dropping

  → replaced with: Measured on one scene: dropping

- **Line 715**, original:

> ruled GPOM scenes 1–4 "not a Flow job"

  → replaced with: ruled four scenes "not a Flow job"

- **Line 717**, original:

> Nano Banana Pro rendered `git push origin master` on a CRT correctly

  → replaced with: Nano Banana Pro rendered a short line of code on a screen correctly


## flow-prompt

- **Line 78**, original:

>  Bank Robbery's answer to the muted default (saturated colour per
> place, two lights of different colours) is that story's rule, not a default for every prompt.

  → `deleted`


## lip-sync-dub

- **L3** ` in a narrated film (Karen, The Bank Robbery, Money For Something).` → ` in a narrated film.`
- **L8** `Built on 2026-10-19 from The Bank Robbery` → `Built on 2026-10-19 from two past films'`
- **L9** `cut 7c and the Karen ending (10b2), after three rounds Jack rejected.` → `dubbed scenes, after three rounds Jack rejected.`
- **L11** deleted:
  > Worked records: `docs/stories/bank-robbery/short-shots.md` § "Cut 7c" and `docs/stories/karen/shot-list.md` § Premiere updates.
- **L17** `(Karen 10b2: its audio said` → `(one past film, 2026-10: its audio said`
- **L58** `(`Ay-Eye Sean`, not `A.I. Sean`, which made a 1.2 s pause).` → `(spell out an initialism phonetically: `A.I.` written with full stops made a 1.2 s pause).`
- **L61** `(Karen 10f: three clips, 11 / 15 / 5 words,` → `(one past film: three clips, 11 / 15 / 5 words,`
- **L63** `plus `The phone stays pressed to his ear the whole time` or whatever must not` → `plus a line holding whatever must not`
- **L82** `on Karen review 10:` → `on one past film's review:`
- **L88** `(Bank Robbery 7f, 0:57: "The` → `(one past film, 2026-10-21: the`
- **L89** `distraction" over 0.6 s of still grin)` → `first phrase over 0.6 s of still grin)`
- **L99** `mouth burst: "Karen, is that you?", "I have an urgent message for you." …` → `mouth burst: `<phrase 1>`, `<phrase 2>` …`
- **L104** `# example: scripts/lipsync/example-karen-10b2-ending.json` → `# a past phrase table sits in scripts/lipsync/ as example-*.json`
- **L108** `(**cap 1.15 on a breathy or whispered voice**: Tarquin warbled at 1.17–1.30)` → `(**cap 1.15 on a breathy or whispered voice**: one warbled at 1.17–1.30)`
- **L114** `(Karen review 8:` → `(one past review:`
- **L115** `"Tarquin's clip is weird":` → `"<character>'s clip is weird":`
- **L117** `That fixed Karen 10f where everything else failed.` → `That fixed one past film's line where everything else failed.`
- **L141** `Jack: "take away the clip you put over tarquin": he wants the face.` → `Jack: "take away the clip you put over <character>": he wants the face.`
- **L142** `"are you even there?" 0.45 s early, "I have seen" 0.34 s early;` → `two phrases 0.45 s and 0.34 s early;`
- **L144** `(GPOM cut 3, 2026-10-20) | Sandra's face left` → `(one past film, 2026-10-20) | The face left`
- **L145** `(the old lady, 17-6)` → `(one past film)`
- **L145** `Same as Karen 10f:` → `Same as another film's fix:`
- **L146** `(Bank Robbery 7e, 2026-10-21)` → `(one past film, 2026-10-21)`
- **L147** `(7e)` → deleted
- **L148** `(7f)` → deleted
- **L149** `(7f)` → deleted
- **L150** `(Bank Robbery 7f, 2026-10-21)` → `(one past film, 2026-10-21)`
- **L150** `"The distraction" played` → `the first phrase played`
- **L150** `closures matched (7g).` → `closures matched.`
- **L151** `A talking close-up of Mr Red (Frames, Omni, 2026-10-21)` → `A talking close-up of one character (Frames, Omni, 2026-10-21)`
- **L152** `(Bank Robbery colour noir, 2026-10-30)` → `(a music video, 2026-10-30)`
- **L153** `(GPOM bridge r2, 2026-11-04) | The old lady 1.7 s late, Sandra 0.9 s early;` → `(one past film, 2026-11-04) | One speaker 1.7 s late, another 0.9 s early;`
- **L153** `Half of the old lady's lag` → `Half of the first speaker's lag`
- **L154** `Sped a Scouse "Sandra!" to x1.07` → `Sped a one-word name call in a regional accent to x1.07`
- **L154** `whisper heard "sundry".` → `whisper heard a different word.`
- **L155** `(GPOM bridge r6, 2026-11-04)` → `(one past film, 2026-11-04)`
- **L155** `labelled as the Derek clip` → `labelled as another character's clip`
- **L156** `Cut Sandra's line` → `Cut one line`
- **L156** `(GPOM bridge r7, 2026-11-04)` → `(one past film, 2026-11-04)`
- **L157** `(GPOM scene A round 18, 2026-11-05)` → `(one past film, round 18, 2026-11-05)`
- **L159** `(GPOM scene A, 2026-11-06,` → `(one past film, 2026-11-06,`
- **L160** `(Priority Lane minister, 2026-11-11)` → `(one past short, 2026-11-11)`
- **L160** `garbled "hors d'oeuvres" into "or doves";` → `garbled a two-word French phrase into nonsense;`
- **L161** `(Infinite Yous, 2026-11-15)` → `(one past short, 2026-11-15)`
- **L173** `The Karen 10b2 one-off that led here` → `The one-off that led here`
- **L111-112** `which happened on "we do not take / action": every TTS read` → `e.g. one three-word phrase: every TTS read`
- **L119-120** `(Karen: 2 s of the President listening; Bank Robbery: café / pans)` → `(e.g. 2 s of the listener, or a slow pan across the room)`

Original of every line: `archive/skill-pollution-2026-11-18/lip-sync-dub/SKILL.md`.


### new-idea: second pass (GPOM)

- **Line 92**, original:

> (`docs/stories/`) or the GPOM arc?

  → replaced with: (`docs/stories/`) or the shared storyverse (`docs/stories/storyverse/`)?


## new-image

- **Line 17**, original:

> some stories want a full paragraph, Bank Robbery's wants it halved)

  → replaced with: some stories want a full paragraph, some want it halved)

- **Line 56**, original:

> The two registers this skill used to hold are now in GPOM's `look.md`, word for word. Camping's look grew out of the PEOPLE one and is
> stated in its own `look.md`; Karen, Bank Robbery and Magic Money Tree each have their own. Don't use one
> story's look for another unless its `look.md` says so.

  → replaced with: Every look lives in its own story's `badcode.md` (the long record in its `look.md`); the library of looks is `docs/library/`. Don't use one story's look for another unless its `badcode.md` says so.

- **Line 85**, original:

> (the 2026-07-25 camping recut produced a third Tarquin)

  → replaced with: (a 2026-07-25 recut produced a third different face for one character)


### new-image: second pass (GPOM)

- **Line 33**, original:

>  (GPOM's does: one bright anchor in the dark, a visible cost in any monumental frame)

  → `deleted`

- **Line 69**, original:

> like GPOM's kill-bot POV,

  → replaced with: like a character's point of view,


## new-scene

- **Line 73**, original:

> "story": "gitpush-origin-master", "scene": "the-vault", "prefix": "vt",
>   "title": "GPOM The Vault",
>   "heading": "GitPush Origin Master <span class=\"tri\">▲</span> the vault",

  → replaced with: "story": "<story>", "scene": "<scene>", "prefix": "<2 letters>",   "title": "<Story> <Scene>",   "heading": "<Story> <span class=\"tri\">▲</span> <scene>",

- **Line 78**, original:

> "media": "/mnt/d/badcode-videos/gitpush-origin-master/clips/the-vault",

  → replaced with: "media": "/mnt/d/badcode-videos/<story>/clips/<scene>",

- **Line 80**, original:

> "beats": [{"key": "door", "at": "0:00", "name": "The door", "blurb": "What this beat must do."}],
>   "existing": {"door": [["NOW-door", "On the timeline now (replace)", "moodboard/current/NOW-door.jpg"]]},

  → replaced with: "beats": [{"key": "<beat>", "at": "0:00", "name": "<Beat name>", "blurb": "What this beat must do."}],   "existing": {"<beat>": [["NOW-<beat>", "On the timeline now (replace)", "moodboard/current/NOW-<beat>.jpg"]]},

- **Line 106**, original:

> Worked examples, built before the tools were generalised: the GPOM opening recut
> (`scripts/gpom/build-opening-*.py`, `scripts/gpom/opening-video/`,
> `docs/stories/gitpush-origin-master/scenes/opening-recut-*`) and the second half
> (`scripts/gpom/second-half-video/`).

  → replaced with: Older one-off builders from before the tools were generalised live in `scripts/gpom/` (code only; their looks belong to that story).


### new-scene: second pass (GPOM)

- **Line 13**, original:

> This is the loop that made the GPOM
> opening recut, the second half, the gaze sequence and the ending.

  → replaced with: This loop has made a whole film's scenes, from the opening to the ending.


## new-short

- **Line 3**, original:

> or any short named on the list (Priority Lane, The Rules, Howard Street…).

  → replaced with: or any short named on the list.

- **Line 77**, original:

> The model is
>   The Rules' https://claude.ai/artifact/GE8koyRsGnm3m3fNiVJTYY.

  → replaced with: The first one   (layout only): https://claude.ai/artifact/GE8koyRsGnm3m3fNiVJTYY.

- **Line 79**, original:

> - **Balaclava gang in motion:** Omni redraws the masks every frame, and the triangles vanish when heads turn
>   (The Rules, 2026-11-11). Write "every mask keeps facing the camera" into the motion prompt, then check the
>   masks zoomed in at three points in each clip.
> 

  → `deleted`

- **Line 93**, original:

> (The Rules, 2026-11-11; model: `docs/stories/short-the-rules/README.md` § "Jack: pulling it")

  → replaced with: (2026-11-11; first done in `docs/stories/short-the-rules/README.md` § "Jack: pulling it")

  (moved, not deleted: now in `docs/library/tricks/README.md`, the balaclava row)

## new-slideshow

- **Line 18**, original:

> First made for Future Proof's launch talk
> (`docs/stories/future-proof/slideshows/launch-talk/`), which is the worked example for every stage
> below.

  → replaced with: The first deck made this way is in `docs/stories/future-proof/slideshows/launch-talk/`: use it for the folder shape and the tools only; its look, jokes and characters are that story's own.

- **Line 65**, original:

>  One recurring invented character (Future Proof: Mel) is the one who noticed, never the fool.

  → replaced with:  One recurring invented character is the one who noticed, never the fool.

- **Line 75**, original:

>  Future Proof's options: Museum of Old Tech / **Update Available** (picked) / Bundle Deal / Building Site.

  → `deleted`

- **Line 77**, original:

>  (same link every round; Future Proof's: https://claude.ai/artifact/LNreQcESnsdmBZD1HVEaCB)

  → replaced with:  (same link every round)

- **Line 78**, original:

>  (Future Proof's: one running installer gag, a character's day, ruthless minimum, stand-up set, patch notes, the support call)

  → `deleted`

- **Line 78**, original:

> Round 1→2 of Future Proof went 8:41 → 3:17 this way.

  → replaced with: One deck's round 1→2 went 8:41 → 3:17 this way.


## new-story

- **Line 3**, original:

> write the canon for <story>", or working on camping / Karen Will Lead the Revolution / The Magic Money Tree / GitPush Origin Master.

  → replaced with: write the canon for <story>", or developing any story under docs/stories/.

- **Line 35**, original:

> - For canon-linked stories, skim `docs/stories/gitpush-origin-master/README.md` to stay
>   consistent with the arc.

  → replaced with: - If the story belongs to the shared storyverse, skim `docs/stories/storyverse/` to stay   consistent with it.

- **Line 60**, original:

> `docs/stories/camping/` is the worked reference — match its shape.

  → replaced with: `docs/stories/badcode-template.md` is the shape of the `badcode.md` at the top.


### new-story: second pass (GPOM)

- **Line 13**, original:

> an existing comic, a GPOM beat — and

  → replaced with: an existing comic, a beat from another story — and

- **Line 68**, original:

> existing comic, or GPOM beat.

  → replaced with: existing comic, or a beat from another story.

- **Line 103**, original:

>  Worked example: GPOM.

  → `deleted`


## premiere-automation

- **Line 293**, original:

> premiere_open_project({ story: "camping" })                          # <mediaRoot>\camping\camping.prproj

  → replaced with: premiere_open_project({ story: "<story>" })                          # <mediaRoot>\<story>\<story>.prproj


### premiere-automation: second pass (GPOM)

- **Line 186**, original:

> GPOM's are `01-s00-orbital` … `06-vantage` (209 clips, imported 2026-08-26).

  → replaced with: For example `01-<cut-id>` … `06-<cut-id>`.


## scene-animation

- **Line 50**, original:

> (the Karen river
> drop)

  → replaced with: (a river drop)


### scene-animation: second pass (GPOM)

- **Line 46**, original:

>  (GPOM's examples: the machine that doesn't care, the wealth piling while the room dims)

  → `deleted`

- **Line 82**, original:

> which is proven across every GPOM clip.

  → replaced with: which is proven across a whole film's clips.



### scene-beats: second pass (GPOM)

- **Line 34**, original:

> Kai's best notes have come from contrast (on GPOM: "zoomed out, a vast parade ground", "a strobe, not a glow", "from outside, through the corner windows").

  → replaced with: Kai's best notes have come from contrast: a change of scale, of light, or of where the camera stands.



### scene-dialogue: second pass (GPOM)

- **Line 12**, original:

> (GPOM's intro and doorstep)

  → replaced with: (one film's intro and doorstep)

- **Line 21**, original:

> (GPOM: a 55 s intro cut to under 20 s)

  → replaced with: (one film: a 55 s intro cut to under 20 s)

- **Line 30**, original:

> | What | Example (GPOM, 26 Oct) |

  → replaced with: | What | What to fill in |

- **Line 32**, original:

> | **Which dialogues** (one or several; one page covers them all) | Maddie's intro (scene A beat 0), the doorstep (scene B) |

  → replaced with: | **Which dialogues** (one or several; one page covers them all) | <speech> (scene, beat) |

- **Line 33**, original:

> | **Target length** each | 20 s or less · about 60 s |

  → replaced with: | **Target length** each | <seconds> |

- **Line 34**, original:

> | **What each must still do** (the plants and payoffs) | she's friendly; he misses us; his worlds failed for want of consciousness; the patrol is out |

  → replaced with: | **What each must still do** (the plants and payoffs) | <each plant or payoff, in a few words> |

- **Line 35**, original:

> | **Protected lines**: Kai's words, kept verbatim if at all possible | "It runs on... well... you." |

  → replaced with: | **Protected lines**: Kai's words, kept verbatim if at all possible | <the lines, quoted> |

- **Line 36**, original:

> | **Rules** | no stated moral; Maddie stays warm and West Country; the lady stays stern; the vote is off screen |

  → replaced with: | **Rules** | <from the story's `badcode.md`: how each character must stay, what stays off screen> |

- **Line 37**, original:

> | **What's in the cut now**, and where it lives | `voice3.py` `MADDIE`; `second-half-b-the-door/script.json` |

  → replaced with: | **What's in the cut now**, and where it lives | <the voice script or `script.json` path> |

- **Line 56**, original:

> (GPOM's shape 07 did)

  → replaced with: (it has happened)

- **Line 109**, original:

> (GPOM: `voice3.py`)

  → `deleted`

- **Line 117**, original:

> GPOM, 26–27 Oct: `design/

  → replaced with: The first run, 26–27 Oct (mechanics only, its words are that story's): `design/


## scene-images

- **Line 69**, original:

> Priority Lane rounds 8-17 lost a round to every one of these.

  → replaced with: One short's rounds 8-17 lost a round to every one of these.



### scene-timeline: second pass (GPOM)

- **Line 130**, original:

> "sequence": "gpom-sh-B-rough1", "guid": "…", "bin": "gpom-sh-B-rough1"

  → replaced with: "sequence": "<story>-<part>-rough1", "guid": "…", "bin": "<story>-<part>-rough1"

- **Line 131**, original:

> "project": "/mnt/d/…/gpom-story.prproj"

  → replaced with: "project": "/mnt/d/…/<story>.prproj"

- **Line 132**, original:

> "sequence": "gpom-sh-B-rough2", "guid": "…", "bin": "gpom-sh-B-rough2"

  → replaced with: "sequence": "<story>-<part>-rough2", "guid": "…", "bin": "<story>-<part>-rough2"

- **Line 169**, original:

> e.g. `gpom-2-A-killbots-r1`, `gpom-3-B-door-r2`.

  → replaced with: e.g. `<story>-2-A-<name>-r1`, `<story>-3-B-<name>-r2`.

- **Line 170**, original:

> (`gpom-1-track-and-off-switch`)

  → replaced with: (`<story>-1-<name>`)



### shot-craft: second pass (GPOM)

- **Line 195**, original:

> the GPOM
>   `vantage` discovery

  → replaced with: one film's   `vantage` discovery


## story-craft

- **Line 120**, original:

> (the existing convention —
> [`docs/stories/gitpush-origin-master/critique-pass-2.md`](../../../docs/stories/gitpush-origin-master/critique-pass-2.md)
> is the worked reference)

  → replaced with: (the existing convention)

- **Line 137**, original:

> - **Respect the canon's own rules.** GPOM's nine binding accuracy rules, the unpersonified-AI rule,
>   the metaphor budget and the Storyverse discipline are constraints on every suggestion, not
>   targets for one.

  → replaced with: - **Respect the canon's own rules.** Whatever binding rules the story's `badcode.md` (and the storyverse, if it   belongs to it) sets are constraints on every suggestion, not targets for one.


## story-style

- **Line 13**, original:

> one story's
> dark register and drum & bass became every story's, and 400+ Bank Robbery takes came out in one
> voice.

  → replaced with: one story's look and genre became every story's, and 400+ takes of one song came out in one voice.


## suno-automation

- **line 3**

> "put this in the gpom-story workspace"

  → "put this in the story's workspace"

- **line 69**

> (Camping r54), custom Duration included

  → (one story's round), custom Duration included

- **line 109**

> a GPOM narration session and a Camping session ran
> simultaneously. The GPOM session read `status`, found a Camping cover loaded (`camping-duet`,
> take c3), and loaded over it.

  → two sessions working on two different stories ran simultaneously. One read `status`, found the other's cover loaded, and loaded over it.

- **line 127**

> docs/stories/gitpush-origin-master/songs/narration.md '`gpom-datacentre` — ' > /tmp/spec.json

  → docs/stories/<story>/songs/<sheet>.md '`<cue-id>` — ' > /tmp/spec.json

- **line 145**

> npx tsx scripts/suno/suno.mts takes gpom-cut1
> 

  → npx tsx scripts/suno/suno.mts takes <story>-<cut> 

- **line 173**

> GPOM's narration taste profile sat in My Taste under **fourteen**
> Camping cover rounds and a scouting set, demanding *one voice* for a two-man duet and *almost no
> music* for a drum-and-bass track.

  → one story's narration taste profile sat in My Taste under **fourteen** rounds of a different story's song and a scouting set, demanding *one voice* for a two-voice duet and *almost no music* for a full-band track.

- **line 209**

> *(Camping's sweep: 644 chars / 78% shared at g1

  → *(One sweep, 2026-09: 644 chars / 78% shared at g1

- **line 213**

> the brief actually names (Camping's brief named its drum foundation; another story's names its own,
> or none).

  → the brief actually names (one brief named its drum foundation; another story's names its own, or none).

- **line 222**

> Camping g1 said *"barked and metrical, locked to
>   the beat"* in all ten lanes, so ten genres arrived in one voice. Keep only the delivery rules
>   that are the *song* (for Camping: two named men, `never sung`)

  → One sweep's g1 used the same delivery phrase   in all ten lanes, so ten genres arrived in one voice. Keep only the delivery rules   that are the *song* (e.g. who is singing, and whether they sing at all)

- **line 292**

> # gpom-c12-cues3-v6-w10  1:40  https://suno.com/song/2ef65422-9967-4ddb-a6f3-1f5a56c96b71

  → # <story>-<cut>-<rev>-v6-w10  1:40  https://suno.com/song/<id>

- **line 340**

> (a story's per-cut budgets live in its own files, e.g. GPOM's narration sheet)

  → (a story's per-cut budgets live in its own files)

- **line 353**

> ✅ **Proven 2026-09-18 (Camping r48):**

  → ✅ **Proven 2026-09-18:**

- **line 356**

> 2026-09-21 (Camping r54): twelve v6 Creates

  → 2026-09-21: twelve v6 Creates

- **line 360**

> e.g. `gpom-cut1-A-v6-w<n>`,
> `gpom-cut1-A-wild-w<n>`

  → e.g. `<story>-cut1-A-v6-w<n>`, `<story>-cut1-A-wild-w<n>`

- **line 381**

> | fourteen Camping rounds under another song's profile |

  → | fourteen rounds under another song's profile |

- **line 382**

> | a two-man duet generated in GPOM's one narrator voice |

  → | a two-voice duet generated in another story's one narrator voice |

- **line 395**

> — which is all the Camping sheets —

  → — as some stories' sheets do —

- **line 406**

> covers of a Camping track — 40 credits

  → covers of another story's track — 40 credits

- **line 407**

> with GPOM's saved Voice (`badcode newsreader`) still attached

  → with another story's saved Voice still attached

- **line 427**

> two GPOM narration pairs (revisions A and B, **40 credits**) were generated as
> covers of a Camping source

  → two narration pairs (revisions A and B, **40 credits**) were generated as covers of another story's source

- **line 487**

> — for GPOM's saved Voice (`badcode newsreader`) that's GPOM's own track style.

  → — that persona's own track style.

- **line 499**

> ### 🆕 Three more, found 2026-10-22 (Bank Robbery)

  → ### 🆕 Three more, found 2026-10-22


## suno-prompt

Original: `archive/skill-pollution-2026-11-18/suno-prompt/SKILL.md`. Line numbers are in that original.

### 1. line 36

> 400+ Bank Robbery takes came out as one voice

→ 

    400+ takes of one song came out as one voice

### 2. line 57

> Bank Robbery's liked "psych folk funk, sitar,
>   tin whistle" take was really acoustic flamenco guitar over boom-bap.

→ 

    one past liked take (2026-10) was really
      a different genre from the one its Style box named.

### 3. line 61

> Bank Robbery Round KA lost the vibe

→ 

    One past refine round (2026-10) lost the vibe

### 4. line 68

> (Bank Robbery: ~150
> takes over one cop-funk backing, Jack heard one voice; "Led Zeppelin" and "Rolling Stones" voices
> came out "basically the same")

→ 

    (one past song, 2026-10: ~150
    takes over one backing, Jack heard one voice; two different named-artist voices
    came out "basically the same")

### 5. line 72

> from the story's own `sound.md`; Bank Robbery's tested wording is in its `sound.md`) and the music after

→ 

    from the story's own `sound.md`) and the music after

### 6. line 97

> four threads: the Karen genre-pool discovery and transplant ladder, My Taste forensics, GPOM's two-voice problem, and **Thread 4, the Camping duet — the tested failures behind "Two characters in one song"**

→ 

    four threads: the genre-pool discovery and transplant ladder, My Taste forensics, a two-voice problem, and **Thread 4, a duet — the tested failures behind "Two characters in one song"**

### 7. line 103

> whole log. Worked example: `docs/stories/camping/songs/`, where `camping.md` is the accepted
> sheet, `camping-released.md` the lyric-fidelity reference, and `archive/camping-prompt-history.md`
> the log. If the song rebuilds

→ 

    whole log. If the song rebuilds

### 8. line 106

> — Camping lost three words across nine rounds and nobody heard it.

→ 

    — one past song lost three words across nine rounds and nobody heard it.

### 9. line 208

> (Karen's voice, Camping's bar-one
> strings, GPOM's narration profile under fourteen Camping rounds)

→ 

    (one song's voice, another's bar-one
    strings, a narration profile under fourteen rounds of a different song)

### 10. line 292

>  Worked example: `stories/gitpush-origin-master/songs/git-push-origin-master-dnb.md` |

→ deleted

### 11. line 293

> **Delete the mention rather than describing a quiet version**. Worked example: `stories/camping/songs/camping.md` §4c |

→ 

    **Delete the mention rather than describing a quiet version**. |

### 12. line 294

>  (Camping: an amen fill over `chopped amen breaks`) has nothing

→ 

     has nothing

### 13. line 297

> Camping's verse cue went 1,010 → 311 with nothing lost.

→ 

    One verse cue went 1,010 → 311 characters with nothing lost.

### 14. line 299

> `suno-tag-mechanics.md`, and the gear table in `stories/camping/songs/camping.md` §4c |

→ 

    `suno-tag-mechanics.md` |

### 15. line 353

> (This cost the Karen track four rounds.)

→ 

    (This once cost a song four rounds.)

### 16. line 362

> Distilled from the eight-round Karen voice war

→ 

    Distilled from an eight-round voice fight

### 17. line 398

> (Karen first appeared on the parenthetical
>    answering-machine lines)

→ 

    (one character's voice first appeared on the
       parenthetical lines)

### 18. line 401

> (whiny complainer → comedy patter song, sparse piano)

→ 

    (the genre whose default singer already is that character)

### 19. line 413

> the smooth vocalist that kept invading Karen's lead became the institution's choir,
> singing the functionaries' answers against her spoken whine.

→ 

    in one past song the vocalist that kept invading the lead was recast as a second
    character answering the lead.

### 20. line 427

> (Camping looked like a
> two-hander and was really two solo verses either side of a 32-bar drop

→ 

    (One past song looked like a
    two-hander and was really two solo verses either side of an instrumental drop

### 21. line 434

> <accent>, <delivery>`; Bank Robbery's actual translation is in its `sound.md`). It moved the voice when accent, origin and timbre words all failed
> (Bank Robbery, 2026-10-21, `suno-voices.md` §2c).

→ 

    <accent>, <delivery>`; the story's own translation lives in its `sound.md`). It moved the voice when accent, origin and timbre words all failed
    (one past song, 2026-10-21, `suno-voices.md` §2c).

### 22. line 438

> A detailed Scouse spec produced zero

→ 

    A detailed regional-accent spec produced zero

### 23. line 448

> Camping stripped its accent language and lost `UK grime influence` in the same
> edit, and both men came back American.

→ 

    One past song stripped its accent language and lost its nationality-carrying genre word in the same
    edit, and both singers came back American.

### 24. line 454

> `UK grime` fixed Camping's nationality and cast both leads as
> young MCs, when they're a weathered fifty-something and a City banker. Choose the **tradition**
> instead — Camping's candidates were `British post-punk spoken word` for a middle-aged working-class
> bloke and a BBC-announcer tradition for the establishment one, with grime and drill only where a <!-- style-lint: ok — labelled GPOM/Camping examples -->
> young street voice is actually right (examples of the method, not a cast list).

→ 

    In one past song a national genre word fixed the nationality and cast both leads as
    young performers, when the characters were middle-aged. Choose the **tradition**
    instead: the performance tradition whose default performer is that age, class and place (the
    candidates come from the story's own `sound.md`).

### 25. line 490

> Drum & bass is one genre <!-- style-lint: ok — labelled GPOM/Camping examples -->
>   some of our songs use (GPOM's, Camping's), not BadCode's; if the song is D&B, see the D&B notes
>   below, because Suno is weak at exactly its subgenres.

→ 

    No genre is BadCode's;
      if the story's genre is a niche one, see "Where Suno will fight you" below.

### 26. line 503

> A song sung by
>   a character (Karen, Camping's two men) speaks

→ 

    A song sung by
      a character speaks

### 27. line 516

> - **Stay in canon.** If the idea ties to the GitPush Origin Master arc, skim
>   [`docs/stories/gitpush-origin-master/README.md`](../../../docs/stories/gitpush-origin-master/README.md)
>   and keep the polyphonic future-narrator voice and arc beats consistent.

→ 

    - **Stay in canon.** Read the story's own `badcode.md` and keep its narrator voice and arc beats
      consistent.

### 28. line 521

> Karen's whole outro
>   ("Hold, please") came from a statue panel the canon never mentions. They can also *disagree* with
>   canon (AI Sean vs "AI Shaun");

→ 

    One song's whole outro
      came from a panel the canon never mentions. They can also *disagree* with
      canon (a name spelled two ways);

### 29. line 529

> (the Karen track, 2026-07: first

→ 

    (one past track, 2026-07: first

### 30. line 538

> ### Skit / dialogue tracks — the worked recipe (Karen, 2026-07)

→ 

    ### Skit / dialogue tracks — the worked recipe (2026-07)

### 31. line 547

> — for
>   Karen: the hold-muzak loop *is* the lead melodic element, touch-tone beeps are percussion, dial
>   tone opens and closes the track.

→ 

    — a
      sound from the story's setting becomes the lead melodic element, another becomes the percussion,
      a third opens and closes the track.

### 32. line 554

> which also lets each voice get its own
>   phone EQ,

→ 

    which also lets each voice get its own
      EQ,

### 33. line 560

> ("I'm sorry, I can't help you" / "That's OK")

→ 

    (the background line asks, the lead's same answer comes back each time)

### 34. line 564

> *Ruled 2026-09-01 on the Camping narration, after ten rounds.

→ 

    *Ruled 2026-09-01 on one story's narration, after ten rounds.

### 35. line 568

> Nine
> Camping rounds asked for it

→ 

    Nine
    rounds of one song asked for it

### 36. line 601

> `Madchester
>   skit` is a British place name plus an *American* form word

→ 

    a British
      scene name plus `skit` is a British place word plus an *American* form word

### 37. line 622

> (GPOM's narrator: its `sound.md`)

→ 

    (that story's `sound.md` holds its recipe)

### 38. line 624

> Two notes from building GPOM's (its recipe and settings live in GPOM's `sound.md`):

→ 

    Two notes from building one (its recipe and settings live in that story's `sound.md`):

### 39. line 627

> GPOM built its narrator that way; which register (oratory, opera, preacher,
>   crooner, anything) is the story's choice. Audio influence 40–60 had the strongest effect there. <!-- style-lint: ok — GPOM's narrator, labelled on the line above -->

→ 

    One story built its narrator that way; which register is the story's choice. Audio influence
      40–60 had the strongest effect there.

### 40. line 633

> ### If the song is drum & bass — where Suno will fight you
> 
> 1. **Half-time drums are a known blind spot.** Repeated controlled tests never produced half-time
>    from a `breakdown` tag — it slows and thins the arrangement instead. Since the half-time drop is a
>    defining D&B device, **assume you cannot prompt it.** Get it by editing in Studio or splicing
>    sections, and tell the user that rather than selling them a prompt that won't work. **Live lead,
>    untested:** Studio 2.0's MIDI tracks let you program the pattern by hand instead of asking the
>    model for a concept it doesn't hold (`suno-studio.md` §2). Offer it as an experiment worth an
>    hour, not as a solution — and write the result back into the doc either way.
> 2. **Niche subgenres fail; broad ones work.** Riddim came back as generic dubstep with none of the
>    characteristic sound design — expect the same at neurofunk / liquid / jump-up level. **Mitigation:
>    describe the sound design and rhythm rather than relying on the subgenre name.** **v6 data
>    point (2026-09-09, ChillPanic):** a lazy `liquid DnB` prompt came back as two-step drums, while
>    an engineered one naming the drum mechanics (`jungle breaks, rapid chop, hyperdetail
>    percussion, dark synth bassline`) worked on both models. Same lesson, now on v6. v6 Wild is
>    deliberately "less tuned towards preferences" — the model to hunt niche D&B in, then Cover
>    into v6 (`suno-v6.md` §9). `producer-
>    vocabulary.md` is exactly that toolkit — reese bass, sample-and-hold on the cutoff, amen break,
>    sub layering, sparse drop.
> 3. **Suno's harshness sits exactly where D&B lives** — brittle cymbals, sizzling hats, sibilance in
>    2–6 kHz. Budget for de-essing, or plan to replace the drum stem.
> 4. **Sidechain pumping can't be undone** — it's baked in, not a real sidechain.
> 5. **Sounds mode is a post-production kit** — risers, downlifters, sweeps, impacts, fills, at
>    your project's BPM and key. Suno won't build transitions into a generation, so this is how you get
>    them.

→ 

    ### Where Suno will fight you (niche genres)
    
    Engine facts measured on one genre (the full original notes are archived in
    `archive/skill-pollution-2026-11-18/suno-prompt/`); the genre itself is the story's call.
    
    1. **Half-time drums are a known blind spot.** Repeated controlled tests never produced half-time
       from a `breakdown` tag — it slows and thins the arrangement instead. If a genre's defining device
       is a half-time drop, **assume you cannot prompt it.** Get it by editing in Studio or splicing
       sections, and tell the user that rather than selling them a prompt that won't work. **Live lead,
       untested:** Studio 2.0's MIDI tracks let you program the pattern by hand (`suno-studio.md` §2).
       Offer it as an experiment worth an hour, not as a solution, and write the result back either way.
    2. **Niche subgenres fail; broad ones work.** A niche subgenre name comes back as its broad parent
       with none of the characteristic sound design. **Mitigation: describe the sound design and rhythm
       rather than relying on the subgenre name** (v6, 2026-09-09: a lazy subgenre prompt failed, one
       naming the drum mechanics worked on both models). v6 Wild is deliberately "less tuned towards
       preferences": the model to hunt a niche sound in, then Cover into v6 (`suno-v6.md` §9).
       `producer-vocabulary.md` is the toolkit for naming the mechanics.
    3. **Suno's harshness sits in 2–6 kHz** — brittle cymbals, sizzling hats, sibilance. Budget for
       de-essing, or plan to replace the drum stem.
    4. **Sidechain pumping can't be undone** — it's baked in, not a real sidechain.
    5. **Sounds mode is a post-production kit** — risers, downlifters, sweeps, impacts, fills, at
       your project's BPM and key. Suno won't build transitions into a generation, so this is how you get
       them.

## variations

- **Line 13**, original:

> Bank Robbery's
> song went 400+ takes as one voice

  → replaced with: One story's song went 400+ takes as one voice


## video-fx

- **Line 158**, original:

> `camping.mp4` — the finished film — shipped

  → replaced with: One finished film shipped

- **Line 161**, original:

> On a dark film (Camping and GPOM both are) this is

  → replaced with: On a dark film this is


## voice-casting

- **Line 13**, original:

> Jack asked for it on 2026-11-11 (Priority Lane:
> "put the voices in a skill that I can pick from like the new scene artifact"). First run:
> `docs/stories/shorts/priority-lane/voices/`.

  → replaced with: Jack asked for it on 2026-11-11: "put the voices in a skill that I can pick from like the new scene artifact".


Second pass, moved not deleted: the balaclava-in-motion tip from new-short now lives in docs/library/tricks/README.md (balaclava row).
