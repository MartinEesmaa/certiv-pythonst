# Example: Matrix Addition

# Program to add two matrices using nested loop

X = [[12, 7], [4, 5], [7, 8]]
Y = [[5, 8], [6, 4], [3, 2]]
result = [[0, 0], [0, 0], [0, 0]]

# Iterate through rows and columns
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

print("Sum of two matrices:")
for r in result:
    print(r)