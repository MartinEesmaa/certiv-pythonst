# Question 7 as final: Combining Lists and Tuples

"""
Following list and tuple are:
list_a = [1, 2, 3, 4]
tuple_b = (5, 6, 7, 8)

Combine these into a single list combined that contains
all the elements from both the list and the tuple.

Print the results.
"""

list_a = [1, 2, 3, 4]
tuple_b = (5, 6, 7, 8)

# Combine list_a and tuple_b into a single list
combined = list_a + list(tuple_b)

# Print the results
print("List combined numbers by merging:")
print(combined)