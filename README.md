# chainringlabs.com

The Chain Ring Labs website: a single static page that showcases the
organisation's open-source projects. Served by GitHub Pages at
<https://chainringlabs.com>.

## Layout

- `site/` is what gets published: `index.html`, `styles.css`, `script.js`,
  `404.html` and `assets/` (screenshots, fonts, the chainring mark).
- `scripts/check.py` checks that every local file the HTML and CSS refer to exists.
- `.github/workflows/pages.yml` runs the check on pull requests and deploys
  `site/` on every push to `main`.

There is no build step and there are no dependencies.

## Working on it

```sh
python3 -m http.server 8473 --bind 127.0.0.1 --directory site   # preview
python3 scripts/check.py                                        # before pushing
```

## Adding or changing a project

Each project is one block in `site/index.html`. Featured projects are
`<article class="feature">`, services are `<article class="service">` and
everything else is an `<article class="card">` in the grid. Screenshots go in
`site/assets/screenshots/`, named `<project>-<view>.png`; featured screenshots
are 1456 × 822.

## Fonts

Archivo and JetBrains Mono are self-hosted from `site/assets/fonts/`, both
under the SIL Open Font License 1.1. The page makes no third-party requests.

## License

MIT for the site's code. Screenshots belong to their projects.
