# Question 1

"""
You have been given a code which is running without any error
but contains a logical error. Your task is to find the logical error.
"""

"""
The code for this program and problem statement is given below:

Problem Statement:

calculate the pvfactor = 1 / (1 + r) ^ n and pv=fv* pvfactor.
You need to receive input from the user for parameter fv, r and n.
"""

"""
The code with the logical error is given below:

fv = input("Enter the amount to be received in the future: ")
r = input("Enter the rate of return (e.g. 0.05 for 5 percent): ")
n = input("Enter the number of years: ")
# calculate the pvfactor = 1 / (1+r)^n
pvfactor = 1 / (1+r) * n
# calcualte the pv = fv * pvfactor
pv = fv * pvfactor
# output the present value
print ("That's worth $", pv, "today.")
"""

"""
Sample Input:
Enter the amount to be received in the future: 100
Enter the rate of return (e.g. 0.05 for 5 percent): 0.05
Enter the number of years: 10

Incorrect:
	That's worth $ 952.380952381 today.
Correct:
	That's worth $ 61.3913253541 today.
"""

# Corrected Code:
fv = float(input("Enter the amount to be received in the future: "))
r = float(input("Enter the rate of return (e.g. 0.05 for 5 percent): "))
n = int(input("Enter the number of years: "))
# calculate the pvfactor = 1 / (1+r)^n
pvfactor = 1 / (1+r) ** n
# calculate the pv = fv * pvfactor
pv = fv * pvfactor
# output the present value
# Round it about 10 decimal places
pv = round(pv, 10)
print ("That's worth $", pv, "today.")

"""
In addition with that do the following task:

a) Print fv, r and n in the following format: fv = 100, r = 0.05, n = 10
b) Display the pvfactor like pvfactor = 0.613913253541
"""
print(f"fv = {fv}, r = {r}, n = {n}")
print(f"pvfactor = {pvfactor}")