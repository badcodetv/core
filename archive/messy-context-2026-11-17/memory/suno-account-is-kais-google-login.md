---
name: suno-account-is-kais-google-login
description: BadCode's Suno account is kaiyadavenport@gmail.com via Continue with Google; Suno is single-session so only one account fits the Chrome profile.
metadata:
  type: project
---

The Suno account that owns the BadCode workspaces is **kaiyadavenport@gmail.com**, signed in
with **Continue with Google** (not email/password).

Suno's Clerk config has `singleSessionMode: true` — there is **no account switcher**, so the
`.flow-profile` Chrome can hold exactly one Suno login at a time. On 2026-09-05 it was found
signed in as `jacktttt330@gmail.com` instead, which cost several rounds to spot: the create
page loads normally with someone else's `?wid=` and silently falls back to their own default
workspace.

**How to check in one call, from the page context:**
an authenticated `fetch('https://studio-api.prod.suno.com/api/project/<wid>')` with
`Authorization: Bearer <await window.Clerk.session.getToken()>` returns **403** when the
signed-in account does not own that workspace, and the account itself reads from
`window.Clerk.user.primaryEmailAddress.emailAddress`.

**Switching accounts is a human step.** The auto-mode classifier blocks both `Clerk.signOut()`
and clicking the profile menu, so hand over the two clicks: profile name bottom-left → Sign out
→ Continue with Google → pick the address. Related: [[flow-hand-driven-not-automated]].
