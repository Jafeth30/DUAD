"""EJERCICIO 4"""

num1 = float (input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
num3 = float (input("Enter the third number:"))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2>= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is : {largest}")

"""EJERCICIO 5 """

grade_counter = 1
passed_grades_count = 0
failed_grades_count = 0
passed_grades_sum = 0
failed_grades_sum = 0
total_grades_sum = 0

total_grades =int(input("Enter the total number of grades:"))

while grade_counter <= total_grades:
    print(f"Enter grade number {grade_counter}:")
    current_grade = float(input())
    total_grades_sum += current_grade

    if current_grade < 70:
        failed_grades_count += 1
        failed_grades_sum += current_grade
    else:
        passed_grades_count += 1
        passed_grades_sum += current_grade

    grade_counter += 1

total_grades_average = total_grades_sum / total_grades if total_grades > 0 else 0
passed_grades_average = passed_grades_sum / passed_grades_count if passed_grades_count > 0 else 0
failed_grades_average = failed_grades_sum / failed_grades_count if failed_grades_count > 0 else 0

print(f"The student has {passed_grades_count} passed grades.")
print(f"Average of passed grades: {passed_grades_average:.2f}")
print(f"The student has {failed_grades_count} failed grades.")
print(f"Average of failed grades: {failed_grades_average:.2f}")
print(f"Total average of all grades: {total_grades_average:.2f}")

