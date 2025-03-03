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

