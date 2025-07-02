# P3LAB_Necuzeaguet_Juan
#Program will calculate change for a given amount of money

input_amount = float(input('Enter the amount of money as a float: '))
total_cents = int(input_amount * 100)

# Calculate Dollars

num_dollars = total_cents // 100
cents_remaining = total_cents % 100

# Calculate Quarters

num_quarters = cents_remaining // 25
cents_remaining = cents_remaining % 25

# Calculate Dimes

num_dimes = cents_remaining // 10
cents_remaining = cents_remaining % 10


# Calculate Nickels

num_nickels = cents_remaining // 5

# Calculate Pennies

num_pennies = cents_remaining % 5

# Create output strings for Dollars, Quarters, Dimes, Nickels, and Pennies (Special Pluralization)

dollar_string = (str(num_dollars) + ' Dollar' + ('s' * (num_dollars > 1)) + '\n') * (num_dollars > 0)
quarter_string = (str(num_quarters) + ' Quarter' + ('s' * (num_quarters > 1)) + '\n') * (num_quarters > 0)
dime_string = (str(num_dimes) + ' Dime' + ('s' * (num_dimes > 1)) + '\n') * (num_dimes > 0)
nickel_string = (str(num_nickels) + ' Nickel' + ('s' * (num_nickels > 1)) + '\n') * (num_nickels > 0)
penny_string = (str(num_pennies) + ' Penn' + ('y' * (num_pennies == 1)) + ('ies' * (num_pennies > 1)) + '\n') * (num_pennies > 0)



# Combine all the individual coin strings

change_output = dollar_string + quarter_string + dime_string + nickel_string + penny_string

# Define the output for the zero case

no_change_output = 'No change'

# Select which output to use based on the total amount

final_output = change_output * (total_cents > 0) + no_change_output * (total_cents == 0)


print(final_output)            
                
                 
