import { describe, it, expect } from 'vitest'
import { toWindows, toWsl, isUnderRoot, stripExtendedPrefix, PathError } from './paths'

describe('toWindows', () => {
  it('converts an /mnt/<drive> path to <DRIVE>:\\...', () => {
    expect(toWindows('/mnt/c/Users/kai/x.mp4')).toEqual({ path: 'C:\\Users\\kai\\x.mp4' })
  })

  it('is drive-generic, not C:-specific — the media root is on D:', () => {
    expect(toWindows('/mnt/d/badcode-videos/gitpush-origin-master/x.mp4')).toEqual({
      path: 'D:\\badcode-videos\\gitpush-origin-master\\x.mp4',
    })
  })

  it('uppercases a lowercase or mixed-case drive letter', () => {
    expect(toWindows('/mnt/c/x.mp4').path).toBe('C:\\x.mp4')
    expect(toWindows('/mnt/D/x.mp4').path).toBe('D:\\x.mp4')
  })

  it('passes an already-Windows path through unchanged', () => {
    expect(toWindows('C:\\Users\\kai\\x.mp4')).toEqual({ path: 'C:\\Users\\kai\\x.mp4' })
  })

  it('passes an already-UNC path through unchanged', () => {
    const p = '\\\\wsl.localhost\\Ubuntu-22.04\\home\\kai\\x.mp4'
    expect(toWindows(p)).toEqual({ path: p })
  })

  it('maps a non-/mnt absolute WSL path to a \\\\wsl.localhost\\ UNC path with a warning', () => {
    expect(toWindows('/home/kai/x.mp4', 'Ubuntu-22.04')).toEqual({
      path: '\\\\wsl.localhost\\Ubuntu-22.04\\home\\kai\\x.mp4',
      warning: 'outside media root',
    })
  })

  it('defaults the distro from WSL_DISTRO_NAME', () => {
    const prev = process.env.WSL_DISTRO_NAME
    process.env.WSL_DISTRO_NAME = 'Ubuntu-24.04'
    try {
      expect(toWindows('/home/kai/x.mp4').path).toBe('\\\\wsl.localhost\\Ubuntu-24.04\\home\\kai\\x.mp4')
    } finally {
      if (prev === undefined) delete process.env.WSL_DISTRO_NAME
      else process.env.WSL_DISTRO_NAME = prev
    }
  })

  it('preserves a trailing separator', () => {
    expect(toWindows('/mnt/d/badcode-videos/').path).toBe('D:\\badcode-videos\\')
  })

  it('preserves spaces in path segments', () => {
    expect(toWindows('/mnt/d/badcode-videos/foo bar/x.mp4').path).toBe('D:\\badcode-videos\\foo bar\\x.mp4')
  })

  it('throws PathError RELATIVE_PATH on a relative path', () => {
    expect(() => toWindows('relative/x.mp4')).toThrow(PathError)
    try {
      toWindows('relative/x.mp4')
      expect.unreachable()
    } catch (err) {
      expect(err).toBeInstanceOf(PathError)
      expect((err as PathError).code).toBe('RELATIVE_PATH')
    }
  })
})

describe('toWsl', () => {
  it('converts a drive-letter path to /mnt/<lower-drive>/...', () => {
    expect(toWsl('C:\\Users\\kai\\x.mp4')).toBe('/mnt/c/Users/kai/x.mp4')
  })

  it('is drive-generic', () => {
    expect(toWsl('D:\\badcode-videos\\gitpush-origin-master\\x.mp4')).toBe(
      '/mnt/d/badcode-videos/gitpush-origin-master/x.mp4'
    )
  })

  it('lowercases a mixed-case drive letter', () => {
    expect(toWsl('D:\\x.mp4')).toBe('/mnt/d/x.mp4')
  })

  it('strips a \\\\wsl.localhost\\<distro>\\ UNC path back to /home/...', () => {
    expect(toWsl('\\\\wsl.localhost\\Ubuntu-22.04\\home\\kai\\x')).toBe('/home/kai/x')
  })

  it('passes an already-WSL path through unchanged', () => {
    expect(toWsl('/mnt/c/Users/kai/x.mp4')).toBe('/mnt/c/Users/kai/x.mp4')
  })

  it('round-trips an /mnt/<drive> path through toWindows and back', () => {
    const original = '/mnt/d/badcode-videos/foo bar/x.mp4'
    expect(toWsl(toWindows(original).path)).toBe(original)
  })

  it('round-trips a UNC path through toWindows and back, regardless of distro', () => {
    const original = '/home/kai/foo bar/x.mp4'
    const { path: winPath } = toWindows(original, 'Ubuntu-24.04')
    expect(toWsl(winPath)).toBe(original)
  })

  it('round-trips a trailing separator', () => {
    const original = '/mnt/d/badcode-videos/'
    expect(toWsl(toWindows(original).path)).toBe(original)
  })
})

describe('isUnderRoot', () => {
  const root = 'D:\\badcode-videos'

  it('is true for a path directly under the root', () => {
    expect(isUnderRoot('D:\\badcode-videos\\gitpush-origin-master\\x.mp4', root)).toBe(true)
  })

  it('is true for the root itself', () => {
    expect(isUnderRoot('D:\\badcode-videos', root)).toBe(true)
  })

  it('is case-insensitive', () => {
    expect(isUnderRoot('d:\\BadCode-Videos\\x.mp4', root)).toBe(true)
  })

  it('is separator-normalised (forward slashes)', () => {
    expect(isUnderRoot('D:/badcode-videos/x.mp4', root)).toBe(true)
  })

  it('tolerates a trailing separator on the root', () => {
    expect(isUnderRoot('D:\\badcode-videos\\x.mp4', 'D:\\badcode-videos\\')).toBe(true)
  })

  it('is false for a sibling path that merely shares the root as a string prefix', () => {
    expect(isUnderRoot('D:\\badcode-videos-old\\x.mp4', root)).toBe(false)
  })

  it('is false for a path on a different drive', () => {
    expect(isUnderRoot('C:\\badcode-videos\\x.mp4', root)).toBe(false)
  })
})

// Found live 2026-08-21: `project.path` comes back from Premiere as an extended-length path
// (`\\?\D:\…`). Untreated, it matched none of the drive-letter patterns and passed straight
// through untranslated — so every path the session saw would have been a raw Windows string.
describe('extended-length (\\\\?\\) prefixes', () => {
  it('strips the prefix on the way to WSL', () => {
    expect(toWsl('\\\\?\\D:\\badcode-videos\\gpom\\gpom.prproj')).toBe('/mnt/d/badcode-videos/gpom/gpom.prproj')
  })

  it('strips the prefix on the way to Windows', () => {
    expect(toWindows('\\\\?\\D:\\badcode-videos').path).toBe('D:\\badcode-videos')
  })

  it('un-escapes the UNC variant', () => {
    expect(stripExtendedPrefix('\\\\?\\UNC\\server\\share\\clip.mp4')).toBe('\\\\server\\share\\clip.mp4')
  })

  it('leaves an ordinary path alone', () => {
    expect(stripExtendedPrefix('D:\\badcode-videos')).toBe('D:\\badcode-videos')
    expect(stripExtendedPrefix('/mnt/d/badcode-videos')).toBe('/mnt/d/badcode-videos')
  })

  it('still recognises the media root through the prefix', () => {
    expect(isUnderRoot('\\\\?\\D:\\badcode-videos\\gpom', 'D:\\badcode-videos')).toBe(true)
  })
})
