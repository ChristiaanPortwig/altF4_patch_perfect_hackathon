from sklearn.neural_network import MLPRegressor
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('../../CSV_Files/combined.csv')

# Define your features and target
X = data[['pothole_area']]
y = data['tar_bags']

# Initialize and fit the model
model = MLPRegressor(hidden_layer_sizes=(100, 100), max_iter=500)
model.fit(X, y)

# Save the model
joblib.dump(model, './models/neural_network_model.pkl')
