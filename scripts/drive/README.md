# Drive push / pull for Premiere folders

Instead of Drive Desktop syncing everything, push or pull **one** Premiere folder when you mean to.

```
scripts/drive/drive.sh list                    # which local folder goes to which Drive folder
scripts/drive/drive.sh status karen-music      # what would move, both ways (changes nothing)
scripts/drive/drive.sh push   karen-music --go # D:\badcode-videos\karen-music -> Drive "Karen Music "
scripts/drive/drive.sh pull   karen-music --go # Drive -> D:
```

- **Copy only, never delete.** A file is replaced only by a newer copy (`--update`). Without `--go` every command is a dry run.
- **Skipped (exclude.txt):** Premiere preview caches, Auto-Save, `.bridge/`; anything a script rebuilds
  (a cut's `segs/` and `picture.mp4`); and `renders/` (finished exports: re-export from the project).
  Sources, projects, edl.json and preview.mp4 go up.
- **Built not to hang:** a connection that goes quiet for 60 s is dropped and retried, the run retries
  5 times, and it ends with `done: N file(s) copied, nothing failed` or `FAILED ... rerun the same command`.
  A rerun is always safe: what's already there is skipped. Every real run is logged to `~/.cache/badcode-drive/`.
- **`status` counts everything:** it prints how many files each way and the first 20, never a silent cap.
- **Folder map:** `folders.json`, matched by Drive folder ID (the Drive names differ from the D: names, one has a trailing space). Add a row for a new project.
- ⚠ If two people edit the same `.prproj` between syncs, the newer one wins and the other's changes are lost. Push when you finish a session, pull before you start one.
- **One-time setup:** `rclone config create badcode drive scope drive`, then sign in as kaiyadavenport@gmail.com in the browser link it prints. The Drive folders belong to Jack's "Badcode - Official"; files Kai uploads count against Kai's storage.

## Setting it up on another machine (Jack, Tom)

1. Install rclone: Windows `winget install Rclone.Rclone`, Mac `brew install rclone`, Linux/WSL `sudo apt install rclone`.
   The script also needs bash and python3 (WSL or Git Bash on Windows; built in on a Mac).
2. Pull the repo.
3. Sign in once, with your own Google account (the one the BadCode folder is shared with):
   `rclone config create badcode drive scope drive`. A browser opens, you click Allow.
4. Tell the script where your videos live, if not `/mnt/d/badcode-videos`:
   `export BADCODE_MEDIA_ROOT="/path/to/badcode-videos"` (put it in your shell profile).
5. `scripts/drive/drive.sh list`, then `status`, `pull`, `push` as above.

Or, in Claude Code inside the repo, just say "pull karen music" / "push karen music".
