import * as anchor from '@coral-xyz/anchor'
import { Keypair, LAMPORTS_PER_SOL, PublicKey, SystemProgram, Transaction } from '@solana/web3.js'
import { expect } from 'chai'
import { createHash } from 'node:crypto'
import { readFileSync } from 'node:fs'
// The generated types, from the same chain/idl a page would read.
import type { Deliberation } from '../idl/deliberation'

/**
 * The deliberation program: an append-only record of policies, arguments,
 * predictions, resolutions and labels.
 *
 * Every test uses fresh keys, so the shared ledger (which accumulates across
 * runs, see chain/README.md) never makes a case pass once and fail forever.
 */
describe('deliberation', () => {
  anchor.setProvider(anchor.AnchorProvider.env())
  const provider = anchor.getProvider() as anchor.AnchorProvider
  const program = anchor.workspace.Deliberation as anchor.Program<Deliberation>
  const connection = provider.connection

  // ── helpers ────────────────────────────────────────────────────────────────
  /** One real account of each kind, as the tests make them, for the cost report. */
  const made: Record<string, PublicKey> = {}
  const sha = (text: string): number[] => Array.from(createHash('sha256').update(text).digest())
  const le = (n: anchor.BN | number) => new anchor.BN(n).toArrayLike(Buffer, 'le', 8)
  const pda = (seeds: Buffer[]) => PublicKey.findProgramAddressSync(seeds, program.programId)[0]
  const authorPda = (key: PublicKey) => pda([Buffer.from('author'), key.toBuffer()])
  const recordPda = (kind: string, key: PublicKey, seq: anchor.BN | number) =>
    pda([Buffer.from(kind), key.toBuffer(), le(seq)])

  async function funded(sol = 2): Promise<Keypair> {
    const kp = Keypair.generate()
    const tx = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: provider.wallet.publicKey,
        toPubkey: kp.publicKey,
        lamports: sol * LAMPORTS_PER_SOL,
      }),
    )
    await provider.sendAndConfirm(tx)
    return kp
  }

  async function registered(): Promise<Keypair> {
    const kp = await funded()
    await program.methods.register().accountsPartial({ authorRecord: authorPda(kp.publicKey), author: kp.publicKey }).signers([kp]).rpc()
    made.author = authorPda(kp.publicKey)
    return kp
  }

  const nextSeq = async (kp: Keypair) => (await program.account.author.fetch(authorPda(kp.publicKey))).nextSeq

  async function postPolicy(kp: Keypair, text: string, parent: PublicKey | null = null): Promise<PublicKey> {
    const policy = recordPda('policy', kp.publicKey, await nextSeq(kp))
    await program.methods
      .postPolicy(sha(text), `ar://${text.replace(/\W/g, '')}`)
      .accountsPartial({ authorRecord: authorPda(kp.publicKey), policy, parent, author: kp.publicKey })
      .signers([kp])
      .rpc()
    made.policy = policy
    return policy
  }

  async function postArgument(kp: Keypair, target: PublicKey, stance: object, text: string): Promise<PublicKey> {
    const argument = recordPda('argument', kp.publicKey, await nextSeq(kp))
    await program.methods
      .postArgument(stance as never, sha(text), 'https://example.org/a')
      .accountsPartial({ authorRecord: authorPda(kp.publicKey), argument, target, author: kp.publicKey })
      .signers([kp])
      .rpc()
    made.argument = argument
    return argument
  }

  async function chainNow(): Promise<number> {
    const slot = await connection.getSlot('confirmed')
    return (await connection.getBlockTime(slot)) ?? Math.floor(Date.now() / 1000)
  }

  async function postPrediction(
    kp: Keypair,
    policy: PublicKey,
    resolver: PublicKey,
    checkAt: number,
    priorBps = 7000,
  ): Promise<PublicKey> {
    const prediction = recordPda('prediction', kp.publicKey, await nextSeq(kp))
    await program.methods
      .postPrediction(resolver, new anchor.BN(checkAt), priorBps, sha(`rule ${checkAt}`), 'ar://rule', 'https://example.org/source')
      .accountsPartial({ authorRecord: authorPda(kp.publicKey), prediction, policy, author: kp.publicKey })
      .signers([kp])
      .rpc()
    made.prediction = prediction
    return prediction
  }

  async function resolve(resolver: Keypair, prediction: PublicKey, outcome: object): Promise<PublicKey> {
    const resolution = pda([Buffer.from('resolution'), prediction.toBuffer()])
    await program.methods
      .resolvePrediction(outcome as never, sha('evidence'), 'https://example.org/evidence')
      .accountsPartial({ prediction, resolution, resolver: resolver.publicKey })
      .signers([resolver])
      .rpc()
    made.resolution = resolution
    return resolution
  }

  async function postLabel(kp: Keypair, target: PublicKey, tag: string): Promise<PublicKey> {
    const label = recordPda('label', kp.publicKey, await nextSeq(kp))
    await program.methods
      .postLabel(tag, new Array(32).fill(0), '')
      .accountsPartial({ authorRecord: authorPda(kp.publicKey), label, target, author: kp.publicKey })
      .signers([kp])
      .rpc()
    made.label = label
    return label
  }

  /** Assert the promise rejects, and that the failure names `code`. */
  async function refuses(p: Promise<unknown>, code: string) {
    let err: unknown = null
    try {
      await p
    } catch (e) {
      err = e
    }
    expect(err, `expected a refusal naming ${code}`).to.not.be.null
    const text = String((err as { message?: string }).message ?? err) + JSON.stringify((err as { logs?: string[] }).logs ?? [])
    expect(text, `refused, but not with ${code}`).to.include(code)
  }

  // ── the interface ──────────────────────────────────────────────────────────
  // Asserted against the published JSON (Rust names), not program.idl, which the
  // client has already camelCased: this is the file a reader would audit.
  const published = JSON.parse(readFileSync(new URL('../idl/deliberation.json', import.meta.url), 'utf8')) as {
    instructions: { name: string; accounts: { name: string; writable?: boolean }[] }[]
    accounts: { name: string }[]
  }

  describe('the interface', () => {
    it('is deployed at the id its IDL declares', async () => {
      const info = await connection.getAccountInfo(program.programId)
      expect(info?.executable).to.be.true
      expect(program.idl.address).to.equal(program.programId.toBase58())
    })

    it('has exactly six instructions, none of which edits, closes or configures', () => {
      const names = published.instructions.map((i) => i.name).sort()
      expect(names).to.deep.equal(
        ['post_argument', 'post_label', 'post_policy', 'post_prediction', 'register', 'resolve_prediction'].sort(),
      )
    })

    it('has no config, admin or editor account: only the six record kinds', () => {
      const accounts = published.accounts.map((a) => a.name).sort()
      expect(accounts).to.deep.equal(['Argument', 'Author', 'Label', 'Policy', 'Prediction', 'Resolution'])
    })

    it('never takes an existing record as writable: only the one it creates', () => {
      // Writable accounts per instruction: the payer, the author's own counter,
      // and the single new record. Anything else writable would be a path to
      // editing the record, and this test is the promise that there is none.
      const allowed: Record<string, string[]> = {
        register: ['author_record', 'author'],
        post_policy: ['author_record', 'policy', 'author'],
        post_argument: ['author_record', 'argument', 'author'],
        post_prediction: ['author_record', 'prediction', 'author'],
        resolve_prediction: ['resolution', 'resolver'],
        post_label: ['author_record', 'label', 'author'],
      }
      for (const ix of published.instructions) {
        const writable = ix.accounts
          .filter((a) => a.writable)
          .map((a) => a.name)
          .sort()
        expect(writable, ix.name).to.deep.equal([...allowed[ix.name]].sort())
      }
    })
  })

  // ── posting ────────────────────────────────────────────────────────────────
  describe('policies and arguments', () => {
    let alice: Keypair
    let bob: Keypair
    let policy: PublicKey

    before(async () => {
      alice = await registered()
      bob = await registered()
    })

    it('registers an author once, and refuses a second registration', async () => {
      const rec = await program.account.author.fetch(authorPda(alice.publicKey))
      expect(rec.key.toBase58()).to.equal(alice.publicKey.toBase58())
      expect(rec.nextSeq.toNumber()).to.equal(0)
      await refuses(
        program.methods.register().accountsPartial({ authorRecord: authorPda(alice.publicKey), author: alice.publicKey }).signers([alice]).rpc(),
        'already in use',
      )
    })

    it('posts a policy at the address its author and seq derive', async () => {
      policy = await postPolicy(alice, 'the slice v1')
      const p = await program.account.policy.fetch(policy)
      expect(p.author.toBase58()).to.equal(alice.publicKey.toBase58())
      expect(p.seq.toNumber()).to.equal(0)
      expect(p.contentHash).to.deep.equal(sha('the slice v1'))
      expect(p.parent).to.be.null
      expect((await nextSeq(alice)).toNumber()).to.equal(1)
    })

    it('records a revision and a fork as children of the parent', async () => {
      const revision = await postPolicy(alice, 'the slice v2', policy)
      const fork = await postPolicy(bob, 'a thinner slice', policy)
      expect((await program.account.policy.fetch(revision)).parent?.toBase58()).to.equal(policy.toBase58())
      const f = await program.account.policy.fetch(fork)
      expect(f.parent?.toBase58()).to.equal(policy.toBase58())
      expect(f.author.toBase58()).to.equal(bob.publicKey.toBase58())
    })

    it('refuses a parent that is not a policy', async () => {
      const arg = await postArgument(bob, policy, { against: {} }, 'no')
      await refuses(postPolicy(alice, 'orphan', arg), 'AccountDiscriminatorMismatch')
    })

    it('refuses an empty hash and a URI with a space', async () => {
      const p = recordPda('policy', alice.publicKey, await nextSeq(alice))
      const accts = { authorRecord: authorPda(alice.publicKey), policy: p, parent: null, author: alice.publicKey }
      await refuses(program.methods.postPolicy(new Array(32).fill(0), 'ar://x').accountsPartial(accts).signers([alice]).rpc(), 'EmptyHash')
      await refuses(program.methods.postPolicy(sha('x'), 'ar://x y').accountsPartial(accts).signers([alice]).rpc(), 'InvalidUri')
    })

    it('builds an argument tree: an argument on a policy, a reply on the argument', async () => {
      const against = await postArgument(bob, policy, { against: {} }, 'it leaves out the self-employed')
      const reply = await postArgument(alice, against, { amend: {} }, 'fair: widen it')
      const a = await program.account.argument.fetch(against)
      const r = await program.account.argument.fetch(reply)
      expect(a.target.toBase58()).to.equal(policy.toBase58())
      expect(a.targetKind).to.deep.equal({ policy: {} })
      expect(a.stance).to.deep.equal({ against: {} })
      expect(r.target.toBase58()).to.equal(against.toBase58())
      expect(r.targetKind).to.deep.equal({ argument: {} })
    })

    it('refuses an argument whose target is not one of its records', async () => {
      // A wallet, the program's own author counter, and a label are all refused.
      await refuses(postArgument(bob, alice.publicKey, { for: {} }, 'x'), 'InvalidTarget')
      await refuses(postArgument(bob, authorPda(alice.publicKey), { for: {} }, 'x'), 'InvalidTarget')
      const label = await postLabel(bob, policy, 'unsourced')
      await refuses(postArgument(bob, label, { for: {} }, 'x'), 'InvalidTarget')
    })
  })

  // ── predictions and resolutions ────────────────────────────────────────────
  describe('predictions and resolutions', () => {
    let asker: Keypair
    let resolver: Keypair
    let stranger: Keypair
    let policy: PublicKey

    before(async () => {
      asker = await registered()
      resolver = await funded()
      stranger = await funded()
      policy = await postPolicy(asker, 'a policy to test')
    })

    it('freezes the prediction: policy, resolver, check time, prior and rule', async () => {
      const checkAt = (await chainNow()) + 3_600
      const pred = await postPrediction(asker, policy, resolver.publicKey, checkAt, 6500)
      const p = await program.account.prediction.fetch(pred)
      expect(p.policy.toBase58()).to.equal(policy.toBase58())
      expect(p.resolver.toBase58()).to.equal(resolver.publicKey.toBase58())
      expect(p.checkAt.toNumber()).to.equal(checkAt)
      expect(p.priorBps).to.equal(6500)
      expect(p.ruleHash).to.deep.equal(sha(`rule ${checkAt}`))
    })

    it('refuses a certainty, a past check time, a millisecond timestamp and a null resolver', async () => {
      const now = await chainNow()
      await refuses(postPrediction(asker, policy, resolver.publicKey, now + 3_600, 0), 'InvalidPrior')
      await refuses(postPrediction(asker, policy, resolver.publicKey, now + 3_600, 10_000), 'InvalidPrior')
      await refuses(postPrediction(asker, policy, resolver.publicKey, now - 10), 'InvalidCheckTime')
      await refuses(postPrediction(asker, policy, resolver.publicKey, (now + 3_600) * 1000), 'InvalidCheckTime')
      await refuses(postPrediction(asker, policy, PublicKey.default, now + 3_600), 'InvalidResolver')
    })

    it('refuses a prediction against something that is not a policy', async () => {
      const arg = await postArgument(asker, policy, { neutral: {} }, 'context')
      await refuses(postPrediction(asker, arg, resolver.publicKey, (await chainNow()) + 3_600), 'AccountDiscriminatorMismatch')
    })

    it('refuses resolution before the check time, even by the named resolver', async () => {
      const pred = await postPrediction(asker, policy, resolver.publicKey, (await chainNow()) + 3_600)
      await refuses(resolve(resolver, pred, { held: {} }), 'TooEarly')
    })

    it('lets only the named resolver resolve, once, after the check time', async () => {
      const checkAt = (await chainNow()) + 2
      const pred = await postPrediction(asker, policy, resolver.publicKey, checkAt)
      // Wait for the chain's clock, not the host's, to pass the check time.
      for (let i = 0; i < 60 && (await chainNow()) < checkAt + 1; i++) await new Promise((r) => setTimeout(r, 500))

      await refuses(resolve(stranger, pred, { failed: {} }), 'NotTheResolver')
      // The asker named someone else, so the asker cannot mark it either.
      await refuses(resolve(asker, pred, { held: {} }), 'NotTheResolver')

      const resolution = await resolve(resolver, pred, { held: {} })
      const r = await program.account.resolution.fetch(resolution)
      expect(r.outcome).to.deep.equal({ held: {} })
      expect(r.resolver.toBase58()).to.equal(resolver.publicKey.toBase58())
      expect(r.prediction.toBase58()).to.equal(pred.toBase58())

      await refuses(resolve(resolver, pred, { failed: {} }), 'already in use')
      // And the prediction itself was never written to.
      expect((await program.account.prediction.fetch(pred)).checkAt.toNumber()).to.equal(checkAt)
    })
  })

  // ── labels ─────────────────────────────────────────────────────────────────
  describe('labels', () => {
    let author: Keypair
    let judge: Keypair
    let policy: PublicKey

    before(async () => {
      author = await registered()
      judge = await registered()
      policy = await postPolicy(author, 'labelled policy')
    })

    it('lets any registered key label any record, labels included', async () => {
      const l = await postLabel(judge, policy, 'unmeasurable')
      const meta = await postLabel(author, l, 'disputed')
      expect((await program.account.label.fetch(l)).tag).to.equal('unmeasurable')
      expect((await program.account.label.fetch(meta)).targetKind).to.deep.equal({ label: {} })
    })

    it('refuses a tag that is not a lowercase slug, and a half-given note', async () => {
      await refuses(postLabel(judge, policy, 'Unsourced'), 'InvalidTag')
      const label = recordPda('label', judge.publicKey, await nextSeq(judge))
      await refuses(
        program.methods
          .postLabel('unsourced', sha('note'), '')
          .accountsPartial({ authorRecord: authorPda(judge.publicKey), label, target: policy, author: judge.publicKey })
          .signers([judge])
          .rpc(),
        'InvalidOptionalUri',
      )
    })
  })

  // ── rate limit ─────────────────────────────────────────────────────────────
  describe('rate limit', () => {
    it('stops one key after its allowance for the window', async () => {
      const kp = await registered()
      const target = await postPolicy(kp, 'rate-limit target') // post 1
      const limit = 24 // MAX_POSTS_PER_WINDOW in state.rs
      for (let i = 1; i < limit; i++) await postLabel(kp, target, `n${i}`)
      expect((await program.account.author.fetch(authorPda(kp.publicKey))).postsInWindow).to.equal(limit)
      await refuses(postLabel(kp, target, 'one-too-many'), 'RateLimited')
      // A different key is unaffected: the limit bounds a key, not a person.
      const other = await registered()
      await postLabel(other, target, 'fine')
    })
  })

  // ── cost ───────────────────────────────────────────────────────────────────
  describe('cost', () => {
    it('reports each record size and its rent-exempt deposit on this validator', async () => {
      // Measured from real accounts the suite made, so it is the space the
      // program allocates (strings at their max), not a client-side estimate.
      const rows: string[] = []
      for (const kind of ['author', 'policy', 'argument', 'prediction', 'resolution', 'label']) {
        expect(made[kind], `no ${kind} was made earlier in the suite`).to.not.be.undefined
        const size = (await connection.getAccountInfo(made[kind]))!.data.length
        const lamports = await connection.getMinimumBalanceForRentExemption(size)
        rows.push(`${kind.padEnd(11)} ${String(size).padStart(4)} bytes  ${lamports} lamports (${(lamports / LAMPORTS_PER_SOL).toFixed(6)} SOL)`)
      }
      console.log('      ' + rows.join('\n      '))
    })
  })
})
