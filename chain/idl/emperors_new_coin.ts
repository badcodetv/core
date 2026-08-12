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
      "name": "initAsset",
      "docs": [
        "Create one parody asset and its NFT. Called ten times, in order."
      ],
      "discriminator": [
        133,
        1,
        51,
        41,
        37,
        45,
        8,
        38
      ],
      "accounts": [
        {
          "name": "authority",
          "writable": true,
          "signer": true
        },
        {
          "name": "program",
          "docs": [
            "program — the same gate as `initialize`."
          ],
          "address": "5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT"
        },
        {
          "name": "programData"
        },
        {
          "name": "config",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "vault",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "writable": true
        },
        {
          "name": "assetMint",
          "docs": [
            "The NFT.",
            "",
            "`metadata_address` points at the mint itself, which is what \"embedded",
            "metadata\" means: there is no separate metadata account to lose."
          ],
          "writable": true
        },
        {
          "name": "vaultNftAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "account",
                "path": "tokenProgram"
              },
              {
                "kind": "account",
                "path": "assetMint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        },
        {
          "name": "rent",
          "address": "SysvarRent111111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        },
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "symbol",
          "type": "string"
        },
        {
          "name": "uri",
          "type": "string"
        },
        {
          "name": "genesisPrice",
          "type": "u64"
        }
      ]
    },
    {
      "name": "initialize",
      "docs": [
        "Create the mint, the vault, the rules and the printer. Once, ever, and",
        "only by the program's upgrade authority."
      ],
      "discriminator": [
        175,
        175,
        109,
        31,
        13,
        152,
        155,
        237
      ],
      "accounts": [
        {
          "name": "authority",
          "docs": [
            "The program's upgrade authority, and nobody else."
          ],
          "writable": true,
          "signer": true
        },
        {
          "name": "program",
          "docs": [
            "record of who may upgrade this program."
          ],
          "address": "5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT"
        },
        {
          "name": "programData"
        },
        {
          "name": "config",
          "docs": [
            "`init` is what makes this callable exactly once: the second attempt",
            "fails because the account already exists."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "printer",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  114,
                  105,
                  110,
                  116,
                  101,
                  114
                ]
              }
            ]
          }
        },
        {
          "name": "vault",
          "docs": [
            "authority, the landlord and the faucet, and it signs by seed."
          ],
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "mint",
          "docs": [
            "ENC itself. Classic SPL so every DEX can list it.",
            "",
            "**Freeze authority is `None`, and that is not optional.** A freeze",
            "authority is a live key over other people's coins; omitting the",
            "constraint is what sets it to `None` at creation, irreversibly.",
            "The mint authority stays on the vault PDA forever, so scanners will",
            "report ENC as arbitrarily inflatable — which is true, and is the joke."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  109,
                  105,
                  110,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "vaultTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        },
        {
          "name": "rent",
          "address": "SysvarRent111111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "params",
          "type": {
            "defined": {
              "name": "initializeParams"
            }
          }
        }
      ]
    },
    {
      "name": "syncM2",
      "docs": [
        "Read the oracle and move the supply to `k × M2`. **Anyone may call",
        "this.** The ten Asset PDAs go in `remaining_accounts`, writable, in",
        "index order."
      ],
      "discriminator": [
        183,
        4,
        78,
        180,
        186,
        237,
        229,
        237
      ],
      "accounts": [
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "printer",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  114,
                  105,
                  110,
                  116,
                  101,
                  114
                ]
              }
            ]
          }
        },
        {
          "name": "oracle",
          "docs": [
            "knows what shape this account has — a Switchboard feed in a real build,",
            "a mock in a mock one."
          ]
        },
        {
          "name": "mint",
          "writable": true
        },
        {
          "name": "vault",
          "docs": [
            "tokens this instruction may burn."
          ],
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "vaultTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        }
      ],
      "args": []
    }
  ],
  "accounts": [
    {
      "name": "asset",
      "discriminator": [
        234,
        180,
        241,
        252,
        139,
        224,
        160,
        8
      ]
    },
    {
      "name": "config",
      "discriminator": [
        155,
        12,
        170,
        224,
        30,
        250,
        204,
        130
      ]
    },
    {
      "name": "printer",
      "discriminator": [
        111,
        163,
        143,
        162,
        163,
        3,
        241,
        112
      ]
    }
  ],
  "events": [
    {
      "name": "synced",
      "discriminator": [
        114,
        244,
        163,
        97,
        99,
        80,
        164,
        70
      ]
    }
  ],
  "errors": [
    {
      "code": 6000,
      "name": "mathOverflow",
      "msg": "Arithmetic overflow or underflow"
    },
    {
      "code": 6001,
      "name": "invalidRate",
      "msg": "A rate was given outside the range 0-10000 basis points"
    },
    {
      "code": 6002,
      "name": "oracleUnavailable",
      "msg": "This build cannot read the oracle"
    },
    {
      "code": 6003,
      "name": "wrongFeed",
      "msg": "The quote is for a different feed than this program accepts"
    },
    {
      "code": 6004,
      "name": "staleRelease",
      "msg": "That M2 release has already been applied"
    },
    {
      "code": 6005,
      "name": "changeTooLarge",
      "msg": "M2 changed more in one release than the sanity cap allows"
    },
    {
      "code": 6006,
      "name": "mintTooLarge",
      "msg": "That would mint more in one step than the cap allows"
    },
    {
      "code": 6007,
      "name": "notUpgradeAuthority",
      "msg": "Only the program's upgrade authority may do that"
    },
    {
      "code": 6008,
      "name": "assetOutOfOrder",
      "msg": "Assets must be initialised in order"
    },
    {
      "code": 6009,
      "name": "notFullyInitialized",
      "msg": "The ten assets are not all initialised yet"
    },
    {
      "code": 6010,
      "name": "invalidAssetIndex",
      "msg": "Asset index out of range"
    },
    {
      "code": 6011,
      "name": "assetAlreadyInitialized",
      "msg": "That asset already exists"
    },
    {
      "code": 6012,
      "name": "wrongHolderAccount",
      "msg": "That token account does not belong to the holder"
    },
    {
      "code": 6013,
      "name": "invalidInterpolationWindow",
      "msg": "Invalid price interpolation window"
    },
    {
      "code": 6014,
      "name": "alreadyClaimedThisEpoch",
      "msg": "You have already claimed this epoch"
    },
    {
      "code": 6015,
      "name": "epochNotSettled",
      "msg": "That epoch is not settled yet"
    }
  ],
  "types": [
    {
      "name": "asset",
      "docs": [
        "One of the ten parody assets: a Token-2022 NFT, held for a term.",
        "",
        "The NFT itself never leaves program custody — this account records who holds",
        "the *tenancy*, and the holder's own wallet gets a certificate instead. That",
        "is what lets settlement be permissionless without a permanent delegate:",
        "there is no wallet to reach into."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "index",
            "type": "u8"
          },
          {
            "name": "holder",
            "docs": [
              "Who holds it. Equal to the vault PDA when the Emperor holds it — the",
              "client renders that case as \"unowned\". A sentinel rather than an",
              "`Option` so the account layout is fixed-size and the two cases cost the",
              "same to read."
            ],
            "type": "pubkey"
          },
          {
            "name": "priceFrom",
            "docs": [
              "Price interpolation: `price_from` at `interp_start`, `price_to` at",
              "`interp_end`, straight line between, flat outside. Every supply change",
              "rescales both endpoints and restarts the window, so the displayed price",
              "moves every slot rather than jumping once a month."
            ],
            "type": "u64"
          },
          {
            "name": "priceTo",
            "type": "u64"
          },
          {
            "name": "interpStart",
            "type": "i64"
          },
          {
            "name": "interpEnd",
            "type": "i64"
          },
          {
            "name": "lastTouched",
            "docs": [
              "When this asset was last written to — set by `init_asset` and by every",
              "price rescale.",
              "",
              "**Open for T12.** It was the rent clock; rent is gone. The auction needs",
              "a term anchor, and this field is either it or is replaced by an explicit",
              "`term_ends_at`. Left here rather than deleted so T12 decides deliberately",
              "instead of inheriting a guess made during a deletion."
            ],
            "type": "i64"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "config",
      "docs": [
        "The rules. Written once at `initialize`, never changed afterwards.",
        "",
        "There is deliberately no instruction that mutates the economic parameters —",
        "not gated behind an authority, not present at all — because the program ships",
        "non-upgradeable and \"not even we can change the rule\" has to be literally",
        "true, not merely intended. The single exception is `initialized_assets`,",
        "which counts up to ten during bootstrap and then never moves again."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "mint",
            "docs": [
              "The ENC mint. Classic SPL, 6 decimals, freeze authority `None`."
            ],
            "type": "pubkey"
          },
          {
            "name": "vault",
            "docs": [
              "The vault PDA — mint authority, landlord, and the Emperor's pocket."
            ],
            "type": "pubkey"
          },
          {
            "name": "expectedFeedId",
            "docs": [
              "The Switchboard feed this program will accept a quote from, and only",
              "this one. A feed *is* the hash of its own fetch job, so pinning the hash",
              "pins the data source itself: no key exists that could repoint it."
            ],
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "k",
            "docs": [
              "Base units of ENC per unit of `m2_value`. `supply = k × m2_value`."
            ],
            "type": "u64"
          },
          {
            "name": "encDecimals",
            "docs": [
              "Decimals on the mint. Six: nine would overflow u64 at this supply."
            ],
            "type": "u8"
          },
          {
            "name": "faucetAlphaBps",
            "docs": [
              "Share of the distributable surplus paid out per epoch, in basis points."
            ],
            "type": "u16"
          },
          {
            "name": "floorBps",
            "docs": [
              "The vault's floor, in basis points of total supply. Below it the faucet",
              "pays nothing at all — no share, no welcome grant."
            ],
            "type": "u16"
          },
          {
            "name": "welcomeGrant",
            "docs": [
              "One-off payment to a wallet's first ever claim, in base units."
            ],
            "type": "u64"
          },
          {
            "name": "grantsPerEpoch",
            "docs": [
              "How many welcome grants may be issued in a single epoch."
            ],
            "type": "u16"
          },
          {
            "name": "maxChangeBps",
            "docs": [
              "Largest M2 move, in basis points, this program will believe in one",
              "release."
            ],
            "type": "u16"
          },
          {
            "name": "maxSingleMint",
            "docs": [
              "Largest mint, in base units, this program will perform in one sync."
            ],
            "type": "u64"
          },
          {
            "name": "initializedAssets",
            "docs": [
              "Counts up to `ASSET_COUNT` during bootstrap. The only mutable field."
            ],
            "type": "u8"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "initializeParams",
      "docs": [
        "The economic parameters, chosen once and then unchangeable.",
        "",
        "Supplied by the caller rather than hardcoded so `chain/params.genesis.json`",
        "stays the single source of truth and T15 can replace the placeholders",
        "without touching Rust. Everything here is validated below; nothing here has",
        "a setter anywhere in the program."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "expectedFeedId",
            "docs": [
              "The Switchboard feed this program will ever accept a quote from."
            ],
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "k",
            "docs": [
              "Base units of ENC per unit of `m2_value`."
            ],
            "type": "u64"
          },
          {
            "name": "faucetAlphaBps",
            "type": "u16"
          },
          {
            "name": "floorBps",
            "type": "u16"
          },
          {
            "name": "welcomeGrant",
            "type": "u64"
          },
          {
            "name": "grantsPerEpoch",
            "type": "u16"
          },
          {
            "name": "maxChangeBps",
            "type": "u16"
          },
          {
            "name": "maxSingleMint",
            "type": "u64"
          }
        ]
      }
    },
    {
      "name": "printer",
      "docs": [
        "What the Fed last told us, and what we did about it."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "m2Value",
            "docs": [
              "M2SL in **billions of USD, fixed-point with 6 decimals**.",
              "`22176.1` is stored as `22_176_100_000`. Getting this wrong by a factor",
              "of a thousand is the easiest catastrophic mistake available here."
            ],
            "type": "u64"
          },
          {
            "name": "m2ReleaseDate",
            "docs": [
              "Unix seconds of the **Fed's release**, not of our sync. This is what the",
              "anti-double-mint guard compares, because it is the only timestamp an",
              "attacker cannot advance by waiting."
            ],
            "type": "i64"
          },
          {
            "name": "lastSyncSlot",
            "docs": [
              "Slot of the last successful sync. Informational."
            ],
            "type": "u64"
          },
          {
            "name": "targetSupply",
            "docs": [
              "`k × m2_value` at the last sync — what supply was aimed at.",
              "",
              "Actual supply can sit *above* this, when a burn was larger than the",
              "vault could cover. That is the honest invariant: `supply ≥ k × M2`."
            ],
            "type": "u64"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "synced",
      "docs": [
        "Emitted on every successful sync, so the website and any indexer can show",
        "what the printer did without replaying the whole chain."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "m2Value",
            "type": "u64"
          },
          {
            "name": "m2ReleaseDate",
            "type": "i64"
          },
          {
            "name": "targetSupply",
            "type": "u64"
          },
          {
            "name": "supplyDelta",
            "docs": [
              "Positive when minted, negative when burned."
            ],
            "type": "i128"
          },
          {
            "name": "uncoveredBurn",
            "docs": [
              "How much of a burn the vault could not cover. Non-zero means supply is",
              "left above target on purpose."
            ],
            "type": "u64"
          },
          {
            "name": "slot",
            "type": "u64"
          }
        ]
      }
    }
  ]
};
