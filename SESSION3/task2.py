# Task: Write an if/elif that assigns a value to the variable bonus depending on the
# amount of sales. Assume the amount of the sales is stored in a variable called sales

# Assume input to enter sales number and receive additional bonus.

"""
Flowchart:

Sales | Bonus
>=100,000 | 10,000
>= 75,000 | 5,000
>= 50,000 | 2,500
>= 25,000 | 1,000
"""

input_sales = int(input("Enter your sales amount: "))

bonus = 0
if input_sales >= 100000:
    bonus = 10000
elif input_sales >= 75000:
    bonus = 5000
elif input_sales >= 50000:
    bonus = 2500
elif input_sales >= 25000:
    bonus = 1000

print(f"Your bonus is: ${bonus}")