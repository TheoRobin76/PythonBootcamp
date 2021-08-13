import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Returns the sum of all of the cards in a list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)


def compare_score(player_score, comp_score):
    """Determines who wins based on the scores"""
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if comp_score == 0:
        print("Computer wins with blackjack!")
    elif player_score == comp_score:
        print("Draw!")
    elif user_score == 0:
        print("You win with blackjack!")
    elif user_score > 21:
        print("You went bust! Computer wins!")
    elif computer_score > 21:
        print("Computer went bust! You win!")
    elif user_score > computer_score:
        print("You win!")
    elif computer_score > user_score:
        print("Computer wins!")


def blackjack():
    global user_score, computer_score, user_cards, computer_cards
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    keep_playing = True
    while keep_playing:
        user_score = (calculate_score(user_cards))
        computer_score = (calculate_score(computer_cards))
        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            keep_playing = False

        else:
            twist = input("Would you like to draw another card? (y/n): ").lower()
            if twist == "y":
                user_cards.append(deal_card())
            else:
                break

    if user_score > 21:
        compare_score(user_score, computer_score)
    else:
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = (calculate_score(computer_cards))
        compare_score(user_score, computer_score)


blackjack()

another_round = True
while another_round:
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        blackjack()
    else:
        print("Thank you for playing.")
        another_round = False
