import numpy as np

# Given eigenvalues
lambda_1 = 3
lambda_2 = 4
lambda_3 = 5

# Given eigenvectors
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 2])
v3 = np.array([0, 1, 0])

# Construct the matrix A
P = np.column_stack((v1, v2, v3))
lambda_matrix = np.array(
    [[lambda_1, 0, 0], 
     [0, lambda_2, 0], 
     [0, 0, lambda_3]])

# Compute the matrix A with P * lambda * P^{-1}
A = P@lambda_matrix@np.linalg.inv(P)
print(A)