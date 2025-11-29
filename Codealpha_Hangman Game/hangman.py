# ================================================
#       HANGMAN GAME - TASK 1
#   Concepts: random, while loop, if-else, strings, lists
# ================================================

import random

# Predefined list of 5 words
WORDS = ["python", "computer", "keyboard", "hangman", "coding"]

# Hangman stages (6 incorrect guesses allowed)
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    GAME OVER!
    """
]

def choose_word():
    """Randomly pick a word from the list"""
    return random.choice(WORDS).upper()

def display_word(word, guessed_letters):
    """Show the word with unguessed letters as _"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    print("Welcome to HANGMAN!")
    print("Guess the word letter by letter. You have 6 lives!\n")

    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("The word has", len(word), "letters:")
    print(display_word(word, guessed_letters))
    print(HANGMAN_STAGES[incorrect_guesses])

    while incorrect_guesses < max_incorrect:
        guess = input("\nEnter a letter: ").upper().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        # Show current state
        print("\nWord:", display_word(word, guessed_letters))
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Lives left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You WIN!")
            print(f"The word was: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")
        print("Better luck next time!")

# Start the game
if __name__ == "__main__":
    while True:
        play_hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y", "yeah"]:
            print("Thanks for playing! Goodbye!")
            break
        print("\n" + "="*50 + "\n")