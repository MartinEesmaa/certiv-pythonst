# Task 2

"""
Write a python program that will sort the words in alphabetic order using for loop.
Code constructors: for loop, Python strings, string methods
"""

fruitlist = ['banana', 'apple', 'orange', 'mango']
swapFlag=True
while swapFlag:
    swapFlag=False
    for i in range(len(fruitlist)-1):
        if fruitlist[i]>fruitlist[i+1]:
            temp=fruitlist[i]
            fruitlist[i]=fruitlist[i+1]
            fruitlist[i+1]=temp
            swapFlag=True
print("The sorted list is: ", fruitlist)