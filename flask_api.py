from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dummy data for chatbot responses
chatbot_responses = {
    "What is cloud computing?": "Cloud computing is the delivery of computing services over the internet.",
    "What is AI?": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines."
}

def calculate_fake_insurance_value(car_type, age, insurance_company):
    # Basic example to vary the insurance value based on input
    base_value = 500
    car_factor = {"Sedan": 1.0, "SUV": 1.2, "Truck": 1.3, "Motorcycle": 1.5}.get(car_type, 1.0)
    age_factor = 1 + (age - 30) * 0.05 if age > 30 else 1 - (30 - age) * 0.05
    company_factor = random.uniform(0.8, 1.2)  # Simulate variability between companies

    insurance_value = base_value * car_factor * age_factor * company_factor
    return round(insurance_value, 2)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    car_type = data.get('car_type')
    age = data.get('age')
    insurance_company = data.get('insurance_company')

    insurance_value = calculate_fake_insurance_value(car_type, age, insurance_company)

    return jsonify({"insurance_value": insurance_value})

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question')

    # Return a response based on predefined data
    answer = chatbot_responses.get(question, "I don't know the answer to that. Try asking something else.")

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
