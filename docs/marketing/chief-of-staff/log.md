# The log

Every ruling and every weekly review, newest first. One entry per event, a few lines each.
Format: `## YYYY-MM-DD — what` then who said what, in their words where possible.

## 2026-10-19 — Kai: checked against other chief-of-staff prompts; three fixes applied

Kai asked whether ours is the best chief-of-staff pattern going. Compared with loganhc's
claude-chief-of-staff, OpenAI Academy's chief-of-staff brief and ClaudeCodeHQ's weekly check-in:
ours already had the core (three priorities, human publish gate, written log, finish before
starting) plus a separate gatekeeper none of them have. loganhc's own lesson ("a smaller system you
trust beats a big one you don't", after 52 scheduled jobs broke silently) backs keeping ours small
and unscheduled. Kai: "Yes, please apply" to three additions to the skill: open each brief by asking
what happened off-repo; name any Do next item still there from the last run ("open since", a fact,
not a deadline); keep facts (with a source) apart from guesses.

## 2026-10-15 — Kai and Jack (call): short beats long; don't wait on music

On the 15 Oct 2026 call, comparing a two-minute film with Camping and GitPush Origin Master, Kai and
Jack agreed that short, high-retention films (about two minutes) hold people and long ones lose them. Kai also warned against getting bogged down in unpolished music (a Magic Money Tree
lyric was in the mix). The same call ruled full narration with no lip-sync, because viewers dislike AI
voices, and changed Karen's ending (a "to be continued" cliffhanger, no moral). That doesn't fix Karen's
beneficiary problem (next list, item 8). Source: `docs/misc/2026-10-15-meeting.md`.

## 2026-10-15 — Kai: the repo is the board; the page is read-only

Kai: "we shouldn't interact with this page at all ... me and Jack both look at it, me and Jack chat to
Claude CLI, and it then updates the artifact ... manage this in this repository and just as a final step,
publish it to the artifact simply as a way of me and Jack sharing it with each other." Done: the page is
generated from `board.md` by `scripts/marketing/build-board.mjs`; its database is switched off; it leads
with what to do next, in Claude's opinion.

## 2026-10-15 — Kai: take time out of the plan

Kai: "remove entirely the idea of time from it ... this feels now like it's a boss nobody wants,
whereas what we really want is like what do we need to do next? And what should we be doing that
we're not doing? ... when I say plan, I don't think I mean carefully orchestrated timing." Done:
`plan.md` rewritten as the goal + an ordered next list + the gaps; no weeks, deadlines, streak or
calendar. The board page and the skill follow. The dated version stays in git history.

## 2026-10-15 — Kai: Money For Something is a scratch pad; balaclava host; triangle logo to try

Kai (with Jack): voice models "are not good", so as much as possible "rely on text to speech models
outside of video models", using the narration approach. Money For Something leans into the logo: "a
guy in a white balaclava with the red triangle eyepatch, so the point is you don't see his mouth move",
narrated "as the voice of bad code". "Please treat money for something just as a scratch pad, like a
conceptual idea right now ... we would come up with content as we go." The line-by-line rulings
(living people, real footage, the three lines) wait until there is an episode. Also: try the logo
mark as a red triangle inside the white circle (logo bench reworked; not ruled). New decision opened:
what goes out in weeks 1 to 3.

## 2026-10-15 — Kai: marketing is a human job; Bob shared memory parked

Kai: Bob was meant to run marketing "automatically in the background", but "it's going to require
us humans to interact with the content we put out. So, it is a kind of interactive process that we
just need to do." The chief of staff "is very important"; focus there and grow the plan. Parked: a
shared memory where Kai's and Jack's Claude Code sessions post labelled summaries into Bob (hooks
at session end and start). Not before the 90 days are reviewed.

## 2026-10-14 — Kai: Claude Code, not Bob; plan accepted by Kai

Kai: "We don't need to complicate our world by trying to add stuff to Bob. We just share stuff
through Claude code at the moment because it is just me and Jack." And: "I have a tendency to
overcomplicate things ... I think what's missing is just getting on with it." On the 90-day plan:
"it's bloody brilliant, that's exactly what we need." Still owed: Jack's yes. Kai asked for a shared
artifact page showing the plan and next steps, updated together as things get done.

## 2026-10-14 — chief of staff proposed

Kai asked for a chief-of-staff pattern to run the marketing, portable between Claude Code and
Agent Bob, after noticing that "we're just sort of indulging ourselves in being creative and not
actually getting anything out of the door". Proposed: [`README.md`](./README.md) (the pattern),
[`plan.md`](./plan.md) (the 90 days), [`board.md`](./board.md) (the three decisions). Runs in
Claude Code with git as the shared desk until four weeks of publishing, then reconsider Bob.
Not yet accepted by Kai or Jack.
