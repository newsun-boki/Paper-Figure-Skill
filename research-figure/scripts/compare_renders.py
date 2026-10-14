#!/usr/bin/env python3
"""Visual QA aids for equal-sized reference and exported figures. Requires Pillow.

No similarity score or automatic scientific-quality verdict. Inputs are read only.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance


def load_on_white(path):
    with Image.open(path) as source:
        rgba = source.convert("RGBA")
        background = Image.new("RGBA", rgba.size, "white")
        return Image.alpha_composite(background, rgba).convert("RGB")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--render", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    reference = load_on_white(args.reference)
    render = load_on_white(args.render)
    if reference.size != render.size:
        parser.error(f"Canvas mismatch: {reference.size} vs {render.size}. "
                     "Export both at the same canvas size; do not distort to fit.")

    outputs = {name: args.out_dir / f"{name}.png" for name in
               ("side-by-side", "overlay", "difference")}
    inputs = {args.reference.resolve(), args.render.resolve()}
    if any(path.resolve() in inputs for path in outputs.values()):
        parser.error("Output paths must not replace either input image.")
    if not args.overwrite and any(path.exists() for path in outputs.values()):
        parser.error("Output already exists; use a new directory or --overwrite.")

    width, height = reference.size
    side = Image.new("RGB", (width * 2 + 24, height), "#E2E8F0")
    side.paste(reference, (0, 0))
    side.paste(render, (width + 24, 0))
    overlay = Image.blend(reference, render, 0.5)
    difference = ImageEnhance.Brightness(ImageChops.difference(reference, render)).enhance(4)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, picture in (("side-by-side", side), ("overlay", overlay), ("difference", difference)):
        picture.save(outputs[name])
    print("Left: reference. Right: exported figure. Overlay: 50/50. Difference: 4x brightness.")
    print("Inspect visually; pixel differences do not assess scientific correctness.")


if __name__ == "__main__":
    main()
