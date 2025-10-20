# Class exercise

"""
Task 3: Write a program to read the grade of 5 student
from a file called letter.txt. Manager asked me to write
down the gpa of five students based on their grade in another file
called gpa.txt

The formula for grade to GPA conversion is given below:
A = 4, B = 3, C = 2
D = 1, F = 0, others = -1
"""
grade_to_gpa = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "F": 0,
    "others": -1
}

# Write letter.txt for testing purpose
with open("letter.txt", "w") as file:
    file.write("A\nB\nC\nD\nF\nothers\n")
file.close()
# Read grades from letter.txt and write corresponding gpa to gpa.txt
grades = []
with open("letter.txt", "r") as file:
    for line in file:
        grades.append(line.strip())
file.close()
gpas = []
for grade in grades:
    gpa = grade_to_gpa.get(grade, -1)
    gpas.append(gpa)
with open("gpa.txt", "w") as file:
    for gpa in gpas:
        file.write(str(gpa) + "\n")
file.close()
print("GPA values have been written to gpa.txt")