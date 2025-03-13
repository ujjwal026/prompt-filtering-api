from flask import Flask, request, jsonify
from filter_logic import is_safe_prompt
import requests

app = Flask(__name__)



load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route("/ask", methods=["POST"])
def ask_gemini():
    """Handles user queries by filtering unsafe prompts before sending to Gemini."""
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Check if the prompt is safe
    if not is_safe_prompt(prompt):
        return jsonify({"error": "Blocked due to security concerns"}), 403

    # If safe, forward the request to Gemini
    try:
        response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=10
        )

        # Parse the response from Gemini
        result = response.json()
        candidates = result.get("candidates", [])
        if candidates and "content" in candidates[0]:
            ai_response = candidates[0]["content"].strip()
        else:
            ai_response = "I am unable to provide a response."

        return jsonify({"response": ai_response})

    except Exception as e:
        return jsonify({"error": f"Error communicating with Gemini: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
