/**
 * Put `Buffer` on the global, because Anchor reaches for it and browsers do not
 * have one.
 *
 * **This is not the same problem `chain-kit` already solved.** That package
 * imports `buffer` explicitly so that *its* PDA derivation works without a
 * polyfill, which is right and stays right. But Anchor's own
 * `BorshInstructionCoder.encode` calls `Buffer.alloc` against the **global**,
 * inside a dependency nobody here can edit — so the read half of a page works
 * perfectly and the first button that builds an instruction throws
 * `Buffer is not defined`, with a stack that names none of this.
 *
 * Found at T20 by clicking Claim in a real browser; every unit test and the
 * whole typecheck passed with the bug in place, because nothing but a browser
 * has this gap.
 *
 * It lives in the app rather than in `chain-kit` or `chain-react` on purpose:
 * assigning to `globalThis` is a side effect, and a library that quietly
 * mutates the global scope on import is a worse neighbour than an app that
 * says out loud what it is installing. Imported first thing in `main.tsx`,
 * before anything that might touch Anchor.
 */
import { Buffer } from 'buffer'

const scope = globalThis as unknown as { Buffer?: typeof Buffer }
scope.Buffer ??= Buffer
