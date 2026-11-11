#!/usr/bin/env -S npx tsx
/**
 * One-time sign-in: `npx tsx packages/youtube-mcp/src/login.ts`
 *
 * Opens Google's consent page in the Windows browser, catches the redirect on a localhost port
 * (WSL2 forwards Windows' localhost into WSL), and saves the refresh token outside the repo.
 *
 * 🔴 On the consent page, pick the BadCode CHANNEL (badcode.tv@gmail.com, or its brand account if
 * Google lists one), not a personal channel. Whatever you pick is what the server will manage;
 * `youtube_status` prints the channel name so you can check.
 */
import { createServer } from 'node:http'
import { createHash, randomBytes } from 'node:crypto'
import { spawn } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'
import { SCOPES, clientCreds, loadEnvFile, tokenFile } from './config'
import { exchangeCode, writeToken } from './auth'

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..', '..')
loadEnvFile(REPO_ROOT)

const creds = clientCreds()
if (!creds) {
  console.error('YOUTUBE_CLIENT_ID and YOUTUBE_CLIENT_SECRET must be in .env first. See docs/youtube/README.md §Setup.')
  process.exit(1)
}

const b64url = (b: Buffer) => b.toString('base64url')
const verifier = b64url(randomBytes(48))
const challenge = b64url(createHash('sha256').update(verifier).digest())
const state = b64url(randomBytes(16))

const server = createServer()
server.listen(0, () => {
  const addr = server.address()
  const port = typeof addr === 'object' && addr ? addr.port : 0
  const redirectUri = `http://localhost:${port}`
  const url =
    'https://accounts.google.com/o/oauth2/v2/auth?' +
    new URLSearchParams({
      client_id: creds.clientId,
      redirect_uri: redirectUri,
      response_type: 'code',
      scope: SCOPES.join(' '),
      access_type: 'offline',
      prompt: 'consent', // forces a refresh token even if this app was approved before
      code_challenge: challenge,
      code_challenge_method: 'S256',
      state,
    }).toString()

  console.log('\nOpen this in your browser (trying to open it for you):\n\n' + url + '\n')
  // WSL: hand the URL to Windows. Elsewhere, xdg-open / open. Failure is fine, the URL is printed.
  const opener = process.platform === 'darwin' ? 'open' : 'cmd.exe'
  const args = opener === 'cmd.exe' ? ['/c', 'start', '""', url.replace(/&/g, '^&')] : [url]
  try {
    spawn(opener, args, { stdio: 'ignore', detached: true }).on('error', () => {}).unref()
  } catch {
    /* printed above */
  }

  server.on('request', async (req, res) => {
    const u = new URL(req.url ?? '/', redirectUri)
    if (u.pathname !== '/') {
      res.writeHead(404).end()
      return
    }
    const done = (status: number, msg: string) => {
      res.writeHead(status, { 'content-type': 'text/plain; charset=utf-8' }).end(msg)
    }
    if (u.searchParams.get('state') !== state) return done(400, 'State mismatch, ignored.')
    const err = u.searchParams.get('error')
    if (err) {
      done(400, `Google said: ${err}`)
      console.error(`Sign-in refused: ${err}`)
      process.exit(1)
    }
    try {
      const tok = await exchangeCode(creds, u.searchParams.get('code') ?? '', redirectUri, verifier)
      if (!tok.refresh_token) throw new Error('Google returned no refresh token.')
      const file = tokenFile()
      writeToken(file, { refresh_token: tok.refresh_token, scope: tok.scope, obtained_at: new Date().toISOString() })
      done(200, 'Signed in. You can close this tab and go back to Claude.')
      console.log(`Saved the YouTube sign-in to ${file}. Run youtube_status in Claude to check the channel.`)
      setTimeout(() => process.exit(0), 200)
    } catch (e) {
      done(500, 'Sign-in failed; see the terminal.')
      console.error(e instanceof Error ? e.message : e)
      process.exit(1)
    }
  })
})
