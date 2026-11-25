"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (117 characters) about the best advice the writer
ever received to /output/entry.txt, as the competition's gate requires.
Pure Python standard library, no network, no input files.
"""

import os

SENTENCE = (
    "Before my first shift, my father said, 'Be the worker they'd miss "
    "on your day off, not the one they're glad is gone.'"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
