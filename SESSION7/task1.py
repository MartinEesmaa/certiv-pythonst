# Task 1

"""
You are working in the HR department of a factory and they have asked you
to create a program to calculate gross pay of the workers based
on hours worked and hourly rate of pay. 

Your program will take “Hours” and “Rate” as inputs and display the gross pay as output. 
Take into consideration that workers are paid 1.5 times the hourly rate
for the hours worked above 40 hours. 

Write the program by using a function named salarycalculator
that takes hours and rate as input and returns payment as output. 

Sample Executions:

Enter Hours: 30     Enter Hours: 45
Enter Rate: 10      Enter Rate: 10
Pay: $300.0         Pay: $475.0
"""

def salarycalculator(hours, rate):
    if hours <= 40:
        payment = hours * rate
    else:
        payment = (40 * rate) + ((hours - 40) * rate * 1.5)
    return payment
hours = int(input("How many hours did you work last week? "))
rate = 10
pay = salarycalculator(hours, rate)
print("Paycheck received: $", pay)