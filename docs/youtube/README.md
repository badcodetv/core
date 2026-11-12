# YouTube: managing the channel from Claude

**The procedure is the [`youtube-channel` skill](../../.claude/skills/youtube-channel/SKILL.md)**; this page is the tool and its setup.

Kai, 2026-11-11: stop clicking through YouTube Studio by hand. The `youtube` MCP server
(`packages/youtube-mcp/`) manages the BadCode channel through Google's official **YouTube Data API
v3**: upload, edit titles / descriptions / tags, thumbnails, playlists, and a list of every video.

**Going public stays a human click in Studio.** Uploads land **private** by default; Kai or Jack
flips them public. (The tools can set unlisted / public / a scheduled release, but only when one of
you has asked for that video in words.)

## What's in this folder

| File | What |
| --- | --- |
| `channel.json` | The repo's copy of the channel: every video's title, description, tags, privacy, schedule, AI label. Rewritten by every `youtube_list_videos` and after every change. View counts are left out on purpose (they'd fill git with noise). |
| `log.jsonl` | One line per change made through the server (upload, edit, thumbnail, playlist), with the time and what changed. Appended, never rewritten. |

## The tools

| Tool | Does |
| --- | --- |
| `youtube_status` | Set up? Signed in? **Which channel** (check it says BadCode). Gives the next setup step if not. |
| `youtube_list_videos` | Every video, private and scheduled too, newest first, with counts, `isShort` (vertical/square and ≤3 min, from the file; the API has no Shorts flag) and `aiLabel`. Refreshes `channel.json`. |
| `youtube_get_video` | One video in full. Takes an id or any YouTube / Studio link. |
| `youtube_upload` | Upload a file (WSL or `D:\…` path; big files fine, resumable). Private by default, no subscriber ping. The **AI label** ("altered or synthetic content") is **on by default** (Kai, 2026-11-12: every video carries it). Optional thumbnail and playlists. |
| `youtube_label_ai` | Puts the AI label on every video the log has no record of labelling (e.g. Jack's hand uploads). 🔴 YouTube accepts the label but never reads it back, so `log.jsonl` is the only record of which videos have it. |
| `youtube_update_video` | Change only the fields you pass; the rest is kept. Tags are replaced as a whole list. |
| `youtube_set_thumbnail` | PNG/JPEG under 2 MB, 1280×720 ideal. Needs the channel phone-verified. |
| `youtube_playlists` | List, create, add a video. |
| `youtube_categories` | Category ids. Default on upload is `1` (Film & Animation); `10` Music, `25` News & Politics. |

Before writing any title or description: [`the-reader.md`](../marketing/the-reader.md),
[`voice.md`](../voice.md), [`using-ai.md`](../using-ai.md), and **no spoilers** (setup only, never
the twist). Drafting and checking public copy is the chief-of-staff's `marketing-producer` and
`marketing-gatekeeper`.

## Setup (once, about 10 minutes)

All in a browser signed in as **badcode.tv@gmail.com**.

1. **Make a Google Cloud project.** https://console.cloud.google.com → project picker → *New
   project* → name it `badcode-youtube`.
2. **Turn the API on.** *APIs & Services → Library* → search **YouTube Data API v3** → *Enable*.
3. **Consent screen.** *Google Auth Platform* (older consoles: *OAuth consent screen*) → *Get
   started*: app name `BadCode`, support email badcode.tv@gmail.com, audience **External**,
   contact email the same.
4. 🔴 **Publish the app.** *Audience* → *Publish app* → status **In production**. Left in
   "Testing", Google kills the sign-in every **7 days** and the tools stop working with
   `TOKEN_REVOKED`. Unverified is fine: it's only our own account.
5. **Make the client.** *Clients* → *Create client* → type **Desktop app** → name `badcode-claude`
   → copy the **Client ID** and **Client secret**.
6. **Put them in `.env`** at the repo root (git-ignored; never commit them):
   ```
   YOUTUBE_CLIENT_ID=….apps.googleusercontent.com
   YOUTUBE_CLIENT_SECRET=…
   ```
7. **Sign in.** In Claude: `! npx tsx packages/youtube-mcp/src/login.ts`. A Google page opens
   (or copy the printed link). Pick the **BadCode channel**. You'll see "Google hasn't verified this
   app" → *Advanced* → *Go to BadCode* → allow. The sign-in is saved to
   `~/.config/badcode/youtube-token.json` (outside the repo, private to this machine).
8. **Restart Claude** so it loads the new server, then ask for `youtube_status`. It should name
   the BadCode channel.

**Jack's machine:** the same Client ID and secret go in his `.env` (pass them privately, not in
git or chat); he runs step 7 himself. Each machine has its own sign-in.

## Limits and traps

- **Quota:** 10,000 units a day per Cloud project; a read costs 1, an edit about 50. Uploads used to
  cost 1,600 (about 6 a day), and reports from 2025–26 say they moved to their own bucket of about 100
  a day. Check *APIs & Services → YouTube Data API v3 → Quotas* if a `quotaExceeded` appears. It
  resets at midnight Pacific time.
- **The private lock (unverified):** Google used to force every upload from an unverified Cloud
  project to private, whatever you asked. As of late 2026 that seems to have been lifted, but nobody
  had checked it on our channel when this was written. It doesn't matter much, since we upload
  private anyway. `youtube_upload` returns `privacyAsRequested`, so a public request that comes back
  private shows the lock is on. The fix is Google's *YouTube API Services audit* form.
- **Updates wipe what they don't mention.** YouTube's own update call replaces a whole section. The
  tool reads the video first and keeps every field you didn't pass, so this only bites someone
  calling the API another way.
- **Studio-only:** end screens, cards, monetisation and copyright claims have no API. Those stay in
  Studio.
- Uploads don't make a provenance recipe card: the file was already carded when it was made.
  `log.jsonl` records which file went up as which video.
