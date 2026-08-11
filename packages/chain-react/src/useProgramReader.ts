import { type Idl, Program } from '@coral-xyz/anchor'
import { useConnection } from '@solana/wallet-adapter-react'
import type { PublicKey } from '@solana/web3.js'
import { useMemo } from 'react'

/**
 * A read-only program handle. No wallet required, never null.
 *
 * Use this for everything you display; use `useProgram` only to build
 * instructions to sign. A page that shows chain state should be legible to a
 * visitor who never connects a wallet.
 *
 * It also exists to avoid a trap worth stating plainly. Anchor emits **two**
 * artifacts: `target/idl/x.json` uses the Rust field names (`updated_at`), while
 * `target/types/x.ts` is its camelCase view (`updatedAt`). `Program` converts the
 * IDL internally, so its coder returns camelCase and matches the generated
 * types. A `BorshAccountsCoder` built from the raw JSON does **not** convert, so
 * it returns snake_case while TypeScript insists the fields are camelCase — the
 * compiler is happy and every field reads `undefined` at runtime. Decode through
 * a Program, always.
 */
export function useProgramReader<T extends Idl>(idl: T, programId: PublicKey): Program<T> {
  const { connection } = useConnection()

  return useMemo(
    // Anchor only needs a connection to read; the provider's wallet is used for
    // signing, which this handle deliberately cannot do.
    () => new Program<T>({ ...idl, address: programId.toBase58() }, { connection }),
    [connection, idl, programId],
  )
}
