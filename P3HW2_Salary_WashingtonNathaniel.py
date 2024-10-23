# Nathaniel Washington
# 10/23/2024
# P3HW2_Salary
# This program calculates the gross pay for an employee based on hours worked and pay rate,
# accounting for overtime if applicable.
# Input: Employee name, hours worked, pay rate
# Output: Employee details and calculated pay

# Pseudocode
# 1. Start program
# 2. Prompt user to enter employee name
# 3. Prompt user to enter number of hours worked
# 4. Prompt user to enter pay rate
# 5. If hours worked > 40, calculate:
#    a. Overtime hours = hours worked - 40
#    b. Overtime pay = Overtime hours * (pay rate * 1.5)
#    c. Regular hours pay = 40 * pay rate
# 6. Else:
#    a. Overtime pay = 0
#    b. Regular hours pay = hours worked * pay rate
# 7. Gross pay = Regular hours pay + Overtime pay
# 8. Display employee name, pay rate, hours worked, overtime hours, overtime pay, regular hours pay, and gross pay
# 9. End program


# Get employee details
employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Pay
overtime_hours = 0
overtime_pay = 0
regular_hours_pay = 0

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_hours_pay = 40 * pay_rate
else:
    regular_hours_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_hours_pay + overtime_pay

# Display results in landscape format
print("\nEmployee Pay Details")
print("---------------------")
print(f'Employee Name:         {employee_name}')
print(f'Pay Rate:              ${pay_rate:.2f}')
print(f'Hours Worked:          {hours_worked:.2f}')
print(f'Overtime Hours:        {overtime_hours:.2f}')
print(f'Overtime Pay:          ${overtime_pay:.2f}')
print(f'Regular Hours Pay:     ${regular_hours_pay:.2f}')
print(f'Gross Pay:             ${gross_pay:.2f}')

# Optional: Print all labels in one line for clarity
print("--------------------------")
print(f"Employee Name: {employee_name:<15}")
print("Pay Rate | Hours Worked | Overtime Hours | Overtime Pay | Regular Hours Pay | Gross Pay")
print("--------------------------------------------------------------------------------------------------------")
print(f'${pay_rate:<8.2f}   {hours_worked:<12.2f}   {overtime_hours:<14.2f}   ${overtime_pay:<12.2f}   ${regular_hours_pay:<18.2f}   ${gross_pay:<10.2f}')
