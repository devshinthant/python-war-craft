def displayMenu(pos_name):
    print("\nWhat would you like to do?")
    print("1. Move to another position")
    print("2. Shop an item") if pos_name == 'Shop' else print("2. Look for an item")
    print("3. Check your bag")
    print("4. Combine items")
    print("5. Check body hydration")
    print("6. Check Weapons")
    print("7. Exit the game")

