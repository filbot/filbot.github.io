+++
date = '{{ .Date }}'
draft = true
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
description = ''
tags = []
cover = ''
+++

<!--
Create new post:
  hugo new content/projects/my-project-name/index.md --kind post

Add images to the same directory:
  content/projects/my-project-name/
    ├── index.md
    ├── cover.webp
    └── screenshot.png

Reference images using shortcodes:
  {{</* img src="screenshot.png" alt="Description" */>}}
  {{</* video src="demo.mp4" */>}}
-->
