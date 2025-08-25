# Some List Operations

odd = [2, 4, 6, 8]
# change the 1stitem
odd[0] = 1
# Output: [1, 4, 6, 8]
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9,11,13])
print(odd)
odd.insert(0,8)
print(odd)
odd.sort()
print(odd)
odd.reverse()
print(odd)