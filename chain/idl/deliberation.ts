/**
 * Program IDL in camelCase format in order to be used in JS/TS.
 *
 * Note that this is only a type helper and is not the actual IDL. The original
 * IDL can be found at `target/idl/deliberation.json`.
 */
export type Deliberation = {
  "address": "HXU6VKRYKMWNBe8qaqa6myKVcFpRK8pKNacuCvV9FC6Y",
  "metadata": {
    "name": "deliberation",
    "version": "0.1.0",
    "spec": "0.1.0",
    "description": "An append-only public record of proposals, arguments, dated predictions, their resolutions and advisory labels."
  },
  "instructions": [
    {
      "name": "postArgument",
      "docs": [
        "Post an argument for, against, amending or about a policy, a",
        "prediction, a resolution or another argument."
      ],
      "discriminator": [
        171,
        63,
        105,
        228,
        202,
        94,
        163,
        11
      ],
      "accounts": [
        {
          "name": "authorRecord",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  97,
                  117,
                  116,
                  104,
                  111,
                  114
                ]
              },
              {
                "kind": "account",
                "path": "author"
              }
            ]
          }
        },
        {
          "name": "argument",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  97,
                  114,
                  103,
                  117,
                  109,
                  101,
                  110,
                  116
                ]
              },
              {
                "kind": "account",
                "path": "author"
              },
              {
                "kind": "account",
                "path": "authorRecord.nextSeq",
                "account": "author"
              }
            ]
          }
        },
        {
          "name": "target",
          "docs": [
            "(owner, then discriminator) and of a kind an argument may target."
          ]
        },
        {
          "name": "author",
          "writable": true,
          "signer": true
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "stance",
          "type": {
            "defined": {
              "name": "stance"
            }
          }
        },
        {
          "name": "contentHash",
          "type": {
            "array": [
              "u8",
              32
            ]
          }
        },
        {
          "name": "uri",
          "type": "string"
        }
      ]
    },
    {
      "name": "postLabel",
      "docs": [
        "Attach an advisory label to any record. Any key; no power."
      ],
      "discriminator": [
        120,
        233,
        95,
        126,
        7,
        151,
        168,
        162
      ],
      "accounts": [
        {
          "name": "authorRecord",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  97,
                  117,
                  116,
                  104,
                  111,
                  114
                ]
              },
              {
                "kind": "account",
                "path": "author"
              }
            ]
          }
        },
        {
          "name": "label",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  108,
                  97,
                  98,
                  101,
                  108
                ]
              },
              {
                "kind": "account",
                "path": "author"
              },
              {
                "kind": "account",
                "path": "authorRecord.nextSeq",
                "account": "author"
              }
            ]
          }
        },
        {
          "name": "target"
        },
        {
          "name": "author",
          "writable": true,
          "signer": true
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "tag",
          "type": "string"
        },
        {
          "name": "noteHash",
          "type": {
            "array": [
              "u8",
              32
            ]
          }
        },
        {
          "name": "noteUri",
          "type": "string"
        }
      ]
    },
    {
      "name": "postPolicy",
      "docs": [
        "Post a policy. `parent`, if given, must be a policy already on the",
        "record (a revision of one's own, or a fork of someone else's)."
      ],
      "discriminator": [
        105,
        157,
        12,
        10,
        74,
        109,
        92,
        165
      ],
      "accounts": [
        {
          "name": "authorRecord",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  97,
                  117,
                  116,
                  104,
                  111,
                  114
                ]
              },
              {
                "kind": "account",
                "path": "author"
              }
            ]
          }
        },
        {
          "name": "policy",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  111,
                  108,
                  105,
                  99,
                  121
                ]
              },
              {
                "kind": "account",
                "path": "author"
              },
              {
                "kind": "account",
                "path": "authorRecord.nextSeq",
                "account": "author"
              }
            ]
          }
        },
        {
          "name": "parent",
          "docs": [
            "The policy this one revises or forks, if any. Read-only."
          ],
          "optional": true
        },
        {
          "name": "author",
          "writable": true,
          "signer": true
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "contentHash",
          "type": {
            "array": [
              "u8",
              32
            ]
          }
        },
        {
          "name": "uri",
          "type": "string"
        }
      ]
    },
    {
      "name": "postPrediction",
      "docs": [
        "Post a dated prediction against a policy, naming who will mark it.",
        "Everything about it is frozen here; there is no instruction to edit it."
      ],
      "discriminator": [
        115,
        29,
        186,
        96,
        84,
        47,
        214,
        168
      ],
      "accounts": [
        {
          "name": "authorRecord",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  97,
                  117,
                  116,
                  104,
                  111,
                  114
                ]
              },
              {
                "kind": "account",
                "path": "author"
              }
            ]
          }
        },
        {
          "name": "prediction",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  114,
                  101,
                  100,
                  105,
                  99,
                  116,
                  105,
                  111,
                  110
                ]
              },
              {
                "kind": "account",
                "path": "author"
              },
              {
                "kind": "account",
                "path": "authorRecord.nextSeq",
                "account": "author"
              }
            ]
          }
        },
        {
          "name": "policy",
          "docs": [
            "The policy the prediction tests. Read-only."
          ]
        },
        {
          "name": "author",
          "writable": true,
          "signer": true
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "resolver",
          "type": "pubkey"
        },
        {
          "name": "checkAt",
          "type": "i64"
        },
        {
          "name": "priorBps",
          "type": "u16"
        },
        {
          "name": "ruleHash",
          "type": {
            "array": [
              "u8",
              32
            ]
          }
        },
        {
          "name": "ruleUri",
          "type": "string"
        },
        {
          "name": "sourceUri",
          "type": "string"
        }
      ]
    },
    {
      "name": "register",
      "docs": [
        "Create the caller's author record. Once per key; required before the",
        "key posts. Free of any gate: anyone may register."
      ],
      "discriminator": [
        211,
        124,
        67,
        15,
        211,
        194,
        178,
        240
      ],
      "accounts": [
        {
          "name": "authorRecord",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  97,
                  117,
                  116,
                  104,
                  111,
                  114
                ]
              },
              {
                "kind": "account",
                "path": "author"
              }
            ]
          }
        },
        {
          "name": "author",
          "writable": true,
          "signer": true
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": []
    },
    {
      "name": "resolvePrediction",
      "docs": [
        "Resolve a prediction. Only its named resolver, only at or after its",
        "check time, only once (the resolution's address is derived from the",
        "prediction's, so a second `init` fails)."
      ],
      "discriminator": [
        199,
        159,
        54,
        235,
        121,
        68,
        53,
        137
      ],
      "accounts": [
        {
          "name": "prediction",
          "docs": [
            "Read-only: resolving writes a new account and never touches this one."
          ]
        },
        {
          "name": "resolution",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  114,
                  101,
                  115,
                  111,
                  108,
                  117,
                  116,
                  105,
                  111,
                  110
                ]
              },
              {
                "kind": "account",
                "path": "prediction"
              }
            ]
          }
        },
        {
          "name": "resolver",
          "writable": true,
          "signer": true
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "outcome",
          "type": {
            "defined": {
              "name": "outcome"
            }
          }
        },
        {
          "name": "evidenceHash",
          "type": {
            "array": [
              "u8",
              32
            ]
          }
        },
        {
          "name": "evidenceUri",
          "type": "string"
        }
      ]
    }
  ],
  "accounts": [
    {
      "name": "argument",
      "discriminator": [
        82,
        42,
        165,
        198,
        74,
        184,
        0,
        148
      ]
    },
    {
      "name": "author",
      "discriminator": [
        136,
        201,
        168,
        93,
        108,
        12,
        36,
        134
      ]
    },
    {
      "name": "label",
      "discriminator": [
        81,
        55,
        13,
        178,
        66,
        159,
        10,
        78
      ]
    },
    {
      "name": "policy",
      "discriminator": [
        222,
        135,
        7,
        163,
        235,
        177,
        33,
        68
      ]
    },
    {
      "name": "prediction",
      "discriminator": [
        98,
        127,
        141,
        187,
        218,
        33,
        8,
        14
      ]
    },
    {
      "name": "resolution",
      "discriminator": [
        31,
        13,
        235,
        201,
        17,
        66,
        5,
        138
      ]
    }
  ],
  "errors": [
    {
      "code": 6000,
      "name": "invalidUri",
      "msg": "A URI must be 1-200 bytes of printable ASCII with no spaces"
    },
    {
      "code": 6001,
      "name": "invalidOptionalUri",
      "msg": "An optional URI must be at most 200 bytes of printable ASCII with no spaces"
    },
    {
      "code": 6002,
      "name": "invalidTag",
      "msg": "A label tag must be 1-32 characters of a-z, 0-9 and -"
    },
    {
      "code": 6003,
      "name": "emptyHash",
      "msg": "A hash of all zeroes is not a hash"
    },
    {
      "code": 6004,
      "name": "invalidPrior",
      "msg": "A prior must be between 1 and 9999 basis points"
    },
    {
      "code": 6005,
      "name": "invalidResolver",
      "msg": "The resolver must be a real key"
    },
    {
      "code": 6006,
      "name": "invalidCheckTime",
      "msg": "The check time must be in the future and within the horizon"
    },
    {
      "code": 6007,
      "name": "invalidTarget",
      "msg": "That account is not a record this instruction can target"
    },
    {
      "code": 6008,
      "name": "notTheResolver",
      "msg": "Only the resolver named in the prediction may resolve it"
    },
    {
      "code": 6009,
      "name": "tooEarly",
      "msg": "This prediction cannot be resolved before its check time"
    },
    {
      "code": 6010,
      "name": "rateLimited",
      "msg": "This key has reached its posting limit for this window; try again later"
    },
    {
      "code": 6011,
      "name": "mathOverflow",
      "msg": "Arithmetic overflow"
    }
  ],
  "types": [
    {
      "name": "argument",
      "docs": [
        "One node of the debate tree: a reasoned position on a policy, a prediction,",
        "a resolution, or another argument."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "author",
            "type": "pubkey"
          },
          {
            "name": "seq",
            "type": "u64"
          },
          {
            "name": "target",
            "type": "pubkey"
          },
          {
            "name": "targetKind",
            "type": {
              "defined": {
                "name": "recordKind"
              }
            }
          },
          {
            "name": "stance",
            "type": {
              "defined": {
                "name": "stance"
              }
            }
          },
          {
            "name": "contentHash",
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "uri",
            "type": "string"
          },
          {
            "name": "createdAt",
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
      "name": "author",
      "docs": [
        "One per key that posts. Holds the key's sequence number (so every record's",
        "address is derivable without the client inventing ids) and its rate-limit",
        "window. Created by `register`; changed only by that key's own posts."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "key",
            "type": "pubkey"
          },
          {
            "name": "nextSeq",
            "docs": [
              "The seq the next record by this key will take. Also its total posts."
            ],
            "type": "u64"
          },
          {
            "name": "windowStart",
            "type": "i64"
          },
          {
            "name": "postsInWindow",
            "type": "u16"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "label",
      "docs": [
        "An advisory tag from any key on any record. Carries no power: no",
        "instruction in this program reads a label."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "author",
            "type": "pubkey"
          },
          {
            "name": "seq",
            "type": "u64"
          },
          {
            "name": "target",
            "type": "pubkey"
          },
          {
            "name": "targetKind",
            "type": {
              "defined": {
                "name": "recordKind"
              }
            }
          },
          {
            "name": "tag",
            "type": "string"
          },
          {
            "name": "noteHash",
            "docs": [
              "Optional reasoning; all zeroes and an empty URI when there is none."
            ],
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "noteUri",
            "type": "string"
          },
          {
            "name": "createdAt",
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
      "name": "outcome",
      "type": {
        "kind": "enum",
        "variants": [
          {
            "name": "held"
          },
          {
            "name": "failed"
          },
          {
            "name": "void"
          }
        ]
      }
    },
    {
      "name": "policy",
      "docs": [
        "A proposal: its text lives off-chain at `uri`; `content_hash` proves what",
        "the text said. `parent` makes revisions and forks a visible lineage: a",
        "parent by the same author reads as a revision, by another author as a fork."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "author",
            "type": "pubkey"
          },
          {
            "name": "seq",
            "type": "u64"
          },
          {
            "name": "contentHash",
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "uri",
            "type": "string"
          },
          {
            "name": "parent",
            "type": {
              "option": "pubkey"
            }
          },
          {
            "name": "createdAt",
            "type": "i64"
          },
          {
            "name": "createdSlot",
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
      "name": "prediction",
      "docs": [
        "A dated, falsifiable claim about the world, attached to a policy. Frozen at",
        "creation: the rule (metric, comparator, threshold, revision handling) is",
        "`rule_hash` of the text at `rule_uri`; the source is `source_uri`; who",
        "marks it is `resolver`. None of it can be changed afterwards by anyone."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "author",
            "type": "pubkey"
          },
          {
            "name": "seq",
            "type": "u64"
          },
          {
            "name": "policy",
            "type": "pubkey"
          },
          {
            "name": "resolver",
            "type": "pubkey"
          },
          {
            "name": "checkAt",
            "docs": [
              "Unix seconds. The resolver may act at or after this, never before."
            ],
            "type": "i64"
          },
          {
            "name": "priorBps",
            "docs": [
              "The author's stated probability that it holds, in basis points.",
              "Stored so calibration can be scored from the chain alone."
            ],
            "type": "u16"
          },
          {
            "name": "ruleHash",
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "ruleUri",
            "type": "string"
          },
          {
            "name": "sourceUri",
            "type": "string"
          },
          {
            "name": "createdAt",
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
      "name": "recordKind",
      "type": {
        "kind": "enum",
        "variants": [
          {
            "name": "policy"
          },
          {
            "name": "argument"
          },
          {
            "name": "prediction"
          },
          {
            "name": "resolution"
          },
          {
            "name": "label"
          }
        ]
      }
    },
    {
      "name": "resolution",
      "docs": [
        "The named resolver's signed verdict on one prediction. At most one per",
        "prediction, ever: its address is derived from the prediction's."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "prediction",
            "type": "pubkey"
          },
          {
            "name": "resolver",
            "type": "pubkey"
          },
          {
            "name": "outcome",
            "type": {
              "defined": {
                "name": "outcome"
              }
            }
          },
          {
            "name": "evidenceHash",
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "evidenceUri",
            "type": "string"
          },
          {
            "name": "resolvedAt",
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
      "name": "stance",
      "type": {
        "kind": "enum",
        "variants": [
          {
            "name": "for"
          },
          {
            "name": "against"
          },
          {
            "name": "amend"
          },
          {
            "name": "neutral"
          }
        ]
      }
    }
  ]
};
