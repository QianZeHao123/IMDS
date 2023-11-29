# import numpy as np

# # Define the given vectors
# a = np.array([7, 1, 2])
# b = np.array([8, 1, 4])
# c = np.array([-1, 0, 2])

# # Define the target matrices
# fa_target = np.array([1, 0, 0, 0])
# fb_target = np.array([0, 1, 0, 0])
# fc_target = np.array([0, 0, 0, 0])

# # Form the matrix equation [f] * [a, b, c] = [fa_target, fb_target, fc_target]
# A = np.column_stack((a, b, c))
# B_target = np.column_stack((fa_target, fb_target, fc_target))

# # Solve for the matrix [f]
# f_matrix, residuals, rank, s = np.linalg.lstsq(A, B_target, rcond=None)

# print("Matrix [f]:")
# print(f_matrix)



import numpy as np

# Define the given vectors
a = np.array([7, 1, 2])
b = np.array([8, 1, 4])
c = np.array([-1, 0, 2])

# Define the target matrices
fa_target = np.array([1, 0, 0, 0])
fb_target = np.array([1, -1, 0, 0])
fc_target = np.array([0, 1, 0, 0])

# Form the matrix equation [f] * [a, b, c] = [fa_target, fb_target, fc_target]
A = np.vstack((a, b, c)).T  # Transpose to make it 3x3
B_target = np.vstack((fa_target, fb_target, fc_target)).T  # Transpose to make it 3x4

# Solve for the matrix [f]
try:
    f_matrix, residuals, rank, s = np.linalg.lstsq(A, B_target, rcond=None)
    print("Matrix [f]:")
    print(f_matrix)
except np.linalg.LinAlgError:
    print("No solution exists for the given conditions.")
