# Exercise 2

"""
Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.
"""

def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    return s1[:middle_index] + s2 + s1[middle_index:]

# Example usage
string1 = "Hello"
string2 = "World"
result = append_in_middle(string1, string2)
print(result)
print("The original strings are: ", string1, " and ", string2)