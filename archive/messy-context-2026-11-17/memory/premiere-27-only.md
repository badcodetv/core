---
name: premiere-27-only
description: Jack 2026-11-16: use only the newest Premiere (27.0.0, project Version 46); when Premiere converts a project, keep the new copy under the ORIGINAL name and delete the old one, never leave _1 files
metadata:
  type: user
---

Jack, 2026-11-16: "can we just have all of them in 2027 premire as in the latest one and delete the old ones, i dont want multiple versions for no reason", then "please clean up for all of them".

Premiere on Jack's machine is now **27.0.0** (`premiere_status` appVersion). Project format stamp (`zcat x.prproj | grep -o '<Project ObjectID="1" ClassID="[^"]*" Version="[0-9]*"'`): 43 = Pro 25.x, 45 = 26.x, 46 = 27.

Done 2026-11-16: 14 pairs swapped (newest copy renamed to the original name, old copy + its .prin deleted; the three empty "no master recording*.prproj" deleted, the real one is no-master-recording.prproj). Repo scene.json / agreed lists now point at the original names. ~100 projects are still Version 43; each converts when next opened.

**Why:** duplicates confused which project is live; keeping the original name keeps every repo path and Drive list valid.

**How to apply:** after opening any project in Premiere, if it made a `name_1.prproj`, close Premiere, delete the old file and rename the copy back (Premiere must be closed for the rename). Kai must be on Premiere 27 too: an older Premiere cannot open these projects; anything pushed to Drive needs that.

Supersedes [[jack-uses-premiere-pro-25-6]].
