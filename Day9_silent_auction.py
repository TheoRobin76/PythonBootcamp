from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def make_bid(name, bid):
    bid_info = {"name": name, "bid": bid}
    bidders.append(bid_info)


bidders = []
print(logo)
auction = True
while auction:
    name = input("Please enter your name:\n")
    bid = int(input("please enter your bid:\n$"))
    make_bid(name, bid)
    more_bidders = input("Are there any other potential bidders?\ny/n: ").lower()
    # this clears the console on replit.com, not in pycharm
    clear()
    # this obscures the previous bid from the current bidder in pycharm (I will find a better way)
    print("                                                                                               " * 100)
    bidders = sorted(bidders, key=lambda k: k['bid'])
    if more_bidders == "n":
        auction = False
        winner = bidders[-1]
        print(f"Congratulations {winner['name']}, you have won the auction with a bid of ${winner['bid']}.")
