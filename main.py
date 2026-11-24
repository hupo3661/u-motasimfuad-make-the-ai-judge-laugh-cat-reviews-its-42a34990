#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The line is a single line of at most 200 characters.

Deterministic: no input, no network, no randomness, no clock.
"""

import os
from pathlib import Path

LINE = "One star. He closed the bathroom door on me, so I screamed outside it for an hour, then walked away the second he opened it."

MAX_CHARS = 200


def main() -> None:
    # Validate the line before writing it: the gate only accepts UTF-8
    # text of 1 to 200 characters, not only white space, on a single line.
    line = LINE.strip()
    assert line, "review must not be blank"
    assert "\n" not in line and "\r" not in line, "review must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"review must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
