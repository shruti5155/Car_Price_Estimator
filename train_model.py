import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# Load the data
df = pd.read_csv("Cleaned_Car.csv")

# Features and target
X = df[['name', 'company', 'year', 'kms_driven', 'fuel_type']]
y = df['Price']

# Define column transformer for encoding categorical data
ohe = ColumnTransformer([
    ('encoder', OneHotEncoder(handle_unknown='ignore'), ['name', 'company', 'fuel_type'])
], remainder='passthrough')

# Create pipeline
model = Pipeline(steps=[
    ('preprocessor', ohe),
    ('regressor', LinearRegression())
])

# Fit the model
model.fit(X, y)

# Save the model
with open("LinearRegressionModel.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as LinearRegressionModel.pkl")
