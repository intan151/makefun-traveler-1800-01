#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun bounty
u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.

Writes one sentence (<=200 chars) explaining the modern internet
to a traveler from 1800, using only things a person from 1800
already knows — a road, a post office, a library — to
/output/entry.txt. Stdlib only.
"""
import os

SENTENCE = "Picture a road joining every library and post office on earth, so a letter sent from your desk is answered before the ink dries."

def main():
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert "\n" not in SENTENCE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
