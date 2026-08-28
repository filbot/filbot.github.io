+++
date = '{{ .Date }}'
draft = true
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
slug = '{{ .File.ContentBaseName }}'
description = ''
tags = []
cover = ''
+++

<!--
Create new post:
  hugo new content/projects/my-project-name/index.md --kind post

`slug` sets the URL and is prefilled from the folder name. Keep it set — without
it Hugo derives the URL from the title, so renaming the post breaks its links.
If you change a slug after publishing, add the old URL to `aliases`.

Add images and video to the same directory:
  content/projects/my-project-name/
    ├── index.md
    ├── cover.webp
    ├── screenshot.png
    ├── demo.mp4
    └── demo-poster.jpg   (optional; auto-detected as the video poster)

Videos should be 1080p H.264 MP4 with +faststart. See the README.

Reference them using shortcodes:
  {{</* img src="screenshot.png" alt="Description" */>}}
  {{</* video src="demo.mp4" */>}}
-->
