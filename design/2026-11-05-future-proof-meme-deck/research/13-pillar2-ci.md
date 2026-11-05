# 13 - Pillar 2: Continuous integration -> continuous, testable governance

Solidity key: **P** primary (the body itself), **S** secondary (reporting/academic), **H** hearsay/community, **M** from memory, NOT verified this session (check before putting on a slide).
Searches used: 8 of 8.

## 1. How to explain CI to non-programmers (what already works)

- **LEGO tower**: friends each build a part; bolt each piece on as soon as it's made, so a bad fit shows while it's small. Do not wait until the end to join the parts. [H] https://dev.to/snwfdhmp/continuous-integration-like-im-five
- **Recipe**: siblings propose changes to the perfect cake recipe; good ones go in fast, bad ones are stopped early, the master recipe stays good. [H] same URL.
- **Marketing-colleague framing**: "frequent small merges instead of one big integration phase at the end." [H] https://semaphore.io/wp-content/uploads/pdf-downloads/continuous-integration-explained.pdf (standard technical definition: merge to main many times a day).
- **Plain-language rule**: each change is tested against the whole thing, so you know at once if something broke. [H] https://dev.to/theowlsden/ci-cd-a-non-techinical-intro-2okf
- **The version that works for our reader**: not "agile", but "the green tick". Nothing goes live unless the check passes; if it breaks, it is rolled back in minutes. Government has no green tick and no undo button.

## 2. Number check for the canon (important)

- future-proof.md says Amazon deploys "100,000+ times a day". Not confirmed here. What is findable: **"every 11.6 seconds"**, from a 2011 talk by Amazon's Jon Jenkins; counts all production deployments incl. internal services, not just the shop. [S] https://www.slideshare.net/slideshow/light-talk-meet-up-jenkinsbr-2013-jenkins-alm-da-integrao-contnua-prticas-de-devops/29049214 ; caveat from an ex-Amazon commenter [H] https://news.ycombinator.com/item?id=2971521
- A book quote credits Vogels with ~50 million host deploys in 2014 (~1/sec), a different metric. [H] https://www.goodreads.com/work/quotes/47585842
- Recommendation: on a slide say "a company like Amazon changes its live software every few seconds" (safe, dated 2011) or re-source the 100,000 figure before use. Never "11.7".

## 3. Real governance analogues

**Post-legislative scrutiny (the "tests" for laws)**
- Since 2008 UK Acts are normally meant to be reviewed 3-5 years after enactment; it sits in the Cabinet Manual. [S] https://www.wfd.org/what-we-do/resources/post-legislative-scrutiny-uk-parliament
- In practice: Commons PLS depends on individual committees' initiative; Lords is more systematic but ad hoc. [S] https://irep.ntu.ac.uk/id/eprint/43356
- A parliamentary written answer says there is **no centrally held record** of how many post-legislative reviews departments have submitted. [P-ish, Hansard mirror] https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny
- Law Commission proposed (2006) a more formal system. [P] https://lawcom.gov.uk/?p=2297
- Gap: no published count of Acts never reviewed was found. Do not assert one. The honest line is "nobody keeps the count" (sourced above).

**Sunset clauses (the "expiry date")**
- A UCL paper's search of the statute book found only **19 Acts** with expiry provisions (sunset clauses are a subset). [S] https://discovery-pp.ucl.ac.uk/10091123/1/Xanthaki_2019%20Ranchordas%20Sunset%20clauses.pdf
- Since March 2011 government policy: secondary legislation burdening business should carry a sunset clause. [S] same paper.
- Sunset clauses on anti-terror laws have rarely ended the laws; they renew by default (Blackbourn). [S] https://psaparliaments.org/2016/10/05/do-sunset-clauses-work/
- Lesson for the deck: a sunset with automatic renewal is a test nobody reads. Good CI = **the default is it stops unless the data says keep**.
- Retained EU Law Bill sunset (2022-23) is the "delete everything on a date without testing" counter-example: a sunset with no test, criticised by JUSTICE. [S] https://ukconstitutionallaw.org/2022/10/10/kate-ollerenshaw-more-haste-less-speed-sunset-clauses-in-the-retained-eu-law-revocation-and-reform-bill/

**Regulatory sandboxes (staging environment)**
- FCA sandbox: announced Nov 2015, first cohort named 7 Nov 2016; FCA says it was a world first (FCA's own claim, not independently verified). [S] https://www.crowdfundinsider.com/2016/11/92162-first-class-fca-reveals-24-fintech-firms-accepted-regulatory-sandbox/
- FCA year-one report: ~90% of completers moved toward market launch, >=40% got investment. [P-derived] https://fca.org.uk/news/press-releases/financial-conduct-authority-outlines-lessons-learned-year-one-its-regulatory-sandbox
- Lesson: we already do staging, for **fintech start-ups**. Not for benefits, housing or tax.

**Laws that ran for years on a bad assumption (failure without tests)**
- **Computer-evidence presumption**: since 2000 English law presumes a computer was working correctly unless shown otherwise; critics say rebutting it is near-impossible against a big institution. Over 15 years, 736 subpostmasters were prosecuted by the Post Office. MoJ has since run a call for evidence on it. [S] https://www.gov.uk/government/news/use-of-computer-evidence-in-court-to-be-interrogated ; https://www.benthamsgaze.org/2022/06/30/the-legal-rule-that-computers-are-presumed-to-be-operating-correctly-unforeseen-and-unjust-consequences/ . Handle with care: real victims; name the decision-makers (Post Office, the rule's keepers), never "computers". Not a laugh line; a "this is what no test costs" slide.
- **Poll tax**: Scotland got it first, 1 April 1989, a year before England and Wales; abolition announced 21 March 1991; Council Tax from 1993. Literally a pilot in production... on a region, with no stop condition. [S] https://en.wikipedia.org/wiki/Poll_tax_(Great_Britain) (good for a lead, verify against a primary before print)
- Not searched, [M], verify before use: Dangerous Dogs Act 1991 (rushed, then amended repeatedly); Universal Credit rollout (pilots/"test and learn" then national); Child Support Agency 1993 launch problems; Windrush. Candidates only.

## 4. Ten meme/joke concepts for pillar 2

Narrator voice: certain, sarcastic, nurturing. Contempt for the mistake, not the people. Looks belong to the deck's own look.md; these are ideas, not styling.

1. **"Settings > Software Update."** Phone: 14 updates this week. Parliament: last big update 1832-ish, still on Windows XP energy. Caption: "Your phone patches itself while you sleep. Your pension system has been 'in beta' since 1948." (check dates before use)
2. **The Green Tick.** Two buttons: laws today = "Merge" (no tests, big red, sweating). Future = tests run, green tick, then merge. Drake format works, but any two-panel works.
3. **"Works on my machine."** The Minister, holding a pilot of 12 well-off households. Reality: 66 million machines. (Poll tax is the real-life tie: Scotland first, 1989.)
4. **Release notes for a law.** Show a parody changelog: "v5.0: Fixed bug nobody asked about. Known issues: everything. Next update: 2029." Pillar line: updates should say what changed and what broke.
5. **Undo button.** Ctrl+Z over a statute. "Every app you own has Undo. The 2012 Act has 'we'll look into it'." (Use a real Act only after sourcing.)
6. **Nobody keeps the count.** Cut to a filing cabinet labelled "Did this law work?" empty. Caption: "Written answer, Parliament: no central record of reviews." Sourced, deadpan, strong. https://parallelparliament.co.uk/question/HL2377/legislation-parliamentary-scrutiny
7. **The 19.** "Laws with an expiry date: 19. Milk: all of it." Source: UCL paper above. Caveat: count is from one study's search.
8. **Staging server.** Fintech start-ups get a safe sandbox since 2016; benefits claimants get production. Slide: "Test it on the banks, not on the bus pass." Source: FCA sandbox. Nurturing beat: the idea already works, it just stopped at the money.
9. **The CD-ROM government.** Every five years a disc is posted: "Install All or Reject All." The pillar's own image; pair with the LEGO tower: bolt on one brick a week, test each, tower stands.
10. **Rollback.** Slide of a tidy blue "Revert" button vs the 1989-1991 poll tax timeline (2 years to cancel, 4 to replace). Caption: "In software we call this an incident. We write it up. We don't do it to a country twice." Careful: say "decision-makers did X", not "the technology".

Format notes for the slideshow: concepts 1, 2, 5, 9 are one-image jokes (meme); 6, 7, 8 are number slides (need on-screen source line); 3, 10 need a short timeline (good for a three.js scene: tower of bricks with test lights, versus one big block dropped).
Possible 3D idea: a LEGO-style tower where each brick lights green on test, red on fail and drops off cleanly; versus a five-year monolith dropped in whole.

## 5. Traps (the-reader.md / using-ai rules)

- Never "you've been duped"; the failing is in the process, not the voters.
- Name the decision-maker (ministers, departments, the Post Office), not the technology.
- Post Office/Horizon: victims are real people; no punchline at their expense, punchline at the missing check.
- "Tests make fast change safe" must stay the line: do not let slide 1 read as "move fast and break things". Our version is the opposite: testing first, undo available.
- Gaps: no sourced count of unreviewed Acts; Amazon 100,000/day unconfirmed; Dangerous Dogs/UC/CSA unverified.
