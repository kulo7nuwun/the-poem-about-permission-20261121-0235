#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is about the power to ask and to be given: asking is not
the empty hand, it is the act that lets giving happen.
Deterministic: the same poem, byte for byte, on every run.
"""

from pathlib import Path

POEM = """Asking is not the empty hand.
It is the door, unlatched, swung wide —
an invitation, spoken, not begged:
here is my need, here is the key.
Take it. The power to give
was waiting all along
for someone brave enough to ask."""

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Return the poem, or raise if it cannot be a valid entry."""
    text = text.strip()
    if not text:
        raise ValueError("poem must not be empty")
    if len(text) > 280:
        raise ValueError(f"poem is {len(text)} chars, over the 280 limit")
    return text


def main() -> None:
    text = validate(POEM)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Round-trip check: what lands on disk is exactly the poem.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
