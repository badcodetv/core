---
name: first-release-four-stories
description: "2026-10-22 Kai ruling — the first release, in order, is GPOM, Camping, Karen, The Bank Robbery (film + song each on YouTube); MMT is out; badcode.tv = apps/site static page on Cloudflare"
metadata:
  node_type: memory
  type: project
  originSessionId: 85fe9802-2b47-439c-90db-5bf9dedcfc6a
  modified: 2026-10-22T15:02:47.039Z
---

Kai, 2026-10-22: the four stories released first are, in this order, **GitPush Origin Master, Camping,
Karen Will Lead the Revolution, The Bank Robbery**. On the site the title is written "Git Push Origin Master" (Kai: two words). The Bank Robbery replaces The Magic Money Tree (mid-recut, back to the pool).
Each ships as a film and a song on YouTube (eight videos); the songs also go to SoundCloud and Spotify.
Canon of the list: docs/stories/gitpush-origin-master/ep1.md.

The website for now is a one-page map to the content and socials: `apps/site/` (plain static HTML,
no build), deployed as a static-assets Cloudflare Worker via `apps/site/wrangler.jsonc`. It is NOT apps/web.

**Why:** time to start releasing; the site just has to point people at the videos and accounts.
**How to apply:** when a video or account goes live, swap its `<span class="soon">` for a link in
apps/site/public/index.html. Related: [[chief-of-staff-marketing]], [[website-reset-initiative]].
