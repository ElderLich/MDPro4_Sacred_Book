# MDPro4 Sacred Book

Documentation and data-generation tools for MDPro4/YGOPro Lua card scripting.

This repository builds a VitePress site with beginner lessons, scripting guides,
generated API/reference pages, and card-script examples generated from
`cards.cdb` plus `Scripts/`. The Rush collection uses `rush_cards.cdb`,
`Rush/Scripts/`, and `Rush/Utilities/` separately, with its own helper reference
and a format selector in Script Explorer. Card Explorer, also under **Tools**,
browses every card in each database, including cards without scripts. It keeps
Standard and Rush separate, with searchable names, archetypes, complete card
text, Pendulum text, and card details. Source commits are recorded in
`UPSTREAM_SOURCES.md`.

## Generate Everything

```powershell
npm install
npm run docs:generate
```

This runs:

1. `Tools/FunctionDocs/generate_function_docs.py`
2. `Tools/Site/generate_site.py`, including Card Explorer data from
   `Tools/Site/generate_card_catalog.py`

Card Explorer data is generated locally from the checked-in databases and
archetype-name snapshot. It loads only the chosen format and requested card
details, so mobile visitors do not download every language or both formats at once.
The language selector remembers a browser's default; a shared link can override
it for that visit. Card-text search downloads its separate index only when enabled.
To refresh all localized snapshots, use the import command in "UPSTREAM_SOURCES.md". Run
`npm run site:test` to validate the site and card-data generators.

Tutorial navigation and analytics settings live in `docs/.vitepress/config.mts`.
The generator updates only `navigation.generated.json` for the API namespaces
and featured examples, so authored navigation survives every refresh.

## Preview Locally

```powershell
npm run docs:dev
```

## Build

```powershell
npm run docs:build
```

The production site is written to `docs/.vitepress/dist`.

## GitHub Pages

The workflow in `.github/workflows/deploy.yml` builds and deploys the site with
GitHub Actions. It asks GitHub to enable Pages automatically during deployment.

If GitHub blocks automatic enablement, open the repository settings and set
Pages to use `GitHub Actions` as the source, then rerun the workflow.

## Private Visitor Analytics

The production build supports optional Cloudflare Web Analytics. The public
site receives Cloudflare's cookie-free analytics beacon; traffic totals and
page reports remain in the Cloudflare account that owns the analytics site.
Local previews and builds without a token do not load the beacon.

