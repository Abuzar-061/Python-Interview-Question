import numpy as np

# Define Matrix A
A = np.array([[1, 2, 3], [4, 5, 6]])

# Define Matrix B
B = np.array([[3, 2], [4, 2], [5, 4]])

# Calculate the product of Matrix A and Matrix B
C = A @ B  # This is equivalent to np.dot(A, B) or A.dot(B)

# Print the result
print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Product of Matrix A and Matrix B (Matrix C):")
print(C)
