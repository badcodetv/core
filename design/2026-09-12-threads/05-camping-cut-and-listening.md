# Thread 05 — Camping: a cut of the music video, using the new listening tools

You are in `~/projects/badcode/badcode`. Read `CLAUDE.md`, then `design/2026-09-11-claude-can-hear.md`
(the index for the two listening plans and their stop gates), `design/2026-09-11-listen-mcp.md` T3's
Notes (why it is blocked), `design/2026-09-11-understand-song-loop.md` (T11 and T13 are the pending
tickets), `docs/suno-gpt/session-method.md` (how we work a song: one variable per round, diagnose before
rewording), `docs/suno-gpt/files/suno-v6.md` (all new Suno work is v6), and the camping canon:
`docs/stories/camping/songs/camping.md` (the accepted sheet), `songs/camping-sheet.md` (Jack's 2026-08-27
brief: "we have lost the aggression and the pace, experiment with different genres over the drum and
bass"), `songs/camping-released.md` (the take Jack's video is cut to — its lyrics are frozen) and
`music-video.md` (Kai's hand cut in Premiere, surveyed 2026-08-24: picture ends at 43.56 s of a
236.4 s sequence).

## Goal

Two things, in this order:

1. **Prove the listening tools on a real job.** Yesterday we built `packages/listen-mcp` (give it an audio
   file, get a description from Gemini via AI Studio plus local measurements) and the Suno loop commands
   (`record`, `explore`, `narrow` in `scripts/suno/`). Use them on camping takes and say honestly whether
   they helped: did the description match what Kai hears, did the loop narrow faster than the old
   listen-and-reword method. File the answer in `docs/listening/log/`.
2. **Get the camping track where Jack wants it**, then a cut. **Jack's reference band is Imagine Dragons**
   (Kai, 2026-09-12: https://en.wikipedia.org/wiki/Imagine_Dragons). What that means in producible terms:
   arena pop-rock with huge stomping percussion and claps, a half-shouted, strained male lead with big
   dynamic lifts, chant-along hooks, heavy reverb, electronic and dubstep-adjacent low end; the songs to
   hold in mind are "Radioactive", "Believer", "Thunder" and "Demons". Jack's earlier brief said the
   track had lost aggression and pace, so this is the same note made concrete. Warning: the accepted
   camping sheet's exclude list currently bans "live rock band", "epic trailer music", "power chords",
   "uplifting" and "major key" — several of those *are* the Imagine Dragons sound, so the exclude list is
   the first thing to reopen, one variable per round. Do not name the band in the Style box (Suno strips
   artist names); describe the sound. Kai may add more of Jack's guidance. Turn that into a v6 style description (genre picks the
   vocalist pool — `docs/suno-gpt/suno-voices.md`), keep the lyrics frozen, run the loop, and when Kai
   accepts a take, lay it into the Premiere project (`/mnt/d/badcode-videos/camping-music/camping.prproj`)
   as a new sequence beside Kai's, never over it. Then extend picture past 43.56 s per `edit-plan.md`.

## 🔴 Stop gates — never work around

- **listen-mcp T3 is blocked**: AI Studio returns 403 to Chrome for Testing. The recorded fix is to run
  the listening channel in normal branded Chrome. Propose the change to `scripts/flow-chrome.sh` /
  `browser-channel.sh`, then stop: the window must be signed into **Jack's Ultra Google account**, which
  only a human does. If AI Studio saves uploads to Jack's Drive with no off switch, stop.
- **Every 20-credit Suno run needs Kai's explicit yes.** Dry-run first, always. Run `status` first;
  **one Suno tab, ever**; never navigate away from `suno.com/create`; never automate a download.
  **Check the form mode before every fill** (Cover mode and attachments survive a box fill).
- **Suno is one session at a time.** Thread 08 (GPOM narration) also wants Suno. You own Suno while
  you run; say in your reports when you release it.
- Kai approves every take; you propose and describe, you never accept.

## House rules

Shared checkout: commit per ticket on `main`, stage only your own files, never push, never switch
branches. Media outside the repo (`LISTEN_MEDIA_ROOT`, default `/mnt/c/Users/kai/Desktop/suno-recordings`);
words and logs inside. Browser channels via `./scripts/browser-channel.sh claim`, never a hand-picked port.
The 8 kHz preview filter touches only the human's copy. Rundown style; gloss every ticket.

## First action

Reply with: (a) the exact human step to unblock T3 (which window, which account, what to click); (b) a
one-paragraph plan for turning Jack's band reference into a v6 style, with the questions you need answered
(paste the guidance, please); (c) the dry-run command for the first `explore` round, not yet run.
