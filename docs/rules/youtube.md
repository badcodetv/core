# YouTube: standing rules
> Moved out of Kai's per-machine memory on 2026-11-18 (the context reset). Mechanics and working habits only.
> Originals: `archive/messy-context-2026-11-17/memory-kai/`. Procedure: the `youtube-channel` skill; record: `docs/youtube/`.

## The tool [youtube-mcp]

`packages/youtube-mcp` (Kai, 2026-11-11) manages the channel: list, get, upload, update, thumbnail, playlists,
categories. Connected 2026-11-12 (Cloud project "Bad Code YouTube", channel Badcode @badcode-tv).
- **Upload private by default.** Set unlisted / public / `publishAt` only when Kai or Jack asks for that video. Going
  public is a human click and does not need automating.
- **AI label on every video** (default on; `youtube_label_ai`). The API accepts `containsSyntheticMedia` but never
  reads it back, so `docs/youtube/log.jsonl` is the record.
- Titles are Kai's and Jack's call; descriptions and tags are written for growth from the repo playbooks.

## Public is final [youtube-public-is-final]

YouTube cannot replace a video's file (not by API, not in Studio). A new cut is a new video ID at zero views.
- Recut freely while private; go public only on a locked cut.
- After public: small fixes through the Studio editor (it can only remove: trim, cut, blur, swap music); a real recut
  is a new upload, with the old video pointing at it.

## Other platforms are parked [release-tool-parked]

Kai, 2026-11-12: YouTube only until all the content is on it; then one release tool (official APIs where allowed,
written manual steps where not), with the YouTube channel as the reference. Research: `docs/marketing/release-automation.md`.
Don't start Meta / TikTok / music-platform tooling unprompted, and re-check the research when it reopens.
