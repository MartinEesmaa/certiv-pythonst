# Parametrized functions

"""
Write a function to check a number is odd or even.
"""

def odd_even(x):
    if x % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
    odd_even(5)

"""
Here, x is a parameter. We can send as many as we want by seperating them with commas.
"""