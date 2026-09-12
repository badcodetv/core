# Thread prompts — 2026-09-12

One file per thread from [`../2026-09-12-work-board.md`](../2026-09-12-work-board.md). Each file is a
complete opening message: open a Claude session in the named checkout and paste the whole file.

| File | Paste into a session in… | Needs from Kai first |
| --- | --- | --- |
| `01-ovh-ops.md` | `~/projects/badcode/agent-bob` | OVH account + card; ~15 min of Step 0 accounts |
| `02-agent-bob-fleet.md` | `~/projects/badcode/agent-bob` | nothing |
| `03-agent-bob-three-projects.md` | `~/projects/badcode/agent-bob` | SSH to Platinum's production host; a yes before its first WhatsApp send (ticket W0) |
| `04-agent-wolf-live.md` | `~/projects/badcode/agent-wolf` | a box from 01; run after 02 |
| `05-camping-cut-and-listening.md` | `~/projects/badcode/badcode` | Jack's guidance + band name; Jack's Google sign-in once |
| `06-gpom-stills-variety.md` | `~/projects/badcode/badcode` | nothing (approve the rules on the first reply) |
| `07-mmt-footage.md` | `~/projects/badcode/badcode` | nothing |
| `08-gpom-narration.md` | `~/projects/badcode/badcode` | nothing for the sheet; a yes before any credits |
| `09-park-ideas.md` | `~/projects/badcode/badcode` | nothing |

## Do not run at the same time

- **05 and 08 both need Suno.** The conflict is real but narrow: Suno is one browser tab on one
  account (`binocarlos`), and the create page is a single form with no drafts. Two sessions filling it
  at once overwrite each other's Style, lyrics, Voice and mode mid-fill, and the mode/attachment state
  is account-wide (a Cover attachment left by one session silently turns the other's run into a cover:
  40 credits and a false diagnosis, 2026-08-27). Resolution: **time-slice, not parallelise.** 08 does all
  its free work (the v6 sheet, the dry run) at any time; generation is a hand-off — 05 posts "Suno
  released" in its report, Kai tells 08 "you have Suno", 08 runs `status` first and hands back the same
  way. Each round is ~5 minutes of form time, so the hand-offs are cheap. A second Suno account would
  remove the conflict but costs a second subscription; not worth it for two threads.
- **05 and 06 both open browsers.** That is fine: each claims its own channel with
  `./scripts/browser-channel.sh claim` and never picks a port.
- **All four badcode threads share one checkout.** Every prompt carries the shared-checkout rules:
  commit per ticket on `main`, stage only your own files, never push, never switch branches.
- **02 before 04.** Wolf runs on Bob; a Bob with five unverified branches is not a base to ship on.
- **02 and 03 both touch Bob's `main`.** The project-connections branch (`feat/project-connections`,
  32 commits, three tickets pending) is needed by 03's WhatsApp channel; 02 owns merging into `main`,
  03 asks for it. New repo for 03: `~/projects/badcode/agent-enc` (storage only, no app).
