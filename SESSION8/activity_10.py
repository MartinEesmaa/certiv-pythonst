# Iterating through String & Python string methods

"""
Using for loop we can iterate trough a string, an example to count the number of 'l's in a string.
"""

count = 0
for letter in 'Hello World':
    if letter == 'l':
        count += 1
print(count, "letters found")