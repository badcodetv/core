/**
 * OAuth for the BadCode channel: store the refresh token, hand out short-lived access tokens.
 *
 * 🔴 Trap: while the Google Cloud app's consent screen is in "Testing", Google expires refresh
 * tokens after 7 days and the server silently stops working a week later (invalid_grant). Set the
 * app to "In production" (unverified is fine for our own one account; the consent page shows a
 * warning you click through). docs/youtube/README.md §Setup.
 */
import { chmodSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname } from 'node:path'
import type { ClientCreds } from './config'

const TOKEN_URL = 'https://oauth2.googleapis.com/token'

export interface StoredToken {
  refresh_token: string
  scope?: string
  obtained_at: string
}

export function readToken(file: string): StoredToken | null {
  if (!existsSync(file)) return null
  try {
    const t = JSON.parse(readFileSync(file, 'utf-8')) as StoredToken
    return t.refresh_token ? t : null
  } catch {
    return null
  }
}

export function writeToken(file: string, t: StoredToken): void {
  mkdirSync(dirname(file), { recursive: true, mode: 0o700 })
  writeFileSync(file, JSON.stringify(t, null, 2) + '\n', { mode: 0o600 })
  chmodSync(file, 0o600)
}

export class AuthError extends Error {
  constructor(
    public code: 'NO_CLIENT' | 'NOT_SIGNED_IN' | 'TOKEN_REVOKED' | 'TOKEN_REFRESH_FAILED',
    message: string,
  ) {
    super(message)
  }
}

/** Swaps the refresh token for an access token, caching it until a minute before it expires. */
export class TokenSource {
  private access: { token: string; expiresAt: number } | null = null

  constructor(
    private creds: ClientCreds | null,
    private file: string,
  ) {}

  async accessToken(): Promise<string> {
    if (this.access && Date.now() < this.access.expiresAt - 60_000) return this.access.token
    if (!this.creds) {
      throw new AuthError('NO_CLIENT', 'YOUTUBE_CLIENT_ID / YOUTUBE_CLIENT_SECRET are not set (.env at the repo root).')
    }
    const stored = readToken(this.file)
    if (!stored) throw new AuthError('NOT_SIGNED_IN', `No YouTube sign-in saved at ${this.file}.`)
    const res = await fetch(TOKEN_URL, {
      method: 'POST',
      headers: { 'content-type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        client_id: this.creds.clientId,
        client_secret: this.creds.clientSecret,
        refresh_token: stored.refresh_token,
        grant_type: 'refresh_token',
      }),
    })
    const body = (await res.json().catch(() => ({}))) as Record<string, unknown>
    if (!res.ok) {
      const err = String(body.error ?? res.status)
      if (err === 'invalid_grant') {
        throw new AuthError(
          'TOKEN_REVOKED',
          'Google rejected the saved sign-in (invalid_grant): it was revoked, or it expired because the app is still in "Testing".',
        )
      }
      throw new AuthError('TOKEN_REFRESH_FAILED', `Token refresh failed: ${err} ${String(body.error_description ?? '')}`)
    }
    this.access = {
      token: String(body.access_token),
      expiresAt: Date.now() + Number(body.expires_in ?? 3600) * 1000,
    }
    return this.access.token
  }
}

export async function exchangeCode(
  creds: ClientCreds,
  code: string,
  redirectUri: string,
  verifier: string,
): Promise<{ refresh_token?: string; scope?: string }> {
  const res = await fetch(TOKEN_URL, {
    method: 'POST',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: creds.clientId,
      client_secret: creds.clientSecret,
      code,
      code_verifier: verifier,
      redirect_uri: redirectUri,
      grant_type: 'authorization_code',
    }),
  })
  const body = (await res.json()) as Record<string, unknown>
  if (!res.ok) throw new Error(`Code exchange failed: ${String(body.error)} ${String(body.error_description ?? '')}`)
  return { refresh_token: body.refresh_token as string | undefined, scope: body.scope as string | undefined }
}
