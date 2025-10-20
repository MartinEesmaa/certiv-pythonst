# Class exercise

"""
Task 2: Write a python program to write a list to a file.
"""

data = ["Test nr 1", "Number two who is", "Always three"]
with open("output.txt", "w") as file:
    for line in data:
        file.write(line + "\n")
file.close()
print("Sample lines has been written to output.txt")