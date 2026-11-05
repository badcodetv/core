# Layouts: Future Proof "Update Available" theme

The look (picked by Kai 2026-11-05): **Britain is an old computer that has clicked "remind me later"
since 1872.** Every slide is a desktop with a window on it: error boxes, installers, release
notes, tickets, notifications, an image viewer for the pictures. The taskbar clock always reads
**1872** (override with `clock` only for a deliberate gag). The look's warning: it is a
technology joke, and the reader rules say name the **decision-maker**, not the machine. The pop-up
text blames whoever designed the system, never "the computer".

Slides live in `../slides.json` as `{ "slides": [ {...}, ... ] }`. Every slide has `id`
(matching `deck.md`) and `layout`. Text fields take `**bold**` and `\n`. Short meme text is
best: the window is the joke's setup and the button or caption is the punchline.

## Common fields (any layout)

| field | what |
| --- | --- |
| `top`, `bottom` | classic meme caption above/below the window (white, outlined, upper-case). Over 70 characters drops a size. |
| `task` | the taskbar tab label (defaults to `title`) |
| `sticky` | a yellow sticky note on the desktop (Mel's handwriting, an aside) |
| `image` | a picture slot: `{ "file": "mel-booth.jpg", "prompt": "what the picture shows" }`. It is a labelled placeholder until the picture is made and `src` is filled in |
| `reveal` | `{ "field": stepNumber }`: hide a field until that click (0 is shown at once). Fields: `top`, `bottom`, `text`, `sticky`, `footer`, `total`, `side`, `left`, `right`, `highlight`, `window`; `lines` takes the step of the FIRST line, and each line after it is one more click |
| `steps` | total number of clicks on the slide (scenes need this) |
| `dark` | `true` = dark desktop (rare; the bad-news beat) |

## Layouts

- **`dialog`**: one system box. `title` (title bar), `icon` (`error` · `warn` · `question` · `ok` · `info`), `heading`, `text`, `small`, `buttons` (array; the FIRST is the default, outlined), `progress` `{pct, label, err}`, `w` (window width px), optional `image` (puts a picture on the left).
- **`picture`**: an image viewer showing one big picture. `title` (the filename), `image`, plus `top`/`bottom` captions: the classic meme. Optional `side` `{title, icon, text, buttons}`: a small dialog over the picture's corner.
- **`split`**: two windows side by side (then/now, no/yes, bank/ballot). `left` and `right` each `{title, label, image, heading, text, lines, buttons}`.
- **`release`**: release notes / patch notes. `title`, `heading`, `lines` (strings or `[left, right]` pairs), `footer`, `buttons`.
- **`ticket`**: a bug-tracker issue. `title`, `heading`, `fields` (`[[key, value], ...]`), `highlight` (the key to highlight yellow), optional `image`.
- **`list`**: an order summary / till receipt. `title`, `heading`, `rows` (`[[item, amount], ...]`), `total` `[label, amount]`, `footer`, optional `image`.
- **`toasts`**: notifications stacking bottom-right. `wall` `{heading, small}` (big wallpaper text on the left), `toasts` (`[{title, text}]`), `reveal: {}` (any value) to bring each toast on its own click, optional `image`.
- **`title`**: a boot screen. `heading`, `sub`, `progress` `{pct, label}`, optional small `image`.
- **`link`**: a montage stop: a desktop shortcut plus an "Open web page?" box with the buttons "Open" and "Remind me in 5 years". `name`, `url`, `line`, `n` (e.g. "3 of 15", on a sticky), optional `image`.
- **`card`**: "Tip of the day": `title`, `heading`, `lines` (each line is its own click), `icon`, optional small `image`.
- **`fatal`**: a full-screen blue crash page for the big turn. `code` (header), `big`, `text`, `footer`.
- **`diagram`**: a window with a live 3D scene. `title`, `scene` (a name in `scenes/`), `caption` (above), `small` (below), `steps`. Scene-specific fields (e.g. `bricks`, `picks`) are read by the scene itself.

## Scenes (scenes/*.js)

`THEME.scenes[name] = (mount, slide, H) => ({ step(n), stop() })`, built on `THEME.three` in
`scenes/_common.js` (setup, box, label, damp, ease, palette). Flat, low-poly and chunky, in the
palette; labels are HTML tags (`.tag3d`, plus `ok`/`err`/`warn`). Respect `H.reduced` (jump
straight to the step's end state). Every scene must be followed by a meme slide.
