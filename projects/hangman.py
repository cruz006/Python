import random

def generate_random_word():
    """Generates a random English word from a list."""

    words = ["apple", "banana", "cherry", "dragonfruit", "elderberry",  # Add more words here!
             "fig", "grape", "honeydew", "jackfruit", "kiwi"]

    random_index = random.randint(0, len(words) - 1)
    random_word = words[random_index]
    tries = len(random_word)

    return random_word, tries

def play_word_guessing_game():
    """Plays a word guessing game with the generated word."""

    random_word, tries = generate_random_word()
    guessed_letters = set()  # Keep track of guessed letters
    guessed_word = ["_"] * len(random_word)  # Initialize with underscores

    while tries > 0:
        print("The word:", " ".join(guessed_word))  # Display current guessed word
        guess = input("Guess a letter: ").lower()  # Convert input to lowercase for consistency

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)  # Add the guessed letter to the set

        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    guessed_word[i] = guess
        else:
            tries -= 1
            print("Incorrect guess. You have", tries, "tries remaining.")

        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", random_word)
            break

    if tries == 0:
        print("You ran out of tries. The word was:", random_word)

# Start the game
play_word_guessing_game()