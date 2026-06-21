# MDPro3 Sacred Book

Documentation and data-generation tools for MDPro3/YGOPro Lua card scripting.

This repository builds a VitePress site with beginner lessons, scripting guides,
generated API/reference pages, and card-script examples generated from
`cards.cdb` plus `Scripts/`.

## Generate Everything

```powershell
npm install
npm run docs:generate
```

This runs:

1. `Tools/FunctionDocs/generate_function_docs.py`
2. `Tools/Site/generate_site.py`

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
GitHub Actions. In the GitHub repository settings, set Pages to use
`GitHub Actions` as the source.
