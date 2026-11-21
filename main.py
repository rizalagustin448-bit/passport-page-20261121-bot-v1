#!/usr/bin/env python3
"""passport-page-20261121-bot-v1: copy the pre-rendered entry.png to output.

The entry is an invented passport spread for the Republic of Sulara
(salt-flat republic): data page with portrait + MRZ, visa page with
arrival/departure stamps from Almara and Tevrin, a salt-harvest permit,
and a visa condition (entry by salt road only, dry season only).

Why a copy instead of drawing: the make.fun server runs the entrypoint
with Python 3.13 standard library ONLY -- nothing is installed before it
runs (see RULES.txt). The image is drawn offline with Pillow and shipped
as entry.png, so this program only copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default "/output").

Stdlib only: os, shutil, pathlib. No Pillow, no fonts, no network.
"""

import os
import shutil
import struct
from pathlib import Path

MAX_BYTES = 1_048_576
EXPECTED_W, EXPECTED_H = 1024, 1024


def validate_png(path: Path) -> None:
    """Fail loudly if the shipped entry.png breaks the bounty limits.

    Size cap 1,048,576 bytes and 1024x1024 pixels (RULES.txt). Dimensions
    are read from the PNG IHDR chunk with struct -- stdlib only, no Pillow.
    """
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise SystemExit(
            f"entry.png too large: {size} bytes > {MAX_BYTES} byte limit"
        )
    with path.open("rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if header[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        raise SystemExit(
            f"entry.png is {width}x{height}, expected "
            f"{EXPECTED_W}x{EXPECTED_H}"
        )


def main() -> None:
    src = Path(__file__).with_name("entry.png")
    validate_png(src)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out / "entry.png")
    print(f"copied {src} -> {out / 'entry.png'}")


if __name__ == "__main__":
    main()
