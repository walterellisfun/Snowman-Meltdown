import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
   ___
 /___\\
 (o o)
 ( : )
 ( : )
""",
    # Stage 1: Bottom part starts melting
    """
   ___
 /___\\
 (o o)
 ( : )
""",
    # Stage 2: Only the head remains
    """
   ___
 /___\\
 (o o)
""",
    # Stage 3: Snowman completely melted
    """
   ___
 /___\\
"""
]

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman and the word with underscores."""
    print(STAGES[mistakes])

    word_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_display += letter + " "
        else:
            word_display += "_ "
    print("Word:", word_display.strip())
    print("\n")


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")
    print(f"(Debug) Secret word: {secret_word}")  # Remove later

    # Show initial state
    display_game_state(mistakes, secret_word, guessed_letters)

    # Placeholder prompt
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    print(f"You guessed: {guess}")


if __name__ == "__main__":
    play_game()