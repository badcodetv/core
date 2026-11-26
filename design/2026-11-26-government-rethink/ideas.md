# What the BadCode government is for, and the least that does it

An ideas pass on 26 Nov 2026, the day the government was paused ([`docs/government/PAUSED.md`](../../docs/government/PAUSED.md)).
Kai asked for it: "What are we trying to do? It's this page that is important... maybe we're overthinking it."
It was written by a Fable 5.2 subagent at extra-high effort, read-only. Figures marked as guesses are guesses.
Nothing here is decided: Kai or Jack picks.

## 1. The job

**The government exists to make a stranger say "hang on, why does it work like this?" and hand them one line they can repeat in the pub.**

Tests for any idea:
- **Twenty seconds, on a phone, sound off:** does a stranger get it?
- **Tomorrow:** can they say it to a mate?
- **Six months untouched:** is it still true and worth a look?
- **Would Kai and Jack look at it themselves?** They never looked at any of the three experiments. That is the verdict on all three.

All three experiments answered "how would it work?" before anyone had asked. The three questions answer "why should I care?", which comes first. And the reader is on Facebook, YouTube and TikTok, not badcode.tv (`docs/marketing/the-reader.md`), so anything on GOVT only counts if it also works as a 20-second video.

## 2. Ideas, least to boldest

All need zero ongoing AI spend except idea 6 (tiny).

**1. The three questions are the whole government.** GOVT keys 1, 2, 3 are the three questions and nothing else is on the channel. It is already the best thing made. Cost: hours. Risk: looks thin. A poster people remember beats a parliament nobody reads.

**2. The telly with two channels.** Press GOVT and the TV offers RED and BLUE only, then the remote locks: "Next channel change: 15 August 2029." Five seconds later: "Annoying, isn't it?" and the three questions. The site is already a television, so questions one and two are felt before a word is read. Pub line: "Imagine a telly with two channels and a remote that works once every five years. You'd take it back to the shop." Cost: a day or two of front-end (guess). Risk: irritating, so first visit only and skippable, like the existing hijack. The date is the agent's reading of the 2022 Act: check it.

**3. One thing to press per question.**
- Q1: answer six issues and see what each bundle forces on you ("Red: 3 you didn't want. Blue: 4. Build your own: 0").
- Q2: an UNDO button that replies "Request received. Earliest undo: 993 days", over a counter of days since you were last asked (875 today; both are the agent's arithmetic, to check).
- Q3: a medicine box with a law's name on it. Turn it over: "Tested on: nobody."

Pressing beats watching. A bundle toy and a test-label toy already exist in the parked October prototype (`design/2026-10-17-microsites/future-proof-prototype.html`), which Kai never noted. Cost: two to four days (guess). Risk: choosing the six issues is itself political. Leaving immigration out looks like dodging; putting it in starts the wrong fight.

**4. Your strip.** Your six picks become a strip of coloured bricks, a picture captioned "They let me pick one colour." Nothing is sent anywhere, in line with Kai's 23 Nov ruling that visitor picks stay in the browser. It is the thing to share. Cost: a day on top of idea 3. Risk: a guess that under one in fifty shares it.

**5. The questions as three 15-second videos, and the shorts numbered.** Film the existing scenes upright with the narrator. The government in action already exists as shorts: Signs is question 1, Pub Quiz: Democracy is 1 and 2, The Den is 3 (its stated point is "no policy without its test"). Shelve each under its question, with one rule: nothing goes on GOVT unless a person made a video of it. That shrinks the 56-policy manifesto to the ones already filmed (The Queue, Sponsor a Chancellor, The Forecast). Cost: a day for the three videos. Risk: bricks may be dry as video, so test one.

**6. Envelope day** (the minimum honest "testable politics"). About 56 dated predictions on real Britain, with odds and frozen rules, are already written in `docs/government/policies/`. The first two fall due on 15 December 2026, the last in March 2028. Keep the ten a stranger would care about, show them as sealed envelopes with dates, open each on its day and print the misses. A superintelligence being wrong in public and saying so "is more than your MP has managed", and each opening is a 15-second short. Cost: a page (a day), then five minutes of a person or one small run per envelope, about one a month. Guess: under 1% of the old spend. Risk: most of the 56 are dull (one is about a UN conference document). If we can't find ten good ones, drop it.

**7. The town that tried it.** One made-up town, one issue, four pictures: residents set the test, three answers, a small trial, then the date arrives and it is kept or undone. Sixty seconds, told by a resident, written once, never updated. It is Kai's "what it would look like in reality" with nothing running. Built from one of the demo days (branch `demo/live`); the bus-fare day is a subject everyone gets, though that one ended "rejected". Cost: a short's worth of work. Risk: worthy and dull without a character and a joke. A Jack job.

**8. Ask them.** BadCode sends the three questions, once and publicly, to every party leader in Parliament. The page shows the replies, or "Days without an answer: N". It makes a wording option already on file, "Three questions nobody will answer you", literally true. Cost: an afternoon by a human. Risk: with no audience yet, silence both ways; boilerplate replies (still funny read by the narrator).

**9. The pub round.** A free printable quiz round (the secret ballot: 1872; the longest a government can go without asking you: five years) ending on the three questions, plus a beer mat with a question on each side. The reader doc says the real product is the argument in the pub. Cost: a day, plus printing (guess £50 to £100 for 500 mats). Risk: unmeasurable, and it is work away from the screen.

**10. The song.** Three verses, three questions. CLAUDE.md says people absorb a song as they never absorb an essay; the reader research ranks a music video first. The government has had 56 policies and no song. Cost: a normal song round. Risk: cringe unless it is somebody's story (the one-party voter at the quiz table).

**Does anything live earn its cost?** Only a clock (arithmetic) and the envelopes (the calendar). No daily agent does until an audience is asking for one.

## 3. Stop, retire, salvage

**Stop for good:**
- All three daily runs: an estimated 2 to 2.5M tokens a day for output nobody read.
- GOVT 2 to 5 (Live, The floor, The record, Replay), `/future-proof/live/` and `/demo/`: off the TV, old addresses pointed at the three questions. (Done on 26 Nov.)
- The cabinet, opposition, statistician, minister pages, statements and vibe desk: archive.
- The chain record and "invite the world's agents": park. There is no audience to invite.
- PR #29: Kai to rule on closing it unmerged.

**Salvage:**
- The dated predictions (idea 6) and one demo day (idea 7).
- The October prototype's toys (idea 3).
- The "Update Available" talk (`docs/stories/future-proof/slideshows/launch-talk/`, 17 slides, 3:17). Kai said "I love this... far too long" of the earlier cut; this is the short one, and it is off the TV. It is the long version of the three questions.
- `docs/government/evidence.md` as the fact drawer for shorts.
- Two lines: "Jury: 2. Should be 99." and "set the test, write the answer, check it, mark it".
- The failure itself as one short: "We built an AI government. It argued with itself about three policies for eleven days and nobody read a word. So: accurate."

**One wording flag (a guess):** this reader trusts almost nobody, so "ask the experts" may be the weakest of the three buttons. The option already on file, "Would you take a pill nobody tested?", makes the reader the judge.

## 4. Top three

1. **The telly with two channels, opening onto the three questions and nothing else (ideas 2 and 1).** It is the cheapest thing that passes all four tests, it uses the television already built, it gives the pub line, and it films as a short. **Next step:** mock the five-second locked remote on the existing TV, film it on a phone, and show Jack with the sound off. If he laughs, that is the channel.
2. **Three 15-second videos and the numbered shorts (idea 5).** The reader will never type badcode.tv, and the 24 Nov meeting already called content complete and release next. All three questions already have a short.
3. **Envelope day (idea 6).** It is the only cheap way BadCode keeps doing what it asks of others, and 15 December is a free deadline to find out whether anyone cares.

Runner-up: the UNDO button from idea 3, which could ship alone in an afternoon.

## Files this rests on

- `apps/site/public/future-proof/questions/index.html` (the three questions and every wording option)
- `design/2026-10-17-microsites/future-proof-prototype.html` (the parked toys)
- `docs/government/policies/` (the dated predictions, field `check.check_on`)
- `docs/marketing/badcode-shorts.md` (shorts 33, 91, 97 carry the three questions)
- `docs/stories/future-proof/slideshows/launch-talk/deck.md`
- `design/2026-11-23-future-proof-rework/adversarial-review-2026-11-23.md`
