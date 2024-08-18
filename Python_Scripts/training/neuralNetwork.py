from sklearn.neural_network import MLPRegressor
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('C:/Users/mgshe/Documents/altF4_patch_perfect_hackathon/CSV_Files/combined.csv')

# Define your features and target
X = data.iloc[:,[4]]
y = data.iloc[:,3]
# Initialize and fit the model
model = MLPRegressor(hidden_layer_sizes=(100, 100), max_iter=500)
model.fit(X, y)

# Save the model
joblib.dump(model, './models/neural_network_model.pkl')
