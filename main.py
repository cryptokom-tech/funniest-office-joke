#!/usr/bin/env python3
"""Funniest Office Joke entry: one line about office life.

Writes a single one-line office joke (117 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, no network, deterministic.
"""

import os

JOKE = (
    "The birthday card has circulated for signatures since March. "
    "The birthday boy retired in May. We still need two more."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be whitespace-only"
    assert "\n" not in written, "entry must be a single line"
    assert written == written.strip(), "entry must not start/end with space"


if __name__ == "__main__":
    main()
