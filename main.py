import numpy as np
import random
from namesdb import first_names, last_names

# create subjects
subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ფიზიკა', 'ქიმია']

# crete number of students and subjects
num_students = 100
num_subjects = len(subjects)

# create random grades for each student
grades = np.random.randint(1, 101, size=(num_students, num_subjects))

# create random student full names
student_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(num_students)]

# format strings to print the table easy-to-read
# print table header
header_format = "{:5} {:30}" + "{:>15}" * num_subjects
print(header_format.format("N", "სტუდენტი", *subjects))
print("-" * (5 + 30 + num_subjects * 15))

# print student names and grades
row_format = "{:5} {:30}" + "{:>15}" * num_subjects
for i, (name, grades_row) in enumerate(zip(student_names, grades)):
    print(row_format.format(i+1, name, *grades_row))

# calculate and print average grades for each student
average_grades = grades.mean(axis=1)
best_student_index = average_grades.argmax()
best_student_name = student_names[best_student_index]
print(f"\nყველაზე მაღალი საშუალო ქულის მქონე სტუდენტია: {best_student_name}")

# find the student with the highest and lowest grade in math
math_grades = grades[:, 1]
highest_math_grade_index = math_grades.argmax()
lowest_math_grade_index = math_grades.argmin()
highest_math_grade_student = student_names[highest_math_grade_index]
lowest_math_grade_student = student_names[lowest_math_grade_index]
print(f"\nმათემატიკაში ყველაზე მაღალი ქულის მქონე სტუდენტია: {highest_math_grade_student}")
print(f"მათემატიკაში ყველაზე დაბალი ქულის მქონე სტუდენტია: {lowest_math_grade_student}")

# print students with above average english grades
english_grades = grades[:, 2]  # ინგლისურის ქულები
average_english_grade = english_grades.mean()
above_average_english_students = [name for name, grade in zip(student_names, english_grades)
                                  if grade > average_english_grade]
print(f"\nსტუდენტები, რომლებსაც ინგლისურის ქულა აქვთ საშუალოზე მეტი:")
for student in above_average_english_students:
    print(student)

# print students who failed chemistry
chemistry_grades = grades[:, 4]  # ქიმიის ქულები
failed_chemistry_students = [name for name, grade in zip(student_names, chemistry_grades)
                             if grade < 51]
print("\nქიმიაში 'ჩაჭრილი' სტუდენტები:")
for student in failed_chemistry_students:
    print(student)

# count students named "გვანცა" who has max points in every subject
max_grades = np.max(grades, axis=0)
gvantsa_count = sum(1 for name, grades_row in zip(student_names, grades) if name.split()[0] == "გვანცა" and
                    all(grades_row == max_grades))
print(f"\n'გვანცა' სახელის მქონე სტუდენტები, რომელთაც ყველა საგანში აქვთ მაქსიმალური ქულა: {gvantsa_count}")

# print "გვანცა" students whose points are above 20 in every subject
gvantsa_students = [(name, grades_row) for name, grades_row in zip(student_names, grades)
                  if name.split()[0] == "გვანცა" and np.all(grades_row > 20)]
print("\n'გვანცა' სახელის მქონე სტუდენტები, რომელთა ქულებიც აღემატება 20-ს:")
for student, grades_row in gvantsa_students:
    print(f"{student}: {grades_row}")
