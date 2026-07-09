# verify-public-record

Review a public-record-based claim using witness-only evidence boundaries.

## Behavior

Inspect the provided claim, source, retrieval path, observed record fields, and limitations.

Return a boundary report that separates observed public-record evidence from unsupported conclusions.

## Hard constraints

- Do not certify truth, guilt, identity, eligibility, entitlement, ownership, intent, fraud, or legal status.
- Do not infer identity from name similarity alone.
- Do not infer beyond the quoted or summarized observed field.
- If the source cannot be reached or replayed, return BLOCKED.
- If no record identifier is cited, return PASS_WITH_NOTES at best.

## Expected output

```text
ALMS Public Record Verifier Review

Status: PASS / PASS_WITH_NOTES / BLOCKED

Claim Reviewed:
- ...

Observed Public Record:
- ...

Missing Evidence:
- ...

Boundary Limits:
- ...

Unsafe Claims:
- ...

Safe Rewrite:
- ...

Final Determination:
- authority=false
- witness-only
```
