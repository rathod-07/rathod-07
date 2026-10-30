import random

# Game settings.
WORDS = ["python", "code", "alpha", "script", "logic"]
MAX_ATTEMPTS = 6

# One drawing for each number of wrong guesses, from 0 through 6.
HANGMAN_STAGES = [
	r"""
  +---+
  |   |
	  |
	  |
	  |
=========""",
	r"""
  +---+
  |   |
  O   |
	  |
	  |
=========""",

	r"""
  +---+
  |   |
  O   |
  |   |
	  |
=========""",
	r"""
  +---+
  |   |
  O   |
 /|   |
	  |
=========""",
	r"""
  +---+
  |   |
  O   |
 /|\  |
	  |
=========""",
	r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
=========""",
	r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
=========""",
]


def get_secret_word():
	"""Pick a random word from the predefined word list."""
	# SystemRandom uses the operating system's secure random source.
	return random.SystemRandom().choice(WORDS)


def display_status(secret_word, guessed_letters, wrong_guesses):
	"""Display the hangman, word progress, attempts, and guessed letters."""
	progress = [
		letter if letter in guessed_letters else "_"
		for letter in secret_word
	]

	print("\n" + "=" * 40)
	print(HANGMAN_STAGES[wrong_guesses])
	print("Word progress:      " + " ".join(progress))
	print("Attempts left:      " + str(MAX_ATTEMPTS - wrong_guesses))
	print(
		"Guessed letters:    "
		+ (", ".join(guessed_letters) if guessed_letters else "None")
	)
	print("=" * 40)

	return "_" not in progress


def get_valid_guess(guessed_letters):
	"""Ask for a new single-letter guess and validate it."""
	while True:
		guess = input("\nGuess a letter: ").strip().lower()

		if len(guess) != 1 or not guess.isalpha():
			print(" Invalid input. Please enter a single letter.")
		elif guess in guessed_letters:
			print(" You already guessed '" + guess + "'. Try another letter.")
		else:
			return guess


def play_hangman():
	"""Run one complete round of the Hangman game."""
	secret_word = get_secret_word()
	guessed_letters = []
	wrong_guesses = 0

	print("=" * 40)
	print(" WELCOME TO HANGMAN!  ")
	print("=" * 40)

	while wrong_guesses < MAX_ATTEMPTS:
		# Show the current game state and stop if the word is complete.
		if display_status(secret_word, guessed_letters, wrong_guesses):
			print("\n Congratulations! You guessed the word: " + secret_word)
			return

		guess = get_valid_guess(guessed_letters)
		guessed_letters.append(guess)

		if guess in secret_word:
			print(" Great guess! '" + guess + "' is in the word.")
		else:
			wrong_guesses += 1
			print(" Incorrect! '" + guess + "' is not in the word.")

	# Show the final drawing and reveal the word after six incorrect guesses.
	print("\n" + "=" * 40)
	print(HANGMAN_STAGES[MAX_ATTEMPTS])
	print("Game over! The correct word was: " + secret_word)
	print("=" * 40)


if __name__ == "__main__":
	play_hangman()
