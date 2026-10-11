# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Personal Hugo blog (filbot.com). No npm, no theme, no tests or linter: just Hugo templates, one CSS file, and Markdown page bundles. `README.md` covers authoring posts, slugs, shortcode usage, video encoding, and the project layout.

## Commands

- `hugo server` runs the dev server on :1313 (`.claude/launch.json` adds `--disableFastRender`). Add `-D` to include drafts.
- `hugo --gc --minify` reproduces the production build into `public/`. A clean build is the only check there is, and the `img` shortcode fails the build on a missing image, so a broken reference shows up here.
- `hugo new content/projects/<slug>/index.md --kind post` scaffolds a post from `archetypes/post.md`, with `slug` prefilled from the folder name.

Deploy happens on push to `master` via `.github/workflows/hugo.yml`, which pins `HUGO_VERSION`. Compare it with `hugo version` before using a template function that may not exist on one side. `public/` and `resources/_gen/` are build output and gitignored.

## How the site fits together

- **URLs**: `permalinks.projects = "/:slug/"` puts every post at the site root. Every post sets `slug`; without one Hugo falls back to the urlized title, so a title edit would silently move the page. When a published URL changes, add the old path to `aliases`.
- **Homepage** (`layouts/index.html`) is the only post listing: projects newest first, paginated (`pagerSize` in `hugo.toml`), each rendered by `partials/project-card.html`. `content/projects/_index.md` sets `render = 'never'`, so `/projects/` itself does not exist.
- **Taxonomies are disabled** (`disableKinds`). `tags` in front matter are stored but generate no pages.
- **Front matter params the templates read**: `cover` (a page-bundle image, cropped to 640x427 for the card and 1200x630 for `og:image`), `description` (card text and meta description, falling back to summary then `site.Params.description`), `repository` (renders a Repository button), `toc`, `noindex`.
- **Post vs. page chrome**: `baseof.html` shows the site header only on list pages and `type: page` content. Posts use `layouts/projects/single.html`, which has a back link instead. `head.html` owns `<title>` and all meta tags.
- **Images and video** go through the `img` and `video` shortcodes, which resolve files from the page bundle. Raw HTML in Markdown is stripped (`goldmark.renderer.unsafe = false`) and inline shortcodes are disabled, so new embed behaviour means a new file in `layouts/shortcodes/`.
- **Social icons** live in `assets/icons/` (not `static/`) because `footer.html` inlines the SVG markup; links come from `params.social` in `hugo.toml`.
- **CSS**: `assets/css/main.css` is Pico CSS v2.1.1 vendored in full, with site-specific styles appended from around line 2200 onward. Edit site styles there rather than Pico's rules. Syntax highlighting is class-based (`noClasses = false`) with separate light and dark stylesheets selected by `prefers-color-scheme`. CSS is minified and fingerprinted only in production.
- `static/CNAME` holds the custom domain. Google Analytics is configured in `hugo.toml`.
