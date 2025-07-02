# P3HW1_NecuzeaguetJuan
# This program calculates student grades based on six module scores.
# June 25, 2025
# CTI-110 P3HW1 - Debugging
# Juan Necuzeaguet


# 1. Ask for grades and store them in a list



grades = []
grades.append(float(input('Enter grade for Module 1: ')))
grades.append(float(input('Enter grade for Module 2: ')))
grades.append(float(input('Enter grade for Module 3: ')))
grades.append(float(input('Enter grade for Module 4: ')))
grades.append(float(input('Enter grade for Module 5: ')))
grades.append(float(input('Enter grade for Module 6: ')))


#  Perform calculations using list functions

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# 3. Display the calculated results

print("\n---------Results---------------")
print(f'Lowest Grade: {lowest_grade:.1f}')
print(f'Highest Grade: {highest_grade:.1f}')
print(f'Sum of Grades: {sum_of_grades:.1f}')
print(f'Average Grade: {average_grade:.2f}')
print("---------------------------------")






# 4. Determine and display the letter grade using an if-elif-else chain


if average_grade >= 90:
    print('Your grade is: A')
elif average_grade >= 80:
    print('Your grade is: B')
elif average_grade >= 70:
    print('Your grade is: C')
elif average_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')  

 





