age = 18
int_age = int(age)

print(int_age)

pi = 3.1456

calculate = int (input("Enter a radius:"))
area = pi * (calculate ** 2)
print(area)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(sum_result)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
k = (a-b) / c
print(k)

def calculate_area(radius):
    pi = 3.1456
    return pi * (radius ** 2)

print(calculate_area(5))
print(5 * 2 // 2)
print(5 * (2 // 3))

print("""
Organize everything together
Plug in kettle
Put teabeag in cup
Wait for kettle to boil
Add water to cup
Remove teabag with spoon/fork
Add milk and/or sugar
Serve!
""")