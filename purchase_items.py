shop_items = ['sword','cross_guard','helmet']

def purchaseItems(player):
    try:
        print('\nWhat would you like to buy?')
        for i, item in enumerate(shop_items, 1):
            print(f'{i}. Buy {item}')
        print(f'{len(shop_items) + 1}. Back')
        
        combineItem = int(input('\nEnter your choice: '))
        
        if combineItem == 1:
            if 'steel' in player.inventory and 'leather' in player.inventory:
                player.equip_weapons('sword')
                player.inventory.remove('steel') 
                player.inventory.remove('leather') 
                print("You bought a Sword!")
            else:
                print('\nYou need steel and leather to buy a Sword.')
        
        elif combineItem == 2:
            if 'steel' in player.inventory:
                player.inventory.remove('steel') 
                player.equip_weapons('cross-guard')
                print("You bought a Cross Guard!")
            else:
                print('\nYou need 2 steels to combine a Cross Guard.')
        
        elif combineItem == 3:
            if 'steel' in player.inventory and 'leather' in player.inventory:
                player.equip_weapons('helmet')
                player.inventory.remove('steel') 
                player.inventory.remove('leather') 
                print("You bought a Helmet!")
            else:
                print('\nYou need steel and leather to combine a Helmet.')
        
        elif combineItem == len(shop_items) + 1:
            print("Exiting the shop.")
            return
        
        else:
            print("Invalid choice. Please select a valid option.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")


