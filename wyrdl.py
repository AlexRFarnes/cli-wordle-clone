# wyrdl.py

from pathlib import Path
from random import choice

WORDLIST = Path("wordlist.txt")

words = [
    word.upper() for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]

word = choice(words)

for guess_num in range(1, 7):
    guess = input("Guess a word: ").upper()

    if guess == word:
        print("Correct")
        break

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print(f"Correct letter: {', '.join(correct_letters)}")
    print(f"Misplaced letter: {', '.join(misplaced_letters)}")
    print(f"Wrong letter: {', '.join(wrong_letters)}")

else:
    print(f"The word was {word}")
