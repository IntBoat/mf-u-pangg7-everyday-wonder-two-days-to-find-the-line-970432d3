#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "The lift doors opened on a stranger humming my favourite song, and for one floor the building felt like home."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
