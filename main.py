#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line (make.fun).

Writes the entry -- one sentence on a small moment of wonder in
everyday life -- to /output/entry.txt, where the sealed scorer reads it.
Single sentence, no trailing newline.
"""

import os

TEXT = "The lift doors opened on a stranger humming my grandmother's song, and for three floors the whole building felt like a house I had once lived in."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
