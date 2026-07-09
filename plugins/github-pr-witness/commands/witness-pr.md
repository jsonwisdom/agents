# witness-pr

Run a witness-only review of the current GitHub pull request.

## Behavior

Inspect the PR metadata, changed files, claims, and available evidence.

Return a reviewer-facing report suitable for posting as a PR comment.

## Hard constraints

- Do not approve the PR.
- Do not request merge.
- Do not certify correctness.
- Do not infer workflow success.
- Do not treat documentation as execution authority.
- If CI, receipts, hashes, CIDs, transactions, or reproduction paths are missing, mark the relevant claim as missing evidence.

## Expected output

Produce:

1. concise status
2. observed evidence
3. missing evidence
4. unsafe claims
5. recommended PR comment
6. final authority=false determination
