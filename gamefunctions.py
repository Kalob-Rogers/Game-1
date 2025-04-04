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
    


'''
Kalob Rogers
Due date March 23 2025
Once again i wrote this in python and im simply copying and pasting it here
that way i have multiple files. I understand that takes up alot of space but
im comfortable doing it that way while i try to understand github and how 
it fundementally works
'''


import random
import gamefunctions

# Initialize player stats
player_hp = 30
player_gold = 10

def fight_monster():
    """Handles the fighting loop with a randomly generated monster."""
    global player_hp, player_gold

    monster = gamefunctions.new_random_monster()
    print(f"\nA {monster['name']} appears! {monster['description']}")
    print(f"It has {monster['health']} HP and {monster['power']} power.\n")

    while monster['health'] > 0 and player_hp > 0:
        print(f"Your HP: {player_hp}, Monster HP: {monster['health']}")
        print("1) Attack")
        print("2) Run Away")

        choice = input("Choose an action: ")

        if choice == "1":
            damage_to_monster = random.randint(5, 10)
            monster['health'] -= damage_to_monster
            print(f"You hit the {monster['name']} for {damage_to_monster} damage!")

            if monster['health'] > 0:
                damage_to_player = monster['power']
                player_hp -= damage_to_player
                print(f"The {monster['name']} hits you for {damage_to_player} damage!")

            if player_hp <= 0:
                print("You have been defeated! Game Over.")
                exit()

            if monster['health'] <= 0:
                print(f"You defeated the {monster['name']} and earned {monster['money']} gold!")
                player_gold += monster['money']
                break  # Exit fight loop after winning

        elif choice == "2":
            print("You run away safely!")
            break  # Exit fight loop

        else:
            print("Invalid choice. Try again.")

def rest():
    """Restores HP in exchange for gold."""
    global player_hp, player_gold
    cost = 5

    if player_gold >= cost:
        player_hp = 30  # Restore full HP
        player_gold -= cost
        print("You rested and restored your HP!")
    else:
        print("Not enough gold to rest.")

def main():
    """Main game loop."""
    global player_hp, player_gold

    player_name = input("Enter your name: ")
    gamefunctions.print_welcome(player_name)

    while True:
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            fight_monster()
        elif choice == "2":
            rest()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
'''
Kalob Rogers
Due date March 30 2025
This code allows for item purchasing, combat items and shop interface
also ive had issue witht game.py over the last two assignments but i
belive ive fixed that problem
'''
'''
This is inventory 
'''
# Initialize the inventory
inventory = []

def purchase_item(item, quantity, player_gold):
    """Purchase an item and add it to the player's inventory."""
    item_price = item['price']
    total_cost = item_price * quantity
    if player_gold >= total_cost:
        player_gold -= total_cost
        # Add item(s) to the inventory
        for _ in range(quantity):
            inventory.append(item)
        print(f"Purchased {quantity} {item['name']}(s).")
    else:
        print("Not enough gold!")
    return player_gold

def show_inventory():
    """Display the player's inventory."""
    if inventory:
        print("Your Inventory:")
        for idx, item in enumerate(inventory, start=1):
            print(f"{idx}. {item['name']} ({item['type']})")
    else:
        print("Your inventory is empty!")

def equip_item(item_name):
    """Equip an item from the inventory."""
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            print(f"You equipped the {item_name}.")
            return item
    print(f"No item named {item_name} found.")
    return None

''' 
This is combat
'''
def fight_monster():
    global player_hp, player_gold
    monster = gamefunctions.new_random_monster()

    # Check if the player has a sword in inventory
    sword = None
    for item in inventory:
        if item['type'] == "weapon":
            sword = item
            break

    if sword:
        print(f"You equipped the sword! It has {sword['currentDurability']} uses left.")
    
    print(f"A wild {monster['name']} appears!")
    while monster['health'] > 0 and player_hp > 0:
        print(f"Your HP: {player_hp}, Monster HP: {monster['health']}")
        print("1) Attack")
        print("2) Run Away")

        choice = input("Choose an action: ")

        if choice == "1":
            if sword:
                # Attack with sword and decrease durability
                damage = random.randint(5, 10)
                monster['health'] -= damage
                sword['currentDurability'] -= 1
                print(f"You hit the monster for {damage} damage with your sword!")

                if sword['currentDurability'] <= 0:
                    print("Your sword is broken and cannot be used anymore.")
                    sword = None

            else:
                print("You have no weapon equipped!")

            if monster['health'] > 0:
                # Monster attacks back
                monster_damage = monster['power']
                player_hp -= monster_damage
                print(f"The monster hits you for {monster_damage} damage!")

            if player_hp <= 0:
                print("You have been defeated!")
                break
            elif monster['health'] <= 0:
                print(f"You defeated the monster! You earned {monster['money']} gold!")
                player_gold += monster['money']
                break

        elif choice == "2":
            print("You run away!")
            break
        else:
            print("Invalid choice.")
'''
this is the store interface
'''

def main():
    player_name = input("Enter your name: ")
    gamefunctions.print_welcome(player_name)

    player_gold = 100  # Starting money

    # Show the shop menu
    gamefunctions.print_shop_menu("Sword", 50, "Shield", 40)

    # Purchase a sword
    player_gold = purchase_item(sword, 1, player_gold)
    show_inventory()

    # Equip the sword
    equip_item("Sword")

    # Start fighting monsters
    while True:
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        print("What would you like to do?")
        print("1) Fight Monster")
        print("2) Rest (Restore HP)")
        print("3) Quit")

        choice = input("Enter choice: ")
        if choice == "1":
            fight_monster()
        elif choice == "2":
            rest()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

'''
Kalob Rogers
Due date April 6 2025
This code should add saving the game aswell as loading the game
'''
import json

def save_game(filename, player_name, player_hp, player_gold, inventory):
    """Saves the game state to a JSON file."""
    game_data = {
        'player_name': player_name,
        'player_hp': player_hp,
        'player_gold': player_gold,
        'inventory': inventory
    }
    
    with open(filename, 'w') as f:
        json.dump(game_data, f)
    
    print(f"Game saved to {filename}.")

def load_game(filename):
    """Loads the game state from a JSON file."""
    try:
        with open(filename, 'r') as f:
            game_data = json.load(f)
        return game_data
    except FileNotFoundError:
        print(f"No save file found with the name {filename}. Starting a new game.")
        return None
import gamefunctions
import json

# Add a save game feature
def save_game(filename, player_name, player_hp, player_gold, inventory):
    """Saves the game state to a JSON file."""
    game_data = {
        'player_name': player_name,
        'player_hp': player_hp,
        'player_gold': player_gold,
        'inventory': inventory
    }
    
    with open(filename, 'w') as f:
        json.dump(game_data, f)
    
    print(f"Game saved to {filename}.")

def load_game(filename):
    """Loads the game state from a JSON file."""
    try:
        with open(filename, 'r') as f:
            game_data = json.load(f)
        return game_data
    except FileNotFoundError:
        print(f"No save file found with the name {filename}. Starting a new game.")
        return None


def main():
    # Prompt user to either start a new game or load a saved game
    print("Welcome to the Adventure Game!")
    choice = input("Would you like to (N)ew game or (L)oad a saved game? ").lower()

    if choice == 'l':
        filename = input("Enter the filename to load: ")
        game_data = load_game(filename)
        if game_data:
            player_name = game_data['player_name']
            player_hp = game_data['player_hp']
            player_gold = game_data['player_gold']
            inventory = game_data['inventory']
        else:
            return  # Exit the game if loading fails
    else:
        player_name = input("Enter your name: ")
        player_hp = 30  # Starting HP
        player_gold = 100  # Starting money
        inventory = []  # Empty inventory

    gamefunctions.print_welcome(player_name)

    while True:
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Save and Quit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            fight_monster()
        elif choice == "2":
            rest()
        elif choice == "3":
            save_choice = input("Are you sure you want to save and quit? (Y/N): ").lower()
            if save_choice == 'y':
                filename = input("Enter the filename to save: ")
                save_game(filename, player_name, player_hp, player_gold, inventory)
                print("Game saved. Exiting...")
                break  # Exit the game
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
def fight_monster():
    global player_hp, player_gold, inventory
    monster = gamefunctions.new_random_monster()

    # Check if the player has a sword in inventory
    sword = None
    for item in inventory:
        if item['type'] == "weapon":
            sword = item
            break

    if sword:
        print(f"You equipped the sword! It has {sword['currentDurability']} uses left.")
    
    print(f"A wild {monster['name']} appears!")
    while monster['health'] > 0 and player_hp > 0:
        print(f"Your HP: {player_hp}, Monster HP: {monster['health']}")
        print("1) Attack")
        print("2) Run Away")

        choice = input("Choose an action: ")

        if choice == "1":
            if sword:
                # Attack with sword and decrease durability
                damage = random.randint(5, 10)
                monster['health'] -= damage
                sword['currentDurability'] -= 1
                print(f"You hit the monster for {damage} damage with your sword!")

                if sword['currentDurability'] <= 0:
                    print("Your sword is broken and cannot be used anymore.")
                    sword = None

            else:
                print("You have no weapon equipped!")

            if monster['health'] > 0:
                # Monster attacks back
                monster_damage = monster['power']
                player_hp -= monster_damage
                print(f"The monster hits you for {monster_damage} damage!")

            if player_hp <= 0:
                print("You have been defeated!")
                break
            elif monster['health'] <= 0:
                print(f"You defeated the monster! You earned {monster['money']} gold!")
                player_gold += monster['money']
                break
        elif choice == "2":
            print("You run away!")
            break
        else:
            print("Invalid choice.")

