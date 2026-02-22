# Semicolons & Side Projects

Personal blog at [filbot.com](https://filbot.com) — built with [Hugo](https://gohugo.io), styled with [Pico CSS](https://picocss.com), and deployed to GitHub Pages.

## Getting started

You just need Hugo installed on your machine. Install it with Homebrew:

```sh
brew install hugo
```

Then clone the repo and start the local dev server:

```sh
git clone https://github.com/filbot/filbot.github.io.git
cd filbot.github.io
hugo server
```

Open [localhost:1313](http://localhost:1313) in your browser. The page will automatically reload whenever you save a file.

## Writing a new post

Each post is a folder inside `content/projects/`. The folder holds the markdown file along with any images or videos that go with it. Hugo calls this a "page bundle" — it just means everything for a post lives together in one place.

To scaffold a new post:

```sh
hugo new content/projects/my-post-name/index.md --kind post
```

That creates a folder like this:

```
content/projects/my-post-name/
  └── index.md
```

Open `index.md` and you'll see some metadata at the top between the `+++` markers. Fill in the title, description, and tags. The post starts as a draft — when you're ready to publish, change `draft = true` to `draft = false`.

### Adding images

Drop image files right into the same folder as `index.md`:

```
content/projects/my-post-name/
  ├── index.md
  ├── cover.jpg
  ├── wiring-closeup.png
  └── demo.mp4
```

Then reference them in your markdown using shortcodes:

```
{{< img src="wiring-closeup.png" alt="Close-up of the wiring" >}}

{{< img src="diagram.png" alt="Circuit layout" caption="Final wiring diagram" >}}

{{< video src="demo.mp4" >}}
```

Images are automatically resized, converted to WebP, and lazy-loaded. You don't need to do anything special — just use reasonably sized source files (under 2 MB or so) and the build handles the rest.

### Cover images

The `cover` field in the post metadata sets the image that appears on the card on the homepage. Set it to the filename of an image in the same folder:

```toml
cover = 'cover.jpg'
```

### Drafts

Posts with `draft = true` won't show up on the live site. To preview drafts locally, run:

```sh
hugo server -D
```

## Project structure

```
archetypes/        Templates for new content (used by `hugo new`)
assets/css/        Stylesheets
  main.css         Main stylesheet (based on Pico CSS)
  syntax-light.css Code block colors (light mode)
  syntax-dark.css  Code block colors (dark mode)
content/           All the posts and pages
  projects/        Blog posts (each in its own folder)
  about.md         The about page
layouts/           HTML templates
  _default/        Base page wrappers
  partials/        Reusable pieces (head, header, footer, etc.)
  shortcodes/      Custom markdown helpers (img, video)
  projects/        Post-specific template
static/            Files served as-is (fonts, icons, favicon)
hugo.toml          Site configuration
```

## How it builds and deploys

Pushing to `master` triggers a GitHub Actions workflow that builds the site and deploys it to GitHub Pages. The workflow lives at `.github/workflows/hugo.yml`. You don't need to build anything manually — just push your changes and the site updates within a couple of minutes.

## Editing the styles

The main stylesheet is `assets/css/main.css`. It's a single plain CSS file built on top of [Pico CSS](https://picocss.com), a lightweight framework that styles plain HTML elements so you don't need to write classes for everything. Syntax highlighting for code blocks has its own pair of files — one for light mode, one for dark mode.

Dark mode works automatically based on your system preference.

## Editing the about page

It's just a markdown file at `content/about.md`. Edit it like any other text file.

## Configuration

All site settings live in `hugo.toml` at the root. Social links, site title, author name, and image processing settings are all in there.
