import pandas as pd

# Load your dataset from Stat
# Assuming you have exported the data to a CSV or Excel file
data = pd.read_csv('path.csv')

# Inspect the data
print(data.head())

# Preprocess the data (cleaning, feature engineering, etc.)
# Example: Handling missing data
data.fillna(method='ffill', inplace=True)

# Example: Encoding categorical variables
data = pd.get_dummies(data, drop_first=True)

# Example: Splitting the data into features (X) and target (y)
X = data.drop('target_column', axis=1)
y = data['target_column']
