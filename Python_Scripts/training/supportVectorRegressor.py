from sklearn.svm import SVR
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('CSV_Files/combined.csv')

# Define your features and target
X = data.iloc[:,[4]]
y = data.iloc[:,3]

# Initialize and fit the model
model = SVR(kernel='rbf')
model.fit(X, y)

# Save the model
joblib.dump(model, './models/svr_model.pkl')
