# Question 6: Matrix Addition

"""
Q17: Write a Python program to perform matrix addition 
on the following 3x3 matrices:
matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

The result should be a new matrix where each element is the sum of the
corresponding elements in matrix_1 and matrix_2.
"""

# Define the matrices
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

# Initialize result matrix with zeros
result = [[0 for _ in range(3)] for _ in range(3)]

# Perform matrix addition
for i in range(3):
    for j in range(3):
        result[i][j] = matrix_1[i][j] + matrix_2[i][j]

# Display the result
print("Resultant Matrix after Addition:")
for row in result:
    print(row)