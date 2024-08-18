from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('your_data.csv')

# Define your features and target
X = data[['pothole_area']]
y = data['tar_bags']

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Create directory if it doesn't exist
os.makedirs('./models', exist_ok=True)

# Save the model
joblib.dump(model, './models/linear_regression_model.pkl')
