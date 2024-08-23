from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Features and target
X = df[['region_risk', 'vehicle_risk', 'age']]
y = df['insurance_value']

# Split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model initialization
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Training the model
model.fit(X_train, y_train)

# Validation
y_pred = model.predict(X_test)
print(f"Validation MSE: {mean_squared_error(y_test, y_pred)}")
