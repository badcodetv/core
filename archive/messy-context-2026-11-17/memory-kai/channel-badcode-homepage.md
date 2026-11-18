---
name: channel-badcode-homepage
description: "2026-11-04 Kai picked \"Channel BadCode\" (whole site = an old TV + teletext) for the three-strand homepage; DNS stays at Gandi; deployment is the website-ops session"
metadata:
  node_type: memory
  type: project
  originSessionId: f3c0f245-2373-47a2-ac43-5516d5defbf6
  modified: 2026-11-04T20:02:39.699Z
---

2026-11-04: Kai wants the homepage to show BadCode as three strands: Stories (films + songs), the news bulletin (working name Money For Something) and the BadCode Government (a spoof party promising Future Proof). A 10-agent Sonnet research workflow produced 8 concepts (design/2026-11-04-homepage/concepts.md, picking page https://claude.ai/artifact/N167K9nMoHc2A8ywVmWa38). **Kai picked Channel BadCode**: the whole website is an old TV. He liked the CRT-style story titles and wants teletext played up.

Working TV prototype with an ideas vote list: https://claude.ai/artifact/EG5GDmGjYX7ZHLKHypALLG. Source is design/2026-11-04-homepage/channel-badcode.src.html; rebuild with build-channel.py, which inlines the stills. Votes are in the db collection `votes`, one doc per person.

**Built 2026-11-04 (Kai: "go with your options"):** apps/site is now the TV. Edit src/content.json, run `node apps/site/build.mjs`, and the output goes to apps/site/dist. The six rules: channel = section, number = programme (Stories 1–4 films, 5–8 songs); YouTube plays inside the TV; TEXT holds the words; every state has a real address (/stories/3, /text/888); the hijack plays on the first visit only; few extras. See apps/site/README.md.

**DNS stays at Gandi** (Kai, same day). This reverses ops' plan to move the nameservers. www.badcode.tv points to Cloudflare Pages by CNAME, and the bare domain redirects to www. **The `website-ops` session owns deployment.** It builds apps/site/dist and uploads that.

**2026-11-11 remote ruling (Kai):** the three buttons stay STORIES · NEWS · GOVT. NEWS is the catch-all for specials: Future Proof, the Storyverse, shorts, Money For Something. GOVT = the government in action (status page + Live / The floor / The record / Replay, from the round-2 studio prototype https://claude.ai/artifact/9z6azvKiekhoRJrX23SkH3). He considered "specials" and dropping NEWS, and rejected both.

**Why:** a TV holds all three strands as channels, and teletext gives the plain-text layer.
**How to apply:** design and content work here; deploys go through website-ops. Related: [[first-release-four-stories]], [[website-reset-initiative]], [[microsite-prototypes]].
