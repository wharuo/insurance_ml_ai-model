#This includes cleaning, feature engineering, and normalization.

# Handling missing data
df.fillna(method='ffill', inplace=True)

# Removing outliers
df = df[df['value'] < df['value'].quantile(0.99)]

# Creating a risk score based on region and type of car
def calculate_region_risk(region):
    # Example logic (replace with actual logic)
    region_risk_mapping = {'Urban': 0.8, 'Suburban': 0.5, 'Rural': 0.2}
    return region_risk_mapping.get(region, 0.5)

def calculate_vehicle_risk(car_type):
    # Example logic (replace with actual logic)
    vehicle_risk_mapping = {'Sedan': 0.3, 'SUV': 0.6, 'Truck': 0.8, 'Motorcycle': 1.0}
    return vehicle_risk_mapping.get(car_type, 0.5)

df['region_risk'] = df['region'].apply(calculate_region_risk)
df['vehicle_risk'] = df['car_type'].apply(calculate_vehicle_risk)

# Normalizing the data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['region_risk', 'vehicle_risk', 'age']] = scaler.fit_transform(df[['region_risk', 'vehicle_risk', 'age']])
