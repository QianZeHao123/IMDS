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
max_abs_eigenvalue_index = np.argmax(np.abs(eigenvalues))
initial_eigenvector = eigenvectors[:, max_abs_eigenvalue_index]

# Normalize the eigenvector to have a norm of 10
initial_state = 10 * (initial_eigenvector /
                      np.linalg.norm(initial_eigenvector))

# Print the results
print("Initial state vector with norm 10:", initial_state)


# import numpy as np
# import matplotlib.pyplot as plt

# # Given matrix A
# A = np.array([
#     [1.03552632, 0.01842105, -0.16447368],
#     [-0.00921053, 1.10263158, -0.00921053],
#     [-0.13815789, 0.03947368, 1.06184211]
# ])

# # Calculate eigenvectors and eigenvalues
# eigenvalues, eigenvectors = np.linalg.eig(A)

# # Find eigenvector corresponding to the eigenvalue with the maximum absolute value
# max_abs_eigenvalue_index = np.argmax(np.abs(eigenvalues))
# initial_eigenvector = eigenvectors[:, max_abs_eigenvalue_index]

# # Normalize the eigenvector to have a norm of 10
# initial_state = 10 * (initial_eigenvector / np.linalg.norm(initial_eigenvector))

# # Initialize lists to store norms and iterations
# norms = []
# iterations = range(50)  # You can adjust the number of iterations

# # Calculate norms for each iteration
# for i in iterations:
#     current_state = np.linalg.matrix_power(A, i) @ initial_state
#     norm_i = np.linalg.norm(current_state)
#     norms.append(norm_i)

# # Plotting
# plt.plot(iterations, norms, marker='o')
# plt.title('Norm of (xi, yi, zi) over Iterations')
# plt.xlabel('Iterations')
# plt.ylabel('Norm')
# plt.grid(True)
# plt.show()
