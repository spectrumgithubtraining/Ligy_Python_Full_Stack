# Sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Find the transpose of the matrix
transposed_matrix = []

# Iterate through columns
for i in range(len(matrix[0])):
    transposed_row = []
    # Iterate through rows
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)

# Print the original and transposed matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
