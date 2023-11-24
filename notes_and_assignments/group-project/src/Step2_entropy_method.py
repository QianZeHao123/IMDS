import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Read the CSV file
df = pd.read_csv('./Data/2023_24.csv')
# Extract attribute columns

# Select the columns to be processed
selected_columns = ['MP', 'Win', 'Draw', 'GF', 'GD', 'Points']
# Extract data from the selected columns
selected_data = df[selected_columns]

# Use Min-Max scaling to standardize each column's data
scaler = MinMaxScaler()
df[selected_columns] = scaler.fit_transform(df[selected_columns])
print(df)

# Calculate the information entropy for each attribute
entropies = []
for column in selected_columns:
    values = df[column]
    p = values / values.sum()
    entropy = -np.sum(p * np.log2(p))
    entropies.append(entropy)

# Calculate the weights for each attribute
weights = [1 - entropy / np.sum(entropies) for entropy in entropies]
# Normalize the weights
normalized_weights = [weight / sum(weights) for weight in weights]

# Print the weights
print("Attribute Weights:")
for column, weight in zip(selected_columns, normalized_weights):
    print(f"{column}: {weight}")

# Multiply each column in the selected data by its normalized weight
weighted_df = df[selected_columns] * normalized_weights

# Calculate the weighted sum for each row
weighted_sum = weighted_df.sum(axis=1)

# Print the result
# print("Weighted Sum:")
# print(weighted_sum)

result_df = pd.DataFrame({'Team': df['Team'], 'Weighted Sum': weighted_sum})
print(result_df)
