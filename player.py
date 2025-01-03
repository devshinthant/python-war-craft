class Player:
    def __init__(self,name,current_pos,inventory = []):
        self.name = name
        self.inventory = inventory
        self.current_pos = current_pos
        self.weapons = []
        self.hydration_level = 10
    
    def add_to_inventory(self,item):
       if item == 'water':
          self.hydration_level = 10
          return
       if(self.hydration_level < 5):
          print(f'Your body hydration is too low to pick up item.')
          return
       if(len(self.inventory) < 5):
        if item != 'Shop':
            self.inventory.append(item)
            self.current_pos.item = []
            print(f"{item} has been added to your inventory.")
       else:
        print("Your inventory is full.")
        print("You can combine items or go to the shop.")

    def equip_weapons(self,weapon):
        self.weapons.append(weapon)
        print(f'{weapon} has been equipped.')

    def show_inventory(self):
        if(len(self.inventory) > 0):
            print("\nInventory Contents:")
            for i, item in enumerate(self.inventory,1):
              print(f"{i}. {item}")
        else:
           print("\nInventory is empty.")

    def show_weapons(self):
        if(len(self.weapons) > 0):
            print("\nEquipped Weapons:")
            for i, item in enumerate(self.weapons,1):
              print(f"{i}. {item}")
        else:
           print("\nNo Weapon equipped.")
           
    def check_hydration_level(self):
        print(f"\nBody hydration level is <{self.hydration_level}>.")






    