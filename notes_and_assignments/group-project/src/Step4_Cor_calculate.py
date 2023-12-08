# Import the pandas library
import pandas as pd

# Read the CSV file
# Replace '2023_24_Processed.csv' with the actual file name and path
df = pd.read_csv('./Results/2023_24_Processed.csv')

# Define the target column for Spearman correlation
target_column = 'Points'

# Calculate Spearman correlation between the target column and all other columns
correlation_result = df.corrwith(df[target_column], method='spearman')

# Create a DataFrame containing the correlation results
result_df = pd.DataFrame({
    'Positive Correlation': correlation_result[correlation_result > 0].sort_values(ascending=False),
    'Negative Correlation': correlation_result[correlation_result < 0].sort_values(ascending=True)
})

# Print the results
print(result_df)

# Save the results to a CSV file
result_df.to_csv('./Results/Cor_result.csv', index=True)

# Extract the variables with absolute correlation greater than 0.6
positive_correlation_list = correlation_result[(correlation_result > 0) & (correlation_result.abs() > 0.65)].sort_values(ascending=False)
negative_correlation_list = correlation_result[(correlation_result < 0) & (correlation_result.abs() > 0.65)].sort_values(ascending=True)

# Print the lists of variables with absolute correlation greater than 0.6
print(positive_correlation_list)
print(negative_correlation_list)

positive_correlation_list.to_csv('./Results/Positive_Cor_result.csv', index=True)
negative_correlation_list.to_csv('./Results/Negative_Cor_result.csv', index=True)


positive_correlation_variables = list(positive_correlation_list.index)
negative_correlation_variables = list(negative_correlation_list.index)


print(positive_correlation_variables)
print(negative_correlation_variables)