from player import Player
from map import setUpMap
from move_position import movePosition
from look_items import lookItems
from purchase_items import purchaseItems
from combine_items import combineItems
from display_menu import displayMenu


def game():
    print("\n WELCOME TO THE GAME !! \n")
    print("# You are in the forest. \n")
    print("<==== Before you join the war, you must need to get weapons by collecting items in the forest. ====> \n")

    game_end = False
    initial_position = setUpMap()
    player = Player(input('Enter your username: '),initial_position)
    print(f"\nWelcome {player.name} !!")

    def end_game_fn(): 
      nonlocal game_end
      print("Congratulations! You won the game.")
      game_end = True
   
    while game_end == False:
        displayMenu(player.current_pos.name)
        choice = input("\nEnter your choice (1-7):")

        if player.hydration_level == 0:
          print("You are dehyrdated and Lost the game!")
          return;
       
        # Move position 
        if(choice == '1'): 
            movePosition(player,end_game_fn)

        # Look for items & Pick items
        elif choice == '2':
             if player.current_pos.item:
               purchaseItems(player) if player.current_pos.name == 'Shop' else lookItems(player)
             else:
                print("\nThere is no items.")

        # Show items in the bag
        elif choice == '3':
          player.show_inventory()
        elif choice == '4':
          combineItems(player)
        elif choice == '5':
          player.check_hydration_level()
        elif choice == '6':
          player.show_weapons()
        elif choice == '7':
         print('Thank you for playing! GoodBye!')
         break
        else:
         print("Invalid choice. Try again.")

game()

