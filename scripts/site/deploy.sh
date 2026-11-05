#!/usr/bin/env bash
#
# scripts/site/deploy.sh — build the website and upload it to Cloudflare Pages.
# Run it through ./stack:
#
#   ./stack site preview     build + upload as the current branch → https://<branch>.badcode-web.pages.dev
#   ./stack site deploy      build + upload as production → https://www.badcode.tv (needs a clean tree)
#   ./stack site status      the last deployments Cloudflare holds
#   ./stack site login       sign wrangler in to Cloudflare (browser), if no token is in .env
#
# Deploying was manual until 2026-11-05. Kai, 2026-11-05: a push to main that touches apps/site/** or
# docs/government/manifesto/** now deploys through .github/workflows/site-deploy.yml (same build,
# same pinned wrangler). This script still works for previews and hand deploys.
# Rollback: Cloudflare dashboard → Workers & Pages → badcode-web → Deployments → "Rollback",
# or check out an older commit and `./stack site deploy` again.
#
# The plan behind this: ops repo, design/2026-11-04-badcode-tv-on-cloudflare.md.
# DNS stays at Gandi (§3a): www.badcode.tv is a CNAME to badcode-web.pages.dev; the bare
# badcode.tv is redirected to www by Caddy on the box.
#
# Settings (override from the environment or the git-ignored .env):
#   SITE_DIST        the folder that IS the site        (default apps/site/dist)
#   SITE_BUILD       command that builds it, from the repo root (default: node apps/site/build.mjs; empty = no build)
#   SITE_ORIGIN      the site's public address          (default https://www.badcode.tv; given to a build as VITE_SITE_ORIGIN)
#
# What ships (2026-11-04): apps/site, the "Channel BadCode" TV site, built by apps/site/build.mjs
# (plain Node, no dependencies) into apps/site/dist, which is git-ignored, so every upload builds first.
# The origin the site writes into its own links is apps/site/src/content.json `origin`, not SITE_ORIGIN.
#   PAGES_PROJECT    Cloudflare Pages project name      (default badcode-web)
#   CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID         (optional; else `./stack site login`)
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

# .env is git-ignored. Only the names below are read from it, never sourced whole.
if [[ -f .env ]]; then
  while IFS='=' read -r k v; do
    case "$k" in
      CLOUDFLARE_API_TOKEN|CLOUDFLARE_ACCOUNT_ID|SITE_BUILD|SITE_DIST|SITE_ORIGIN|PAGES_PROJECT)
        v="${v%\"}"; v="${v#\"}"; if [[ -z "${!k:-}" ]]; then export "$k=$v"; fi ;;
    esac
  done < <(grep -E '^[A-Z_]+=' .env)
fi

SITE_BUILD="${SITE_BUILD-node apps/site/build.mjs}"
SITE_DIST="${SITE_DIST:-apps/site/dist}"
SITE_ORIGIN="${SITE_ORIGIN:-https://www.badcode.tv}"
PAGES_PROJECT="${PAGES_PROJECT:-badcode-web}"
# Pinned: an unpinned npx fetches whatever is newest on the day.
WRANGLER=(npx -y wrangler@4.40.0)
LOG="$ROOT/scripts/site/releases.tsv"

die() { echo "site: $*" >&2; exit 1; }

need_auth() {
  [[ -n "${CLOUDFLARE_API_TOKEN:-}" ]] && return
  "${WRANGLER[@]}" whoami 2>&1 | grep -q "not authenticated" \
    && die "not signed in to Cloudflare. Run: ./stack site login  (or put CLOUDFLARE_API_TOKEN in .env)"
  return 0
}

ensure_project() {
  if ! "${WRANGLER[@]}" pages project list 2>/dev/null | grep -qw "$PAGES_PROJECT"; then
    echo "── creating Pages project $PAGES_PROJECT (production branch: main)"
    "${WRANGLER[@]}" pages project create "$PAGES_PROJECT" --production-branch main
  fi
}

build() {
  if [[ -n "$SITE_BUILD" ]]; then
    echo "── building: $SITE_BUILD"
    VITE_SITE_ORIGIN="$SITE_ORIGIN" bash -c "$SITE_BUILD"
  else
    echo "── no build step: uploading $SITE_DIST as it is"
  fi
  [[ -f "$SITE_DIST/index.html" ]] || die "$SITE_DIST/index.html is missing"
  # Pages refuses any single file over 25 MiB. Say which, rather than fail mid-upload.
  local big; big="$(find "$SITE_DIST" -type f -size +25M)"
  [[ -z "$big" ]] || die "files over Cloudflare's 25 MiB limit (host them elsewhere):"$'\n'"$big"
  echo "── built: $(du -sh "$SITE_DIST" | cut -f1), $(find "$SITE_DIST" -type f | wc -l) files"
}

upload() { # $1 = branch name Cloudflare files it under
  local branch="$1" sha subject dirty="" out url
  sha="$(git rev-parse --short HEAD)"
  subject="$(git log -1 --format=%s)"
  [[ -n "$(git status --porcelain)" ]] && dirty="+dirty"
  out="$("${WRANGLER[@]}" pages deploy "$SITE_DIST" \
          --project-name "$PAGES_PROJECT" --branch "$branch" \
          --commit-hash "$(git rev-parse HEAD)" --commit-message "$subject$dirty" \
          --commit-dirty="$([[ -n $dirty ]] && echo true || echo false)" 2>&1 | tee /dev/stderr)"
  url="$(grep -oE 'https://[a-z0-9.-]+\.pages\.dev' <<<"$out" | head -1)"  # the unique deployment URL, not the branch alias
  [[ -n "$url" ]] || die "upload did not print a deployment URL — see above"
  [[ -f "$LOG" ]] || printf 'when_utc\tkind\tbranch\tcommit\turl\n' >"$LOG"
  printf '%s\t%s\t%s\t%s%s\t%s\n' "$(date -u +%FT%TZ)" "$KIND" "$branch" "$sha" "$dirty" "$url" >>"$LOG"
  echo
  echo "✅ $KIND: $url"
  [[ "$KIND" == production ]] && echo "   live at $SITE_ORIGIN once the custom domain is attached"
  echo "   logged in scripts/site/releases.tsv (commit it so 'what is live' is in git)"
}

cmd="${1:-help}"; shift || true
case "$cmd" in
  login)   "${WRANGLER[@]}" login ;;
  status)  need_auth; "${WRANGLER[@]}" pages deployment list --project-name "$PAGES_PROJECT" ;;
  preview)
    need_auth; ensure_project; build
    branch="$(git branch --show-current)"; [[ -n "$branch" ]] || branch="detached-$(git rev-parse --short HEAD)"
    # `main` IS production on Pages, so a preview from main goes up under a separate name.
    [[ "$branch" == main ]] && branch="preview"
    KIND=preview upload "$branch" ;;
  deploy)
    [[ "${1:-}" == --force ]] || {
      [[ -z "$(git status --porcelain -- "$(dirname "$SITE_DIST")" packages)" ]] \
        || die "uncommitted changes in the site or its packages — commit first, or --force (the log marks it +dirty)"
    }
    need_auth; ensure_project; build
    KIND=production upload main ;;
  *) awk 'NR<3 {next} /^#/ {sub(/^# ?/, ""); print; next} {exit}' "$0" ;;
esac
