#!/usr/bin/env python3
"""Generate a QR code for the apartment sales page."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


DEFAULT_URL = "https://sren95.github.io/bolig-til-salg/"
DEFAULT_OUTPUT = "qr-code.png"
DEFAULT_CENTER_TEXT = "Sundgade 1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a QR code image linking to the apartment website."
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"URL to encode. Defaults to {DEFAULT_URL}",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Output PNG file. Defaults to {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--box-size",
        type=int,
        default=18,
        help="Pixel size for each QR module. Defaults to 18.",
    )
    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="White border size in QR modules. Defaults to 4.",
    )
    parser.add_argument(
        "--center-text",
        default=DEFAULT_CENTER_TEXT,
        help=f"Text to place in the QR center. Defaults to {DEFAULT_CENTER_TEXT!r}.",
    )
    parser.add_argument(
        "--no-center-text",
        action="store_true",
        help="Generate a plain QR code without center text.",
    )
    return parser.parse_args()


def load_font(size: int):
    from PIL import ImageFont

    font_candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ]
    for font_path in font_candidates:
        if Path(font_path).exists():
            return ImageFont.truetype(font_path, size=size)
    return ImageFont.load_default()


def add_center_text(image, text: str) -> None:
    from PIL import ImageDraw

    draw = ImageDraw.Draw(image)
    max_text_width = int(image.width * 0.42)
    font_size = max(18, int(image.width * 0.07))
    font = load_font(font_size)

    while font_size > 18:
        text_box = draw.textbbox((0, 0), text, font=font)
        text_width = text_box[2] - text_box[0]
        if text_width <= max_text_width:
            break
        font_size -= 2
        font = load_font(font_size)

    text_box = draw.textbbox((0, 0), text, font=font)
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]
    padding_x = int(image.width * 0.035)
    padding_y = int(image.width * 0.022)
    label_width = text_width + padding_x * 2
    label_height = text_height + padding_y * 2
    x0 = (image.width - label_width) // 2
    y0 = (image.height - label_height) // 2
    x1 = x0 + label_width
    y1 = y0 + label_height
    radius = max(10, int(image.width * 0.018))

    draw.rounded_rectangle(
        (x0, y0, x1, y1),
        radius=radius,
        fill="#ffffff",
        outline="#18201d",
        width=max(2, image.width // 300),
    )
    draw.text(
        ((image.width - text_width) // 2, (image.height - text_height) // 2 - text_box[1]),
        text,
        fill="#18201d",
        font=font,
    )


def main() -> int:
    args = parse_args()

    try:
        import qrcode
        import PIL  # noqa: F401
        from qrcode.constants import ERROR_CORRECT_H
    except ModuleNotFoundError:
        print(
            "Missing dependency: install qrcode with PNG support first:\n"
            "  python3 -m pip install \"qrcode[pil]\"",
            file=sys.stderr,
        )
        return 1

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=args.box_size,
        border=args.border,
    )
    qr.add_data(args.url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="#18201d", back_color="#ffffff").convert("RGB")
    if args.center_text and not args.no_center_text:
        add_center_text(image, args.center_text)

    image.save(output)

    print(f"Wrote QR code for {args.url} to {output}")
    return 0


if __name__ == "__main__":
    main()
