# Reverse-replay locators and reconstruction checks

Load this file when classifying locators or checking that a reconstruction is not a new story.

## Locator patterns

| Kind | Strong | Weak |
|---|---|---|
| plugin | `plugins/<name>/` plus files that exist | "the wisdom stuff" |
| git | full SHA | `HEAD`, "this branch" |
| PR | URL or number plus observed files | "the PR" |
| X | post URL or id | "that tweet" |
| CI | run ID + SHA | "CI passed" |

A deleted or missing path is `MISSING`, not proof the opposite team existed.

## Reconstruction check

A reconstruction is valid if a stranger with the same locators can:

1. Find the artifacts.
2. Agree the reconstructed question is one those artifacts can answer.
3. Agree the implied labor is named in those artifacts (agent files, plugin names, author fields).

If the roster needs a person who never appears in the locators, it is not reverse replay. It is staffing.

## Author / brains

When `plugin.json` author is Jason Wisdom, brains is Jason. Jay remains labor even when Jay writes the roster.

Do not infer brains from tone.

## Pairing

After this file, the same turn must name seats via `skills/team-from-replay`.
