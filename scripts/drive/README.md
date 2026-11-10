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
- **Fixed 2026-11-10:** `status` used to stop after the push side when that side had nothing to copy, so files waiting on Drive were never listed. It now always shows both sides.
- **Baton:** Kai and Jack agree out loud who holds each story. Whoever holds it pushes when they hand it over; the next holder pulls before they open the project. The tool has no lock and doesn't need one.

## Setting it up on a machine (Kai, Jack, Tom)

Each person signs in with **their own** Google account, the one "Badcode - Official" is shared with.
Files you upload count against your own Drive storage.

1. **Install rclone.** Windows `winget install Rclone.Rclone` (then open a new terminal), Mac `brew install rclone`, Linux/WSL `sudo apt install rclone`.
2. **Bash and Python.** On Windows, use WSL or Git Bash, plus a real Python (`winget install Python.Python.3.12`; the Microsoft Store `python3` stub doesn't work). A Mac has both built in.
3. **Pull the repo.**
4. **Sign in once:** `rclone config create badcode drive scope drive`. A browser opens: pick your Google account, click Allow.
   Check it worked: `rclone lsf badcode: --drive-root-folder-id 1aqkmEhj64V56V3TnyqbzuhUs8cGjWrym --dirs-only` should list Camping Music, Karen Music, Misc and the rest.
5. **Tell the script where your videos live**, unless it's `/mnt/d/badcode-videos`. Put this in your shell profile (`~/.bashrc`):
   WSL `export BADCODE_MEDIA_ROOT="/mnt/d/badcode-videos"` · Git Bash `export BADCODE_MEDIA_ROOT="/d/badcode-videos"` · Mac `export BADCODE_MEDIA_ROOT="$HOME/badcode-videos"`.
   Each story is a subfolder named as in `folders.json` (`karen-music`, `camping-story`...).
6. **Try it:** `scripts/drive/drive.sh list`, then `status <folder>`. Nothing moves without `--go`.

Or, in Claude Code inside the repo, just say "pull karen music" / "push karen music".

**A new story:** make its folder inside "Badcode - Official" on Drive, copy the folder ID from the end of its URL, and add a row to `folders.json`. The key must match the local folder name.
**Ignored:** the Drive `Misc` folder is for anything that isn't an official story or music video. It has no row and is never synced.
