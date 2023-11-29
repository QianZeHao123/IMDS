import numpy as np

# Given eigenvalues
lambda_1 = 3
lambda_2 = 4
lambda_3 = 5

# Given eigenvectors
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 2])
v3 = np.array([0, 1, 10])

# Construct the matrix A
A = np.column_stack((v1, v2, v3))

# Display the matrix A
print("Matrix A:")
print(A)

# Check if A has the correct eigenvalues and eigenvectors
for i in range(3):
    result = np.dot(A, A[:, i])
    print(f"Eigenvalue {i+1}:", result)
