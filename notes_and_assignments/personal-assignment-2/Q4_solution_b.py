# import numpy as np

# # Given matrix A
# A = np.array([
#     [1.03552632, 0.01842105, -0.16447368],
#     [-0.00921053, 1.10263158, -0.00921053],
#     [-0.13815789, 0.03947368, 1.06184211]
# ])

# # Calculate eigenvectors and eigenvalues
# eigenvalues, eigenvectors = np.linalg.eig(A)

# # Given initial state vector
# x0 = np.array([100, 100, 100])

# # Solve for coefficients c1, c2, c3
# coefficients = np.linalg.solve(eigenvectors, x0)

# # Print the results
# print("Eigenvectors:")
# print(eigenvectors)
# print("Eigenvalues:")
# print(eigenvalues)
# print("Initial state vector as a linear combination of eigenvectors:")
# print(
#     f"x0 = {coefficients[0]:.2f} * v1 + {coefficients[1]:.2f} * v2 + {coefficients[2]:.2f} * v3")


import numpy as np
x, y, z = 100, 100, 100
# Given matrix A
A = np.array([
    [1.03552632, 0.01842105, -0.16447368],
    [-0.00921053, 1.10263158, -0.00921053],
    [-0.13815789, 0.03947368, 1.06184211]
])

# Calculate eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)

# Given vector (x, y, z)
v = np.array([x, y, z])

# Solve for coefficients c1, c2, c3
coefficients = np.linalg.solve(eigenvectors.T, v)

# Print the coefficients
print("Coefficients (c1, c2, c3):", coefficients)
