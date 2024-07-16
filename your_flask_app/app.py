from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

# Define your Codestral API key
API_KEY = "ZpW38nTHQXgO5OK2v02PE9uG0GEu7yVR"

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint for handling chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']

    # Make request to Codestral chat endpoint
    url = "https://codestral.mistral.ai/v1/fim/completions"                  #"https://codestral.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # Corrected to use API_KEY variable
    }
    data = {
        "message": message
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        chatbot_response = response.json().get('response', 'No response received from chatbot')
    except requests.exceptions.RequestException as e:
        chatbot_response = f"Error: {e}"
    
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
