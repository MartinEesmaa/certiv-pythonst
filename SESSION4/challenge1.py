# Challenge 1: Prime Number Checker
"""
Write a Python program that uses a while loop to check if a given number is prime.
Use break when you find the first divisor.
"""

num = int(input("Enter a number: "))
is_prime = True
i = 2

while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")