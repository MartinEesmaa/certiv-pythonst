# Chaning a Tuple

my_tuple = (4, 2, 3, [6, 5])
# We cannot change an element of a tuple
# If you uncomment line you will get an error
"""
TypeError: 'tuple' object does not support item assignment
"""
# my_tuple[1] = 9
"""
But item of mutable element can be changed
Output: (4, 2, 3, [9, 5])
"""
my_tuple[3][0] = 9
print(my_tuple)
"""
Tuples can be reassigned by output programiz
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
"""
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)