# Goal 3: the Future Proof Demo, from a blank page

Kai, 24 Nov 2026. A new experiment that sits beside everything built so far. **Nothing existing is
changed or removed**: the Future Proof simulation (`simulation/live`, `/future-proof/live/`, the `sim-*`
workers, the routine) keeps running as it is. Later we may bring the two worlds together.

## The idea

Show the process, don't prove it. Like fixture data in a test: the data is written to tell the story;
what matters is that the process visibly works. Every day one issue on a big topic goes through the
Future Proof loop and ends in a clear, chosen way. A demo government sits on top. Everything it says is
built from those days.

## Three layers

1. **The daily debate (the engine).**
   - **Topic:** a headline area people care about, rotating: housing, health, education, work, energy,
     transport, crime.
   - **The issue:** a real topic in that day's news (from Bob's `kind=news-digest` memory for the date),
     plus a made-up case: an invented town, proposal and numbers.
     - No real person or company is named.
     - Real public figures (a published statistic) may be used, with their source.
   - **The ending:** chosen up front, one of:
     - **accepted:** one answer passes every test, and the minister signs it as written;
     - **partly:** the best answer passes some tests, the minister signs a small trial of what passed, and
       the gaps become dated predictions;
     - **rejected:** no answer passes, nothing is signed, and the record says which tests failed and why.
   - **The stations:** citizens set the tests → three answers → the checker → the jury → the minister →
     a date to check back.
   - **Steer the inputs, never fake the marks.**
     - The case and the tests are written so the chosen ending is reachable.
     - The checker still marks honestly against what the answers say.
     - If the marks miss the chosen ending, rewrite the case or the answers and run the checker again.
       Never edit a mark.
2. **The record.** Every day's decision, filterable by topic and by ending. Only accepted and partly
   endings are **adopted**.
3. **The demo government.**
   - One new minister per headline area (seven), each starting with an empty manifesto. Today's cabinet
     is not reused.
   - A manifesto line exists only because a day adopted it, and it links to that day.
   - **The daily debate:** after each day, the ministers argue the day's issue and keep, change or drop
     what they adopted before. Each change cites the day that caused it.
   - Content and social accounts for the ministers come later, with Kai's separate go-ahead. Nothing in
     this goal posts anywhere.

## Done means

1. **Backfill in one batch.**
   - Fourteen days, news dates **10 to 23 Nov 2026**, all run now, in parallel, not one per real day.
   - Each topic appears twice. The endings are spread across the fortnight: about five accepted, five
     partly and four rejected, with no topic getting the same ending twice.
   - The minister's daily debate is replayed in date order, so the manifestos grow day by day.
2. **Every day after,** one new day runs by itself (Bob workers, then the site rebuilds), with the ending
   taken from the rotation.
3. **A new public page at badcode.tv/demo/:**
   - today's issue moving through the stations with its data;
   - the record;
   - the seven ministers and their manifestos;
   - the debate.
   - One banner saying "This is a demo", plus "Demo" in the page title and link preview. No per-card
     labels.
4. **Renamed throughout:** demo branch, `demo-*` workers, folders, scripts and schedules. No `sim` names
   in anything new.
5. The `marketing-gatekeeper` passes the page before the first deploy.
6. A build log in this folder, ending with:
   - what runs when;
   - the cost of one day;
   - what failed.

## Keep from the simulation (copy, don't move)

- The station-by-station worker pattern.
- The issue format and its validator.
- The page's loop animation.
- The site build that reads a data branch.
- The scoreboard and dated predictions.

## Rules

- **Never change or delete anything from the simulation:**
  - the `simulation/live` branch;
  - `/future-proof/live/`;
  - the `sim-*` workers;
  - routine `trig_012kXE2KMjrHYuber7bJBmev`.
- **Never edit** `docs/government/policies/` (the real manifesto) or today's government pages.
- **Never touch** PRs #29 or #22.
- **No posts** to social media or YouTube.
- **No real person or company named** in a made-up case. Never put words in a real person's mouth.
- **Every prediction falls due after its run date.**

## Merging

- Open one PR for the work.
- Kai merges it, unless he confirms in the goal message that I may.
