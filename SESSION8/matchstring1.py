# Task 3

"""
Write a python program that matches a string that has an a followed by one or more b’s.
You can use functions to write this simple program.
"""

import re

def match_string(input_string):
    pattern = r'a+b+?'
    if re.search(pattern, input_string):
        return "Match found"
    else:
        return "No match"

test_string = "aaabbb"
print(match_string(test_string))