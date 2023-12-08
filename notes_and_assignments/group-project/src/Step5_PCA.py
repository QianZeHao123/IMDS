# Import the pandas library
import pandas as pd
from sklearn.decomposition import PCA


# Read the CSV file
# Replace '2023_24_Processed.csv' with the actual file name and path
df = pd.read_csv('./Results/2023_24_Processed.csv')


select_col = ['Win', 'GD', 'GF', 'GF_max_value', 'GD_max_value', 'Points_rms',
              'GF_mean', 'Points_mean', 'GF_rms', 'Win_rms', 'GF_median', 'Points_max_value',
              'GD_mean', 'Win_max_value', 'GF_power_spectral_density', 'GF_total_power',
              'Win_mean', 'GF_max_frequency_magnitude', 'Points_power_spectral_density',
              'Points_max_frequency_magnitude', 'Points_total_power', 'Win_total_power',
              'Win_power_spectral_density', 'Points_median', 'GF_min_value', 'GF_std_dev',
              'Draw_centroid_frequency', 'Loss', 'GA', 'Loss_min_value', 'Loss_mean',
              'Loss_rms', 'Loss_median', 'Loss_max_value']


selected_columns = df[select_col]
selected_columns.to_csv('./Results/2023_24_Processed_PCA.csv', index=False)

pca = PCA()
pca_result = pca.fit_transform(selected_columns)

pca_df = pd.DataFrame(data=pca_result, columns=[
                      f'PC{i+1}' for i in range(pca_result.shape[1])])
# result_df = pd.concat([selected_columns.reset_index(drop=True), pca_df], axis=1)

# result_df.to_csv('./pca_result.csv', index=False)
pca_df.to_csv('./Results/pca_result.csv', index=False)
