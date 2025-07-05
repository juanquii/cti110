# P4HW2
# Juan Necuzeaguet
# 07/03/2025
# This program detreminne gross pay for multiple employees using a condition-controlled
# loop. It handles overtime pay and shows individual and comlpete payroll statistics.


# -------------------------------------------------------------------------------------
# START
#   Begin complete counters for employees, overtime, regular, and gross pay to 0.
#
#   LOOP indefinitely until user enters "Done":
#       PROMPT for employee's name or "Done".
#       IF "Done", exit loop.
#
#       GET employee's hours and pay rate.
#       CALCULATE overtime, regular, and gross pay based on hours worked.
#       ADD current pay amounts to total counters.
#       DISPLAY current employee's detailed pay information.
#   END LOOP
#
#   DISPLAY final summary totals for all employees.
# END
# -------------------------------------------------------------------------------------


total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
total_employees = 0

while True:
    
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    
    if employee_name == "Done":
        break  
        
    total_employees += 1
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    overtime_hours = 0.0
    overtime_pay = 0.0
    regular_pay = 0.0
    gross_pay = 0.0

    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * pay_rate * 1.5

    else:
        regular_hours = hours_worked
        regular_pay = regular_hours * pay_rate
        overtime_pay = 0.0
        
    gross_pay = regular_pay + overtime_pay
    
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    print(f"\nEmployee name: {employee_name}\n")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay'}")
    print("-" * 85)
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}${overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<.2f}\n")


print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:,.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:,.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:,.2f}")
