# P5HW
# Juan Necuzaguet
# 07/10/2025
# P5HW
# This program is a text-based adventure game where choices affect the end result.

import random

# Defines a function to create a player character as a dictionary.
def create_player():
    player = {
        "name": "Adventurer",
        "health": 100,
        "inventory": []
    }
    return player

# Defines a function to get and validate player input for a choice.
def get_player_choice(prompt_text, valid_choices):
    is_valid = False
    while not is_valid:
        choice = input(prompt_text).strip().lower()
        if choice in valid_choices:
            is_valid = True
            return choice
        else:
            print("Invalid choice. Please try again.")

# Defines a function to show a random outcome for a scenario.
def display_random_outcome(scenario_type, player):
    outcomes = {
        "treasure": ["You find a pile of gold!", "You discover an ancient artifact!", "You locate a hidden gem!"],
        "danger": ["A trap springs and you lose health!", "A monster ambushes you!", "You fall into a pit!"]
    }
    
    outcome_message = random.choice(outcomes[scenario_type])
    print(outcome_message)

    if scenario_type == "danger":
        damage = 25
        player['health'] -= damage
        print("You quickly escape, but feel weakened.")
        print(f"You lost {damage} health! Your current health is {player['health']}.")

# Defines the main function where the game logic is.
def main():
    play_again = 'yes'
    player_char = create_player()
    
    while play_again == 'yes':
        print(f"\n--- Welcome to The Mysterious Cave! ---")
        
        print(f"You, the brave {player_char['name']}, stand at the entrance of a dark cave.")
        print(f"Your health: {player_char['health']}")

        print("\nYou see two paths ahead: a narrow passage (1) and a wide tunnel (2).")
        choice1 = get_player_choice("Which path do you choose? (1 or 2): ", ['1', '2'])

        if choice1 == '1':
            print("\nYou venture into the narrow passage. It's damp and quiet.")
            scenario = random.choice(["treasure", "danger"])
            display_random_outcome(scenario, player_char)
        else:
            print("\nYou cautiously enter the wide tunnel. You hear distant echoes.")
            display_random_outcome("treasure", player_char)

        print("\nThe path eventually leads you back to the cave entrance.")

        if player_char['health'] <= 0:
            print("\nYou have run out of health. The cave has claimed you.")
            print("Thanks for playing!")
            break

        play_again = get_player_choice("Do you want to explore again? (yes/no): ", ['yes', 'no'])
        if play_again == 'no':
            print("\nThanks for exploring The Mysterious Cave!")
        else:
            player_char['health'] = 100 
            print("\nYou take a moment to rest and recover your strength.")
            
# Calls the main function to start the game when the script is run.
if __name__ == "__main__":
    main()
