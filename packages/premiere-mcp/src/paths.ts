/**
 * Windows <-> WSL path translation. Pure string logic — no `wslpath` shell-out, no fs — because
 * the panel only ever sees Windows paths and the server only ever sees WSL ones; every boundary
 * crossing goes through here (Decision 5 in the plan).
 */

export class PathError extends Error {
  constructor(public code: 'RELATIVE_PATH', message: string) {
    super(message)
    this.name = 'PathError'
  }
}

const UNC_WSL_PREFIX = '\\\\wsl.localhost\\'

/**
 * Premiere hands back **extended-length** paths: `project.path` comes out as
 * `\\?\D:\badcode-videos\x.prproj`, not `D:\badcode-videos\x.prproj` (found live 2026-08-21).
 * Left alone, that prefix defeats every drive-letter match here and the path silently passes
 * through untranslated. Strip it before anything else looks at the string.
 *
 * The UNC variant `\\?\UNC\server\share` un-escapes to `\\server\share`.
 */
export function stripExtendedPrefix(p: string): string {
  if (p.startsWith('\\\\?\\UNC\\')) return `\\\\${p.slice('\\\\?\\UNC\\'.length)}`
  if (p.startsWith('\\\\?\\')) return p.slice('\\\\?\\'.length)
  return p
}

/**
 * `/mnt/<drive>/...` -> `<DRIVE>:\...` (drive-generic — the media root lives on D:, not C:).
 * An already-Windows path (drive letter or `\\wsl.localhost\...` UNC) passes through unchanged.
 * Anything else absolute (e.g. `/home/kai/...`, not under a mount) becomes a `\\wsl.localhost\`
 * UNC path with a warning: it works, but media belongs under the configured root, not there.
 */
export function toWindows(
  p: string,
  distro = process.env.WSL_DISTRO_NAME ?? 'Ubuntu-22.04'
): { path: string; warning?: string } {
  p = stripExtendedPrefix(p)
  if (/^[a-zA-Z]:[\\/]/.test(p) || p.startsWith('\\\\')) return { path: p }

  const mnt = p.match(/^\/mnt\/([a-zA-Z])(\/.*)?$/)
  if (mnt) {
    const [, drive, rest = ''] = mnt
    return { path: `${drive.toUpperCase()}:${rest.replace(/\//g, '\\')}` }
  }

  if (p.startsWith('/')) {
    return {
      path: `${UNC_WSL_PREFIX}${distro}${p.replace(/\//g, '\\')}`,
      warning: 'outside media root',
    }
  }

  throw new PathError('RELATIVE_PATH', `Path must be absolute: ${p}`)
}

/**
 * Reverses `toWindows` in both its forms. `/mnt/...` (already WSL form) passes through
 * unchanged. Does not need a `distro` argument: a UNC `\\wsl.localhost\<distro>\...` path
 * carries its own distro segment, which is simply dropped.
 */
export function toWsl(p: string): string {
  p = stripExtendedPrefix(p)
  if (p.startsWith(UNC_WSL_PREFIX)) {
    const rest = p.slice(UNC_WSL_PREFIX.length)
    const sep = rest.indexOf('\\')
    const tail = sep === -1 ? '' : rest.slice(sep + 1)
    return `/${tail.replace(/\\/g, '/')}`
  }

  const drive = p.match(/^([a-zA-Z]):[\\/](.*)$/)
  if (drive) {
    const [, letter, rest] = drive
    return `/mnt/${letter.toLowerCase()}/${rest.replace(/\\/g, '/')}`
  }

  return p
}

/** Case-insensitive, separator-normalised: is `windowsPath` at or under `mediaRoot`? */
export function isUnderRoot(windowsPath: string, mediaRoot: string): boolean {
  const normalise = (s: string) => stripExtendedPrefix(s).replace(/\//g, '\\').replace(/\\+$/, '').toLowerCase()
  const path = normalise(windowsPath)
  const root = normalise(mediaRoot)
  return path === root || path.startsWith(`${root}\\`)
}
