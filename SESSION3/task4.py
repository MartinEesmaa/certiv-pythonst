#Q2
# Write a program to display three integer from user and display the minimum number.

a=int(input("Enter number 1\n"))
b=int(input("Enter number 2\n"))
c=int(input("Enter number 3\n"))
if a<b and a<c:
    print(str(a) +' is the minimum number')
elif b<a and b<c:
    print(str(b)+ ' is the minimum number')
else:
    print(str(c) +' is the minimum number')