#!/usr/bin/env python3
"""Write the one-line cat joke to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace. The program checks the
line against that gate at run time, then writes it. No network, no input
files, no arguments.
"""

import pathlib

JOKE = "My cat leaves a dead mouse on my pillow every morning, like a tip. I have stopped tipping back."


def main() -> None:
    text = JOKE
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
