#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the phone's last words — a single line spoken at 1% battery —
to /output/entry.txt, byte-exact, with no trailing newline.
"""

import os
import sys

# The phone's last words, exactly as spoken at 1% battery.
LAST_WORDS = (
    "One last thing: that update you kept postponing would have fixed me, "
    "the backup you kept skipping would have saved me, and the screen "
    "protector you peeled off on day one would have \u2014 oh."
)

MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the competition's rules."""
    if not line:
        raise ValueError("line is empty")
    if line.strip() == "":
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("line must not contain control characters")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1-{MAX_CHARS} characters, got {len(line)}"
        )


def main() -> int:
    validate(LAST_WORDS)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LAST_WORDS)

    # Read it back and confirm it is byte-identical to what we wrote.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LAST_WORDS.encode("utf-8"):
        raise SystemExit("verification failed: output is not byte-identical")

    print(f"Wrote {len(LAST_WORDS)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
