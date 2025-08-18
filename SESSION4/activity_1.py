# Activity 1
"""
Write a Python program that prints all numbers from 1 to 20
but stops when it encounters the first multiple of 7.
"""

for i in range(1, 21):
    if i % 7 == 0:
        break
    print(i)