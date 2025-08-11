# Q2: Write a program to solve following grading system:

"""
A: 90% +
B: 80% - 89%
C: 70% - 79%
D: 60% - 69%
E: 50% - 59%
Fail: 0-49%
Take score as a input from user.
"""

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade: E")
else:
    print("Grade: Fail")
