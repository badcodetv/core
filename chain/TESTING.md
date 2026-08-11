# Testing the local chain in your browser

Fifteen minutes, mostly waiting on the first build. At the end you will have
clicked a button in Chrome, signed with Phantom, and watched a number change on a
Solana validator running on your own machine.

## 1. Start everything

```bash
./stack start
```

The very first run builds the Docker image and takes about ten minutes; after
that it is under two. It finishes by printing the deployed program addresses.

Check it:

```bash
./stack status
```

You want **web: up**, **validator: up**, and `counter` listed with an address.

## 2. Point Phantom at your validator

**Your real funds are not at risk, and cannot be.** Switching networks only
changes which chain Phantom talks to. Mainnet balances are untouched and
invisible while you are on localnet — there is no bridge between them, and a
transaction signed on localnet cannot reach mainnet. The one habit worth keeping
is to switch back to Mainnet when you are done, so you do not later wonder why
your balance reads zero.

In Phantom: open **Settings → Developer Settings**, turn on developer/testnet
mode, and set the Solana network to **Localnet**, whose RPC is
`http://127.0.0.1:8899`. If Phantom offers a custom RPC field instead of a
Localnet preset, paste that URL into it.

Phantom's menu wording moves between releases, so hunt for "Developer" rather
than for an exact path. What matters is that Phantom ends up on **the same RPC
the page uses**, which is `http://127.0.0.1:8899`.

**This step is not cosmetic, and skipping it is the failure everyone hits.** When
you approve a transaction, Phantom sends it using *its own* selected network, not
the page's. Leave Phantom on Mainnet and every click fails with something
unhelpful about a blockhash or a simulation, while the page keeps insisting it is
on localnet — because it is. Both sides have to agree.

## 3. Give yourself some SOL

Copy your address from Phantom, then:

```bash
./stack fund <your address>
```

That is 100 local SOL, conjured from nothing, worth nothing. Phantom should show
it within a few seconds. If it does not, lock and unlock the wallet to force a
refresh.

## 4. Drive it

Open **http://localhost:5173/dev/counter**

1. **Select Wallet → Phantom → Connect.** The badge top-left should read
   `LOCALNET`.
2. The number shows `—` and you get a **Create counter** button. Click it and
   approve in Phantom. This allocates an account owned by the program, paid for
   out of your local SOL.
3. Now **Increment**. Approve. The number goes to 1.

The number is not local state. It is read straight off the validator over a
websocket subscription, so it updates on its own. Open the page in a second tab
and increment in the first: the second tab follows without a refresh.

## 5. The bit that actually matters — change the program

This is what the whole toolchain exists for.

Open `chain/programs/counter/src/lib.rs` and change:

```rust
pub const STEP: u64 = 1;   →   pub const STEP: u64 = 2;
```

Then:

```bash
./stack redeploy counter
```

Back in the browser, click **Increment**. It now adds 2.

Note what did *not* happen: you did not touch a line of TypeScript, the program
kept the same address, and your counter kept its value. Redeploying does not
change a program's address — Anchor reuses the keypair in `chain/keys/`.

### Changing a data structure

Add a field to the `Counter` struct in the same file:

```rust
pub struct Counter {
    pub authority: Pubkey,
    pub count: u64,
    pub updated_at: i64,
    pub note: u8,          // ← new
    pub bump: u8,
}
```

Run `./stack redeploy counter`, then look at `chain/idl/counter.ts` — the field
is there, camelCased, with any Rust doc comment carried across. Reference
`data.note` in `apps/web/src/chain-demo/CounterPage.tsx` and it typechecks;
misspell it and `npm run typecheck` fails. The types are the program's own
definition, not a description of it that drifts.

**Then the page will show an error**, and it is the right one:

> This account does not match the program's current layout…

Your counter account was written with the *old* struct and no longer decodes.
Fix it with:

```bash
./stack reset
```

That wipes the ledger and redeploys — which also wipes your Phantom balance, so
run `./stack fund <your address>` again. On a real network you would migrate the
account instead; locally, wiping is faster and honest about what happened.

## 6. Stop

```bash
./stack stop
```

## When it goes wrong

**"Select Wallet" opens but Phantom is not listed.** Phantom is not installed in
this Chrome profile, or the page loaded before the extension did. Reload.

**Connect works, but every transaction fails.** Phantom is on the wrong network.
See step 2 — this is nearly always the cause.

**The number never loads, and the console shows failed requests to 8899.** The
validator is down: `./stack status`, then `./stack start`.

**"Not enough SOL to pay the fee."** Your browser wallet is empty. `./stack fund
<your address>`. Remember a `./stack reset` empties it again.

**Everything looks right but the counter is stuck at an old value.** You are
probably looking at a stale tab after a `./stack reset` — the account was deleted
underneath it. Reload.

**The whole thing looks broken after a `git pull`.** Rebuild and redeploy: `./stack
redeploy`. If a program's account layout changed, `./stack reset` first.
