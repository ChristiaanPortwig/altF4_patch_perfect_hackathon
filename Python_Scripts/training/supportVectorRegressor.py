from sklearn.svm import SVR
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('your_data.csv')

# Define your features and target
X = data[['pothole_area']]
y = data['tar_bags']

# Initialize and fit the model
model = SVR(kernel='rbf')
model.fit(X, y)

# Save the model
joblib.dump(model, './models/svr_model.pkl')
