
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
