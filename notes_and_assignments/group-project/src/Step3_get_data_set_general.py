# -------------------------------------------------------------------------
import os
import pandas as pd
from extractFeatures import extract_features
# -------------------------------------------------------------------------
# Folder path containing all CSV files
folder_path = "./Data"

# Target team
target_team = "Everton FC"
target_teams = ['Manchester City FC', 'Liverpool FC', 'Arsenal FC',
                'Tottenham Hotspur FC', 'Aston Villa FC',
                'Manchester United FC', 'Newcastle United FC',
                'Brighton & Hove Albion FC', 'West Ham United FC',
                'Chelsea FC', 'Brentford FC', 'Crystal Palace FC',
                'Wolverhampton Wanderers FC', 'Nottingham Forest FC',
                'Fulham FC', 'AFC Bournemouth', 'Luton Town FC',
                'Sheffield United FC', 'Everton FC', 'Burnley FC']
# List of all CSV file names
csv_files = [
    '2007_08.csv', '2008_09.csv', '2009_10.csv', '2010_11.csv',
    '2011_12.csv', '2012_13.csv', '2013_14.csv', '2014_15.csv',
    '2015_16.csv', '2016_17.csv', '2017_18.csv', '2018_19.csv',
    '2019_20.csv', '2020_21.csv', '2021_22.csv', '2022_23.csv'
]
# -------------------------------------------------------------------------


def get_result_df(target_team):
    # Create an empty DataFrame to store the extracted data
    result_df = pd.DataFrame(
        columns=["File", "Team", "MP", "Win",
                 "Draw", "Loss", "GF", "GA",
                 "GD", "Points"]
    )
    # Loop through each CSV file
    for csv_file in csv_files:
        # Build the full path of the CSV file
        file_path = os.path.join(folder_path, csv_file)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Extract data for the target team
        team_data = df[df["Team"] == target_team]

        # If data for the target team is found, add it to the result DataFrame
        if not team_data.empty:
            # Use pd.concat to add the target team's data from the current file to the result DataFrame,
            # and add the file name column
            result_df = pd.concat(
                [result_df, team_data.assign(File=csv_file)], ignore_index=True)

    return result_df

# print(result_df)
# result_df.to_csv("output.csv", index=False)
# -------------------------------------------------------------------------
selected_columns = ['Win','Draw','Loss','GF','GA','GD','Points']

dfs = []

for target_team in target_teams:
    result_df = get_result_df(target_team)


    features_dict = {}
    for column in selected_columns:
        selected_data = result_df[column]
        features_column = extract_features(selected_data)
        features_dict[column] = features_column

    # Flatten the nested structure and convert to a DataFrame
    flattened_features = {}
    for column, feature_dict in features_dict.items():
        for key, value in feature_dict.items():
            flattened_features[f'{column}_{key}'] = value

    flattened_df = pd.DataFrame([flattened_features])

    # Append the DataFrame to the list
    dfs.append(flattened_df)

# Concatenate all DataFrames into a single DataFrame

result_df = pd.concat(dfs, ignore_index=True)
# -------------------------------------------------------------------------
df_23_24 = pd.read_csv('./Data/2023_24.csv')
result = pd.concat([df_23_24, result_df], axis=1)
# Export the result to a CSV file
result.to_csv("2023_24_General.csv", index=False)