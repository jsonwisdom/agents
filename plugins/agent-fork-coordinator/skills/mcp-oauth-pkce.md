# MCP OAuth PKCE Boundary

Use this skill when a fork coordinator proposes or uses an MCP server that requires OAuth authorization.

## Rule

OAuth enables access. It does not grant authority.

A fork may request a token only for the minimum read scope required by the task. Write-capable scopes require explicit operator approval and must be excluded by default.

## Discovery

Before authorization, observe the authorization server metadata.

Required discovery fields:

- issuer
- authorization_endpoint
- token_endpoint
- supported response types
- supported code challenge methods
- supported scopes if available

If discovery fails, return BLOCKED.

## PKCE requirements

- Use S256.
- Generate a fresh code_verifier per fork.
- Do not reuse code_verifier values.
- Do not expose code_verifier to subagents.
- Store token only in the coordinator boundary.
- Never place tokens in subagent prompts, logs, reports, or environment exports.

## Token receipt

Every token event must record:

- event: token_issued
- timestamp
- server
- scope
- audience if available
- expiration if available
- storage boundary
- authority=false

Do not record token secrets.

## Tool invocation receipt

Every MCP tool call must record:

- event: tool_invoked
- timestamp
- server
- tool
- requested resource
- read/write classification
- approval status
- authority=false

Every result must record:

- event: tool_result_observed
- timestamp
- observed fields
- missing fields
- result boundary
- authority=false

## Failure states

Return BLOCKED when:

- discovery endpoint is unavailable
- S256 is unsupported
- requested scope exceeds task boundary
- token would be exposed to a subagent
- tool is write-capable and no explicit operator approval exists
- result cannot be tied to a task, repo, PR, commit, or source path

## Safe language

Use:

- access requested
- token issued to coordinator boundary
- read-only scope observed
- tool result observed
- missing evidence
- blocked pending approval
- authority=false

Never use:

- authorized to mutate
- approved
- verified
- certified
- safe to merge

unless a separate human approval and evidence path exists.
