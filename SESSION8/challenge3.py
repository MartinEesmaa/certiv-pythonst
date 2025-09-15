# Exercise 3

"""
Given a string input count all lower case, upper case, digits, and special symbols.
"""
def count_characters(input_string):
    lower_case = 0
    upper_case = 0
    digits = 0
    special_symbols = 0

    for char in input_string:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return {
        "lower_case": lower_case,
        "upper_case": upper_case,
        "digits": digits,
        "special_symbols": special_symbols
    }

# Example usage
input_str = "Hello World@! 123"
result = count_characters(input_str)
print(result)
print("The input string is: ", input_str)