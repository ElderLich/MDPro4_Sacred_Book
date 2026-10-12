# MDPro4 Sacred Book

Documentation and data-generation tools for MDPro4/YGOPro Lua card scripting.

This repository builds a VitePress site with beginner lessons, scripting guides,
generated API/reference pages, and card-script examples generated from
`cards.cdb` plus `Scripts/`. The Rush collection uses `rush_cards.cdb`,
`Rush/Scripts/`, and `Rush/Utilities/` separately, with its own helper reference
and a format selector in Script Explorer. Source commits are recorded in
`UPSTREAM_SOURCES.md`.

## Generate Everything

```powershell
npm install
npm run docs:generate
```

This runs:

1. `Tools/FunctionDocs/generate_function_docs.py`
2. `Tools/Site/generate_site.py`

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

To enable it:

1. Create a free Cloudflare account and open **Web Analytics → Add a site**.
   In **Set up hostname**, enter `elderlich.github.io` exactly: no `https://`,
   slash, or `/MDPro4_Sacred_Book/` path. Select the message box that appears
   beneath the field, choose **Done**, then copy the site's beacon token. This
   does not require moving the site or changing its DNS.
2. In this GitHub repository, open **Settings → Secrets and variables →
   Actions**, create a repository secret named
   `CLOUDFLARE_WEB_ANALYTICS_TOKEN`, and paste the token.
3. Rerun the **Deploy Sacred Book to GitHub Pages** workflow.

Keep the Cloudflare account private. The beacon token identifies which
analytics site receives events, but it does not provide dashboard access.
