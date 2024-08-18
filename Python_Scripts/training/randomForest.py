from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('your_data.csv')

# Define your features and target
X = data[['pothole_area']]
y = data['tar_bags']

# Initialize and fit the model
model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# Save the model
joblib.dump(model, './models/random_forest_regressor_model.pkl')
