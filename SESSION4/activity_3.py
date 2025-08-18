# Activity 3
"""
Write a program that prints a 3x3 grid of numbers (1 to 9) using
nested for loops but breaks out of both loops when it encounters
the number five.
"""

for i in range(1, 4):
    for j in range(1, 4):
        num = (i - 1) * 3 + j
        if num == 5:
            break
        print(num, end=' ')
    if num == 5:
        break
    print()