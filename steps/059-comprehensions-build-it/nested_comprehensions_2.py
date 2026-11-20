# Filter in nested comprehension: keeps only even numbers
even_flat = [item for row in matrix for item in row if item % 2 == 0]
print(even_flat)  # [2, 4, 6, 8]

# Transpose a matrix: inner comprehension builds each row
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
