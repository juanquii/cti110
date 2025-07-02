# P3HW2_Salary_Necuzeaguet_Juan
# June 26, 2025
# CTI-110 P3HW2 - Salary
# This program asks a user for an employee's name, hours worked, and pay rate.
# It then calculates the employee's regular pay, overtime pay, and gross pay
# and displays the results in a formatted table.


# Define the Pseudocode
# START
#   ASK user for employee's name and STORE in variable `employee_name`.
#   ASK user for number of hours worked and STORE in variable `hours_worked`.
#   ASK user for pay rate and STORE in variable `pay_rate`.
#
#   SET `overtime_hours` to 0.
#   START `overtime_pay` to 0.
#
#   IF `hours_worked` is greater than 40:
#       DETERMINE `regular_hours` as 40.
#       FIND `overtime_hours` as `hours_worked` - 40.
#       DETERMINE `overtime_pay_rate` as `pay_rate` * 1.5.
#       WORK OUT `overtime_pay` as `overtime_hours` * `overtime_pay_rate`.
#       DETERMINE `regular_pay` as `regular_hours` * `pay_rate`.
#   ELSE:
#       CALCULATE `regular_pay` as `hours_worked` * `pay_rate`.
#
#   CALCULATE `gross_pay` as `regular_pay` + `overtime_pay`.
#
#   SHOW `employee_name`.
#   SHOW formatted table headers: "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "Reghour Pay", "Gross Pay".
#   SHOW formatted results for `hours_worked`, `pay_rate`, `overtime_hours`, `overtime_pay`, `regular_pay`, `gross_pay`.
# END

# Retrieve the user input

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-" * 30)

# Start the variables for calculation

overtime_hours = 0.0
overtime_pay = 0.0
regular_pay = 0.0
gross_pay = 0.0

# See if employee worke overtime

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40

    # Calculate pay for regular and overtime hours

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    regular_pay = hours_worked * pay_rate
    
gross_pay = regular_pay + overtime_pay

# displayed result in a formated table

print(f"Employee name: {employee_name}\n") # \n

# Headers

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"Reghour Pay":<20}{"Gross Pay"}')
print("-" * 100)

print(f'{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<19.2f}${regular_pay:<19.2f}${gross_pay:.2f}')













    
    
