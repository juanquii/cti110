# P1HW1
# Juan E Necuzzeaguet
# June 11, 2025
# A brief description: This program performs basic calculations with user input.

#----Calculating Exponents----
print("----Calculating Exponents----")

base = int(input("Enter a integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result_exp = base ** exponent
print(str(base) + " raised to the power of " + str(exponent) + " is " + str(result_exp) + " !!")

#----Addition and Subtraction----
# This title is now in the correct place.
print("\n----Addition and Subtraction----") 
start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
# The duplicated line that was here has been removed.
sub_num = int(input("Enter an integer to subtract: "))
result_calc = start_num + add_num - sub_num
print(str(start_num) + " + " + str(add_num) + " - " + str(sub_num) + " is equal to " + str(result_calc))
