'''
Game.py
Kalob Rogers
Due date March 09 2025
This imports the new gamefunctions that i wrote.  It will ask for the players
name then displays a welcome message, shows a shop screen then does an
item purchase and monster generation
'''

import gamefunctions

import json  # To enable saving/loading functionality

def save_game(player_name, player_hp, player_gold, inventory, filename):
    """Saves the game state to a JSON file."""
    game_data = {
        'player_name': player_name,
        'player_hp': player_hp,
        'player_gold': player_gold,
        'inventory': inventory
    }
    with open(filename, 'w') as file:
        json.dump(game_data, file)
    print(f"Game saved to {filename}.")

def load_game(filename):
    """Loads the game state from a JSON file."""
    try:
        with open(filename, 'r') as file:
            game_data = json.load(file)
            return game_data
    except FileNotFoundError:
        print("Save file not found!")
        return None

def main():
    # Get player's name
    player_name = input("Enter your name: ")

    # Print welcome message
    gamefunctions.print_welcome(player_name)

    # Initialize player stats
    player_hp = 30  # Starting HP
    player_gold = 100  # Starting money
    inventory = []  # Starting with an empty inventory

    # Game loop
    while True:
        # Ask the player what they want to do
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        
        action = input("What would you like to do?\n1) Leave town (Fight Monster)\n2) Sleep (Restore HP for 5 Gold)\n3) Go to shop\n4) Save and Quit\n5) Load Game\nEnter choice: ")

        if action == '1':  # Fight monster
            # Generate a random monster
            print("\nA wild monster appears!")
            monster = gamefunctions.new_random_monster()
            print(f"{monster['description']} It has {monster['health']} HP and {monster['power']} power.")
            
            # Start combat loop
            while True:
                print(f"\nYour HP: {player_hp}, Monster HP: {monster['health']}")
                combat_action = input("Choose an action:\n1) Attack\n2) Run Away\n> ")

                if combat_action == '1':  # Attack
                    player_attack = 8  # Simplified attack power for now
                    monster['health'] -= player_attack
                    print(f"You hit the {monster['name']} for {player_attack} damage!")

                    # Monster attacks back
                    player_hp -= monster['power']
                    print(f"The {monster['name']} hits you for {monster['power']} damage!")
                    
                    if player_hp <= 0:
                        print(f"\nThe {monster['name']} defeated you! Game over.")
                        return  # Game over
                    elif monster['health'] <= 0:
                        print(f"You defeated the {monster['name']}!")
                        break  # Monster defeated, break out of combat

                elif combat_action == '2':  # Run away
                    print("\nYou run away safely!")
                    break  # Exit combat and return to town

                else:
                    print("\nInvalid choice. Please choose 1 or 2.")
            
        elif action == '2':  # Sleep to restore HP
            if player_gold >= 5:
                player_gold -= 5
                player_hp = 30  # Restore full HP
                print("\nYou rested and restored your HP!")
            else:
                print("\nYou don't have enough gold to sleep!")

        elif action == '3':  # Go to shop
            print("\nWelcome to the shop!")
            gamefunctions.print_shop_menu("Sword", 50, "Shield", 40)
            
            # Ask player if they want to buy something
            buy_action = input("\nWould you like to buy an item? (yes/no): ").lower()
            
            if buy_action == 'yes':
                # Allow the player to choose what to buy
                choice = input("Which item would you like to buy?\n1. Sword\n2. Shield\n> ")
                
                if choice == '1':  # Sword
                    item_purchased, remaining_money = gamefunctions.purchase_item(50, player_gold, 1)
                    if item_purchased:
                        print(f"You bought a Sword! You now have ${remaining_money:.2f} left.")
                        player_gold = remaining_money  # Update player's gold
                    else:
                        print("You don't have enough gold for that item.")
                elif choice == '2':  # Shield
                    item_purchased, remaining_money = gamefunctions.purchase_item(40, player_gold, 1)
                    if item_purchased:
                        print(f"You bought a Shield! You now have ${remaining_money:.2f} left.")
                        player_gold = remaining_money  # Update player's gold
                    else:
                        print("You don't have enough gold for that item.")
                else:
                    print("\nInvalid choice. Please choose 1 or 2.")
            else:
                print("\nYou decided not to buy anything.")

        elif action == '4':  # Save and Quit
            filename = input("Enter the filename to save your game: ")
            save_game(player_name, player_hp, player_gold, inventory, filename)
            print("\nExiting the game. Goodbye!")
            return  # Exit the game entirely.

        elif action == '5':  # Load Game
            filename = input("Enter the filename to load your game: ")
            game_data = load_game(filename)
            if game_data:
                player_name = game_data['player_name']
                player_hp = game_data['player_hp']
                player_gold = game_data['player_gold']
                inventory = game_data['inventory']
                print(f"\nGame loaded successfully. Welcome back, {player_name}!")
            else:
                print("Failed to load game.")

        else:
            print("\nInvalid option, please choose again.")

if __name__ == "__main__":
    main()

'''
Kalob Rogers
April 3 2025
I met someone in my trigonometry class is quite good at coding in python
and he sat down with me and we completly revamped my code and this is the result
all bugs should be fixed and the game should work as intended I also added saving
and loading into the game
'''
