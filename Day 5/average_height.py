students_height= input("Input the heights of students").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

total_height = 0
for height in students_height:
    total_height += height
print(total_height)

number_of_students = 0
for student in students_height:
    number_of_students += 1
print(number_of_students)

average_height = total_height / number_of_students
print(round(average_height))
