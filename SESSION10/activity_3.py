# Write a program to check whether the weather is hot or not.
# If it's less than 30, then it's not hot.
# If it's 30 or more than 30, then it's hot.

# Note: Celsius temperature is used in this program.

temp=int(input('Enter the temperature: '))
if (temp>=30):
    print("The weather is hot")
elif (temp <30):
    print("The weather is not hot")
else:
    print("This code will never run") 