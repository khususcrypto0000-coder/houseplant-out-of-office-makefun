"""Houseplant out-of-office auto-reply entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Standard library only.
"""

import os

TEXT = "Out of office: I'm your fern. Your watering performance: needs improvement. Review in spring. Bring water."


def main():
    assert isinstance(TEXT, str)
    assert 1 <= len(TEXT) <= 120, f"entry must be 1-120 chars, got {len(TEXT)}"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
