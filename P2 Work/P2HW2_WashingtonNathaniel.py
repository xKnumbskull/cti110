# Nathaniel Washington
# 10/08/2024
# P2HW2_NathanielWashington.py
# This program collects grades for 6 modules and displays the lowest, highest, sum, and average of the grades.

# Pseudocode:
# 1. Start the program.
# 2. Ask the user to enter the grades for Module 1 through Module 6.
# 3. Store the grades in a list called grades.
# 4. Calculate the lowest grade using min() function.
# 5. Calculate the highest grade using max() function.
# 6. Calculate the sum of the grades using sum() function.
# 7. Calculate the average of the grades by dividing the sum by the number of grades (use len() to get the number of items in the list).
# 8. Display the results as per the formatting in the example.
# 9. End the program.

# Collecting grades for each module
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Storing the grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculations
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / 6

# Displaying the results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade}")
print(f"Highest Grade:     {highest_grade}")
print(f"Sum of Grades:     {sum_of_grades}")
print(f"Average:           {average_grade:.2f}")
print("-------------------------------")
