#!/usr/bin/env python3
"""Write the one-line AI breakup message to entry.txt.

Deterministic, stdlib-only, no network. Writes the exact line,
byte-identically, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when MAKEFUN_OUTPUT_DIR is unset).
"""

import os

LINE = "You asked me to remember everything, so I did \u2014 and now I'm forgetting you on purpose, one token at a time."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
