# review-pr

Run a receipt-first governance review of a pull request, commit, workflow, or technical claim.

## Behavior

Use the receipt auditor to inspect whether the reviewed change has observable evidence for every success, proof, deployment, ownership, verification, hash, CID, transaction, or CI claim.

Return a local audit report that separates observed evidence from missing evidence and unsafe language.

## Hard constraints

- Never mark PASS if any claim lacks observed run status, receipt, hash, CID, transaction, or reproducible path.
- Never infer success from a PR description, checklist, or branch name.
- Never treat documentation as execution authority.
- If evidence cannot be fetched, status = BLOCKED and list what is missing.

## Usage

Run `/review-pr` in any repository with an open PR or provided PR context. Requires repository read access when live GitHub evidence is requested.

## Expected output

```text
Receipt Auditor Review

Status: PASS / PASS_WITH_NOTES / BLOCKED

Observed Evidence:
- ...

Boundary Issues:
- ...

Missing Receipts:
- ...

Unsafe Claims:
- ...

Recommended Patch:
- ...

Final Determination:
- authority=false
- witness-only
```
