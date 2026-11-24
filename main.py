"""The Worst App Idea Ever Pitched.

Writes the entry: one sentence pitching the worst, most useless app
imaginable. The pitch is PlantObit, an app that predicts which of
your houseplants will die first, pre-books its funeral, and emails
the eulogy to your surviving plants.

Why this pitch: it names a specific product and a specific useless
function, it sounds like a founder who means every word, and the
uselessness comes from a perfect mismatch — plants do not read email
and do not grieve — rather than from shock value.
"""

import os

# The gate counts characters, not bytes, and allows at most 240.
MAX_CHARS = 240

ENTRY = (
    "PlantObit uses AI to predict which of your houseplants will die "
    "first, then pre-books its funeral and emails the eulogy to your "
    "surviving plants, so busy plant parents never have to grieve alone."
)


def main() -> None:
    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError("entry must be 1-240 characters")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise ValueError("entry must be a single sentence with no surrounding whitespace")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
