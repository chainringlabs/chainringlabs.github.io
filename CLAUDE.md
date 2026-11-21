# chainringlabs.com

## Overview

Static project-showcase website for the Chain Ring Labs GitHub organisation,
published with GitHub Pages at https://chainringlabs.com.

## Tech Stack

- Language: HTML, CSS, a few lines of JavaScript (no framework, no build step)
- Hosting: GitHub Pages, deployed by GitHub Actions from `site/`
- Fonts: Archivo and JetBrains Mono, self-hosted variable woff2

## Commands

- `python3 -m http.server 8473 --bind 127.0.0.1 --directory site` — preview locally
- `python3 scripts/check.py` — check every local reference resolves (run before pushing)

## Architecture

- `site/index.html` — the page. Three tiers in priority order: featured
  (`.feature`: TurfOps, Showrunner), services (`.service`: slacklistener,
  gmailclassifier), then the `.grid` of `.card`s. Project numbers ("No. 05")
  follow page order; renumber when the order changes and keep the "14 projects"
  count in the hero in step.
- `site/styles.css` — one stylesheet. Colours and fonts are custom properties on
  `:root`. Two width breakpoints: 980px and 680px.
- `site/script.js` — screenshot gallery buttons only.
- `site/assets/` — screenshots, fonts, `chainring.svg`.

## Conventions

- No third-party requests: no CDN scripts, fonts or analytics.
- Blurbs describe what a project's README says it does. Code panels quote real
  config or commands from that project, never invented output.
- Screenshots must not show personal data.
- `main` is protected by the org ruleset; changes land by pull request.

## Environment Variables

None.
