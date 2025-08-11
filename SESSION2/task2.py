"""
Scenario take a look at the code below it reads a float value, puts into a variable
named x, and prints the value of a variable named y. Your task is to complete the code
in order to evaluate the following expression:

3x(square root 3) + 2x(square root 2) + 3x - 1
"""

import math

x = float(input("Enter a float value for x: "))
y = 3 * x * math.sqrt(3) + 2 * x * math.sqrt(2) + 3 * x - 1
print("The value of y is:", y)