def lookItems(player):
     try:
        print("\nYou see the following items")
        for i,item in enumerate(player.current_pos.item,1):
            print(f" {i}.{item} {"Drink water to get hydrated." if item == 'water' else ""}")
            print(f" {len(player.current_pos.item)+1}.back (type 'back')")
            item_choice = input("\nChoose an item to pick up:")
            if item_choice == 'back':
                return;
            if 0 <= int(item_choice) <= len(player.current_pos.item):
                item = player.current_pos.item[int(item_choice) - 1]
                player.add_to_inventory(item)
            else:       
                print("Invalid choice. Try again.")
     except ValueError:
        print("Invalid input. Please enter a number.")
