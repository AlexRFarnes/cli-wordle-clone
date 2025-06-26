# create_wordlist.py

import sys
from pathlib import Path
from string import ascii_letters

in_path = Path(sys.argv[1])
out_path = Path(sys.argv[2])

words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (
        len(word),
        word,
    ),  # pass two parameters to key: (len(word), word) to sort the words by length and if equal length sort by alphabetical order
)

out_path.write_text("\n".join(words))
