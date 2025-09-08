# Exercise 3

"""
Create a nested function to perform the following steps:
Create an external / outer function that will accept two parameters a and b;
Create an inner function inside an outer function that will calculate the addition  of the above two parameters;
Lastly, the outer function will add a value 10 into the addition and return it.

def outFunc(a, b):
    def inFunc(a, b):
        return a + b
    add = inFunc(a, b)
    return add + 10

result = outFunc(3, 6)
print(result)
"""

def outer_function(a, b):
    def inner_function(a, b):
        return a + b
    addition = inner_function(a, b)
    return addition + 10
result = outer_function(3, 6)
print("The final result is:", result)