# Future Proof v3 draft: MEL'S DAY

**Pitch.** One day. Mel tries to fix three ordinary things (the bus at 7am, the bins at 9am, the bills at noon), and each errand hits one design flaw, worse than the last, until the country blue-screens at 6pm.
**The turn.** An "Update available: 3 patches" box arrives, and the three pillars ARE the patches, each one fixing one of Mel's errands by callback (the bus = vote on the thing, the bins = keep an undo, the bills = test the sentence).
**The button.** Mel clicks Install, it sticks at 3%, the taskbar clock ticks from 1872 to 1873, and the 14 bus finally turns up ("unrelated").

Format as v2: number · TYPE · seconds, then Visual / On-screen / Say / Source, plus Layout. The taskbar clock carries Mel's time of day beside the year ("07:14 · 1872") as a deliberate `clock` gag; the year stays 1872 until the last slide. Facts are only v2 ledger rows marked OK. Things I left out on purpose: "five years" and "2029" (CHECK), "voted out loud" (CHECK), the iPhone (GK), Frome, poll tax, sewage, small-ideas.org.

---

### ACT 1: THE DAY (1-8)

### 1 · meme · 8s
- **Visual:** Mel at a bus stop in the rain, 7:14am, mug in hand, dog under the bench. The timetable panel reads "14: DUE", with DUE scribbled out.
- **On-screen:** top "WHY CAN'T I VOTE ON MORE THAN ONE THING?"
- **Say:** "Why can't I vote on more than one thing? Mel asked that at a bus stop at quarter past seven, in the rain. Let's follow Mel's day."
- **Source:** framing, no fact.
- **Layout:** `picture` (mel-busstop.jpg) with a `side` dialog "Bus 14: Delayed" and two buttons "OK" / "Also OK"; clock "07:14 · 1872".

### 2 · meme · 13s
- **Visual:** a release-notes window over Mel's phone screen. No picture needed.
- **On-screen:** "BRITAIN OS: RELEASE NOTES" · 1265 Parliament (beta) · 1832 Reform Act · 1872 Secret ballot · 1878 Somebody invents the light bulb · footer "Your voting system is older than the light bulb."
- **Say:** "Parliament: the twelve hundreds. Reform Act: 1832. Secret ballot: 1872. The light bulb: 1878. The way you pick a government is older than the light bulb. That's why the clock says 1872: somebody keeps clicking 'remind me later'."
- **Source:** ledger rows 3 (1265, say "1200s"; 1832; 1872; Swan Dec 1878), all OK. research/15. Never "before electricity". The "remind me later" line is the OS gag aimed at whoever kept clicking it, not a claim that nothing changed.
- **Layout:** `release` titled "Britain OS 1872: what's new", `lines` as [year, change] pairs revealed one per click, buttons "Remind me later" / "Remind me later" (identical, the first outlined as the default). This hook replaces the `timeline` scene so the deck keeps all three diagram slots for the pillars.

### 3 · meme · 9s
- **Visual:** Mel's cursor hovering over a ballot.
- **On-screen:** heading "Select the issues you'd like to vote on:" with one ticked box: "[x] EVERYTHING (this option cannot be unticked)"
- **Say:** "Mel wants a better bus. The ballot has one box. It says 'everything'. Mel ticks it for the bus. The box says: lovely, that's everything."
- **Source:** framing (UK ballot is one cross for one candidate). The joke is on whoever built the box.
- **Layout:** `dialog` titled "Ballot.exe", icon `question`, buttons "Everything" / "Everything, but sadder"; sticky note in Mel's hand: "I only wanted the bus".

### 4 · meme · 7s
- **Visual:** Mel at the front door at 9am, dog looking at three bins of different colours, none of them emptied.
- **On-screen:** three toasts stacking: "Bin update installed for every household." / "The previous version has been deleted." / "Your bin day is now a surprise."
- **Say:** "Nine a.m. The bins. New rules, every street at once. Did they try it on one street first? Bless you for asking."
- **Source:** Mel's town is fiction and is never named; no claim about any real council.
- **Layout:** `toasts` with `wall` "BINS" / small "09:02", each toast on its own click, image mel-bins.jpg; clock "09:02 · 1872".

### 5 · meme · 13s
- **Visual:** a bug-tracker issue, Mel's mug ring on the corner of the window.
- **On-screen:** heading "ISSUE: Did this law work?" · Review due: 3 to 5 years after · Central record of reviews: none · Status: Remind me later
- **Say:** "Big laws too. An Act is meant to be reviewed three to five years later. How many reviews happen? The Lords was told there's no central record. I'm not saying none. I'm saying nobody's counting."
- **Source:** ledger row 20 (Acts reviewed 3-5 years after, https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament, OK) and row 21 (no central record, https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny, OK). No count of unreviewed Acts.
- **Layout:** `ticket` titled "Issue #1872", `fields` as above, `highlight` "Central record of reviews"; a small "(Lords written answer)" under the field.

### 6 · meme · 7s
- **Visual:** two windows. Left: a pill bottle with a thick paper trail behind it. Right: a podium with a microphone.
- **On-screen:** left "PILL: years of trials. Control group: yes." / right "POLICY: a confident announcement. Tested: no."
- **Say:** "Noon. The bills. A pill gets years of trials before it's allowed near your bathroom shelf. A policy gets a podium."
- **Source:** ledger row 26 (RCTs routine in medicine, rare in domestic policy; Test, Learn, Adapt, https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials, OK).
- **Layout:** `split`, left titled "Pill.exe" with progress "Trial 3 of many", right titled "Policy.exe" with one button "Announce"; clock "12:00 · 1872".

### 7 · meme · 12s
- **Visual:** an installer window over a picture of a coach of teenagers pulling up at a prison gate. Mel is not in this one.
- **On-screen:** "Installing COMMON SENSE... 100%" then the error "Result: reoffending went UP."
- **Say:** "Scared Straight: take teenagers to meet prisoners, frighten them off crime. The people running it were sure. Nine controlled trials: it made reoffending worse. Common sense is a guess with good posture."
- **Source:** ledger row 28 (Petrosino et al. 2013 Campbell review, 9 randomised studies, likely harmful, https://ideas.repec.org/a/wly/camsys/v9y2013i1p1-55.html, OK). It names who was sure (the programme's runners). The test cuts both ways, so the tough-on-crime viewer stays with us.
- **Layout:** `dialog` titled "Setup: Common Sense v1.0", icon `error`, progress {pct 100, label "complete", err true}, buttons "Install anyway" / "Install it everywhere".

### 8 · meme · 9s
- **Visual:** full-screen blue crash page. Nothing else.
- **On-screen:** code "BRITAIN.SYS 0x1872" · big ":( Mel asked for three things." · text "Bus: bundled. Bins: no undo. Bills: untested. This fault was built in by the people who designed the system, not by the person pressing the buttons." · footer "Press any key to wait for the next election."
- **Say:** "Six p.m. Three errands, and the country's blue-screened. Not Mel's fault. Mel pressed the only buttons on offer."
- **Source:** callback, no new fact.
- **Layout:** `fatal`, `dark: true`; clock "18:00 · 1872".

### ACT 2: THE PATCHES (9-15)

### 9 · meme · 10s
- **Visual:** the desktop back up. An update box in the middle, Mel's cursor drifting toward it.
- **On-screen:** heading "3 important updates are available" · Patch 1: vote on the thing, not the bundle · Patch 2: change small, keep an undo · Patch 3: test it first · small "You're not gambling by installing. You're gambling by not."
- **Say:** "Where I'm from, nobody installed anything, and I know exactly how that version ends. So I've brought three patches. Software's had them for decades. Small, boring, and they work."
- **Source:** canon (research/01-canon.md: the bad branch is finished; "not gambling by changing the system, gambling by keeping it", ledger row 55/57, OK), reworded for the OS.
- **Layout:** `dialog` titled "Britain Update", icon `info`, buttons "Remind me later" (first, so it's the default and outlined) / "Install now"; lines revealed one per click.

### 10 · diagram (three.js) · 20s
- **Visual:** the `pub` scene. Five people at a pub table, Mel is one. Three Sun-party policy cards. Phase 1: each card loses 3-2. Phase 2: the five slide into party stacks and the Sun party wins 3-2.
- **On-screen:** caption "PATCH 1: VOTE ON THE THING, NOT THE BUNDLE" · phase 1 "EVERY POLICY LOSES 3-2" · phase 2 "THE PARTY WINS 3-2" · small "software calls it composition over inheritance"
- **Say:** "Patch one. Five people in a pub. The Sun party has three policies. Vote on each, and every one loses three-two. Vote for the party: it wins three-two. Same people. Same pints. Only the ballot changed. Software calls the fix composition over inheritance. You can call it voting on the bus."
- **Source:** ledger row 13 (Ostrogorski paradox, https://www.newamerica.org/insights/the-paradoxical-reason-republicans-win-elections-despite-unpopular-policies/ and https://arxiv.org/abs/2307.11873v1, OK; worked example is ours, checked by hand). Invented parties only.
- **Layout:** `diagram`, scene `pub`, title "Pub.exe", steps 3 (cards, phase 1, phase 2).

### 11 · meme · 8s
- **Visual:** Mel holding a slice from a half-and-half pizza, delighted, the dog eyeing the other half.
- **On-screen:** top "HALF AND HALF IS ALLOWED ON A PIZZA" / bottom "ASK FOR IT ON A COUNTRY"
- **Say:** "A pizza can be half and half. A country, apparently, is a set menu. Some places already print several boxes. The pencils coped."
- **Source:** ledger row 15 (some countries vote issue by issue, https://www.admin.ch/gov/en/start/documentation/votes.html, OK, no number, no country named, no results, never the word "referendum").
- **Layout:** `picture` (mel-pizza.jpg) with top and bottom captions; sticky "patch 1 installed".

### 12 · diagram (three.js) · 17s
- **Visual:** the `tower` scene. Left: a tower of small bricks, each one ticked green as it lands; one goes red and the undo arm lifts it out while the tower stands. Right: a crane drops one huge monolith. No ticks.
- **On-screen:** caption "PATCH 2: CHANGE SMALL. CHECK IT. KEEP AN UNDO." · left "SMALL. CHECKED. UNDOABLE." · right "ONE DROP. NO TICKS."
- **Say:** "Patch two. Change small, check each piece, keep an undo. Not move fast and break things: move small, and take it back. Right now we drop the whole tower off a crane and check it in three to five years."
- **Source:** ledger row 19 (the green tick, research/13, OK, explanatory) and the row 20 callback (3-5 years, OK). No deploy-rate figure.
- **Layout:** `diagram`, scene `tower`, title "Build.exe", steps 2 (left builds and reverts, right drops).

### 13 · meme · 9s
- **Visual:** two windows. Left: a bright test room with a "try it here first" banner. Right: Mel's three bins on the kerb, still full.
- **On-screen:** left "NEW MONEY APPS: a safe sandbox to test in first." / right "MEL'S BINS: Monday."
- **Say:** "This exists. The financial regulator gives new money apps a safe place to test first. Mel's bins got Monday."
- **Source:** ledger row 24 (FCA regulatory sandbox, announced Nov 2015, first cohort 7 Nov 2016, https://www.crowdfundinsider.com/2016/11/92162-first-class-fca-reveals-24-fintech-firms-accepted-regulatory-sandbox/, OK). Never "world first".
- **Layout:** `split`, left titled "Sandbox" with button "Try again", right titled "Production" with the single button "Too late"; sticky "patch 2 installed".

### 14 · diagram (three.js) · 17s
- **Visual:** the `letters` scene. Two envelopes fan out; bars rise to 67.5% and 79%; a tag on the taller bar: "most people in your postcode have already paid".
- **On-screen:** caption "PATCH 3: NO POLICY WITHOUT ITS EXPERIMENT" · "SAME LETTER, ONE EXTRA LINE: 67.5% → 79% PAID" · small "HMRC, overdue tax"
- **Say:** "Patch three: no policy without its experiment. HMRC tried versions of one tax letter and counted who paid. Plain letter: sixty-seven and a half percent. Add 'most people in your postcode have paid': seventy-nine. Nobody passed a law. Somebody tested a sentence."
- **Source:** ledger row 27 (67.5% control vs 79% postcode line only, https://thedecisionlab.com/intervention/how-normative-messaging-increased-tax-compliance-by-15 and https://blogs.worldbank.org/voices/ongoing-impact-nudging-people-pay-their-taxes, OK). No "eleven", no "best of", no sample size, no £ figure.
- **Layout:** `diagram`, scene `letters`, title "Bills.exe", steps 2.

### 15 · meme · 10s
- **Visual:** Mel back at the 7:14 bus stop, reading a notice pinned up, and giving it one satisfied nod.
- **On-screen:** heading "HOW WE'LL KNOW" · What we're testing: the 14 bus every 10 minutes · Who goes first: this town · Number that means stop: ____ · Ends on: ____
- **Say:** "So every policy carries a label: what we're testing, who goes first, the number that means stop. Can't fill it in? Not ready. Number says stop? We stop, and nobody has to resign."
- **Source:** research/14 concept 8 (the "How we'll know" label) and the trial-is-public rule; the bus trial is a made-up example, not a claim about a real service.
- **Layout:** `dialog` titled "Notice.txt", icon `question`, `image` mel-notice.jpg on the left, buttons "Run the test" / "Announce it confidently"; sticky "patch 3 installed".

### CLOSE (16-17)

### 16 · meme · 18s
- **Visual:** Mel on the sofa with the dog, phone buzzing. Five notifications stack up fast, one per click.
- **On-screen:** wall "YOU'RE NOT THE FIRST" · toasts: "FixMyStreet · fixmystreet.com" / "Sortition Foundation · sortitionfoundation.org" / "PB Scotland · pbscotland.scot" / "TheyWorkForYou · theyworkforyou.com" / "Pol.is · pol.is"
- **Say:** "You're not the first. FixMyStreet: the country finally got a bug tracker, and the bug is the pothole. Sortition Foundation: jury service, but for the bins. PB Scotland: the council's actual money. TheyWorkForYou: how your MP voted, issue by issue. Pol.is: where the other side secretly agrees with you. Other people are already rethinking this. Go and look."
- **Source:** ledger rows 40-54 (explore-directory.md, checked live 2026-11-05, OK). Names and URLs as plain text, no logos. small-ideas.org is left out (GATE).
- **Layout:** `toasts`, `wall` {heading "YOU'RE NOT THE FIRST", small "5 new notifications"}, each toast on its own click, image mel-sofa.jpg; clock "21:30 · 1872".

### 17 · meme · 11s
- **Visual:** the desktop. An installer window, Mel's cursor just off the "Install now" button it has clicked.
- **On-screen:** "Installing update 1 of 3... 3%" · small "Time remaining: depends who helps" · then the taskbar clock flips 1872 → 1873 · then one last toast: "Bus 14: arriving (unrelated)"
- **Say:** "Mel clicks install. Three percent. First update since the light bulb. But look at the clock. Eighteen seventy-three. We're moving. Oh, and there's the bus. Unrelated. Future Proof."
- **Source:** callbacks (slides 1, 2, 9), no new fact.
- **Layout:** `title` heading "FUTURE PROOF", `progress` {pct 3, label "Installing update 1 of 3"}, sub "badcode.tv/future-proof" (CHECK the URL is live before printing), `clock` "1872" revealed to "1873" on step 1, then a single toast "Bus 14: arriving (unrelated)" on step 2; steps 2.

---

**Total: 17 slides, 198 seconds (3:18).** 541 spoken words, about 2.7 a second: brisk stand-up pace, with no room left for laughs, so a live run lands nearer 3:45. 3 diagrams (pub, tower, letters; each followed at once by a meme), 1 crash screen, 13 memes and title-style windows. Scenes not used: timeline (its job is done by the release-notes hook), slab, towns, pipe, dots, tokens.

**Running gags and callbacks:** the two identical bad buttons (1, 2, 3, 7); "Remind me later" as the default (2, 5, 9) until Mel clicks the other one (17); clock time of day (1, 4, 6, 8, 16) and the year finally ticking (17); the 14 bus (1, 3, 10, 15, 17); the bins (4, 13); "three to five years" (5, 12); "patch N installed" stickies (11, 13, 15).

**If it needs to lose 20s:** cut 7 (Scared Straight), though it has the best line, and trim 16 to three projects.
