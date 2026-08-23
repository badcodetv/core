---
scene: bulletin
cut: 4
canon: story.md scene 7
built: 2026-08-23
runtime: 104s (13 beats × 8s)
scratch: /mnt/c/Users/kai/Desktop/gpom-bulletin/
---

# Cut 4 — `bulletin`

**The collapse, told entirely as news.** Three stories from the song — the redundancies, the
banks, the autonomous army — reported across years that we never date on screen. The degradation
is in the *signal and the room*, never in a caption.

Kai's framing, 2026-08-22: *"we should just cut from news report to news report to news report,
and maybe there's like a year between them… each time it moves on, there's a kind of marked
degradation in the news report quality and studio, like everything is going downhill."*

---

## 1. The shape — four phases, thirteen beats

| # | Beat | Plate | Phase |
| --- | --- | --- | --- |
| 1 | `p0-newsreader` | `bulletin-p0-newsreader.jpg` | **0 — the bulletin itself** |
| 2 | `p1-london-a` | `bulletin-p1-london-a.jpg` | **1 — the crowds** |
| 3 | `p1-london-b` | `bulletin-p1-london-b.jpg` | 1 |
| 4 | `p1-shibuya` | `bulletin-p1-shibuya.jpg` | 1 |
| 5 | `p2-station` | `bulletin-p2-station.jpg` | **2 — emptying** |
| 6 | `p2-airport1` | `bulletin-p2-airport1.jpg` | 2 |
| 7 | `p2-airport2` | `bulletin-p2-airport2.jpg` | 2 |
| 8 | `p3-studio-man` | `bulletin-p3-studio-man.jpg` | **3 — the studio dies** |
| 9 | `p3-studio-empty` | `bulletin-p3-studio-empty.jpg` | 3 |
| 10 | `p3-collapse` | `bulletin-p3-collapse.jpg` | 3 |
| 11 | `p3-dark` | `bulletin-p3-dark.jpg` | 3 |
| 12 | `p4-london` | `bulletin-p4-london.jpg` | **4 — where are the humans** |
| 13 | `p4-shibuya` | `bulletin-p4-shibuya.jpg` | 4 |

Plate→beat provenance was **measured**, not remembered: every finished clip's first frame was
matched against every still in the scratch folder. Worth doing — five of the thirteen came from
an earlier round and the mapping was no longer in anyone's head.

Rebuild: `assemble.sh` in the scratch folder. Stream-copy concat, so every beat must already be
1920×1080 / 24fps / 8s.

---

## 2. The rulings that shaped it

**Only phase 1 shows what the news actually *is*.** Phases 2 and 3 show nobody and nothing, and
the voiceover carries them. Showing the story three times would flatten it.

**Start full so the emptying can happen.** The first attempt at this scene shot a shop window on a
dead empty street — which is scene *8's* image. Kai's Piccadilly instinct was the correction: the
crowd has to exist before its absence means anything.

**Three rooms, not one studio.** Canon puts the degradation in the *signal*, not the set, so
locking to a single studio was never required. Ruled by Kai after the question was put with that
evidence.

**The phase-1 newsreader is the phase-3 studio, intact.** Same slatted back wall, same round
columns, same lighting truss with square softboxes, same domed pendant lamp. Phase 3 then stops
being generic decay and becomes *that room, later* — which costs nothing extra to shoot.

**The callback replays the exact camera position.** `flow_edit_image` cannot re-compose, and that
is precisely why it is the right tool here: derived off the original plate, it holds the framing,
so "same place, later" reads without a word. Daylight, empty, weeds, litter, screens dead.

**`p4-shibuya` keeps one red banner strip still lit on an otherwise dead screen** — an emergency
still being flagged to an empty crossing.

---

## 3. Load-bearing text goes in the PLATE

Kai, 2026-08-23, on the empty red bar: *"it just looks like a red bar across the bottom."* He was
right — it was a coloured band with nothing to say.

🔴 **Do not ask Veo to render text, and do not reach for post first.** The route that worked:

1. **Nano Banana Pro sets the type** into the still — `200,000 OFFICE WORKERS FIRED`, correct
   first try on both candidates, correctly curved to a curved screen. **Images do not bill.**
2. **Veo then holds it.** One Lite clip, 10 credits, proved it: legible and unchanged at 0s, 2s,
   4s, 6s and 7s, screen swing **4/255**. The other two straps came back at swing **2** and **0**.

Post-compositing (`docs/flow/post-production.md` §3.10) stays the fallback for text that must be
pixel-exact, must change later, or whose plate cannot be regenerated — and note it needs a
per-frame track, because even a "static" clip creeps 34–66px.

The number is **200,000**, matching canon. Once it is rendered as on-screen text it stops being
flexible, so it was confirmed with Kai before a credit was spent.

---

## 4. Holding a screen — the whole technique

**Veo animates a screen whether you ask it to or not.** Unheld, screens grew into blown-out
lightboxes with lens flares, or switched off mid-clip.

The motion prompt that works, in this order:

1. **Name the real-world motion first, and hard** — rain stippling the road and breaking up the
   screen's reflection; umbrellas rocking; a figure shifting weight; static rolling.
2. **Then hold the screen explicitly** — *"the screen keeps showing exactly the same picture from
   the first frame to the last: the same size, the same brightness, no flicker, no flare, no
   blowing out, no cut to another shot, no change of channel."*
3. **Then** *"the camera stays where it is."*

Measured effect: screen swing fell from **96/255 to under 4/255**.

For a screen meant to read as **dead**, invert the clause — *"stays completely dead matte black…
no shapes, no blocks, no letters, no logos, no picture, no glow, no flicker"* — and say what
should NOT appear, positively and by name.

---

## 5. What cost the most, and why

**A plate with an ambiguous bright patch is a paid re-roll.** `p4-london`'s screen carried pale
patches of damage. Veo read them as content and lit them into a white graphic — twice, **80
credits**. One `flow_edit_image` flattening the panel to matte black killed it for free. Now
rule 19 in `docs/flow/README.md`.

**The gate has a ceiling.** Sealing stops Veo *inventing*; it does not stop it *re-interpreting*.
`p4-shibuya`'s fine static damage came back scrubbed clean on Lite and re-damaged elsewhere on
Fast — **neither tier reproduced it**. Fine texture is not safe; rendered text is.

**A cluttered project hands back old media as if it were new.** In a project holding ~50 clips,
one call returned **twelve** candidates, all byte-identical to the previous day's takes, with no
error. A second call animated a *different plate* than the one passed. **One fresh project per
shot** — free, and it makes the mis-pick impossible. Law 19.

**Never generate a diagnostic image into the project you are about to animate in.** A throwaway
"empty grey room" ping test was picked up as the start frame: the clip opened on that room,
dissolved into a different studio and rendered the strap as garbled Cyrillic. **40 credits.**
Law 21.

**Upload from the WSL filesystem, never `/mnt/c`.** Four consecutive calls died with the picker
never finding the file, across two Chrome instances, three projects and two filenames. A free
`flow_generate_image` (no upload) worked throughout — that is the cheap probe that isolates it.
Copying the file into the WSL filesystem fixed it first try. Intermittent, not absolute. Law 20.

---

## 6. Grade and finish

`hold_grade.py` holds colour on a p90 anchor and delivers 1080p — but 🔴 **it fails when the
brightest object in frame is a screen that legitimately changes**, because it then measures
*content* rather than lighting.

Measured here: **3 of 7** clips tripped it. `p3-dark` reported **97.2/255** of "drift" — that was
the static, not the lighting — and slammed both gain clamps. `p1-london-b` hit the 1.140 ceiling,
`p3-collapse` the 0.880 floor.

**When it clamps, fall back to a plain upscale:**

```bash
ffmpeg -i in.mp4 -vf "scale=1920:1080:flags=lanczos,setsar=1" \
       -c:v libx264 -crf 17 -pix_fmt yuv420p -an out.mp4
```

The four strap/newsreader takes measured 0–4/255 of drift, so there was nothing to correct and
they went straight to lanczos.

**Still owed:** a monotonicity guard in `hold_grade.py`, so a non-monotonic "drift" is recognised
as content and refuses the correction rather than clamping.

---

## 7. Superseded — do not re-run

| Dropped | Why |
| --- | --- |
| `C4-mall1`, `C4-mall2` | Too many empty-transit beats, and a running fountain fought the grain |
| `C4-tokyo1`, `C4-tokyo2` | Anonymous city — replaced by the Shibuya scramble crossing, which reads on sight |
| `b3-wide` (car on a street) | Cut; the beat did not earn its 8 seconds |
| `bulletin-*`, `b1-*` first round | The wrong scene — a dead street, which is cut 5's image |
| `V-LA`, `V-LA2`, `V-LA3`, `LITE-LA` | Superseded London-after rolls; see §8 |

---

## 8. Known defects, unresolved

🔴 **`p4-london` drifts.** Veo would not lock off on that high-angle aerial plate — **four takes
across three prompts and both tiers, all drift**. The mildest was kept (motion 12 against a
locked-off ~5 elsewhere). Adding *"locked-off tripod… no pan, no tilt, no zoom, no drift; the
edges of the frame sit on the same buildings in the last frame as the first"* reduced it and did
not remove it. If it reads badly in the edit, the fix is a post counter-move, not another roll.

🟡 **The two phase-4 callbacks do not rhyme.** Shibuya keeps a lit red bar on a dead screen;
London's screens are fully dead. Offered and not yet done: re-derive `p4-london` with the same
lit-red-strip detail.

🟡 **`p2-airport2` has a real camera drift**, unlike the locked-off rest of phase 2. Inherited
from the earlier round.

🟡 **A "Boots" shopfront is visible** in the `p1-london-b` plate. A release decision for Kai,
separate from whether it generated.

⬜ **No narration exists for this cut, and none has been generated for any cut.**
[`songs/narration.md`](../songs/narration.md) carries written boxes for cuts 1–3 only, still at
`status: draft — nothing generated yet`. So every beat length in all four cuts is a guess,
including the 8s assumed here — and cut 4 needs its boxes written before that guess can be tested.

⬜ **Year cards** (2033/34/35) are still unruled — as is cut 3's `2032` card.
