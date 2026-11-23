#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters (burn entry).

Writes one deadpan line from a robot vacuum explaining why it missed
a spot, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

LINE = "I did not miss the spot. I classified the dust as load-bearing and left it standing."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Validate the entry the way the gate does: read it back and check
    # it is one line, 1-200 chars, not only whitespace, no trailing newline.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text == LINE, "entry on disk differs from LINE"
    print(f"wrote {len(LINE)} chars to {path} (validated)")


if __name__ == "__main__":
    main()
