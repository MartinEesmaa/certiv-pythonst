# Activity 2
"""
Write a Python program that prints all numbers from 1 to 30
but skips the numbers that are divisible by 4.
"""

count = 1
while count <= 30:
    if count % 4 == 0:
        count += 1
        continue
    print(count)
    count += 1