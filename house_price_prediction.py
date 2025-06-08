
# house_price_prediction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a synthetic dataset
data = {
    'bedrooms': [2, 3, 4, 3, 5, 4, 3, 2, 5, 4],
    'square_feet': [1000, 1500, 2000, 1700, 2500, 2100, 1600, 1200, 2700, 2300],
    'price': [150000, 200000, 250000, 220000, 300000, 260000, 210000, 170000, 320000, 280000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['bedrooms', 'square_feet']]
y = df['price']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R² Score:", r2)
