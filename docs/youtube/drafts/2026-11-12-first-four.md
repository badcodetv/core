# YouTube words: the first four videos (draft, 2026-11-12)

**Status:** DRAFT by marketing-producer. Not checked by the gatekeeper yet. Not applied. Kai or Jack picks.
Titles are fixed (Kai, 2026-11-12) and are not touched here.

**How to read this:** each video has two or three opening options (the part that shows before "more"),
marked **PICK** with one line why, then one body, the AI line, links, hashtags, tags and a pinned comment.
Every choice cites the repo doc that justified it. No new research was done (chief-of-staff plan §9 rule 1).

## Before any of this goes on

- 🔴 **The full account page does not exist.** `using-ai.md` §0 says the one-line disclosure links to "the
  full account" at a stable URL. `apps/site/` has the one-liner on `/about` but no account page. Every
  description below carries the placeholder `[FULL ACCOUNT URL: not built yet]`. Either build it, or point the
  line at `https://www.badcode.tv/about` for now and say so.
- 🟡 **badcode.tv is deployed** (production upload 2026-11-04 in `scripts/site/releases.tsv`, served at
  `www.badcode.tv`), but its story pages still say "Coming to YouTube": `apps/site/src/content.json` has
  `film: null` and `songVideo: null` for all four. Fill in the YouTube ids there when these go public, so the
  site and the descriptions point at each other. Page map (from `apps/site/build.mjs`): films are
  `/stories/1`–`4`, songs `/stories/5`–`8`, so GPOM film = `/stories/1`, Karen's song = `/stories/7`,
  The Bank Robbery song = `/stories/8`. The Rules has no page yet (NEWS is where shorts go, `apps/site/README.md`).
- 🟡 **Cross-links between videos** use the real `youtu.be` ids from `docs/youtube/channel.json`. They only
  work once the target video is public or unlisted.
- ⬜ **No mailing list yet** (board.md "Do next" 1), so no signup link anywhere. Add it to every description
  the day "Transmissions" exists (shorts-growth.md §4, "One landing page, one offer").
- ⬜ **TikTok handle not recorded** (`social-media-accounts.md`), so TikTok is left out of the links.

---

## 1. Git Push Origin Master (9:32, 16:9 film) · https://youtu.be/OaP0RthL_0Q

### Opening (shows before "more")

- **A (PICK):** Somebody pushed the code live without checking it. A sci-fi short film scored in drum & bass,
  told by an AI from a future that already went wrong.
  *Why: plain words for a reader who has never typed `git`, and it carries the search words "sci-fi short film",
  "drum & bass" and "AI" in the first two lines; the first sentence is the site's own blurb, so the film reads the
  same everywhere.*
- **B:** `git push origin master`: the command that sends your code to everyone, with no undo. Humanity just ran
  it. A sci-fi short film in drum & bass, from a future that already went wrong.
  *Better for people searching the title itself, worse for the reader who doesn't code.*
- **C:** I've seen how this ends. You haven't, yet. Nine minutes of sci-fi and drum & bass about the week the
  redundancies hit the news.
  *Strongest voice, weakest search.*

### Body

```
It starts on the news. Office workers sent home. The economy coming apart a bulletin at a time. Everyone very calm about it.

Nobody tested it, because testing costs money today and the damage comes due tomorrow. Somebody made that call. I know, because I'm what came of it.

You still have time to read the code before you ship it. That's why I'm here.

Watch it with the sound up. The track is the first half of the story.
```

### AI line, links, hashtags

```
Made by machines trained on work nobody was paid for. So was the future I come from.
The full account: [FULL ACCOUNT URL: not built yet]

The story, the song and the rest: https://www.badcode.tv/stories/1?src=yt
Next: Karen will lead the revolution (music video) https://youtu.be/c9jhLpkjv6o

#drumandbass #scifi #shortfilm
```

### Tags (347 characters, counting the quotes YouTube adds round multi-word tags)

`Git Push Origin Master, git push origin master, sci-fi short film, AI short film, short film, drum and bass, dnb, drum and bass music video, dnb music video, artificial intelligence, superintelligence, AI future, dystopia, dystopian short film, British sci-fi, UK short film, redundancies, automation, cost of living, BadCode, badcode tv`

### Pinned comment

```
Written by two people in the UK. Made with machines. Told by one that came back to say sorry in advance. What did you hear in the bulletins? — Kai / Jack
```

*Optional. Ends on a question so the first comments have somewhere to start (chief-of-staff plan §7, "be there,
and answer the first comments"). Signed, because it is about who made it (plan §7, "as ourselves, signed").*

### Why each choice

- Search words up front, explained title in the body: plan.md §3.10 (evergreen search, "titled/described for
  search"); platform-playbooks.md §3 Provisional ("long-form: title/describe for search").
- Setup only: the bulletins are the film's first act; the robot, the hundred, the bunker, the time machine and
  the last line are left out. Kai's ruling 2026-10-22 (apps/site/README.md, "Blurbs and stills are setup only").
- "Somebody made that call", not "AI did it": the-reader.md rule 5 (name the decision, not the technology) and
  rule 6 (aim the anger; relaxed to advice, so the chooser is implied, not named).
- "I'm what came of it": using-ai.md §8 (the narrator is a defendant, not a prophet; certainty about what
  happened, never about what must happen).
- Drum & bass in hashtags and tags: chief-of-staff plan §6 ("Second audience: drum & bass listeners, reached
  through the music").
- Website with `?src=yt`: shorts-growth.md §4 (one landing page, source tag per platform); plan.md (UTM tags).
- "Next:" link: platform-playbooks.md §3 Provisional ("end screens to the next core"); shorts-growth.md §4
  (links work in long films' descriptions and end screens).
- No swear word in the hook: lane rule from the producer brief (none in YouTube titles; kept out of the
  preview lines too, where it would read as the title's neighbour).

---

## 2. Karen will lead the revolution (music video) (4:10, 4K 16:9) · https://youtu.be/c9jhLpkjv6o

### Opening

- **A (PICK):** "I want to speak to your manager." The most hated sentence in the English language, finally
  pointed at the right people. A music video for All Day to Complain.
  *Why: the phrase people actually search sits first, the second line re-aims it upward without spoiling how far
  up it goes, and the song title is in the preview for anyone searching the song.*
- **B:** Karen has lost her job, and she would like to speak to the manager. She has all day. The music video
  for All Day to Complain.
  *The site's blurb word for word. Safest, quieter.*
- **C:** Every company has a complaints line. Nobody has ever reached the top of one. Karen has all day.
  *Funniest, but loses "speak to the manager" from the preview.*

### Body

```
Karen has lost her job. She did not take it quietly. She took it to the front desk, then the man behind the front desk, then the man behind him.

Somebody signed off on letting her go. She would like a word. She has all day.

Blues, a baritone sax, and one woman who will not hang up.
```

### AI line, links, hashtags

```
Made by machines trained on work nobody was paid for. So was the future I come from.
The full account: [FULL ACCOUNT URL: not built yet]

The song and the story: https://www.badcode.tv/stories/7?src=yt
Next: The bank robbery (music video) https://youtu.be/XinO1Kze_5A

#Karen #SpeakToTheManager #MusicVideo
```

### Tags (350 characters, as YouTube counts them)

`Karen, Karen music video, Karen song, speak to the manager, I want to speak to your manager, All Day to Complain, Karen will lead the revolution, funny music video, comedy music video, satire, political satire, blues rock, saxophone, customer service, complaints, made redundant, laid off, fired from my job, New York, BadCode, badcode tv`

### Pinned comment

```
Who would you make her call first? — Kai / Jack
```

*Optional. Invites the argument in the comments (the-reader.md rule 8, "write for the conversation afterwards").*

### Why each choice

- No AI in the Karen words: shorts-karen-camping.md §9, way 1 ("lean on the comedy and the complaint, not the
  automation"), because board.md "Then" 8 still says Karen's beneficiary fix is unpicked. If Kai or Jack want the
  AI firing named, add way 2's line: `The machine didn't buy itself.`
- "Somebody signed off on letting her go": the-reader.md rule 5 (name the chooser) without spending the ending.
- Karen is the hero, not the joke: voice.md "Don't punch down… the 'Karen' — these are sympathetic";
  the-reader.md rule 1 (hero, not pupil).
- Setup only: the phone box and the first rungs of the ladder; the President, the live broadcast, the statue and
  the cliffhanger are left out. Kai's ruling 2026-10-22.
- Hashtags: shorts-growth.md §3 ("one to three topical hashtags at most").
- Tags lead with what people type ("Karen song", "speak to the manager"): shorts-growth.md §3 (plain search
  words); plan.md §3.10.

---

## 3. The bank robbery (music video) (3:07, 16:9) · https://youtu.be/XinO1Kze_5A

### Opening

- **A (PICK):** Own a printer and you don't feel winter. A heist music video about money printing, the cost of
  living, and who got the money first.
  *Why: a line from the song as the hook (quotable, rule 8), then the search words "music video", "money
  printing", "cost of living", and the beneficiary in the same breath (rule 6).*
- **B:** Call the police, it's a robbery. A balaclava gang raps the cost of living straight down the lens: rent,
  landlords, money printing, and grandma freezing.
  *The chorus as hook; more picture, no beneficiary in the preview.*
- **C:** The Bank of England made £895 billion. Grandma's still freezing. A heist music video.
  *Hardest hitting, but the two sentences together imply a cause the canon won't let us claim
  (bank-robbery/story.md, "QE made inequality worse" is on the may-not-say list). Gatekeeper would likely fail it.*

### Body

```
A gang in coloured balaclavas and sharp suits robs banks and raps it straight down the lens. Tommy guns, hot rods, and a lyric sheet about rent, landlords and quantitative easing.

The left and the right both watched it happen, and blamed each other. Nobody broke a window. The money was made, it bought what was already owned, and it reached the people who owned it first.

Count it again.
```

### AI line, links, hashtags

```
Made by machines trained on work nobody was paid for. So was the future I come from.
The full account: [FULL ACCOUNT URL: not built yet]

The song and the story: https://www.badcode.tv/stories/8?src=yt
Next: The Rules Are Not Working Anymore https://youtu.be/9ha83RIv0YU

#CostOfLiving #QuantitativeEasing #MusicVideo
```

### Tags (340 characters, as YouTube counts them)

`The bank robbery, bank robbery music video, bank robbery song, heist, heist music video, balaclava, balaclava gang, music video, money printing, quantitative easing, cost of living, inflation, landlords, rent, wealth inequality, political song, economics song, British rap, boom bap, acoustic boom bap, satire, BadCode, badcode tv`

### Pinned comment

```
The numbers, from the Bank of England's own paper: spread evenly, the money it made would have come to about £10,000 each. It wasn't spread evenly. The poorest tenth of households gained about £3,000; the wealthiest tenth about £350,000. Who did you see it reach first? — Kai / Jack
```

*Every figure is on the may-say list in `docs/stories/bank-robbery/story.md` ("What we may and may not say"):
£10,000 is "the Bank's own illustration, not a debt"; the £3,000 / £350,000 gains are allowed, "QE made
inequality worse" is not, so the comment states the gains and draws no conclusion. 🟡 Add the paper's link
from `bank-robbery/research.md` before it goes up.*

### Why each choice

- "Who got the money first": the-reader.md rule 6 (aim the flame); bank-robbery/story.md ("the money made, and
  who it reached first").
- "The left and the right both watched it": the song's own line, and the story's rule that left and right are
  mocked equally (bank-robbery/characters/the-crew.md, via README); the-reader.md rule 2 (show the trick run on
  someone else, never "you've been duped").
- "Nobody broke a window": keeps the film's twist (they carry the money *in*) out of the song's blurb. Kai's ruling
  2026-10-22.
- No immigration line at all: the-reader.md rule 10 (never repeat the lie to refute it).
- Source note in the pinned comment: shorts-growth.md §4 (a pinned comment is still useful "for a source note").
- Hashtags and tags: shorts-growth.md §3; the reader's own words ("cost of living", "rent", "landlords"):
  the-reader.md portrait.

---

## 4. The Rules Are Not Working Anymore (0:28, 9:16 Short) · https://youtu.be/9ha83RIv0YU

### Opening (a Short's description is short and is rarely read: the title and the first second do the work)

- **A (PICK):** We can't afford a bed for you. There's room on all those islands. Are the rules working? Let's
  look out the window.
  *Why: the sung words and the on-screen question, so speech, screen and description share the same search words
  ("bed", "islands", "rules").*
- **B:** A stack of rules taller than the room, and one question: are they working? Let's look out the window.
  *Cleaner, but drops "bed" and the islands.*
- **C:** Tax havens and homelessness, in one school hymn and 28 seconds.
  *Most searchable, least funny.*

### Body

```
Some rules are good. Don't murder people: keep that one. Some rules were written by the people they protect.

The test of a rule book is the street outside it.

Send this to whoever told you there's no money.
```

### AI line, hashtags (no links: they can't be tapped on a Short)

```
Made by machines trained on work nobody was paid for. So was the future I come from.

#TaxHavens #Homelessness #TheRules
```

### Tags (254 characters, as YouTube counts them)

`The Rules, the rules are not working, tax havens, tax avoidance, offshore, homelessness, homeless, housing crisis, school hymn, hymn, balaclava, balaclava gang, satire, political satire, UK politics, funny short, BadCode, BadCode Shorts, badcode tv`

### Pinned comment

```
The islands: some of them fly our flag, and a company's profits booked there can pay little or no tax. The full story of where the money goes: The bank robbery (music video), linked above. — Kai / Jack
```

*🔴 Hold until the tax-haven wording is fact-checked: it is still owed in `short-the-rules/scenes/the-rules/picks.md`
("Little or no tax" and "flies our flag" are the safer shapes; Bermuda's 15% for big multinationals means "no tax"
is not true everywhere). Text only: pinned comments can't be tapped on a Short (shorts-growth.md §4).*

### Studio steps that matter more than the words

- **Related video → The bank robbery (music video).** Same balaclava gang, so the jump makes sense. This is "the
  one official clickable path" from a Short, set by hand in Studio on desktop (shorts-growth.md §4;
  shorts-release.md §4). Needs phone verification (shorts-growth.md §8).
- **No `#Shorts`**: "#Shorts isn't needed" for a vertical video under 3 minutes (shorts-release.md §4, official).
- **Cover:** the first frame is the sure cover (shorts-release.md §4).

### Why each choice

- Lyric + on-screen question as the description: shorts-growth.md §3 ("same plain words in speech, screen and
  caption", naming "homeless", "tax havens", "bed").
- "Send this to whoever told you there's no money": shorts-growth.md §3 ("Sends: write one line people would
  forward", the doc's own example line).
- Good rules stay: short-the-rules/README.md and badcode-shorts.md #24 (tearing up must read as rewrite, not "no
  rules").
- "Written by the people they protect" (not a named party or person): short-the-rules/README.md (the target is
  the rule-makers); shorts-growth.md §5 notes policy beats party as a hypothesis to test, not a fact.
- Setup only: the tear and the pen are left out. Kai's ruling 2026-10-22.

---

## How much tags matter (the one line)

The repo's playbooks say nothing about tags themselves. The nearest evidence is shorts-growth.md §2: hashtags
"do not matter" for Shorts (official, YouTube staff 2025), and §3: titles and the words people hear and see do
the search work. So tags here are cheap insurance (misspellings, the song's name, the reader's own words), not a
growth lever. Spend the effort on the title, the first two lines, the Related video and the end screens.

---

## Rules of thumb we used

For the youtube-channel skill. General, not about these four.

1. **The first two lines are the description.** Put the plain words a viewer would type there, in the order they'd
   type them. (plan.md §3.10 evergreen search; platform-playbooks.md §3 Provisional.)
2. **Same words in speech, on screen and in the description.** If the song says "bed", the description says "bed".
   (shorts-growth.md §3, "Search words".)
3. **One to three topical hashtags, never more; no `#Shorts`.** Hashtags don't move Shorts reach, and a vertical
   video under 3 minutes is a Short without the tag. (shorts-growth.md §2–3; shorts-release.md §4.)
4. **Tags are insurance, not a lever.** The repo has no evidence that they move reach; keep them honest, under 500
   characters, in the viewer's words. (shorts-growth.md §2–3; see "How much tags matter".)
5. **Links only where they click.** On a Short: set the Related video by hand in Studio; the description and pinned
   comment are text only. On a long film: website with `?src=yt`, the next video, end screens. (shorts-growth.md §4.)
6. **Every description carries the one-line AI disclosure, in voice, linked to the full account; Studio's
   "altered or synthetic content" is set to Yes.** The label costs no reach. (using-ai.md §0; shorts-release.md §4;
   platform-playbooks.md §3; shorts-growth.md §6.)
7. **Setup only. Never the twist, never the ending.** (Kai, 2026-10-22, in apps/site/README.md.)
8. **Name the decision, not the technology; aim the anger at who benefits.** If a description mentions AI, jobs or
   money, someone chose it and someone gained. (the-reader.md rules 5–6.)
9. **Never tell the viewer they've been fooled.** Show the trick being run on someone else. (the-reader.md rule 2;
   chief-of-staff plan §6.)
10. **Write one line people would forward or argue about.** The goal is sends and the pub argument, not views.
    (shorts-growth.md §3 "Sends"; the-reader.md rule 8; chief-of-staff plan §2.)
11. **Only claims the story's own may-say list allows, with the source in the pinned comment.** (Each story's
    `story.md` "What we may and may not say"; shorts-growth.md §4, pinned comment "for a source note".)
12. **Don't look templated.** Vary the shape of each description; a named series, written words and our own music
    are what read as authored, and mass-produced AI is what YouTube demonetises. (shorts-growth.md §6.)

---

## Gatekeeper verdicts (2026-11-12)

Checked against the-reader.md (ten rules), voice.md, using-ai.md §0 and the never-say list, each story's canon
(no-spoilers, Kai 2026-10-22) and its may-say list, and the claim sources in `bank-robbery/research.md`.
Titles not judged.

### Across all four

- **AI line wording: PASS.** It is using-ai.md §0's own line, in voice, escalates rather than excuses. Same line
  on `/about` (`apps/site/src/content.json` `about.ai`), so it is consistent.
- **AI line link: REVISE (do not publish the placeholder).** `/about` carries the one-liner and the origin story
  but **names no tools**, so linking it does not meet §0 / §5.3 ("the account, naming the specific tools, one click
  away"); someone who clicks gets the same sentence back, which reads as dodging. Fix, in order of preference:
  (1) build a minimal account page first (tools named: Flow/Nano Banana/Omni, Suno, AI Studio voices, Premiere;
  what humans did; the costs stated bare) and link it; (2) if Kai wants these up before that exists, link `/about`
  **and** add the tools to the About page the same day. Never ship `[FULL ACCOUNT URL: not built yet]`.
- **Site links /stories/1, /7, /8: PASS, not guessed.** `apps/site/build.mjs` builds films at `/stories/{i+1}`
  and songs at `/stories/{i+5}` over `content.json` order GPOM, Camping, Karen, Bank Robbery, so GPOM film = 1,
  Karen song = 7, Bank Robbery song = 8. Condition: fill `film` / `songVideo` in `content.json` the day these go
  public, or the link lands on "Coming to YouTube".
- **Studio "altered or synthetic content" = Yes: PASS.**
- **Footage credits:** none of the finished cuts' `final.json` lists third-party footage. If any archive or CC
  clip is in the GPOM bulletins, a credit line is owed in that description. Kai to confirm.

### 1. Git Push Origin Master: REVISE (one line)

- **Opening A: PASS, PICK.** Setup only; "somebody pushed" names a chooser (rule 5). Drum & bass checks out
  (GPOM `sound.md` §1, LOCKED).
- **Opening B: PASS**, not picked (codes at a reader who doesn't code).
- **Opening C: PASS**, not picked (weakest search).
- **Body: PASS.** Bulletins are act one; chooser named ("Somebody made that call"); beneficiary implied, allowed
  under rule 6 as relaxed 2026-10-23. "I'm what came of it" is the BadCode premise, already on `/about`.
- **AI line / links / hashtags: PASS** (link target per "Across all four").
- **Tags: PASS.** ("cost of living" is a stretch for this film; harmless.)
- **Pinned comment: REVISE.** `Told by one that came back to say sorry in advance.` The apology is a back-half beat
  (README: "the AI regrets, apologises and sends itself back"), so it spends the ending. Fix:
  `Written by two people in the UK. Made with machines. Told by one that has seen how it ends. What did you hear in the bulletins? — Kai / Jack`

### 2. Karen will lead the revolution (music video): PASS

- **Opening A: PASS, PICK.** Karen stays the hero (rule 1, voice.md "don't punch down"); "pointed at the right
  people" aims upward without reaching the President.
- **Opening B: PASS** (site blurb, safe). **Opening C: PASS**, not picked (loses the search phrase).
- **Body: PASS.** Stops at the second rung; President, live broadcast, statue and callback all kept out. No AI
  mentioned, so rule 6 is not triggered; the chooser is named ("Somebody signed off").
- **Way-2 option `The machine didn't buy itself.`: PASS if Kai wants AI named** (it carries its own beneficiary).
- **AI line / links / hashtags / tags: PASS.**
- **Pinned comment: PASS.**

### 3. The bank robbery (music video): REVISE (pinned comment)

- **Opening A: PASS, PICK.** "Own a printer and you don't feel winter" is the sung line (`mv-gang/song-transcript.json`);
  beneficiary in the same breath (rule 6). "Money printing" is the song's idiom, not the may-not claim.
- **Opening B: PASS**, not picked (no beneficiary in the preview).
- **Opening C ("£895 billion… Grandma's still freezing"): FAIL.** £895bn alone is on the may-say list, but the hook
  works only by implying the money could or should have reached grandma, i.e. the may-not "they printed £895bn and
  gave it to the rich". Reworded to remove that, it stops being a hook and becomes option A.
- **Body: PASS.** "The left and the right both watched it happen" matches the lyric ("The right and the left both
  witness the theft"); "it bought what was already owned, and it reached the people who owned it first" matches the
  may-say ("bought assets"; "who it reached first"). "Nobody broke a window" hints, but does not give, the
  money-in twist.
- **AI line / links / hashtags / tags: PASS.**
- **Pinned comment: REVISE.** Three factual errors against `research.md`:
  1. "from the Bank of England's own paper": it is **two** papers (2012 Bank paper; 2018 Bank **staff** working paper).
  2. "the money it made would have come to about £10,000 each": the £10,000 is the 2012 paper's figure for the
     **first £325bn** raising household wealth by ~£600bn, not the £895bn total.
  3. The £3,000 / £350,000 figures cover **all the easing 2006-08 to 2012-14, rate cuts included**, not QE alone,
     and research.md says they "must travel with" the broadly-similar-in-percentage finding. Omitting it in a
     *source note* is the selective quote a hostile reply will screenshot.
  Fix:
  `The numbers are the Bank of England's own. 2012: the first £325bn it made lifted household wealth by about £600bn, around £10,000 a person if evenly spread. It wasn't. 2018, Bank staff, on all the easing 2006–2014: the poorest tenth gained about £3,000, the wealthiest tenth about £350,000. In percentage terms, they say, much the same. In pounds, judge for yourself. Who did you see it reach first? — Kai / Jack`
  plus both paper links from `research.md`. (Kai/Jack: Jack ruled the percentage defence "a target, not a limit";
  this puts it in the Bank's mouth and answers it, as scene 14 does. If they'd rather drop the percentage clause,
  then drop the £3,000/£350,000 sentence too.)

### 4. The Rules Are Not Working Anymore: REVISE (pinned comment)

- **Opening A: PASS, PICK.** Sung words plus on-screen question; no fact claim.
- **Opening B: PASS. Opening C: PASS**, not picked.
- **Body: PASS.** Keeps the good rules (rewrite, not anarchy); "written by the people they protect" names no one.
  "Send this to whoever told you there's no money" puts the reader on the sending side, not the duped side (rule 2).
- **AI line: PASS**, but as text add `badcode.tv/about` (or the account URL) after it: a Short can't link,
  but it can name where the account is.
- **Hashtags / tags: PASS.**
- **Pinned comment: REVISE.** The tax-haven claim, judged: "some of them fly our flag" is true (the Overseas
  Territories do; the Crown Dependencies don't, and "some" covers it); "can pay little or no tax" holds with "can"
  (several territories levy no corporate income tax; Bermuda's 15% from 2025 binds only big multinationals). Still
  owed: a researcher's one-line source before it goes up, as `picks.md` asks. Second problem: "The full story of
  where the money goes: The bank robbery" is untrue; that film is about QE, not tax havens. And "linked above" is
  wrong on a Short. Fix:
  `Those islands: some of them fly our flag, and profits booked there can pay little or no tax. Same gang, different job: The bank robbery (music video), linked on this Short. — Kai / Jack`
- **Studio steps: PASS.**
