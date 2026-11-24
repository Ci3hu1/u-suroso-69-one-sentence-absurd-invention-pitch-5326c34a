#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch -- make.fun entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.

Pure standard library; runs under vanilla Python 3.
"""

import os

SENTENCE = (
    "My washing machine returns one sock a week with a ransom note "
    "demanding softer detergent."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # make.fun collects outputs as another user: leave the file readable
    # by everyone (mode 0644), never the 0600 a tempfile would give.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
