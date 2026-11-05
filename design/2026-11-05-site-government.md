# The government on badcode.tv, deployed on every merge — Design & Implementation Plan

> **EXECUTION RULES (for agents):** Work ONE ticket at a time, in order unless dependencies say
> otherwise. Only the orchestrator changes ticket Status; workers may only append to Notes and the
> Discovered Issues Log. A ticket's checkbox is checked only after its Validation commands have been
> re-run by the orchestrator and pass. Do not expand scope; log surprises in the Discovered Issues Log.

Status: done (built 2026-11-05; ministers are 402–410: nine, the PM is the heading)
Relates: design/2026-11-05-badcode-government.md (this **replaces its T13**); ops
design/2026-11-04-badcode-tv-on-cloudflare.md; Future Proof talk on GOVT 2 (commit 1594e01).

## Context

The BadCode government (see `docs/government/README.md`) runs daily in Bob and changes this repo
only through one rolling PR. Its public output is `docs/government/manifesto/NN-<post>.md` (ten
files, `00-prime-minister` … `09-energy-climate`; front matter `title:` and `line:`, the line never
contains a colon; then a markdown body). The first manifesto was merged on 2026-11-05 (PR #5).

The website `apps/site` ("Channel BadCode", a TV with teletext) has three strands: STORIES, NEWS and
GOVT. GOVT 1 today shows a hand-written promise and three pledges from `src/content.json`
`government` (`apps/site/src/tv.js:117-121`, plain text `apps/site/build.mjs:38`); GOVT 2 is the
Future Proof talk, owned by the `future-proof` session (iframe, `tv.js:112-116`). Teletext 400 shows
the pledges (`tv.js` `400:` page). Deploying is manual today: `./stack site deploy` runs
`scripts/site/deploy.sh`, which builds `apps/site/build.mjs` into `apps/site/dist` and uploads with
`wrangler@4.40.0 pages deploy` to the Cloudflare Pages project `badcode-web`
(`www.badcode.tv`). The script already accepts `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`.

**Kai, 2026-11-05:** the site shows the government's manifesto, driven by commits, and **deploys
on every push to main** — reversing the 2026-11-04 "a push never deploys" rule.

## Architecture

```
 cabinet (Bob) ──► rolling PR ──► Kai/Jack merge ──► main
                                                     │ push
                     ┌───────────────────────────────┴────────────────────┐
                     ▼                                                    ▼
          bob-sync.yml (exists)                         site-deploy.yml (new)
          workers/briefs → Bob                           node apps/site/build.mjs
                                                         (reads docs/government/manifesto/*.md)
                                                         wrangler pages deploy → www.badcode.tv
```

**Decisions:**

1. **The manifesto files are the only source.** `build.mjs` reads `docs/government/manifesto/*.md`
   at build time into `C.government.manifesto = [{post, title, line, body}]`, which is embedded in
   the page like the rest of `content.json`. Nobody copies text into `content.json`.
2. **GOVT 1 = the cabinet.** The existing promise heading ("We promise to enact Future Proof") and
   the party-political-broadcast intro stay; the three hand-written pledges move off GOVT 1 (they
   remain in `content.json` and on teletext 400) and are replaced by the ten ministers, each as
   title + line. The `00-prime-minister` file's line is the promise, so the PM is shown as the
   heading, not repeated in the list. "Press 2 for Future Proof" stays.
3. **Full text lives on its own pages, not on the TV screen.** Each minister gets
   `/government/<post>/` (a real page with its own title, description = the line, plain-text body
   for search and screen readers) linked from GOVT 1. The TV's own UI stays a single screen.
4. **Teletext:** 400 keeps its pledges and gains one line "CABINET  401"; 401 is the cabinet index
   (ten dotted lines, 402–411); 402–411 show one minister each: title, line, at most 14 wrapped body
   lines, then `MORE: badcode.tv/government`. Every page fits the fixed 40×24 box.
5. **Deploy on every push to main** that touches `apps/site/**` or `docs/government/manifesto/**`
   (and `workflow_dispatch`). The Action runs the same build and the same pinned wrangler as
   `deploy.sh`; `concurrency: site-deploy` (newest wins, in-progress cancelled). A deploy that fails
   leaves the previous version live. The Future Proof talk ships as its committed
   `apps/site/public/future-proof/talk/index.html`; regenerating it stays a manual step of the
   `future-proof` work, so `docs/stories/future-proof/**` is **not** a trigger.
6. **Statements are not shown.** They are drafts until a person posts them.
7. **Rollback** stays as documented: revert the merge on GitHub (which redeploys), or Cloudflare
   dashboard → badcode-web → Deployments → Rollback.

Rejected: Cloudflare's own Git builds (a second build system to configure; the Action keeps build
and deploy in the repo next to `bob-sync.yml`); copying manifesto text into `content.json` by script
(two sources that drift).

## File Structure

| Path | Action | Purpose |
| --- | --- | --- |
| `apps/site/build.mjs` | Modify | read the manifesto files; `C.government.manifesto`; plain-text bodies for `/government`, `/government/<post>/`, `/text/401`–`411`; add those pages |
| `apps/site/manifesto.mjs` | Create | pure `readManifesto(dir) → [{post, title, line, body}]` and `parseFrontMatter(text)` (split on the first colon only) |
| `apps/site/manifesto.test.mjs` | Create | vitest unit tests (run by the root `npm test`? no: root runs `vitest run --dir scripts`; run with `npx vitest run apps/site`) |
| `apps/site/src/tv.js` | Modify | GOVT 1 cabinet list with links; teletext 400 line, 401 index, 402–411 pages; page order |
| `apps/site/src/tv.css` | Modify | styles for the cabinet list on GOVT 1 |
| `.github/workflows/site-deploy.yml` | Create | build + `wrangler pages deploy` on push to main |
| `scripts/site/deploy.sh` | Modify | header comment: push to main now deploys (Kai, 2026-11-05); manual deploy still works |
| `apps/site/README.md` | Modify | the manifesto comes from `docs/government/manifesto/`; merges deploy |
| `docs/government/README.md` | Modify | "a merged manifesto PR is live on badcode.tv within minutes" replaces the manual-deploy caveat |
| ops `design/2026-11-04-badcode-tv-on-cloudflare.md` | Modify (ops repo) | one dated status line: deploys now run from GitHub Actions on push |

## Interfaces

- `readManifesto(dir)`: reads `NN-<post>.md` sorted by name; `post` = file name without `NN-` and
  `.md`; throws on a file with no `title` or `line`. Body = everything after the front matter,
  trimmed. The site renders body as escaped text paragraphs (split on blank lines; `## ` headings
  become `<h2>`; no raw HTML ever passes through).
- Secrets on `badcodetv/core`: `CLOUDFLARE_API_TOKEN` (an API token with **Account → Cloudflare
  Pages → Edit** only) and `CLOUDFLARE_ACCOUNT_ID`. Kai creates the token in the Cloudflare
  dashboard (My Profile → API Tokens → Create Token → Custom) and sets both with `gh secret set`.
- Action command: `node apps/site/build.mjs && npx -y wrangler@4.40.0 pages deploy apps/site/dist
  --project-name badcode-web --branch main --commit-hash $GITHUB_SHA --commit-message "<subject>"`.

## Out of Scope

- Changing GOVT 2 or the Future Proof talk (the `future-proof` session owns it).
- Showing statements, news, or the cabinet's minutes on the site.
- Moving DNS to Cloudflare (ops §3, on hold).
- `scripts/site/releases.tsv` logging from CI (Cloudflare's deployment list is the record for CI deploys).

## Tickets

### S1: Read the manifesto at build time   [Status: pending | Model: sonnet]
- **Scope:** Create `apps/site/manifesto.mjs` + tests; in `build.mjs` set
  `C.government.manifesto = readManifesto(<repo>/docs/government/manifesto)` before the page is
  built; add plain-text pages `/government/<post>/` (title `<Title> · The BadCode Government`,
  description = line) and update `plainBody.gov` to list every minister's title, line and link.
- **Files:** `apps/site/manifesto.mjs`, `apps/site/manifesto.test.mjs`, `apps/site/build.mjs`.
- **Acceptance criteria:** tests cover a good file, a line with no colon, a missing title (throws),
  body with a `## ` heading, file order; the build writes `dist/government/chancellor/index.html`
  containing the Chancellor's line.
- **TDD:** yes
- **Validation:** `npx vitest run apps/site` → pass; `node apps/site/build.mjs && grep -c "mortgages at home" apps/site/dist/government/chancellor/index.html` ≥ 1.
- **Depends on:** —
- [ ] done
- Notes:

### S2: GOVT 1 shows the cabinet   [Status: pending | Model: sonnet]
- **Scope:** In `tv.js` GOVT 1 (`s.p !== 2` branch) keep the bar, the promise `<h1>`, the PPB intro
  and "Press 2 for Future Proof"; replace the pledges list with the nine ministers (skip
  `prime-minister`): title + line, each a link to `/government/<post>/`. Style in `tv.css` so ten
  rows fit the screen at phone width (16px gutter) without scrolling the page.
- **Files:** `apps/site/src/tv.js`, `apps/site/src/tv.css`.
- **Acceptance criteria:** GOVT 1 renders nine ministers; GOVT 2 unchanged; no layout overflow at
  360px width.
- **TDD:** no
- **Validation:** `node apps/site/build.mjs`; `./stack site preview` and check GOVT 1 at desktop and phone width by eye (screenshot).
- **Depends on:** S1
- [ ] done
- Notes:

### S3: Teletext 401–411   [Status: pending | Model: sonnet]
- **Scope:** Per Decision 4. Add 401–411 to the teletext page order and to `build.mjs`'s `/text/`
  page list; fast-text "Govt" still goes to 400.
- **Files:** `apps/site/src/tv.js`, `apps/site/build.mjs`.
- **Acceptance criteria:** every teletext page ≤24 rows and ≤40 columns; 402 shows the Chancellor.
- **TDD:** no
- **Validation:** `node apps/site/build.mjs && test -f apps/site/dist/text/411/index.html`; preview by eye.
- **Depends on:** S1
- [ ] done
- Notes:

### S4: Deploy on push   [Status: pending | Model: sonnet]
- **Scope:** `.github/workflows/site-deploy.yml` per Decision 5 and Interfaces (checkout, setup-node
  22, build, deploy; `concurrency: {group: site-deploy, cancel-in-progress: true}`). Update the
  `deploy.sh` header, `apps/site/README.md`, `docs/government/README.md`, and the ops design doc's
  status line (ops repo: edit only that line; it has other people's uncommitted work, so commit
  only that file).
- **Files:** as listed.
- **Acceptance criteria:** the workflow is valid; docs no longer say a push never deploys.
- **TDD:** no
- **Validation:** `gh workflow view site-deploy.yml --repo badcodetv/core` after push; `grep -n "never deploys" scripts/site/deploy.sh apps/site/README.md` → no hits.
- **Depends on:** —
- [ ] done
- Notes:

### S5: Secrets, merge, prove it   [Status: pending | Model: sonnet]
- **Scope:** Kai creates the Cloudflare token and sets `CLOUDFLARE_API_TOKEN` and
  `CLOUDFLARE_ACCOUNT_ID` on `badcodetv/core`. Merge S1–S4 as one PR. Confirm the Action deploys and
  `https://www.badcode.tv/government/` shows the ministers; then prove the chain end to end on the
  next merged government PR (the site changes with no manual step).
- **Files:** none.
- **Acceptance criteria:** Action green; `curl -s https://www.badcode.tv/government/chancellor/ | grep -c "mortgages"` ≥ 1; `/text/402/` returns 200.
- **TDD:** no
- **Validation:** `gh run list --repo badcodetv/core --workflow site-deploy.yml --limit 1` → success.
- **Depends on:** S1, S2, S3, S4
- [ ] done
- Notes:

## Discovered Issues Log

(appended by executors during implementation)
