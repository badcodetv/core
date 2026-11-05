# 19 - Meme legal: UK copyright for a political meme deck

Not legal advice. 4 web searches used. Grades: P = primary, S = secondary, H = hearsay, K = from model knowledge, not re-verified this session (check before relying).

## What the law says
- **s30A CDPA 1988** (in force 1 Oct 2014): "fair dealing with a work for the purposes of caricature, parody or pastiche does not infringe copyright in the work." Terms undefined; IPO said dictionary meanings suffice. [P-ish: quoted in https://www.pinsentmasons.com/out-law/news/uk-reforms-enabling-private-copying-parodying-and-general-quotation-of-copyrighted-material-come-into-force (S); IPO guidance https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/448273/Exceptions_to_copyright_-_Guidance_for_consumers.pdf (P, 2014, non-binding)]
- IPO's gloss: parody imitates a work for humorous/satirical effect while being noticeably different; the exception covers "limited amounts" of another's material. [P, same IPO PDF]
- The exception is only as good as **fair dealing**: how much taken, whether it substitutes for the original, commercial effect. The UK has no US-style "transformative" safe harbour; fair dealing is narrower. [S: https://sprintlaw.co.nz/articles/fair-use-youtube/]
- The key UK case is **Shazam Productions v Only Fools The Dining Experience [2022] EWHC 1379 (IPEC)**: parody and pastiche defence rejected. Humour came from the original itself, not from mocking it; copying was for commercial gain; defendants never framed it as pastiche. Lesson: the new work must add its own comment, not just reuse the original's jokes. [S: https://www.ashfords.co.uk/news-and-media/news/only-fools-horses-copyright-case-win-sets-new-precedent ; https://shepwedd.com/knowledge/copyright-fictional-characters-del-boy-high-court]
- K, unverified here: Shazam is an IPEC (first-instance) decision, so thin authority; the CJEU **Deckmyn** (C-201/13) test (evoke an existing work + be noticeably different + humour/mockery) is persuasive but post-Brexit status is uncertain. Also K: the 2014 exception cannot be overridden by contract (s30A is protected by s29-style rules), and **moral rights** (derogatory treatment, s80) can still bite on caricature of a work.
- Criticism/review (s30) and quotation (s30(1ZA)) are separate fair dealings: need sufficient acknowledgement and the quote must be genuinely for criticism of that work or another. Useful when the slide critiques the source itself. [K; summarised in IPO guidance above]

## Memes in practice
- Most memes are unmodified or lightly captioned copies of a photo/film still. Commentators say unaltered reproduction is likely infringement; a meme that adds real commentary stands better. [S: https://www.abajournal.com/magazine/article/do_memes_violate_copyright_law (US-flavoured)]
- **Getty / stock photos:** the Socially Awkward Penguin episode (2015) - Getty demanded fees from sites, one paid about $868; backlash followed. Getty says its embed tool avoids claims. [S: https://archive.techdirt.com/articles/20150908/00155432189/getty-images-goes-copyright-trolling-after-meme-penguin.shtml ; https://openmedia.org/blog/daily-dot-getty-claims-copyright-socially-awkward-penguin-forces-site-pay-868] Getty also runs automated image-matching and settlement letters (K).
- **Film stills:** studios do enforce. Constantin Film's 2010 Downfall claims pulled many Hitler-bunker parodies off YouTube. [S: https://www.nbcnews.com/id/wbna36693704]
- **Content ID:** cannot judge context, so parody gets claimed; risk is demonetisation or claim, then slow disputes, not a lawsuit. YouTube lets disputed videos keep earning during dispute (policy as of 2010s; check current). [S: https://blog.youtube/news-and-events/content-id-and-fair-use/ ; https://www.tubefilter.com/?p=80353] Content ID matches moving video and audio far more than static stills; a deck video with a few seconds of film clip is the real danger, a still image less so (K).
- Being a political/non-profit outlet helps the fairness argument; BadCode releases coins and may monetise, so assume "commercial" (K).

## Practical rule set for BadCode
**Green (use freely)**
1. **Self-made originals in meme grammar** (AI-generated or drawn: the "distracted" layout, two-panel "drake" structure, "this is fine"-style room, expanding brain). Format/layout is not copyrightable; the specific image is. Never prompt for a named character or a real person's likeness.
2. **Public-domain art** as the picture: pre-1900-ish painters (life+70 expired), Rijksmuseum / Met / Wikimedia Commons PD scans (check each file's own licence; a faithful scan of a 2D PD work carries no new UK copyright per Commons practice, K). Great fit for "invented before electricity" jokes (Victorian engravings, oil portraits of MPs of 1800s).
3. **Crown/archive films we already cleared** under the find-footage skill (pre-1957 Crown films, picture only, per memory). Stay within footage-sources.md tiers.
4. **Text-only memes, diagrams, charts, 3D scenes** (three.js): no third-party work involved.

**Amber (use with a reason, short, edited, attributed)**
5. **Classic meme templates whose source is a famous photo** (e.g. stock photo, film still): treat as a risk, not a right. Prefer re-creating the pose with our own generated image. If a real template is used, use it large-edit-heavy, once, with the comment aimed AT the thing the image depicts or evokes (satire of that work), not just borrowing its fame.
6. **Short film/TV clip in the talk-to-camera video**: max a few seconds, must be commenting on that clip, name the source on screen, expect Content ID. Never in the thumbnail. Keep a dispute template ready: "s30A parody/pastiche, s30 criticism, UK fair dealing".
7. **Political figures' photos** (news photos): the copyright sits with the agency, not the politician; avoid. Prefer our own caricature drawing (caricature is within s30A but beware likeness plus defamation, and the-reader.md rule: name the decision-maker, not a person to hate).

**Red (do not)**
8. Getty/agency stock photos with watermark, or "grabbed from Google Images".
9. Music from any film/TV/pop track under the slides (Content ID certain). Use our own Suno-made or cleared bed.
10. Anything that looks like a real organisation's branding, or a fake quote from a real person (rules also bar impersonation).
11. Relying on "it's a meme" or "we credited them" as a defence: neither is one in UK law.

## Process
- Add a column in the deck's slide table: `image source: original | PD(url) | cleared(url) | template(risk)`. Log it in the scene's provenance recipe card (docs/provenance/README.md).
- Keep a **swap-out** original for every amber template, so a takedown costs ten minutes.
- Audit before publishing: reverse-image search every non-original image once; check licence of PD scans.
- If a claim lands: remove or swap first, argue later. Do not fight a studio over a joke slide.
- For anything amber that matters to the pitch, ask an IP solicitor once; budget a short paid opinion (K: s30A case law is thin).

## Open questions
- UK status of AI-generated outputs: s9(3) CDPA gives computer-generated works a 50-year author-owner (person making arrangements); the government consulted on changing this (2024-25). Check current position before claiming ownership of our originals. [K, unverified]
- Did anyone test s30A on memes in the courts since 2022? Not found in these searches.
