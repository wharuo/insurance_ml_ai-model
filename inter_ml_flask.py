from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('insurance_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Assuming data contains the required fields for prediction
    features = [data['car_type'], data['age'], data['insurance_company']]

    # Convert features to a DataFrame or numpy array matching the model input
    prediction = model.predict([features])

    return jsonify({"insurance_value": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
