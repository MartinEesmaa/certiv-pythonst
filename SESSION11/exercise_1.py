# Class exercise

"""
Task 1 : Write a python program to read a file line by line
and store it into a variable. Print a result.
"""

write_content = ""
with open("TEST.txt", "r") as file:
    for line in file:
        write_content += line
file.close()
print(write_content)