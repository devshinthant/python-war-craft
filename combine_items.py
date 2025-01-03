combine_items = ['steel','charcoal']

def combineItems(player):
   try:
      print('\n<== Iron Ore + Charcoal = Steel ==>')
      print('<== Rocks + Wood = Charcoal ==>\n')
      print('What would you like to combine?')
      for i,item in enumerate(combine_items,1):
         print(f'{i}. Combine {item}')
      print(f'{len(combine_items)+1}. back')
      combineItem = int(input('\nChoose an item: '))

      if combineItem == 1:
         if 'iron-ore' in player.inventory and 'charcoal' in player.inventory:
            player.inventory.remove('iron-ore')
            player.inventory.remove('charcoal')
            player.add_to_inventory('steel')
         else:
            print('You need iron ore and charcoal to combine steel')
      if combineItem == 2:
         if 'rocks' in player.inventory and 'wood' in player.inventory:
            player.inventory.remove('wood') 
            player.add_to_inventory('charcoal')
         else: 
            print('You need rocks and wood to combine charcoal')
      if combineItem == 3:
         return
   except ValueError:
      print("Invalid input. Please enter a number.")
