import numpy as np

# Given matrix A
A = np.array([
    [1.03552632, 0.01842105, -0.16447368],
    [-0.00921053, 1.10263158, -0.00921053],
    [-0.13815789, 0.03947368, 1.06184211]
])

# Initial state (x0, y0, z0)
initial_state = np.array([100, 100, 100])

# Calculate the next states (x1, y1, z1) and (x2, y2, z2)
state_1 = np.dot(A, initial_state)
state_2 = np.dot(A, state_1)

# Print the results
print("Initial State:", initial_state)
print("Next State (x1, y1, z1):", state_1)
print("Next State (x2, y2, z2):", state_2)
