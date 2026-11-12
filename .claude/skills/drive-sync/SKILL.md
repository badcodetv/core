---
name: drive-sync
description: Use to push or pull ONE story's Premiere folder between this machine and its folder in the shared Google Drive ("Badcode - Official"), to check what would move, to hand the baton over (or take it), and to record which local folder holds a story on this machine. Triggers on "here's where my karen story lives", "my <story> is in <folder>", "my Karen music folder is …", "push karen music", "pull the camping story", "sync <story> with Drive", "is <story> in sync", "what's on Drive", "I'm handing over <story>", "I've got the baton for <story>", "where is <story> on this machine", "set up the drive tool", "add a story to Drive".
---

# drive-sync

The tool is `scripts/drive/drive.sh` (rclone underneath); its manual is `scripts/drive/README.md`. Read the
README once for the details; this is the procedure.

## The two maps

- **Shared, in git:** `scripts/drive/folders.json`, story name -> its Google Drive folder ID. Same for everyone.
- **Per machine, gitignored:** `badcode.local.json` at the repo root, `"stories"`, story name -> the folder
  that holds it on THIS machine. Kai's and Jack's are different and that is fine: nobody moves or renames
  their folders to suit the tool. `scripts/drive/localmap.py` reads and writes it.

## Sharing timelines between machines

Cut files (`edl.json`) and `scene.json` hold full paths from whichever machine wrote them. Each story in
`folders.json` lists its `homes`: every folder it has lived in on anyone's machine. The scene and lip-sync
tools (`scripts/scene/*`, `scripts/lipsync/*`, `run.mts`) pass what they load through
`scripts/drive/localmap.py` `localize()`, which re-points any path inside a story's home at this machine's
folder for that story. Files on disk are never rewritten. So: Jack's cut opens on Kai's machine and Kai's on
Jack's, once both have `where`d the story. **After a `where` that adds a new home, commit and push
`scripts/drive/folders.json`**, or the other machine can't read cuts written here.
Not covered: GPOM's one-off cut scripts under `scripts/gpom/` (their paths are in the code), and command lines
stored as text (scene.json `cut.script`). Rerun those on the machine that wrote them, or fix the path by hand.
Check: `python3 scripts/drive/test_localmap.py`; one path: `python3 scripts/drive/localmap.py path "<path>"`.

🛑 **Never `ls` a path read from a cut file or scene.json.** It names the writer's machine (`/mnt/d/…` is
Kai's; Jack has no D:). To ask "is the media here?", run
`python3 scripts/drive/localmap.py check <scene.json> <edl.json> …`: it localizes every path and reports
found / missing / story not mapped. A missing `renders/` file is expected (never synced). On 2026-11-10 a raw
`ls /mnt/d` made Claude tell Jack a fully pulled story was missing.
Provenance follows the same map: `prov.py` (check / freeze / cards) localizes, and a shared story's file gets
ONE card in `docs/provenance/cards/` whichever machine made it (`flow-mcp` `prov.ts` matches).

## "Here's where my <story> lives"

When someone tells you in their own words where a story sits on their machine ("my Karen story is in
C:\Users\jackt\OneDrive\Desktop\Youtube Vids\Karen", "Camping music lives in /mnt/c/.../camping"):
1. Work out which story they mean (`drive.sh list`). If it could be two (Karen Music or Karen Story), ask.
2. Run `scripts/drive/drive.sh where <story> "<their folder exactly as given>"`. It checks the folder exists;
   if it doesn't, read the error back and ask them to check the path. Don't hunt for a lookalike.
3. If it printed "added this machine's folder to <story>'s homes", commit and push `scripts/drive/folders.json`
   alone (`git add scripts/drive/folders.json && git commit -m "<Name>'s <story> folder" && git push`), and say so:
   that's what lets the other machine open cuts made here. Nothing else gets committed with it.
4. Say what's recorded, then offer `status <story>` to show what a pull or push would move.
They never need to type the command themselves.

## 🛑 Never guess a local folder

If the story is not in this machine's map, the tool exits 3 with `NOT SET`. Then **stop and ask the person**:
*"Which folder on this computer holds <story>?"* Do not search the disk and pick one, and do not assume
`D:\badcode-videos\<story>`. When they answer, record it with
`scripts/drive/drive.sh where <story> "<their folder>"` (it checks the folder exists), then carry on.
Same if they name a story with no row in `folders.json`: ask which Drive folder it is (its link), and add
the row (key = a short story name such as `bank-robbery-music`; ID = the end of the folder's URL).

"Karen" alone is ambiguous: ask whether it's Karen Music or Karen Story. Run `drive.sh list` to show the options.

## Procedure

1. `scripts/drive/drive.sh list`: every story, its Drive folder, and its folder here (or NOT SET).
2. `scripts/drive/drive.sh status <story>`: what a push and a pull would each copy. Changes nothing. Show
   both counts. Nothing moves without `--go`.
3. Push or pull with `--go` only when the person asked for that direction. It copies only, never deletes,
   and replaces a file only with a newer copy. A long upload can run in the background; a rerun is always safe.
4. Ignore the Drive `Misc` folder: it holds what isn't an official story, and is never synced.
5. 🛑 **Push only what the cut uses** (Jack, 2026-11-10): read the `status` list before `--go`. A round sends
   its own new files (edl, any clip it brought in) and the saved `.prproj`; trial cuts, discarded takes and test
   renders nobody chose stay local. **Previews never travel**: `exclude.txt` skips `preview*.mp4`, `*-preview.mp4`
   and any `_local/` folder, so the other machine remakes a preview from the edl (its scene's `trail.json`
   `rebuild`). A new script that writes a look-only video names it `preview…` or puts it in `_local/`.

## Agreed cut only (Jack, 2026-11-10)

A story with a list in `scripts/drive/agreed/<story>.list` is uploaded as its **agreed cut only**, never the
whole folder. "Push the agreed cut for <story>", "carry on uploading to Drive", "how are the Drive uploads":
`scripts/drive/push-agreed.sh <story>` (dry run: N listed, M to push), then `--go`, in the background; it ends
with copied / errors / left. Do NOT answer "push <story>" for such a story with `drive.sh push`: that sends
thousands of old-cut files. Ask which they meant if unsure. A new agreed cut means a new list: build it from
the sequence's `.bridge/state-<sequence>.json` (jq line in the script's header) and commit it. Details and the
current lists: `scripts/drive/README.md`, "Agreed cut only".

## The baton

Kai and Jack agree out loud who holds each story. There is no lock in the tool, and none should be built.
- **Handing over:** dump any timeline-page notes into the scene's `feedback/` (scene-timeline's rule),
  commit and push git, then `push <story> --go`, then `status` again to show 0 to push.
- **Taking over:** `git pull`, `status <story>`, `pull <story> --go`, then open the project or the timeline.
- If `status` shows files both ways on a `.prproj`, stop: two people edited it. Ask which one wins.

## Traps

- 🔴 **Uploads crawl (50–200 KB/s, 5–10 min stalls, no errors at `-v`) = rclone's shared Google app ID.**
  Found 2026-11-12: the remote `badcode:` had no `client_id`, so it used rclone's built-in one (Google
  project 202264815644), shared by every rclone user in the world. Google rations it: a `-vv` test showed
  `403 rateLimitExceeded … defaultPerMinutePerProject` on nearly every call, with the pacer backing off to
  17 s between chunk sends. The line was fine (YouTube took 511 MB at 3 MB/s the same hour). Fix: our own
  OAuth client (Google Cloud → enable the Drive API → OAuth client ID, type Desktop app), its `client_id`
  and `client_secret` in the `badcode` remote, then `rclone config reconnect badcode:`. Test before any big
  push: `rclone -vv … copy <50 MB file>` and grep for `rateLimitExceeded`.
- **rclone from apt is old** (1.53.3, 2020 on this machine). Prefer a current rclone from rclone.org.
