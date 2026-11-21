"""Make the AI judge feel brave.

A small program that writes one short text to /output/entry.txt.
The text is a quiet, first-person moment: hands steadying over a
kettle, then a door opened onto a street that smells like rain.
It shows courage instead of instructing it, and it slows the
reader down sentence by sentence.
"""

import os

TEXT = (
    "I put the kettle on and watched the steam rise, slow as morning. "
    "My hands had stopped shaking by the second cup. "
    "The door was still there, waiting, not rushing me. "
    "I opened it, and the street smelled like rain."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
