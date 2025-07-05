# P4HW1
# Juan Necuzeaguet
# 07/03/2025
# This program gets a specific number of scores from the user, verify them,
# drops the lowest score, calculates the average of the remaining scores,
# and determines a letter grade for that average.

# Pseudocode (Detailed Algorithm)
# --------------------------------------------------------------------------------------------------
# 1. Initialize an empty list called 'scores_list' to store valid integer scores.
# 2. Ask the user: "How many scores do you want to enter?"
#  Convert the user's input to an integer and save  it in 'num_scores'.
#
# 3. Begin an outer loop to iterate 'num_scores' times (from 1 up to num_scores):
#    a. For each iteration (representing 'score_number'):
#       i. Set a flag 'score_valid' to False.
#       ii. Start an inner loop (e.g., 'while' loop) that continues as long as 'score_valid' is False:
#           - Tell the user: "Enter score #{score_number}: "
#           - Change the input to an integer and save it in 'current_score'.
#           - Validate 'current_score':
#             - If 'current_score' is greater than or equal to 0 AND 'current_score' is less than or equal to 100:
#               - Set 'score_valid' to True.
#             - Else (if 'current_score' is invalid):
#               - Print "INVALID Score entered!!!"
#               - Print "Score should be between 0 and 100"
#               - (Inner loop will automatically re-prompt)
#
#       iii. After the inner loop, the 'current_score' is certain to be correct.
#       iv. Add 'current_score' to the 'scores_list'.
#
# 4. After the outer score collection loop finishes:
#    a. If 'scores_list' is empty (e.g., user entered 0 scores):
#       - Print a message indicating no scores to process.
#    b. Else (if 'scores_list' is not empty):
#       i. Find the 'lowest_score' in 'scores_list' (using min() function).
#       ii. Create a 'modified_scores_list' by making a copy of 'scores_list'.
#       iii. Remove the 'lowest_score' from 'modified_scores_list' (using remove() method).
#       iv. Calculate the 'total_modified_scores' (sum() of 'modified_scores_list').
#       v. Calculate the 'count_modified_scores' (len() function) of 'modified_scores_list'.
#       vi. If 'count_modified_scores' is greater than 0:
#           - Calculate the 'scores_average' by dividing 'total_modified_scores' by 'count_modified_scores'.
#       vii. Else (if 'modified_scores_list' is empty after removing lowest, e.g., only one score was entered):
#           - Set 'scores_average' to 0.0.
#
#       viii. Determine the 'letter_grade' based on 'scores_average' using if/elif/else statements:
#           - If 'scores_average' is greater than or equal to 90: Grade is 'A'
#           - Else if 'scores_average' is greater than or equal to 80: Grade is 'B'
#           - Else if 'scores_average' is greater than or equal to 70: Grade is 'C'
#           - Else if 'scores_average' is greater than or equal to 60: Grade is 'D'
#           - Else (if 'scores_average' is less than 60): Grade is 'F'
#
#       ix. Show the results to the user in the specified format:
#           - Print "----Results----"
#           - Print "Lowest Score : [lowest_score]"
#           - Print "Modified List : [modified_scores_list]"
#           - Print "Scores Average : [scores_average formatted to 2 decimal places]"
#           - Print "Grade : [letter_grade]"
#           - Print a dashed separator line.
# --------------------------------------------------------------------------------------------------

scores_list = []

num_scores_str = input("How many scores do you want to enter? ")
num_scores = int(num_scores_str)

for score_number in range(1, num_scores + 1):
    score_is_valid = False
    while not score_is_valid:
        score_input_str = input(f"Enter score #{score_number}: ")
        current_score = int(score_input_str)

        if 0 <= current_score <= 100:
            scores_list.append(current_score)
            score_is_valid = True
        else:
            print("INVALID Score entered!!!")
            print("Score should be between 0 and 100")

if scores_list: # Only process if scores were entered
    lowest_score = min(scores_list)
    
    modified_scores_list = list(scores_list) # Create a copy to modify
    modified_scores_list.remove(lowest_score)

    total_modified_scores = sum(modified_scores_list)
    count_modified_scores = len(modified_scores_list)

    if count_modified_scores > 0: # Prevent division by zero if list becomes empty (e.g., only one score entered)
        scores_average = total_modified_scores / count_modified_scores
    else:
        scores_average = 0.0 # Handle case where all scores were removed (e.g., only one score entered)

    letter_grade = ""
    if 90 <= scores_average <= 100:
        letter_grade = "A"
    elif 80 <= scores_average < 90:
        letter_grade = "B"
    elif 70 <= scores_average < 80:
        letter_grade = "C"
    elif 60 <= scores_average < 70:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("\n" + "-" * 15 + "Results" + "-" * 15)
    print(f"Lowest Score : {lowest_score:.1f}")
    print(f"Modified List : {modified_scores_list}")
    print(f"Scores Average : {scores_average:.2f}")
    print(f"Grade : {letter_grade}")
    print("-" * 37)

else: # Case if 0 scores were entered initially
    print("\nNo scores were entered to process.")
