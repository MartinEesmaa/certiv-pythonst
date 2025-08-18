# Question 1
"""
Write a program to print all integers
that are not divisible by 2 and 3 and
lie between 1 and 100.
"""

for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        continue
    print(i)