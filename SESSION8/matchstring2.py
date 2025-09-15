# Task 4 - matches a string has an a followed by 3b

import re
def match_string(input_string):
    pattern = r'ab{3}'
    if re.search(pattern, input_string):
        return "Match found"
    else:
        return "No match"

test_string = "ab"
print(match_string(test_string))
test_string = "abbbb"
print(match_string(test_string))