# Drive push / pull for Premiere folders

Instead of Drive Desktop syncing everything, push or pull **one** Premiere folder when you mean to.

```
scripts/drive/drive.sh list                    # every story: its Drive folder, and its folder on THIS machine
scripts/drive/drive.sh where karen-music "D:\badcode-videos\karen-music"   # record where a story lives here
scripts/drive/drive.sh status karen-music      # what would move, both ways (changes nothing)
scripts/drive/drive.sh push   karen-music --go # this machine's karen-music folder -> Drive "Karen Music "
scripts/drive/drive.sh pull   karen-music --go # Drive -> this machine
```

- **Copy only, never delete.** A file is replaced only by a newer copy (`--update`). Without `--go` every command is a dry run.
- **Skipped (exclude.txt):** Premiere preview caches, Auto-Save, `.bridge/`; anything a script rebuilds
  (a cut's `segs/` and `picture.mp4`); and `renders/` (finished exports: re-export from the project).
  Sources, projects, edl.json and preview.mp4 go up.
- **Built not to hang:** a connection that goes quiet for 60 s is dropped and retried, the run retries
  5 times, and it ends with `done: N file(s) copied, nothing failed` or `FAILED ... rerun the same command`.
  A rerun is always safe: what's already there is skipped. Every real run is logged to `~/.cache/badcode-drive/`.
- **`status` counts everything:** it prints how many files each way and the first 20, never a silent cap.
- **Two maps.** `folders.json` (shared, in git): story name -> Drive folder ID (IDs, so a rename or a trailing space on Drive can't break it).
  `badcode.local.json` `"stories"` (one per machine, gitignored): story name -> the folder that holds it on THIS machine.
  Kai's and Jack's folders can be named and placed however each likes. A story with no local entry stops with `NOT SET` and
  asks; nothing is guessed. In Claude Code the `drive-sync` skill asks you and records the answer.
- **Timelines work on both machines.** Each story's `homes` in `folders.json` lists every folder it has lived in on anyone's
  machine (`where` adds yours: commit `folders.json` after). The scene tools translate paths in cut files and `scene.json`
  as they read them, so a timeline made on Jack's machine opens on Kai's and back. Nothing on disk is rewritten.
  Details: `localmap.py`; test: `python3 scripts/drive/test_localmap.py`.
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
5. **Say where each story lives on your machine**, wherever that is (leave your folders where they are):
   `scripts/drive/drive.sh where camping-story "C:\Users\Jack\OneDrive\Desktop\YouTube vids\Camping story"`.
   One line per story you hold. It's saved in `badcode.local.json` (yours only, never committed). For a story you
   don't have yet, make an empty folder wherever you like, `where` it, then `pull`.
6. **Try it:** `scripts/drive/drive.sh list`, then `status <story>`. Nothing moves without `--go`.

Or, in Claude Code inside the repo, just say "pull karen music" / "push karen music".

**A new story:** make its folder inside "Badcode - Official" on Drive, copy the folder ID from the end of its URL, and add a row to `folders.json`. The key must match the local folder name.
**Ignored:** the Drive `Misc` folder is for anything that isn't an official story or music video. It has no row and is never synced.
