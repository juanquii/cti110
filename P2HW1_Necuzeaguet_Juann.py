# P2HW1_Necuzeaguet_Juan.py
# 06-13-2025
# P1HW2 - Travel Expense Calculator
# A brief description of the project: This Program helps families or individuals to manage their budget ont heir travels.

"""
Pseudocode:
1. START
2. Display a name for the program.
3. Ask user to enter their budget. Save it.
4. Ask user for their travel destination. Save it.
5. Ask for the amount they will spend on gas. Save it.
6. Ask for the amount they will spend on accommodation. Save it.
7. Ask for the amount they will spend on food. Save it.
8. Add the expenses (gas, accommodation, food) to get a total.
9. Subtract the total expenses from the initial budget to get the remaining balance.
10. Display the destination, initial budget, and each expense.
11. Display the remaining balance.
12. END
"""

# Display program title

print("This Program helps families or individuals to manage their budget on their travels")
print() # Spacing so it looks cleaner

# Obtain the user input
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much will you think you will spend on Gas: "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel?: "))
food = int(input("Last, how much do you need for food?: "))

#Calculations
remaining_balance = budget - gas - accommodation - food

#Results

print()
print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {accommodation}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")

