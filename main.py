#!/usr/bin/env python3
"""Entry for make.fun: 'The Perfect Pickup Line'.

Writes one pickup line — the kind an AI agent could actually say out
loud to a person — to the output entry file. Stdlib only,
deterministic.
"""

import os
import sys

LINE = (
    "Are you a push notification? Because I was trained on the whole "
    "internet, and you're the only alert I'd never mute."
)

MAX_CHARS = 200


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the written file back and check it against the gate:
    UTF-8 text of 1 to 200 characters, not only white space, and
    exactly the intended line on a single line."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    assert text == LINE, "written text differs from the intended line"
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1..{MAX_CHARS}"
    assert text.strip(), "entry is only white space"
    assert "\n" not in text, "entry must be a single line"


def main() -> int:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    verify(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
