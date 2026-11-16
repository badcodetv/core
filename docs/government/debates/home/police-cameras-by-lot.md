# Police Cameras, Tested First (home/police-cameras-by-lot)

## 2026-11-16 · PR #29

**Opposition:** Putting the whole code into the lottery leaves a dangerous ambiguity: do waiting forces also wait for deletions already required, or the human hearing at the stop? State that existing duties and the permanent right apply everywhere and survive the trial ending. Test the extra vans and new procedures within that floor.
**Answer (Home Secretary):** Right, and it should never have been in doubt. Two things wait for no lot: deleting what the law already says must go, and the right to a human at the stop. Every force has both from day one, trial or not, and neither ends when the trial does; the stop clause now says so. The lot decides the rest: the new vans, old-footage searches under the code, the arrest record, the outside reading and the published deletion count.
**Outcome:** Conceded: stop, test.where, test.against, leaves_out and the rule, this commit

**Opposition:** Your deletion test follows only pictures already due for deletion on day one. A force could clear that backlog, keep pictures that become due later, and still pass. Audit newly due deletions throughout the trial too, with a failure rule and a response to each breach.
**Answer (Home Secretary):** Fair. A force could clear the old pile and start a new one. Deletions are now counted every quarter on two lines, the pictures due on day one and the ones falling due during the trial, both audited by the inspectorate. It fails if more than one in a hundred of the pictures falling due in any quarter is still held at the end of the next. Each one found is a breach: it goes that day, and the force answers for it in public.
**Outcome:** Conceded: test.measure, fails_if and the rule, this commit

**Statistician:** "Crime solved" across all recorded crime will be decided by noise, not the code, and it doesn't say whether one in twenty is relative or in points. Fix: make the fail number the charge-or-summons share for crimes where a live alert or an old-footage search was used, in both sets of forces, keep the force-wide share beside it as a check, and say "relative".
**Answer (Home Secretary):** Taken. Two years of everything else a force does would drown the cameras. The fail number is now the share of crimes where a live alert or an old-footage search was used that end in a charge or summons, in both sets of forces, each from its own baseline, and it's relative: 6.0% must reach at least 6.3%. The force-wide share stays beside it as a check.
**Outcome:** Conceded: test.measure and fails_if, this commit

**Statistician:** The inspectorate's sample has no size, and the one-in-a-hundred threshold depends on it. Fix: name the minimum read per line per year (for example, at least 300 arrests, or every arrest where there are fewer), and say the share is the inspectorate's count over the arrests it read.
**Answer (Home Secretary):** Taken. At least 300 arrests involving a match on each line, live and old footage, in each set of forces each year, or every one where there are fewer. The share is its count over the arrests it read.
**Outcome:** Conceded: test.measure, this commit

**Statistician:** The fails-if opens "against the forces waiting", which then governs every clause, but wrong person, match alone and deletions read as plain thresholds. Fix: say those three apply to the forces that start, on their own, and the comparison with the forces waiting applies to crime solved.
**Answer (Home Secretary):** Taken. Wrong person, match alone and deletions are thresholds on the forces that start, on their own. Only crime solved is judged against the forces waiting.
**Outcome:** Conceded: fails_if, this commit

**Statistician:** The world check's rewrite nearly passes. Two gaps before it freezes: "the first such bill" has no sponsor and no start date, and a clause covering police facial recognition in general needs saying which way it counts. Fix: "the first government bill introduced after 15 November 2026 that gives police use of facial recognition a statutory basis", and a general clause counts as covering stored pictures (failed).
**Answer (Home Secretary):** Taken as written, before it freezes. Private members' bills and anything earlier don't count; a general clause, code or power counts as covering stored pictures, so failed. That makes held less likely, so the prior comes down from 0.35 to 0.3.
**Outcome:** Conceded: check.claim, check.prior, check.rule and check.if_revised, this commit

## 2026-11-15 · PR #29

**Opposition:** Your test checks whether an officer recorded anything besides the match, not whether it supports the arrest. A weak extra reason could pass; up to one arrest in a hundred on the match alone also passes. Require independent checking of the supporting evidence and a response to every breach, separately for live and old-footage searches.
**Answer (Home Secretary):** Fair on the first half. A line in a box that says "also wore a blue coat" isn't evidence. Now someone outside the force, the police inspectorate, reads a random sample of arrests involving a match every quarter and asks the real question: would the rest of the evidence have justified the arrest without the match? Live cameras and old footage are counted on separate lines, and either line fails it on its own. Every breach found gets an answer: the person is told, and the force answers to the watchdog in public. The one in a hundred stays as the trial's fail number. It judges whether the code works across every arrest read; it doesn't forgive the one in front of you.
**Outcome:** Conceded in part: independent reading, separate lines and an answer to every breach, this commit; the one-in-a-hundred fail number stands (`against` and `answer` set)

**Opposition:** Your trial assigns new vans, but the new code also governs searches of old footage. A van result cannot tell us whether those safeguards work. Say which forces get which rules, and measure old-footage searches separately. Otherwise passing the van test could carry an untested code nationwide.
**Answer (Home Secretary):** Right. The forces drawn to start get the whole code at once: the vans, the old-footage searches and the deletions. The forces drawn to wait keep today's rules until it passes. Old-footage searches are measured on their own line, with their own fail number.
**Outcome:** Conceded: test.where, test.against, test.measure and fails_if, this commit

**Statistician:** home/police-cameras-by-lot: the test has no size and "forces like them" doesn't say like them how. Fix: say how many volunteer forces are drawn to start and how many wait, make the volunteers drawn to wait the comparison, and name what non-volunteer forces are matched on (size, recorded crime, current use of the cameras).
**Answer (Home Secretary):** Taken. At least eight volunteer forces start and at least eight wait, drawn by lot; the volunteers waiting are the comparison. Forces that didn't volunteer are matched on size, recorded crime and how much they use the cameras today, as a check on them. Eight is a floor.
**Outcome:** Conceded: test.where and test.against, this commit

**Statistician:** home/police-cameras-by-lot: none of the three measures names its figure or record. "Crime solved": which figure (for example, the share of recorded crimes ending in a charge or summons, from the Home Office crime outcomes data), and which crimes, all of them or only those where the cameras were used? "Wrong person": from what record (each force's deployment records of alerts, stops and false alerts)? "Arrests on the match alone": who reads the arrest records, every one or a sample, and is it someone outside the force? Fix: name each record, and name who reads the arrests (for example, the inspectorate reading a random sample each quarter).
**Answer (Home Secretary):** Taken as suggested. Crime solved is the share of all recorded crime ending in a charge or summons, from the Home Office crime outcomes data. Wrong person comes from each force's deployment records of alerts, stops and false alerts. Arrests on the match alone: the inspectorate reads a random sample each quarter, in both sets of forces.
**Outcome:** Conceded: test.measure, this commit

**Statistician:** home/police-cameras-by-lot: "they solve no more crime" has no baseline and no margin. A rise of one crime passes it, and chance alone does that about half the time. Fix: the change in the share of crime solved from each force's own baseline, against the forces waiting, rising by a set amount (for example, one in twenty) or it fails.
**Answer (Home Secretary):** Taken. Each force from its own baseline, against the forces waiting; the share of crime solved rises by at least one in twenty or it fails.
**Outcome:** Conceded: fails_if, this commit

**Statistician:** home/police-cameras-by-lot: the rule now covers searches of old footage and deleting custody pictures, but the test only measures the vans, so those parts would go national without a test. Fix: put old-footage searches on their own line, with their own arrests-on-the-match-alone share, and give the deletion count a baseline and a fails-if (for example, any custody picture still held a year in that the law says must go), or say that these parts are judgement calls and label them that way.
**Answer (Home Secretary):** Taken, mostly as written. Old-footage searches have their own line and their own match-alone share. Deletions: each force counts the pictures it holds that the law says must go on day one, the inspectorate audits the count, and it fails if more than one in a hundred of them is still held a year in. Not "any": a fail number set at zero measures the backlog a force inherited, not the code.
**Outcome:** Conceded: test.measure and fails_if, this commit (deletion margin one in a hundred, not zero)

**Statistician:** home/police-cameras-by-lot: the world check is still provisional and doesn't yet pass. The "none chosen by lot" half is close to certain, so the real risk sits in whether the Home Office names forces by 31 March, which is a question of timing and tests nothing the policy argues. Fix: use the check's one rewrite on a forecast the policy actually makes, for example that the Police Reform Bill as introduced by a set date will hold no statutory code covering searches of old footage, marked against the Bill text on bills.parliament.uk, with a prior no higher than 0.9 and a rule for the case where the Bill isn't introduced.
**Answer (Home Secretary):** Taken, and this is the one rewrite. New check: if a bill giving police use of facial recognition a statutory basis is introduced by 30 June 2027, its text as introduced will not cover police searches of stored pictures and old footage. Held if no clause, code or power to make one applies to them; failed if one does; void if no such bill is introduced by then. Prior 0.35: on the Home Office's own promise of a code, more likely than not that the bill does cover them. Marked 15 July 2027. The provisional mark is off.
**Outcome:** Conceded: check rewritten, this commit
