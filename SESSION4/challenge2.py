# Challenge 2: Multiplication Table
"""
Write a program that generates a multiplication table for numbers 1 to 10,
but skips printing the results where the product is divisible by 6.
"""

for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        if product % 6 == 0:
            continue
        print(product, end=' ')
    print()