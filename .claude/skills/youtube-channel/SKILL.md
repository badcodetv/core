---
name: youtube-channel
description: Use to MANAGE the BadCode YouTube channel from a session — list what's on it, upload a finished cut, give a video its title, description and tags, put the AI label on, set a thumbnail, sort playlists, or tell which videos are Shorts. Drives the `youtube` MCP tools (YouTube Data API v3) and keeps docs/youtube/ as the record. Triggers on "upload this to YouTube", "what's on the channel", "sync the channel", "add descriptions / tags", "retitle this video", "label it as AI", "is this a Short", "YouTube thumbnail", "add it to a playlist", "set up the YouTube tool", "the YouTube tool says not signed in". The words themselves are drafted by the chief-of-staff's marketing-producer and checked by marketing-gatekeeper; this skill is the procedure and the tool.
---

# youtube-channel

Kai, 2026-11-11: "the management of this channel will exceed our capabilities if we don't automate it."
The tool is the `youtube` MCP server (`packages/youtube-mcp/`). Setup, the tool list and the API's limits
are in [`docs/youtube/README.md`](../../../docs/youtube/README.md). This file is the procedure.

## Standing rulings

- **Going public is a human click in Studio.** Kai, 2026-11-11: managing the videos is the job, not
  publishing them. Uploads go up **private**. Only set unlisted, public or a schedule when Kai or Jack has
  asked for that video, in words.
- **Every video carries the AI label** (YouTube's "altered or synthetic content"). Kai, 2026-11-12.
  `youtube_upload` sets it by default; `youtube_label_ai` labels anything else (Jack's hand uploads).
  🔴 YouTube **accepts** this label but **never reads it back**, so `docs/youtube/log.jsonl` is the only
  record of which videos have it. Never "fix" a video because `get` shows no label.
- **Kai or Jack picks the titles.** Retitle only on their word. The first four, as ruled 2026-11-12: "Git
  Push Origin Master", "Karen will lead the revolution (music video)", "The bank robbery (music video)",
  "The Rules Are Not Working Anymore".
- **Descriptions and tags are written for growth.** They come from the story's own canon and the growth
  playbooks the repo already has, not from new research (the chief-of-staff plan's rule one). No spoilers:
  setup only, never the twist.

## The loop

1. **Sync.** `youtube_list_videos`. It rewrites `docs/youtube/channel.json` and lists `needsAiLabel`.
2. **Label.** If anything needs it: `youtube_label_ai`.
3. **Know what each video is.** `isShort` (vertical or square, 3 minutes or less; the API has no Shorts
   flag, so it is worked out from the file's frame size and length). Find each video's canon folder in
   `docs/stories/` (shorts are `short-<slug>/`).
4. **Draft the words.** Hand the marketing-producer subagent: the fixed titles, each video's length and
   shape, its canon folder, and the growth docs listed below. It writes to
   `docs/youtube/drafts/<date>-<what>.md`: description, tags, hashtags, an optional pinned comment, and the
   doc behind each choice.
5. **Check.** marketing-gatekeeper on the draft file (reader rules, voice, AI disclosure, spoilers, legal).
   Fix anything marked FAIL or REVISE before a human sees it.
6. **Kai or Jack picks.** Show the drafts and apply only what they approve. A whole set at once is fine.
7. **Apply.** `youtube_update_video` per video, passing only the changed fields (it keeps the rest).
   Tags are the **full** list. Every change lands in `log.jsonl`, with the snapshot refreshed.
8. **Commit** `docs/youtube/`. The commit message names the videos and what changed.

**Uploading a new cut:** run the delivery QC first (`scripts/delivery-qc.sh`, the `video-fx` skill). Then
`youtube_upload` with the file (a `D:\…` path works) and the title Kai or Jack gave. Leave the label on and
privacy at private, then go to step 4.

## Where growth guidance lives

Read these before drafting, and cite them. Don't re-research them:

- [`docs/marketing/platform-playbooks.md`](../../../docs/marketing/platform-playbooks.md): YouTube's section
- [`docs/marketing/shorts-growth.md`](../../../docs/marketing/shorts-growth.md) and
  [`shorts-release.md`](../../../docs/marketing/shorts-release.md): Shorts
- [`docs/marketing/chief-of-staff/plan.md`](../../../docs/marketing/chief-of-staff/plan.md): what we're
  pushing and what's parked
- [`the-reader.md`](../../../docs/marketing/the-reader.md), [`voice.md`](../../../docs/voice.md) and
  [`using-ai.md`](../../../docs/using-ai.md): the words

## Rules of thumb

1. **The first two lines are the description.** Put the plain words a viewer would type there, in the order they'd
   type them. (plan.md §3.10 evergreen search; platform-playbooks.md §3 Provisional.)
2. **Same words in speech, on screen and in the description.** If the song says "bed", the description says "bed".
   (shorts-growth.md §3, "Search words".)
3. **One to three topical hashtags, never more; no `#Shorts`.** Hashtags don't move Shorts reach, and a vertical
   video under 3 minutes is a Short without the tag. (shorts-growth.md §2–3; shorts-release.md §4.)
4. **Tags are insurance, not a lever.** The repo has no evidence that they move reach; keep them honest, under 500
   characters, in the viewer's words. (shorts-growth.md §2–3; see "How much tags matter".)
5. **Links only where they click.** On a Short: set the Related video by hand in Studio; the description and pinned
   comment are text only. On a long film: website with `?src=yt`, the next video, end screens. (shorts-growth.md §4.)
6. **Every description carries the one-line AI disclosure, in voice, linked to the full account; Studio's
   "altered or synthetic content" is set to Yes.** The label costs no reach. (using-ai.md §0; shorts-release.md §4;
   platform-playbooks.md §3; shorts-growth.md §6.)
7. **Setup only. Never the twist, never the ending.** (Kai, 2026-10-22, in apps/site/README.md.)
8. **Name the decision, not the technology; aim the anger at who benefits.** If a description mentions AI, jobs or
   money, someone chose it and someone gained. (the-reader.md rules 5–6.)
9. **Never tell the viewer they've been fooled.** Show the trick being run on someone else. (the-reader.md rule 2;
   chief-of-staff plan §6.)
10. **Write one line people would forward or argue about.** The goal is sends and the pub argument, not views.
    (shorts-growth.md §3 "Sends"; the-reader.md rule 8; chief-of-staff plan §2.)
11. **Only claims the story's own may-say list allows, with the source in the pinned comment.** (Each story's
    `story.md` "What we may and may not say"; shorts-growth.md §4, pinned comment "for a source note".)
12. **Don't look templated.** Vary the shape of each description; a named series, written words and our own music
    are what read as authored, and mass-produced AI is what YouTube demonetises. (shorts-growth.md §6.)

From the first drafting round (`docs/youtube/drafts/2026-11-12-first-four.md`); each cites the repo doc it came from.

## Traps

- **The tool server reads `.env` on every token refresh**, so fixing `.env` mid-session works. A
  `TOKEN_REVOKED` error means re-run the login. If it happens weekly, the Cloud app is still in "Testing".
- **A read straight after an update can show the OLD text** for a few seconds. Re-read before calling an update
  failed. **Tags come back sorted alphabetically**, so compare them as a set, not in order.
- **Pinned comments and a Short's Related video can't be set through the API.** They're a Studio click each,
  listed in the draft file's "Studio steps".
- **The Shorts URL check doesn't work from here.** `youtube.com/shorts/<id>` redirects to an EU cookie
  wall, so use `isShort`.
- **Sign in as badcode.tv@gmail.com**, the account that owns the channel. The Cloud project (Bad Code
  YouTube) belongs to Kai's account, which is fine.
