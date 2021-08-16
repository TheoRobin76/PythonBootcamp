import random

logo = """
  _____                   ________         _  __           __          
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_
"""


def guess_the_number():
    print(logo)
    print("Welcome to Guess The Number!")
    print("I am thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    select_difficulty = True
    while select_difficulty:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            lives = 10
            select_difficulty = False
        elif difficulty == "hard":
            lives = 5
            select_difficulty = False
        else:
            print("Please enter a valid entry")

    print(f"You have selected {difficulty} mode, giving you {lives} lives.")

    play = True
    while play:
        guess = int(input("Please guess a number: "))
        if lives == 1:
            print(f"You ran out of lives! You have lost Guess the number.\nThe number was {number}.")
            play = False
        elif guess < number:
            print("Too low!")
            lives -= 1
            print(f"Lives remaining: {lives}")
        elif guess > number:
            print("Too high!")
            lives -= 1
            print(f"Lives remaining: {lives}")
        elif guess == number:
            print(f"You guessed the number! The winning number was {number}.")
            play = False


guess_the_number()

play_again = True
while play_again:
    again = input("Would you like to play again? (y/n): ").lower()
    if again == "y":
        guess_the_number()
    elif again == "n":
        print("Thank you for playing.")
        play_again = False
    else:
        print("Please enter a valid entry.")




