# Exercise 1

"""
Given a dictionary get all values from the dictionary 
and add it in a list but don’t add duplicates.
"""

def get_unique_values(input_dict):
    unique_values = []
    for value in input_dict.values():
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 4}
print("Removed duplicate values:", get_unique_values(my_dict))