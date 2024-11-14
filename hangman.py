import random

def hangman():
    # Word list for the game
    words = ["algorithm", "function", "variable", "compile", "iterate",
             "recursion", "binary", "array", "syntax", "pointer"]

    # Choose a random word from the list
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts_left = len("HANGMAN")  # 7 attempts, one for each letter in "HANGMAN"
    guessed_letters = set()

    print("HANGMAN")
    pointer_position = 0
    print(" " * pointer_position + "^")

    while attempts_left > 0 and ''.join(guessed_word) != word:
        print("\nCurrent word:", ' '.join(guessed_word))
        print("Guessed letters:", ', '.join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            pointer_position += 1
            print("Incorrect guess!")
            print("HANGMAN")
            print(" " * pointer_position + "^")

        # Check if the player has won
        if ''.join(guessed_word) == word:
            print("\nPhew… you are saved!")
            break
    else:
        if attempts_left == 0:
            print("\nYou are hanged!")

    print("The word was:", word)

def main():
    while True:
        hangman()
        replay = input("\nPlay again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


    
