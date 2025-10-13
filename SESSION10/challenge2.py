# Question 2

"""
Write a program to do the unit test of four different modules.
Here module means, you need to create four different functions
to perform four tasks like addition, subtraction, multiplication and division.

More specificially, the tasks are given below:

A) Create a class to do this.
B) Under this class create four functions
C) Test all the functions using for different input and output set.
"""
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero error"

# Unit tests
calc = Calculator()
print(calc.add(2, 3))  # 5
print(calc.subtract(5, 2))  # 3
print(calc.multiply(2, 3))  # 6
print(calc.divide(6, 2))  # 3.0
print(calc.divide(6, 0))  # Division by zero error