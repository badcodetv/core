# Future Proof: v3 draft, shape RUTHLESS MINIMUM

**Pitch.** Thirteen slides, about 2:50 spoken. A five-minute pub talk from someone very sure, and the pub is Britain's old computer.
Each pillar gets one diagram, one meme and one killer line, and nothing that explains. The cold open folds the light-bulb timeline into the first release-notes joke, so the deck uses three diagrams, all in the pillars.
The OS gag runs all the way through: every box has two buttons that say "Remind me later", the boot is stuck at 3%, the man from the future says he is the reminder, and at the end Mel clicks Install and the bar moves to 4%.

Departures from v2 (deliberate): the timeline becomes a meme, not a diagram (it saves a slide and keeps the three diagrams for the pillars). The montage becomes ONE slide of six projects. Cut: Mel's profile card, bank/ballot, receipt, package, crate, album, ballot-box, Frome, pizza, pilot, poll tax, sewage, sandbox, Scared Straight, Troubled Families, Horizon, the label, the towns, petitions, Pol.is, judgement, the good branch, and the 15-stop montage. "Five years" and "2029" are never said or printed (ledger status CHECK), and neither is any "Remind me in 5 years" button.

---

### 1 · meme · 9s
- **Visual:** Mel in a polling booth, mug in hand, holding a ballot with one box. The word printed beside the box is "EVERYTHING". The dog waits outside.
- **On-screen:** heading "Why can't I vote on more than one thing?" / buttons "Remind me later" · "Remind me later"
- **Say:** "Why can't I vote on more than one thing? Brilliant question. Whoever runs the place has given the same answer since 1872."
- **Source:** framing, no fact. A UK ballot is one cross for one candidate (common knowledge).
- **Layout:** `dialog`, title "Democracy (1872 edition)", icon `question`, image of Mel in the booth on the left, both buttons "Remind me later" (they arrive on a click: that is the punchline).

### 2 · meme · 17s
- **Visual:** a changelog window over the desktop, with a light bulb icon on the 1878 line.
- **On-screen:** "BRITAIN v1872 CHANGELOG" / 1200s Parliament · 1832 Reform Act · 1872 Secret ballot · 1878 Light bulb (someone else's) · 1928 Last big patch / footer "Known issues: all of them." / bottom caption "OLDER THAN THE LIGHT BULB"
- **Say:** "Here's the changelog. Parliament: the twelve hundreds. The Reform Act: 1832. The secret ballot: 1872. Then in 1878 somebody invents the light bulb. The way you pick a government is older than the light bulb. Last big patch: 1928. Known issues: all of them."
- **Source:** v2 ledger, all OK: 1265 de Montfort (say "1200s"), https://www.parliament.uk/demontfort/ ; 1832 and 1872, https://en.wikipedia.org/wiki/Reform_Acts ; Swan lamp Dec 1878, https://gracesguide.co.uk/Electric_Lighting ; 1928 Equal Franchise Act (research/15). Never "before electricity". Nothing dated after 1878 sits on the "older than" side except the 1928 patch, which is shown as a patch.
- **Layout:** `release`, title "Release notes", `lines` as year/label pairs revealed one per click (the bulb line last but one), footer "Known issues: all of them.", buttons "Remind me later" · "Remind me later", `bottom` caption "OLDER THAN THE LIGHT BULB" on the 1878 click.

### 3 · title · 6s
- **Visual:** a boot screen.
- **On-screen:** "FUTURE PROOF" / "Installing 3 updates politics never installed" / progress bar 3%, label "stuck since 1872"
- **Say:** "Future Proof. Three updates. Three minutes. Let's get it off three percent."
- **Source:** canon, research/01-canon.md (the three tenets).
- **Layout:** `title`, heading "FUTURE PROOF", sub "Installing 3 updates politics never installed", `progress` {pct: 3, label: "3% · stuck since 1872"}.

### 4 · diagram (three.js) · 17s
- **Visual:** the `pub` scene. Five people at a table (Mel is one), "Sun party" and "Moon party" beer mats, three Sun policy cards overhead. Phase 1: each card loses 3-2. Phase 2: everyone goes into party stacks and Sun wins 3-2.
- **On-screen:** phase 1 "EVERY POLICY LOSES 3-2" / phase 2 "THE PARTY WITH ALL THREE WINS 3-2" / small "same five people. same pints."
- **Say:** "Five people in a pub. The Sun party has three policies. Vote on each one and every one of them loses, three-two. Vote for the party and the Sun party wins, three-two. Same people. Same pints. All that changed was the ballot."
- **Source:** our worked example, hand-checked (v2 slide 13): the Ostrogorski paradox, https://www.newamerica.org/insights/the-paradoxical-reason-republicans-win-elections-despite-unpopular-policies/ ; https://arxiv.org/abs/2307.11873v1. Ledger OK. The parties are invented objects (sun/moon), not real parties.
- **Layout:** `diagram`, title "pub.sim", scene `pub`, caption "Same five people. Two ballots.", small "same opinions, same pints", steps 2.

### 5 · meme · 14s
- **Visual:** a cookie-consent banner across Mel's ballot. Mel in the corner, mug up, one eyebrow raised.
- **On-screen:** heading "We value your democracy." / text "By voting, you accept all policies in this bundle, including the ones you can't stand." / buttons "Accept all" · "Accept all" / greyed link "Manage preferences (coming soon since 1872)"
- **Say:** "Every website on earth lets you untick the cookies. Your ballot says accept all, and whoever built it gave you two buttons that say the same thing. Software calls the fix composition over inheritance. Mel calls it: let me pick."
- **Source:** lands slide 4. Named concept "bundling", https://en.wikipedia.org/wiki/Bundling_(public_choice) (ledger OK). The joke is on the designer, by act ("whoever built it").
- **Layout:** `dialog`, title "Your vote: cookie settings", icon `info`, image of Mel on the left, buttons "Accept all" · "Accept all", `small` "Manage preferences (coming soon since 1872)".

### 6 · diagram (three.js) · 15s
- **Visual:** the `tower` scene. Left: small bricks go on one at a time, each gets a green tick, one goes red and the undo arm lifts it clean out. Right: a crane drops one monolith, with no ticks.
- **On-screen:** left "SMALL. CHECKED. UNDOABLE." / right "ONE DROP. NO TICKS."
- **Say:** "Software changes things in small pieces. Every piece gets checked. If one fails, the undo arm lifts it straight back out. That's not move fast and break things. It's move small, check, and take it back. Politics drops the whole tower in one go and hopes."
- **Source:** research/13 section 1 (the green tick, roll back), ledger OK (explanatory). No deploy-rate number. The trap guard ("not move fast and break things") is said aloud.
- **Layout:** `diagram`, title "build.log", scene `tower`, caption "Two ways to build", small "one has an undo", steps 2.

### 7 · meme · 15s
- **Visual:** a keyboard with Ctrl and Z glowing, beside a thick statute book with a sticky note on it: "UNDO?"
- **On-screen:** heading "Undo is not available for this law." / text "A review is normally due 3 to 5 years later." / small "Central record of whether that happened: none. (Lords written answer)" / buttons "We'll look into it" · "Remind me later"
- **Say:** "Every app on your phone has undo. A law gets a review three to five years later. Ask how many of those reviews actually happen and a written answer in the Lords says nobody keeps a central record. Your phone has Ctrl-Z. Your country has 'we'll look into it'."
- **Source:** reviews normally due 3 to 5 years after enactment, https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament (OK); no central record of post-legislative reviews, https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny (OK). No count of unreviewed Acts is claimed.
- **Layout:** `dialog`, title "Edit", icon `warn`, image of keyboard and statute book on the left, buttons "We'll look into it" · "Remind me later".

### 8 · diagram (three.js) · 14s
- **Visual:** the `letters` scene. Two envelopes fan out and two bars rise: "plain letter" 67.5%, "+ one line" 79%. The tag on the tall bar reads "most people in your postcode have already paid".
- **On-screen:** "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID" / small "HMRC, overdue tax"
- **Say:** "HMRC sent a plain letter to people who owed tax. Sixty-seven and a half percent paid. They added one line: most people in your postcode have already paid. Seventy-nine percent. Nobody passed a law. Somebody tested a sentence."
- **Source:** https://thedecisionlab.com/intervention/how-normative-messaging-increased-tax-compliance-by-15 ; https://blogs.worldbank.org/voices/ongoing-impact-nudging-people-pay-their-taxes . Ledger OK for 67.5 vs 79 only: no variant count, no "best of", no sample size, no £ figure.
- **Layout:** `diagram`, title "letters.xls", scene `letters`, caption "Same letter. One extra line.", small "HMRC, overdue tax", steps 2.

### 9 · meme · 14s
- **Visual:** two windows side by side. Left: a pill bottle with a long paper trail and a "CONTROL GROUP" sign. Right: a megaphone over a map with an "IT'LL WORK, TRUST US" banner.
- **On-screen:** left "PILL" / "Years of trials. A control group." / button "Prescribe" · right "POLICY" / "A confident announcement." / buttons "Run on everyone" · "Run on everyone" / bottom caption "NO POLICY WITHOUT ITS EXPERIMENT"
- **Say:** "A pill gets years of trials before it goes in your bathroom cabinet. A policy gets a confident announcement and runs on everyone. No policy without its experiment. If they can test a sentence, they can test a law."
- **Source:** RCTs are routine in medicine and rare in domestic policy, "Test, Learn, Adapt" (Cabinet Office / BIT 2012), https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials (ledger OK). "Run on everyone" is the button joke, not a claim that no policy is ever tested.
- **Layout:** `split`, left {title "pill.exe", image of the pill, heading "Years of trials. A control group.", buttons ["Prescribe"]}, right {title "policy.exe", image of the megaphone, heading "A confident announcement.", buttons ["Run on everyone", "Run on everyone"]}, `bottom` "NO POLICY WITHOUT ITS EXPERIMENT" on the second click.

### 10 · meme · 8s
- **Visual:** a "Tip of the day" card, with Mel's mug in the small image slot.
- **On-screen:** "1. Vote on each thing." / "2. Change small. Keep an undo." / "3. Test it before it runs on everyone."
- **Say:** "So. Three updates. Vote on each thing. Change small and keep an undo. Test it before it runs on everyone."
- **Source:** canon, research/01-canon.md. Callback to slide 9's button.
- **Layout:** `card`, title "Tip of the day", icon `info`, three `lines` (one per click), small image of Mel's mug.

### 11 · meme · 12s
- **Visual:** the full blue crash screen. The 1872 clock is still in the corner.
- **On-screen:** code "FUTURE_BRANCH_FAILED" / big "Where I'm from, the people in charge kept clicking 'Remind me later'." / text "Hi. I'm the reminder." / footer "Press any key to change the story"
- **Say:** "Where I'm from, the people in charge kept clicking remind me later. We finished that version, and I've seen how it ends. So, hi. I'm the reminder. I came back because I'd quite like you to make it."
- **Source:** canon framing (BadCode's future, CLAUDE.md / docs/vision.md; "the bad branch is finished", research/01-canon.md, ledger OK). This is the deck's one "where I'm from". The blame goes on the people in charge, never the voter or the machine.
- **Layout:** `fatal`, code "FUTURE_BRANCH_FAILED", big "Where I'm from, the people in charge kept clicking 'Remind me later'.", text "Hi. I'm the reminder." (on a click), footer "Press any key to change the story".

### 12 · meme · 17s
- **Visual:** an "Available updates" order summary, with Mel ticking the list over a mug.
- **On-screen:** "6 UPDATES AVAILABLE (written by other people, already)" / Sortition Foundation, jury service for the bin collection, sortitionfoundation.org · PB Scotland, the council's money and a ballot box, pbscotland.scot · CONSUL, free software for your council, consuldemocracy.org · TheyWorkForYou, how your MP actually voted, theyworkforyou.com · What Works Network, nine centres that check what works, gov.uk/guidance/what-works-network · Participedia, thousands of democratic experiments, participedia.net / footer "None of these are us. Go and look."
- **Say:** "Good news. Other people are already rethinking this. Jury service, but for the bin collection. A village hall, a ballot box and the council's actual money. Free software your council could copy. How your MP actually voted. Nine centres that check what works. Thousands of experiments. Pause it, open a tab, go and look."
- **Source:** explore-directory.md #2, #3, #5, #9, #11, #13 (checked live 2026-11-05; ledger OK). "Nine centres" exactly as on gov.uk. Participedia shows 2,442 cases (5 Nov 2026), so the slide says "thousands" and prints no count. small-ideas.org is left out (GATE). No logos, names and URLs as plain text only.
- **Layout:** `list`, title "Windows Update for Britain", heading "6 updates available", `rows` [name and one line, url] revealed one per click, `total` ["Written by", "other people, already"], footer "None of these are us. Go and look."

### 13 · meme · 10s
- **Visual:** the last box. Mel's cursor is on "Install now" and the bar has just ticked from 3% to 4%. The taskbar clock now shows today's date, not 1872.
- **On-screen:** heading "Update Britain?" / text "You're not gambling by changing the system. You're gambling by keeping it." / buttons "Install now" · "Remind me later" / progress 4% / sticky "Mel: already clicked it."
- **Say:** "You're not gambling by changing the system. You're gambling by keeping it. Mel's already clicked. Four percent. It's a start."
- **Source:** canon line, research/01-canon.md (ledger OK). This is the button: "Install now" is the default for the first time in the deck, the 3% boot bar is called back, and the clock gag pays off.
- **Layout:** `dialog`, title "Update available", icon `ok`, buttons "Install now" (default, outlined) · "Remind me later", `progress` {pct: 4, label: "Installing update 1 of 3"}, `sticky` "Mel: already clicked it." on the last click, `clock` set to today (the one deliberate clock override).

---

**Total: 168 seconds (2:48), 13 slides, 3 diagrams (pub, tower, letters), every one followed at once by a meme.**

Facts on the main deck, all OK in the v2 ledger: 1200s / 1832 / 1872 / 1878 / 1928, bundling, the pub paradox, the 3 to 5 year review, no central record, HMRC 67.5 → 79, RCTs in medicine vs policy, the six directory projects, and the canon lines. Not used: five years / 2029, iPhone, public voting before 1872, Frome, poll tax, sewage, small-ideas.org.
