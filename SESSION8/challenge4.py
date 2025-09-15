# Exercise 4

"""
Given an input string, count occurrences of all characters within a string.
"""
def count_character_occurrences(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Example usage
input_str = "Hello World!"
result = count_character_occurrences(input_str)
print("The input string is:", input_str)

# Print each character and its count on a separate line
for char, count in result.items():
    print(f"{char}: {count}")