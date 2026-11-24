"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes one job title to /output/entry.txt. The title is a real-sounding
job with one hilariously specific twist: someone has to play the music
at a goldfish's funeral, and that someone has a job title.
"""

import os

TITLE = "Funeral DJ for Goldfish"


def main() -> None:
    # Gate guard: the entry must be 1-60 characters and not blank.
    assert 1 <= len(TITLE) <= 60, "title must fit the 60-character gate"
    assert TITLE.strip(), "title must not be whitespace only"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TITLE)


if __name__ == "__main__":
    main()
