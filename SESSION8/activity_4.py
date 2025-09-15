# Deleting or removing elements from Dictionary

"""
This can remove individual items or clear the entire dictionary. 
It can also delete entire dictionary just simple using del statement.
"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']  # remove entry with key 'Name'
dict.clear()      # remove all entries in dict
del dict          # delete entire dictionary

"""
We can remove a particular item in a dictionary by using the pop() method.
We can also use the popitem() method to remove and return an arbitrary (key, value) pair from the dictionary.
"""