# Question 3

"""
Write a code to sort the numbers using bubble sort algorithm.
Sample input: 2 5 5 3
Sample output: 2 3 5 5
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Sample input
input_numbers = [2, 5, 5, 3]
# Sorting the numbers
sorted_numbers = bubble_sort(input_numbers)
# Sample output
print("Sorted output:", *sorted_numbers)

"""
After solving the problem, the following tasks for technical documentation:

a) Write short description about bubble sort algorithm.
b) Create one or more logical errors. Explain what I need to do
if this happens. For example, change > to < or vice versa.
c) Create at least three syntax errors and explain all of those with solutions.
"""

# a) Bubble Sort Algorithm Description:
"""
Bubble sort is number sorting from lowest to highest or vice versa numbers.
"""
# b) Logical Error Example:
"""
In the bubble sort implementation, we can make mistake
if we change the comparison operator from '>' to '<' and other results.
"""
# c) Syntax Error Example:
"""
input_numbers = 2, 5, 5, 3  # Missing brackets

Missing colon of input numbers:
sort
    arr[j], arr[j+1] = arr[j+1], arr[j]
    ~~~^^^
TypeError: 'tuple' object does not support item assignment
"""