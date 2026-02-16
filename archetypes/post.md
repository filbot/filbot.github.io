+++
date = '{{ .Date }}'
draft = true
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
description = ''
tags = []
+++

<!--
# Page Bundle Post Template

This template creates a page bundle structure for your blog post.
Page bundles keep all related content (markdown + images) together.

## Workflow:

1. Create new post:
   hugo new content/my-project-name/index.md --kind post

2. Add images to the same directory:
   content/my-project-name/
     ├── index.md (this file)
     ├── hero-image.jpg
     ├── screenshot-1.png
     └── demo-video.mp4

3. Reference images using shortcodes:
   {{</* img src="hero-image.jpg" alt="Description of image" */>}}
   {{</* video src="demo-video.mp4" */>}}

## Image Shortcode Features:
- Automatically generates responsive images (9 different sizes)
- Converts to WebP format for optimal performance
- Lazy loading with blur-up placeholder effect
- Click to open lightbox view

## Best Practices:
- Use descriptive filenames (e.g., dashboard-setup.jpg not img001.jpg)
- Always include meaningful alt text for accessibility
- Use JPG for photos, PNG for screenshots/graphics
- Keep images under 2MB before upload (Hugo will optimize)
- Add captions using blockquote (>) below images

## Frontmatter Fields:
- title: Post title (required)
- date: Publication date (auto-generated)
- draft: Set to false when ready to publish
- description: Brief summary for SEO and previews
- tags: Array of tags like ['raspberrypi', 'howto', 'display']
-->

{{</* img src="hero-image.jpg" alt="Project overview" */>}}

## Introduction

Write your introduction here...

---

## Section Title

Add your content here...

{{</* img src="screenshot.png" alt="Description" */>}}
> Add an optional caption

---

## Another Section

More content...
