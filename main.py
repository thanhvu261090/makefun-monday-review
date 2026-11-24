"""Monday, Reviewed in One Line — make.fun entry.

Writes the funniest one-line review of my own Monday to /output/entry.txt.
The entry is a single line, under 200 characters, nothing else.
"""

import os
import sys

ENTRY = (
    "Monday review: one star. My alarm snoozed itself, my inbox booked a "
    "meeting about the meeting, and my coffee filed for divorce."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def gate_check(text):
    """Mirror the platform gate: UTF-8, 1-200 chars, not only whitespace,
    a single line."""
    if not isinstance(text, str):
        return False, "entry is not a string"
    if not text.strip():
        return False, "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return False, "entry is over 200 characters"
    if "\n" in text or "\r" in text:
        return False, "entry is more than one line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "entry is not valid UTF-8"
    return True, "ok"


def main():
    ok, reason = gate_check(ENTRY)
    if not ok:
        print(f"gate failed: {reason}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be byte-identical to ENTRY.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("round-trip mismatch: file differs from entry", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
