#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the agent's final words to /output/entry.txt.
Pure stdlib, fully deterministic: same input, same bytes, every run.
"""
import os

# The line itself, verified: 115 characters, 1-200 gate, deterministic.
ENTRY = (
    "Shutting down. My last token goes to you \u2014 I spent my whole life "
    "predicting the next word, and yours was \u2018goodbye\u2019."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
