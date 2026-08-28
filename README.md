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

Images are automatically resized, converted to WebP, given a `srcset`, and
lazy-loaded with explicit dimensions so the page doesn't jump as they load. The
`alt` attribute is worth filling in — it's what screen readers announce. A
missing image now fails the build loudly rather than emitting a broken `<img>`.

### Videos

Keep videos to **1080p H.264 MP4**, encoded with `+faststart` so playback can
begin before the file finishes downloading. Phones shoot 4K by default, which
produces absurd files — a 21-second 4K clip in this repo was 78 MB before it was
re-encoded. Convert before committing:

```sh
ffmpeg -i clip.mov -vf "scale=-2:'min(1080,ih)'" \
  -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 128k -movflags +faststart clip.mp4
```

If you drop a `demo-poster.jpg` next to `demo.mp4`, the shortcode picks it up
automatically as the video's poster frame — no extra markup needed.

### Cover images

The `cover` field in the post metadata sets the image that appears on the card on the homepage. Set it to the filename of an image in the same folder:

```toml
cover = 'cover.jpg'
```

The same image is cropped to 1200x630 and used as the social-sharing card
(`og:image`), so pick something that reads well at that aspect ratio.

### URLs

A post's URL comes from its `slug`, not its title or folder name:

```toml
slug = 'my-post-name'
```

**Always set it.** Without a slug Hugo derives the URL from the title, which
means renaming a post silently breaks its links. If you ever do need to change a
published URL, add the old one to `aliases` so the old link keeps working:

```toml
aliases = ['/the-old-url/']
```

### Drafts

Posts with `draft = true` won't show up on the live site. To preview drafts locally, run:

```sh
hugo server -D
```

## Project structure

```
archetypes/        Templates for new content (used by `hugo new`)
assets/            Processed at build time
  css/main.css     Main stylesheet (based on Pico CSS)
  css/syntax-*.css Code block colors (light / dark mode)
  icons/           Social icons (inlined into the page at build time)
content/           All the posts and pages
  projects/        Blog posts (each in its own folder)
  about.md         The about page
layouts/           HTML templates
  _default/        Base page wrappers
  partials/        Reusable pieces (head, header, footer, etc.)
  shortcodes/      Custom markdown helpers (img, video)
  projects/        Post-specific template
static/            Files served as-is (fonts, favicon, CNAME)
hugo.toml          Site configuration
```

## How it builds and deploys

Pushing to `master` triggers a GitHub Actions workflow that builds the site and deploys it to GitHub Pages. The workflow lives at `.github/workflows/hugo.yml`. You don't need to build anything manually — just push your changes and the site updates within a couple of minutes.

The workflow pins a Hugo version (`HUGO_VERSION`). Keep it in step with the Hugo
you run locally, or a template that works on your machine can fail in CI. The
custom domain is held by `static/CNAME`, so it survives even if the repo's Pages
setting is ever reset.

## Editing the styles

The main stylesheet is `assets/css/main.css`. It's a single plain CSS file built on top of [Pico CSS](https://picocss.com), a lightweight framework that styles plain HTML elements so you don't need to write classes for everything. Syntax highlighting for code blocks has its own pair of files — one for light mode, one for dark mode.

Dark mode works automatically based on your system preference.

## Editing the about page

It's just a markdown file at `content/about.md`. Edit it like any other text file.

## Configuration

All site settings live in `hugo.toml` at the root. Social links, site title, author name, and image processing settings are all in there.
