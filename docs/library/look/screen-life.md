---
slug: screen-life
name: Screen-life (story told on screens)
kind: look
family: Television and contemporary screen grammar
checked: 2026-10-28, references and engine notes (see Web check)
---

# Screen-life (story told on screens)

> The whole film plays inside a laptop or phone: chat windows, video calls, browser tabs, cursor movement.
>
> Library entry: read only by the `story-style` interview. A story that picks this copies what it
> needs into its own look.md / sound.md; it never links here as its style.

A found-interface form where the camera is a screen recording. Developed through Unfriended (2014) and refined in Searching (2018), it tells the story through typing, deleting, search queries, video calls and notifications. The cursor is the camera and the drafts the character's thoughts. It suits contemporary life where debt, work and benefits are managed through portals.

## Signature traits

- Fixed frame of an operating-system desktop, with windows opening, stacking and closing
- Cursor movement and hesitation as performance: hovering, typing then deleting
- Chat bubbles and email text appearing in real time with typing indicators
- Video call grid with webcam rectangles and lagging or frozen faces
- Notification pop-ups, tab titles and search suggestions as exposition
- Zooms and pans on the screen content to direct attention
- Digital sound: keyboard clicks, message pings, call tones
- Limited colour palette set by interface UI; harsh monitor glare on faces

## References

- *Unfriended* — Levan Gabriadze, 2014. Feature film that plays entirely on a teenager's laptop screen.
- *Searching* — Aneesh Chaganty, 2018. Proves screen-life can carry emotional drama and a mystery with real pathos.
- *Host* — Rob Savage, 2020. Lockdown horror made over Zoom; UK-made and very cheap.
- *Missing* — Nick Johnson and Will Merrick, 2023. Shows the format scaled up with layers of apps and records.
- *Noah* — Patrick Cederberg and Walter Woodman, 2013. Short film that popularised the screen-only form.

## What it carries

Anxious, intimate, claustrophobic, voyeuristic, immediate. Carries bureaucracy, surveillance and loneliness. Fights against scale, landscape and anything wanting physical presence.

## What it suits, and what it would undermine

Stories about portals and algorithms: a Universal Credit claimant trapped in a chatbot loop, a gig worker being rated, an automated redundancy email. Very resonant with a UK working-class viewer who deals with apps for benefits, work and bills. Undermines mythic, historical or outdoor stories and any film that needs a human face to hold the emotion. Names the decision-maker through the sender field and signature.

## Asking Flow (Nano Banana stills, Veo clips) for it

Treat it as UI design rather than cinematography. Nano Banana can render a plausible screenshot: 'flat screen recording of a laptop desktop, email client window open, cursor hovering over a button, legible short text, 16:9, no device frame'. Keep on-screen copy to a few short words. For motion, generate the screens as stills and animate them in Premiere or ffmpeg or HTML; use Veo only for the webcam faces and for pushes into the screen. Exclude: photographed monitors with moire, reflections, keyboard hands, lens distortion, real brand logos.

## How generators get it wrong

Interface text in generated video becomes unreadable gibberish and drifts between frames, which destroys the format that depends on reading; build the UI as real overlays or scripted HTML and capture it. Cursor motion in Veo is jittery and inconsistent. Real brands such as Gmail or banks look like infringement or hit policy; use invented interface skins. Fake screenshots can look uncannily clean; add compression, scaling artefacts and clutter in tabs.

## Production cost

The cheapest format in generation, because it is mostly design. Highest craft is in the writing of the chat and cursor beats plus screen-recording tooling. Webcam faces need consistent identity. Lip-sync is limited because the faces are small and often frozen by lag, which is a plus.

## Web check (2026-10-28)

Engine notes: plausible, not documented anywhere the checker found: treat as a first guess to test.

**Correction:** Garbled on-screen text from the original Nano Banana is widely reported; Nano Banana Pro and later are marketed for accurate text rendering, so short legible UI copy is plausible but not guaranteed. Flow has no Exclude field, so exclusions must be written as positives.

Sources:
- <https://www.analyticsvidhya.com/blog/2025/09/create-videos-using-veo-3-and-nano-banana/>
