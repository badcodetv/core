# The Rules (a BadCode short)

> **A short is a project like a story or a music video** (Kai, 2026-11-10): its own ID
> (`short-the-rules`), its own Drive folder (`Shorts/The Rules`, row in `scripts/drive/folders.json`),
> and each machine points the ID at its own folder (`drive.sh where`). Made with the `new-short` skill,
> which runs `new-scene` on the one scene in `scenes/the-rules/`. The running list of every short is
> [`docs/marketing/badcode-shorts.md`](../../marketing/badcode-shorts.md) (#24).

## The idea (Kai, 2026-11-10)

The balaclava gang sit looking up at a massive stack of paper labelled THE RULES. *Are the rules
working?* "Let's look out the window." Outside: utter chaos. Back inside, the gang tears up the rules.
With music: a new Suno track of its own, about rule-breaking, not the Bank Robbery song.

Kai: *"There's a lot of rules and a lot of them are sensible. But at the same time, a lot of them are
not sensible. And how do we know, how do we measure this? Let's look out the window. Is everything
working? If everything was working, then excellent, the rules are good. But it's not, so clearly
something is wrong about the rules. So full permission granted to go and look at the rules and change them."*

**Good rules stay:** "don't murder people" is not in question. **Rules to challenge:** the ones that shield the people who wrote them. Kai's example (2026-11-10, replacing a corporate-liability one): **tax havens**, a company booking its profits on an island that flies our flag and paying little or no tax. Wording ⬜ checked before it goes on screen (`scenes/the-rules/picks.md`).

**The real target:** deference. Working-class people hand their say over the rules to credentialed
establishment figures, and it isn't working. A challenge to the rule-makers, and permission to the
viewer.

## State (2026-11-11: CUT)

| What | Where | Status |
| --- | --- | --- |
| The cut | Premiere `the-rules.prproj`, sequence **`short-the-rules-1-rules-r3`** (27.6 s, 1080×1920, 24 fps) | ✅ CUT (Kai, 2026-11-11: *"it's a cut… brilliant"*); frozen to `scenes/the-rules/final.json` |
| Timeline page | https://claude.ai/artifact/NxaG6N48KfExaHi6aL1z8E (round 5 = Premiere r3 frame for frame) · built by `scripts/shorts/the_rules_cut.py` | ✅ |
| Clips page | https://claude.ai/artifact/GE8koyRsGnm3m3fNiVJTYY | ✅ |
| Beats, picks | `scenes/the-rules/picks.md` (every ruling, Kai's words) | ✅ |
| Look | [`look.md`](./look.md) (the gang is FIVE) | ✅ |
| Sound | [`sound.md`](./sound.md): the hymn + the dnb-r3 concrete-stairwell drop | ✅ |
| Release master | `renders/the-rules-master-r3-tagged.mp4` (H.264 17 Mbps, AAC 48k, −14.3 LUFS) on Kai's machine; renders never go to Drive, re-export from r3 | ✅ exported; ⬜ uploaded |
| Tax-haven overlay | `scenes/the-rules/picks.md` | 🔴 owed: the fact check before any text goes on screen |
| Media | `D:\badcode-videos\shorts\the-rules` (Kai) · Drive `Shorts/The Rules` (agreed cut: `scripts/drive/agreed/short-the-rules.list`) | ✅ pushed 2026-11-11 |

## Jack: pulling it onto your machine

1. **Git:** `git pull` in the repo. You get this folder, the cut script, the Premiere preset and the Drive list.
2. **Tell Claude where it lives:** "my The Rules short lives in `<your folder>`". Claude runs
   `scripts/drive/drive.sh where short-the-rules "<folder>"` (and commits `folders.json` so Kai's machine can read your cuts).
3. **Drive:** "pull the rules short" = `scripts/drive/drive.sh pull short-the-rules --go`. You get the `.prproj`,
   the nine clips (each as the Flow original and the `-noaudio` copy Premiere uses), the hymn, both drops and `cut/edl.json`.
4. **Open** `<your folder>\the-rules.prproj` in Premiere and open the sequence **`short-the-rules-1-rules-r3`**. If it asks
   where the media is, point it at your folder once (`video\`, `music\`) and it relinks the rest. r2 is Kai's earlier edit.
5. **The preset (only for making a NEW short sequence; r3 carries its own settings):** copy
   `docs/premiere/presets/BadCode Short 9x16 24 fps.sqpreset` into
   `Documents\Adobe\Premiere Pro\<version>\Profile-<you>\Settings\Custom\`, restart Premiere, and it appears under Custom in New Sequence.
6. **The page preview** never travels: `python3 scripts/shorts/the_rules_cut.py` remakes `cut/preview.mp4` from the clips.
   The release master is re-exported from r3 (`docs/marketing/shorts-release.md`).

Edit r3 only when you hold the baton (say so out loud); push with "push the rules short" (`scripts/drive/push-agreed.sh short-the-rules --go`).
