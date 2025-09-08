# Exercise 2

"""
Write a Python Function calculation() such that it can accept two variables and
calculate the addition and subtraction of it. 
And it must return both addition and subtraction in a single return call.

def calc(a, b):
    return a + b, a - b
result = calc(10, 20)
print(result) # (30, -10)
"""
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
result = calculation(10, 20)
print("Addition and Subtraction are:", result) # (30, -10)
