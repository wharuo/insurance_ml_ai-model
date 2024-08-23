from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def calculate_fake_insurance_value(region, car_type, age):
    # This is a simple mock function that returns a fake insurance value based on the input.
    base_value = 500
    region_factor = {"Urban": 1.2, "Suburban": 1.0, "Rural": 0.8}.get(region, 1.0)
    car_factor = {"Sedan": 1.0, "SUV": 1.2, "Truck": 1.3, "Motorcycle": 1.5}.get(car_type, 1.0)
    age_factor = 1 + (age - 30) * 0.05 if age > 30 else 1 - (30 - age) * 0.05

    # Calculate the fake insurance value
    insurance_value = base_value * region_factor * car_factor * age_factor
    # Adding some randomness to simulate real-world unpredictability
    insurance_value += random.uniform(-50, 50)

    return round(insurance_value, 2)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Get the input data
    region = data.get('region')
    car_type = data.get('car_type')
    age = data.get('age')

    # Generate a fake insurance value
    insurance_value = calculate_fake_insurance_value(region, car_type, age)
    
    # Return the result as a JSON response
    return jsonify({"insurance_value": insurance_value})

if __name__ == '__main__':
    app.run(debug=True)
