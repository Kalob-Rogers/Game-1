#Kalob Rogers
#Feb 16 2024
#This should call the functions "purchase_item()" and "new_random_monster()"
#three times with three different inputs
#Updated on feb 23 2024 for the next assignment
import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """Attempts to purchase a specified quantity of an item and returns the quantity purchased and remaining money."""
    total_cost = itemPrice * quantityToPurchase
    if startingMoney >= total_cost:
        return quantityToPurchase, startingMoney - total_cost
    else:
        max_items = int(startingMoney // itemPrice)  # How many items can be purchased
        return max_items, startingMoney - (max_items * itemPrice)

def new_random_monster():
    """Generates a random monster with properties."""
    monster_names = ["Goblin", "Orc", "Dragon"]
    name = random.choice(monster_names)
    description = f"This is a {name}. It looks dangerous!"
    
    if name == "Goblin":
        health = random.randint(20, 50)
        power = random.randint(5, 10)
        money = round(random.uniform(5.0, 20.0), 2)
    elif name == "Orc":
        health = random.randint(50, 100)
        power = random.randint(10, 20)
        money = round(random.uniform(10.0, 40.0), 2)
    else:  # Dragon
        health = random.randint(100, 200)
        power = random.randint(20, 50)
        money = round(random.uniform(50.0, 200.0), 2)
    
    return {'name': name, 'description': description, 'health': health, 'power': power, 'money': money}

def print_welcome(name, width=20):
    """Prints a centered welcome message within a specified width."""
    print(f"{'Hello, ' + name + '!':^{width}}")

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Prints a formatted shop menu with two items and their prices, aligned properly."""
    border = "/" + "-" * 22 + "\\"
    item_format = "| {:12} ${:>6.2f} |"
    print(border)
    print(item_format.format(item1Name, item1Price))
    print(item_format.format(item2Name, item2Price))
    print("\\" + "-" * 22 + "/")

# Testing purchase_item function
print(purchase_item(1.23, 10, 3))  # Expected: (3, 6.31)
print(purchase_item(1.23, 2.01, 3))  # Expected: (1, 0.78)
print(purchase_item(3.41, 21.12))  # Expected: (1, 17.71)

# Testing new_random_monster function
print(new_random_monster())  # Should print a random monster with health, power, and money
print(new_random_monster())
print(new_random_monster())

# Testing print_welcome function
print_welcome("Jeff")  # Expected: '    Hello, Jeff!    '
print_welcome("Audrey")  # Expected: '   Hello, Audrey!   '
print_welcome("Sam")  # Expected: '     Hello, Sam!     '

# Testing print_shop_menu function
print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
print_shop_menu("Milk", 2.5, "Bread", 3.75)

# Here  is the new game functions 
'''
Kalob Rogers
Due date: March 09 2025
Im a little confused on if needed to update the gamefunctions on my computer or on
github, so i wrote this "copied and pasted then edited from gamefunctions.py"
separettly that way i wont lose gamefunctions if i was to edit it. Ill commit it
to gamefunctions on github without changing the original wich probobly will
make the whole code stop working but im not sure what else to do.
'''

import random

def print_welcome(name: str, width: int = 20) -> None:
   Hello, Jeff!    '
_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:

    border = "/" + "-" * 22 + "\\"
    item_format = "| {:12} ${:>6.2f} |"
    print(border)
    print(item_format.format(item1Name, item1Price))
    print(item_format.format(item2Name, item2Price))
    print("\\" + "-" * 22 + "/")


def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple:

    total_cost = itemPrice * quantityToPurchase
    if startingMoney >= total_cost:
        return quantityToPurchase, startingMoney - total_cost
    else:
        max_items = int(startingMoney // itemPrice)  # How many items can be purchased
        return max_items, startingMoney - (max_items * itemPrice)


def new_random_monster() -> dict:

    monster_names = ["Goblin", "Orc", "Dragon"]
    name = random.choice(monster_names)
    description = f"This is a {name}. It looks dangerous!"
    
    if name == "Goblin":
        health = random.randint(20, 50)
        power = random.randint(5, 10)
        money = round(random.uniform(5.0, 20.0), 2)
    elif name == "Orc":
        health = random.randint(50, 100)
        power = random.randint(10, 20)
        money = round(random.uniform(10.0, 40.0), 2)
    else:  # Dragon
        health = random.randint(100, 200)
        power = random.randint(20, 50)
        money = round(random.uniform(50.0, 200.0), 2)
    
    return {'name': name, 'description': description, 'health': health, 'power': power, 'money': money}


def test_functions():

    print("Testing print_welcome:")
    print_welcome("Jeff")
    
    print("\nTesting print_shop_menu:")
    print_shop_menu("Apple", 2.5, "Banana", 1.2)

    print("\nTesting purchase_item:")
    print(purchase_item(1.23, 10, 3))  # Expected: (3, 6.31)
    print(purchase_item(1.23, 2.01, 3))  # Expected: (1, 0.78)
    print(purchase_item(3.41, 21.12))  # Expected: (6, remaining money)

    print("\nTesting new_random_monster:")
    print(new_random_monster())
    print(new_random_monster())
    print(new_random_monster())


if __name__ == "__main__":
    test_functions()
    
# Here is the game.py

'''
Game.py
Kalob Rogers
Due date March 09 2025
This imports the new gamefunctions that i wrote.  It will ask for the players
name then displays a welcome message, shows a shop screen then does an
item purchase and monster generation
'''

import gamefunctions

def main():
   
    # Get player's name
    player_name = input("Enter your name: ")
    
    # Print welcome message
    gamefunctions.print_welcome(player_name)

    # Display a shop menu
    print("\nWelcome to the shop!")
    gamefunctions.print_shop_menu("Sword", 50, "Shield", 40)

    # Simulate a purchase
    money = 100  # Starting money
    print("\nYou have $100.")
    item_purchased, remaining_money = gamefunctions.purchase_item(50, money, 1)
    print(f"You bought {item_purchased} item(s). You now have ${remaining_money:.2f} left.")

    # Generate a random monster
    print("\nA wild monster appears!")
    monster = gamefunctions.new_random_monster()
    print(f"{monster['description']} It has {monster['health']} HP and {monster['power']} power.")

if __name__ == "__main__":
    main()

