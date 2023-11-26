import numpy as np

# Define the Matrix A
A = np.array([
    [5, 2, 3],
    [-2, 3, 1],
    [0, 2, 2],
    [1, 0, 1]
])
# AB matrix
AB = np.array([
    [8, 6],
    [-1, 9],
    [2, 6],
    [2, 0]
])
# Solve the system of equations
B = np.linalg.lstsq(A, AB, rcond=None)[0]
print("Solution for B:")
print(B)
