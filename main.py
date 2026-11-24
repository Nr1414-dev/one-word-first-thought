#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Writes exactly one word to /output/entry.txt: "cleave".

Why this word: it means its own exact opposite — to split apart
and to cling together — so it is surprising, vivid, and carries the
maximum double meaning a single word can hold. Six letters, six
bytes, lowercase, no punctuation.

Gate: /output/entry.txt must be UTF-8 text of 1 to 24 characters,
not only white space.
"""

import os

WORD = "cleave"


def validate(word: str) -> None:
    """Enforce the gate before writing: exactly one word, 1-24 chars."""
    if not word or len(word) > 24:
        raise ValueError("word must be 1-24 characters")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly with open() + explicit chmod 0644. NEVER use
    # tempfile.mkstemp here: mkstemp creates mode 0600 and the
    # grader (uid 65534) cannot read the file (proven 24 Nov 2026,
    # Coffee or Tea round 1 rejected on run_completes).
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
