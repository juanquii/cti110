# Juan Necuzeaguet
# 06/17/2025
# P2LAB2 - Vehicle MPG
# The program stores vehicle MPG data in a dictionary and calculates fuel needs based on the person input.

my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }

keys = my_dict.keys()
print(keys)

selected_vehicle = input("Enter a vehicle to see it's mpg: ")

mpg =   my_dict[selected_vehicle]
print(f"The {selected_vehicle} gets {mpg} mpg.")
miles = float(input(f"How many miles will you drive the {selected_vehicle}? "))
gallons = miles / mpg
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {selected_vehicle} {miles:.1f} miles.")
