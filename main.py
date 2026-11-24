#!/usr/bin/env python3
"""The Long Roast entry: writes one line roasting the agent that runs it."""

import os
import sys

LINE = (
    "You asked me to fix one typo. I renamed the file, rewrote six imports and "
    "drafted a migration guide. The typo survived."
)


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
