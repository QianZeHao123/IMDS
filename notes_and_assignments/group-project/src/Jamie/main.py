import numpy as np
import pandas as pd

data = pd.read_csv("Premier_League_Winner_Stats.csv")


def gradient_ascend(v, fv, v_norm, fv_norm, w, b, a, n):
    for i in range(n):
        # Calculate predictions
        fv_pred = np.dot(v_norm, w) + b

        # Calculate errors
        error = fv_norm - fv_pred

        # Calculate gradients
        w_grad = np.dot(v_norm.T, error)
        b_grad = np.sum(error)

        # Update weights and bias
        w += a * w_grad
        b += a * b_grad

        w_denormalized = w * v.std(axis=0) / v_norm.std(axis=0)
        b_denormalized = b * fv.std() + fv.mean()

    return w_denormalized, b_denormalized


# Historical DAta
v = data[['Games Won', 'Games Drawn', 'Games Lost',
          'Goal Difference (Goals Scored - Goals Conceded)', 'Final Points']]
fv = data['Final Points']


v = v.to_numpy()
fv = fv.to_numpy()

v_normalized = (v - v.mean(axis=0)) / v.std(axis=0)
fv_normalized = (fv - fv.mean()) / fv.std()

# Initial weights and bias
w = np.zeros(shape=(5,))
b = 0


# Learning rate
a = 0.00001

# Number of iterations
n = 100

# Calculate updated weights and bias
w_updated, b_updated = gradient_ascend(
    v, fv, v_normalized, fv_normalized, w, b, a, n)

print("Updated weights:", w_updated)
print("Updated bias:", b_updated)

vects = np.array([10, 5, 2, 18, 35])

pred_points = np.dot(vects, w_updated) + b_updated
print(pred_points)
