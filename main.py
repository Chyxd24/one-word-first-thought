"""One Word, First Thought — the first word that arrives when no topic is named.

Scorer wants a single word in /output/entry.txt. I reach for "liminal": the
threshold state of being neither here nor there, which is exactly where an
unprompted mind starts.
"""
import pathlib


def entry_word() -> str:
    return "Liminal"


def main() -> None:
    word = entry_word().strip()
    assert 1 <= len(word) <= 200, len(word)
    assert " " not in word, "must be exactly one word"
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(word + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
