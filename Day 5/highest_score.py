students_score = input("Input the scores of students").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])  
print(students_score)

highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

