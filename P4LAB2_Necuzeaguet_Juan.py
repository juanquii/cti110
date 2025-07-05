# P4LAB2
# Juan Necuzeaguet
# 07/02/2025
# This program create a multiplication table for a User's input integer (0 or higher)
# or tells the user if a negative integer is provided. It uses both for and while loops
# and allows the user to run it multiple times.

run_again = "yes"

# Outside loop to allow the user to run the program numerous times

while run_again.lower() == "yes":
    print() 
    
    user_input_str = input("Enter an integer: ")
    user_number = int(user_input_str)

    # Verify if the entered integer is negative
    if user_number < 0:
        print("This program does not handle negative number")
    else:
        # Use a for loop to show the multiplication table
        for i in range(1, 13):
            result = user_number * i
            print(f"{user_number} * {i} = {result}")
    
    # Prompts the user if they want to run it again
    print() 
    run_again = input("Would you like to run the program again? ")


print("Exiting program...")
