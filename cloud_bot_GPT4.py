import openai

openai.api_key = 'your-openai-api-key'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question')

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Using the latest insurance data and AI trends from Stat {question}",
        max_tokens=150
    )

    answer = response.choices[0].text.strip()

    return jsonify({"answer": answer})
