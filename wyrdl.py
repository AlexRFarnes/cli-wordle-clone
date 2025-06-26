# wyrdl.py

WORD = "SNAKE"

for guess_num in range(1, 7):
    guess = input("Guess a word: ").upper()

    if guess == WORD:
        print("Correct")
        break

    correct_letters = {
        letter for letter, correct in zip(guess, WORD) if letter == correct
    }
    misplaced_letters = set(guess) & set(WORD) - correct_letters
    wrong_letters = set(guess) - set(WORD)

    print(f"Correct letter: {', '.join(correct_letters)}")
    print(f"Misplaced letter: {', '.join(misplaced_letters)}")
    print(f"Wrong letter: {', '.join(wrong_letters)}")
