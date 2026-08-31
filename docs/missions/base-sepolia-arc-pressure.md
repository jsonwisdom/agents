# Base Sepolia ARC Pressure Mission

Status: EXECUTION SPEC
Target: jsonwisdom/COMPUTERWISDOM
Network: Base Sepolia only (chain ID 84532)

## Purpose

Build a reusable cross-harness agent/plugin that pressure-tests public COMPUTERWISDOM / Base Sepolia surfaces with transparent receipts.

This is not a media amplification system and must not target journalists, newsrooms, media accounts, social-media audiences, or unrelated third-party services.

## Hard exclusions

```text
MEDIA_TARGETING=false
NEWSROOM_SCRAPING=false
JOURNALIST_TARGETING=false
SOCIAL_AMPLIFICATION=false
SPAM_CANON=false
THIRD_PARTY_HARASSMENT=false
MAINNET=false
AUTONOMOUS_SIGNING=false
AUTHORITY_CREATED=false
NO_FAKE_GREEN=true
```

## Lane A — Public read pressure

- JSON-RPC read calls only by default.
- Provider-agnostic RPC URL supplied at runtime.
- Client-side concurrency/rate caps.
- Exponential backoff + jitter for 429/5xx/timeouts.
- Collect request count, success/failure, latency p50/p95/p99, RPC error classes, chain ID observed, latest block, start/end timestamps.
- Emit deterministic JSON receipt and human-readable summary.
- Refuse chain IDs other than 84532.
- Do not hammer Base's public shared RPC; sustained load requires a dedicated provider or operator-controlled node.

## Lane B — Bounded write pressure

- Disabled by default.
- Base Sepolia only.
- No autonomous signing.
- Every write requires an externally supplied signer/wallet approval surface.
- Configurable max transaction count and max spend/gas budget with conservative defaults.
- Never retry a submitted transaction blindly; reconcile by transaction hash first.
- Record pending/confirmed/reverted/unknown states.
- No mainnet fallback.

## ARC trajectory object

Each lane must declare:

- arc_id
- mode: READ | WRITE
- target_chain_id
- target_endpoint_class
- concurrency
- rate_limit
- duration
- max_requests / max_transactions
- backoff_policy
- stop_conditions
- receipt_path

## Required tests

- wrong-chain refusal
- rate-cap enforcement
- backoff behavior
- write-disabled default
- duplicate-transaction prevention
- media/news/social target rejection

## Required quality gates

Run the repo-standard gates from AGENTS.md:

```bash
make generate-all
make validate STRICT=1
make garden
make test
make smoke-test
```

## Delivery rule

Do not stop at a design memo. Implement the smallest complete source slice under `plugins/`, generate cross-harness outputs, run validation, and report exact files, commit/PR receipt, and test results.
