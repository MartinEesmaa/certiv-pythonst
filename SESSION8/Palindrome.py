# Task 1

"""
Write a python program to check whether a string is palindrome or not.
A Palindrome is a string which is same read forward or backwards, eg, “dad“.
Code constructors: if/else, Python strings, string methods
"""

# Define a string variable
my_str=input("Enter a string to check if it is a palindrome: ")

# Reverse the original string
reversed_str = reversed(my_str)

# Compare
if list(reversed_str) == list(my_str):
    print(f"'{my_str}' is a palindrome.")
else:
    print(f"'{my_str}' is not a palindrome.")