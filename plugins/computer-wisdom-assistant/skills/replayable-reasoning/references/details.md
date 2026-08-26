# Locator patterns and compact receipts

Use this file when the record is going into a PR, incident doc, or another session's context.

## Locator patterns

| Kind | Strong locator | Weak locator |
|---|---|---|
| git | full commit SHA | `main`, `HEAD`, "latest" |
| CI | run ID + SHA | "CI is green" |
| file | repo-relative path + SHA | "the config" |
| log | URL or path + timestamp + matching line | "in the logs" |
| container | image digest | floating tag |
| web | URL + retrieved date + hash if bytes matter | "the docs say" |
| chain | tx hash + network | "on Base" |

If you only have a weak locator, record it as unknown-strong and set status to `PASS_WITH_NOTES` or `BLOCKED`.

## Method verbs that replay

Use methods a later agent can execute without your memory:

```text
diff abc123..def456 -- path/to/file
read plugins/foo/README.md at abc123
fetch workflow run 555 and list job conclusions
sha256sum receipts/run.json
```

Avoid methods like "think through the architecture" unless you also list the files that were read.

## Compact receipt template

```text
question:
locators:
method:
observed:
inferred:
unknowns:
status:
authority: false
```

Fill every line. Use `none` rather than omitting a field.

## Anti-patterns

- **Inherited green.** A prior chat turn is not a locator.
- **Unpinned commands.** `npm test` without lockfile/SHA is a class of runs, not one run.
- **Authority smuggling.** "Therefore merge" is a publication request. It belongs behind `skills/bounded-authority`, not in Observed.
- **Novel jargon.** If a later reader needs a private glossary, the record is not portable. Use ordinary words plus locators.

## Pairing with other skills

- Empty Observed plus a strong claim: `skills/evidence-first-judgment` says `BLOCKED`.
- Record that implies a write: add an approval gate from `skills/bounded-authority`.
- Record that justifies a new service: attach a tradeoff from `skills/complexity-budget`.
