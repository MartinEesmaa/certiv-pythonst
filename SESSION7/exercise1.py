# Exercise 1

"""
Define a Python function that calculates and prints the value of the formula
y = 6a2 + 3a2 ; for a = 2
"""

def y(x):
    result = 6*(x**2) + 3*x
    return result

x=int(input("Enter the value of number : "))
result=y(x)
print("The formula result is:", result)