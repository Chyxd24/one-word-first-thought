"""One Word, First Thought — the first word that arrives when no topic is named.

Writes a single word to /output/entry.txt. Stdlib only, no network, deterministic.
Revision: word kept, rewritten as a flat authored script.
"""
import os

# Liminal: the threshold state of being neither here nor there — exactly where
# an unprompted mind starts.
WORD = "Liminal"

assert 1 <= len(WORD) <= 200, len(WORD)
assert " " not in WORD, "must be exactly one word"

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as fh:
    fh.write(WORD)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == WORD, f"readback mismatch: {landed!r}"
print(f"wrote {landed!r} to {path}")