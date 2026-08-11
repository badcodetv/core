import { BorshAccountsCoder, type Idl, type IdlAccounts } from '@coral-xyz/anchor'
import { deriveAddress } from '@badcode/chain-kit'
import type { Cluster } from '@badcode/chain-kit'
import {
  ClusterBadge,
  ConnectWallet,
  SolanaProvider,
  useAccount,
  useProgram,
  useSendTransaction,
  useWalletAddress,
} from '@badcode/chain-react'
import { PublicKey } from '@solana/web3.js'
import { useMemo } from 'react'
import idlJson from '@chain/idl/counter.json'
import type { Counter as CounterIdl } from '@chain/idl/counter'
import '@solana/wallet-adapter-react-ui/styles.css'
import './counter.css'

/**
 * The toolchain's shop window.
 *
 * There is no product here. This page exists so that a change to the Rust
 * program can be watched arriving in the browser: rebuild, redeploy, and both
 * the number and the *types* on this page follow, with nothing to edit in
 * between. If this page works, the toolchain works.
 *
 * Note what is NOT here: no hardcoded program address. It comes from the
 * generated IDL, so a redeploy to a different address needs no code change.
 */
const CLUSTER: Cluster = 'localnet'

// The JSON import widens every literal to `string`/`number[]`; the generated .ts
// carries the exact literal types Anchor wants. Same bytes, two views of them.
const IDL = idlJson as CounterIdl
const PROGRAM_ID = new PublicKey(IDL.address)

/**
 * The account as the *program* defines it, derived from the generated IDL.
 *
 * This is the load-bearing line. Add or remove a field in the Rust struct and
 * this type changes on the next `chain build`, so any code below that used the
 * old shape stops compiling. The types are not a description of the program;
 * they are the program's own definition, arriving here automatically.
 */
type CounterAccount = IdlAccounts<CounterIdl>['counter']

// Module scope: useAccount requires a stable decode function, and decodeAny
// matches on the account discriminator, so renaming the Rust struct cannot
// silently break the read path.
const coder = new BorshAccountsCoder(IDL as Idl)
const decodeCounter = (data: Buffer): CounterAccount => coder.decodeAny(data)

function Counter() {
  const address = useWalletAddress()
  const program = useProgram<CounterIdl>(IDL, PROGRAM_ID)
  const { send, pending, error } = useSendTransaction()

  const authority = useMemo(() => (address ? new PublicKey(address) : null), [address])
  const counterPda = useMemo(
    () => (authority ? deriveAddress(['counter', authority], PROGRAM_ID) : null),
    [authority],
  )

  const { data, loading, missing, error: readError } = useAccount(counterPda, decodeCounter)

  if (!address) {
    return (
      <p className="counter-hint">
        Connect a wallet set to <strong>localhost:8899</strong>. It needs SOL:{' '}
        <code>badcode chain airdrop &lt;your address&gt;</code>
      </p>
    )
  }

  const call = async (method: 'initialize' | 'increment' | 'reset') => {
    if (!program || !counterPda || !authority) return
    const accounts = method === 'initialize' ? { authority } : { counter: counterPda, authority }
    // Build the instruction with Anchor, send it with our own hook, so failures
    // arrive as sentences rather than as base58 soup.
    const ix = await program.methods[method]().accounts(accounts).instruction()
    await send([ix]).catch(() => {
      /* surfaced through `error` below */
    })
  }

  return (
    <>
      <p className="counter-value" aria-live="polite">
        {loading ? '…' : missing ? '—' : (data?.count.toString() ?? '—')}
      </p>

      <div className="counter-actions">
        {missing ? (
          <button onClick={() => call('initialize')} disabled={pending || !program}>
            Create counter
          </button>
        ) : (
          <>
            <button onClick={() => call('increment')} disabled={pending || !program}>
              Increment
            </button>
            <button className="counter-secondary" onClick={() => call('reset')} disabled={pending || !program}>
              Reset
            </button>
          </>
        )}
      </div>

      {error ? <p className="counter-error">{error}</p> : null}

      {readError ? (
        // Almost always a layout change: the account on chain was written by an
        // older version of the struct. Say so, because the raw borsh error does
        // not, and the fix is not one anyone guesses.
        <p className="counter-error">
          This account does not match the program&rsquo;s current layout — it was written before
          the last change. Run <code>badcode chain reset</code> and redeploy. ({readError.message})
        </p>
      ) : null}

      <dl className="counter-facts">
        <dt>Program</dt>
        <dd><code>{PROGRAM_ID.toBase58()}</code></dd>
        <dt>Counter PDA</dt>
        <dd><code>{counterPda?.toBase58()}</code></dd>
        <dt>Last change</dt>
        <dd>
          {/* Reads a field that did not exist two commits ago. If you delete
              `updated_at` from the Rust, this line stops compiling. */}
          {data ? new Date(data.updatedAt.toNumber() * 1000).toLocaleString() : '—'}
        </dd>
      </dl>
    </>
  )
}

export function CounterPage() {
  return (
    <SolanaProvider cluster={CLUSTER}>
      <main className="counter">
        <header className="counter-header">
          <ClusterBadge className="counter-cluster" />
          <h1>Counter</h1>
          <p className="counter-strap">
            A number, on a chain, on your machine. It proves the toolchain, and nothing else.
          </p>
        </header>

        <ConnectWallet />
        <Counter />

        <footer className="counter-footer">
          <p>
            Change <code>STEP</code> in <code>chain/programs/counter/src/lib.rs</code>, then{' '}
            <code>badcode chain build &amp;&amp; badcode chain deploy --cluster localnet</code>. The button
            starts adding a different number, and the types on this page change with it. Change an
            account field and run <code>badcode chain reset</code> first, or the old data will not
            decode.
          </p>
        </footer>
      </main>
    </SolanaProvider>
  )
}
