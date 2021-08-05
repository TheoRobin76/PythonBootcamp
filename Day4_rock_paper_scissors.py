import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
num_choices = len(choices)

comp = random.randint(0, 2)
comp_turn = choices[comp]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while player >= 3 or player < 0:
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

player_turn = choices[player]
print(player_turn)
print(f"Computer chose:\n{comp_turn}")


if player_turn == rock and comp_turn == rock:
    print("Draw!")
elif player_turn == rock and comp_turn == paper:
    print("Computer Wins!")
elif player_turn == rock and comp_turn == scissors:
    print("Player Wins!")
elif player_turn == paper and comp_turn == rock:
    print("Player Wins!")
elif player_turn == paper and comp_turn == paper:
    print("Draw!")
elif player_turn == paper and comp_turn == scissors:
    print("Computer Wins!")
elif player_turn == scissors and comp_turn == rock:
    print("Computer Wins!")
elif player_turn == scissors and comp_turn == paper:
    print("Player Wins!")
elif player_turn == scissors and comp_turn == scissors:
    print("Draw!")
