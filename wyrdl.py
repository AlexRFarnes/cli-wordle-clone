# wyrdl.py

from pathlib import Path
from random import choice
from string import ascii_letters


def get_random_word(path_to_txt):
    wordlist = Path(__file__).parent / path_to_txt

    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]

    return choice(words)


def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print(f"Correct letter: {', '.join(correct_letters)}")
    print(f"Misplaced letter: {', '.join(misplaced_letters)}")
    print(f"Wrong letter: {', '.join(wrong_letters)}")


def game_over(word):
    print(f"The word was {word}")


def main():
    # Pre-process
    word = get_random_word("wordlist.txt")

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            print("Correct")
            break

    # Post-process
    else:
        game_over(word)


if __name__ == "__main__":
    main()
