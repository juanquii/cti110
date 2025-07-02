# Juan Necuzeaguet
# 06/20/2025
# Assignment Name: P2HW2 List
# Brief description of program Brief description of program: This program asks the user for six module grades,
# stores them in a list, and then calculates and displays the lowest grade,
# highest grade, the sum of the grades, and the average grade


# Pseudocode (Detail Algorithm)
# 1. START
# 2. Ask the user to input the mark of Module 1. Save into a variable which you can call 'mod1'.
# 3. Ask the user to type the grade of Module 2. Put this in a new variable called 'mod2'
# 4. Ask the user to input the grade for Module 3. Save it in a variable called 'mod3'.
# 5. Ask the user what their grade was for Module 4. Save in a variable 'mod4'.
# 6. Write code that asks the user for the grade for Module 5. Put this into a variable called mod5.
# 7. Ask the user to input his/her score for Module 6. Save it in a variable called 'mod6'.
# 8. Create a new list as 'grades_list' and include the mod1, mod2, mod3, mod4, mod5 and mod6 values in it.
# 9. Use the min() function to get the lowest grade in 'grades_list' and assign the result to a variable called 'lowest_grade'.
# 10. Use the max() function to find the highest grade in 'grades_list' and assign it to the variable 'highest_grade'.
# 11. Using the sum() function, sum all the grades in 'grades_list' and assign the result to a variable called 'sum_of_grades.'
# 12. Find the average of the grades by dividing 'sum_of_grades' by 6 and assign it to a variable 'average_grade'.
# 13. Display a "Results" header.
# 14. Display the 'lowest_grade' with one decimal point precision.
# 15. Show the field 'highest_grade', now formatted to one decimal point.
# 16. Show's the 'sum_of_grades', rounded to one decimal point.
# 17. Show the 'average_grade', with two decimal places.
# 18. END
# 

print("Enter grade for Module 1:", end=" ")
mod1 = float(input())

print("Enter grade for Module 2:", end=" ")
mod2 = float(input())

print("Enter grade for Module 3:", end=" ")
mod3 = float(input())

print("Enter grade for Module 4:", end=" ")
mod4 = float(input())

print("Enter grade for Module 5:", end=" ")
mod5 = float(input())

print("Enter grade for Module 6:", end=" ")
mod6 = float(input())

grades_list = [mod1, mod2, mod3, mod4, mod5, mod6]

lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = sum_of_grades / len(grades_list)

print("\n------------Results------------")
print(f'Lowest Grade:    {lowest_grade:.1f}')
print(f'Highest Grade:   {highest_grade:.1f}')
print(f'Sum of Grades:   {sum_of_grades:.1f}')
print(f'Average:         {average_grade:.2f}')
print("-------------------------------")
