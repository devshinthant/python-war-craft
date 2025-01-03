def movePosition(player,end_game_fn):
    try: 
        next_positions = player.current_pos.possible_positions
        print("\nYou can move to:")

        for i,key in enumerate(next_positions):
         print(f"{i+1}: {key.capitalize()}")

        move_choice = int(input("\nChoose a position :"))

        if 0 <= move_choice <= len(next_positions):
            keys = list(next_positions.keys())
            selected_key = keys[move_choice - 1]

            # Move
            next_position = next_positions[selected_key]
            if next_position.name == 'War':
                if 'helmet' not in player.weapons:
                    print('\n === Helmet is required to join the war ===')
                if 'cross-guard' not in player.weapons:
                    print('\n === CrossGuard is required to join the war ===')
                if 'sword' not in player.weapons:
                    print('\n === Sword is required to join the war ===')
                if 'helmet' in player.weapons and 'cross-guard' in player.weapons and 'sword' in player.weapons:
                    end_game_fn()
            else:
                player.current_pos = next_position
                player.hydration_level = player.hydration_level - 1
                print(f"\nYou moved to {player.current_pos.name}.")
                print(f"{next_position.description}")
        else:
            print("Invalid choice. Try again.")
    except ValueError:
       print("Invalid input. Please enter a number.")
