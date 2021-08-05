print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("You approach a sinister crossroads, do you turn left or right? ").lower()
if direction == "left":
    print(f"Unfortunately you turned {direction}, tripped on some loose gravel and fell down a well. Game over.")
elif direction == "right":
    decision = input(
        f"You turn {direction}, wandering across a large open field, until you reach an abandoned pier. Will you wait or swim? ").lower()
    if decision == "swim":
        print(
            f"Unfortunately deciding to {decision} was the last decision you ever made. You are eaten by school of carp. Game over.")
    elif decision == "wait":
        final = input(
            f"Deciding to {decision} was a wise and brave choice, a sea turtle appears and ferries you across the lake to an old mansion. You enter and are greeted with three doors. Will you go through the blue, the red or the yellow door? ").lower()
        if final == "blue":
            print(
                f"You open the {final} door, the room is filled with loose gravel and a well. You trip on the loose gravel and fall down the well. Game over.")
        elif final == "red":
            print(
                f"You open the {final} door, the room is filled with a school of carp who proceed to eat you. Game over.")
        elif final == "yellow":
            print(
                f"You open the {final} door, the room is filled with W.H.Smith vouchers. Congratulations! You have found the treasure.")
