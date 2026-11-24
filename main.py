#!/usr/bin/env python3
"""Entry for make.fun bounty: charm the commuter — forecast for a city that does not exist.

Writes one line of weather forecast for the imaginary city of Puddlewick
to /output/entry.txt.
"""

import os

LINE = (
    "Puddlewick: rain again today, falling upward as usual — commuters are "
    "reminded to carry their umbrellas upside down and arrive dry."
)


def check_gate(text: str) -> None:
    """Gate: UTF-8, 1-140 characters, not only whitespace, single line."""
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    assert 1 <= len(text) <= 140, f"length {len(text)} outside 1-140"


def main() -> None:
    check_gate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
