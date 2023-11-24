import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Read the CSV file
# df = pd.read_csv('./Data/2007_08.csv')
# Load all datasets

start_year = 2007
end_year = 2021

datasets = []
Years = [
    f'{year}_{str(year+1)[-2:]}' for year in range(start_year, end_year + 1)]
for year in Years:
    filename = csv_file_path = './' + 'Data/' + year + '.csv'
    dataset = pd.read_csv(filename)
    datasets.append(dataset)

df = pd.concat(datasets, ignore_index=True)


# Select relevant columns for prediction
features = ['MP', 'Win', 'Draw', 'GF', 'GD']
target = 'Points'

# Extract data for selected features and target
X = df[features].values.astype(float)
y = df[target].values.astype(float).reshape(-1, 1)

# Use Min-Max scaling to standardize each column's data
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42)

# Convert data to PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

# Define a simple neural network model


class RegressionModel(nn.Module):
    def __init__(self, input_size):
        super(RegressionModel, self).__init__()
        self.fc = nn.Linear(input_size, 1)

    def forward(self, x):
        return self.fc(x)


# Instantiate the model
input_size = X_train.shape[1]
model = RegressionModel(input_size)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training the model
num_epochs = 1000

for epoch in range(num_epochs):
    model.train()

    # Forward pass
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Evaluate the model on the test set
model.eval()
with torch.no_grad():
    test_outputs = model(X_test_tensor)
    mse = criterion(test_outputs, y_test_tensor)
    print(f'Mean Squared Error on Test Set: {mse.item():.4f}')


# Make predictions on new data
# new_data_tensor = torch.tensor(scaler_X.transform(
#     [[some_values]]), dtype=torch.float32)
# predicted_scaled = model(new_data_tensor)
# predicted_points = scaler_y.inverse_transform(predicted_scaled.numpy())
# print(f'Predicted Points: {predicted_points[0][0]}')
