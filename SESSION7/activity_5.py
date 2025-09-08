# Returning a result from a function

"""
The return statement is followed by an expression which is evaluated and the value is returned to the caller.
"""

def square(x):
    y = x * x
    return y
toSquare = 10
result = square(toSquare)
print("The result of", toSquare, "squared is", result)

def fahr_to_celsius(temp):
    y = ((temp - 32) * 5) / 9
    return y
temp = 100
result = fahr_to_celsius(temp)
print("The temperature of fahrenheit is", temp, "\nIn Celsius is", result)