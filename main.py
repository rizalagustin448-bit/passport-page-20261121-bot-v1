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
from pathlib import Path


def main() -> None:
    src = Path(__file__).with_name("entry.png")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out / "entry.png")
    print(f"copied {src} -> {out / 'entry.png'}")


if __name__ == "__main__":
    main()
