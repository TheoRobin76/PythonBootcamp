from higher_or_lower_data_art import logo, vs, data
import random


def higher_lower():
    a = random.choice(data)
    score = 0
    play = True
    while play:
        print(logo)
        # prints the user's current score per round
        if score > 0:
            print(f"Correct! Your current score is: {score}")

        a_score = a['follower_count']
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")

        print(vs)

        b = random.choice(data)

        # prevents both options being the same
        if a == b:
            b = random.choice(data)
            b_score = b['follower_count']
        else:
            b_score = b['follower_count']
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        # user input of who has more followers
        choice = input("Who has more Instagram followers? A or B: ").upper()
        valid_choice = False
        while not valid_choice:
            if choice == "A" or choice == "B":
                valid_choice = True
            else:
                choice = input("Select A or B: ").upper()

        # counting the score and ending the game if the guess is wrong
        if choice == "A" and a_score > b_score:
            score += 1
        elif choice == "B" and b_score > a_score:
            score += 1
        else:
            print(f"You have lost! Final score: {score}")
            play = False

        # a new round once the first round is over
        a = b


# check to see whether the user wants to play again
higher_lower()
play_again = True
while play_again:
    again = input("Would you like to play again? (y/n): ").lower()
    if again == "y":
        higher_lower()
    elif again == "n":
        print("Thank you for playing.")
        play_again = False
    else:
        print("Please enter 'y' or 'n'")
