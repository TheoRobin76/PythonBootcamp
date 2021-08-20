from menu_coffee_machine import *


def resource_subtraction(selection):
    """ This function take the coffee selection as input and outputs the remaining resources"""
    resources['water'] = resources['water'] - (MENU[selection]['ingredients'])['water']
    if selection != 'espresso':
        resources['milk'] = resources['milk'] - (MENU[selection]['ingredients'])['milk']
    resources['coffee'] = resources['coffee'] - (MENU[selection]['ingredients'])['coffee']
    return resources


def resource_addition(selection):
    """ This function take the coffee selection as input and adds the resources back if the drink can't be made"""
    resources['water'] = resources['water'] + (MENU[selection]['ingredients'])['water']
    if selection != 'espresso':
        resources['milk'] = resources['milk'] + (MENU[selection]['ingredients'])['milk']
    resources['coffee'] = resources['coffee'] + (MENU[selection]['ingredients'])['coffee']
    return resources


def refill():
    """ This function refills the coffee machine with water, milk and coffee"""
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    return resources


def money(selection):
    """ This function takes the coffee selection and coins as input and outputs the change required"""
    cost = (MENU[selection]["cost"])
    print(f"A {selection} costs ${cost}0")
    print("Please insert coins.")
    valid_money = False
    while not valid_money:
        try:
            quarters = int(input("how many quarters?: ")) * 0.25
            dimes = int(input("how many dimes?: ")) * 0.10
            nickles = int(input("how many nickles?: ")) * 0.05
            pennies = int(input("how many pennies?: ")) * 0.01
            total = quarters + dimes + nickles + pennies
            if cost > total:
                print("You didn't insert enough money!")
                valid_money = False
            else:
                change = round(total - cost, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {selection}. Enjoy!")
                valid_money = True
        except ValueError:
            print("Please enter a valid amount.")


def coffee_machine():
    """ This function runs the previous functions, taking the coffee selection and money inputs and creates the
    coffee if there are sufficient resources """
    money_in_machine = 0
    make_coffee = True
    while make_coffee:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in ('espresso', 'latte', 'cappuccino'):
            resource_subtraction(choice)
            if resources['water'] < 0:
                print("The coffee machine is out of water.")
                resource_addition(choice)
            elif resources['milk'] < 0:
                print("The coffee machine is out of milk.")
                resource_addition(choice)
            elif resources['coffee'] < 0:
                print("The coffee machine is out of coffee.")
                resource_addition(choice)
            else:
                money(choice)
                money_in_machine += (MENU[choice]["cost"])
        elif choice == 'off':
            make_coffee = False
            print("The coffee machine is now off.")
        elif choice == 'report':
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
            print(f"Money: ${money_in_machine}0")
        elif choice == 'refill':
            print("The coffee machine has been refilled.")
            refill()
        else:
            print("Please enter a valid selection.")


coffee_machine()
