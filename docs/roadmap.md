# Sacred Book Roadmap

This is the working todo for turning Sacred Book into a complete MDPro3 scripting reference. The goal is to teach from the first script file through advanced card behavior, while keeping every reference page grounded in this repository's own data.

## Current Milestone

- [x] Publish the VitePress site through GitHub Pages.
- [x] Add a beginner learning path with MDPro3-focused examples.
- [x] Generate API and constant pages from the Sacred Book data.
- [x] Generate featured card example pages from `cards.cdb` and `Scripts/`.
- [x] Add the Script Explorer for searching cards and function usage.
- [x] Add function usage and script examples directly to API pages.
- [x] Add a generated translation review queue for awkward/imported function English.
- [x] Record the source-plan boundary for Miraheze/scrapi-book/scrapiyard inspiration without importing their API content.
- [ ] Translate and review the highest-use imported function descriptions.
- [ ] Add tutorial-style `How To Use It` sections to the highest-traffic API pages.

## Documentation Coverage

- [ ] Give every function a clear summary, parameter notes, return notes, and at least one script-backed example where possible.
- [ ] Review all `imported_from_dataeditorx` function English and replace awkward machine-style wording with natural MDPro3 terminology.
- [ ] Check for any raw Chinese text that leaked into English fields after each generation.
- [ ] Mark uncertain or inferred behavior clearly, with source confidence.
- [ ] Add focused pages for common scripting patterns: targeting, costs, operation flow, once-per-turn handling, field zones, counters, and summon procedures.
- [ ] Expand the beginner path with small complete card scripts that build up one concept at a time.
- [ ] Analyze every downloaded tutorial page and create an original Sacred Book equivalent for each topic.
- [ ] Add terminology review passes for official Yu-Gi-Oh! wording such as Graveyard, banish, GY, hand, Deck, Extra Deck, and Set.
- [ ] Move reviewed function docs into a multilingual machine-readable override file instead of keeping long manual batches in the generator.

## Data And Tools

- [x] Add generated "used by" sections to function pages from `/data/function-usage.json`.
- [x] Add source script snippets around detected function calls.
- [ ] Add card text search and category filtering to the Script Explorer.
- [ ] Sync reviewed `_functions` and `_function_english` exports into DataEditorX and commit that repo separately.
- [ ] Review `DataEditorX/data/lua/constant*` against the generated constant docs and export updated editor-facing files.
- [ ] Review `DataEditorX/data/mse` category and genre mappings against current scripts/locales.

## Quality Checks

- [ ] Add a site generation check in CI.
- [ ] Add markdown link validation for generated and hand-written pages.
- [ ] Add a data freshness report that compares scripts, constants, strings, and locale files against the source folders.
- [ ] Keep milestone commits small enough that generated-data changes are easy to review.
