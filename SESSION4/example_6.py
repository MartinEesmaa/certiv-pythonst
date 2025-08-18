# Logic and bit operations in Python

a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
c = 0

# Bitwise AND operation
c = a & b # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

# Bitwise OR operation
c = a | b # 61 = 0011 1101
print("Line 2 - Value of c is ", c)

# Bitwise XOR operation
c = a ^ b # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

# Bitwise left shift
c = a << 2; # 240 = 1111 0000
print("Line 4 - Value of c is ", c)

# Bitwise right shift
c = a >> 2; # 15 = 0000 1111
print("Line 5 - Value of c is ", c)