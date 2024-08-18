from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
import os

# Load your data
data = pd.read_csv('your_data.csv')

# Define your features and target
X = data[['pothole_area']]
y = data['tar_bags']

# Transform features to polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Initialize and fit the model
model = LinearRegression()
model.fit(X_poly, y)

# Save the polynomial features transformer and the model
joblib.dump(poly, './models/polynomial_features.pkl')
joblib.dump(model, './models/polynomial_regression_model.pkl')
