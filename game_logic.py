import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    if mistakes < len(STAGES):
        print(STAGES[mistakes])
    else:
        print(STAGES[-1])  # Show melted state if out of bounds

    word_display = []
    for letter in secret_word:
        if letter in guessed_letters:
            word_display.append(letter)
        else:
            word_display.append("_")

    print("Word: " + " ".join(word_display))
    print()


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check for win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You saved the snowman. The word was '{secret_word}'.")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print(f"Sorry, '{guess}' is not in the word.")
            mistakes += 1

    # If loop ends, user lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"The snowman has melted! The word was '{secret_word}'.")