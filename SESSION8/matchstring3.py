# Task 5 - Write a Python program to find substrings within a string.

"""
Write a Python program to find sub-strings within a string

Sample text :
'Python exercises, PHP exercises, C# exercises'

Pattern :
'exercises'

Note: There are two instances of exercises in the input string.
"""

import re
text="Python exercises, PHP exercises, C# exercises"
pattern = r'exercises'
matches = re.findall(pattern, text)
print(f"Number of matches found: {len(matches)}")