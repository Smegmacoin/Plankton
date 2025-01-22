from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS for handling cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return "Plankton Karaoke Backend is running!"

@app.route("/sing", methods=["POST"])
def sing():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Placeholder for TTS logic
    # In the future, generate audio for Plankton's voice
    return jsonify({"message": f"Plankton is singing: {text}"})

if __name__ == "__main__":
    app.run(debug=True)
