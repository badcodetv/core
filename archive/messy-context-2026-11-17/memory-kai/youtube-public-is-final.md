---
name: youtube-public-is-final
description: "2026-11-12 Kai: a public YouTube upload is final; the file can never be replaced (only cut in Studio), so lock the cut while private"
metadata:
  node_type: memory
  type: project
  originSessionId: 33a4fdac-9db2-4eb1-a4f9-b5fb47322a30
  modified: 2026-11-12T16:05:51.174Z
---

YouTube cannot replace a video's file, not through the API and not in Studio. A new cut is always a new video ID, which starts at zero views, comments and links. The Studio editor can only *remove* material (trim, cut a section, blur, swap music), and does keep the views.

**Why:** 12 Nov 2026, replacing GPOM's 4 Nov private upload (OaP0RthL_0Q) with the final cut. Kai: "as part of our release strategy we need to understand that uploading to YouTube is final."

**How to apply:**
- Upload private and recut freely while private: a re-upload costs nothing then.
- Only go public (a human click) once the cut is locked.
- After public: small fixes go through the Studio editor; a real recut means a new upload, with the old video pointing at it (card or end screen, pinned comment, description line), and the old video kept or hidden.

Related: [[youtube-mcp]].
