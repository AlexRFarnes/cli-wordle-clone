# wyrdl.py

from pathlib import Path
from random import choice
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))


def get_random_word(word_list):
    if words := [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]:
        return choice(words)
    else:
        console.print("No words of length 5 in the word list.", style="warning")
        raise SystemExit()


def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
        console.print("".join(styled_guess), justify="center")


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:video_game: {headline} :video_game:[/]\n")


def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"[bold white on red]Sorry, the word was {word}[/]")


def guess_word(previous_guesses):
    guess = console.input("\nGuess word: ").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)

    if len(guess) != 5:
        console.print("Your guess must be 5 letters.", style="warning")
        return guess_word(previous_guesses)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"Invalid letter: '{invalid}'. Please use English letters.", style="warning"
        )
        return guess_word(previous_guesses)

    return guess


def main():
    # Pre-process
    word_path = Path(__file__).parent / "wordlist.txt"
    word_list = word_path.read_text(encoding="utf-8").split("\n")
    word = get_random_word(word_list)
    print(word)
    guesses = ["_" * 5] * 6

    # Process (main loop)
    for idx in range(6):
        refresh_page(f"Guess {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = guess_word(guesses[:idx])

        if guesses[idx] == word:
            break

    # Post-process
    game_over(guesses, word, guessed_correctly=guesses[idx] == word)


if __name__ == "__main__":
    main()
