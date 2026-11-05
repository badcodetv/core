# Future Proof: deck v3 (the big edit, 2026-11-05)

**Replaces deck v2** (58 slides, 8:41), which is kept in [`history/deck-v2.md`](./history/deck-v2.md). Kai on round 1: "I love this... I think it works... far too long. A very, very big edit. Much, much smaller. The simplest possible way we could make these points. And we must be more funny than we are being."

**What v3 is:** 17 slides, about 3:17 spoken. Three pillars, one pass each, one diagram each, a meme straight after every diagram. It is built from six drafts and one harsh ranking (`design/2026-11-05-future-proof-meme-deck/v3-drafts/`). The **installer** draft is the spine, cut to the **ruthless** draft's size, with the **standup** draft's punchlines and a few lines grafted from the other three. The window and button text for each slide is in `v3-drafts/v3-layouts.md`.

**The look is locked: "Update Available".** Britain is an old computer that has clicked "Remind me later" since 1872. Every slide is a desktop with system windows on it, and the taskbar clock reads 1872 until the last slide.

**The one running gag.** An update called Democracy 2.0 has sat at 3% since 1872. Each time it is ready, the administrator (whoever is in charge that year, never Mel, never "the computer") clicks the default button, and that button gets longer at each pillar:
*Remind me later* (4) → *Remind me after the next election* (6) → *Remind me when it's someone else's problem* (10).
On 15 the button is greyed out ("You have used all your laters"), and the narrator turns out to be the reminder. On 17 the future removes the button, the bar reaches 4%, the clock ticks over to 1873, and the bus Mel has been waiting for turns up.

## Contents
1. Rules this deck runs on
2. Mel, the recurring voter
3. Main deck, slides 1-17 (open 1-4, pillar 1 5-6, pillar 2 7-10, pillar 3 11-13, close 14-17)
4. Appendix: six backup answers
5. Fact ledger: only the claims v3 uses
6. Image-source and legal
7. Timing, the two-minute cut, 9:16 picks
8. What changed from v2, and why
9. Open flags for Kai and Jack

---

## 1. Rules this deck runs on

- **One idea per slide, one pass per pillar.** No point is made twice: no "known issues" followed by "fixed in this version".
- **Every diagram is followed at once by a meme.** Three diagrams in all: pub (5→6), tower (8→9), letters (12→13).
- **The voter is never the butt.** The joke lands on the design or on the administrator, named by what they do ("whoever's in charge that year", "whoever built it"). The line that carries this rule is a joke, not a sermon: "It's working exactly as designed. That's the bug."
- **Never "the computer".** The pop-up text blames whoever designed or runs the system. "Only the administrator can install updates."
- **Software words come after the plain picture**, as a caption: the cookie banner first, "composition over inheritance" second.
- **Facts only from the ledger (section 5), status OK.** No five years, no 2029, no counts that will go stale, no small-ideas.org on the main deck.
- **Our own images, meme grammar.** Layouts are borrowed and pictures are never copied: no template characters, no real people, no project logos (names and URLs as plain text).
- **No party names, no Brexit and no referendum on a slide.** Referendums and PR are appendix answers.
- **Narrator register (docs/voice.md).** Sarcastic and certain, warm underneath. Short sentences that Kai can say live. There is one "I'm from later" reveal, on slide 15, and no other.
- **AI disclosure** lives in the voiceover or description (docs/using-ai.md), never on an apology slide.

## 2. Mel, the recurring voter

One invented, ordinary UK adult, with a mug, a dog, a bus stop where the 14 is always delayed, and one cross.

- Mel is calm, notices things and is never confused, shouted at or made the joke. No party, newspaper, flat cap or catchphrase. Mel's town is never named.
- Mel is a **standard user**, the one person in the deck who can see the problem and cannot install the fix. That is Mel's whole arc, in four appearances:
  - 1: in the booth, with one box that says EVERYTHING;
  - 4: the sticky note "who's the administrator?";
  - 10: at the bus stop, under "14: DELAYED", which plants the last joke;
  - 13: opening the tax letter on the doormat. Mel's last appearance is on 17, where the sticky now reads "...me?" and the 14 arrives.
- Character sheet (content only): adult, plain clothes, mug usually in hand, dog usually at their feet. One reference image, so the face and outfit are the same on every slide.

---

## 3. Main deck

Format per slide: **number · TYPE · seconds**, then Visual / On-screen / Say / Source. "Click:" in Say marks the punchline, which arrives on the click. "Say" is the narrator's line, for the recorded voice or for Kai live. Paths in "src" are inside `design/2026-11-05-future-proof-meme-deck/` unless stated.

### OPEN (1-4)

### 1 · meme · 7s
- **Visual:** Mel in a polling booth, mug in hand, holding a ballot with a single box. Printed beside the box: "EVERYTHING". The dog waits outside, its lead on the hook. An error box sits over the scene.
- **On-screen:** heading "Why can't I vote on more than one thing?" / click: "You have selected ONE (1) cross. Your cross will now be applied to: EVERYTHING." / buttons "OK" · "Also OK"
- **Say:** "Why can't I vote on more than one thing? Buses. Bins. Bills. One cross." Click: "And the cross does the rest."
- **Source:** framing, no fact. A UK general-election ballot is one cross for one candidate (common knowledge, no number).

### 2 · meme · 10s
- **Visual:** the "About this system" window every old computer has. Where the logo would be there is a small candle.
- **On-screen:** heading "Democracy, version 1872" / lines, one per click: "Parliament: 1200s" · "Secret ballot: 1872" · "Light bulb: not invented yet (1878)" / footer "Known issues: all of them." / bottom caption "OLDER THAN THE LIGHT BULB."
- **Say:** "Here's what you're running. Parliament: the twelve-hundreds. Secret ballot: 1872. The light bulb: 1878." Beat. "The way you pick a government is older than the light bulb."
- **Source:** ledger rows L1-L3 (OK). Say "1200s", never "760 years". Never "before electricity" (Faraday 1831).

### 3 · meme · 9s
- **Visual:** two windows side by side. Left: a smart bulb glowing, with a phone beside it that controls it. Right: the shelf in a polling booth, with a pencil tied to it on a string.
- **On-screen:** left "LIGHT BULB, since 1878: dimmable · 16 million colours · talks to your phone" / right "BALLOT, since 1872:" then, on the click, "a pencil. On a string."
- **Say:** "The light bulb's had a few updates since. It dims. It changes colour. It talks to your phone." Click: "The ballot got a pencil. On a string."
- **Source:** observation, not a statistic (smart bulbs and the polling-booth pencil are common knowledge). See flag 2.

### 4 · meme · 14s
- **Visual:** the setup screen for the new version, with a progress bar stuck at 3% (a cobweb in the corner of the bar). In front of it, the update nag: a padlock on "Restart now", and Mel's sticky note on the screen bezel.
- **On-screen:** behind: "DEMOCRACY 2.0 SETUP · 3 updates ready" and progress 3% "Installing... (since 1872)" / front: heading "Restart Britain to finish installing?" / buttons "Remind me later" · "Restart now" (greyed) / small "Only the administrator can install updates." / sticky (Mel) "who's the administrator?"
- **Say:** "Three updates. Stuck at three percent since 1872, because every time it's ready, somebody clicks..." Click: "...remind me later. Not you, Mel. You're a standard user. The administrator is whoever's in charge that year." Beat. "And they've got a lot on."
- **Source:** framing; the three updates are the three pillars (research/01-canon.md, L13). The blame goes on whoever holds the button, by their act; never the voter, never "the computer".

### PILLAR 1: VOTE ISSUE BY ISSUE (composition over inheritance) (5-6)

### 5 · diagram (three.js) · 13s
- **Visual:** the `pub` scene. Five people at a pub table (Mel is one), with "Sun party" and "Moon party" beer mats and three Sun policy cards hanging overhead. Phase 1: each card loses 3-2. Phase 2: everyone slides into party stacks, and Sun wins 3-2.
- **On-screen:** phase 1 "VOTE ON EACH POLICY: ALL THREE LOSE 3-2" / phase 2 "VOTE FOR THE PARTY: SUN PARTY WINS 3-2" / small "same five people. same opinions."
- **Say:** "Five people in a pub. The Sun party has three policies. Vote on each one: every one loses, three-two. Vote for the party: Sun wins, three-two. Same five people. Same opinions." Beat. "Slightly more pints."
- **Source:** L5 (Ostrogorski paradox, OK). The worked example is ours, checked by hand: three Sun voters each dislike a different policy, and the two Moon voters dislike all three. Invented parties only (sun and moon).

### 6 · meme · 16s
- **Visual:** a cookie-consent banner across Mel's ballot paper. On the second click a smaller update nag stacks on top of it.
- **On-screen:** heading "We value your democracy." / text "By voting, you accept all policies in this bundle, including the ones you can't stand." / buttons "Accept all" · "Accept all" / greyed link "Manage preferences (coming soon since 1872)" / click 1: bottom "IT'S WORKING EXACTLY AS DESIGNED. THAT'S THE BUG." / click 2, the nag: "Install 'Manage preferences'?" · buttons "Remind me after the next election" · "Install" · small "Note: the next election is also a bundle."
- **Say:** "Every website lets you untick the cookies. Your ballot: accept all, or accept all." Click: "It's working as designed. That's the bug. Software calls the fix composition over inheritance. You'd call it 'manage preferences'." Click: "Remind me after the next election." Beat. "Which is also a bundle."
- **Source:** lands slide 5. "Bundling" is a named concept (L4, OK). The joke is on the design and on whoever built it, never on the voter. Laters: 2 of 3.

### PILLAR 2: CHANGE IT SMALL, KEEP AN UNDO (continuous integration) (7-10)

### 7 · meme · 7s
- **Visual:** one huge red button on an otherwise empty desk. On the click, an error box stacks on top of it, with a frozen installer bar behind.
- **On-screen:** heading "Apply this law to EVERYONE, ALL AT ONCE?" / buttons "Yes" · "YES" / click: "Undo is not available for this action." with the bar label "Installing... please do not turn off your country."
- **Say:** "Here's how a law goes live. Everyone. All at once. Two buttons. Both yes." Click: "And there's no undo."
- **Source:** framing, explanatory (research/13 section 1, L6: "no green tick and no undo button"). No number. "Please do not turn off your country" is on screen only and is not spoken.

### 8 · diagram (three.js) · 15s
- **Visual:** the `tower` scene. Left: small bricks land one at a time, each lighting a green tick; one lights red and the undo arm lifts it straight out, and the tower stays standing. Right: a crane drops one monolith whole, with no ticks.
- **On-screen:** left "SMALL. CHECKED. UNDOABLE." / right "ONE DROP. NO TICKS."
- **Say:** "Software ships in small bricks. Tick. Tick. That one's wrong: lift it out, the tower's fine. Not move fast and break things. Move small, and keep the undo." Beat. "Politics drops the whole tower off a crane, then schedules a review."
- **Source:** L6 (the green tick, OK, explanatory). No deploy-rate figure. The trap guard ("not move fast and break things") is said aloud.

### 9 · meme · 12s
- **Visual:** a keyboard with Ctrl and Z glowing, beside a thick statute book with a sticky note on it: "UNDO?" Over both, the Edit menu with "Undo" greyed out.
- **On-screen:** heading "Undo is not available for this law." / text "Review: normally 3 to 5 years later." / small "Central record of whether that happened: none." / click: buttons "We'll look into it" · "OK"
- **Say:** "That review comes three to five years later. How many actually happen? The Lords were told: nobody keeps a central record." Click: "Your phone has Ctrl-Z. Your country has 'we'll look into it'."
- **Source:** L7 (Acts normally reviewed 3-5 years after enactment, OK); L8 (no central record, OK). No count of unreviewed Acts is claimed.

### 10 · meme · 12s
- **Visual:** two windows. Left: a bright room with a "TEST HERE FIRST" banner and little boxes of app icons. Right: Mel at a bus stop under a sign that reads "14: DELAYED", the timetable pinned to the post. On the second click the update nag appears again, with its longest button yet, which pushes "Install" against the edge of the window.
- **On-screen:** left "NEW MONEY APPS: a safe sandbox to test in first (since 2016)" / right "YOUR BUS TIMETABLE: straight to live" / click 1: bottom "TESTED ON YOU." / click 2, the nag: "Install 'test it first' everywhere?" · buttons "Remind me when it's someone else's problem" · "Install"
- **Say:** "And it can be done. Since 2016 the regulator has given new money apps a sandbox to test in first." Click: "Your bus timetable gets tested on you." Click: "Everywhere? Remind me when it's someone else's problem."
- **Source:** L9 (FCA sandbox, first cohort 7 Nov 2016, OK). Never "world first". The bus timetable is a joke, not a claim about any real timetable. This slide plants the 14 bus. Laters: 3 of 3.

### PILLAR 3: NO POLICY WITHOUT ITS EXPERIMENT (data-driven) (11-13)

### 11 · meme · 10s
- **Visual:** two windows. Left: a pill bottle trailing a long paper trial record, with a "CONTROL GROUP" sign. Right: a microphone on an empty lectern under a "TRUST US" banner (nobody at it).
- **On-screen:** left "A PILL: years of trials · a control group" · button "Prescribe" / right "A POLICY: a confident announcement" · buttons "Run on everyone" · "Run on everyone" / click: small print under the right window "Side effects may include: all of us."
- **Say:** "A pill gets years of trials before it's allowed in your bathroom cabinet. A policy gets a confident announcement." Click: "Side effects may include: all of us."
- **Source:** L10 (Test, Learn, Adapt, 2012: RCTs routine in medicine, rare in domestic policy, OK). "Run on everyone" is the button joke, not a claim that no policy is ever tested. No real person at the lectern.

### 12 · diagram (three.js) · 14s
- **Visual:** the `letters` scene. Two envelopes fan out and two bars rise: "plain letter" to 67.5%, "+ one line" to 79%. The tag on the taller bar reads "most people in your postcode have already paid".
- **On-screen:** caption "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID" / small "HMRC, overdue tax"
- **Say:** "The other way. HMRC wrote to people who owed tax. Plain letter: sixty-seven and a half percent paid. Add one line, 'most people in your postcode have already paid': seventy-nine." Beat. "Nobody passed a law. They tested a sentence."
- **Source:** L11 (OK for 67.5 vs 79 only). No variant count, no "best of", no sample size, no £ figure.

### 13 · meme · 6s
- **Visual:** Mel on the doormat opening a brown envelope, the dog looking up at it. A dialog sits over the letter.
- **On-screen:** heading "Most people in your postcode have already paid." / click: buttons "Pay" · "Move house" / bottom "PEER PRESSURE. NOW EVIDENCE-BASED."
- **Say:** "Your neighbours have paid. Two options." Click: "Peer pressure. Now evidence-based."
- **Source:** lands slide 12; no new fact.

### CLOSE (14-17)

### 14 · meme · 11s
- **Visual:** release notes for the version nobody has installed. Three lines, and that is the whole talk.
- **On-screen:** heading "DEMOCRACY 2.0: what's new" / one per click: "1. Vote issue by issue, not one bundle." · "2. Change laws small. Check them. Keep an undo." · "3. No policy without its experiment." / footer "Download size: smaller than one manifesto."
- **Say:** "So that's the update. Vote issue by issue. Change laws small, check them, keep an undo. No policy without its experiment." Click: "Download size: smaller than one manifesto."
- **Source:** canon, the three tenets (research/01-canon.md, L13).

### 15 · meme · 13s
- **Visual:** the nag from slide 4, one last time. "Remind me later" is greyed out. Mel's cursor drifts toward "Install now". On the second click a toast pops in: "Reminder from: later."
- **On-screen:** heading "Remind me later?" / small "You have used all your laters. (154 years of them.)" / buttons "Install now" · "Remind me later" (greyed) / click: toast "Reminder from: later. It's later."
- **Say:** "Every time, somebody clicked remind me later. Well. Hello. I'm from later." Click: "I've seen how it ends when nobody installs it. I am the reminder. And I'd quite like you lot to make it."
- **Source:** canon framing: the narrator is the superintelligence from the bad branch (research/01-canon.md, L13). This is the deck's only "where I'm from". 154 = 2026 minus 1872 (L2, our arithmetic).

### 16 · meme · 16s
- **Visual:** the desktop wallpaper, with notifications stacking fast in the bottom right, one per click.
- **On-screen:** wall "PARTIAL UPDATES FOUND NEARBY" / small "other people are already rethinking this. thousands more: participedia.net" / toasts:
  - "Sortition Foundation · jury service, but for the bin collection · sortitionfoundation.org"
  - "PB Scotland · the council's actual money, voted on in a village hall · pbscotland.scot"
  - "FixMyStreet · somebody gave the country a bug tracker · fixmystreet.com"
  - "TheyWorkForYou · how your MP voted, issue by issue · theyworkforyou.com"
  - "What Works Network · nine centres that check what works · gov.uk/guidance/what-works-network"
  - "Pol.is · in Taiwan, an argument about Uber went from four camps to two · pol.is"
- **Say:** "Somebody's had the mouse since 1872. Ask for a go. Other people already are. Jury service, for the bins. Council money, voted on in a village hall. A bug tracker for potholes. How your MP voted, issue by issue. In Taiwan, four camps became two. Go and look."
- **Source:** L12 (explore-directory.md #2, #3, #6, #9, #11, #14, all checked live 2026-11-05, OK) and L14 (Pol.is four camps to two only, OK; no participant counts, no claim about what the government did). Participedia appears as "thousands", with no count. small-ideas.org is left off (GATE). Names and URLs as plain text, no logos.

### 17 · title · 12s
- **Visual:** the setup screen from slide 4, with the nag in front of it. "Remind me later" is struck through and labelled "(button removed by the future)". Mel's sticky now reads "...me?". The bar moves from 3% to 4%, the taskbar clock ticks from 1872 to 1873, and one last toast arrives.
- **On-screen:** heading "DEMOCRACY 2.0" / buttons "Install now" · "~~Remind me later~~" / small "(button removed by the future)" / sticky "...me?" / click 1: progress 3% → 4% "Installing... (fastest it's moved since 1872)" / click 2: clock 1872 → 1873 / click 3: toast "Bus 14: arriving (unrelated)"
- **Say:** "So I've taken the liberty of removing a button." Click: "Four percent. Don't laugh. Fastest it's moved since 1872." Click: "Ooh. Eighteen seventy-three. We're moving." Click: "...Unrelated."
- **Source:** callbacks to 4, 10 and 15; no new fact. The `clock` override is the one deliberate clock gag the look allows. `badcode.tv/future-proof` is not printed until it is live (flag 7).

---

## 4. Appendix: six backup answers

These are not in the three minutes. Each is a one-slide answer for a raised hand, or a slot in a longer web version. Every one is a meme and is written in the narrator's voice.

### A1 · "So, referendums?"
- **Visual:** two doors: "ASK OFTEN, ON SMALL THINGS" and "ONE GIANT VOTE, ONCE, ON EVERYTHING". Mel takes the first one.
- **Say:** "No. One enormous yes-or-no on everything is just a bundle with a bigger box. We mean small questions, asked often, starting where the stakes are low. Paper stays for the big ones."
- **Source:** research/21 (advisory first; start low-stakes). Never name a real referendum.

### A2 · "Can't we just vote on our phones?"
- **Visual:** a ballot box with a padlock next to a phone with a question mark on it. Mel holds the paper ballot.
- **Say:** "Not yet, and I say that as a computer. Voting in secret, securely, from a phone is a hard problem nobody has cracked. Estonia shows people will use it. It doesn't prove it's safe. You can vote on more things without voting on your phone."
- **Source:** research/21 (Schneier 2026; LSE). No Estonia percentage, and no claim about Estonia's security or its effect.

### A3 · "Isn't this just common sense?"
- **Visual:** a bug ticket. "FEATURE: take teenagers round a prison to scare them off crime" / "Status: SOUNDED GREAT" / "Tested by: 9 controlled trials" / "Result: MORE REOFFENDING" (highlighted). The attachment is named `scared_straight_final_FINAL.jpg`.
- **Say:** "Scared Straight. Walk teenagers round a prison and frighten them off crime. The people running it were sure. Nine controlled trials later: more reoffending, not less. Common sense is a guess with good posture."
- **Source:** L15 (Petrosino et al. 2013, OK). It names who was sure by their act. The test is neutral and kills ideas from every side, so the tough-on-crime viewer stays with us. This is the first slide back into the main deck if there's time (after 13).

### A4 · "Why not just proportional representation?"
- **Visual:** a ballot box wrapped in a tangled sign. Mel declines it politely.
- **Say:** "Different argument, and a party fight. Ours is smaller and stranger: you choose each thing, not the package. You can want both."
- **Source:** research/20. Q&A only: never lead with PR, and never quote PR polling on a slide.

### A5 · "Where does AI sit in all this?"
- **Visual:** a laptop pointed at a spread of opinions; a named person holds the pen.
- **Say:** "Coming from me, this is rich. AI can help sort a few thousand opinions into a map of where people agree. It decides nothing. A named person signs, and somebody checks their work."
- **Source:** research/21 (Habermas Machine, Science 2024; Anthropic CCAI). Early and small: no numbers.

### A6 · "Does anywhere actually vote issue by issue?"
- **Visual:** a ballot paper with several boxes next to a calendar with several dates circled.
- **Say:** "Yes. Some countries vote on questions one at a time, several times a year. The results go every which way. That's what happens when you ask people."
- **Source:** L16 (admin.ch, OK, no number). Switzerland's voting-day count is CHECK, so no count is given.

---

## 5. Fact ledger (only the claims v3 uses)

Status as in v2: OK = sourced in research; CHECK = needs a primary before it leaves draft; GK = general knowledge. The "v2 row" column points to `history/deck-v2.md` section 5.

| # | Claim | Used on | Source (file + URL) | Status | v2 row |
| --- | --- | --- | --- | --- | --- |
| L1 | De Montfort parliament 1265 (said "1200s") | 2 | research/15; https://www.parliament.uk/demontfort/ | OK (label contested; say "1200s") | 3 |
| L2 | Secret ballot 1872 (Ballot Act); "154 years" = 2026 minus 1872 | 2, 4, 15, 17 | research/15; https://en.wikipedia.org/wiki/Reform_Acts | OK (S) | 3, 4 |
| L3 | Swan lamp Dec 1878 | 2, 3 | research/15; https://gracesguide.co.uk/Electric_Lighting | OK (S) | 3 |
| L4 | "Bundling" is a named concept | 6 | https://en.wikipedia.org/wiki/Bundling_(public_choice) | OK (S) | 11 |
| L5 | Ostrogorski paradox: voting bundled vs issue by issue can reverse the result | 5 | https://www.newamerica.org/insights/the-paradoxical-reason-republicans-win-elections-despite-unpopular-policies/ ; https://arxiv.org/abs/2307.11873v1 | OK; example is ours, hand-checked | 13 |
| L6 | The "green tick" explanation (software checks each change; it can be rolled back) | 7, 8 | research/13 section 1 | OK (explanatory) | 19 |
| L7 | Acts normally reviewed 3-5 years after enactment | 9 | https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament | OK (S) | 20 |
| L8 | No central record of post-legislative reviews (Lords written answer) | 9 | https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny | OK (Hansard mirror) | 21 |
| L9 | FCA sandbox: first cohort 7 Nov 2016 | 10 | https://www.crowdfundinsider.com/2016/11/92162-first-class-fca-reveals-24-fintech-firms-accepted-regulatory-sandbox/ | OK (S); never "world first" | 24 |
| L10 | RCTs routine in medicine, rare in domestic policy | 11 | https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials | OK (P) | 26 |
| L11 | HMRC: control letter 67.5% paid, postcode-norm line 79% | 12, 13 | https://thedecisionlab.com/intervention/how-normative-messaging-increased-tax-compliance-by-15 ; https://blogs.worldbank.org/voices/ongoing-impact-nudging-people-pay-their-taxes | OK for 67.5 vs 79 only | 27 |
| L12 | Sortition Foundation, PB Scotland, FixMyStreet, TheyWorkForYou, What Works Network ("nine centres"), Pol.is, Participedia ("thousands"): URLs and one-liners | 16 | explore-directory.md #2, #3, #6, #9, #11, #13, #14 (checked live 2026-11-05) | OK; dates and counts perishable (no count printed) | 40-54 |
| L13 | The three tenets; the narrator is the AI from the finished bad branch | 4, 14, 15 | research/01-canon.md | OK (canon) | 55, 57 |
| L14 | vTaiwan / Pol.is on Uber: four camps collapsed to two | 16 | https://scrapbox.io/nishio-en/How_the_discussion_on_Uber_has_evolved_in_vTaiwan ; https://eprints.soton.ac.uk/496942/1/Sorting_a_Public_2023_AAM.docx | OK for four-to-two camps only | 37 |
| L15 | Scared Straight: 9 randomised trials, harmful effect (appendix only) | A3 | https://ideas.repec.org/a/wly/camsys/v9y2013i1p1-55.html | OK (P abstract) | 28 |
| L16 | Some countries vote issue by issue (appendix only, no number) | A6 | https://www.admin.ch/gov/en/start/documentation/votes.html | OK (no number) | 15 |
| L17 | Polling-booth pencil on a string; smart bulbs dim, change colour, pair with a phone | 3 | observation | GK (not in the v2 ledger; flag 2) | none |

**Not used, and why:** "five years" / "2029" / "every five years" (v2 row 2, 6: CHECK, which killed the best joke in the pile, flag 1); "before electricity" (false); "760 years"; 1832 and 1928 (true, but cut so that the About box has three lines); the iPhone "nineteen" (GK); public voting before 1872 (CHECK); Frome (CHECK); poll tax (CHECK); sewage (CUT-IF); Troubled Families and Horizon (cut for length; Horizon's victims are real, and a comedy installer is the wrong room for them); petitions; small-ideas.org (GATE); Participedia's "2,400 / 160 countries" (perishable); "Pol.is: where the other side secretly agrees with you" (goes beyond L14); HMRC variant counts, sample sizes and £.

## 6. Image-source and legal

- Every picture is **original** (generated fresh, with a recipe card and the same-prompt check), in meme grammar: layouts are borrowed, never template images or characters, and no real people. Mel is one invented character with one reference image.
- Nothing impersonates a real organisation. The windows are a made-up OS: no real OS chrome, logo, typeface or sounds, no GOV.UK crown or colours, and no HMRC or FCA branding. The fake "Windows Update" naming in the drafts is **not** used: the title bar says "Update Available" or "Democracy 2.0 Setup" (see `v3-layouts.md`).
- Named real bodies (HMRC, the FCA, the Lords) appear only as facts about public acts. They are cited and never mocked as people.
- The project toasts on slide 16 use names and URLs as plain text, with no logos.
- No film, TV or pop music under any slide. Any score is our own, per the story's sound.md. Do not rely on UK fair dealing (research/19).

## 7. Timing, the two-minute cut, 9:16 picks

- **Scripted runtime: 197s (3:17)**, 17 slides. Per slide: 7 + 10 + 9 + 14 + 13 + 16 + 7 + 15 + 12 + 12 + 10 + 14 + 6 + 11 + 13 + 16 + 12. By section: open 40s, pillar 1 29s, pillar 2 46s, pillar 3 30s, close 53s. The spoken script is about 520 words at a brisk 2.8 words a second, plus about a second on each click and beat.
- **Diagrams: 3** (pub 5, tower 8, letters 12), each followed at once by a meme (6, 9, 13). Memes: 13. Title: 1 (17, which is a boot screen).
- **Live:** with laughs it runs about 3:45 to 4:00 on a stage. Kai can say every line as written. The one aside to keep for live is "Not you, Mel" on 4, where the room should laugh with Mel, not at the screen.
- **If it must come in under 3:00 (about 177s):** cut 3 (the pencil, 9s), cut 7 (Yes/YES, 7s; the tower then opens pillar 2) and cut 16 down to four toasts (Sortition, PB Scotland, FixMyStreet, TheyWorkForYou; about 4s).
- **Two-minute cut (10 slides, about 120s):** 1, 2, 4, 5, 6, 8, 12, 13, 15, 17. It drops the pencil, Yes/YES, Ctrl-Z, the sandbox (and with it the bus plant, so the last toast on 17 changes to "Update 1 of 3: started"), the pill, the release notes and the montage. The montage goes into the description. Slide 8 still ends on "then schedules a review".
- **9:16 shorts (one slide, or a pair):**
  - 2 + 3, "older than the light bulb / a pencil on a string" (19s);
  - 6, the cookie banner (16s);
  - 9, "Your phone has Ctrl-Z" (12s);
  - 12 + 13, "they tested a sentence / move house" (20s);
  - 15 + 17, "I am the reminder" and the 4% button (25s).
- **Montage-only short:** 16 on its own, extended to v2's 15 stops (`history/deck-v2.md` slides 40-54, with no small-ideas.org until it is verified), about 60s.

## 8. What changed from v2, and why

1. **58 slides → 17; 8:41 → 3:17.** Kai: "far too long... much, much smaller." Each pillar now gets one diagram, one meme and at most two more slides. v2 gave pillar 1 ten slides; v3 gives it two.
2. **8 diagrams → 3.** Kept: pub, tower, letters (one per pillar). Cut from the main deck: timeline (the About box does its job in one window), slab, towns, pipe, dots, tokens.
3. **One running gag instead of many objects.** v2 told the bundle joke with a new object on every slide (receipt, package, crate, album, pizza). v3 tells it once, with the one object everyone in the room has clicked this week: a cookie banner. The OS look now carries the jokes instead of decorating them, through the button that grows at each pillar, the 3% bar and the 1872 clock.
4. **Funnier: setup on the slide, punchline on the click.** Most slides end on a click line: "And the cross does the rest", "A pencil. On a string", "Slightly more pints", "That's the bug", "Your country has 'we'll look into it'", "Side effects may include: all of us", "Peer pressure. Now evidence-based", "Smaller than one manifesto", "Unrelated".
5. **Built from six drafts and a ranking** (`v3-drafts/ranking.md`). The spine is installer's. The size is ruthless's. The punchlines are mostly standup's. Grafts: the cookie banner (ruthless), "That's the bug" and "Ask for a go" (customer-support), the pencil on a string and "do not turn off your country" (patch-notes), Bus 14 and the 1873 clock (mel-day).
6. **The judge's condemned lines are all out:**
   - every "five years";
   - "first update since the light bulb";
   - "Bless you for asking";
   - "You'll laugh, then you'll want them";
   - "Democracy v1832" and "turning it off and on again";
   - "Nobody has ever answered it";
   - "Somebody built the box that way. Wasn't Mel.";
   - "Works on my machine";
   - "A computer can summarise";
   - "Waiting on customer";
   - the Participedia counts;
   - "the other side secretly agrees";
   - the receipt's "thing you hate x6";
   - the earnest ending;
   - every repeat "where I'm from".
7. **Where v3 departs from the judge's spine, and why:**
   - Scared Straight moves to the appendix (A3), as the judge allowed: it is the first slide to come back if there's time.
   - "You call it pizza" became "You'd call it 'manage preferences'", because the pizza is cut and the banner sets up its own callback.
   - "Ask for a go" opens the montage instead of closing the deck, so the last laugh stays with the bus.
   - The clock ticks to 1873, not to today (mel-day's version is funnier, and it is honest: one step).
   - The About box loses 1832 and 1928, leaving three lines in a rule of three.
   - Participedia moves into the montage's wallpaper line, so six toasts plus "thousands more" lists seven places in the time of six.
   - Mel's sticky "who's the administrator?" (4) is called back as "...me?" (17), which is new in v3 (flag 3).
8. **The close is the rule-one ending Kai asked for:** other people are already rethinking this, go and look. It is one slide of six projects instead of fifteen 5-second stops. "Write one rule" (v2 56) and "the good branch isn't written" (v2 55) are cut, because each was a second ending.
9. **No Layout lines in deck.md.** The layouts, window titles and button text are in `design/2026-11-05-future-proof-meme-deck/v3-drafts/v3-layouts.md`, for the dresser.

## 9. Open flags for Kai and Jack

1. **Five years.** If parliament.uk confirms the five-year maximum (v2 row 2/6, CHECK), the best joke in the pile can come back on slide 4 or 6: "Have you tried turning it off and on again?" / "We only get to do that every five years." / "Brilliant. So it's working." (customer-support draft). Until then it stays out.
2. **The pencil on a string (3)** is an observation, not a ledger fact. It is common in polling booths but not universal. If you'd rather not risk a "well, mine was chained" heckle, the fallback is "The ballot got... a pencil." That keeps the joke and loses the string.
3. **Mel's "...me?" sticky (17).** Mel's ask is meant as an invitation (ask for a go), not blame: the fault was put on the administrator on slide 4. Cut it if it reads as homework for the viewer.
4. **The theme's `link` layout** prints a "Remind me in 5 years" button, which rests on the same CHECK fact. v3 doesn't use `link`, but the dresser should not bring it back for the montage.
5. **"154 years"** assumes the talk is given in 2026. In 2027 it becomes 155 (slide 15).
6. **Who speaks.** Every line works from Kai's mouth. Slide 15 is the one moment that needs the "I'm from later" register. Live, Kai can play it straight or point at the screen and let the recorded voice take it.
7. **`badcode.tv/future-proof`** is intended, but deployment is unverified. It is not printed until it is live.
8. **Mel casting:** one reference image, to be approved before any generation (still gate).
9. **The pub example (5)** rests on our hand-checked numbers. If someone asks for it after the talk, the worked table is in `history/deck-v2.md` slide 13's source line.
