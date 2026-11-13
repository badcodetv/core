# Karen story on Drive (Jack, 2026-11-13)

Jack: "Karen vid_1.prproj please only upload what is neccary to this file/cut, not the whole folder".

- `karen-story.list` holds `Karen vid_1.prproj` plus every file it references inside `Karen VID NEW!` (105 paths). It is pushed with `scripts/drive/push-agreed.sh karen-story --go`.
- `karen-story.outside.list` holds the 174 files the project references outside that folder:
  - `Karen/narration-v2`
  - `Karen/narrator-auditions`
  - `Karen/vol 4`
  - one file in `songs/Karen`

  Paths are relative to `Desktop\Youtube Vids\animation`. They are on Drive under **Karen Story/_outside/**, with the same structure, 800 MB, checked file for file. Uploaded with:
  `rclone copy "<animation>" badcode:_outside --drive-root-folder-id <karen-story drive id> --files-from karen-story.outside.list --update`
- **Opening on another machine:** pull Karen Story, open `Karen vid_1.prproj`, and when Premiere asks to relink, point it at one file under `_outside/Karen/narration-v2/…`. The rest relink from the same structure.
- 🔴 Kai holds the Karen baton (2026-11-13 meeting). This only added files to Drive and deleted nothing.
