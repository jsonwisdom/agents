# PR Evidence Map

Use this skill to map PR claims to supporting evidence.

## Claim types

- test passed
- CI passed
- deployed
- verified
- fixed
- secured
- owned
- signed
- hashed
- anchored
- receipt created
- transaction submitted

## Required evidence

| Claim | Required evidence |
|---|---|
| tests passed | command output or CI run |
| CI passed | workflow run tied to commit |
| deployed | deployment URL, receipt, or run log |
| verified | verifier output |
| fixed | diff + reproduction or test |
| secured | security check or scoped explanation |
| owned | signature, auth flow, or explicit proof |
| hashed | digest |
| CID created | CID + reachable artifact |
| transaction submitted | tx hash + chain/block context |

## Rule

No evidence means no green claim.
