/**
 * Program IDL in camelCase format in order to be used in JS/TS.
 *
 * Note that this is only a type helper and is not the actual IDL. The original
 * IDL can be found at `target/idl/emperors_new_coin.json`.
 */
export type EmperorsNewCoin = {
  "address": "5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT",
  "metadata": {
    "name": "emperorsNewCoin",
    "version": "0.1.0",
    "spec": "0.1.0",
    "description": "Emperor's New Coin — supply pegged to the Fed's M2 money supply."
  },
  "instructions": [
    {
      "name": "ping",
      "docs": [
        "Proves the build/deploy/test loop works end to end. Removed once",
        "`initialize` lands."
      ],
      "discriminator": [
        173,
        0,
        94,
        236,
        73,
        133,
        225,
        153
      ],
      "accounts": [],
      "args": []
    }
  ]
};
