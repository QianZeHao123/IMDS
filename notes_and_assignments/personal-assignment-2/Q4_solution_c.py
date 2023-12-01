import numpy as np

# Given matrix A
A = np.array([
    [1.03552632, 0.01842105, -0.16447368],
    [-0.00921053, 1.10263158, -0.00921053],
    [-0.13815789, 0.03947368, 1.06184211]
])

# Calculate eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find eigenvector corresponding to the eigenvalue with the maximum absolute value
min_abs_eigenvalue_index = np.argmin(np.abs(eigenvalues))
initial_eigenvector = eigenvectors[:, min_abs_eigenvalue_index]

# Normalize the eigenvector to have a norm of 10
initial_state = 10 * (initial_eigenvector /
                      np.linalg.norm(initial_eigenvector))

# Print the results
print("Initial state vector with norm 10:", initial_state)
