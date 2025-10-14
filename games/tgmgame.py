# Multiplication Tables Generation Game
# Programmed by Martin Eesmaa (2025)
# License: MIT
# Source code: https://github.com/MartinEesmaa/certiv-pythonst
# Script language version: Python 3
# Filename: tgmgame.py
# Date: 14.10.2025

"""
This activity requires an algorithmic solution and corresponding script 
implementation to automatically generate a multiplication table for 
a specific number and print the multiplicand, multiplier (also called factors), 
and product for a given number of times. 

For example, output the 6 times table from 1 to 12.
"""

print("\nWelcome to the Multiplication Tables Generation Game!\n")
print("Programmed by Martin Eesmaa (2025)\n")

while True:
    try:
        number = int(input("Type number for which you want the times table: "))
        if number >= 1:
            break
        else:
            print("The number must be 1 or greater. Please try again.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

while True:
    try:
        limit = int(input("Type number how many times you want to multiply (e.g., 12 for 1 to 12): "))
        if limit >= 1:
            break
        else:
            print("The limit must be 1 or greater. Please try again.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

print(f"\nTable result: {number} times from 1 to {limit} are:\n")
for i in range(1, limit + 1):
    product = number * i
    print(f"{number} x {i} = {product}")
print("\nThank you for playing the Multiplication Tables Generation Game!\n")