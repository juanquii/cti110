# P5LAB
# Juan Necuzeaguet
# 07/08/2025
#  P5LAB
# This program will simulate a self-checkout machine, calculate and dispense change in currency denominations using a function and random values.

import random

# Delineates a function to calculate and print currency denominations for a given amount of change.

def disperse_change(change_owed):

    # Converts the float change owed to an integer representing total cents.

    total_cents = int(change_owed * 100 + 0.005)

    # Estimatte whole dollars and updates remaining cents following the same concept for quarters, dimes,nickels.

    num_dollars = total_cents // 100
    total_cents = total_cents % 100

    
    num_quarters = total_cents // 25
    total_cents = total_cents % 25

    
    num_dimes = total_cents // 10
    total_cents = total_cents % 10

    
    num_nickels = total_cents // 5
    total_cents = total_cents % 5

    
    num_pennies = total_cents

    # Creates formatted strings for each denomination, handling pluralization.
    
    dollar_string = (str(num_dollars) + ' Dollar' + ('s' * (num_dollars > 1)) + '\n') * (num_dollars > 0)
    quarter_string = (str(num_quarters) + ' Quarter' + ('s' * (num_quarters > 1)) + '\n') * (num_quarters > 0)
    dime_string = (str(num_dimes) + ' Dime' + ('s' * (num_dimes > 1)) + '\n') * (num_dimes > 0)
    nickel_string = (str(num_nickels) + ' Nickel' + ('s' * (num_nickels > 0)) + '\n') * (num_nickels > 0)
    penny_string = (str(num_pennies) + ' Penn' + ('y' * (num_pennies == 1)) + ('ies' * (num_pennies > 1)) + '\n') * (num_pennies > 0)

    # Prints the denomination strings. 'end=' prevents extra blank lines.
    print(dollar_string, end='')
    print(quarter_string, end='')
    print(dime_string, end='')
    print(nickel_string, end='')
    print(penny_string, end='')


# Defines the main function where the program's primary logic resides.

def main():

    # Generates a random amount owed by the customer, rounded to two decimal places.

    amount_owed = round(random.uniform(0.01, 100.00), 2)

    # Displays the randomly generated amount owed.

    print(f"You owe ${amount_owed:.2f}")

    # Suggests the user for cash input and converts it to a floating-point number.

    cash_input = float(input("How much cash will you put in the self-checkout? "))

    # Calculates the difference between cash provided and amount owed.

    change_due = cash_input - amount_owed

    
    print(f"Change is: ${change_due:.2f}")

    # Requests the disperse_change function to process and print the change breakdown.

    disperse_change(change_due)

# Ensures main() is called when the script is executed directly.

if __name__ == '__main__':
    main()
