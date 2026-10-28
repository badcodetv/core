---
slug: teletext-ceefax
name: Teletext and Ceefax page graphics
kind: look
family: Archive and period media textures
checked: 2026-10-28, references and engine notes (see Web check)
---

# Teletext and Ceefax page graphics

> Blocky 40-by-24 mosaic pages in eight bright colours on black: news, weather and adverts as chunky text and crude pictures.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

Ceefax (BBC, from 1974), Oracle (ITV) and later Teletext services broadcast text pages through the TV signal. The display is a grid of 40 columns by 24 rows of characters in eight colours (black, red, green, yellow, blue, magenta, cyan, white), with a mosaic character set that allows crude blocky graphics, and large double-height headlines. It is a uniquely British piece of media memory, associated with holiday adverts, football scores, subtitles and the 1990s children's show Digitiser. It is the least obvious entry here: not a camera texture but a screen-graphic one, which means it can carry text, data and diagrams in a form that feels official and absurd at once.

## Signature traits

- Black background, 40x24 character grid, bold pixel font
- Eight pure flat colours only: red, green, yellow, blue, magenta, cyan, white on black
- Mosaic block graphics that build crude images from 2x3 sub-cells in each character cell
- Double-height headline lines and coloured header bars with page number (P100) and time in the corner
- Page numbers navigated by the viewer: three-digit codes and coloured Fastext links at the bottom
- Flicker and horizontal colour fringing on a CRT; slow page-by-page reveal with hidden answers
- Terse headline-style writing in capitals with no articles

## References

- *Ceefax* — BBC, 1974-2012. The original service; its page design and colour use define the look.
- *Digitiser* — Channel 4 (Paul Rose and others, on Teletext), 1993-2003. A comedy and video game magazine on teletext pages, the proof that the form can carry satire and jokes in the same voice.
- *Pages from Ceefax* — BBC Two, 1986-2003. The BBC Two filler broadcast of rotating teletext pages with music, showing the pages as a watchable image sequence. **(Unconfirmed on the web.)**
- *Teefax* — Dan Farrimond and collaborators (teletext art and revival service), 2010s-. A modern revival of teletext art, which shows the form working as contemporary graphic design. **(Unconfirmed on the web.)**

## What it carries

Deadpan, bureaucratic, nostalgic and funny. It carries absurd official statements, list-form facts and numbers, and gives a headline the blunt flatness of a bulletin. It fights against emotion, character and narrative scenes with people.

## What it suits, and what it would undermine

Excellent for the facts and numbers part of an argument: a ledger of who owns what, a countdown, a chart of wages against rents, a punchline in capitals. It is a perfect device for chapter cards and interludes inside a longer film, and a satirical 'bulletin from the future'. It cannot carry a story by itself because it has no people, and its charm can slide into pure nostalgia if the content is not sharp.

## Asking Flow (Nano Banana stills, Veo clips) for it

Image models can approximate the grid but not reliably the exact rules, so describe them explicitly: '1980s teletext television page, 40 columns by 24 rows, pure black background, flat saturated colours only (white, yellow, cyan, green, magenta, red, blue), blocky mosaic pixel graphics, double-height headline text, page number P101 top left, CRT scanlines'. Keep text short. Exclude: gradients, anti-aliasing, drop shadows, photography, modern fonts, smooth curves. The reliable method is to generate pages deterministically as text and images with code (a teletext renderer or a pixel-font script) and use the image model only for the CRT-screen photograph around them.

## How generators get it wrong

The model produces something that looks like teletext but with the wrong details: smooth gradients, anti-aliased fonts, too many colours, misaligned grid, and text that is garbled or misspelled. Longer copy always fails. Video models animate the text, causing letters to wobble and change between frames. For this reason, anything legible should be rendered by code, and Veo should only be asked for camera moves on the screen (a CRT push-in) with the text locked as an input still.

## Production cost

Low if rendered by code (every page is a simple grid, perfectly consistent), high if left to the generators. The only hard part is writing short, funny copy in the page idiom and keeping a consistent page numbering scheme across the film.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.
