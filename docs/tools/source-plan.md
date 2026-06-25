# Source Plan

Sacred Book can learn from the shape of other scripting docs without importing their API behavior or wording. This page records that boundary so future updates stay clean.

## Reviewed For Structure Only

- Local topic archive: useful topic order for beginners, especially script structure, effect objects, effect types, callbacks, activation legality, filters/groups, card movement, Equip Card flow, LP damage/recovery patterns, set codes, and the DataEditorX-to-script workflow.
- A book-shaped VitePress site: useful as an example of getting-started pages, guides, API navigation, and local search.
- A machine-readable API documentation project: useful as an example of keeping API entries in data files that can feed both docs and tools.

## Project Rules

- Canonical behavior comes from MDPro3/YGOPro sources: `ygopro-core`, `Define/`, `Utilities/`, `Scripts/`, `cards.cdb`, and generated DataEditorX exports.
- External references can inspire organization, not wording, examples, function semantics, or non-local simulator assumptions.
- Examples should be linked to real MDPro3 scripts whenever possible, so users can jump from a function page to a card that actually uses it.
- When behavior is inferred from scripts or core code instead of directly documented, the page should say so clearly.

## Documentation Shape

- Function-page depth target: each important API page should explain when to use the function, how it fits into condition/cost/target/operation flow, common pitfalls, and a small MDPro3-style Lua example.
- Beginner path: teach script structure first, then small complete scripts, card data wiring, effect construction, activation flow, filters/groups, card movement, Equip Card flow, LP changes, and shared patterns.
- API pages: show signature, clean summary, parameters/returns, source files, used-by cards, and short script snippets.
- Tools: provide card/name/function/card-text search through the Script Explorer, with filters for card type and operation category labels.
- Data model: move reviewed function docs toward a small machine-readable override format with separate Chinese and English fields.

## Next Implementation Work

- Continue translating the highest-use `imported_from_dataeditorx` function descriptions.
- Add multilingual parameter and return notes so `_functions` and `_function_english` can both be polished without sharing one description field.
- Add deeper Script Explorer filters when local data exposes useful constants beyond card type and operation category.
- Continue source-backed wiki integration one page cluster at a time, expanding only gaps that are not already covered by focused Sacred Book guides.
