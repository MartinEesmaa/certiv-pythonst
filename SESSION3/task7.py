# Q1. Write a program to choose three values from user and do one of the following options:
"""
A) If press 1, do sum of the values.
B) If press 2, do average of the three values
C) If press 3, find out the largest of the three.
D) Otherwise, find out the minimum of the three.
"""

"""
Display after entering the numbers, user can read the choices and press number
"""

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

print("\nChoose an option:")
print("1. Sum of the values")
print("2. Average of the values")
print("3. Largest of the values")
print("4. Smallest of the values")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("The sum is:", a + b + c)
elif choice == 2:
    print("The average is:", (a + b + c) / 3)
elif choice == 3:
    print("The largest number is:", max(a, b, c))
else:
    print("The smallest number is:", min(a, b, c))