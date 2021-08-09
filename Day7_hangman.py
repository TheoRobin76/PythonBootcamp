import random
from hangman_words_art import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
guessed_letters = []
display = list("_" * word_length)
print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You have already guessed {guess}!")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word and guess not in guessed_letters:
        print(f"{guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    guessed_letters.append(guess)
    print(stages[lives])
