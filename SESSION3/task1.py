# Description: This program prompts the user for their numeric grade
# and prints one of three mesages depending on the grade.

"""
Flowchart:

Greater than 90 = Very good!
Between 80 and 89 = Good!
Between 70 and 79 = Satisfactory!
Between 60 and 69 = Fair
Less than 60 = Poor
"""

grade = int(input("Enter your grade: "))
if grade >= 90:
    print("Very good!")
elif grade >= 80:
    print("Good!")
elif grade >= 70:
    print("Satisfactory!")
elif grade >= 60:
    print("Fair!")
else:
    print("Poor!")