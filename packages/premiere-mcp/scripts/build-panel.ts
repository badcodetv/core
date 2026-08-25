/**
 * Builds the UXP panel and puts it where Premiere can load it.
 *
 *   npm run build:panel        --workspace @badcode/premiere-mcp
 *   npm run build:panel:watch  --workspace @badcode/premiere-mcp
 *
 * Two outputs, and both matter:
 *   1. `panel/dist/`  — the bundle plus its statics (manifest, html, icons).
 *   2. `<mediaRoot>\_bridge\panel\` — a mirror of (1). UXP Developer Tool loads the plugin from
 *      a Windows path, so the built panel has to exist on the Windows side. Skipped with a
 *      notice when no media root is configured, because the build itself still works without one.
 *
 * The bundle is CommonJS with `premierepro` / `uxp` external: those are resolved by UXP's own
 * runtime `require` inside Premiere, and must never be bundled.
 *
 * 🔴 Rebuilding does NOT reload the panel. After this runs, press ⋯ → Load in UXP Developer
 * Tool, or Premiere keeps executing the previous bundle.
 */
import * as esbuild from 'esbuild'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { ConfigError, loadConfig, panelMirrorDir } from '../src/config'
import { toWsl } from '../src/paths'

const scriptDir = path.dirname(fileURLToPath(import.meta.url))
const packageDir = path.resolve(scriptDir, '..')
const repoRoot = path.resolve(packageDir, '..', '..')

const panelDir = path.join(packageDir, 'panel')
const srcDir = path.join(panelDir, 'src')
const distDir = path.join(panelDir, 'dist')

const STATICS = ['manifest.json', 'index.html']

const watch = process.argv.includes('--watch')

async function main(): Promise<void> {
  fs.mkdirSync(distDir, { recursive: true })

  const options: esbuild.BuildOptions = {
    entryPoints: [path.join(srcDir, 'main.ts')],
    outfile: path.join(distDir, 'main.js'),
    bundle: true,
    format: 'cjs',
    platform: 'neutral',
    target: 'es2020',
    external: ['premierepro', 'uxp', 'os', 'fs', 'path'],
    sourcemap: false,
    logLevel: 'info',
    plugins: [
      {
        name: 'badcode-statics',
        setup(build) {
          build.onEnd((result) => {
            if (result.errors.length > 0) return
            copyStatics()
            mirror()
          })
        },
      },
    ],
  }

  if (watch) {
    const ctx = await esbuild.context(options)
    await ctx.watch()
    console.log('[build-panel] watching panel/src …  (press ⋯ → Load in UDT after each rebuild)')
    return
  }

  await esbuild.build(options)
}

function copyStatics(): void {
  for (const name of STATICS) {
    fs.copyFileSync(path.join(panelDir, name), path.join(distDir, name))
  }
  fs.cpSync(path.join(panelDir, 'icons'), path.join(distDir, 'icons'), { recursive: true })
}

/** Mirror `panel/dist/` to `<mediaRoot>\_bridge\panel\` so UDT can load it from Windows. */
function mirror(): void {
  let target: string
  try {
    target = toWsl(panelMirrorDir(loadConfig(repoRoot)))
  } catch (err) {
    if (err instanceof ConfigError) {
      console.log(`[build-panel] no media root configured (${err.code}) — dist built, mirror skipped.`)
      console.log('[build-panel] ' + (err.hint ?? ''))
      return
    }
    throw err
  }

  try {
    fs.mkdirSync(target, { recursive: true })
    fs.cpSync(distDir, target, { recursive: true })
    console.log(`[build-panel] mirrored to ${target}`)
    console.log('[build-panel] 🔴 press ⋯ → Load in UXP Developer Tool — Premiere will not pick this up on its own.')
  } catch (err) {
    // A missing or unmounted drive is a setup problem, not a build failure — say so and leave
    // dist/ usable rather than failing the whole build.
    console.error(`[build-panel] could not mirror to ${target}: ${err instanceof Error ? err.message : String(err)}`)
    console.error('[build-panel] dist/ is still built; fix the media root and re-run.')
  }
}

main().catch((err: unknown) => {
  console.error(err)
  process.exit(1)
})
