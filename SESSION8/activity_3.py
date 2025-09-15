# Changing or adding elements in Dictionary

"""
Dictionaries are mutable, meaning they can be changed or new items to the existing items using assignment operator.
If the key is already present, the value gets updated, else a new key: value pair is added to the dictionary.
"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# When the above code is executed, it produces the following result:

"""
dict['Age']:  8
dict['School']:  DPS School
"""