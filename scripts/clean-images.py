#!/usr/bin/env python3
"""Prepare source photos for a post: strip metadata (GPS included) and cap size.

Usage: scripts/clean-images.py content/projects/my-post [more dirs or files...]

Hugo only ever serves resized copies (at most 1536px wide), so source images
are capped at MAX_EDGE on the long side to keep the repo and builds lean.
Images that need resizing or rotating are re-encoded with Pillow; everything
else is stripped losslessly with exiftool. The ICC colour profile is kept.

Needs Pillow (pip install pillow) and exiftool (brew install exiftool).
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_EDGE = 2560
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def images(args):
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            yield from sorted(f for f in p.rglob("*") if f.suffix.lower() in EXTENSIONS)
        elif p.suffix.lower() in EXTENSIONS:
            yield p


def reencode(path, im):
    icc = im.info.get("icc_profile")
    im = ImageOps.exif_transpose(im)
    if max(im.size) > MAX_EDGE:
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.Resampling.LANCZOS)
    fmt = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".webp": "WEBP"}[path.suffix.lower()]
    opts = {"icc_profile": icc} if icc else {}
    if fmt == "JPEG":
        im = im.convert("RGB")
        opts.update(quality=90, optimize=True, progressive=True)
    elif fmt == "WEBP":
        opts.update(quality=90, method=6)
    else:
        opts.update(optimize=True)
    im.save(path, fmt, **opts)
    return im.size


def main(args):
    if not args:
        sys.exit(__doc__)
    paths = list(images(args))
    for path in paths:
        with Image.open(path) as im:
            im.load()
            rotated = im.getexif().get(0x0112, 1) != 1
            if rotated or max(im.size) > MAX_EDGE:
                before = im.size
                after = reencode(path, im)
                print(f"resized {path}: {before[0]}x{before[1]} -> {after[0]}x{after[1]}")
    if paths:
        subprocess.run(
            ["exiftool", "-q", "-q", "-overwrite_original", "-all=",
             "-tagsfromfile", "@", "-icc_profile", *map(str, paths)],
            check=True,
        )
        print(f"stripped metadata from {len(paths)} image(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
