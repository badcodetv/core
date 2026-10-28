# apps/site — badcode.tv

The live website for now: one static page that maps to our content and our socials. No build
step, no framework. The full React app in `apps/web` is separate and is not what badcode.tv serves.

- `public/` is the whole site. `index.html` holds the four stories and the social links.
- To add a link when a video or account goes live: in `index.html`, swap the
  `<span class="soon">…</span>` for `<a href="URL">…</a>` with the same words.
- Brand files in `public/` are copies from `docs/brand/logo/`. If the logo changes, copy them again.

## Preview

    npx serve apps/site/public

## Deploy (Cloudflare)

It is a Cloudflare Worker that only serves static files (`wrangler.jsonc`).

    cd apps/site
    npx wrangler login     # once, opens a browser
    npx wrangler deploy    # prints a *.workers.dev address

To serve it on badcode.tv, the domain's DNS must be on Cloudflare; then uncomment `routes` in
`wrangler.jsonc` and deploy again.

## Story stills

`public/stills/` holds one frame per story, 800×600 WebP (4:3), cut with ffmpeg from the films on
`D:\badcode-videos`. The instant-photo look (paper border, tilt, faded film colour) is CSS, so the
files stay plain frames. Git Push Origin Master: 0:09 of `renders/gpom-second-half-rough2.mp4`.
Camping: 3:08.5 of `camping.mp4` (Bob's tent, the wank tank, the Waitrose sign; Kai asked for this
over the camp-fire shot, which gave the plot away). Karen: 2:48.5 of `All Day to Complain - yes.mp4`
(real footage, not the cartoon shots). The Bank Robbery is a blank, undeveloped photo for now.
