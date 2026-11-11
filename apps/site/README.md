# apps/site — badcode.tv (Channel BadCode)

The website is a television. Its three strands are channels, and number keys pick a programme within one:

| Remote | Channel | Programmes | Address |
| --- | --- | --- | --- |
| STORIES | BadCode One | 1–4 the films, 5–8 their songs | `/stories`, `/stories/1` … `/stories/8` |
| NEWS | the catch-all for specials (Kai, 2026-11-11) | 1 Future Proof (three questions play in the screen), 2 The Storyverse (Maddie's hologram); Money For Something joins as 3 with its first bulletin; shorts go here too | `/news` (also `/future-proof`), `/news/2` (also `/storyverse`, and `/stories/9`, its old home) |
| GOVT | The BadCode Government | 1 the manifesto, with where it stands (each minister at `/government/<post>`, each policy at `/government/<post>/<slug>`), then the government in action as a broadcast: 2 Live, 3 The floor (every policy), 4 The record, 5 Replay (any argument, point by point) | `/government`, `/government/2` … `/government/5` |
| 0 | Test card | about BadCode | `/about` |
| (no button since 2026-11-11) | Teletext pages, still open from old links | 100 index, 200 stories (201–204), 300 news, 400 manifesto, 401 the cabinet (402–410 one minister each), 700 follow, 800 about, 888 Future Proof | `/text/100` … |

Every address is a real page with its own title and link-preview picture, plus a plain-text copy of
what is on screen for screen readers, search engines and browsers without JavaScript.

## Change what's on it

**The government's manifesto is not in `content.json`.** `build.mjs` reads it from
`docs/government/manifesto/*.md` (`manifesto.mjs`), which the BadCode government writes through its
rolling PR (`docs/government/README.md`). Merge that PR and the site redeploys with it.

**`src/content.json` holds every word, picture and link.** To make a film play, put its YouTube id
(the 11 characters after `watch?v=`) in that story's `film` (or `songVideo`). A news bulletin
is an entry in `news.bulletins`: `{"title": "...", "youtube": "..."}`. A social account goes
live when its `url` is filled in. Blurbs and stills are setup only: no twist and no ending (Kai, 2026-10-22).

The story stills are in `public/stills/`, one frame per film (800×600 WebP), cut with ffmpeg from the
films on `D:\badcode-videos`. Git Push Origin Master is from 0:09 of `renders/gpom-second-half-rough2.mp4`.
Camping is from 3:08.5 of `camping.mp4`: Kai picked it over the camp-fire shot, which gives the plot away.
Karen is from 2:48.5 of `All Day to Complain - yes.mp4`. The Bank Robbery has no still yet: its film
isn't on this machine, so its channel shows "PICTURE COMING". To add one, put the file in `stills/`
and give it a `still` in `content.json`.

## Files

- `src/content.json`: the content (above)
- `src/page.html`: the one page template every address is built from
- `src/tv.css`, `src/tv.js`: the TV. Plain CSS and JS, no framework
- `public/`: static files copied as-is (stills, logo, favicons). The old one-page map
  (`public/index.html`, `404.html`, `styles.css`) is no longer shipped and can be deleted.
- `build.mjs`: builds everything into `dist/` (git-ignored)

## Future Proof (NEWS 1)

NEWS programme 1 is Future Proof: a home page and three giant questions (red or blue / once every five
years / ask the experts), each with a how-it-is / how-it-could-be three.js scene. It plays inside the
screen in an iframe of `/future-proof/questions/`, a static file in
`public/future-proof/questions/index.html`, built from the prototype Kai noted on
(`design/2026-11-11-future-proof-simple/index.html`, artifact https://claude.ai/artifact/LWVX8GbT8ZyNH9qvzmaewz).
After any change to the prototype, rebuild it, then build the site:

    python3 scripts/future-proof/build-questions.py
    node apps/site/build.mjs

Opened on its own (the "Full screen" link), it shows a "Back to the TV" link.

The older launch talk (the "Update Available" slideshow) is still served at `/future-proof/talk/` but
is no longer on the TV. To regenerate it:

    python3 scripts/slideshow/build.py docs/stories/future-proof/slideshows/launch-talk \
        --public apps/site/public/future-proof/talk/index.html --home /future-proof/

The words of
Future Proof for teletext page 888 and the plain-text page still come from `content.json`.

## The Storyverse (NEWS 2)

NEWS programme 2 plays Maddie's hologram inside the screen, in an iframe of `/storyverse/hologram/`.
That page, `public/storyverse/hologram/index.html`, is **generated**: `storyverse.mjs` derives it from the
hologram's editor page, `design/2026-11-05-gpom-meeting/lookdev/index.html` (look locked), keeping the scene
code and the default timing and dropping the editor (timeline, sliders, subtitles, saving). `build.mjs`
regenerates it on every build, so never edit it by hand. If the editor page changes shape so the derivation
no longer understands it, the build warns and keeps the last copy. It needs a tap to start (for the sound), plays
once from the CRT switch-on to the switch-off, then offers to watch again. three.js comes from jsdelivr.

The voice is `public/storyverse/hologram/voice/cNN.mp3` (96 kbps mono), encoded from the WAV masters on D:.
After a line is re-voiced, re-encode:

    node apps/site/storyverse.mjs --voice /mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1k/clips

Its link-preview still is `public/stills/storyverse.webp` (a frame of the choices, 27 s in). Its words are
`storyverse` in `content.json`: setup only (Kai knowingly let the hologram itself reveal parts of GPOM).

## Build and preview

    node apps/site/build.mjs                       # → apps/site/dist (needs Node 18+, nothing to install)
    python3 -m http.server 8080 -d apps/site/dist  # open http://localhost:8080

## Deploy (Cloudflare Pages)

The build output, `dist/`, is uploaded to the Cloudflare Pages project `badcode-web`. Run these from
the repo root. The script is `scripts/site/deploy.sh`, and every upload is logged in
`scripts/site/releases.tsv`.

    ./stack site login     # once, opens a browser
    ./stack site preview   # a preview at <branch>.badcode-web.pages.dev
    ./stack site deploy    # production, www.badcode.tv (a push to main that touches apps/site or docs/government/manifesto deploys by itself: .github/workflows/site-deploy.yml)
    ./stack site status

**DNS stays at Gandi** (Kai, 2026-11-04). `www.badcode.tv` is a CNAME at Gandi pointing to the Pages
project. The bare `badcode.tv` redirects to `www`, because Pages only serves a bare domain when Cloudflare
runs the DNS. That is also why this is Pages and not a Worker: a Worker's custom domain needs the
zone on Cloudflare too. `wrangler.jsonc` is left over from the Worker setup and the Pages deploy doesn't use it.

## Where the design came from

`design/2026-11-04-homepage/`: the 10-agent research (`concepts.md`), the eight-concept picking
page, the Channel BadCode prototype with its list of ideas, and the six rules Kai approved on
2026-11-04: channel = section, number = programme; the video plays inside the TV; TEXT holds the
words; every state has a real address; it is always on (the hijack plays on the first visit only,
and closedown between 1 and 6am never blocks a button); and the extras stay few.

## The government in action (GOVT 2–5)

Four views of one broadcast, from the same data: the policy files (`docs/government/policies/`) and the
debate logs (`docs/government/debates/`). `debates.mjs` turns each log into short captions in plain words
(field names never reach the screen; `debates.test.mjs` checks it). Live plays every point of every
argued policy, attack then answer; The floor shows all policies as small monitors grouped by minister;
The record lists what happened and what's coming up; Replay steps through any argument and shows what
changed. Roles keep one colour everywhere: minister green, opposition red, statistician blue, human
amber. Design and prototypes: `design/2026-11-11-future-proof-government/visual/`. A new debate log
reaches the site on the next deploy (the deploy watches `docs/government/debates/`).

## The remote (2026-11-11)

Kai: the top row is gone. No power, TEXT or CLEAN buttons; a small ✕ on the remote's corner hides it
and a REMOTE tab brings it back (on an upright phone the remote docks under the picture and has no ✕).
Teletext pages still open from old `/text/…` links. Reduced-motion visitors still get the clean
picture automatically.
Subtitles under the three buttons (Kai asked for funny): STORIES *spoiler alert*, NEWS
*from next week*, GOVT *arguing in public* A number with no programme on the current
channel is greyed out.
