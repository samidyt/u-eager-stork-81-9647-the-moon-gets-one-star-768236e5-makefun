#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon.

Writes the review to /output/entry.txt. The review must be UTF-8 text of
1 to 120 characters, not only white space, per the bounty gate.
"""

import os

# Bounty gate: the entry must be 1 to 120 characters of UTF-8 text.
MAX_CHARS = 120

REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Would not recommend. Ruins my sleep, "
    "drags the ocean around, then vanishes for days. Ghosted by a rock."
)


def main() -> None:
    text = REVIEW.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
